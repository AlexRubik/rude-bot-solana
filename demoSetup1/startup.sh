#!/bin/bash

# Read the JSON file
mints=$(jq -r '.mints | join(",")' mints.json)

# Remove newlines and spaces
mints=$(echo "$mints" | tr -d '[:space:]' | tr '\n' ',' | sed 's/,$//')

# Construct the command
CMD="/fullPathToJupHere/jupiter-swap-api --filter-markets-with-mints $mints --market-cache https://cache.jup.ag/markets?v=3 \
--rpc-url https://quicknodeRpc --allow-circular-arbitrage \
--enable-new-dexes \
-x access-token-here -e https://shyftGrpc"

# Execute the constructed command
exec $CMD