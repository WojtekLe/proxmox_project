
import json

with open("terraform-output.json") as f:
    data = json.load(f)

print(data)
