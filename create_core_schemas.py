import os
import json

base_dir = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/api/gig-core-api/schemas/"

schemas_map = {
    "Actor": ("actor.mdx", "Actor"),
    "Add-on": ("add-on.mdx", "Addon"),
    "Allowance": ("allowance.mdx", "Allowance"),
    "APIKey": ("apikey.mdx", "APIKey"),
    "Coverage": ("coverage.mdx", "Coverage"),
    "Device": ("device.mdx", "Device"),
    "DeviceModel": ("device-model.mdx", "DeviceModel"),
    "DeviceModelBrands": ("device-model-brands.mdx", "DeviceModelBrands"),
    "Error": ("error.mdx", "Error"),
    "EsimProfile": ("esim-profile.mdx", "eSimProfile"),
    "Metadata": ("metadata.mdx", "Metadata"),
    "NetworkAvailability": ("network-availability.mdx", "NetworkAvailability"),
    "Organization": ("organization.mdx", "Organization"),
    "Period": ("period.mdx", "Period"),
    "Plan": ("plan.mdx", "Plan"),
    "PlanDocument": ("plan-document.mdx", "PlanDocument"),
    "Porting": ("porting.mdx", "Porting"),
    "PortOut": ("port-out.mdx", "PortOut"),
    "DeprecatedPortOutCredentials": ("deprecated-port-out-credentials.mdx", "DeprecatedPortOutCredentials"),
    "PortOutCredentials": ("port-out-credentials.mdx", "PortOutCredentials"),
    "Price": ("price.mdx", "Price"),
    "Project": ("project.mdx", "Project"),
    "ProjectCredentials": ("project-credentials.mdx", "ProjectCredentials"),
    "PropertyErrorDetail": ("property-error-detail.mdx", "PropertyErrorDetail"),
    "ServiceProvider": ("service-provider.mdx", "ServiceProvider"),
    "Sim": ("sim.mdx", "Sim"),
    "SimCredentials": ("sim-credentials.mdx", "SimCredentials"),
    "Subscription": ("subscription.mdx", "Subscription"),
    "SubscriptionAddon": ("subscription-addon.mdx", "SubscriptionAddon"),
    "SubscriptionChange": ("subscription-change.mdx", "SubscriptionChange"),
    "UsageBalance": ("usage-balance.mdx", "UsageBalance"),
    "UsageBalanceSource": ("usage-balance-source.mdx", "UsageBalanceSource"),
    "UsageRecord": ("usage-record.mdx", "UsageRecord"),
    "User": ("user.mdx", "User"),
    "UserAddress": ("user-address.mdx", "UserAddress"),
    "VirtualNumber": ("virtual-number.mdx", "VirtualNumber")
}

os.makedirs(base_dir, exist_ok=True)

docs_pages = []
for title, (filename, schema_name) in schemas_map.items():
    content = f'---\ntitle: "{title}"\nopenapi-schema: "{schema_name}"\n---\n'
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)
    docs_pages.append(f"api/gig-core-api/schemas/{filename.replace('.mdx', '')}")

# Now update docs.json safely
docs_json_path = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/docs.json"
with open(docs_json_path, "r", encoding="utf-8") as f:
    docs = json.load(f)

# Find 'Gig Core API' group under navigation -> tabs[0] -> groups
for tab in docs.get("navigation", {}).get("tabs", []):
    if tab.get("tab") == "Reference":
        for group in tab.get("groups", []):
            if group.get("group") == "Gig Core API":
                # Check if "Schemas" already exists
                schema_group = next((g for g in group["pages"] if isinstance(g, dict) and g.get("group") == "Schemas"), None)
                if schema_group:
                    schema_group["pages"] = docs_pages
                else:
                    group["pages"].append({
                        "group": "Schemas",
                        "pages": docs_pages
                    })
                break
        break

with open(docs_json_path, "w", encoding="utf-8") as f:
    json.dump(docs, f, indent=2)

print("Created MDX files and updated docs.json!")
