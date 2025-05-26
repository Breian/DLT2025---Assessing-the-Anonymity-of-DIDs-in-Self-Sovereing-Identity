import os
import json

# List of Closeness Centrality DIDs (Top 5 by Closeness Centrality)
closeness_centrality_dids = [
    "0xdca7ef03e98e0dc2b855be647c39abe984fcf21b",
    "0x7a250d5630b4cf539739df2c5dacb4c659f2488d",
    "0x445b774c012c5418d6d885f6cbfeb049a7fe6558",
    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "0x6b175474e89094c44da98b954eedeac495271d0f"
]

# File paths
input_json_file = 'cross_community_interactions.json'  # Replace with the correct path to your input JSON file
output_json_file = 'closeness_dids_operations.json'  # Output file for Closeness DIDs operations

# Load the operations data from the input JSON file
with open(input_json_file, 'r') as f:
    operations_data = json.load(f)

# Initialize a dictionary to store the operations performed by each DID, separating source and target
operations_by_did = {did: {"source": {}, "target": {}} for did in closeness_centrality_dids}

# Process the operations data and collect the operations performed by each Closeness Centrality DID
for entry in operations_data:
    source_did = entry["sourceDID"]
    target_did = entry["targetDID"]
    operation = entry["operation"]
    count = entry["count"]

    # If the source DID is one of the Closeness Centrality DIDs, save the operation under 'source'
    if source_did in closeness_centrality_dids:
        if operation not in operations_by_did[source_did]["source"]:
            operations_by_did[source_did]["source"][operation] = 0
        operations_by_did[source_did]["source"][operation] += count

    # If the target DID is one of the Closeness Centrality DIDs, save the operation under 'target'
    if target_did in closeness_centrality_dids:
        if operation not in operations_by_did[target_did]["target"]:
            operations_by_did[target_did]["target"][operation] = 0
        operations_by_did[target_did]["target"][operation] += count

# Save the operations for all Closeness Centrality DIDs into a single JSON file
with open(output_json_file, 'w') as f:
    json.dump(operations_by_did, f, indent=2)
    print(f'Operations for Closeness Centrality DIDs saved to {output_json_file}')
