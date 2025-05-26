import os
import json

# Directory containing all the community metrics files
metrics_directory = './'

# Output file for the consolidated JSON with nodes and edges
output_file_nodes_edges = 'nodes_edges_communities.json'

# Prepare the structure for the output JSON
nodes_edges_summary = {}

# Iterate over all the files in the directory
for file_name in os.listdir(metrics_directory):
    if file_name.endswith('.json'):
        file_path = os.path.join(metrics_directory, file_name)
        
        # Load each community metrics file
        with open(file_path, 'r') as f:
            community_data = json.load(f)
        
        # Debugging: print the content of the current file
        print(f"Processing file: {file_name}")
        print(f"Content: {community_data}")
        
        # Iterate over the keys (community numbers) in the community data
        for community_id, metrics in community_data.items():
            # Check if "number_of_nodes" and "number_of_edges" exist
            nodes = metrics.get("number_of_nodes")
            edges = metrics.get("number_of_edges")
            
            # Debugging: check if nodes and edges are properly accessed
            print(f"Community {community_id} - Nodes: {nodes}, Edges: {edges}")
            
            if nodes is not None and edges is not None:
                # Store the nodes and edges for the community
                nodes_edges_summary[community_id] = {
                    "number_of_nodes": nodes,
                    "number_of_edges": edges
                }

# Save the resulting nodes and edges summary into a JSON file
with open(output_file_nodes_edges, 'w') as outfile:
    json.dump(nodes_edges_summary, outfile, indent=4)

print(f"Community nodes and edges summary saved to {output_file_nodes_edges}")
