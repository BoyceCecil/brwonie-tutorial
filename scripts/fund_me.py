from brownie import FundMe
from .helpful_scripts import get_account


def fund():
    account = get_account()
    entrance_fee = FundMe[-1].getEntranceFee()

    # this payable function need a transaction and brownie help you make the transaction
    FundMe[-1].fund({"from": account, "value": entrance_fee})
    print(f"you have deposit {entrance_fee} to {FundMe[-1]}")


def withdraw():
    account = get_account()
    FundMe[-1].withdraw({"from": account})
    print(f"you have withdrawn all ether from {FundMe[-1]}")


def main():
    withdraw()
