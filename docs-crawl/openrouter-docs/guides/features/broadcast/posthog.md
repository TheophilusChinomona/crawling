Source: https://openrouter.ai/docs/guides/features/broadcast/posthog

Broadcast to PostHog | OpenRouter Observability | OpenRouter | Documentation

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

* [Step 1: Get your PostHog project API key](#step-1-get-your-posthog-project-api-key)
* [Step 2: Enable Broadcast in OpenRouter](#step-2-enable-broadcast-in-openrouter)
* [Step 3: Configure PostHog](#step-3-configure-posthog)
* [Step 4: Test and save](#step-4-test-and-save)
* [Step 5: Send a test trace](#step-5-send-a-test-trace)
* [Custom Metadata](#custom-metadata)
* [Supported Metadata Keys](#supported-metadata-keys)
* [Example](#example)
* [Additional Context](#additional-context)
* [Privacy Mode](#privacy-mode)

[Features](/docs/guides/features/presets)[Broadcast](/docs/guides/features/broadcast/overview)

PostHog
=======

Copy page

Send traces to PostHog

[PostHog](https://posthog.com/) is an open-source product analytics platform that helps you understand user behavior. With PostHog’s LLM analytics, you can track and analyze your AI application usage.

Step 1: Get your PostHog project API key
----------------------------------------

In PostHog, navigate to your project settings:

1. Log in to your PostHog account
2. Go to **Project Settings**
3. Copy your Project API Key (starts with `phc_...`)

Step 2: Enable Broadcast in OpenRouter
--------------------------------------

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

Step 3: Configure PostHog
-------------------------

Click the edit icon next to **PostHog** and enter:

* **Api Key**: Your PostHog project API key (starts with `phc_...`)
* **Endpoint** (optional): Default is `https://us.i.posthog.com`. For EU region, use `https://eu.i.posthog.com`

Step 4: Test and save
---------------------

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

Step 5: Send a test trace
-------------------------

Make an API request through OpenRouter and view the LLM analytics in your
PostHog dashboard.

![PostHog LLM Analytics](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/c4b6f05846279a1425ed82450ff599981a7770f8ef5a80c560cc91d56e5e1b39/content/pages/features/broadcast/broadcast-posthog-analytics.png)

Custom Metadata
---------------

PostHog receives LLM analytics events with custom metadata included as event properties. Use the `trace` field to attach additional context to your analytics data.

### Supported Metadata Keys

| Key | PostHog Mapping | Description |
| --- | --- | --- |
| `trace_id` | Event property | Custom trace identifier for grouping related events |
| `trace_name` | Event property | Custom name for the trace |
| `generation_name` | Event property | Name for the LLM generation event |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Recommend a product..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_name": "Product Recommendations", |
| 8 | "generation_name": "Generate Recommendation", |
| 9 | "feature": "shopping-assistant", |
| 10 | "ab_test_group": "variant_b" |
| 11 | } |
| 12 | } |
```

### Additional Context

* The `user` field maps to PostHog’s `$ai_user` property for user-level LLM analytics
* The `session_id` field maps to `$ai_session_id` for session grouping
* Custom metadata keys from `trace` are included as properties on the LLM analytics event
* PostHog’s LLM analytics dashboard automatically tracks token usage, costs, and model performance

Privacy Mode
------------

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, the `$ai_input` and `$ai_output_choices` properties are excluded from events. All other analytics data — token usage, costs, model information, and custom metadata — is still sent normally.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/broadcast/otel-collector)[#### 

S3 / S3-Compatible

Send traces to Amazon S3 or S3-compatible storage

Next](/docs/guides/features/broadcast/s3)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)