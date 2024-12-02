# canonical-1.13.2 Upgrade

For the standard upgrade procedure, see the [upgrade template](./UPGRADE_TEMPLATE.md).

## Version-Specific Instructions

## Notes for Validators

You must remove the wasm cache before upgrading to the new version (rm -rf .injectived/wasm/wasm/cache/).

1.  Verify you are currently running the correct version (`af924ca9`) of `injectived`:

    ```bash
       injectived version
       Version dev (af924ca9)
       Compiled at 20240728-0905 using Go go1.22.5 (amd64)
    ```
2.  Make a backup of your `.injectived` directory

    ```bash
    cp ~/.injectived ./injectived-backup
    ```

    3. Download and install the injective-chain `v1.13.2 release`

    ```bash
    wget https://github.com/InjectiveLabs/injective-chain-releases/releases/download/v1.13.2-1723753267/linux-amd64.zip
    unzip linux-amd64.zip
    sudo mv injectived peggo /usr/bin
    sudo mv libwasmvm.x86_64.so /usr/lib
    ```
3.  Verify you are currently running the correct version (`6f57bf03`) of `injectived` after downloading the v1.13.2 release:

    ```bash
    injectived version
    Version dev (6f57bf03)
    Compiled at 20240815-2021 using Go go1.22.5 (amd64)
    ```
4.  Start injectived

    ```bash
    injectived start
    ```
5.  Verify you are currently running the correct version (`ead1119`) of `peggo` after downloading the v1.13.2 release:

    ```bash
     peggo version
     Version dev (ead1119)
     Compiled at 20240815-2021 using Go go1.22.5 (amd64)
    ```
6.  Start peggo

    ```bash
    peggo orchestrator
    ```
