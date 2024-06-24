import json
from web3 import Web3


# use remix to compile as local solc fails
# ganache-cli => run terminal

def _connect(file: str):
    # Connect to Ganache
    ganache_url = "http://127.0.0.1:7545"
    client = Web3(Web3.HTTPProvider(ganache_url))

    # Check if connected
    if not client.is_connected():
        print("Failed to connect to Ganache")
        exit()

    # Read the compiled contract bytecode and ABI
    with open('../contracts/build/SimpleStorage.bin', 'r') as file:
        bytecode = file.read().strip()

    with open('../contracts/build/SimpleStorage.abi', 'r') as file:
        abi = json.load(file)

    # Create the contract instance
    simple_storage = (client.eth.contract(abi=abi, bytecode=bytecode))

    return client, simple_storage


def main():
    client, contract = _connect('SimpleStorage')

    accounts = client.eth.accounts

    recent_transaction = client.eth.get_transaction_count(accounts[0])
    print(f"recent_transaction: {recent_transaction}")
    print(contract)


if __name__ == '__main__':
    main()
#
# # Create the contract instance
# SimpleStorage = web3.eth.contract(abi=abi, bytecode=bytecode)
#

#
# chainId = 1337
#
# # Deploy the contract
# transaction = SimpleStorage.constructor().transact({
#     "chainId": chainId,
#     "from": account,
#     "nonce": recent_transaction,
#     "gasPrice": web3.eth.gas_price
# })
#
# print(f"transaction: {transaction}")
#
# tx_receipt = web3.eth.wait_for_transaction_receipt(transaction)
#
# # # Get contract address
# contract_address = tx_receipt.contractAddress
# print(f"Contract deployed at address: {contract_address}")
# #
# # # Create a contract instance to interact with
# contract_instance = web3.eth.contract(address=contract_address, abi=abi)
# #
# # # Interact with the contract
# # # Set value
# tx_hash = contract_instance.functions.set(15).transact({
#     # "chainId": chainId,
#     "from": account,
#     # "nonce": tx_receipt,
#     "gasPrice": web3.eth.gas_price
# })
# web3.eth.wait_for_transaction_receipt(tx_hash)
# # #
# # # # Get value
# stored_data = contract_instance.functions.get().call()
# print(f"Stored data: {stored_data}")
