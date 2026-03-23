import json

openapi_path = 'c:/Users/saima/OneDrive/Desktop/fiverr/docs/api-reference/openapi.json'

with open(openapi_path, 'r', encoding='utf-8') as f:
    openapi = json.load(f)

def traverse_and_fix(node):
    if isinstance(node, dict):
        if 'type' in node and isinstance(node['type'], list):
            # If the type is a list like ["string", "null"], fix it
            types = node['type']
            if "null" in types:
                types.remove("null")
                if len(types) == 1:
                    node['type'] = types[0]
                node['nullable'] = True
        for key, value in node.items():
            traverse_and_fix(value)
    elif isinstance(node, list):
        for item in node:
            traverse_and_fix(item)

traverse_and_fix(openapi)

with open(openapi_path, 'w', encoding='utf-8') as f:
    json.dump(openapi, f, indent=2)

print("OpenAPI 3.0 compliant fixes applied.")
