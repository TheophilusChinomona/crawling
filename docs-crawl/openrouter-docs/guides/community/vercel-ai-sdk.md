Source: https://openrouter.ai/docs/guides/community/vercel-ai-sdk#vercel-ai-sdk

Vercel AI SDK Integration | OpenRouter SDK Support | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* Overview

  + [Quickstart](/docs/quickstart)
  + [Principles](/docs/guides/overview/principles)
  + [Models](/docs/guides/overview/models)
  + Multimodal
  + Authentication
  + [FAQ](/docs/faq)
  + [Report Feedback](/docs/guides/overview/report-feedback)
  + [Enterprise](https://openrouter.ai/enterprise)
* Models & Routing

  + [Model Fallbacks](/docs/guides/routing/model-fallbacks)
  + [Provider Selection](/docs/guides/routing/provider-selection)
  + Model Variants
  + Routers
* Features

  + [Presets](/docs/guides/features/presets)
  + [Tool Calling](/docs/guides/features/tool-calling)
  + Plugins
  + [Structured Outputs](/docs/guides/features/structured-outputs)
  + [Message Transforms](/docs/guides/features/message-transforms)
  + [Zero Completion Insurance](/docs/guides/features/zero-completion-insurance)
  + [ZDR](/docs/guides/features/zdr)
  + [App Attribution](/docs/app-attribution)
  + [Guardrails](/docs/guides/features/guardrails)
  + Broadcast
* + Privacy
  + Best Practices
  + Guides
  + Community

Light

On this page

* [Vercel AI SDK](#vercel-ai-sdk)

[Community](/docs/guides/community/frameworks-and-integrations-overview)

Vercel AI SDK
=============

Copy page

Using OpenRouter with Vercel AI SDK

Vercel AI SDK
-------------

You can use the [Vercel AI SDK](https://www.npmjs.com/package/ai) to integrate OpenRouter with your Next.js app. To get started, install [@openrouter/ai-sdk-provider](https://github.com/OpenRouterTeam/ai-sdk-provider):

```
|  |  |
| --- | --- |
| $ | npm install @openrouter/ai-sdk-provider |
```

And then you can use [streamText()](https://sdk.vercel.ai/docs/reference/ai-sdk-core/stream-text) API to stream text from OpenRouter.

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { createOpenRouter } from '@openrouter/ai-sdk-provider'; |
| 2 | import { streamText } from 'ai'; |
| 3 | import { z } from 'zod'; |
| 4 |  |
| 5 | export const getLasagnaRecipe = async (modelName: string) => { |
| 6 | const openrouter = createOpenRouter({ |
| 7 | apiKey: '${API_KEY_REF}', |
| 8 | }); |
| 9 |  |
| 10 | const response = streamText({ |
| 11 | model: openrouter(modelName), |
| 12 | prompt: 'Write a vegetarian lasagna recipe for 4 people.', |
| 13 | }); |
| 14 |  |
| 15 | await response.consumeStream(); |
| 16 | return response.text; |
| 17 | }; |
| 18 |  |
| 19 | export const getWeather = async (modelName: string) => { |
| 20 | const openrouter = createOpenRouter({ |
| 21 | apiKey: '${API_KEY_REF}', |
| 22 | }); |
| 23 |  |
| 24 | const response = streamText({ |
| 25 | model: openrouter(modelName), |
| 26 | prompt: 'What is the weather in San Francisco, CA in Fahrenheit?', |
| 27 | tools: { |
| 28 | getCurrentWeather: { |
| 29 | description: 'Get the current weather in a given location', |
| 30 | parameters: z.object({ |
| 31 | location: z |
| 32 | .string() |
| 33 | .describe('The city and state, e.g. San Francisco, CA'), |
| 34 | unit: z.enum(['celsius', 'fahrenheit']).optional(), |
| 35 | }), |
| 36 | execute: async ({ location, unit = 'celsius' }) => { |
| 37 | // Mock response for the weather |
| 38 | const weatherData = { |
| 39 | 'Boston, MA': { |
| 40 | celsius: '15°C', |
| 41 | fahrenheit: '59°F', |
| 42 | }, |
| 43 | 'San Francisco, CA': { |
| 44 | celsius: '18°C', |
| 45 | fahrenheit: '64°F', |
| 46 | }, |
| 47 | }; |
| 48 |  |
| 49 | const weather = weatherData[location]; |
| 50 | if (!weather) { |
| 51 | return `Weather data for ${location} is not available.`; |
| 52 | } |
| 53 |  |
| 54 | return `The current weather in ${location} is ${weather[unit]}.`; |
| 55 | }, |
| 56 | }, |
| 57 | }, |
| 58 | }); |
| 59 |  |
| 60 | await response.consumeStream(); |
| 61 | return response.text; |
| 62 | }; |
```

Was this page helpful?

YesNo

[Previous](/docs/guides/community/tanstack-ai)[#### Xcode

Using OpenRouter with Apple Intelligence in Xcode

Next](/docs/guides/community/xcode)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)