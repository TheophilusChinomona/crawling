Source: https://openrouter.ai/docs/api/api-reference/guardrails/create-guardrail

Create a guardrail | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[Guardrails](/docs/api/api-reference/guardrails/list-guardrails)

Create a guardrail
==================

Copy page

POST

https://openrouter.ai/api/v1/guardrails

POST

/api/v1/guardrails

TypeScript

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/guardrails \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "name": "My New Guardrail", |
| 6 | "description": "A guardrail for limiting API usage", |
| 7 | "limit_usd": 50, |
| 8 | "reset_interval": "monthly", |
| 9 | "allowed_providers": [ |
| 10 | "openai", |
| 11 | "anthropic", |
| 12 | "deepseek" |
| 13 | ], |
| 14 | "enforce_zdr": false |
| 15 | }' |
```

Try it

201Created

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "id": "550e8400-e29b-41d4-a716-446655440000", |
| 4 | "name": "My New Guardrail", |
| 5 | "created_at": "2025-08-24T10:30:00Z", |
| 6 | "description": "A guardrail for limiting API usage", |
| 7 | "limit_usd": 50, |
| 8 | "reset_interval": "monthly", |
| 9 | "allowed_providers": [ |
| 10 | "openai", |
| 11 | "anthropic", |
| 12 | "google" |
| 13 | ], |
| 14 | "enforce_zdr": false |
| 15 | } |
| 16 | } |
```

Create a new guardrail for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

namestringRequired`1-200 characters`

Name for the new guardrail

descriptionstring or nullOptional`<=1000 characters`

Description of the guardrail

limit\_usddouble or nullOptional`>=0`

Spending limit in USD

reset\_intervalenum or nullOptional

Interval at which the limit resets (daily, weekly, monthly)

Allowed values:dailyweeklymonthly

allowed\_providerslist of strings or nullOptional

List of allowed provider IDs

allowed\_modelslist of strings or nullOptional

Array of model identifiers (slug or canonical\_slug accepted)

enforce\_zdrboolean or nullOptional

Whether to enforce zero data retention

### Response

Guardrail created successfully

dataobject

The created guardrail

Show 10 properties

### Errors

400

Bad Request Error

401

Unauthorized Error

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/guardrails/list-guardrails)[#### Get a guardrail

Next](/docs/api/api-reference/guardrails/get-guardrail)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)