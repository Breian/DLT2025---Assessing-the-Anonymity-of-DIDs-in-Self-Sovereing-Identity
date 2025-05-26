import json

# File paths
nametags_file = 'nametags.json'

# DIDs categorized by centrality metric
degree_centrality_dids = [
    "0xdca7ef03e98e0dc2b855be647c39abe984fcf21b",
    "0xa6ec692942dc8c590693dc2a1cba5a7413de851f",
    "0x2d9e5de7d36f3830c010a28b29b3bdf5ca73198e",
    "0x775060cb6eb1789919554c129b08bba097c8786b",
    "0x5b93ff82faaf241c15997ea3975419dddd8362c5"
]

betweenness_centrality_dids = [
    "0xdca7ef03e98e0dc2b855be647c39abe984fcf21b",
    "0x5b93ff82faaf241c15997ea3975419dddd8362c5",
    "0xb203faa6207ce9384d46fa5b9f397d304f17943c",
    "0x049808d5eaa90a2665b9703d2246dded34f1eb73",
    "0x5f67ffa4b3f77dd16c9c34a1a82cab8daea03191"
]

closeness_centrality_dids = [
    "0xdca7ef03e98e0dc2b855be647c39abe984fcf21b",
    "0x7a250d5630b4cf539739df2c5dacb4c659f2488d",
    "0x445b774c012c5418d6d885f6cbfeb049a7fe6558",
    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "0x6b175474e89094c44da98b954eedeac495271d0f"
]

# Load nametags from the JSON file
with open(nametags_file, 'r', encoding="ISO-8859-1") as f:
    nametags_data = json.load(f)

# Function to print nametag or 'Unknown' for each DID in a list
def print_nametags_for_dids(centrality_type, did_list, nametags_dict):
    print(f"\n{centrality_type} Centrality DIDs:")
    for did in did_list:
        nametag = nametags_dict.get(did, "Unknown")  # Get the nametag or 'Unknown' if not present
        print(f"DID: {did}, Nametag: {nametag}")

# Print the nametags for each centrality metric category
print_nametags_for_dids("Degree", degree_centrality_dids, nametags_data)
print_nametags_for_dids("Betweenness", betweenness_centrality_dids, nametags_data)
print_nametags_for_dids("Closeness", closeness_centrality_dids, nametags_data)
