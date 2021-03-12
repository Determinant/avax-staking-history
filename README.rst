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

    rm -rf ~/.avalanchego
    ./build/avalanchego

- When P Chain finishes bootstrap, extract the dumped data:

  ::

    grep 'csv ' ~/.avalanchego/logs/chain/P/*.log | sed 's/.* csv \(.*\)/\1/g' > dumped.csv
