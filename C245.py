from web3 import Web3
API_url = 'https://mainnet.infura.io/v3/a36a08419aeb437ca8c79973e97b5868'
web3 = Web3(Web3.HTTPProvider(infura_url))
gas_price = web3.eth.gas_price

safe_low_gas_price = int(gas_price * 0.9)
average_gas_price = int(gas_price * 1.0)
fast_gas_price = int(gas_price * 1.1)
fastest_gas_price = int(gas_price * 1.2)

safe_low_gas_price_gwei = web3.from_wei(safe_low_gas_price, 'gwei')
average_gas_price_gwei = web3.from_wei(average_gas_price, 'gwei')
fast_gas_price_gwei = web3.from_wei(fast_gas_price, 'gwei')
fastest_gas_price_gwei = web3.from_wei(fastest_gas_price, 'gwei')

print('Safe Low Gas Price (Gwei)', safe_low_gas_price_gwei)
print('Average Gas Price (Gwei)', average_gas_price_gwei)
print('Fast Gas Price (Gwei)', fast_gas_price_gwei)
print('Fastest Gas Price (Gwei)', fastest_gas_price_gwei)

gas_price = web3.eth.gas_price
print("Gas Price In Gwei", gas_price)