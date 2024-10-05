
"""
Module to fetch contract ABI from Etherscan and save it to a file.
"""

import json
import requests

ABI_ENDPOINT = 'https://api.etherscan.io/api?module=contract&action=getabi&address='

# Define contract address and output file
CONTRACT_ADDRESS = '0xYourContractAddress'
OUTPUT_FILE = 'abi.json'

response = requests.get(f'{ABI_ENDPOINT}{CONTRACT_ADDRESS}', timeout=10)
response_json = response.json()
abi_json = json.loads(response_json['result'])
result = json.dumps({"abi": abi_json}, indent=4, sort_keys=True)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
    file.write(result)
