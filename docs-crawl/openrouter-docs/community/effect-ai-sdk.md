Source: https://openrouter.ai/docs/community/effect-ai-sdk

Effect AI SDK Integration | OpenRouter SDK Support | OpenRouter | Documentation

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

* [Effect AI SDK](#effect-ai-sdk)

[Community](/docs/guides/community/frameworks-and-integrations-overview)

Effect AI SDK
=============

Copy page

Integrate OpenRouter using the Effect AI SDK

Effect AI SDK
-------------

You can use the [Effect AI SDK](https://www.npmjs.com/package/@effect/ai) to integrate OpenRouter with your Effect applications. To get started, install the following packages:

* [effect](https://www.npmjs.com/package/effect): the Effect core (if not already installed)
* [@effect/ai](https://www.npmjs.com/package/@effect/ai): the core Effect AI SDK abstractions
* [@effect/ai-openrouter](https://www.npmjs.com/package/@effect/ai-openrouter): the Effect AI provider integration for OpenRouter
* [@effect/platform](https://www.npmjs.com/package/@effect/platform): platform-agnostic abstractions for Effect

```
|  |  |
| --- | --- |
| $ | npm install effect @effect/ai @effect/ai-openrouter @effect/platform |
```

Once that’s done you can use the [LanguageModel](https://effect.website/docs/ai/getting-started/#define-an-interaction-with-a-language-model) module to define interactions with a large language model via OpenRouter.

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { LanguageModel } from "@effect/ai" |
| 2 | import { OpenRouterClient, OpenRouterLanguageModel } from "@effect/ai-openrouter" |
| 3 | import { FetchHttpClient } from "@effect/platform" |
| 4 | import { Config, Effect, Layer, Stream } from "effect" |
| 5 |  |
| 6 | const Gpt4o = OpenRouterLanguageModel.model("openai/gpt-4o") |
| 7 |  |
| 8 | const program = LanguageModel.streamText({ |
| 9 | prompt: [ |
| 10 | { role: "system", content: "You are a comedian with a penchant for groan-inducing puns" }, |
| 11 | { role: "user", content: [{ type: "text", text: "Tell me a dad joke" }] } |
| 12 | ] |
| 13 | }).pipe( |
| 14 | Stream.filter((part) => part.type === "text-delta"), |
| 15 | Stream.runForEach((part) => Effect.sync(() => process.stdout.write(part.delta))), |
| 16 | Effect.provide(Gpt4o) |
| 17 | ) |
| 18 |  |
| 19 | const OpenRouter = OpenRouterClient.layerConfig({ |
| 20 | apiKey: Config.redacted("OPENROUTER_API_KEY") |
| 21 | }).pipe(Layer.provide(FetchHttpClient.layer)) |
| 22 |  |
| 23 | program.pipe( |
| 24 | Effect.provide(OpenRouter), |
| 25 | Effect.runPromise |
| 26 | ) |
```

Was this page helpful?

YesNo

[Previous](/docs/guides/community/awesome-openrouter)[#### Arize

Using OpenRouter with Arize

Next](/docs/guides/community/arize)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)