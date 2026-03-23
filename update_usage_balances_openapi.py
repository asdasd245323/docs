import json
from pathlib import Path

openapi_path = Path("c:/Users/saima/OneDrive/Desktop/fiverr/docs/api-reference/openapi.json")

with open(openapi_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Add paths
paths = data.get("paths", {})

paths["/projects/{project}/usageBalances"] = {
    "get": {
        "summary": "List all usage balances",
        "description": "Returns a list of usage balances for the given project. The list can be filtered by subscription, subscription period, or subscription add-on. When filtering by subscription without specifying subscriptionPeriod or subscriptionAddon, all usage balances for the subscription are returned regardless of source type or period.\n\n#### Preview\nThis endpoint is currently in preview and might change in the future.\nWe’re excited to hear your feedback and ideas. Please send an email to support@gigs.com to share your thoughts.",
        "tags": ["Usage Balances"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "subscription",
                "in": "query",
                "description": "Filter usage balances by Subscription ID.",
                "schema": {"type": "string"}
            },
            {
                "name": "subscriptionPeriod",
                "in": "query",
                "description": "Filter usage balances by subscription period. Requires the `subscription` parameter. Accepts a positive integer, the special value `current`, or a negative integer to request previous periods (e.g., `-1` for the previous period). Cannot be combined with `subscriptionAddon`. A usage balance is sourced from either a subscription period or a subscription add-on, never both - combining these will return an error.",
                "schema": {"type": "string"}
            },
            {
                "name": "subscriptionAddon",
                "in": "query",
                "description": "Filter usage balances by Subscription Add-on ID. Can be combined with `subscription` but not with `subscriptionPeriod`. A usage balance is sourced from either a subscription period or a subscription add-on, never both — combining these will return an error.",
                "schema": {"type": "string"}
            }
        ],
        "responses": {
            "200": {
                "description": "Returns a list of usage balances.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UsageBalanceList"
                        }
                    }
                }
            }
        }
    }
}

paths["/projects/{project}/usageBalances/{usageBalance}"] = {
    "get": {
        "summary": "Retrieve a usage balance",
        "description": "Returns the details of an existing usage balance.\n\n#### Preview\nThis endpoint is currently in preview and might change in the future.\nWe’re excited to hear your feedback and ideas. Please send an email to support@gigs.com to share your thoughts.",
        "tags": ["Usage Balances"],
        "parameters": [
            {
                "name": "project",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the project.",
                "schema": {"type": "string"}
            },
            {
                "name": "usageBalance",
                "in": "path",
                "required": True,
                "description": "The unique identifier for the usage balance.",
                "schema": {"type": "string"}
            }
        ],
        "responses": {
            "200": {
                "description": "Returns the usage balance.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UsageBalance"
                        }
                    }
                }
            }
        }
    }
}

data["paths"] = paths

# Add schemas
schemas = data.get("components", {}).get("schemas", {})

schemas["AllowanceCoverage"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["coverage"]
        },
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "countries": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    }
}

schemas["Allowance"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["allowance"]
        },
        "id": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "coverage": {
            "$ref": "#/components/schemas/AllowanceCoverage"
        },
        "limit": {
            "type": "integer"
        },
        "unit": {
            "type": "string"
        },
        "priority": {
            "type": "integer"
        }
    }
}

schemas["UsageBalanceSource"] = {
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "enum": ["subscriptionPeriod", "subscriptionAddon"],
            "description": "The entity type providing the allowance."
        },
        "subscriptionPeriod": {
            "type": "integer",
            "nullable": True,
            "description": "When the allowance is provided by the subscription's plan, the subscription period this usage balance is bound by."
        },
        "subscriptionAddon": {
            "type": "string",
            "nullable": True,
            "description": "When the allowance is provided by a Subscription Add-on, the subscription add-on this usage balance is provided by."
        }
    }
}

schemas["UsageBalance"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["usageBalance"],
            "description": "Type of object is always `usageBalance`."
        },
        "id": {
            "type": "string",
            "description": "Unique identifier for the usage balance.",
            "example": "ubl_0V9n0zo90CE0NuvcsN0j88"
        },
        "allowance": {
            "$ref": "#/components/schemas/Allowance"
        },
        "subscription": {
            "type": "string",
            "description": "Unique identifier of the Subscription the usage balance is related to.",
            "example": "sub_0SNlurA049MEWV2gSfSxi00xlPIi"
        },
        "source": {
            "$ref": "#/components/schemas/UsageBalanceSource"
        },
        "unit": {
            "type": "string",
            "enum": ["bytes", "seconds", "messages"],
            "description": "The unit the usage is counted in."
        },
        "used": {
            "type": "integer",
            "description": "The amount of usage consumed, counted in `unit`."
        },
        "limit": {
            "type": "integer",
            "nullable": True,
            "description": "The amount of usage permitted by the associated allowance counted in `unit`. A value of `null` indicates an unlimited allowance."
        },
        "remaining": {
            "type": "integer",
            "nullable": True,
            "description": "The amount remaining that can still be consumed, counted in `unit`. A value of `null` indicates an unlimited allowance."
        },
        "usedPercent": {
            "type": "integer",
            "nullable": True,
            "description": "The percentage of `limit` that has been used, expressed as an integer between 0 and 100. A value of `null` indicates an unlimited allowance."
        },
        "remainingPercent": {
            "type": "integer",
            "nullable": True,
            "description": "The percentage of `limit` that has not been used, expressed as an integer between 0 and 100. A value of `null` indicates an unlimited allowance."
        },
        "usableFrom": {
            "type": "string",
            "description": "Timestamp representing the beginning of this usage balance's validity."
        },
        "usableUntil": {
            "type": "string",
            "description": "Timestamp representing the end of this usage balance's validity."
        }
    }
}

schemas["UsageBalanceList"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["list"]
        },
        "items": {
            "type": "array",
            "items": {
                "$ref": "#/components/schemas/UsageBalance"
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

data["components"]["schemas"] = schemas

with open(openapi_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("openapi.json has been updated with Usage Balances endpoints and schemas.")
