import json
import os

openapi_path = 'c:/Users/saima/OneDrive/Desktop/fiverr/docs/api-reference/openapi.json'

with open(openapi_path, 'r', encoding='utf-8') as f:
    openapi = json.load(f)

# Ensure components and schemas exist
if 'components' not in openapi:
    openapi['components'] = {}
if 'schemas' not in openapi['components']:
    openapi['components']['schemas'] = {}

schemas = openapi['components']['schemas']
paths = openapi.get('paths', {})

# Add Schema
schemas['Voucher'] = {
  "type": "object",
  "properties": {
    "object": { "type": "string", "enum": ["voucher"], "description": "Type of object is always `voucher`." },
    "id": { "type": "string", "description": "Unique identifier for the voucher." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Time when the voucher was created." },
    "name": { "type": "string", "description": "The voucher's name." },
    "priceDiscount": {
      "type": "object",
      "nullable": True,
      "properties": {
        "amount": { "type": "integer", "description": "The discount amount in the currency's minor unit." },
        "currency": { "type": "string", "description": "Three-letter ISO 4217 currency code." }
      },
      "description": "The price amount of the discount applied via the voucher."
    },
    "priceDiscountPercentage": { "type": "number", "nullable": True, "description": "The percentage amount of the discount applied via the voucher." },
    "recurrence": {
      "type": "object",
      "properties": {
        "type": { "type": "string", "enum": ["once", "repeating", "forever"], "description": "Whether and how the voucher discount recurs." },
        "durationInMonths": { "type": "integer", "nullable": True, "description": "For how many months is the discount applied via the voucher." }
      },
      "description": "Details on whether and for how long the discounts applied via the voucher recur."
    },
    "redemptions": { "type": "integer", "description": "Number of times the voucher has been redeemed." },
    "retiredReason": { "type": "string", "nullable": True, "enum": ["manualAction", "expired", "maxRedemptionsReached", "unknown"], "description": "Label indicating the reason why the voucher is retired." },
    "status": { "type": "string", "enum": ["available", "retired"] }
  }
}

# --- Paths --- #

voucher_tags = ["Vouchers"]

paths['/projects/{project}/vouchers'] = {
  "get": {
    "summary": "List all vouchers",
    "description": "Returns a list of vouchers. The vouchers returned are sorted by creation date, with the most recently created vouchers appearing first.",
    "tags": voucher_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "status", "in": "query", "schema": { "type": "array", "items": { "type": "string" }, "default": ["available"] } },
      { "name": "code", "in": "query", "schema": { "type": "string" } },
      { "name": "after", "in": "query", "schema": { "type": "string" } },
      { "name": "before", "in": "query", "schema": { "type": "string" } },
      { "name": "limit", "in": "query", "schema": { "type": "integer", "default": 10 } }
    ],
    "responses": {
      "200": {
        "description": "Returns a list of vouchers.",
        "content": { "application/json": { "schema": { "type": "object", "properties": { "object": { "type": "string", "enum": ["list"] }, "items": { "type": "array", "items": { "$ref": "#/components/schemas/Voucher" } }, "moreItemsAfter": { "type": "string", "nullable": True }, "moreItemsBefore": { "type": "string", "nullable": True } } } } }
      }
    }
  },
  "post": {
    "summary": "Create a voucher",
    "description": "Creates a new voucher in the specified project.",
    "tags": voucher_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "required": ["name", "recurrence"],
            "properties": {
              "name": { "type": "string" },
              "priceDiscount": { "type": "object", "nullable": True, "properties": { "amount": { "type": "integer" }, "currency": { "type": "string" } } },
              "priceDiscountPercentage": { "type": "number", "nullable": True },
              "recurrence": { "type": "object", "required": ["type"], "properties": { "type": { "type": "string" }, "durationInMonths": { "type": "integer", "nullable": True } } }
            }
          }
        }
      }
    },
    "responses": {
      "201": { "description": "Returns the newly created voucher.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/Voucher" } } } }
    }
  }
}

paths['/projects/{project}/vouchers/{voucher}'] = {
  "get": {
    "summary": "Retrieve a voucher",
    "description": "Retrieves the details of an existing voucher.",
    "tags": voucher_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "voucher", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "responses": {
      "200": { "description": "Returns the voucher object.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/Voucher" } } } }
    }
  }
}

paths['/projects/{project}/vouchers/{voucher}/retire'] = {
  "post": {
    "summary": "Retire a voucher",
    "description": "Retires the voucher. This marks the voucher as no longer redeemable for new subscriptions.",
    "tags": voucher_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "voucher", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "responses": {
      "200": { "description": "Returns the voucher.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/Voucher" } } } }
    }
  }
}

openapi['paths'] = paths

with open(openapi_path, 'w', encoding='utf-8') as f:
    json.dump(openapi, f, indent=2)

print("OpenAPI updated for Vouchers!")
