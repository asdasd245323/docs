import json
import os

openapi_path = 'api-reference/openapi.json'

with open(openapi_path, 'r', encoding='utf-8') as f:
    openapi = json.load(f)

# Ensure components and schemas exist
if 'components' not in openapi:
    openapi['components'] = {}
if 'schemas' not in openapi['components']:
    openapi['components']['schemas'] = {}

schemas = openapi['components']['schemas']
paths = openapi.get('paths', {})

# Add Schemas
schemas['Price'] = {
  "type": "object",
  "properties": {
    "amount": {
      "type": "integer",
      "description": "The price amount in the currency's minor unit, e.g. 'cents' for many currencies."
    },
    "currency": {
      "type": "string",
      "description": "Three-letter ISO 4217 currency code. Must be a supported currency."
    }
  }
}

schemas['CreditNote'] = {
  "type": "object",
  "properties": {
    "object": { "type": "string", "enum": ["creditNote"], "description": "Type of object is always `creditNote`." },
    "id": { "type": "string", "description": "Unique identifier for the credit note." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Time when the credit note was created." },
    "creditTo": { "type": "string", "enum": ["outOfBand", "userBalance"], "description": "Specifies where the credit amount should be credited to." },
    "fees": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "amount": { "$ref": "#/components/schemas/Price" },
          "name": { "type": "string", "description": "The name of the fee." },
          "type": { "type": "string", "enum": ["recoveryFee"], "description": "The type of the fee." }
        }
      },
      "description": "The credited fees."
    },
    "fileUrl": { "type": ["string", "null"], "description": "A signed URL to download the credit note PDF file." },
    "invoice": { "type": "string", "description": "The unique identifier for the invoice that the credit note applies to." },
    "lineItems": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "amount": { "$ref": "#/components/schemas/Price" },
          "invoiceLineItem": { "type": "string" },
          "tax": { "$ref": "#/components/schemas/Price" },
          "taxes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "amount": { "$ref": "#/components/schemas/Price" },
                "invoiceTax": { "type": "string" }
              }
            }
          },
          "total": { "$ref": "#/components/schemas/Price" }
        }
      },
      "description": "The line items for the credit note."
    },
    "status": { "type": "string", "enum": ["issued", "voided"], "description": "The status of the credit note." },
    "subtotal": { "$ref": "#/components/schemas/Price", "description": "The total amount credited before any taxes or fees." },
    "tax": { "$ref": "#/components/schemas/Price", "description": "The sum of the amounts in taxes credited for each line item." },
    "total": { "$ref": "#/components/schemas/Price", "description": "The total amount credited after taxes and fees." },
    "voidedAt": { "type": ["string", "null"], "format": "date-time", "description": "Time when the credit note was voided." }
  }
}

schemas['Invoice'] = {
  "type": "object",
  "properties": {
    "object": { "type": "string", "enum": ["invoice"], "description": "Type of object is always `invoice`." },
    "id": { "type": "string", "description": "Unique identifier for the invoice." },
    "address": { "type": ["string", "null"], "description": "The unique identifier for the address this invoice relates to." },
    "appliedBalance": { "$ref": "#/components/schemas/Price", "description": "The amount of user balance applied to pay this invoice." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Time when the invoice was created." },
    "discount": { "$ref": "#/components/schemas/Price", "description": "The total discount applied. This is the sum of the discounts of each line item." },
    "dueAt": { "type": ["string", "null"], "format": "date-time", "description": "Time when the invoice is due to be paid." },
    "fees": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "amount": { "$ref": "#/components/schemas/Price" },
          "name": { "type": "string" },
          "type": { "type": "string", "enum": ["recoveryFee"] }
        }
      },
      "description": "The fees for the invoice."
    },
    "fileUrl": { "type": ["string", "null"], "description": "A signed URL to download the invoice PDF file." },
    "finalizedAt": { "type": ["string", "null"], "format": "date-time", "description": "Time when the invoice was finalized and could no longer be changed." },
    "lineItems": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "object": { "type": "string", "enum": ["invoiceLineItem"] },
          "id": { "type": "string" },
          "addon": { "type": ["string", "null"] },
          "creditedPlan": { "type": ["string", "null"] },
          "discount": { "$ref": "#/components/schemas/Price" },
          "plan": { "type": ["string", "null"] },
          "subscription": { "type": ["string", "null"] },
          "subscriptionAddon": { "type": ["string", "null"] },
          "subscriptionChange": { "type": ["string", "null"] },
          "subtotal": { "$ref": "#/components/schemas/Price" },
          "tax": { "$ref": "#/components/schemas/Price" },
          "taxes": { "type": "array", "items": { "type": "object", "properties": { "object": { "type": "string", "enum": ["invoiceTax"] }, "id": { "type": "string" }, "amount": { "$ref": "#/components/schemas/Price" }, "inclusive": { "type": "boolean" }, "jurisdiction": { "type": "string" }, "name": { "type": "string" } } } },
          "total": { "$ref": "#/components/schemas/Price" }
        }
      },
      "description": "The line items that make up the invoice."
    },
    "overdueAt": { "type": ["string", "null"], "format": "date-time", "description": "Time when the invoice is considered overdue." },
    "paidAt": { "type": ["string", "null"], "format": "date-time", "description": "Time when the invoice was paid." },
    "payment": { "type": ["string", "null"], "description": "The unique identifier for the payment associated with the invoice, if any." },
    "period": {
      "type": ["object", "null"],
      "properties": {
        "number": { "type": "integer" },
        "start": { "type": "string", "format": "date-time" },
        "end": { "type": "string", "format": "date-time" }
      },
      "description": "The subscription period that this invoice relates to."
    },
    "reason": { "type": "string", "enum": ["subscriptionCreation", "subscriptionRenewal", "subscriptionChange", "subscriptionRestore", "other"] },
    "status": { "type": "string", "enum": ["draft", "finalized", "paid", "voided"] },
    "subscription": { "type": "string" },
    "subtotal": { "$ref": "#/components/schemas/Price" },
    "tax": { "$ref": "#/components/schemas/Price" },
    "taxExemptionReason": { "type": ["string", "null"], "enum": ["calculationFailed", "fullyDiscounted", "inclusiveTaxExceedsPrice", "userExempted"] },
    "total": { "$ref": "#/components/schemas/Price" },
    "voucher": { "type": ["string", "null"] }
  }
}

