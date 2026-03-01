Source: https://openrouter.ai/docs/api/api-reference/chat/send-chat-completion-request

Create a chat completion | OpenRouter | Documentation

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

[API Reference](/docs/api/api-reference/responses/create-responses)[Chat](/docs/api/api-reference/chat/send-chat-completion-request)

Create a chat completion
========================

Copy page

POST

https://openrouter.ai/api/v1/chat/completions

POST

/api/v1/chat/completions

cURL

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/chat/completions \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "messages": [ |
| 6 | { |
| 7 | "role": "system", |
| 8 | "content": "You are a helpful assistant." |
| 9 | }, |
| 10 | { |
| 11 | "role": "user", |
| 12 | "content": "What is the capital of France?" |
| 13 | } |
| 14 | ], |
| 15 | "model": "openai/gpt-4", |
| 16 | "max_tokens": 150, |
| 17 | "temperature": 0.7 |
| 18 | }' |
```

Try it

200Successful

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "chatcmpl-123", |
| 3 | "choices": [ |
| 4 | { |
| 5 | "finish_reason": "stop", |
| 6 | "index": 0, |
| 7 | "message": { |
| 8 | "role": "assistant", |
| 9 | "content": "The capital of France is Paris." |
| 10 | } |
| 11 | } |
| 12 | ], |
| 13 | "created": 1677652288, |
| 14 | "model": "openai/gpt-4", |
| 15 | "object": "chat.completion", |
| 16 | "usage": { |
| 17 | "completion_tokens": 15, |
| 18 | "prompt_tokens": 10, |
| 19 | "total_tokens": 25 |
| 20 | } |
| 21 | } |
```

Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

messageslist of objectsRequired

List of messages for the conversation

Show 5 variants

providerobject or nullOptional

When multiple model providers are available, optionally indicate your routing preference.

Show 13 properties

pluginslist of objectsOptional

Plugins you want to enable for this request, including their settings.

Show 5 variants

userstringOptional

Unique user identifier

session\_idstringOptional`<=128 characters`

A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 128 characters.

traceobjectOptional

Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations.

Show 5 properties

modelstringOptional

Model to use for completion

modelslist of objectsOptional

Models to use for completion

frequency\_penaltydouble or nullOptional`-2-2`

Frequency penalty (-2.0 to 2.0)

logit\_biasmap from strings to doubles or nullOptional

Token logit bias adjustments

logprobsboolean or nullOptional

Return log probabilities

top\_logprobsdouble or nullOptional`0-20`

Number of top log probabilities to return (0-20)

max\_completion\_tokensdouble or nullOptional`>=1`

Maximum tokens in completion

max\_tokensdouble or nullOptional`>=1`

Maximum tokens (deprecated, use max\_completion\_tokens)

metadatamap from strings to stringsOptional

Key-value pairs for additional object information (max 16 pairs, 64 char keys, 512 char values)

presence\_penaltydouble or nullOptional`-2-2`

Presence penalty (-2.0 to 2.0)

reasoningobjectOptional

Configuration options for reasoning models

Show 2 properties

response\_formatobjectOptional

Response format configuration

Show 5 variants

seedinteger or nullOptional

Random seed for deterministic outputs

stopstring or list of strings or anyOptional

Stop sequences (up to 4)

Show 3 variants

streambooleanOptionalDefaults to `false`

Enable streaming response

stream\_optionsobjectOptional

Streaming configuration options

Show 1 properties

temperaturedouble or nullOptional`0-2`Defaults to `1`

Sampling temperature (0-2)

parallel\_tool\_callsboolean or nullOptional

tool\_choiceenum or objectOptional

Tool choice configuration

Show 4 variants

toolslist of objectsOptional

Available tools for function calling

Show 3 properties

top\_pdouble or nullOptional`0-1`Defaults to `1`

Nucleus sampling parameter (0-1)

debugobjectOptional

Debug options for inspecting request transformations (streaming only)

Show 1 properties

image\_configmap from strings to strings or doubles or lists of anyOptional

Provider-specific image configuration options. Keys and values vary by model/provider. See <https://openrouter.ai/docs/guides/overview/multimodal/image-generation> for more details.

Show 3 variants

modalitieslist of enumsOptional

Output modalities for the response. Supported values are "text", "image", and "audio".

Allowed values:textimageaudio

### Response

Successful chat completion response

idstring

Unique completion identifier

choiceslist of objects

List of completion choices

Show 4 properties

createddouble

Unix timestamp of creation

modelstring

Model used for completion

objectenum

Allowed values:chat.completion

system\_fingerprintstring or null

System fingerprint

usageobject or null

Token usage statistics

Show 5 properties

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

[Previous](/docs/api/api-reference/analytics/get-user-activity)[#### Get remaining credits

Next](/docs/api/api-reference/credits/get-credits)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)