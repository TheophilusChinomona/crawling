Source: https://openrouter.ai/docs/guides/guides/free-models-router-playground

Free Models Router | OpenRouter | OpenRouter | Documentation

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

* [Using the Free Models Router](#using-the-free-models-router)
* [Step 1: Open the Chat Playground](#step-1-open-the-chat-playground)
* [Step 2: Search for Free Models](#step-2-search-for-free-models)
* [Step 3: Select the Free Models Router](#step-3-select-the-free-models-router)
* [Step 4: Start Chatting](#step-4-start-chatting)
* [Selecting Specific Free Models](#selecting-specific-free-models)
* [Using Free Models via API](#using-free-models-via-api)
* [Free Model Limitations](#free-model-limitations)
* [Related Resources](#related-resources)

[Guides](/docs/guides/guides/free-models-router-playground)

Free Models Router
==================

Copy page

Get started with free AI inference using the OpenRouter Chat Playground

OpenRouter offers free models that let you experiment with AI without any cost. The easiest way to try these models is through the [Chat Playground](https://openrouter.ai/chat), where you can start chatting immediately.

Using the Free Models Router
----------------------------

The simplest way to get free inference is to use `openrouter/free`, our Free Models Router that automatically selects a free model at random from the available free models on OpenRouter. The router intelligently filters for models that support the features your request needs, such as image understanding, tool calling, and structured outputs.

### Step 1: Open the Chat Playground

Navigate to [openrouter.ai/chat](https://openrouter.ai/chat) to access the Chat Playground.

### Step 2: Search for Free Models

Click the **Add Model** button (or press `Cmd+K` / `Ctrl+K`) to open the model selector. Type “free” in the search box to filter for free models.

![Searching for free models in the model selector](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/279ff80044cd9fe63c0bbd22776b2ff5bac6c31578d0110d6bf66ee559d44b92/content/pages/guides/free-models-search.png)

You’ll see a list of available free models, including the **Free Models Router** option.

### Step 3: Select the Free Models Router

Click on **Free Models Router** to select it. This router will automatically choose a free model for each request based on your needs.

![Free Models Router selected in the chat playground](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/98bfb39b5b0c0e4d907e5be1adf502d7b87d50ca21bf656a28e86a5ea7785752/content/pages/guides/free-router-selected.png)

### Step 4: Start Chatting

Once selected, you can start sending messages. The Free Models Router will route your request to an appropriate free model, and you’ll see which model responded in the chat.

![A response from a free model showing the model name](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/ea10ad8718aa5c1190c32eabe34d6fe7a1c79124771f619c3160e6e6620bd3a4/content/pages/guides/free-router-response.png)

In this example, the Free Models Router selected Solar Pro 3 (free) to respond to the message.

Selecting Specific Free Models
------------------------------

If you prefer to use a specific free model rather than the Free Models Router, you can select any model with “(free)” in its name from the model selector. Some popular free models include:

* **Trinity Large Preview (free)** - A frontier-scale open-weight model from Arcee
* **Trinity Mini (free)** - A smaller, faster variant
* **DeepSeek R1 (free)** - DeepSeek’s reasoning model
* **Llama models (free)** - Various Meta Llama models

Using Free Models via API
-------------------------

You can also use the Free Models Router programmatically. Simply set the model to `openrouter/free` in your API requests:

```
|  |  |
| --- | --- |
| $ | curl https://openrouter.ai/api/v1/chat/completions \ |
| > | -H "Authorization: Bearer $OPENROUTER_API_KEY" \ |
| > | -H "Content-Type: application/json" \ |
| > | -d '{ |
| > | "model": "openrouter/free", |
| > | "messages": [{"role": "user", "content": "Hello!"}] |
| > | }' |
```

For more details on the Free Models Router API, see the [API Quickstart](https://openrouter.ai/openrouter/free/api).

Free Model Limitations
----------------------

Free models may have different rate limits and availability compared to paid models. They are ideal for experimentation, learning, and low-volume use cases. For production workloads with higher reliability requirements, consider using paid models.

Related Resources
-----------------

* [Free Variant Documentation](/docs/guides/routing/model-variants/free) - Learn about the `:free` variant suffix
* [Models Page](https://openrouter.ai/models) - Browse all available models
* [Free Models Router API](https://openrouter.ai/openrouter/free/api) - API quickstart for the Free Models Router

Was this page helpful?

YesNo

[Previous](/docs/guides/best-practices/reasoning-tokens)[#### Enterprise Quickstart

Get your organization up and running with OpenRouter

Next](/docs/enterprise-quickstart)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)