schemas['Quote'] = {
  "type": "object",
  "properties": {
    "object": { "type": "string", "enum": ["quote"] },
    "id": { "type": "string", "description": "Unique identifier for the quote." },
    "address": { "type": ["string", "null"] },
    "createdAt": { "type": "string", "format": "date-time" },
    "discount": { "$ref": "#/components/schemas/Price" },
    "expiredAt": { "type": "string", "format": "date-time" },
    "fees": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "amount": { "$ref": "#/components/schemas/Price" },
          "name": { "type": "string" },
          "type": { "type": "string" }
        }
      }
    },
    "lineItems": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "addon": { "type": ["string", "null"] },
          "creditedPlan": { "type": ["string", "null"] },
          "discount": { "$ref": "#/components/schemas/Price" },
          "plan": { "type": ["string", "null"] },
          "subtotal": { "$ref": "#/components/schemas/Price" },
          "tax": { "$ref": "#/components/schemas/Price" },
          "taxes": {
            "type": "array",
            "items": { "type": "object", "properties": { "amount": { "$ref": "#/components/schemas/Price" }, "inclusive": { "type": "boolean" }, "jurisdiction": { "type": "string" }, "name": { "type": "string" } } }
          },
          "total": { "$ref": "#/components/schemas/Price" }
        }
      }
    },
    "reason": { "type": "string", "enum": ["subscriptionCreation", "subscriptionChange", "other"] },
    "subtotal": { "$ref": "#/components/schemas/Price" },
    "tax": { "$ref": "#/components/schemas/Price" },
    "taxExemptionReason": { "type": ["string", "null"], "enum": ["calculationFailed", "inclusiveTaxExceedsPrice", "fullyDiscounted", "userExempted"] },
    "total": { "$ref": "#/components/schemas/Price" },
    "user": { "type": "string" },
    "voucher": { "type": ["string", "null"] }
  }
}

# --- Paths --- #

credit_note_tags = ["Credit Notes"]
invoice_tags = ["Invoices"]
quote_tags = ["Quotes"]

# Credit Notes
paths['/projects/{project}/creditNotes'] = {
  "get": {
    "summary": "List all credit notes",
    "description": "Returns a list of credit notes.",
    "tags": credit_note_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "after", "in": "query", "schema": { "type": "string" } },
      { "name": "before", "in": "query", "schema": { "type": "string" } },
      { "name": "limit", "in": "query", "schema": { "type": "integer", "default": 10 } },
      { "name": "invoice", "in": "query", "schema": { "type": "string" } },
      { "name": "status", "in": "query", "schema": { "type": "array", "items": { "type": "string" } } }
    ],
    "responses": {
      "200": {
        "description": "Returns a list of credit notes.",
        "content": { "application/json": { "schema": { "type": "object", "properties": { "object": { "type": "string", "enum": ["list"] }, "items": { "type": "array", "items": { "$ref": "#/components/schemas/CreditNote" } }, "moreItemsAfter": { "type": ["string", "null"] }, "moreItemsBefore": { "type": ["string", "null"] } } } } }
      }
    }
  },
  "post": {
    "summary": "Create a credit note",
    "description": "Creates a new credit note for an invoice.",
    "tags": credit_note_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "required": ["invoice"],
            "properties": {
              "invoice": { "type": "string" },
              "lineItems": {
                "type": ["array", "null"],
                "items": { "type": "object", "properties": { "invoiceLineItem": { "type": "string" }, "amount": { "type": ["integer", "null"] }, "taxes": { "type": "array", "items": { "type": "object", "properties": { "invoiceTax": { "type": "string" }, "amount": { "type": ["integer", "null"] } } } } } }
              },
              "fees": {
                "type": ["array", "null"],
                "items": { "type": "object", "properties": { "type": { "type": "string" }, "amount": { "type": "integer" } } }
              }
            }
          }
        }
      }
    },
    "responses": {
      "201": { "description": "Returns the created credit note.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/CreditNote" } } } }
    }
  }
}

