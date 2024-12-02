# canonical-1-12 Upgrade

For the standard upgrade procedure, see the [upgrade template](./UPGRADE_TEMPLATE.md).

## Version-Specific Instructions

## Notes for Validators

Validator operators should configure the **timeout_commit** in **config.toml** to `300ms`.

You must remove the wasm cache before upgrading to the new version (rm -rf .injectived/wasm/wasm/cache/).

1.  Verify you are currently running the correct version (`69fb0c5`) of `injectived`:

    ```bash
       injectived version
       Version dev (69fb0c5)
       Compiled at 20230710-1016 using Go go1.19.3 (amd64)
    ```
2.  After the chain has halted, make a backup of your `.injectived` directory

    ```bash
    cp ~/.injectived ./injectived-backup
    ```

    \
    **NOTE**: It is recommended for validators and operators to take a full data snapshot at the export height before proceeding in case the upgrade does not go as planned or if not enough voting power comes online in a sufficient and agreed upon amount of time. In such a case, the chain will fallback to continue operating the Chain. See [Recovery](canonical-1-12.md#recovery) for details on how to proceed.
3.  Download and install the injective-chain `v1.12.0 release`

    ```bash
    wget https://github.com/InjectiveLabs/injective-chain-releases/releases/download/v1.12.0-1704530206/linux-amd64.zip
    unzip linux-amd64.zip
    sudo mv injectived peggo /usr/bin
    sudo mv libwasmvm.x86_64.so /usr/lib
    ```
4.  Verify you are currently running the correct version (`b92723b13`) of `injectived` after downloading the v1.12.0 release:

    ```bash
    injectived version
    Version dev (b92723b13)
    Compiled at 20240106-0837 using Go go1.19.3 (amd64)
    ```
5.  Coordinate to restart your injectived with other validators

    ```bash
    injectived start
    ```

    The binary will perform the upgrade automatically and continue the next consensus round if everything goes well.
6. Verify you are currently running the correct version (`9e702f1`) of `peggo` after downloading the v1.12.0 release:

```bash
  peggo version
  Version dev (9e702f1)
  Compiled at 20240106-0837 using Go go1.19.3 (amd64)
```

8.  Start peggo

    ```bash
    peggo orchestrator
    ```
