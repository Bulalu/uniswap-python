from uniswap import Uniswap
import os


address = os.getenv("ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
version = 2
project_id = os.getenv("PROJECT_ID")

provider = f"https://rinkeby.infura.io/v3/{project_id}"


uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)
print("LETS DO THIS THING SER!")
print(f"You are on the {uniswap.netname} network")

# 10**18 wei = 1 ether

tokens = uniswap._get_token_addresses()
eth = tokens["ETH"]
dai = tokens["DAI"]

print(f"You will get {uniswap.get_price_input(eth, dai, 10**18)} DAI for 1 eth")