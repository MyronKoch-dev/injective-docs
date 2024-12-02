---
description: Understanding token representation in Injective's multi-VM architecture
---

# Single Token Representation

## What is Single Token Representation (STR)?

Single Token Representation on Injective refers to the unified handling of tokens across both the native chain and the EVM environment. Instead of creating separate token versions for each environment, Injective designates the chain as the single source of truth for token balances across both native and EVM environments, which both EVM and non-EVM transactions reference. Rather than relying on separate bridging or escrow mechanisms, the system proxies all “mint,” “burn,” and “transfer” calls from ERC-20 contracts directly to the [Bank](../../modules/core/bank/) module.

## Why is STR Important?

STR simplifies token interoperability and enhances user experience, ensuring that any token created or managed within Injective’s ecosystem operates with a consistent balance state. This approach minimizes code complexity and automates conversion, allowing tokens to move fluidly between chain and EVM environments without requiring user intervention. Moreover, STR eliminates the need for double-accounting mechanisms, making transactions, faster, more efficient, and more secure.

## Architecture

The system comprises two main components:

* **Bank Precompile**
* **ERC20 Module**

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption><p>Single Token Representation Architecture</p></figcaption></figure>

### Bank Precompile

A precompile is a Go-based smart contract embedded into the EVM at compile time. When the EVM calls a contract, it checks if the contract’s address corresponds to a precompile; if it does, it invokes the associated Go code directly. Externally, and to other EVM contracts, a precompile functions like any regular smart contract, though internally, it has direct access to Cosmos SDK modules and chain state.

The Bank precompile allows smart contracts to interact directly with the `x/bank` module, effectively bringing ERC-20 tokens on-chain. Any ERC-20 contract using the Bank precompile will be represented as `evm/0x...` denom on-chain. Technically, this means that tokens reside only on-chain, with the EVM providing a view to the chain state rather than maintaining a separate copy. Unlike traditional bridging, where two token versions require user actions to switch, the Bank precompile offers real-time, dual-environment reflection for any transfer using either the on-chain bank denom or the ERC-20 `transfer()` method.

A range of ERC-20 implementations backed by the Bank precompile, alongside precompile interfaces and abstract contracts, are available at [Injective’s Solidity Contracts Repository](https://github.com/InjectiveLabs/solidity-contracts). Key contracts include:

* **Bank.sol** – precompile interface
* **BankERC20.sol** – abstract ERC20 implementation backed by the Bank precompile
* **FixedSupplyBankERC20.sol** – decentralized ERC20 with fixed supply (no owner, no minting or burning)
* **MintBurnBankERC20.sol** – ERC20 with an owner authorized to mint and burn tokens

These implementations are based on OpenZeppelin’s ERC20 contracts. Developers can freely create custom ERC20 contracts utilizing the Bank precompile.

#### Bank Precompile Interface

<pre class="language-solidity" data-full-width="false"><code class="lang-solidity"><strong>interface IBankModule {
</strong>    function mint(address,uint256) external payable returns (bool);
    function balanceOf(address,address) external view returns (uint256);
    function burn(address,uint256) external payable returns (bool);
    function transfer(address,address,uint256) external payable returns (bool);
    function totalSupply(address) external view returns (uint256);
    function metadata(address) external view returns (string memory,string memory,uint8);
    function setMetadata(string memory,string memory,uint8) external payable returns (bool);
}
</code></pre>

### ERC20 Module

The ERC20 module enables **existing** bank denoms (e.g., IBC-bridged tokens, USDC, tokenfactory, and Peggy) to integrate with the Injective EVM. It maintains a mapping between token pairs within its storage, creating an association between ERC20 tokens and their corresponding bank denoms. When a new token pair is generated for an existing bank denom, the module deploys an ERC20 contract that interacts with the Bank precompile, which then references the storage mapping to align the ERC20 address with the respective bank denom. This module serves several essential purposes:

1. **Storage**: Maps between bank denom ↔ ERC20 address
2. **New Message Type**: Enables users to establish new token pair mappings by issuing a chain message

#### Creating a New Token Pair

Currently, three types of bank denoms can have associated token pairs, each with specific rules:

* **Tokenfactory (`factory/...`)**\
  Only the denom admin or governance can create a token pair. The sender can specify an existing ERC20 contract address as a custom implementation. If omitted, a new instance of `MintBurnBankERC20.sol` is deployed, with `msg.sender` as the owner, allowing minting and burning through the contract.
* **IBC (`ibc/...`)**\
  IBC denoms can be integrated into the EVM by any user through token pair creation, though without the option for custom ERC20 addresses. These will always deploy a new, ownerless instance of `FixedSupplyBankERC20.sol`.
* **Peggy (`peggy0x...`)**\
  Peggy denoms can be integrated into the EVM by any user through token pair creation, though without the option for custom ERC20 addresses. These will always deploy a new, ownerless instance of `FixedSupplyBankERC20.sol`.

<table data-card-size="large" data-view="cards" data-full-width="false"><thead><tr><th></th><th data-type="content-ref"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>← Previous</td><td><a href="evm-equivalence.md">evm-equivalence.md</a></td><td><a href="evm-equivalence.md">evm-equivalence.md</a></td></tr><tr><td>Return to Homepage ↺</td><td><a href="../../evm-developers.md">evm-developers.md</a></td><td><a href="../../evm-developers.md">evm-developers.md</a></td></tr></tbody></table>
