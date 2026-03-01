Source: https://openrouter.ai/docs/guides/guides/distillation

Distillation | Compliance with Provider and Model Creator Policies | OpenRouter | Documentation

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

* [Why Distillation Compliance Matters](#why-distillation-compliance-matters)
* [Finding Distillable Models on the Model Page](#finding-distillable-models-on-the-model-page)
* [Using the Routing Parameter](#using-the-routing-parameter)
* [Example: Enforcing Distillable Models](#example-enforcing-distillable-models)
* [Use Cases](#use-cases)
* [Related Documentation](#related-documentation)

[Guides](/docs/guides/guides/free-models-router-playground)

Distillation
============

Copy page

Ensure compliance with provider and model creator policies for distillation

Model distillation is the process of training a smaller, more efficient model using outputs from a larger model. While this technique is powerful for creating specialized models, it’s important to respect the terms of service set by model providers and creators.

Some model providers and creators explicitly prohibit using their model outputs to train other models, while others allow it. OpenRouter makes it easy to filter for models that permit distillation, helping you stay compliant with these policies.

Why Distillation Compliance Matters
-----------------------------------

When you use model outputs to train or fine-tune other models, you need to ensure you have permission to do so. Using outputs from models that prohibit distillation could violate terms of service agreements and potentially expose you to legal liability.

OpenRouter tracks which models allow their outputs to be used for training purposes through the `is_trainable_text` property. Models where the author has explicitly allowed text distillation are marked as distillable.

##### 

OpenRouter provides distillation information on a best-effort basis. You should always verify the specific license terms for your use case, as licensing requirements may vary depending on how you intend to use the model outputs.

Finding Distillable Models on the Model Page
--------------------------------------------

The easiest way to find models that allow distillation is to use the **Distillable** filter on the [Models page](https://openrouter.ai/models?distillable=true).

1. Navigate to the [Models page with the distillable filter enabled](https://openrouter.ai/models?distillable=true)
2. The **Distillable** filter in the filter panel will be set to **Yes**, showing only models that allow distillation

This filter shows you all models where the author has permitted their outputs to be used for training purposes, making it easy to build compliant distillation workflows.

Using the Routing Parameter
---------------------------

For programmatic control, you can use the `enforce_distillable_text` parameter in your API requests. When set to `true`, OpenRouter will only route your request to models that allow text distillation.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `enforce_distillable_text` | boolean | - | Restrict routing to only models that allow text distillation. |

When `enforce_distillable_text` is set to `true`, the request will only be routed to models where the author has explicitly enabled text distillation. If no distillable models are available for your request, you’ll receive an error.

### Example: Enforcing Distillable Models

TypeScript SDKTypeScript (fetch)PythoncURL

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'meta-llama/llama-3.1-70b-instruct', |
| 9 | messages: [{ role: 'user', content: 'Explain quantum computing' }], |
| 10 | provider: { |
| 11 | enforceDistillableText: true, |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

Use Cases
---------

The distillable filter is particularly useful for:

* **Building training datasets**: When collecting model outputs to train or fine-tune your own models, ensure you only use outputs from models that permit this use.
* **Distillation pipelines**: When creating smaller, specialized models from larger teacher models, filter for models that allow their outputs to be used for training.
* **Compliance workflows**: Organizations with strict compliance requirements can enforce distillation policies programmatically across all API requests.

Related Documentation
---------------------

* [Provider Routing](/docs/features/provider-routing) - Learn more about the `enforce_distillable_text` parameter and other provider routing options
* [Models](/docs/overview/models) - Browse all available models and their capabilities

Was this page helpful?

YesNo

[Previous](/docs/guides/guides/user-tracking)[#### Claude 4.6 Migration Guide

Migrate to Claude 4.6 with adaptive thinking and max effort level

Next](/docs/guides/guides/model-migrations/claude-4-6)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)