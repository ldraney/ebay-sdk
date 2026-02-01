# ldraney-ebay-sdk

Python SDK wrapping all eBay REST APIs. Uses [`ldraney-ebay-oauth`](https://pypi.org/project/ldraney-ebay-oauth/) for authentication and `httpx` for HTTP.

## Install

```bash
pip install ldraney-ebay-sdk
```

## Quick Start

```python
from ebay_oauth import EbayOAuthClient
from ebay_sdk import EbayClient

oauth = EbayOAuthClient(
    client_id="your-app-id",
    client_secret="your-secret",
)

with EbayClient(oauth) as ebay:
    # Search for items
    results = ebay.buy_browse.search(q="vintage camera", limit=5)

    # Get category suggestions
    cats = ebay.commerce_taxonomy.get_category_suggestions("0", "camera")

    # List orders
    orders = ebay.sell_fulfillment.get_orders(limit=5)

    # Manage inventory
    ebay.sell_inventory.create_or_replace_inventory_item("MY-SKU", {
        "product": {"title": "Test Item"},
        "condition": "NEW",
        "availability": {"shipToLocationAvailability": {"quantity": 1}},
    })
```

## Sandbox Mode

```python
oauth = EbayOAuthClient(client_id="...", client_secret="...", sandbox=True)
ebay = EbayClient(oauth, sandbox=True)
```

## Available APIs

| Property | API | Endpoints |
|----------|-----|-----------|
| `ebay.buy_browse` | Buy Browse | search, get_item, etc. |
| `ebay.sell_inventory` | Sell Inventory | items, offers, locations |
| `ebay.sell_fulfillment` | Sell Fulfillment | orders, shipping, disputes |
| `ebay.sell_account` | Sell Account | policies, programs, privileges |
| `ebay.sell_finances` | Sell Finances | payouts, transactions, transfers |
| `ebay.sell_marketing` | Sell Marketing | campaigns, ads, promotions |
| `ebay.sell_feed` | Sell Feed | tasks, schedules, templates |
| `ebay.commerce_taxonomy` | Commerce Taxonomy | categories, aspects, compatibility |

## Development

```bash
poetry install
pytest tests/ -m integration  # requires EBAY_CLIENT_ID, EBAY_CLIENT_SECRET
poetry build
```

## License

MIT
