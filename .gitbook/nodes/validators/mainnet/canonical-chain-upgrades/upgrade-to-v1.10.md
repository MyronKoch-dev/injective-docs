# upgrade-to-v1.10 Upgrade

For the standard upgrade procedure, see the [upgrade template](./UPGRADE_TEMPLATE.md).

## Version-Specific Instructions

### Notes for Validators

Validator operators should configure the **timeout_commit** in **config.toml** to `300ms`.

1.  Verify you are currently running the correct version (`3c87354f5`) of `injectived`:

    ```bash
    injectived version
    Version v1.9.0 (3c87354f5)
    Compiled at 20230118-1421 using Go go1.18.3 (amd64)
    ```

2.  After the chain has halted, make a backup of your `.injectived` directory

    ```bash
    cp ~/.injectived ./injectived-backup
    ```

    **NOTE**: It is recommended for validators and operators to take a full data snapshot at the export height before proceeding in case the upgrade does not go as planned or if not enough voting power comes online in a sufficient and agreed upon amount of time. In such a case, the chain will fallback to continue operating the Chain. See Recovery for details on how to proceed.

3.  Download and install the injective-chain `10010 release`

    ```bash
    wget https://github.com/InjectiveLabs/injective-chain-releases/releases/tag/v1.10-1678709842
    unzip linux-amd64.zip
    sudo mv injectived peggo /usr/bin
    sudo mv libwasmvm.x86_64.so /usr/lib
    ```

4.  Verify you are currently running the correct version (`e218afcf7`) of `injectived` after downloading the 10009 release:

    ```bash
    injectived version
    Version dev (e218afcf7)                                                                                                                                                                                               │
    Compiled at 20230313-1224 using Go go1.18.3 (amd64)
    ```

5.  Coordinate to restart your injectived with other validators

    ```bash
    injectived start
    ```

    The binary will perform the upgrade automatically and continue the next consensus round if everything goes well.

6.  Verify you are currently running the correct version (`bede2b6`) of `peggo` after downloading the 10009 release:

```bash
 peggo version
 Version dev (bede2b6)                                                                                                                                                                                                 │
 Compiled at 20230313-1224 using Go go1.18.3 (amd64)
```

8.  Start peggo

    ```bash
    peggo start
    ```
