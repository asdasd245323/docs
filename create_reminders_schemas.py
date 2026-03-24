import os

base_dir = "c:/Users/saima/OneDrive/Desktop/fiverr/docs/api/gigs-reminders/schemas/"
os.makedirs(base_dir, exist_ok=True)

reminders = [
    "com.gigs.reminder.porting.declined",
    "com.gigs.reminder.porting.informationRequired",
    "com.gigs.reminder.porting.requested",
    "com.gigs.reminder.porting.scheduled",
    "com.gigs.reminder.subscription.simNotInstalled",
    "com.gigs.reminder.subscription.usageMissing"
]

for reminder in reminders:
    title = reminder
    filename = reminder + ".mdx"
    schema_name = reminder
    content = f'---\ntitle: "{title}"\nopenapi-schema: "{schema_name}"\n---\n'
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

print("Created MDX files for Gigs Reminders schemas!")
