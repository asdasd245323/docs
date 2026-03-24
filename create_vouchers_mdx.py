import os
import json

base_dir = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/api/gigs-billing"

files_to_create = {
    "vouchers/list-all-vouchers.mdx": '---\ntitle: "List all vouchers"\nopenapi: "GET /projects/{project}/vouchers"\n---',
    "vouchers/create-a-voucher.mdx": '---\ntitle: "Create a voucher"\nopenapi: "POST /projects/{project}/vouchers"\n---',
    "vouchers/retrieve-a-voucher.mdx": '---\ntitle: "Retrieve a voucher"\nopenapi: "GET /projects/{project}/vouchers/{voucher}"\n---',
    "vouchers/retire-a-voucher.mdx": '---\ntitle: "Retire a voucher"\nopenapi: "POST /projects/{project}/vouchers/{voucher}/retire"\n---',
    "schemas/voucher.mdx": '---\ntitle: "Voucher"\nopenapi-schema: "Voucher"\n---'
}

for path, content in files_to_create.items():
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

# Update docs.json
docs_json_path = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/docs.json"
with open(docs_json_path, "r", encoding="utf-8") as f:
    docs = json.load(f)

for tab in docs.get("navigation", {}).get("tabs", []):
    if tab.get("tab") == "Reference":
        for group in tab.get("groups", []):
            if group.get("group") == "Gigs Billing API":
                pages = group["pages"]
                
                # Replace 'api/gigs-billing/vouchers' string with the group dict
                for i, page in enumerate(pages):
                    if page == "api/gigs-billing/vouchers":
                        pages[i] = {
                            "group": "Vouchers",
                            "pages": [
                                "api/gigs-billing/vouchers/list-all-vouchers",
                                "api/gigs-billing/vouchers/create-a-voucher",
                                "api/gigs-billing/vouchers/retrieve-a-voucher",
                                "api/gigs-billing/vouchers/retire-a-voucher"
                            ]
                        }
                        break
                
                # Ensure voucher schema is in schemas (it usually is)
                schema_group = next((g for g in pages if isinstance(g, dict) and g.get("group") == "Schemas"), None)
                if schema_group:
                    if "api/gigs-billing/schemas/voucher" not in schema_group["pages"]:
                        schema_group["pages"].append("api/gigs-billing/schemas/voucher")
                
                break
        break

with open(docs_json_path, "w", encoding="utf-8") as f:
    json.dump(docs, f, indent=2)

print("Vouchers MDX files created and docs.json updated!")