paths['/projects/{project}/creditNotes/{creditNote}'] = {
  "get": {
    "summary": "Retrieve a credit note",
    "description": "Retrieves the details of an existing credit note.",
    "tags": credit_note_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "creditNote", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "responses": {
      "200": { "description": "Returns the credit note.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/CreditNote" } } } }
    }
  }
}

paths['/projects/{project}/creditNotes/{creditNote}/void'] = {
  "post": {
    "summary": "Void a credit note",
    "description": "Marks the credit note as void.",
    "tags": credit_note_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "creditNote", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "responses": {
      "200": { "description": "Returns the voided credit note.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/CreditNote" } } } }
    }
  }
}

# Invoices
paths['/projects/{project}/invoices'] = {
  "get": {
    "summary": "List all invoices",
    "description": "Returns a list of invoices.",
    "tags": invoice_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "after", "in": "query", "schema": { "type": "string" } },
      { "name": "before", "in": "query", "schema": { "type": "string" } },
      { "name": "limit", "in": "query", "schema": { "type": "integer", "default": 10 } },
      { "name": "user", "in": "query", "schema": { "type": "string" } },
      { "name": "subscription", "in": "query", "schema": { "type": "string" } },
      { "name": "subscriptionAddon", "in": "query", "schema": { "type": "string" } },
      { "name": "subscriptionChange", "in": "query", "schema": { "type": "string" } },
      { "name": "status", "in": "query", "schema": { "type": "array", "items": { "type": "string" } } },
      { "name": "reason", "in": "query", "schema": { "type": "array", "items": { "type": "string" } } }
    ],
    "responses": {
      "200": {
        "description": "Returns a list of invoices.",
        "content": { "application/json": { "schema": { "type": "object", "properties": { "object": { "type": "string", "enum": ["list"] }, "items": { "type": "array", "items": { "$ref": "#/components/schemas/Invoice" } }, "moreItemsAfter": { "type": ["string", "null"] }, "moreItemsBefore": { "type": ["string", "null"] } } } } }
      }
    }
  }
}

paths['/projects/{project}/invoices/{invoice}'] = {
  "get": {
    "summary": "Retrieve an invoice",
    "description": "Retrieves the details of an existing invoice.",
    "tags": invoice_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "invoice", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "responses": {
      "200": { "description": "Returns the invoice.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/Invoice" } } } }
    }
  }
}

paths['/projects/{project}/invoices/{invoice}/pay'] = {
  "post": {
    "summary": "Pay an invoice",
    "description": "Marks the invoice as paid.",
    "tags": invoice_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "invoice", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "responses": {
      "200": { "description": "Returns the invoice.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/Invoice" } } } }
    }
  }
}

# Quotes
paths['/projects/{project}/quotes'] = {
  "post": {
    "summary": "Create a quote",
    "description": "Creates a quote for the given plan or add-on.",
    "tags": quote_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "requestBody": {
      "required": True,
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "required": ["user"],
            "properties": {
              "addon": { "type": ["string", "null"] },
              "address": { "type": ["string", "null"] },
              "creditedPlan": { "type": ["string", "null"] },
              "plan": { "type": ["string", "null"] },
              "user": { "type": "string" },
              "voucher": { "type": ["string", "null"] }
            }
          }
        }
      }
    },
    "responses": {
      "200": { "description": "Returns the created quote.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/Quote" } } } }
    }
  }
}

paths['/projects/{project}/quotes/{quote}'] = {
  "get": {
    "summary": "Retrieve a quote",
    "description": "Retrieves the details of an existing quote.",
    "tags": quote_tags,
    "parameters": [
      { "name": "project", "in": "path", "required": True, "schema": { "type": "string" } },
      { "name": "quote", "in": "path", "required": True, "schema": { "type": "string" } }
    ],
    "responses": {
      "200": { "description": "Returns the quote.", "content": { "application/json": { "schema": { "$ref": "#/components/schemas/Quote" } } } }
    }
  }
}

openapi['paths'] = paths

with open(openapi_path, 'w', encoding='utf-8') as f:
    json.dump(openapi, f, indent=2)

print("OpenAPI updated!")
