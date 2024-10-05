
"""
Module to set up Web3 provider and get Ethereum address balance.
"""

from web3 import Web3

# Set up the Web3 provider
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/f8827ad8fea341f6948d164cd39680ed'))

# Set up the Ethereum address
ADDRESS = '0x1234567890abcdef'

# Get the balance of the Ethereum address
balance = w3.eth.get_balance(ADDRESS)

# Print the balance
print(f'The balance of {ADDRESS} is {balance} wei')

def get_web3():
    """Set up Web3 with EthereumTesterProvider and return the instance."""
    web3_instance = Web3(Web3.EthereumTesterProvider())
    web3_instance.eth.default_account = web3_instance.eth.accounts[0]
    return web3_instance
