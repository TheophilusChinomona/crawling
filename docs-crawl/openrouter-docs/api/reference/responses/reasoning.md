Source: https://openrouter.ai/docs/api/reference/responses/reasoning

Responses API Beta Reasoning | Advanced AI Reasoning Capabilities | OpenRouter | Documentation

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

* [Reasoning Configuration](#reasoning-configuration)
* [Reasoning Effort Levels](#reasoning-effort-levels)
* [Complex Reasoning Example](#complex-reasoning-example)
* [Reasoning in Conversation Context](#reasoning-in-conversation-context)
* [Streaming Reasoning](#streaming-reasoning)
* [Response with Reasoning](#response-with-reasoning)
* [Best Practices](#best-practices)
* [Next Steps](#next-steps)

[API Guides](/docs/api/reference/overview)[Responses API](/docs/api/reference/responses/overview)

Reasoning
=========

Copy page

Advanced reasoning capabilities with the Responses API Beta

##### Beta API

This API is in **beta stage** and may have breaking changes.

The Responses API Beta supports advanced reasoning capabilities, allowing models to show their internal reasoning process with configurable effort levels.

Reasoning Configuration
-----------------------

Configure reasoning behavior using the `reasoning` parameter:

TypeScriptPythoncURL

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: 'What is the meaning of life?', |
| 10 | reasoning: { |
| 11 | effort: 'high' |
| 12 | }, |
| 13 | max_output_tokens: 9000, |
| 14 | }), |
| 15 | }); |
| 16 |  |
| 17 | const result = await response.json(); |
| 18 | console.log(result); |
```

Reasoning Effort Levels
-----------------------

The `effort` parameter controls how much computational effort the model puts into reasoning:

| Effort Level | Description |
| --- | --- |
| `minimal` | Basic reasoning with minimal computational effort |
| `low` | Light reasoning for simple problems |
| `medium` | Balanced reasoning for moderate complexity |
| `high` | Deep reasoning for complex problems |

Complex Reasoning Example
-------------------------

For complex mathematical or logical problems:

TypeScriptPython

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: [ |
| 10 | { |
| 11 | type: 'message', |
| 12 | role: 'user', |
| 13 | content: [ |
| 14 | { |
| 15 | type: 'input_text', |
| 16 | text: 'Was 1995 30 years ago? Please show your reasoning.', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | reasoning: { |
| 22 | effort: 'high' |
| 23 | }, |
| 24 | max_output_tokens: 9000, |
| 25 | }), |
| 26 | }); |
| 27 |  |
| 28 | const result = await response.json(); |
| 29 | console.log(result); |
```

Reasoning in Conversation Context
---------------------------------

Include reasoning in multi-turn conversations:

TypeScriptPython

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: [ |
| 10 | { |
| 11 | type: 'message', |
| 12 | role: 'user', |
| 13 | content: [ |
| 14 | { |
| 15 | type: 'input_text', |
| 16 | text: 'What is your favorite color?', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | { |
| 21 | type: 'message', |
| 22 | role: 'assistant', |
| 23 | id: 'msg_abc123', |
| 24 | status: 'completed', |
| 25 | content: [ |
| 26 | { |
| 27 | type: 'output_text', |
| 28 | text: "I don't have a favorite color.", |
| 29 | annotations: [] |
| 30 | } |
| 31 | ] |
| 32 | }, |
| 33 | { |
| 34 | type: 'message', |
| 35 | role: 'user', |
| 36 | content: [ |
| 37 | { |
| 38 | type: 'input_text', |
| 39 | text: 'How many Earths can fit on Mars?', |
| 40 | }, |
| 41 | ], |
| 42 | }, |
| 43 | ], |
| 44 | reasoning: { |
| 45 | effort: 'high' |
| 46 | }, |
| 47 | max_output_tokens: 9000, |
| 48 | }), |
| 49 | }); |
| 50 |  |
| 51 | const result = await response.json(); |
| 52 | console.log(result); |
```

Streaming Reasoning
-------------------

Enable streaming to see reasoning develop in real-time:

TypeScriptPython

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: 'Solve this step by step: If a train travels 60 mph for 2.5 hours, how far does it go?', |
| 10 | reasoning: { |
| 11 | effort: 'medium' |
| 12 | }, |
| 13 | stream: true, |
| 14 | max_output_tokens: 9000, |
| 15 | }), |
| 16 | }); |
| 17 |  |
| 18 | const reader = response.body?.getReader(); |
| 19 | const decoder = new TextDecoder(); |
| 20 |  |
| 21 | while (true) { |
| 22 | const { done, value } = await reader.read(); |
| 23 | if (done) break; |
| 24 |  |
| 25 | const chunk = decoder.decode(value); |
| 26 | const lines = chunk.split('\n'); |
| 27 |  |
| 28 | for (const line of lines) { |
| 29 | if (line.startsWith('data: ')) { |
| 30 | const data = line.slice(6); |
| 31 | if (data === '[DONE]') return; |
| 32 |  |
| 33 | try { |
| 34 | const parsed = JSON.parse(data); |
| 35 | if (parsed.type === 'response.reasoning.delta') { |
| 36 | console.log('Reasoning:', parsed.delta); |
| 37 | } |
| 38 | } catch (e) { |
| 39 | // Skip invalid JSON |
| 40 | } |
| 41 | } |
| 42 | } |
| 43 | } |
```

Response with Reasoning
-----------------------

When reasoning is enabled, the response includes reasoning information:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "resp_1234567890", |
| 3 | "object": "response", |
| 4 | "created_at": 1234567890, |
| 5 | "model": "openai/o4-mini", |
| 6 | "output": [ |
| 7 | { |
| 8 | "type": "reasoning", |
| 9 | "id": "rs_abc123", |
| 10 | "encrypted_content": "gAAAAABotI9-FK1PbhZhaZk4yMrZw3XDI1AWFaKb9T0NQq7LndK6zaRB...", |
| 11 | "summary": [ |
| 12 | "First, I need to determine the current year", |
| 13 | "Then calculate the difference from 1995", |
| 14 | "Finally, compare that to 30 years" |
| 15 | ] |
| 16 | }, |
| 17 | { |
| 18 | "type": "message", |
| 19 | "id": "msg_xyz789", |
| 20 | "status": "completed", |
| 21 | "role": "assistant", |
| 22 | "content": [ |
| 23 | { |
| 24 | "type": "output_text", |
| 25 | "text": "Yes. In 2025, 1995 was 30 years ago. In fact, as of today (Aug 31, 2025), it's exactly 30 years since Aug 31, 1995.", |
| 26 | "annotations": [] |
| 27 | } |
| 28 | ] |
| 29 | } |
| 30 | ], |
| 31 | "usage": { |
| 32 | "input_tokens": 15, |
| 33 | "output_tokens": 85, |
| 34 | "output_tokens_details": { |
| 35 | "reasoning_tokens": 45 |
| 36 | }, |
| 37 | "total_tokens": 100 |
| 38 | }, |
| 39 | "status": "completed" |
| 40 | } |
```

Best Practices
--------------

1. **Choose appropriate effort levels**: Use `high` for complex problems, `low` for simple tasks
2. **Consider token usage**: Reasoning increases token consumption
3. **Use streaming**: For long reasoning chains, streaming provides better user experience
4. **Include context**: Provide sufficient context for the model to reason effectively

Next Steps
----------

* Explore [Tool Calling](/docs/api/reference/responses/tool-calling) with reasoning
* Learn about [Web Search](/docs/api/reference/responses/web-search) integration
* Review [Basic Usage](/docs/api/reference/responses/basic-usage) fundamentals

Was this page helpful?

YesNo

[Previous](/docs/api/reference/responses/basic-usage)[#### Tool Calling

Function calling and tool integration with the Responses API Beta

Next](/docs/api/reference/responses/tool-calling)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)