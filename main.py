""" Tool to kick nominators below a given threshold from the nominator list. """
import argparse
import requests

from substrateinterface import SubstrateInterface


parser = argparse.ArgumentParser(description='Kick nominators.')
parser.add_argument('--min_stake', type=float, nargs='?',
                    help='minimum stake you would like to keep per nominator.')
parser.add_argument('--stash_address', metavar='N', type=str, nargs=1,
                    help='Stash address.')

args = parser.parse_args()

try:
    substrate = SubstrateInterface(
        url="wss://rpc.polkadot.io"
    )
except ConnectionRefusedError:
    print("⚠️ Remote RPC server didn't respond")
    exit()

chain_symbol = substrate.token_symbol
chain_decimals = substrate.token_decimals

print(args.stash_address)
res = requests.get('https://api.polkadot.subvt.io:18900/validator/'+ args.stash_address[0] + '/details')
data = dict(res.json())
# print(data["validator_details"]["nominations"])
print("Found %d nominations" % len(data["validator_details"]["nominations"]))
low_nominators = []
for nominator in data["validator_details"]["nominations"]:
    # print(nominator)
    if nominator["stake"]["total_amount"] < (args.min_stake * 10**chain_decimals):
        low_nominators.append(nominator)
print("Found %d nominations below threshold of %.2f %s" % (len(low_nominators), args.min_stake, chain_symbol))
call = substrate.compose_call(
    call_module='Staking',
    call_function='kick',
    call_params={
        'who': [nominator["stash_account"]["address"] for nominator in low_nominators]
    }
)
print("Copy the following call hash to polkadot.js.org -> Developer Extrinsics -> Decode -> Submit and change to your controller account then submit:")
print(call.encode())