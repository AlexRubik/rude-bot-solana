import requests
import json

# get the slot that a transaction landed in
def get_txn_slot(transaction_signature: str):
    url = "https://api.mainnet-beta.solana.com"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTransaction",
        "params": [
            transaction_signature,
            {
            "commitment": "confirmed",
            "maxSupportedTransactionVersion": 0,
            "encoding": "jsonParsed",
            }
            
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response = response.json()
        return response["result"]["slot"]
    else:
        response.raise_for_status()
        
# get the slot for a specified block
def get_block(slot_number: int):
    url = "https://api.mainnet-beta.solana.com"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBlock",
        "params": [
            slot_number,
            {
                "encoding": "json",
                "maxSupportedTransactionVersion": 0,
                "transactionDetails": "full",
                "rewards": False
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def main():
    
    # 4UdheHjYoBbAZMaj9RetYtw4sUApWjJuyyv5BhQvCbNq9wZbncJSrH7MpKMCruWKnrdzXAcdPte1Ltx3kJGHVK9u | Sent ~ slot 273788708
    tx = get_txn_slot("4UdheHjYoBbAZMaj9RetYtw4sUApWjJuyyv5BhQvCbNq9wZbncJSrH7MpKMCruWKnrdzXAcdPte1Ltx3kJGHVK9u")
    print(tx)
    
    
main()
