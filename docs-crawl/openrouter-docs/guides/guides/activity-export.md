Source: https://openrouter.ai/docs/guides/guides/activity-export

Activity Export | Export Usage Reports with OpenRouter | OpenRouter | Documentation

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

* [Overview](#overview)
* [How to Export](#how-to-export)
* [Detailed Exports](#detailed-exports)

[Guides](/docs/guides/guides/free-models-router-playground)

Activity Export
===============

Copy page

Export your aggregated usage data as CSV or PDF from the [Activity page](https://openrouter.ai/activity).

Overview
--------

The Activity page shows three metrics:

* **Spend**: Total spend (OpenRouter credits + estimated BYOK spend)
* **Tokens**: Total tokens used (prompt + completion)
* **Requests**: Number of AI requests (chatroom included)

Filter by time period (1 Hour, 1 Day, 1 Month, 1 Year) and group by Model, API Key, or Creator (org member). Each time period is sub-grouped by minute, hour, day, and month, respectively.

##### Estimated BYOK Spend

Dollars spent for external BYOK usage is estimated based on market rates for that provider, and don’t reflect any discounts you might have from them.

How to Export
-------------

1. Go to [openrouter.ai/activity](https://openrouter.ai/activity)
2. Select your time period and grouping
3. Open the options dropdown (top right)
4. Choose **Export to…** then **CSV** or **PDF**

![Activity Overview](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/1fdff23f169165c95449be1cf0148f2b9f4d12c22c9c93210c210d2034aa5fd4/content/assets/activity-export-overview.png)

This exports a summary of all three metrics. For detailed breakdowns, click into a specific metric first.

Detailed Exports
----------------

Click any metric card to expand it. From there you can:

* See breakdowns by your selected grouping
* Export the detailed data as CSV or PDF

![Spend by API Key](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/80710434271816ceafb41c0b57a01b37e27fe9d05ab3b5b4285c9a7b6831f6d1/content/assets/activity-export-spend-by-key.png)

For example, a detailed “Tokens by API Key” export to pdf for the last year. It starts with a summary page for all keys, and then granular breakdowns for each key individually:

![PDF Token Report](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6ced925f2c31c3c628524d263b24b005a5fe984cc931b92c5581c408fc7f5b13/content/assets/activity-export-pdf-tokens.png)

##### Reasoning Tokens

Reasoning tokens are included in completion tokens for billing. This shows how many of the completion tokens were used thinking before responding.

Was this page helpful?

YesNo

[Previous](/docs/guides/guides/usage-accounting)[#### User Tracking

Next](/docs/guides/guides/user-tracking)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)