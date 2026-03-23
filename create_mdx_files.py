import os

base_dir = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/api/gig-core-api"

files_to_create = {
    "usage/list-subscription-usage-records.mdx": {
        "title": "List subscription usage records",
        "openapi": "GET /projects/{project}/subscriptions/{subscription}/usage"
    },
    "usage/simulate-subscription-usage.mdx": {
        "title": "Simulate subscription usage",
        "openapi": "POST /testing/projects/{project}/subscriptions/{subscription}/usage"
    },
    "usage-balances/list-all-usage-balances.mdx": {
        "title": "List all usage balances",
        "openapi": "GET /projects/{project}/usageBalances"
    },
    "usage-balances/retrieve-a-usage-balance.mdx": {
        "title": "Retrieve a usage balance",
        "openapi": "GET /projects/{project}/usageBalances/{usageBalance}"
    },
    "users/list-all-users.mdx": {
        "title": "List all users",
        "openapi": "GET /projects/{project}/users"
    },
    "users/create-a-user.mdx": {
        "title": "Create a user",
        "openapi": "POST /projects/{project}/users"
    },
    "users/retrieve-a-user.mdx": {
        "title": "Retrieve a user",
        "openapi": "GET /projects/{project}/users/{user}"
    },
    "users/delete-a-user.mdx": {
        "title": "Delete a user",
        "openapi": "DELETE /projects/{project}/users/{user}"
    },
    "users/update-a-user.mdx": {
        "title": "Update a user",
        "openapi": "PATCH /projects/{project}/users/{user}"
    },
    "users/search-for-users.mdx": {
        "title": "Search for users",
        "openapi": "POST /projects/{project}/users/search"
    },
    "user-addresses/list-all-user-addresses.mdx": {
        "title": "List all user addresses",
        "openapi": "GET /projects/{project}/users/{user}/addresses"
    },
    "user-addresses/create-a-user-address.mdx": {
        "title": "Create a user address",
        "openapi": "POST /projects/{project}/users/{user}/addresses"
    },
    "user-addresses/retrieve-a-user-address.mdx": {
        "title": "Retrieve a user address",
        "openapi": "GET /projects/{project}/users/{user}/addresses/{address}"
    },
    "user-addresses/delete-a-user-address.mdx": {
        "title": "Delete a user address",
        "openapi": "DELETE /projects/{project}/users/{user}/addresses/{address}"
    }
}

for filepath, content in files_to_create.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: \"{content['title']}\"\nopenapi: \"{content['openapi']}\"\n---\n")

print("All MDX files created successfully.")
