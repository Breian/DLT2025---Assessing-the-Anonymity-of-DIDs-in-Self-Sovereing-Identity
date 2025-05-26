import json

# Load the cross-community interactions data
with open('./updated_json_with_communities.json', 'r') as f:
    interactions = json.load(f)

# Initialize a dictionary to store transaction counts for each DID
did_metrics = {}

# Loop through each interaction to count transactions
for interaction in interactions:
    source_did = interaction['sourceDID']
    target_did = interaction['targetDID']
    source_community = interaction['sourceCommunity']
    target_community = interaction['targetCommunity']
    count = interaction['count']

    # Process source DID
    if source_did not in did_metrics:
        did_metrics[source_did] = {
            "community": source_community,
            "internalTransactions": 0,
            "externalTransactions": 0,
            "ratio": 0.0  # To be calculated later
        }

    # Check if the transaction is internal or external
    if source_community == target_community:
        did_metrics[source_did]['internalTransactions'] += count
    else:
        did_metrics[source_did]['externalTransactions'] += count

    # Process target DID
    if target_did not in did_metrics:
        did_metrics[target_did] = {
            "community": target_community,
            "internalTransactions": 0,
            "externalTransactions": 0,
            "ratio": 0.0  # To be calculated later
        }

    # Check if the transaction is internal or external for target DID
    if target_community == source_community:
        did_metrics[target_did]['internalTransactions'] += count
    else:
        did_metrics[target_did]['externalTransactions'] += count

# Calculate the ratio for each DID
for did, metrics in did_metrics.items():
    internal = metrics['internalTransactions']
    external = metrics['externalTransactions']
    
    if external > 0:
        metrics['ratio'] = internal / external
    else:
        metrics['ratio'] = internal  # Set ratio to internal count if no external transactions

# Convert the metrics to the desired JSON structure
final_output = [{"did": did, **metrics} for did, metrics in did_metrics.items()]

# Save the results to a JSON file
output_file_path = './sybil.json'
with open(output_file_path, 'w') as f:
    json.dump(final_output, f, indent=2)

print(f"Transaction metrics saved to {output_file_path}")
