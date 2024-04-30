import requests
import json

ABI_ENDPOINT = 'https://api.etherscan.io/api?module=contract&action=getabi&address='

response = requests.get(f'{ABI_ENDPOINT}{contract_address}')
response_json = response.json()
abi_json = json.loads(response_json['result'])
result = json.dumps({"abi": abi_json}, indent=4, sort_keys=True)
with open(output_file, 'w') as file:
    file.write(result)
