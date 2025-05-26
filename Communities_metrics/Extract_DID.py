import json

# Path to the metrics file
community_metrics_file = 'community_30.json'

# Function to extract top 3 DIDs for each centrality measure
def extract_top_dids(metrics_data):
    # Extract degree, betweenness, and closeness data
    degree_centrality = metrics_data['degree_centrality']
    betweenness_centrality = metrics_data['betweenness_centrality']
    closeness_centrality = metrics_data['closeness_centrality']
    
    # Sort and extract top 3 DIDs for each measure
    top_degree_dids = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:3]
    top_betweenness_dids = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:3]
    top_closeness_dids = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:3]

    return top_degree_dids, top_betweenness_dids, top_closeness_dids

# Load the community metrics from the JSON file
with open(community_metrics_file, 'r') as f:
    community_data = json.load(f)

# Assuming you want to analyze Community 5
community_5_metrics = community_data["30"]

# Extract top DIDs for Community 5
top_degree, top_betweenness, top_closeness = extract_top_dids(community_5_metrics)

# Display the results
print("Top 3 DIDs by Degree Centrality in Community 30:")
for did, value in top_degree:
    print(f"DID: {did}, Degree Centrality: {value}")

print("\nTop 3 DIDs by Betweenness Centrality in Community 30:")
for did, value in top_betweenness:
    print(f"DID: {did}, Betweenness Centrality: {value}")

print("\nTop 3 DIDs by Closeness Centrality in Community 30:")
for did, value in top_closeness:
    print(f"DID: {did}, Closeness Centrality: {value}")
