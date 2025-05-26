import json
import networkx as nx
import community as community_louvain  # For Louvain method

# File paths
json_file_path = './cross_community_interactions.json'
general_metrics_file = 'general_graph_metrics.json'
community_metrics_file = 'community_graph_metrics.json'
output_partition_file = 'community_partition.json'

# Load the JSON data
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Build the graph from the JSON data
for entry in data:
    source = entry["sourceDID"]
    target = entry["targetDID"]
    operation = entry["operation"]
    count = entry["count"]

    # Add nodes and edges with weights
    if G.has_edge(source, target):
        G[source][target]['weight'] += count
    else:
        G.add_edge(source, target, weight=count, operationType=operation)

# Convert the directed graph to an undirected graph for Louvain community detection
G_undirected = G.to_undirected()

print("Graph converted to undirected graph for Louvain method.")

# Function to calculate modularity using the Louvain method
def calculate_modularity(G, partition):
    modularity = community_louvain.modularity(partition, G, weight='weight')
    return modularity

# Function to calculate homogeneity
def calculate_homogeneity(G, partition):
    intra_edges = 0
    inter_edges = 0

    for u, v in G.edges():
        if partition[u] == partition[v]:
            intra_edges += 1  # Intra-community edge
        else:
            inter_edges += 1  # Inter-community edge

    total_edges = intra_edges + inter_edges
    if total_edges == 0:
        return 0

    homogeneity = intra_edges / total_edges
    return homogeneity

# Function to calculate graph metrics
def calculate_metrics(G, partition=None):
    metrics = {
        "number_of_nodes": G.number_of_nodes(),
        "number_of_edges": G.number_of_edges(),
        "density": nx.density(G),
        "clustering_coefficient": nx.average_clustering(G, weight='weight'),
        "assortativity_coefficient": nx.degree_assortativity_coefficient(G),
    }

    # Centrality metrics
    print("Calculating degree..")
    metrics["degree_centrality"] = nx.degree_centrality(G)
    print("Calculating betweenness..")
    metrics["betweenness_centrality"] = nx.betweenness_centrality(G)
    print("Calculating closeness..")
    metrics["closeness_centrality"] = nx.closeness_centrality(G)

    if partition:
        # Modularity and homogeneity
        metrics["modularity"] = calculate_modularity(G, partition)
        metrics["homogeneity"] = calculate_homogeneity(G, partition)
    print("Metrics calculated!")
    return metrics

# Save the calculated metrics to a file
def save_metrics_to_file(metrics, output_file):
    with open(output_file, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f"Metrics saved to {output_file}")

# Function to calculate metrics for each community
def calculate_metrics_by_community(G, partition):
    community_metrics = {}

    # Group nodes by community
    communities = {}
    for node, comm_id in partition.items():
        if comm_id not in communities:
            communities[comm_id] = []
        communities[comm_id].append(node)

    # Calculate metrics for each community subgraph
    for comm_id, nodes in communities.items():
        subgraph = G.subgraph(nodes)
        print(f"Calculating metrics for community {comm_id} with {subgraph.number_of_nodes()} nodes.")
        community_metrics[comm_id] = calculate_metrics(subgraph)

    return community_metrics

# Apply Louvain community detection
print("Applying Louvain community detection...")
partition = community_louvain.best_partition(G_undirected, weight='weight')
print("Community detection completed.")

# Save the partition to a file
with open(output_partition_file, 'w') as f:
    json.dump(partition, f, indent=2)
print(f"Community partition saved to {output_partition_file}")

# Calculate general metrics for the entire graph
print("Calculating general graph metrics...")
general_graph_metrics = calculate_metrics(G_undirected, partition)
save_metrics_to_file(general_graph_metrics, general_metrics_file)

# Calculate metrics for each community and save them
print("Calculating community metrics...")
community_graph_metrics = calculate_metrics_by_community(G_undirected, partition)
save_metrics_to_file(community_graph_metrics, community_metrics_file)

print("All metrics calculation completed.")
