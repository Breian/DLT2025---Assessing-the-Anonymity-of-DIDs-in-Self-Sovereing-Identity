import json

# Load the JSON data
with open('filtered_interactions.json', 'r', encoding="ISO-8859-1") as f:
    data = json.load(f)

# Initialize a dictionary to store the transformed data
transformed_data = {}

# Loop through each entry and group by community
for entry in data:
    community = entry['community']
    
    if community not in transformed_data:
        transformed_data[community] = []  # Initialize a list for each community
    
    # Append the entry to the respective community
    transformed_data[community].append({
        "sourceDID": entry["sourceDID"],
        "targetDID": entry["targetDID"],
        "sourceNametag": entry["sourceNametag"],
        "targetNametag": entry["targetNametag"],
        "operation": entry["operation"],
        "count": entry["count"]
    })

# Save the transformed data to a new JSON file
with open('grouped_by_community.json', 'w') as f:
    json.dump(transformed_data, f, indent=4)

print("Data successfully transformed and saved to 'grouped_by_community.json'.")
