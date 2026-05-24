import json

with open('mmm_model_features.json', 'r') as f:
    features = json.load(f)

print("=== Your Model Features ===")
for i, feature in enumerate(features, 1):
    print(f"{i}. {feature}")