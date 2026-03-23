import json
from pathlib import Path

openapi_path = Path("c:/Users/saima/OneDrive/Desktop/fiverr/docs/api-reference/openapi.json")

with open(openapi_path, "r", encoding="utf-8") as f:
    data = json.load(f)

paths = data.get("paths", {})

# USERS PATHS
paths["/projects/{project}/users"] = {
    "get": {
        "summary": "List all users",
        "description": "Returns a list of users. The users returned are sorted by creation date, with the most recently created users appearing first.",
        "tags": ["Users"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "after",
                "in": "query",
                "description": "A cursor for use in pagination. The `after` parameter takes an object ID that defines the position in the list, only items immediately following the item with that ID will be returned.",
                "schema": {"type": "string"}
            },
            {
                "name": "before",
                "in": "query",
                "description": "A cursor for use in pagination. The `before` parameter takes an object ID that defines the position in the list, only items immediately preceding the item with that ID will be returned.",
                "schema": {"type": "string"}
            },
            {
                "name": "limit",
                "in": "query",
                "description": "The limit of items to be returned in the list, between 0 and 200.",
                "schema": {"type": "integer", "minimum": 0, "maximum": 200, "default": 10}
            }
        ],
        "responses": {
            "200": {
                "description": "Returns a dictionary with an items property that contains an array of user objects.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserList"
                        }
                    }
                }
            }
        }
    },
    "post": {
        "summary": "Create a user",
        "description": "Creates a new user with the given parameters.",
        "tags": ["Users"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            }
        ],
        "requestBody": {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/CreateUser"
                    }
                }
            }
        },
        "responses": {
            "201": {
                "description": "Returns the created user.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/User"
                        }
                    }
                }
            }
        }
    }
}

paths["/projects/{project}/users/{user}"] = {
    "get": {
        "summary": "Retrieve a user",
        "description": "Retrieves the details of an existing user. You need only supply the unique user identifier that was returned upon user creation.",
        "tags": ["Users"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "user",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the user.",
                "schema": {"type": "string"}
            }
        ],
        "responses": {
            "200": {
                "description": "Returns the user object if the user exists.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/User"
                        }
                    }
                }
            }
        }
    },
    "delete": {
        "summary": "Delete a user",
        "description": "Retrieves the details of an existing user and deletes it.",
        "tags": ["Users"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "user",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the user.",
                "schema": {"type": "string"}
            }
        ],
        "responses": {
            "200": {
                "description": "Returns the user after a successful deletion.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/User"
                        }
                    }
                }
            }
        }
    },
    "patch": {
        "summary": "Update a user",
        "description": "Updates the specified user by setting the values of the parameters passed.",
        "tags": ["Users"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "user",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the user.",
                "schema": {"type": "string"}
            }
        ],
        "requestBody": {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/UpdateUser"
                    }
                }
            }
        },
        "responses": {
            "200": {
                "description": "Returns the updated user.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/User"
                        }
                    }
                }
            }
        }
    }
}

paths["/projects/{project}/users/search"] = {
    "post": {
        "summary": "Search for users",
        "description": "Searches for existing users matching the given parameters.",
        "tags": ["Users"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            }
        ],
        "requestBody": {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/SearchUsers"
                    }
                }
            }
        },
        "responses": {
            "200": {
                "description": "Returns the users matching the search criteria.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserList"
                        }
                    }
                }
            }
        }
    }
}

# USER ADDRESSES PATHS
paths["/projects/{project}/users/{user}/addresses/{address}"] = {
    "get": {
        "summary": "Retrieve a user address",
        "description": "Retrieves the details of an existing address for a given user.",
        "tags": ["User Addresses"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "user",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the user.",
                "schema": {"type": "string"}
            },
            {
                "name": "address",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the address.",
                "schema": {"type": "string"}
            }
        ],
        "responses": {
            "200": {
                "description": "Returns the address if it exists and is owned by the user.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserAddress"
                        }
                    }
                }
            }
        }
    },
    "delete": {
        "summary": "Delete a user address",
        "description": "Retrieves the details of an existing user address and deletes it.",
        "tags": ["User Addresses"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "user",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the user.",
                "schema": {"type": "string"}
            },
            {
                "name": "address",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the address.",
                "schema": {"type": "string"}
            }
        ],
        "responses": {
            "200": {
                "description": "Returns the address after a successful deletion.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserAddress"
                        }
                    }
                }
            }
        }
    }
}

paths["/projects/{project}/users/{user}/addresses"] = {
    "get": {
        "summary": "List all user addresses",
        "description": "Returns a list of addresses owned by the given user. The addresses returned are sorted by creation date, with the most recently created addresses appearing first.",
        "tags": ["User Addresses"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "user",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the user.",
                "schema": {"type": "string"}
            }
        ],
        "responses": {
            "200": {
                "description": "Returns a list of address objects.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserAddressList"
                        }
                    }
                }
            }
        }
    },
    "post": {
        "summary": "Create a user address",
        "description": "Create a new address for the given user with the provided parameters.\n\nIf any validations fail during the user address creation process, detailed information will be provided in the error response body. If applicable, suggested alternative values for properties that do not pass the validations will also be included.\n\nPlease note that there is a maximum limit of 10 active addresses permitted per user. Attempts to exceed this limit will result in an error response. Addresses must also be unique for a given user.",
        "tags": ["User Addresses"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "user",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the user.",
                "schema": {"type": "string"}
            }
        ],
        "requestBody": {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/CreateUserAddress"
                    }
                }
            }
        },
        "responses": {
            "201": {
                "description": "Returns the created address.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserAddress"
                        }
                    }
                }
            }
        }
    }
}

data["paths"] = paths

# SCHEMAS
schemas = data.get("components", {}).get("schemas", {})

