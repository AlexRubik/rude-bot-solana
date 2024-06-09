import requests
import time

# Make the GET request
url = "https://api.geckoterminal.com/api/v2/networks/solana/trending_pools"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Initialize an empty list to store the base token strings
    base_token_strings = []

    # Loop through the data and extract the base token strings
    for pool in data["data"]:
        base_token_id = pool["relationships"]["base_token"]["data"]["id"]
        base_token_string = base_token_id.split("_")[1]
        base_token_strings.append(base_token_string)

    # Print the base token strings
    print(base_token_strings)
    # print the length of the array
    print(len(base_token_strings))

    print("Successfully fetched data from coingecko API")
    
    # Iterate over each base token string and make the GET request
    jup_url = "https://quote-api.jup.ag/v6"
    tokens_with_context_slot = []
    for base_token in base_token_strings:
        quote_url = f"{jup_url}/quote?inputMint=So11111111111111111111111111111111111111112&outputMint={base_token}&amount=1000000000&slippageBps=5&onlyDirectRoutes=false&asLegacyTransaction=false&maxAccounts=28"
        quote_response = requests.get(quote_url)

        if quote_response.status_code == 200:
            response_json = quote_response.json()

            # Check if the response has a contextSlot field
            if "contextSlot" in response_json:
                tokens_with_context_slot.append(base_token)
                # has context slot so print the token
                print(f"Valid SOL Pair token: {base_token}")

            print("-" * 40)
        else:
            print(f"Invalid SOL Pair token {base_token}")

        # Delay for 1 second
        time.sleep(1)

    # Print the tokens with contextSlot
    print("Valid SOL Pair Tokens:")
    print(tokens_with_context_slot)
        

else:
    print("Failed to fetch data from the API")