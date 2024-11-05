# Private Testnet Deployment

This guide will walk you through deploying a smart contract on the Injective EVM Testnet network.

{% hint style="info" %}
You can request private EVM testnet funds [here](https://k8s.testnet.evmix.faucet.injective.network/)
{% endhint %}

## Requirements

1. The guide uses [foundry](https://book.getfoundry.sh/) for deployments. Install it by running:

```
curl -L https://foundry.paradigm.xyz | bash
```

To verify the installation:

```
forge --version
```

2. Add Injective EVM to your `foundry.toml`

```
[rpc_endpoints]
injectiveEvm = "https://k8s.testnet.evmix.json-rpc.injective.network"
```

## Deploying

Due to the EVM-equivalence of _Injective_, foundry commands should work as expected. The major difference is the network URL. In most cases, using `--rpc-url injectiveEvm` is sufficient

### Navigate to your smart contract project

```
cd path/to/your/project
```

### Deploying a smart contract <a href="#deploying-a-smart-contract" id="deploying-a-smart-contract"></a>

{% hint style="info" %}
Your private key should have INJ on the Injective network. A transaction will be created which requires a gas fee. You can request private EVM testnet funds [here](https://k8s.testnet.evmix.faucet.injective.network/)
{% endhint %}

<pre class="language-bash"><code class="lang-bash"># Simulating
<strong>forge create src/{YourContract}.sol:{ContractName} --rpc-url injectiveEvm --private-key {YourPrivateKey}
</strong>
# Broadcasting
forge create src/{YourContract}.sol:{ContractName} --rpc-url injectiveEvm --private-key {YourPrivateKey} --broadcast
</code></pre>

### Verifying on Blockscout

After the deployment is completed, you can verify the contract.&#x20;

```bash
forge verify-contract \
  --rpc-url injectiveEvm \
  --verifier blockscout \
  --verifier-url 'https://k8s.testnet.evm.blockscout.api.injective.network/api/' \
  {SmartContractAddress} \
  src/{YourContract}.sol:{ContractName}
```

After that, you can navigate to the contract address in Explorer to see the code, parsed logs, and callable methods ([example](https://k8s.testnet.evm.blockscout.injective.network/address/0x2f9f80b89ef4C9AaBcd630E62B740d6a2f3065E4)).

{% hint style="info" %}
You can read more about foundry deploying [here](https://book.getfoundry.sh/forge/deploying) or you can check [other deployment options\
](https://book.getfoundry.sh/reference/forge/forge-create). You can also read more about [forge verify-contract](https://book.getfoundry.sh/reference/forge/forge-verify-contract).
{% endhint %}