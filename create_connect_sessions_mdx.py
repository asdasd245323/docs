import os
import json

base_dir = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/api/gigs-connect/connect-sessions"
os.makedirs(base_dir, exist_ok=True)

files_to_create = {
    "create-a-connect-session.mdx": '---\ntitle: "Create a connect session"\nopenapi: "POST /projects/{project}/connectSessions"\n---',
    "retrieve-a-connect-session.mdx": '---\ntitle: "Retrieve a connect session"\nopenapi: "GET /projects/{project}/connectSessions/{connectSessionId}"\n---',
    "update-a-connect-session.mdx": '---\ntitle: "Update a connect session"\nopenapi: "PATCH /projects/{project}/connectSessions/{connectSessionId}"\n---'
}

for filename, content in files_to_create.items():
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Update docs.json
docs_json_path = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/docs.json"
with open(docs_json_path, "r", encoding="utf-8") as f:
    docs = json.load(f)

for tab in docs.get("navigation", {}).get("tabs", []):
    if tab.get("tab") == "Reference":
        for group in tab.get("groups", []):
            if group.get("group") == "Gigs Connect API":
                pages = group.get("pages", [])
                
                # Replace the simple string with a group dictionary if it hasn't been replaced yet
                for i, page in enumerate(pages):
                    if page == "api/gigs-connect/connect-sessions" or (isinstance(page, dict) and page.get("group") == "Connect Sessions"):
                        pages[i] = {
                            "group": "Connect Sessions",
                            "pages": [
                                "api/gigs-connect/connect-sessions/create-a-connect-session",
                                "api/gigs-connect/connect-sessions/retrieve-a-connect-session",
                                "api/gigs-connect/connect-sessions/update-a-connect-session"
                            ]
                        }
                        break
                
                break
        break

with open(docs_json_path, "w", encoding="utf-8") as f:
    json.dump(docs, f, indent=2)

print("Created MDX files and updated docs.json for Gigs Connect API / Connect Sessions!")
