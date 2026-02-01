# CLAUDE.md — ebay-sdk project context

## What is this?
`ldraney-ebay-sdk` is a Python SDK wrapping all eBay REST APIs. It's the pure Python layer between raw eBay APIs and a future MCP server.

## Architecture
```
eBay OpenAPI Specs → ldraney-ebay-sdk (this repo) → MCP Server (future repo)
```

- **Auth**: handled by `ldraney-ebay-oauth` (PyPI dependency)
- **HTTP**: `httpx`
- **Testing**: `pytest`, integration tests only (real sandbox API calls, no mocks)

## Package Structure
```
src/ebay_sdk/
├── client.py          # EbayClient — base HTTP + auth
├── buy/browse.py      # Buy Browse API
├── sell/inventory.py   # Sell Inventory API
├── sell/fulfillment.py # Sell Fulfillment API
├── sell/account.py     # Sell Account API
├── sell/finances.py    # Sell Finances API
├── sell/marketing.py   # Sell Marketing API
├── sell/feed.py        # Sell Feed API
└── commerce/taxonomy.py # Commerce Taxonomy API
```

## API Specs (Source of Truth)
Each module maps 1:1 to an eBay OpenAPI 3.0 spec:

| API | Spec URL |
|-----|----------|
| Buy Browse | `https://developer.ebay.com/api-docs/master/buy/browse/openapi/3/buy_browse_v1_oas3.json` |
| Sell Inventory | `https://developer.ebay.com/api-docs/master/sell/inventory/openapi/3/sell_inventory_v1_oas3.json` |
| Sell Fulfillment | `https://developer.ebay.com/api-docs/master/sell/fulfillment/openapi/3/sell_fulfillment_v1_oas3.json` |
| Sell Account | `https://developer.ebay.com/api-docs/master/sell/account/openapi/3/sell_account_v1_oas3.json` |
| Sell Finances | `https://developer.ebay.com/api-docs/master/sell/finances/openapi/3/sell_finances_v1_oas3.json` |
| Sell Marketing | `https://developer.ebay.com/api-docs/master/sell/marketing/openapi/3/sell_marketing_v1_oas3.json` |
| Sell Feed | `https://developer.ebay.com/api-docs/master/sell/feed/openapi/3/sell_feed_v1_oas3.json` |
| Commerce Taxonomy | `https://developer.ebay.com/api-docs/master/commerce/taxonomy/openapi/3/commerce_taxonomy_v1_oas3.json` |

## Commands
```bash
poetry install          # Install dependencies
pytest tests/ -m integration  # Run integration tests (needs sandbox creds)
poetry build            # Build wheel
```

## Testing Philosophy
- Integration tests only — every test hits the real eBay sandbox API
- Test objects (real sandbox item IDs, SKUs) are fine; mock data is not
- `EBAY_CLIENT_ID` and `EBAY_CLIENT_SECRET` env vars required for tests
- Tests skip gracefully when credentials are missing

## Key Dependencies
- `ldraney-ebay-oauth` — OAuth2 token management
- `httpx` — HTTP client
- `pytest` — testing (dev)
