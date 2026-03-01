Source: https://openrouter.ai/docs/community/lang-chain

LangChain Integration | OpenRouter SDK Support | OpenRouter | Documentation

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

* [Using LangChain](#using-langchain)

[Community](/docs/guides/community/frameworks-and-integrations-overview)

LangChain
=========

Copy page

Using OpenRouter with LangChain

Using LangChain
---------------

LangChain provides a standard interface for working with chat models. You can use OpenRouter with LangChain by setting the `base_url` parameter to point to OpenRouter’s API. For more details on LangChain’s model interface, see the [LangChain Models documentation](https://docs.langchain.com/oss/python/langchain/models#initialize-a-model).

**Resources:**

* Using [LangChain for Python](https://github.com/langchain-ai/langchain): [github](https://github.com/alexanderatallah/openrouter-streamlit/blob/main/pages/2_Langchain_Quickstart.py)
* Using [Streamlit](https://streamlit.io/): [github](https://github.com/alexanderatallah/openrouter-streamlit)

TypeScriptPython (using init\_chat\_model)Python (using ChatOpenAI directly)

```
|  |  |
| --- | --- |
| 1 | import { ChatOpenAI } from "@langchain/openai"; |
| 2 | import { HumanMessage, SystemMessage } from "@langchain/core/messages"; |
| 3 |  |
| 4 | const chat = new ChatOpenAI( |
| 5 | { |
| 6 | model: '<model_name>', |
| 7 | temperature: 0.8, |
| 8 | streaming: true, |
| 9 | apiKey: '${API_KEY_REF}', |
| 10 | }, |
| 11 | { |
| 12 | baseURL: 'https://openrouter.ai/api/v1', |
| 13 | defaultHeaders: { |
| 14 | 'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai. |
| 15 | 'X-OpenRouter-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai. |
| 16 | }, |
| 17 | }, |
| 18 | ); |
| 19 |  |
| 20 | // Example usage |
| 21 | const response = await chat.invoke([ |
| 22 | new SystemMessage("You are a helpful assistant."), |
| 23 | new HumanMessage("Hello, how are you?"), |
| 24 | ]); |
```

Was this page helpful?

YesNo

[Previous](/docs/guides/community/arize)[#### LiveKit

Using OpenRouter with LiveKit Agents

Next](/docs/guides/community/livekit)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)