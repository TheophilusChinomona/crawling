Source: https://openrouter.ai/docs/sdks/typescript/api-reference/responses

Beta.Responses | OpenRouter TypeScript SDK | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* + [Agentic Usage](/docs/sdks/agentic-usage)
* DevTools

  + [Overview](/docs/sdks/dev-tools/devtools)
* TypeScript SDK

  + [Overview](/docs/sdks/typescript/overview)
  + Call Model
  + API Reference
* Python SDK

  + [Overview](/docs/sdks/python/overview)
  + API Reference

Light

On this page

* [Overview](#overview)
* [Available Operations](#available-operations)
* [send](#send)
* [Example Usage](#example-usage)
* [Standalone function](#standalone-function)
* [Parameters](#parameters)
* [Response](#response)
* [Errors](#errors)

[TypeScript SDK](/docs/sdks/typescript/overview)[API Reference](/docs/sdks/typescript/api-reference/analytics)

Beta.Responses - TypeScript SDK

Copy page

Beta.Responses method reference

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Overview
--------

beta.responses endpoints

### Available Operations

* [send](/docs/sdks/typescript/api-reference/responses#send) - Create a response

send
----

Creates a streaming or non-streaming response using OpenResponses API format

### Example Usage

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from "@openrouter/sdk"; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: process.env["OPENROUTER_API_KEY"] ?? "", |
| 5 | }); |
| 6 |  |
| 7 | async function run() { |
| 8 | const result = await openRouter.beta.responses.send({}); |
| 9 |  |
| 10 | console.log(result); |
| 11 | } |
| 12 |  |
| 13 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { betaResponsesSend } from "@openrouter/sdk/funcs/betaResponsesSend.js"; |
| 3 |  |
| 4 | // Use `OpenRouterCore` for best tree-shaking performance. |
| 5 | // You can create one instance of it to use across an application. |
| 6 | const openRouter = new OpenRouterCore({ |
| 7 | apiKey: process.env["OPENROUTER_API_KEY"] ?? "", |
| 8 | }); |
| 9 |  |
| 10 | async function run() { |
| 11 | const res = await betaResponsesSend(openRouter, {}); |
| 12 | if (res.ok) { |
| 13 | const { value: result } = res; |
| 14 | console.log(result); |
| 15 | } else { |
| 16 | console.log("betaResponsesSend failed:", res.error); |
| 17 | } |
| 18 | } |
| 19 |  |
| 20 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [models.OpenResponsesRequest](/docs/sdks/typescript/api-reference/models/openresponsesrequest) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](/docs/sdks/typescript/api-reference/lib/retryconfig) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.CreateResponsesResponse](/docs/sdks/typescript/api-reference/operations/createresponsesresponse)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.PaymentRequiredResponseError | 402 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.RequestTimeoutResponseError | 408 | application/json |
| errors.PayloadTooLargeResponseError | 413 | application/json |
| errors.UnprocessableEntityResponseError | 422 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.BadGatewayResponseError | 502 | application/json |
| errors.ServiceUnavailableResponseError | 503 | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524 | application/json |
| errors.ProviderOverloadedResponseError | 529 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

Was this page helpful?

YesNo

[Previous](/docs/sdks/typescript/api-reference/providers)[#### Python SDK

Official OpenRouter Python SDK documentation

Next](/docs/sdks/python/overview)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)