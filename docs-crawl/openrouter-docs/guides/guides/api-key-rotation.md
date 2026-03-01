Source: https://openrouter.ai/docs/guides/guides/api-key-rotation

API Key Rotation | Secure Key Management for OpenRouter | OpenRouter | Documentation

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

* [Why Rotate API Keys?](#why-rotate-api-keys)
* [Rotation Strategy](#rotation-strategy)
* [Rotating Keys with the Management API](#rotating-keys-with-the-management-api)
* [Step 1: Create a New Key](#step-1-create-a-new-key)
* [Step 2: Update Your Applications](#step-2-update-your-applications)
* [Step 3: Delete the Old Key](#step-3-delete-the-old-key)
* [BYOK Advantage: Simplified Key Rotation](#byok-advantage-simplified-key-rotation)
* [Best Practices](#best-practices)
* [Related Resources](#related-resources)

[Guides](/docs/guides/guides/free-models-router-playground)

API Key Rotation
================

Copy page

Securely rotate your OpenRouter API keys

Regular API key rotation is a security best practice that limits the impact of compromised credentials. OpenRouter’s [Management API](/docs/guides/overview/auth/management-api-keys) makes it easy to rotate keys programmatically without service interruption.

Why Rotate API Keys?
--------------------

Rotating API keys regularly helps protect your applications by limiting the window of exposure if a key is compromised, meeting compliance requirements for credential management, enabling clean audit trails of key usage, and allowing you to revoke access for former team members or deprecated systems.

Rotation Strategy
-----------------

A zero-downtime key rotation follows three steps: create a new key, update your applications to use the new key, and delete the old key once all systems have migrated.

##### 

Always verify your new key is working in production before deleting the old one. This prevents accidental service disruption.

Rotating Keys with the Management API
-------------------------------------

First, you’ll need a [Management API key](https://openrouter.ai/settings/management-keys) to manage your API keys programmatically.

### Step 1: Create a New Key

TypeScript SDKPythonTypeScript (fetch)

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: 'your-management-key', |
| 5 | }); |
| 6 |  |
| 7 | const newKey = await openRouter.apiKeys.create({ |
| 8 | name: 'Production Key - Rotated 2025-01', |
| 9 | limit: 1000, |
| 10 | }); |
| 11 |  |
| 12 | console.log('New key created:', newKey.data.key); |
| 13 | console.log('Key hash:', newKey.data.hash); |
```

##### 

Store the key hash returned in the response. You’ll need it to delete the old key later.

### Step 2: Update Your Applications

Deploy your new API key to your applications. The specific process depends on your infrastructure, but common approaches include updating environment variables in your deployment configuration, rotating secrets in your secrets manager (AWS Secrets Manager, HashiCorp Vault, etc.), or updating your CI/CD pipeline variables.

Both keys remain valid during this transition period, so you can roll out changes gradually without service interruption.

### Step 3: Delete the Old Key

Once all your applications are using the new key, delete the old one:

TypeScript SDKPythonTypeScript (fetch)

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: 'your-management-key', |
| 5 | }); |
| 6 |  |
| 7 | const oldKeyHash = 'hash-of-old-key'; |
| 8 | await openRouter.apiKeys.delete(oldKeyHash); |
| 9 |  |
| 10 | console.log('Old key deleted successfully'); |
```

BYOK Advantage: Simplified Key Rotation
---------------------------------------

If you use [Bring Your Own Key (BYOK)](/docs/guides/overview/auth/byok) with OpenRouter, you get a significant advantage when it comes to key rotation: **you can rotate your OpenRouter API keys without ever needing to rotate your provider keys**.

When you configure BYOK, your provider API keys (OpenAI, Anthropic, Google, etc.) are stored securely in OpenRouter and associated with your account, not with individual OpenRouter API keys. This means:

* **Rotate OpenRouter keys freely**: You can rotate your OpenRouter API keys as often as you like for security compliance without touching your provider credentials.
* **Provider keys stay stable**: Your provider API keys remain unchanged, avoiding the complexity of rotating credentials across multiple AI providers.
* **Single point of management**: Manage all your provider keys in one place through OpenRouter’s [integrations settings](https://openrouter.ai/settings/integrations), while rotating your application-facing OpenRouter keys independently.

This separation of concerns makes BYOK particularly valuable for organizations with strict key rotation policies. You get the security benefits of regular key rotation for your application credentials while maintaining stable, long-lived connections to your AI providers.

##### 

With BYOK, your provider keys are tied to your OpenRouter account, not to individual API keys. Rotate your OpenRouter keys as often as needed without any changes to your provider configuration.

Best Practices
--------------

When implementing key rotation, keep these recommendations in mind:

* **Use descriptive key names**: Include rotation dates or version numbers in key names for easy tracking.
* **Monitor key usage**: Check the [Activity page](https://openrouter.ai/activity) to verify traffic has migrated to the new key before deleting the old one.
* **Set appropriate limits**: Apply spending limits to new keys to prevent unexpected costs.
* **Document your rotation schedule**: Establish and follow a regular rotation cadence (e.g., quarterly).
* **Test in staging first**: Validate your rotation process in a non-production environment.

Related Resources
-----------------

* [Management API Keys](/docs/guides/overview/auth/management-api-keys) - Full API reference for key management
* [BYOK](/docs/guides/overview/auth/byok) - Configure your own provider keys

Was this page helpful?

YesNo

[Previous](/docs/enterprise-quickstart)[#### Red Teaming

Policy for red teaming and adversarial testing on OpenRouter

Next](/docs/guides/guides/red-teaming)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)