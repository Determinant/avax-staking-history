All Staking History Data in CSVs
--------------------------------
NOTE: these CSVs are comprehensive and also include those staking/delegation
operations whose uptime was not enough to finally redeem the reward.
https://drive.google.com/drive/folders/1rjrx7sp4Y4iDSAI_ZS3Ffduhg9Qk8pp1

How I Generated This Data
-------------------------

This requires basic knowledge in using Linux commandline.

- First clone the avalanchego repo:

  ::

    git clone https://github.com/ava-labs/avalanchego
    cd ./avalanchego

- Get the patch file:

  ::

    curl -sL https://raw.githubusercontent.com/Determinant/avax-staking-history/main/p-dump.patch -o p-dump.patch

- Apply the patch in this repo:

  ::

    patch -p1 < ./p-dump.patch

    # It should output something like:
    # patching file vms/platformvm/proposal_block.go
    # Hunk #1 succeeded at 138 (offset 7 lines).
    # patching file vms/platformvm/reward_validator_tx.go

- Build avalanchego as normal:

  ::

    ./scripts/build.sh

- Start a fresh node (it is required to bootstrap from scratch):

  ::

    rm -rf ./db_tmp ./logs
    ./build/avalanchego --db-dir ./db_tmp --log-dir ./logs | grep 'csv ' | sed 's/.* csv \(.*\)/\1/g' > dumped.csv

- When P Chain finishes bootstrap, the dumped data is in ``dumped.csv``.
