Source: https://openrouter.ai/docs/guides/privacy/logging

Logging | Provider Data Retention | OpenRouter | Documentation

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

* [Provider Policies](#provider-policies)
* [Training on Prompts](#training-on-prompts)
* [Data Retention & Logging](#data-retention--logging)
* [Enterprise EU in-region routing](#enterprise-eu-in-region-routing)

[Privacy](/docs/guides/privacy/data-collection)

Logging
=======

Copy page

Provider logging and data retention policies

Each AI provider on OpenRouter has its own data handling policies for logging and retention. This page explains how to control which providers can access your data.

Provider Policies
-----------------

### Training on Prompts

Each provider on OpenRouter has its own data handling policies. We reflect those policies in structured data on each AI endpoint that we offer.

On your account settings page, you can set whether you would like to allow routing to providers that may train on your data (according to their own policies). There are separate settings for paid and free models.

Wherever possible, OpenRouter works with providers to ensure that prompts will not be trained on, but there are exceptions. If you opt out of training in your account settings, OpenRouter will not route to providers that train. This setting has no bearing on OpenRouter’s own policies and what we do with your prompts.

##### Data Policy Filtering

You can [restrict individual requests](/docs/features/provider-routing#requiring-providers-to-comply-with-data-policies)
to only use providers with a certain data policy.

This is also available as an account-wide setting in [your privacy settings](https://openrouter.ai/settings/privacy).

### Data Retention & Logging

Providers also have their own data retention policies, often for compliance reasons. OpenRouter does not have routing rules that change based on data retention policies of providers, but the retention policies as reflected in each provider’s terms are shown below. Any user of OpenRouter can ignore providers that don’t meet their own data retention requirements.

The full terms of service for each provider are linked from the provider’s page, and aggregated in the [documentation](/docs/features/provider-routing#terms-of-service).

| Provider | Data Retention | Train on Prompts |
| --- | --- | --- |

Enterprise EU in-region routing
-------------------------------

For enterprise customers, OpenRouter supports EU in-region routing. When enabled for your account, your prompts and completions are processed within the European Union and do not leave the EU. Use the base URL `https://eu.openrouter.ai` for API requests to keep traffic and data within Europe. This feature is only enabled for enterprise customers by request.

##### EU-only models list

To see which models are available for EU in-region routing, call `/api/v1/models/user` through the EU domain. [Learn more](/docs/api/api-reference/models/list-models-user)

If you’re interested, please contact our enterprise team at <https://openrouter.ai/enterprise/form>.

Was this page helpful?

YesNo

[Previous](/docs/guides/privacy/data-collection)[#### Latency and Performance

Understanding OpenRouter's performance characteristics

Next](/docs/guides/best-practices/latency-and-performance)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)