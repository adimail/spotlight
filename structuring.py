import pandas as pd
import json

# Load data from JSON files
with open('taxonomy.json', 'r') as f1, open('legal_functionalities_and_services.json', 'r') as f2:
    taxonomy_data = json.load(f1)
    functionalities_data = json.load(f2)

# Create DataFrames from the JSON data
legal_topics_df = pd.DataFrame(taxonomy_data["LegalTopics"])
functionalities_df = pd.DataFrame(functionalities_data["functionalities"])

# Display the DataFrames
print("Legal Topics DataFrame:")
print(legal_topics_df.head())

print("\nFunctionalities DataFrame:")
print(functionalities_df.head())
