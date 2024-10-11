import json
import requests
import time
import random

base_token_strings = []

default_mints = [
    "So11111111111111111111111111111111111111112",
    "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",
    "USDH1SM1ojwWUga67PGrgFWUHibbjqMvuMaDkRJTgkX", 
    "2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo",
    "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", 
    "HzwqbKZw8HxMN6bF2yFZNrht3c2iXXzpKcFu7uBEDKtr",
    "EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm",
    "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263",
                 ]

for i in range(1, 11):
    print(f"Gecko Iteration number {i}:")
    url = f"https://api.geckoterminal.com/api/v2/networks/solana/trending_pools?page={i}"
    print(url)
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        data = response.json()

        for pool in data["data"]:
            attributes = pool["attributes"]
            h1_transactions = attributes["transactions"]["h1"]["buys"] + attributes["transactions"]["h1"]["sells"]
            h1_volume_usd = float(attributes["volume_usd"]["h1"])

            # Check if the token meets the criteria
            if h1_transactions >= 200 and h1_volume_usd > 50000:
                base_token_id = pool["relationships"]["base_token"]["data"]["id"]
                base_token_string = base_token_id.split("_")[1]
                base_token_strings.append(base_token_string)
                #print(f"Added token: {base_token_string}")
                
        #print(base_token_strings)
        print(len(base_token_strings))
        print("Successfully fetched and filtered data from GeckoTerminal API")
        time.sleep(0.5)
        
# reduce to X random tokens if the list is too long

if len(base_token_strings) > 30:
    base_token_strings = random.sample(base_token_strings, 30)

        
# write all the base token strings to a file called includeMints.json that contains an array of token strings

# append the default mints to the base token strings
base_token_strings.extend(default_mints)

# remove duplicates
base_token_strings = list(set(base_token_strings))

with open("includeMints.json", "w") as f:
    json.dump(base_token_strings, f)

print("Token Count:", len(base_token_strings))
print("Successfully wrote the base token strings to includeMints.json")
    
    
    
# check validity of the base token strings

# check validity function

def check_validity(base_token_strings):

    jup_url = "https://quote-api.jup.ag/v6"
    tokens_with_context_slot = []
    for base_token in base_token_strings:
        quote_url = f"{jup_url}/quote?inputMint=So11111111111111111111111111111111111111112&outputMint={base_token}&amount=1000000000&slippageBps=5&onlyDirectRoutes=false&asLegacyTransaction=false&maxAccounts=32"
        
        quote_response = requests.get(quote_url)

        if quote_response.status_code == 200:
            response_json = quote_response.json()

            if "contextSlot" in response_json:
                tokens_with_context_slot.append(base_token)
                print(f"Valid SOL Pair token: {base_token}")

            print("-" * 40)
        else:
            print(f"INVALID SOL Pair token {base_token}")
            print("-" * 40)

        time.sleep(1)

    tokens_with_context_slot = list(set(tokens_with_context_slot))
    print("Valid SOL Pair Tokens:")
    print(tokens_with_context_slot)
    print(len(tokens_with_context_slot))