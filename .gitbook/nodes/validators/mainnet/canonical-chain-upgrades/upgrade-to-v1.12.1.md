# upgrade-to-v1.12.1 Upgrade

For the standard upgrade procedure, see the [upgrade template](./UPGRADE_TEMPLATE.md).

## Version-Specific Instructions

### Notes for Validators

You must remove the wasm cache before upgrading to the new version (rm -rf .injectived/wasm/wasm/cache/).

1.  Verify you are currently running the correct version (`b92723b13`) of `injectived`:

    ```bash
       injectived version
       Version dev (b92723b13)
       Compiled at 20240106-0837 using Go go1.19.3 (amd64)
    ```
2.  Make a backup of your `.injectived` directory

    ```bash
    cp ~/.injectived ./injectived-backup
    ```

    3. Download and install the injective-chain `v1.12.1 release`

    ```bash
    wget https://github.com/InjectiveLabs/injective-chain-releases/releases/download/v1.12.1-1705909076/linux-amd64.zip
    unzip linux-amd64.zip
    sudo mv injectived peggo /usr/bin
    sudo mv libwasmvm.x86_64.so /usr/lib
    ```
3.  Verify you are currently running the correct version (`c1a64b7ed`) of `injectived` after downloading the v1.12.1 release:

    ```bash
    injectived version
    Version dev (c1a64b7ed)
    Compiled at 20240122-0743 using Go go1.19.3 (amd64)
    ```
4.  Start injectived

    ```bash
    injectived start
    ```
5.  Verify you are currently running the correct version (`e8089a7`) of `peggo` after downloading the v1.12.0 release:

    ```bash
     peggo version
     Version dev (e8089a7)
     Compiled at 20240122-0743 using Go go1.19.3 (amd64)
    ```
6.  Start peggo

    ```bash
    peggo orchestrator
    ```
