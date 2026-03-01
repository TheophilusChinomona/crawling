Source: https://openrouter.ai/docs/enterprise-quickstart

Enterprise Quickstart | OpenRouter for Organizations | OpenRouter | Documentation

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

* [1. Set Up Your Organization](#1-set-up-your-organization)
* [2. Configure API Key Management](#2-configure-api-key-management)
* [Management API Keys](#management-api-keys)
* [API Key Rotation](#api-key-rotation)
* [3. Implement Security Controls](#3-implement-security-controls)
* [Guardrails](#guardrails)
* [Zero Data Retention (ZDR)](#zero-data-retention-zdr)
* [Data Privacy](#data-privacy)
* [4. Set Up Observability](#4-set-up-observability)
* [Broadcast](#broadcast)
* [User Tracking](#user-tracking)
* [5. Monitor Usage and Costs](#5-monitor-usage-and-costs)
* [Usage Accounting](#usage-accounting)
* [Activity Export](#activity-export)
* [6. Optimize for Reliability](#6-optimize-for-reliability)
* [Provider Routing and Fallbacks](#provider-routing-and-fallbacks)
* [Uptime Optimization](#uptime-optimization)
* [Next Steps](#next-steps)

[Guides](/docs/guides/guides/free-models-router-playground)

Enterprise Quickstart
=====================

Copy page

Get your organization up and running with OpenRouter

1. Set Up Your Organization
---------------------------

Organizations enable teams to collaborate with shared credits, centralized API key management, and unified usage tracking.

To create an organization, navigate to [Settings > Preferences](https://openrouter.ai/settings/preferences) and click **Create Organization**. Once created, you can invite team members and switch between personal and organization contexts using the organization switcher.

Key organization capabilities include shared credit pools for centralized billing, role-based access control (Admin and Member roles), and organization-wide activity tracking.

For complete details on organization setup and management, see the [Organization Management](/docs/guides/guides/use-cases/organization-management) guide.

2. Configure API Key Management
-------------------------------

Enterprise deployments typically require programmatic API key management for automated provisioning, rotation, and lifecycle management.

### Management API Keys

Create a [Management API key](https://openrouter.ai/settings/management-keys) to manage API keys programmatically. This enables automated key creation for customer instances, programmatic key rotation for security compliance, and usage monitoring with automatic limit enforcement.

See [Management API Keys](/docs/guides/overview/auth/management-api-keys) for the full API reference and code examples.

### API Key Rotation

Regular key rotation limits the impact of compromised credentials. OpenRouter’s Management API supports zero-downtime rotation: create a new key, update your applications, then delete the old key.

If you use [BYOK (Bring Your Own Key)](/docs/guides/overview/auth/byok), you can rotate OpenRouter API keys without touching your provider credentials, simplifying key management.

See [API Key Rotation](/docs/guides/guides/api-key-rotation) for step-by-step instructions.

3. Implement Security Controls
------------------------------

### Guardrails

Guardrails let organizations control how members and API keys use OpenRouter. Configure spending limits with daily, weekly, or monthly resets, model and provider allowlists to restrict access, and Zero Data Retention enforcement for sensitive workloads.

Guardrails can be assigned to organization members (baseline for all their keys) or directly to specific API keys for granular control. When multiple guardrails apply, stricter rules always win.

See [Guardrails](/docs/guides/features/guardrails) for configuration details and the [Guardrails API reference](/docs/api-reference/guardrails/list-guardrails) for programmatic management.

### Zero Data Retention (ZDR)

Zero Data Retention ensures providers do not store your prompts or responses. Enable ZDR globally in your [privacy settings](/settings/privacy) or per-request using the `zdr` parameter.

OpenRouter itself has a ZDR policy and does not retain your prompts unless you explicitly opt in to prompt logging.

See [Zero Data Retention](/docs/guides/features/zdr) for the full list of ZDR-compatible endpoints and configuration options.

### Data Privacy

OpenRouter does not store your prompts or responses unless you opt in to prompt logging. Only metadata (token counts, latency, etc.) is stored for reporting and your activity feed.

See [Data Collection](/docs/guides/privacy/data-collection) and [Logging](/docs/guides/privacy/logging) for complete privacy documentation.

4. Set Up Observability
-----------------------

### Broadcast

Broadcast automatically sends traces from your OpenRouter requests to external observability platforms without additional instrumentation. Supported destinations include Datadog, Langfuse, LangSmith, Braintrust, OpenTelemetry Collector, S3, and more.

Configure broadcast at [Settings > Observability](https://openrouter.ai/settings/observability). You can filter traces by API key, set sampling rates, and configure up to 5 destinations of the same type for different environments.

See [Broadcast](/docs/guides/features/broadcast) for setup instructions and destination-specific walkthroughs.

### User Tracking

Track your end-users by including a `user` parameter in API requests. This improves caching performance (sticky routing per user) and enables user-level analytics in your activity feed and exports.

See [User Tracking](/docs/guides/guides/user-tracking) for implementation details.

5. Monitor Usage and Costs
--------------------------

### Usage Accounting

Every API response includes detailed usage information: token counts (prompt, completion, reasoning, cached), cost in credits, and timing data. This enables real-time cost tracking without additional API calls.

See [Usage Accounting](/docs/guides/guides/usage-accounting) for response format details and code examples.

### Activity Export

Export aggregated usage data as CSV or PDF from the [Activity page](https://openrouter.ai/activity). Filter by time period and group by Model, API Key, or Creator (organization member) for detailed reporting.

See [Activity Export](/docs/guides/guides/activity-export) for export instructions.

6. Optimize for Reliability
---------------------------

### Provider Routing and Fallbacks

OpenRouter monitors provider health in real-time and automatically routes around outages. Configure fallback chains by specifying multiple models, and customize provider selection based on cost, latency, or specific provider preferences.

See [Provider Selection](/docs/features/provider-routing) and [Model Fallbacks](/docs/routing/model-fallbacks) for configuration options.

### Uptime Optimization

OpenRouter tracks response times, error rates, and availability across all providers. This data powers intelligent routing decisions and provides transparency about service reliability.

See [Uptime Optimization](/docs/guides/best-practices/uptime-optimization) for details on how OpenRouter maximizes availability.

Next Steps
----------

Once your organization is configured, explore these additional resources:

* [Quickstart](/docs/quickstart) for basic API integration examples
* [Structured Outputs](/docs/features/structured-outputs) for JSON schema enforcement
* [Tool Calling](/docs/features/tool-calling) for function calling capabilities
* [Prompt Caching](/docs/guides/best-practices/prompt-caching) for cost optimization
* [Latency and Performance](/docs/guides/best-practices/latency-and-performance) for performance tuning

For enterprise sales inquiries or custom requirements, contact our sales team at [openrouter.ai/enterprise](https://openrouter.ai/enterprise).

Was this page helpful?

YesNo

[Previous](/docs/guides/guides/free-models-router-playground)[#### API Key Rotation

Securely rotate your OpenRouter API keys

Next](/docs/guides/guides/api-key-rotation)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)