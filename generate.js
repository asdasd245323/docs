const fs = require('fs');
const path = require('path');

const outDir = 'c:\\Users\\saima\\OneDrive\\Desktop\\fiverr\\docs\\api\\gigs-events\\schemas';

// Shared rich examples
const subscriptionExample = {
  "object": "subscription",
  "id": "sub_0SNlurA049MEWV2gSfSxi00xlPIi",
  "metadata": {},
  "activatedAt": "2021-01-21T19:38:34Z",
  "billing": {
    "discount": {
      "voucher": "vou_0SNlurA049MEWV0h2jfjkdiOdplN",
      "expiresAt": "2021-02-20T19:38:34Z"
    },
    "invoiceGracePeriodDays": 3,
    "invoiceOverduePeriodDays": 1,
    "invoiceOverdueAction": null,
    "restrictBehavior": null,
    "restoreBehavior": null
  },
  "canceledAt": "2021-01-29T13:22:51Z",
  "cancellationDetails": {
    "cause": "cancellationRequested",
    "userComment": "",
    "userReason": "connectivityIssues"
  },
  "createdAt": "2021-01-21T19:32:13.0Z",
  "currentPeriod": {
    "number": 1,
    "start": "2021-01-21T19:32:13.0Z",
    "end": "2021-02-20T19:38:34.0Z"
  },
  "earliestEndAt": "2021-02-20T19:38:34Z",
  "endedAt": "2021-02-20T19:38:34Z",
  "firstUsageAt": "2021-01-21T19:38:34Z",
  "phoneNumber": "+19591234567",
  "plan": {
    "object": "plan",
    "id": "pln_0SNlurA049MEWV3V0q7gjQbM4EVo",
    "name": "Gigs Global",
    "status": "available",
    "price": {
      "amount": 999,
      "currency": "USD"
    }
  },
  "restrictedAt": "2021-02-21T19:38:34Z",
  "restrictionDetails": {
    "restrictBehavior": "incomingOnly",
    "restoreBehavior": "resetPeriodAnchor",
    "cause": "invoiceOverdue"
  },
  "sim": {
    "object": "sim",
    "id": "sim_0SNlurA049MEWV1BAAmWZULA4lf6",
    "metadata": {},
    "createdAt": "2021-01-21T19:38:34.0Z",
    "iccid": "89883070000007537119",
    "provider": "p9",
    "status": "inactive",
    "type": "eSIM"
  },
  "status": "active",
  "user": {
    "object": "user",
    "id": "usr_0SNlurA049MEWV4OpCwsNyC9Kn2d",
    "metadata": {},
    "birthday": "2017-07-21",
    "createdAt": "2021-01-21T19:38:34.0Z",
    "email": "jerry@example.com",
    "emailVerified": true,
    "fullName": "Jerry Seinfeld",
    "preferredLocale": "en-US",
    "status": "active"
  },
  "userAddress": "adr_0SNlurA049MEWV5ELDmnaqVXgTFT"
};

const subscriptionAddonExample = {
  "object": "subscriptionAddon",
  "id": "sad_0SNlurA049MEWV2gSfSxi",
  "metadata": {},
  "addon": {
    "object": "addon",
    "id": "add_0SNlurA049MEWV3V0q7gj",
    "name": "International Roaming",
    "status": "published",
    "price": {
      "amount": 499,
      "currency": "USD"
    },
    "validity": {
      "type": "recurring",
      "unit": "day",
      "value": 30
    }
  },
  "activatedAt": "2021-01-21T19:38:34Z",
  "canceledAt": null,
  "createdAt": "2021-01-21T19:32:13.0Z",
  "currentPeriod": {
    "number": 1,
    "start": "2021-01-21T19:32:13.0Z",
    "end": "2021-02-20T19:38:34.0Z"
  },
  "endedAt": null,
  "status": "active",
  "subscription": "sub_0SNlurA049MEWV2gSfSxi00xlPIi"
};

