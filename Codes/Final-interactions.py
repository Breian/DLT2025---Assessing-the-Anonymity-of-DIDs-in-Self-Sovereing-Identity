import json

# Define the file path
file_path = 'grouped_interactions_by_community.json'

# Try reading the file with UTF-8 encoding, and fall back to ISO-8859-1 if needed
try:
    # Attempt to read the file with utf-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
except UnicodeDecodeError:
    # Fallback to ISO-8859-1 encoding if utf-8 fails
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        data = json.load(file)

# Analyze the file and extract important entities

important_entities = []

# Example of identifying specific entities like "The Graph: Indexer"
for community, interactions in data.items():
    for interaction in interactions:
        source_nametag = interaction.get('sourceNametag', 'Unknown')
        target_nametag = interaction.get('targetNametag', 'Unknown')
        
        # Check for keywords like "Indexer" or "Token" in source and target nametags
        if "Indexer" in source_nametag or "Indexer" in target_nametag or \
           "Token" in source_nametag or "Token" in target_nametag:
            important_entities.append({
                "community": community,
                "source": {
                    "DID": interaction['sourceDID'],
                    "nametag": source_nametag
                },
                "target": {
                    "DID": interaction['targetDID'],
                    "nametag": target_nametag
                },
                "operation": interaction['operation'],
                "count": interaction['count']
            })

# Save the extracted important entities to a new JSON file
output_file_path = 'important_entities_separated.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(important_entities, output_file, indent=2)

print(f"Important entities extracted and saved to {output_file_path}")
