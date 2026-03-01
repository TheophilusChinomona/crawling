Source: https://openrouter.ai/docs/api/api-reference/responses/create-responses

Create a response | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[Responses](/docs/api/api-reference/responses/create-responses)

Create a response
=================

Copy page

POST

https://openrouter.ai/api/v1/responses

POST

/api/v1/responses

cURL

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/responses \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "input": [ |
| 6 | { |
| 7 | "type": "message", |
| 8 | "role": "user", |
| 9 | "content": "Hello, how are you?" |
| 10 | } |
| 11 | ], |
| 12 | "tools": [ |
| 13 | { |
| 14 | "type": "function", |
| 15 | "name": "get_current_weather", |
| 16 | "description": "Get the current weather in a given location", |
| 17 | "parameters": { |
| 18 | "type": "object", |
| 19 | "properties": { |
| 20 | "location": { |
| 21 | "type": "string" |
| 22 | } |
| 23 | } |
| 24 | } |
| 25 | } |
| 26 | ], |
| 27 | "model": "anthropic/claude-4.5-sonnet-20250929", |
| 28 | "temperature": 0.7, |
| 29 | "top_p": 0.9 |
| 30 | }' |
```

Try it

200Successful

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "completed_at": 1.1, |
| 3 | "created_at": 1704067200, |
| 4 | "frequency_penalty": 1.1, |
| 5 | "id": "resp-abc123", |
| 6 | "instructions": "string", |
| 7 | "model": "gpt-4", |
| 8 | "object": "response", |
| 9 | "parallel_tool_calls": true, |
| 10 | "presence_penalty": 1.1, |
| 11 | "status": "completed", |
| 12 | "tool_choice": "auto", |
| 13 | "tools": [], |
| 14 | "output": [ |
| 15 | { |
| 16 | "id": "msg-abc123", |
| 17 | "role": "assistant", |
| 18 | "type": "message", |
| 19 | "status": "completed", |
| 20 | "content": [ |
| 21 | { |
| 22 | "type": "output_text", |
| 23 | "text": "Hello! How can I help you today?", |
| 24 | "annotations": [] |
| 25 | } |
| 26 | ] |
| 27 | } |
| 28 | ], |
| 29 | "usage": { |
| 30 | "input_tokens": 10, |
| 31 | "input_tokens_details": { |
| 32 | "cached_tokens": 0 |
| 33 | }, |
| 34 | "output_tokens": 25, |
| 35 | "output_tokens_details": { |
| 36 | "reasoning_tokens": 0 |
| 37 | }, |
| 38 | "total_tokens": 35 |
| 39 | } |
| 40 | } |
```

Creates a streaming or non-streaming response using OpenResponses API format

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

inputstring or list of objectsOptional

Input for a response request - can be a string or array of items

Show 2 variants

instructionsstring or nullOptional

metadatamap from strings to stringsOptional

Metadata key-value pairs for the request. Keys must be ≤64 characters and cannot contain brackets. Values must be ≤512 characters. Maximum 16 pairs allowed.

toolslist of objectsOptional

Show 5 variants

tool\_choiceenum or objectOptional

Show 5 variants

parallel\_tool\_callsboolean or nullOptional

modelstringOptional

modelslist of stringsOptional

textobjectOptional

Text output configuration including format and verbosity

Show 2 properties

reasoningobjectOptional

Configuration for reasoning mode in the response

Show 4 properties

max\_output\_tokensdouble or nullOptional

temperaturedouble or nullOptional`0-2`

top\_pdouble or nullOptional`>=0`

top\_logprobsinteger or nullOptional`0-20`

max\_tool\_callsinteger or nullOptional

presence\_penaltydouble or nullOptional`-2-2`

frequency\_penaltydouble or nullOptional`-2-2`

top\_kdoubleOptional

image\_configmap from strings to strings or doublesOptional

Provider-specific image configuration options. Keys and values vary by model/provider. See <https://openrouter.ai/docs/features/multimodal/image-generation> for more details.

Show 2 variants

modalitieslist of enumsOptional

Output modalities for the response. Supported values are "text" and "image".

Allowed values:textimage

prompt\_cache\_keystring or nullOptional

previous\_response\_idstring or nullOptional

promptobjectOptional

Show 2 properties

includelist of enums or nullOptional

Allowed values:file\_search\_call.resultsmessage.input\_image.image\_urlcomputer\_call\_output.output.image\_urlreasoning.encrypted\_contentcode\_interpreter\_call.outputs

backgroundboolean or nullOptional

safety\_identifierstring or nullOptional

storefalseOptional

service\_tierenumOptionalDefaults to `auto`

Allowed values:auto

truncationobjectOptional

streambooleanOptionalDefaults to `false`

providerobject or nullOptional

When multiple model providers are available, optionally indicate your routing preference.

Show 13 properties

pluginslist of objectsOptional

Plugins you want to enable for this request, including their settings.

Show 5 variants

userstringOptional`<=128 characters`

A unique identifier representing your end-user, which helps distinguish between different users of your app. This allows your app to identify specific users in case of abuse reports, preventing your entire app from being affected by the actions of individual users. Maximum of 128 characters.

session\_idstringOptional`<=128 characters`

A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 128 characters.

traceobjectOptional

Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations.

Show 5 properties

### Response

Successful response

completed\_atdouble or null

created\_atdouble

errorobject

Error information returned from the API

Show 2 properties

frequency\_penaltydouble or null

idstring

incomplete\_detailsobject

Show 1 properties

instructionsstring or list of objects or any

Show 3 variants

metadatamap from strings to strings

Metadata key-value pairs for the request. Keys must be ≤64 characters and cannot contain brackets. Values must be ≤512 characters. Maximum 16 pairs allowed.

modelstring

objectenum

Allowed values:response

parallel\_tool\_callsboolean

presence\_penaltydouble or null

statusenum

Show 6 enum values

temperaturedouble or null

tool\_choiceenum or object

Show 5 variants

toolslist of objects

Show 5 variants

top\_pdouble or null

backgroundboolean or null

max\_output\_tokensdouble or null

max\_tool\_callsdouble or null

outputlist of objects or null

Show 6 variants

output\_textstring or null

previous\_response\_idstring or null

promptobject or null

Show 2 properties

prompt\_cache\_keystring or null

reasoningobject or null

Show 2 properties

safety\_identifierstring or null

service\_tierenum or null

Allowed values:autodefaultflexpriorityscale

storeboolean or null

textobject or null

Text output configuration including format and verbosity

Show 2 properties

top\_logprobsdouble or null

truncationenum or null

Allowed values:autodisabled

usageobject or null

Token usage information for the response

Show 8 properties

userstring or null

### Errors

400

Bad Request Error

401

Unauthorized Error

402

Payment Required Error

404

Not Found Error

408

Request Timeout Error

413

Content Too Large Error

422

Unprocessable Entity Error

429

Too Many Requests Error

500

Internal Server Error

502

Bad Gateway Error

503

Service Unavailable Error

Was this page helpful?

YesNo

[Previous](/docs/api/reference/responses/error-handling)[#### Exchange authorization code for API key

Next](/docs/api/api-reference/o-auth/exchange-auth-code-for-api-key)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)