Source: https://openrouter.ai/docs/api/api-reference/models/list-models-user

List models filtered by user provider preferences, privacy settings, and guardrails | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[Models](/docs/api/api-reference/models/list-models-count)

List models filtered by user provider preferences, privacy settings, and guardrails
===================================================================================

Copy page

GET

https://openrouter.ai/api/v1/models/user

GET

/api/v1/models/user

Python

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 |  |
| 3 | url = "https://openrouter.ai/api/v1/models/user" |
| 4 |  |
| 5 | headers = {"Authorization": "Bearer <token>"} |
| 6 |  |
| 7 | response = requests.get(url, headers=headers) |
| 8 |  |
| 9 | print(response.json()) |
```

Try it

200Retrieved

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "id": "openai/gpt-4", |
| 5 | "canonical_slug": "openai/gpt-4", |
| 6 | "name": "GPT-4", |
| 7 | "created": 1692901234, |
| 8 | "pricing": { |
| 9 | "prompt": "0.00003", |
| 10 | "completion": "0.00006", |
| 11 | "request": "0", |
| 12 | "image": "0" |
| 13 | }, |
| 14 | "context_length": 8192, |
| 15 | "architecture": { |
| 16 | "modality": "text->text", |
| 17 | "input_modalities": [ |
| 18 | "text" |
| 19 | ], |
| 20 | "output_modalities": [ |
| 21 | "text" |
| 22 | ], |
| 23 | "tokenizer": "GPT", |
| 24 | "instruct_type": "chatml" |
| 25 | }, |
| 26 | "top_provider": { |
| 27 | "is_moderated": true, |
| 28 | "context_length": 8192, |
| 29 | "max_completion_tokens": 4096 |
| 30 | }, |
| 31 | "supported_parameters": [ |
| 32 | "temperature", |
| 33 | "top_p", |
| 34 | "max_tokens", |
| 35 | "frequency_penalty", |
| 36 | "presence_penalty" |
| 37 | ], |
| 38 | "description": "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy." |
| 39 | } |
| 40 | ] |
| 41 | } |
```

List models filtered by user provider preferences, [privacy settings](https://openrouter.ai/docs/guides/privacy/logging), and [guardrails](https://openrouter.ai/docs/guides/features/guardrails). If requesting through `eu.openrouter.ai/api/v1/...` the results will be filtered to models that satisfy [EU in-region routing](https://openrouter.ai/docs/guides/privacy/logging#enterprise-eu-in-region-routing).

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Response

Returns a list of models filtered by user provider preferences

datalist of objects

List of available models

Show 14 properties

### Errors

401

Unauthorized Error

404

Not Found Error

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/models/get-models)[#### List all endpoints for a model

Next](/docs/api/api-reference/endpoints/list-endpoints)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

List models filtered by user provider preferences, [privacy settings](https://openrouter.ai/docs/guides/privacy/logging), and [guardrails](https://openrouter.ai/docs/guides/features/guardrails). If requesting through `eu.openrouter.ai/api/v1/...` the results will be filtered to models that satisfy [EU in-region routing](https://openrouter.ai/docs/guides/privacy/logging#enterprise-eu-in-region-routing).