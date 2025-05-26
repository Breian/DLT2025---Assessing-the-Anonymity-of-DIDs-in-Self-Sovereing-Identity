import json
import textwrap
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# List of specific DIDs (source)
specific_dids = [
    "0x719e0417768eabbe0a7f10abdb707cab40718e95",
    "0xde3e5a990bce7fc60a6f017e7c4a95fc4939299e",
    "0x00000000000c2e074ec69a0dfb2997ba6c7d2e1e",
    "0x28beb6fd342f7f41c0ebe086f78e43468c7a25c1",
    "0x40c4d5436cee287c9fd1afba4e608da418bc1f16",
    "0x05c111014a6fafca2714cee52e7f3a6c1c246073",
    "0x2e63e1c7fdf4a69edbd0a6045180d02faf241d4f",
    "0x00ff6b7d26407a46af2b631b4fa452a036d027e5",
    "0x72ce9c846789fdb6fc1f34ac4ad25dd9ef7031ef",
    "0xba61f25dd9f2d5f02d01b1c2c1c5f0b14c4b48a3",
    "0x79bf225fbfd40f78b1878a6d1eec1bb03df92aeb",
    "0x7c74f84ab9d211b0ad306fd793c593b744135c49",
    "0x4ada1b9d9fe28abd9585f58cfeed2169a39e1c6b",
    "0x1de6eec2c08830bbec7884f1fc6b502521ae2e54",
    "0x115b65464043e9d0ad7422f95d1398b593c0efd3",
    "0x5f67ffa4b3f77dd16c9c34a1a82cab8daea03191",
    "0x865c2f85c9fea1c6ac7f53de07554d68cb92ed88",
    "0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359",
    "0x505e20c0fb8252ca7ac21d54d5432eccd4f2d076",
    "0xbd1ea07bcc208715e099588add684ed78f3ff3ed",
    "0x445b774c012c5418d6d885f6cbfeb049a7fe6558",
    "0x3d0d7f8720a02cfc9fee5dc7dc08181303a6ed86",
    "0x5f13abd64833173f42c3dc22dbe568476e9d819a",
    "0x049808d5eaa90a2665b9703d2246dded34f1eb73",
    "0xfc9c45516f0c1e0715898b63d834308839cd0b35",
    "0x7a250d5630b4cf539739df2c5dacb4c659f2488d",
    "0x5b93ff82faaf241c15997ea3975419dddd8362c5",
    "0x5a4cd185bfe086b3dae993dca2448914fb4be03d",
    "0x7be8076f4ea4a4ad08075c2508e481d6c946d12b",
    "0x9af481276b075e036bc23e887a8bd275e69ef74c",
    "0xdc0046b52e2e38aee2271b6171ebb65ccd337518",
    "0x780737124207f40dbb2bcad58594fead6ae12db9",
    "0x71eb26d839ddfb6667e16e2fe8c65737a9e619c0",
    "0x5ebda6ff471a9d523c1f6d7520179dded99753e1",
    "0x8c54085ad729fde488338fc50cfc8dfd5e2b5b89",
    "0x49c97bbe8b5f7717e3ac6514a555f82cf7bffc56",
    "0x87956abc4078a0cc3b89b419928b857b8af826ed",
    "0xdca7ef03e98e0dc2b855be647c39abe984fcf21b",
    "0xa6ec692942dc8c590693dc2a1cba5a7413de851f",
    "0x2d9e5de7d36f3830c010a28b29b3bdf5ca73198e",
    "0x0f9fa759f6c408e8c24bf6bf20ed59db24b597a4",
    "0x5461707e13a5090e51a274f0ad7389d0bbf2b078",
    "0x3379536969a63467a85600f8fab93d1faa22b731",
    "0x728fe008491998e528ab34a6ab5818a1651ca586",
    "0x3f74f0af1fa2b2308dd157c7f163307e52e7fed4",
    "0x284f214df3f85526a910979f52c96e54fb228136",
    "x3564e17d5f6b7c9a3c6bd6248bf7b3eeb4927e50",
    "0xc05ed3743d87bee34b76792d28347478015d7754",
    "0x6504aad8bdd40a73a54d65afeac146488db2e31e",
    # Add more DIDs as required...
]

# Load the JSON file
with open("grouped_by_community.json", "r") as file:
    data = json.load(file)

# Counter to track target counts
target_counter = Counter()

# Loop through each community
for community_id, interactions in data.items():
    for interaction in interactions:
        # Extract relevant fields
        source_did = interaction.get("sourceDID", "")
        target_did = interaction.get("targetDID", "")
        target_name = interaction.get("targetNametag", "Unknown")
        count = interaction.get("count", 0)

        # Skip if the sourceDID is not in specific_dids
        if source_did not in specific_dids:
            continue

        # Use targetNametag if available; otherwise, use targetDID
        target = target_name if target_name != "Unknown" else target_did

        # Increment the counter for the target
        target_counter[target] += count

# Debugging: Print the target counter to verify results
print("Target Counter:", target_counter)

# Get the top 10 targets by count
top_targets = target_counter.most_common(50)
print(top_targets)

# Prepare data for plotting
targets, counts = zip(*top_targets) if top_targets else ([], [])

# Use textwrap to wrap long strings
wrapped_targets = [textwrap.fill(target, width=30) for target in targets]

# Create a bar plot with Seaborn
plt.figure(figsize=(12, 8))
sns.barplot(x=counts, y=wrapped_targets, palette="viridis")

# Add titles and labels
plt.title("Top 10 Targets of Main DIDs", fontsize=18)
plt.xlabel("Total Count", fontsize=16)
plt.ylabel("Targets", fontsize=16)

# Show the plot
plt.tight_layout()
plt.show()
