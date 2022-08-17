# polkadot-nomination-kicker

A little tool to kick nominations from oversubscribed validators.
Technically supports any other substrate chain too, just change the RPC endpoint in `main.py`.

## Usage

- Install requirements: `pip3 install -r requirements.txt`
- Run: `python3 main.py --min_stake <min stake in DOT/KSM> --stash_address <validator stash account>`
- Copy the output to https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Frpc.polkadot.io#/extrinsics/decode, change submitter to controller account and sign/execute

## Stake with us!

https://highstake.tech