const subscriptionChangeExample = {
  "object": "subscriptionChange",
  "id": "sch_0SNlurA049MEWV2gSfSxi",
  "metadata": {},
  "createdAt": "2021-01-21T19:32:13.0Z",
  "currentPlan": {
    "object": "plan",
    "id": "pln_0SNlurA049MEWV3V0q7gjQbM4EVo",
    "name": "Gigs Global",
    "status": "available",
    "price": {
      "amount": 999,
      "currency": "USD"
    }
  },
  "effectiveAt": "2021-02-20T19:38:34Z",
  "newPlan": {
    "object": "plan",
    "id": "pln_0SNlurA049MEWV3V0q7gjQbM4EVp",
    "name": "Gigs Premium",
    "status": "available",
    "price": {
      "amount": 1999,
      "currency": "USD"
    }
  },
  "phase": "scheduled",
  "status": "pending",
  "subscription": "sub_0SNlurA049MEWV2gSfSxi00xlPIi",
  "user": "usr_0SNlurA049MEWV4OpCwsNyC9Kn2d"
};

// Descriptions per action
const actionDescriptions = {
  subscription: {
    activated: "Fired when a subscription has been activated and connectivity is now enabled for the user.",
    canceled: "Fired when a subscription has been canceled. The subscription will remain active until the end of the current period.",
    created: "Fired when a new subscription has been created.",
    ended: "Fired when a subscription has ended and connectivity is no longer provided.",
    renewed: "Fired when a subscription has been renewed for a new billing period.",
    restored: "Fired when a previously restricted subscription has been restored to full service.",
    restricted: "Fired when a subscription has been restricted, limiting connectivity based on the configured behavior.",
    resumed: "Fired when a paused subscription has been resumed.",
    updated: "Fired when one or more fields on a subscription have been updated."
  },
  subscriptionAddon: {
    activated: "Fired when a subscription add-on has been activated.",
    created: "Fired when a new subscription add-on has been created and attached to a subscription.",
    ended: "Fired when a subscription add-on has ended.",
    renewed: "Fired when a subscription add-on has been renewed for a new billing period.",
    updated: "Fired when one or more fields on a subscription add-on have been updated."
  },
  subscriptionChange: {
    activated: "Fired when a pending subscription change has been activated and applied.",
    canceled: "Fired when a scheduled subscription change has been canceled before taking effect.",
    created: "Fired when a new subscription change has been created.",
    failed: "Fired when a subscription change has failed and could not be applied.",
    processing: "Fired when a subscription change is currently being processed.",
    updated: "Fired when one or more fields on a subscription change have been updated."
  }
};

const schemaDescriptions = {
  Subscription: "Subscriptions are tied to a user and are created once a user has a plan and SIM. This allows connectivity for their device and SIM.",
  SubscriptionAddon: "A subscription add-on represents an additional feature or service attached to a subscription.",
  SubscriptionChange: "A subscription change represents a pending or applied plan modification for an existing subscription."
};

const schemaExamples = {
  Subscription: subscriptionExample,
  SubscriptionAddon: subscriptionAddonExample,
  SubscriptionChange: subscriptionChangeExample
};

const events = [
  'com.gigs.subscription.activated',
  'com.gigs.subscription.canceled',
  'com.gigs.subscription.created',
  'com.gigs.subscription.ended',
  'com.gigs.subscription.renewed',
  'com.gigs.subscription.restored',
  'com.gigs.subscription.restricted',
  'com.gigs.subscription.resumed',
  'com.gigs.subscription.updated',
  'com.gigs.subscriptionAddon.activated',
  'com.gigs.subscriptionAddon.created',
  'com.gigs.subscriptionAddon.ended',
  'com.gigs.subscriptionAddon.renewed',
  'com.gigs.subscriptionAddon.updated',
  'com.gigs.subscriptionChange.activated',
  'com.gigs.subscriptionChange.canceled',
  'com.gigs.subscriptionChange.created',
  'com.gigs.subscriptionChange.failed',
  'com.gigs.subscriptionChange.processing',
  'com.gigs.subscriptionChange.updated'
];

function indentJson(jsonStr, spaces) {
  const pad = ' '.repeat(spaces);
  return jsonStr.split('\n').map((line, i) => i === 0 ? line : pad + line).join('\n');
}