schemas["User"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["user"],
            "description": "Type of object is always `user`."
        },
        "id": {
            "type": "string",
            "description": "Unique identifier for the user.",
            "example": "usr_0SNlurA049MEWV4OpCwsNyC9Kn2d"
        },
        "metadata": {
            "$ref": "#/components/schemas/Metadata"
        },
        "birthday": {
            "type": "string",
            "nullable": True,
            "description": "The birthday of the user.",
            "example": "2017-07-21"
        },
        "createdAt": {
            "type": "string",
            "description": "Time when the user was created.",
            "example": "2021-01-21T19:38:34Z"
        },
        "email": {
            "type": "string",
            "description": "The primary email address of the user. Must be unique across all users.",
            "example": "jerry@example.com"
        },
        "emailVerified": {
            "type": "boolean",
            "description": "Whether the user's primary email address is verified or not.",
            "example": True
        },
        "fullName": {
            "type": "string",
            "nullable": True,
            "description": "The user's full name. Required for some Plans.",
            "example": "Jerry Seinfeld"
        },
        "preferredLocale": {
            "type": "string",
            "description": "The user's locale preference represented as an IETF language tag.",
            "example": "en-US"
        },
        "status": {
            "type": "string",
            "enum": ["active", "blocked", "deleted"],
            "description": "The current status of the user."
        }
    }
}

schemas["UserList"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["list"]
        },
        "items": {
            "type": "array",
            "items": {
                "$ref": "#/components/schemas/User"
            }
        },
        "moreItemsAfter": {
            "type": "string",
            "nullable": True
        },
        "moreItemsBefore": {
            "type": "string",
            "nullable": True
        }
    }
}

schemas["CreateUser"] = {
    "type": "object",
    "required": ["email"],
    "properties": {
        "birthday": {
            "type": "string",
            "nullable": True,
            "description": "The birthday of the user.",
            "example": "2017-07-21"
        },
        "email": {
            "type": "string",
            "description": "The primary verified email address of the user.",
            "example": "jerry@example.com"
        },
        "fullName": {
            "type": "string",
            "nullable": True,
            "description": "The user's full name.",
            "example": "Jerry Seinfeld"
        },
        "metadata": {
            "$ref": "#/components/schemas/Metadata"
        },
        "preferredLocale": {
            "type": "string",
            "nullable": True,
            "description": "The user's locale preference.",
            "example": "en-US"
        }
    }
}

schemas["UpdateUser"] = {
    "type": "object",
    "properties": {
        "birthday": {
            "type": "string",
            "nullable": True
        },
        "email": {
            "type": "string",
            "nullable": True
        },
        "fullName": {
            "type": "string",
            "nullable": True
        },
        "metadata": {
            "$ref": "#/components/schemas/Metadata"
        },
        "preferredLocale": {
            "type": "string",
            "nullable": True
        }
    }
}

schemas["SearchUsers"] = {
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "nullable": True,
            "description": "The primary email address of the user."
        }
    }
}

schemas["UserAddress"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["userAddress"],
            "description": "Type of object is always `userAddress`."
        },
        "id": {
            "type": "string",
            "description": "Unique identifier for the address.",
            "example": "adr_0SNlurA049MEWV5ELDmnaqVXgTFT"
        },
        "city": {
            "type": "string",
            "description": "The city/municipality of the address.",
            "example": "New York City"
        },
        "country": {
            "type": "string",
            "description": "The ISO 3166-1 alpha-2 country code of the address.",
            "example": "US"
        },
        "createdAt": {
            "type": "string",
            "description": "The time the address was created.",
            "example": "2021-01-21T19:38:34Z"
        },
        "line1": {
            "type": "string",
            "description": "The first line of the address, e.g. street and house number.",
            "example": "129 West 81st Street"
        },
        "line2": {
            "type": "string",
            "nullable": True,
            "description": "The second line of the address, e.g. apartment number.",
            "example": "Apartment 5"
        },
        "postalCode": {
            "type": "string",
            "nullable": True,
            "description": "The postal code of the address.",
            "example": "10024"
        },
        "state": {
            "type": "string",
            "nullable": True,
            "description": "The state/province/region of the address.",
            "example": "NY"
        },
        "user": {
            "type": "string",
            "description": "Unique identifier for the address user.",
            "example": "usr_0SNlurA049MEWV4OpCwsNyC9Kn2d"
        }
    }
}

schemas["UserAddressList"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["list"]
        },
        "items": {
            "type": "array",
            "items": {
                "$ref": "#/components/schemas/UserAddress"
            }
        },
        "moreItemsAfter": {
            "type": "string",
            "nullable": True
        },
        "moreItemsBefore": {
            "type": "string",
            "nullable": True
        }
    }
}

schemas["CreateUserAddress"] = {
    "type": "object",
    "required": ["city", "country", "line1"],
    "properties": {
        "city": {
            "type": "string",
            "description": "The city/municipality of the address."
        },
        "country": {
            "type": "string",
            "description": "The ISO 3166-1 alpha-2 country code of the address."
        },
        "line1": {
            "type": "string",
            "description": "The first line of the address, e.g. street and house number."
        },
        "line2": {
            "type": "string",
            "nullable": True,
            "description": "The second line of the address, e.g. apartment number."
        },
        "state": {
            "type": "string",
            "nullable": True,
            "description": "The state/province/region of the address. Required for US/CA addresses to be a valid ISO 3166-2 2 letter code."
        },
        "postalCode": {
            "type": "string",
            "nullable": True,
            "description": "The postal code of the address. Required for countries with postal codes."
        }
    }
}

data["components"]["schemas"] = schemas

with open(openapi_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("openapi.json has been updated with Users and User Addresses endpoints and schemas.")
