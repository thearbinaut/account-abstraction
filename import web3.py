
# Set up the Web3 provider
w3 = web3.Web3(web3.providers.InfuraProvider('f8827ad8fea341f6948d164cd39680ed'))

# Set up the Ethereum address
address = '0x1234567890abcdef'

# Get the balance of the Ethereum address
balance = w3.eth.get_balance(address)

# Print the balance
print(f'The balance of {address} is {balance} wei')
def w3():
    w3 = Web3(Web3.EthereumTesterProvider())
    w3.eth.default_account = w3.eth.accounts[0]
    return w3