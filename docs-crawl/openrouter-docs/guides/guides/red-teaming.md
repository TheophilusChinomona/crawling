Source: https://openrouter.ai/docs/guides/guides/red-teaming

Red Teaming | Adversarial Testing Policy | OpenRouter | Documentation

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

* [Approval Required](#approval-required)
* [Legitimate Red Teaming](#legitimate-red-teaming)
* [Compatibility with Zero Data Retention](#compatibility-with-zero-data-retention)
* [Request Approval](#request-approval)

[Guides](/docs/guides/guides/free-models-router-playground)

Red Teaming
===========

Copy page

Policy for red teaming and adversarial testing on OpenRouter

Red teaming (testing AI applications and/or models for prompt injection, jailbreaking, or other adversarial scenarios) is a valuable part of AI safety research, but may also violate model terms-of-service.

Approval Required
-----------------

Because most model and provider terms of service do not support red-teaming, you cannot red-team models on OpenRouter without prior approval. This includes prompt injection, jailbreaking, or any attempt to get models to behave in ways that violate their terms of service.

Customers who engage in red teaming without approval may be flagged for model or provider terms of service violations. Unapproved red teaming may result in:

* Provider bans
* Model access restrictions
* Platform-wide account bans

Legitimate Red Teaming
----------------------

OpenRouter supports legitimate AI safety research and red teaming with prior approval. Getting approval allows us to coordinate with providers and prevent your account from being flagged for policy violations.

If you have a legitimate use case for adversarial testing, we encourage you to reach out.

Compatibility with Zero Data Retention
--------------------------------------

Note that certain types of safety classifiers are run online (while the prompt is in-flight and in-memory). Prompts may therefore be flagged by classifiers even with full ZDR configured. These classifiers operate independently of data retention policies and are fully compatible with [Zero Data Retention (ZDR)](/docs/guides/features/zdr).

Request Approval
----------------

To request red teaming approval, email [safety@openrouter.ai](mailto:safety@openrouter.ai) with the following details:

* A description of your research or use case
* The models & providers you intend to test
* The types of adversarial techniques you plan to use
* Your expected timeline

##### 

Approval generally takes **5 business days**. Approval is not guaranteed and is granted at OpenRouter’s discretion based on the details of your use case.

Was this page helpful?

YesNo

[Previous](/docs/guides/guides/api-key-rotation)[#### Crypto API

Purchase credits with crypto

Next](/docs/guides/guides/crypto-api)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)