# tests/test_contract.py
from web3 import Web3
import json
import pytest

# Setup Web3 and Ganache connection
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

# Load ABI and Bytecode from files
with open("../build/SimpleStorage.abi", "r") as abi_file:
    abi = json.load(abi_file)

with open("../build/SimpleStorage.bin", "r") as bin_file:
    bytecode = bin_file.read().strip()


# Deploy contract fixture
@pytest.fixture(scope="module")
def simple_storage():
    SimpleStorage = web3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = SimpleStorage.constructor().transact()
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)


# Test function
def test_set_and_get_number(simple_storage):
    simple_storage.functions.setNumber(42).transact()
    stored_number = simple_storage.functions.getNumber().call()
    assert stored_number == 42
