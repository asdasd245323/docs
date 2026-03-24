import os
import json

base_dir = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/api/gigs-events/schemas/"
os.makedirs(base_dir, exist_ok=True)

events = [
    "com.gigs.addon.archived",
    "com.gigs.addon.created",
    "com.gigs.addon.deleted",
    "com.gigs.addon.published",
    "com.gigs.addon.updated",
    "com.gigs.apiKey.created",
    "com.gigs.apiKey.deleted",
    "com.gigs.connectSession.created",
    "com.gigs.connectSession.updated",
    "com.gigs.creditNote.created",
    "com.gigs.creditNote.updated",
    "com.gigs.creditNote.voided",
    "com.gigs.device.created",
    "com.gigs.device.deleted",
    "com.gigs.device.updated",
    "com.gigs.eSimProfile.deleted",
    "com.gigs.eSimProfile.disabled",
    "com.gigs.eSimProfile.enabled",
    "com.gigs.eSimProfile.installed",
    "com.gigs.eSimProfile.updated",
    "com.gigs.installation.created",
    "com.gigs.installation.updated",
    "com.gigs.invoice.created",
    "com.gigs.invoice.finalized",
    "com.gigs.invoice.overdue",
    "com.gigs.invoice.paid",
    "com.gigs.invoice.updated",
    "com.gigs.invoice.voided",
    "com.gigs.invoice.willBeOverdue",
    "com.gigs.payment.created",
    "com.gigs.payment.disputeLost",
    "com.gigs.payment.disputeWon",
    "com.gigs.payment.disputed",
    "com.gigs.payment.failed",
    "com.gigs.payment.paymentMethodRequired",
    "com.gigs.payment.refunded",
    "com.gigs.payment.requiresConfirmation",
    "com.gigs.payment.succeeded",
    "com.gigs.paymentMethod.confirmed",
    "com.gigs.paymentMethod.created",
    "com.gigs.paymentMethod.deleted",
    "com.gigs.plan.archived",
    "com.gigs.plan.created",
    "com.gigs.plan.deleted",
    "com.gigs.plan.published",
    "com.gigs.plan.updated",
    "com.gigs.portOut.completed",
    "com.gigs.portOut.created",
    "com.gigs.portOut.expired",
    "com.gigs.portOut.failed",
    "com.gigs.portOut.issued",
    "com.gigs.portOut.processing",
    "com.gigs.portOut.updated",
    "com.gigs.portOutCredentials.issued",
    "com.gigs.porting.canceled",
    "com.gigs.porting.completed",
    "com.gigs.porting.created",
    "com.gigs.porting.declined",
    "com.gigs.porting.deleted",
    "com.gigs.porting.expired",
    "com.gigs.porting.failed",
    "com.gigs.porting.informationRequired",
    "com.gigs.porting.requested",
    "com.gigs.porting.updated",
    "com.gigs.project.created",
    "com.gigs.project.deleted",
    "com.gigs.project.updated",
    "com.gigs.quote.created",
    "com.gigs.sim.activated",
    "com.gigs.sim.created",
    "com.gigs.sim.deactivated",
    "com.gigs.sim.deleted",
    "com.gigs.sim.retired",
    "com.gigs.sim.updated",
    "com.gigs.subscription.activated",
    "com.gigs.subscription.canceled",
    "com.gigs.subscription.created",
    "com.gigs.subscription.ended",
    "com.gigs.subscription.renewed",
    "com.gigs.subscription.restored"
]

docs_pages = []

for event in events:
    title = event
    filename = event + ".mdx"
    schema_name = event
    content = f'---\ntitle: "{title}"\nopenapi-schema: "{schema_name}"\n---\n'
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)
    docs_pages.append(f"api/gigs-events/schemas/{event}")

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
                schema_subgroup["pages"] = docs_pages
            else:
                events_group["pages"].append({
                    "group": "Schemas",
                    "pages": docs_pages
                })
        else:
            # Find insertion index (before Gigs Reminders)
            insert_idx = len(groups)
            for i, group in enumerate(groups):
                if group.get("group") == "Gigs Reminders":
                    insert_idx = i
                    break
            
            groups.insert(insert_idx, {
                "group": "Gigs Events",
                "pages": [
                    {
                        "group": "Schemas",
                        "pages": docs_pages
                    }
                ]
            })
        break

with open(docs_json_path, "w", encoding="utf-8") as f:
    json.dump(docs, f, indent=2)

print("Created MDX files and updated docs.json for Gigs Events!")
