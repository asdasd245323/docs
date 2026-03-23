import os

base_dir = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/api/gigs-billing"

files_to_create = {
    "credit-notes/list-all-credit-notes.mdx": '---\ntitle: "List all credit notes"\nopenapi: "GET /projects/{project}/creditNotes"\n---',
    "credit-notes/create-a-credit-note.mdx": '---\ntitle: "Create a credit note"\nopenapi: "POST /projects/{project}/creditNotes"\n---',
    "credit-notes/retrieve-a-credit-note.mdx": '---\ntitle: "Retrieve a credit note"\nopenapi: "GET /projects/{project}/creditNotes/{creditNote}"\n---',
    "credit-notes/void-a-credit-note.mdx": '---\ntitle: "Void a credit note"\nopenapi: "POST /projects/{project}/creditNotes/{creditNote}/void"\n---',
    "invoices/list-all-invoices.mdx": '---\ntitle: "List all invoices"\nopenapi: "GET /projects/{project}/invoices"\n---',
    "invoices/retrieve-an-invoice.mdx": '---\ntitle: "Retrieve an invoice"\nopenapi: "GET /projects/{project}/invoices/{invoice}"\n---',
    "invoices/pay-an-invoice.mdx": '---\ntitle: "Pay an invoice"\nopenapi: "POST /projects/{project}/invoices/{invoice}/pay"\n---',
    "quotes/create-a-quote.mdx": '---\ntitle: "Create a quote"\nopenapi: "POST /projects/{project}/quotes"\n---',
    "quotes/retrieve-a-quote.mdx": '---\ntitle: "Retrieve a quote"\nopenapi: "GET /projects/{project}/quotes/{quote}"\n---',
    "schemas/credit-note.mdx": '---\ntitle: "CreditNote"\nopenapi-schema: "CreditNote"\n---',
    "schemas/invoice.mdx": '---\ntitle: "Invoice"\nopenapi-schema: "Invoice"\n---',
    "schemas/quote.mdx": '---\ntitle: "Quote"\nopenapi-schema: "Quote"\n---',
}

for path, content in files_to_create.items():
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Files created successfully.")
