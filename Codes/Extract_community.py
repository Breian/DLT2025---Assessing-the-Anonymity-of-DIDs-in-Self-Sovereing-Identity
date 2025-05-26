import json
import os

# Path to the input JSON file
input_json_file = 'grouped_by_community.json'  # Replace with your actual file path
output_directory = 'Communities_operations'  # Directory to save the community files

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Load the original JSON data
with open(input_json_file, 'r') as f:
    data = json.load(f)

# Loop through each community in the original data and save each as a separate JSON file
for community_id, operations in data.items():
    output_file_path = os.path.join(output_directory, f'community_{community_id}_operations.json')
    
    # Save the operations for the current community in a separate file
    with open(output_file_path, 'w') as output_file:
        json.dump({community_id: operations}, output_file, indent=2)
    
    print(f'Saved community {community_id} operations to {output_file_path}')
