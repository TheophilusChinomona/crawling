Source: https://openrouter.ai/docs/sdks/typescript/call-model/overview

Call Model Overview (Typescript) | OpenRouter SDK | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* + [Agentic Usage](/docs/sdks/agentic-usage)
* DevTools

  + [Overview](/docs/sdks/dev-tools/devtools)
* TypeScript SDK

  + [Overview](/docs/sdks/typescript/overview)
  + Call Model
  + API Reference
* Python SDK

  + [Overview](/docs/sdks/python/overview)
  + API Reference

Light

On this page

* [Why callModel?](#why-callmodel)
* [Quick Start](#quick-start)
* [Consumption Patterns](#consumption-patterns)
* [Text Methods](#text-methods)
* [Streaming Methods](#streaming-methods)
* [Tool Methods](#tool-methods)
* [Input Formats](#input-formats)
* [What’s Next?](#whats-next)
* [Example Tools](#example-tools)

[TypeScript SDK](/docs/sdks/typescript/overview)[Call Model](/docs/sdks/typescript/call-model/overview)

Call Model (Typescript)

Copy page

A unified API for calling any LLM with automatic tool execution and multiple consumption patterns

Why callModel?
--------------

* **Items-Based Model**: Built on OpenRouter’s Responses API with structured
  items (messages, tool calls, reasoning) instead of raw message chunks
* **Multiple Consumption Patterns**: Get text, stream responses, or access
  structured data - all from a single call
* **Automatic Tool Execution**: Define tools with Zod schemas and let the SDK
  handle execution loops
* **Type Safety**: Full TypeScript inference for tool inputs, outputs, and
  events
* **Format Compatibility**: Convert to/from OpenAI chat and Anthropic Claude
  message formats
* **Streaming First**: Built on a reusable stream architecture that supports
  concurrent consumers

Quick Start
-----------

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openrouter = new OpenRouter({ |
| 4 | apiKey: process.env.OPENROUTER_API_KEY, |
| 5 | }); |
| 6 |  |
| 7 | const result = openrouter.callModel({ |
| 8 | model: 'openai/gpt-5-nano', |
| 9 | input: 'What is the capital of France?', |
| 10 | }); |
| 11 |  |
| 12 | // Get text (simplest pattern) |
| 13 | const text = await result.getText(); |
| 14 | console.log(text); // "The capital of France is Paris." |
```

Consumption Patterns
--------------------

callModel returns a `ModelResult` object that provides multiple ways to consume
the response:

### Text Methods

```
|  |  |
| --- | --- |
| 1 | // Get just the text content |
| 2 | const text = await result.getText(); |
| 3 |  |
| 4 | // Get the full response with usage data |
| 5 | const response = await result.getResponse(); |
| 6 | console.log(response.usage); // { inputTokens, outputTokens, cachedTokens } |
```

### Streaming Methods

```
|  |  |
| --- | --- |
| 1 | // Stream text deltas |
| 2 | for await (const delta of result.getTextStream()) { |
| 3 | process.stdout.write(delta); |
| 4 | } |
| 5 |  |
| 6 | // Stream reasoning (for reasoning models) |
| 7 | for await (const delta of result.getReasoningStream()) { |
| 8 | console.log('Reasoning:', delta); |
| 9 | } |
| 10 |  |
| 11 | // Stream complete items by ID (recommended) |
| 12 | for await (const item of result.getItemsStream()) { |
| 13 | console.log('Item update:', item.type, item.id); |
| 14 | } |
| 15 |  |
| 16 | // Stream all events (including tool preliminary results) |
| 17 | for await (const event of result.getFullResponsesStream()) { |
| 18 | console.log('Event:', event.type); |
| 19 | } |
```

### Tool Methods

```
|  |  |
| --- | --- |
| 1 | // Get all tool calls from the response |
| 2 | const toolCalls = await result.getToolCalls(); |
| 3 |  |
| 4 | // Stream tool calls as they complete |
| 5 | for await (const toolCall of result.getToolCallsStream()) { |
| 6 | console.log(`Tool: ${toolCall.name}`, toolCall.arguments); |
| 7 | } |
| 8 |  |
| 9 | // Stream tool deltas and preliminary results |
| 10 | for await (const event of result.getToolStream()) { |
| 11 | if (event.type === 'delta') { |
| 12 | process.stdout.write(event.content); |
| 13 | } else if (event.type === 'preliminary_result') { |
| 14 | console.log('Progress:', event.result); |
| 15 | } |
| 16 | } |
```

Input Formats
-------------

callModel accepts multiple input formats:

```
|  |  |
| --- | --- |
| 1 | // Simple string |
| 2 | const result1 = openrouter.callModel({ |
| 3 | model: 'openai/gpt-5-nano', |
| 4 | input: 'Hello!', |
| 5 | }); |
| 6 |  |
| 7 | // Message array (OpenResponses format) |
| 8 | const result2 = openrouter.callModel({ |
| 9 | model: 'openai/gpt-5-nano', |
| 10 | input: [ |
| 11 | { role: 'user', content: 'Hello!' }, |
| 12 | ], |
| 13 | }); |
| 14 |  |
| 15 | // With system instructions |
| 16 | const result3 = openrouter.callModel({ |
| 17 | model: 'openai/gpt-5-nano', |
| 18 | instructions: 'You are a helpful assistant.', |
| 19 | input: 'Hello!', |
| 20 | }); |
```

What’s Next?
------------

Explore the guides to learn more about specific features:

* **[Working with Items](/docs/sdks/typescript/call-model/items)** - Understand
  the items-based streaming paradigm
* **[Text Generation](/docs/sdks/typescript/call-model/text-generation)** -
  Input formats, model selection, and response handling
* **[Streaming](/docs/sdks/typescript/call-model/streaming)** - All streaming
  methods and patterns
* **[Tools](/docs/sdks/typescript/call-model/tools)** - Creating typed tools
  with Zod schemas and multi-turn orchestration
* **[nextTurnParams](/docs/sdks/typescript/call-model/next-turn-params)** -
  Tool-driven context injection for skills and plugins
* **[Message Formats](/docs/sdks/typescript/call-model/message-formats)** -
  Converting to/from OpenAI and Claude formats
* **[Dynamic Parameters](/docs/sdks/typescript/call-model/dynamic-parameters)**
  - Async functions for adaptive behavior
* **[Stop Conditions](/docs/sdks/typescript/call-model/stop-conditions)** -
  Intelligent execution control
* **[API Reference](/docs/sdks/typescript/call-model/api-reference)** - Complete
  type definitions and method signatures

### Example Tools

Ready-to-use tool implementations:

* **[Weather Tool](/docs/sdks/typescript/call-model/examples/weather-tool)** - Basic API integration
* **[Skills Loader](/docs/sdks/typescript/call-model/examples/skills-loader)** - Claude Code skills pattern

Was this page helpful?

YesNo

[Previous](/docs/sdks/typescript/overview)[#### Working with Items

Understanding the items-based streaming paradigm for callModel

Next](/docs/sdks/typescript/call-model/working-with-items)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)