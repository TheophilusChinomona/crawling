Source: https://openrouter.ai/docs/api-reference/api-keys/create-api-key

Create a new API key | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* API Guides

  + [Overview](/docs/api/reference/overview)
  + [Streaming](/docs/api/reference/streaming)
  + [Embeddings](/docs/api/reference/embeddings)
  + [Limits](/docs/api/reference/limits)
  + [Authentication](/docs/api/reference/authentication)
  + [Parameters](/docs/api/reference/parameters)
  + [Errors and Debugging](/docs/api/reference/errors-and-debugging)
  + Responses API
* API Reference

  + Responses
  + OAuth
  + Anthropic Messages
  + Analytics
  + Chat
  + Credits
  + Embeddings
  + Generations
  + Models
  + Endpoints
  + Providers
  + API Keys
  + Guardrails

Light

[API Reference](/docs/api/api-reference/responses/create-responses)[API Keys](/docs/api/api-reference/api-keys/list)

Create a new API key
====================

Copy page

POST

https://openrouter.ai/api/v1/keys

POST

/api/v1/keys

TypeScript

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/keys \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "name": "Analytics Service Key", |
| 6 | "limit": 150, |
| 7 | "limit_reset": "monthly", |
| 8 | "include_byok_in_limit": true, |
| 9 | "expires_at": "2028-06-30T23:59:59Z" |
| 10 | }' |
```

Try it

201Created

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "hash": "a3f5c9d8e7b4f2a1c6d8e9f0b7a3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1", |
| 4 | "name": "Analytics Service Key", |
| 5 | "label": "sk-or-v1-analytics-3f5c9d8e", |
| 6 | "disabled": false, |
| 7 | "limit": 150, |
| 8 | "limit_remaining": 150, |
| 9 | "limit_reset": "monthly", |
| 10 | "include_byok_in_limit": true, |
| 11 | "usage": 0, |
| 12 | "usage_daily": 0, |
| 13 | "usage_weekly": 0, |
| 14 | "usage_monthly": 0, |
| 15 | "byok_usage": 0, |
| 16 | "byok_usage_daily": 0, |
| 17 | "byok_usage_weekly": 0, |
| 18 | "byok_usage_monthly": 0, |
| 19 | "created_at": "2026-04-01T09:00:00Z", |
| 20 | "expires_at": "2028-06-30T23:59:59Z" |
| 21 | }, |
| 22 | "key": "sk-or-v1-analytics-3f5c9d8e7b4f2a1c6d8e9f0b7a3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1" |
| 23 | } |
```

Create a new API key for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

namestringRequired`>=1 character`

Name for the new API key

limitdouble or nullOptional

Optional spending limit for the API key in USD

limit\_resetenum or nullOptional

Type of limit reset for the API key (daily, weekly, monthly, or null for no reset). Resets happen automatically at midnight UTC, and weeks are Monday through Sunday.

Allowed values:dailyweeklymonthly

include\_byok\_in\_limitbooleanOptional

Whether to include BYOK usage in the limit

expires\_atdatetime or nullOptional

Optional ISO 8601 UTC timestamp when the API key should expire. Must be UTC, other timezones will be rejected

### Response

API key created successfully

dataobject

The created API key information

Show 19 properties

keystring

The actual API key string (only shown once)

### Errors

400

Bad Request Error

401

Unauthorized Error

429

Too Many Requests Error

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/api-keys/list)[#### Get a single API key

Next](/docs/api/api-reference/api-keys/get-key)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)