from decimal import Decimal
from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIORMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIORMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 400000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIORMENTS
        or network.show_active in FORKED_LOCAL_ENVIORMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Active network is {network.show_active}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("Mock Deployed!")
