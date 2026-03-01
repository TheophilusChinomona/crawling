Source: https://openrouter.ai/docs/guides/features/broadcast/weave

Broadcast to W&B Weave | OpenRouter Observability | OpenRouter | Documentation

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

* [Step 1: Get your W&B API key](#step-1-get-your-wb-api-key)
* [Step 2: Enable Broadcast in OpenRouter](#step-2-enable-broadcast-in-openrouter)
* [Step 3: Configure W&B Weave](#step-3-configure-wb-weave)
* [Step 4: Test and save](#step-4-test-and-save)
* [Step 5: Send a test trace](#step-5-send-a-test-trace)
* [Custom Metadata](#custom-metadata)
* [Supported Metadata Keys](#supported-metadata-keys)
* [Example](#example)
* [Attributes and Inputs](#attributes-and-inputs)
* [Additional Context](#additional-context)
* [Privacy Mode](#privacy-mode)

[Features](/docs/guides/features/presets)[Broadcast](/docs/guides/features/broadcast/overview)

W&B Weave

Copy page

Send traces to W&B Weave

[Weights & Biases Weave](https://wandb.ai/site/weave) is an observability platform for tracking and evaluating LLM applications.

Step 1: Get your W&B API key
----------------------------

In W&B, go to your [User Settings](https://wandb.ai/settings) and copy your API key.

Step 2: Enable Broadcast in OpenRouter
--------------------------------------

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

Step 3: Configure W&B Weave
---------------------------

Click the edit icon next to **W&B Weave** and enter:

* **Api Key**: Your W&B API key
* **Entity**: Your W&B username or team name
* **Project**: The project name where traces will be logged
* **Base Url** (optional): Default is `https://trace.wandb.ai`

![W&B Weave Configuration](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/8c4641a48f3473f905b4d002f888f3a3b678fd7d3b08123d28bf18e38b99567a/content/pages/features/broadcast/broadcast-weave-config.png)

Step 4: Test and save
---------------------

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

![W&B Weave Configured](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/7c23542342bffc7801e184bcd62f793991109b9ba4d68415e657de7584500c46/content/pages/features/broadcast/broadcast-weave-configured.png)

Step 5: Send a test trace
-------------------------

Make an API request through OpenRouter and view the trace in W&B Weave.

![W&B Weave Trace](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5d0b78b2857428ab3e847836b9081d0eb7e6eb55e5d82ad9e32f21014c3ffc5f/content/pages/features/broadcast/broadcast-weave-trace.png)

Custom Metadata
---------------

W&B Weave supports custom attributes and structured inputs for organizing and analyzing your LLM calls.

### Supported Metadata Keys

| Key | Weave Mapping | Description |
| --- | --- | --- |
| `trace_id` | `openrouter_trace_id` attribute | Custom trace identifier stored in attributes |
| `trace_name` | `op_name` | Custom operation name displayed in the Weave call list |
| `generation_name` | `op_name` | Name for the LLM call |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Write a poem about AI..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_name": "Creative Writing Agent", |
| 8 | "prompt_template": "poem_v2", |
| 9 | "experiment_name": "creative_benchmark", |
| 10 | "dataset_version": "1.0.0" |
| 11 | } |
| 12 | } |
```

### Attributes and Inputs

Weave organizes trace data into:

* **Attributes**: Metadata about the call (user IDs, organization IDs, trace identifiers, custom metadata)
* **Inputs**: The actual request data including messages, model parameters (temperature, max\_tokens, etc.)
* **Summary**: Token usage, costs, and timing metrics

### Additional Context

* The `user` field maps to `user_id` in attributes
* The `session_id` field maps to `session_id` in attributes
* Custom metadata keys from `trace` are merged into the call’s attributes
* Model parameters (temperature, max\_tokens, top\_p) are included in inputs for easy filtering

Privacy Mode
------------

When [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](/docs/guides/features/broadcast#privacy-mode) for details.

Was this page helpful?

YesNo

[Previous](/docs/guides/features/broadcast/snowflake)[#### Webhook

Send traces to any HTTP endpoint

Next](/docs/guides/features/broadcast/webhook)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)