import json
import os

openapi_path = 'c:/Users/saima/OneDrive/Desktop/fiverr/docs/api-reference/openapi.json'
with open(openapi_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

schemas = list(d.get('components', {}).get('schemas', {}).keys())
print(", ".join(schemas))
