import json
from pathlib import Path

openapi_path = Path("c:/Users/saima/OneDrive/Desktop/fiverr/docs/api-reference/openapi.json")

with open(openapi_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Add paths
paths = data.get("paths", {})

paths["/projects/{project}/subscriptions/{subscription}/usage"] = {
    "get": {
        "summary": "List subscription usage records",
        "description": "Lists usage records in ascending order for a subscription, defaulting to `daily` aggregation for the latest subscription period. If none of the `start`, `end`, or `period` parameters is provided, records are returned for the latest subscription period.",
        "tags": ["Usage"],
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
                "in": "path",
                "required": True,
                "description": "The unique identifier for the subscription.",
                "schema": {"type": "string"}
            },
            {
                "name": "period",
                "in": "query",
                "description": "Limits the usage data returned to the subscription period provided. This option is incompatible with the `start` and `end` parameters.",
                "schema": {"type": "integer", "minimum": 1}
            },
            {
                "name": "start",
                "in": "query",
                "description": "Limits the usage data to dates greater than or equal to the provided date. Can only be used in combination with `end`.",
                "schema": {"type": "string"}
            },
            {
                "name": "end",
                "in": "query",
                "description": "Limits the usage data to dates up to and including the provided date. Can only be used in combination with `start`.",
                "schema": {"type": "string"}
            },
            {
                "name": "aggregation",
                "in": "query",
                "description": "Determines the aggregation method used, defaulting to `daily`. `period` provides aggregated values for the time range or period requested. The `roaming` aggregation is in preview and may only be used in particular cases.",
                "schema": {
                    "type": "string",
                    "enum": ["daily", "period", "country", "roaming", "daily,country", "daily,roaming", "period,country", "period,roaming", "country,daily", "country,period", "roaming,daily", "roaming,period"]
                }
            }
        ],
        "responses": {
            "200": {
                "description": "Returns the list of usage records.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UsageRecordList"
                        }
                    }
                }
            },
            "redirects": {
                "description": "Error details",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/Error"
                        }
                    }
                }
            }
        }
    }
}

paths["/testing/projects/{project}/subscriptions/{subscription}/usage"] = {
    "post": {
        "summary": "Simulate subscription usage",
        "description": "Simulates usage on a subscription with a test SIM. Can be used to test usage notifications. Subscription must be in status \"active\".\n\n#### Preview\nThis endpoint is currently in preview and might change in the future.\nWe’re excited to hear your feedback and ideas. Please send an email to support@gigs.com to share your thoughts.",
        "tags": ["Usage"],
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
                "in": "path",
                "required": True,
                "description": "The unique identifier for the subscription.",
                "schema": {"type": "string"}
            }
        ],
        "requestBody": {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/SimulateUsage"
                    }
                }
            }
        },
        "responses": {
            "201": {
                "description": "Returns the relevant usage record.",
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UsageRecord"
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

schemas["UsageRecordList"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["list"]
        },
        "items": {
            "type": "array",
            "items": {
                "$ref": "#/components/schemas/UsageRecord"
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

schemas["UsageRecord"] = {
    "type": "object",
    "properties": {
        "object": {
            "type": "string",
            "enum": ["usageRecord"],
            "description": "Type of object is always `usageRecord`."
        },
        "data": {
            "type": "integer",
            "description": "Amount of data used in bytes."
        },
        "dataDeviceBytes": {
            "type": "integer",
            "description": "Amount of on-device data used in bytes."
        },
        "dataTetheringBytes": {
            "type": "integer",
            "description": "Amount of tethering data used in bytes."
        },
        "end": {
            "type": "string",
            "description": "Timestamp representing the exclusive upper bound of the aggregation period."
        },
        "labels": {
            "type": "object",
            "description": "An object containing optional metadata about the usage record.",
            "properties": {
                "country": {
                    "type": "string",
                    "description": "The ISO 3166-1 alpha-2 country code of the country in which the usage occurred."
                },
                "roaming": {
                    "type": "string",
                    "description": "The roaming mode the usage occurred in.",
                    "enum": ["none", "international", "domestic"]
                },
                "subscription": {
                    "type": "string",
                    "description": "The unique identifier for the subscription to which the usage is attributed."
                }
            }
        },
        "sms": {
            "type": "integer",
            "description": "Amount of SMS messages sent and received."
        },
        "smsInternationalMessages": {
            "type": "integer",
            "description": "Amount of SMS messages sent internationally."
        },
        "smsLocalMessages": {
            "type": "integer",
            "description": "Amount of SMS messages sent locally."
        },
        "start": {
            "type": "string",
            "description": "Timestamp representing the inclusive lower bound of the aggregation period."
        },
        "updatedAt": {
            "type": "string",
            "description": "The time at which the aggregation was last updated."
        },
        "voice": {
            "type": "integer",
            "description": "Amount of voice usage in seconds."
        },
        "voiceInternationalSeconds": {
            "type": "integer",
            "description": "Amount of international voice usage in seconds."
        },
        "voiceLocalSeconds": {
            "type": "integer",
            "description": "Amount of local voice usage in seconds."
        }
    }
}

schemas["SimulateUsage"] = {
    "type": "object",
    "properties": {
        "data": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of data used in bytes."
        },
        "dataDevice": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of on-device data used in bytes."
        },
        "dataTethering": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of tethering data used in bytes."
        },
        "voice": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of voice usage in seconds."
        },
        "voiceLocal": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of local voice usage in seconds."
        },
        "voiceInternational": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of international long distance voice usage in seconds."
        },
        "sms": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of SMS messages sent and received."
        },
        "smsLocal": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of local SMS messages sent and received."
        },
        "smsInternational": {
            "type": "integer",
            "nullable": True,
            "default": 0,
            "description": "Amount of international long distance SMS messages sent and received."
        },
        "subscriptionAddon": {
            "type": "string",
            "nullable": True,
            "description": "The unique identifier for the subscription addon to which the simulated usage should be attributed."
        },
        "country": {
            "type": "string",
            "nullable": True,
            "description": "The ISO 3166-1 alpha-2 country code to assign to the simulated usage."
        },
        "roaming": {
            "type": "string",
            "nullable": True,
            "default": "none",
            "enum": ["none", "international", "domestic"],
            "description": "The roaming mode to assign to the simulated usage."
        },
        "usageBalance": {
            "type": "string",
            "nullable": True,
            "description": "The Usage Balance id to assign the simulated usage to."
        },
        "usageBalanceAmount": {
            "type": "integer",
            "nullable": True,
            "description": "The amount of usage to attribute to the specified Usage Balance."
        }
    }
}

data["components"]["schemas"] = schemas

with open(openapi_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("openapi.json has been updated with usage endpoints and schemas.")
