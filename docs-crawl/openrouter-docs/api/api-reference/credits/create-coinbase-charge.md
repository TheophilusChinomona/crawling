Source: https://openrouter.ai/docs/api/api-reference/credits/create-coinbase-charge

Create a Coinbase charge for crypto payment | OpenRouter | Documentation

Search

`/`

Ask AI

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

[Docs](/docs/quickstart)[API Reference](/docs/api/reference/overview)[SDK Reference](/docs/sdks/agentic-usage)

* API Guides

  + [Overview](/docs/api/reference/overview)
  + [Streaming](/docs/api/reference/streaming)
  + [Embeddings](/docs/api/reference/embeddings)
  + [Limits](/docs/api/reference/limits)
  + [Authentication](/docs/api/reference/authentication)
  + [Parameters](/docs/api/reference/parameters)
  + [Errors and Debugging](/docs/api/reference/errors-and-debugging)
  + Responses API
* API Reference

  + Responses
  + OAuth
  + Anthropic Messages
  + Analytics
  + Chat
  + Credits
  + Embeddings
  + Generations
  + Models
  + Endpoints
  + Providers
  + API Keys
  + Guardrails

Light

[API Reference](/docs/api/api-reference/responses/create-responses)[Credits](/docs/api/api-reference/credits/get-credits)

Create a Coinbase charge for crypto payment
===========================================

Copy page

POST

https://openrouter.ai/api/v1/credits/coinbase

POST

/api/v1/credits/coinbase

cURL

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/credits/coinbase \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "amount": 150, |
| 6 | "sender": "0xAbC1234567890DefABC1234567890dEfABC12345", |
| 7 | "chain_id": 1 |
| 8 | }' |
```

Try it

200Successful

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "id": "charge_01F8MECHZX3TBDSZ7XRADM79XV", |
| 4 | "created_at": "2024-06-01T12:00:00Z", |
| 5 | "expires_at": "2024-06-01T12:30:00Z", |
| 6 | "web3_data": { |
| 7 | "transfer_intent": { |
| 8 | "call_data": { |
| 9 | "deadline": "2024-06-01T12:25:00Z", |
| 10 | "fee_amount": "0.0005", |
| 11 | "id": "tx_0x9f8b7c6d5e4a3b2c1d0e", |
| 12 | "operator": "0xOperator1234567890abcdef1234567890abcdef", |
| 13 | "prefix": "0x", |
| 14 | "recipient": "0xRecipient0987654321fedcba0987654321fedcba", |
| 15 | "recipient_amount": "150.00", |
| 16 | "recipient_currency": "USDC", |
| 17 | "refund_destination": "0xRefund1234567890abcdef1234567890abcdef", |
| 18 | "signature": "0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890" |
| 19 | }, |
| 20 | "metadata": { |
| 21 | "chain_id": 1, |
| 22 | "contract_address": "0xContract1234567890abcdef1234567890abcdef", |
| 23 | "sender": "0xAbC1234567890DefABC1234567890dEfABC12345" |
| 24 | } |
| 25 | } |
| 26 | } |
| 27 | } |
| 28 | } |
```

Create a Coinbase charge for crypto payment

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

amountdoubleRequired

senderstringRequired

chain\_idenumRequired

Allowed values:11378453

### Response

Returns the calldata to fulfill the transaction

dataobject

Show 4 properties

### Errors

400

Bad Request Error

401

Unauthorized Error

429

Too Many Requests Error

500

Internal Server Error

Was this page helpful?

YesNo

[Previous](/docs/api/api-reference/credits/get-credits)[#### Submit an embedding request

Next](/docs/api/api-reference/embeddings/create-embeddings)[Built with](https://buildwithfern.com/?utm_campaign=buildWith&utm_medium=docs&utm_source=openrouter.ai)

[![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5a7e2b0bd58241d151e9e352d7a4f898df12c062576c0ce0184da76c3635c5d3/content/assets/logo.svg)![Logo](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/6f95fbca823560084c5593ea2aa4073f00710020e6a78f8a3f54e835d97a8a0b/content/assets/logo-white.svg)](https://openrouter.ai/)

[Models](https://openrouter.ai/models)[Chat](https://openrouter.ai/chat)[Rankings](https://openrouter.ai/rankings)[Docs](/docs/api-reference/overview)