function generateMdx(eventName) {
  const parts = eventName.split('.');
  const resourceType = parts[2]; // 'subscription', 'subscriptionAddon', 'subscriptionChange'
  const action = parts[3];
  const isUpdated = action === 'updated';

  const schemaName = resourceType === 'subscription' ? 'Subscription' :
                     resourceType === 'subscriptionAddon' ? 'SubscriptionAddon' : 'SubscriptionChange';

  const schemaDescription = schemaDescriptions[schemaName];
  const example = schemaExamples[schemaName];
  const eventDescription = (actionDescriptions[resourceType] || {})[action] ||
    `Fired when a ${resourceType} is ${action}.`;

  // Build the full event JSON
  const eventObj = {
    object: "event",
    id: "evt_0SNlurA049MEWV5gNTcQ5A07h3Ol",
    actor: {
      type: "user",
      user: "usr_0SNlurA049MEWV4OpCwsNyC9Kn2d"
    },
    data: example,
    datacontenttype: "application/json",
    project: "gigs",
    source: "https://api.gigs.com",
    specversion: "1.0",
    time: "2022-03-16T14:12:42.0Z",
    type: eventName,
    version: "2026-01-29"
  };

  if (isUpdated) {
    // Insert previousData after datacontenttype
    const ordered = {};
    for (const [k, v] of Object.entries(eventObj)) {
      ordered[k] = v;
      if (k === 'datacontenttype') ordered['previousData'] = {};
    }
    Object.assign(eventObj, ordered);
  }

  const jsonStr = JSON.stringify(eventObj, null, 2);

  let mdx = `---
title: "${eventName}"
description: "${eventDescription}"
---

<ResponseField name="object" type="string">
  Type of object is always \`event\`.

  Allowed values: \`event\`
</ResponseField>

<ResponseField name="id" type="string">
  Unique identifier for the event.

  Example: \`"evt_0SNlurA049MEWV5gNTcQ5A07h3Ol"\`
</ResponseField>

<ResponseField name="actor" type="Actor">
  <Expandable title="properties">
    <ResponseField name="type" type="string" />
    <ResponseField name="user" type="string" />
    <ResponseField name="apiKey" type="string" />
    <ResponseField name="member" type="string" />
  </Expandable>

  Example: \`{"type":"user","user":"usr_0SNlurA049MEWV4OpCwsNyC9Kn2d"},{"type":"apiKey","apiKey":"apk_0SNlurA049MEWV4wRq2ql6SYZxiY"},{"type":"member","member":"mbr_0SNlurA020zhzt0CwsIr53"},{"type":"system"}\`
</ResponseField>

<ResponseField name="data" type="${schemaName}">
  ${schemaDescription}
</ResponseField>

<ResponseField name="datacontenttype" type="string" default="application/json">
  The RFC 2046 content-type.

  Example: \`"application/json"\`
</ResponseField>
`;

  if (isUpdated) {
    mdx += `
<ResponseField name="previousData" type="object">
  Present only for events of type \`*.updated\`. Contains the values fields in
  the schema had prior to the update.

  This field is the result of a shallow diff of the previous schema (i.e., if
  a nested field has changed, then the entire object will be included).
</ResponseField>
`;
  }

  mdx += `
<ResponseField name="project" type="string">
  Unique identifier for the project where the event occurred.

  Example: \`"gigs"\`
</ResponseField>

<ResponseField name="source" type="string" default="https://api.gigs.com">
  URI identifying the event source.

  Example: \`"https://api.gigs.com"\`
</ResponseField>

<ResponseField name="specversion" type="string" default="1.0">
  The CloudEvents spec version.

  Example: \`"1.0"\`
</ResponseField>

<ResponseField name="time" type="string">
  Time when the event occurred.

  Example: \`"2022-03-16T14:12:42Z"\`
</ResponseField>

<ResponseField name="type" type="string">
  Type is always \`${eventName}\`.

  Allowed values: \`${eventName}\`
</ResponseField>

<ResponseField name="version" type="string" default="2026-01-29">
  API version used to serialize the data and the event itself.
</ResponseField>

<RequestExample>
\`\`\`json Example
${jsonStr}
\`\`\`
</RequestExample>
`;

  fs.writeFileSync(path.join(outDir, `${eventName}.mdx`), mdx, 'utf8');
  console.log(`✓ ${eventName}.mdx`);
}

events.forEach(generateMdx);
console.log('\nAll files generated successfully!');
