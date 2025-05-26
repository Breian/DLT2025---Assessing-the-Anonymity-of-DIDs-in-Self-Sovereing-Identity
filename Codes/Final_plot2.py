import json
import textwrap
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# List of target nametags to check
targets = [
    'ENS: Old Registrar', 'BlockchainArtExchange: BAE Token', 'Enjin:  X Token',
    'Axie Infinity: Axie Clock Auction', '0xd48c6a5c3046a29a57dad9b6453769c674b7d22f',
    '0xe60c3a67c51483f7b619ff6e47f5f2d14de7d7d4', 'dYdX: Solo Margin',
    'Falcon Project: FNT Token', 'Axie Infinity: Breeding Contract #1',
    'Uniswap: Universal Router', 'Opium.Team: Match', '0xa32ff8ca08036337fabf50fa029812361cd176c8',
    '0x: Exchange Proxy', 'BAE: BAEPAY Token', 'Wrapped Ether',
    '0x2947f98c42597966a0ec25e92843c09ac17fbaa7', 'MetaCartel: Treasury',
    'Small Love Potion: Old SLP Token', 'Axie Infinity: Ronin Bridge',
    '0x30e0130141b3f113480a5941ca180ad8c5f98612', 'Wrapped Origin Axie : WOA Token',
    '0xd29044ed00822f543ed79ba237006f3f8be31609', 'OpenSea: Wyvern Exchange v1',
    'Async Art: ASYNC Token', '0x91351a04b3365808518d22db2884d3c288a4bbd1',
    'Blockchain Art Exchange: BAE Token', 'DSProxy #145,543', 'Async Art: ASYNC-V2 Token',
    'Opium.Team: Oracle Aggregator V1', 'DSProxy #7,004'
]

# Load the JSON file
with open("grouped_by_community.json", "r") as file:
    data = json.load(file)

# Counter for operations (source and target separately)
operation_source_counter = Counter()
operation_target_counter = Counter()

# Loop through each community
for community_id, interactions in data.items():
    for interaction in interactions:
        # Extract relevant fields
        source_did = interaction.get("sourceDID", "")
        target_did = interaction.get("targetDID", "")
        source_name = interaction.get("sourceNametag", "")
        target_name = interaction.get("targetNametag", "")
        operation_type = interaction.get("operation", "Unknown")
        count = interaction.get("count", 0)

        # Check if source or target matches targets list
        
        if target_name in targets:
            operation_target_counter[(operation_type, target_name)] += count

# Merge counters for plotting
combined_counter =  operation_target_counter

# Get the top 15 most common operation-target/source pairs
top_operations = combined_counter.most_common(50)
print(top_operations)
# Prepare data for plotting
operation_target_labels = [
    f"{op}\n({name})" for op, name in [pair[0] for pair in top_operations]
]
counts = [pair[1] for pair in top_operations]

# Wrap the operation-target labels to fit in multiple lines
wrapped_labels = [textwrap.fill(label, width=30) for label in operation_target_labels]

# Create a bar plot with Seaborn
plt.figure(figsize=(12, 8))
sns.barplot(x=counts, y=wrapped_labels, palette="mako")

# Add titles and labels
plt.title("Top 15 Operations Involving Target Nametags (Source or Target)", fontsize=18)
plt.xlabel("Total Count", fontsize=16)
plt.ylabel("Operation (Nametag)", fontsize=16)

# Show the plot
plt.tight_layout()
plt.show()
