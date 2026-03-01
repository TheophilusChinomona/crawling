Source: https://openrouter.ai/docs/api/reference/streaming

API Streaming | Real-time Model Responses in OpenRouter | OpenRouter | Documentation

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

On this page

* [Additional Information](#additional-information)
* [Stream Cancellation](#stream-cancellation)
* [Handling Errors During Streaming](#handling-errors-during-streaming)
* [Errors Before Any Tokens Are Sent](#errors-before-any-tokens-are-sent)
* [Errors After Tokens Have Been Sent (Mid-Stream)](#errors-after-tokens-have-been-sent-mid-stream)
* [Code Examples](#code-examples)
* [API-Specific Behavior](#api-specific-behavior)

[API Guides](/docs/api/reference/overview)

Streaming
=========

Copy page

The OpenRouter API allows streaming responses from *any model*. This is useful for building chat interfaces or other applications where the UI should update as the model generates the response.

To enable streaming, you can set the `stream` parameter to `true` in your request. The model will then stream the response to the client in chunks, rather than returning the entire response at once.

Here is an example of how to stream a response, and process it:

TypeScript SDKPythonTypeScript (fetch)

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const question = 'How would you build the tallest building ever?'; |
| 8 |  |
| 9 | const stream = await openRouter.chat.send({ |
| 10 | model: '{{MODEL}}', |
| 11 | messages: [{ role: 'user', content: question }], |
| 12 | stream: true, |
| 13 | }); |
| 14 |  |
| 15 | for await (const chunk of stream) { |
| 16 | const content = chunk.choices?.[0]?.delta?.content; |
| 17 | if (content) { |
| 18 | console.log(content); |
| 19 | } |
| 20 |  |
| 21 | // Final chunk includes usage stats |
| 22 | if (chunk.usage) { |
| 23 | console.log('Usage:', chunk.usage); |
| 24 | } |
| 25 | } |
```

### Additional Information

For SSE (Server-Sent Events) streams, OpenRouter occasionally sends comments to prevent connection timeouts. These comments look like:

```
|  |
| --- |
| : OPENROUTER PROCESSING |
```

Comment payload can be safely ignored per the [SSE specs](https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation). However, you can leverage it to improve UX as needed, e.g. by showing a dynamic loading indicator.

Some SSE client implementations might not parse the payload according to spec, which leads to an uncaught error when you `JSON.stringify` the non-JSON payloads. We recommend the following clients:

* [eventsource-parser](https://github.com/rexxars/eventsource-parser)
* [OpenAI SDK](https://www.npmjs.com/package/openai)
* [Vercel AI SDK](https://www.npmjs.com/package/ai)

### Stream Cancellation

Streaming requests can be cancelled by aborting the connection. For supported providers, this immediately stops model processing and billing.

###### Provider Support

**Supported**

* OpenAI, Azure, Anthropic
* Fireworks, Mancer, Recursal
* AnyScale, Lepton, OctoAI
* Novita, DeepInfra, Together
* Cohere, Hyperbolic, Infermatic
* Avian, XAI, Cloudflare
* SFCompute, Nineteen, Liquid
* Friendli, Chutes, DeepSeek

**Not Currently Supported**

* AWS Bedrock, Groq, Modal
* Google, Google AI Studio, Minimax
* HuggingFace, Replicate, Perplexity
* Mistral, AI21, Featherless
* Lynn, Lambda, Reflection
* SambaNova, Inflection, ZeroOneAI
* AionLabs, Alibaba, Nebius
* Kluster, Targon, InferenceNet

To implement stream cancellation:

TypeScript SDKPythonTypeScript (fetch)

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const controller = new AbortController(); |
| 8 |  |
| 9 | try { |
| 10 | const stream = await openRouter.chat.send({ |
| 11 | model: '{{MODEL}}', |
| 12 | messages: [{ role: 'user', content: 'Write a story' }], |
| 13 | stream: true, |
| 14 | }, { |
| 15 | signal: controller.signal, |
| 16 | }); |
| 17 |  |
| 18 | for await (const chunk of stream) { |
| 19 | const content = chunk.choices?.[0]?.delta?.content; |
| 20 | if (content) { |
| 21 | console.log(content); |
| 22 | } |
| 23 | } |
| 24 | } catch (error) { |
| 25 | if (error.name === 'AbortError') { |
| 26 | console.log('Stream cancelled'); |
| 27 | } else { |
| 28 | throw error; |
| 29 | } |
| 30 | } |
| 31 |  |
| 32 | // To cancel the stream: |
| 33 | controller.abort(); |
```

##### 

Cancellation only works for streaming requests with supported providers. For
non-streaming requests or unsupported providers, the model will continue
processing and you will be billed for the complete response.

### Handling Errors During Streaming

OpenRouter handles errors differently depending on when they occur during the streaming process:

#### Errors Before Any Tokens Are Sent

If an error occurs before any tokens have been streamed to the client, OpenRouter returns a standard JSON error response with the appropriate HTTP status code. This follows the standard error format:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "error": { |
| 3 | "code": 400, |
| 4 | "message": "Invalid model specified" |
| 5 | } |
| 6 | } |
```

Common HTTP status codes include:

* **400**: Bad Request (invalid parameters)
* **401**: Unauthorized (invalid API key)
* **402**: Payment Required (insufficient credits)
* **429**: Too Many Requests (rate limited)
* **502**: Bad Gateway (provider error)
* **503**: Service Unavailable (no available providers)

#### Errors After Tokens Have Been Sent (Mid-Stream)

If an error occurs after some tokens have already been streamed to the client, OpenRouter cannot change the HTTP status code (which is already 200 OK). Instead, the error is sent as a Server-Sent Event (SSE) with a unified structure:

```
|  |
| --- |
| data: {"id":"cmpl-abc123","object":"chat.completion.chunk","created":1234567890,"model":"gpt-3.5-turbo","provider":"openai","error":{"code":"server_error","message":"Provider disconnected unexpectedly"},"choices":[{"index":0,"delta":{"content":""},"finish_reason":"error"}]} |
```

Key characteristics of mid-stream errors:

* The error appears at the **top level** alongside standard response fields (id, object, created, etc.)
* A `choices` array is included with `finish_reason: "error"` to properly terminate the stream
* The HTTP status remains 200 OK since headers were already sent
* The stream is terminated after this unified error event

#### Code Examples

Here’s how to properly handle both types of errors in your streaming implementation:

TypeScript SDKPythonTypeScript (fetch)

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | async function streamWithErrorHandling(prompt: string) { |
| 8 | try { |
| 9 | const stream = await openRouter.chat.send({ |
| 10 | model: '{{MODEL}}', |
| 11 | messages: [{ role: 'user', content: prompt }], |
| 12 | stream: true, |
| 13 | }); |
| 14 |  |
| 15 | for await (const chunk of stream) { |
| 16 | // Check for errors in chunk |
| 17 | if ('error' in chunk) { |
| 18 | console.error(`Stream error: ${chunk.error.message}`); |
| 19 | if (chunk.choices?.[0]?.finish_reason === 'error') { |
| 20 | console.log('Stream terminated due to error'); |
| 21 | } |
| 22 | return; |
| 23 | } |
| 24 |  |
| 25 | // Process normal content |
| 26 | const content = chunk.choices?.[0]?.delta?.content; |
| 27 | if (content) { |
| 28 | console.log(content); |
| 29 | } |
| 30 | } |
| 31 | } catch (error) { |
| 32 | // Handle pre-stream errors |
| 33 | console.error(`Error: ${error.message}`); |
| 34 | } |
| 35 | } |
```

#### API-Specific Behavior

Different API endpoints may handle streaming errors slightly differently:

* **OpenAI Chat Completions API**: Returns `ErrorResponse` directly if no chunks were processed, or includes error information in the response if some chunks were processed
* **OpenAI Responses API**: May transform certain error codes (like `context_length_exceeded`) into a successful response with `finish_reason: "length"` instead of treating them as errors

Was this page helpful?

YesNo

[Previous](/docs/api/reference/overview)[#### Embeddings

Generate vector embeddings from text and images

Next](/docs/api/reference/embeddings)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)