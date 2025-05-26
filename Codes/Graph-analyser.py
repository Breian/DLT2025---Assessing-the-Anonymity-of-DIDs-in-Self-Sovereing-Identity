import json

# File paths
json_file_path = './cross_community_interactions.json'  # Your existing JSON file with source, target, operation, and count
partition_file_path = './community_partition.json'  # The partition file with DID-community mapping
output_file_path = './updated_json_with_communities.json'  # Output file

# Load the existing JSON data
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Load the community partition data
with open(partition_file_path, 'r') as f:
    partition = json.load(f)  # This contains DID-community mapping

# Initialize a list to store the updated entries
updated_data = []

# Loop through each entry in the existing JSON data
for entry in data:
    source_did = entry['sourceDID']
    target_did = entry['targetDID']
    
    # Extract the community for both source and target DIDs from the partition
    source_community = partition.get(source_did, "Unknown")  # Default to "Unknown" if DID not in partition
    target_community = partition.get(target_did, "Unknown")
    
    # Create the updated entry with community info
    updated_entry = {
        "sourceDID": source_did,
        "targetDID": target_did,
        "sourceCommunity": source_community,
        "targetCommunity": target_community,
        "operation": entry['operation'],
        "count": entry['count']
    }
    
    # Add the updated entry to the list
    updated_data.append(updated_entry)

# Save the updated JSON data with communities to a new file
with open(output_file_path, 'w') as f:
    json.dump(updated_data, f, indent=2)

print(f"Updated JSON file with communities saved to {output_file_path}")
