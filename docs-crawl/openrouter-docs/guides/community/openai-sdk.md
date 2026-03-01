Source: https://openrouter.ai/docs/guides/community/openai-sdk#using-the-openai-sdk

OpenAI SDK Integration | OpenRouter SDK Support | OpenRouter | Documentation

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

* [Using the OpenAI SDK](#using-the-openai-sdk)

[Community](/docs/guides/community/frameworks-and-integrations-overview)

OpenAI SDK
==========

Copy page

Using OpenRouter with OpenAI SDK

Using the OpenAI SDK
--------------------

* Using `pip install openai`: [github](https://github.com/OpenRouterTeam/openrouter-examples-python/blob/main/src/openai_test.py).
* Using `npm i openai`: [github](https://github.com/OpenRouterTeam/openrouter-examples/tree/main/typescript).

  ##### 

  You can also use
  [Grit](https://app.grit.io/studio?key=RKC0n7ikOiTGTNVkI8uRS) to
  automatically migrate your code. Simply run `npx @getgrit/launcher openrouter`.

TypeScriptPython

```
|  |  |
| --- | --- |
| 1 | import OpenAI from "openai" |
| 2 |  |
| 3 | const openai = new OpenAI({ |
| 4 | baseURL: "https://openrouter.ai/api/v1", |
| 5 | apiKey: "${API_KEY_REF}", |
| 6 | defaultHeaders: { |
| 7 | ${getHeaderLines().join('\n        ')} |
| 8 | }, |
| 9 | }) |
| 10 |  |
| 11 | async function main() { |
| 12 | const completion = await openai.chat.completions.create({ |
| 13 | model: "${Model.GPT_4_Omni}", |
| 14 | messages: [ |
| 15 | { role: "user", content: "Say this is a test" } |
| 16 | ], |
| 17 | }) |
| 18 |  |
| 19 | console.log(completion.choices[0].message) |
| 20 | } |
| 21 | main(); |
```

Was this page helpful?

YesNo

[Previous](/docs/guides/community/mastra)[#### Anthropic Agent SDK

Using OpenRouter with the Anthropic Agent SDK

Next](/docs/guides/community/anthropic-agent-sdk)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)