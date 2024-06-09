import requests

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

    print("Successfully fetched data from the API")
else:
    print("Failed to fetch data from the API")