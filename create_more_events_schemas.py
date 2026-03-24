import os
import json

base_dir = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/api/gigs-events/schemas/"
os.makedirs(base_dir, exist_ok=True)

new_events = [
    "com.gigs.subscription.restricted",
    "com.gigs.subscription.resumed",
    "com.gigs.subscription.updated",
    "com.gigs.subscriptionAddon.activated",
    "com.gigs.subscriptionAddon.created",
    "com.gigs.subscriptionAddon.ended",
    "com.gigs.subscriptionAddon.renewed",
    "com.gigs.subscriptionAddon.updated",
    "com.gigs.subscriptionChange.activated",
    "com.gigs.subscriptionChange.canceled",
    "com.gigs.subscriptionChange.created",
    "com.gigs.subscriptionChange.failed",
    "com.gigs.subscriptionChange.processing",
    "com.gigs.subscriptionChange.updated",
    "com.gigs.usageBalance.thresholdExceeded",
    "com.gigs.usageNotification.created",
    "com.gigs.usageThreshold.exceeded",
    "com.gigs.user.address.created",
    "com.gigs.user.address.deleted",
    "com.gigs.user.blocked",
    "com.gigs.user.created",
    "com.gigs.user.deleted",
    "com.gigs.user.updated",
    "com.gigs.user.verified",
    "com.gigs.virtualNumber.activated",
    "com.gigs.virtualNumber.canceled",
    "com.gigs.virtualNumber.created",
    "com.gigs.virtualNumber.ended",
    "com.gigs.virtualNumber.updated",
    "com.gigs.voucher.created",
    "com.gigs.voucher.retired",
    "com.gigs.voucher.updated"
]

for event in new_events:
    title = event
    filename = event + ".mdx"
    schema_name = event
    content = f'---\ntitle: "{title}"\nopenapi-schema: "{schema_name}"\n---\n'
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Update docs.json safely
docs_json_path = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/docs.json"
with open(docs_json_path, "r", encoding="utf-8") as f:
    docs = json.load(f)

# Find 'Reference' tab groups
for tab in docs.get("navigation", {}).get("tabs", []):
    if tab.get("tab") == "Reference":
        groups = tab.get("groups", [])
        
        # Check if "Gigs Events" already exists
        events_group = next((g for g in groups if g.get("group") == "Gigs Events"), None)
        
        if events_group:
            schema_subgroup = next((g for g in events_group["pages"] if isinstance(g, dict) and g.get("group") == "Schemas"), None)
            if schema_subgroup:
                existing_pages = schema_subgroup.get("pages", [])
                
                # Create a set to avoid duplicates
                page_set = set(existing_pages)
                
                for event in new_events:
                    page_path = f"api/gigs-events/schemas/{event}"
                    if page_path not in page_set:
                        existing_pages.append(page_path)
                
                # Sort them alphabetically
                existing_pages.sort()
                schema_subgroup["pages"] = existing_pages
        break

with open(docs_json_path, "w", encoding="utf-8") as f:
    json.dump(docs, f, indent=2)

print("Created additional MDX files and updated docs.json for Gigs Events!")
