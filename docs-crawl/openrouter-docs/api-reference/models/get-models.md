Source: https://openrouter.ai/docs/api-reference/models/get-models

List all models and their properties | OpenRouter | Documentation

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

List all models and their properties
====================================

Copy page

GET

https://openrouter.ai/api/v1/models

GET

/api/v1/models

cURL

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/models \ |
| 2 | -H "Authorization: Bearer <token>" |
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

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

categoryenumOptional

Filter models by use case category

Show 12 enum values

supported\_parametersstringOptional

use\_rssstringOptional

use\_rss\_chat\_linksstringOptional

### Response

Returns a list of models or RSS feed

datalist of objects

List of available models

Show 14 properties

### Errors

400

Bad Request Error

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/models/list-models-count)[#### List models filtered by user provider preferences, privacy settings, and guardrails

Next](/docs/api/api-reference/models/list-models-user)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)