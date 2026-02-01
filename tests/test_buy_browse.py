"""Integration tests for Buy Browse API.

Spec: https://developer.ebay.com/api-docs/master/buy/browse/openapi/3/buy_browse_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient


@pytest.mark.integration
class TestSearch:
    def test_search_returns_items(self, ebay: EbayClient):
        result = ebay.buy_browse.search(q="laptop", limit=3)
        assert "itemSummaries" in result or "total" in result

    def test_search_by_category(self, ebay: EbayClient):
        # 177 = Cell Phones & Smartphones
        result = ebay.buy_browse.search(category_ids="177", limit=3)
        assert "itemSummaries" in result or "total" in result


@pytest.mark.integration
class TestItem:
    def test_get_item(self, ebay: EbayClient):
        # First search to get a real item ID
        search = ebay.buy_browse.search(q="test", limit=1)
        if not search.get("itemSummaries"):
            pytest.skip("No items found in sandbox")
        item_id = search["itemSummaries"][0]["itemId"]
        item = ebay.buy_browse.get_item(item_id)
        assert item["itemId"] == item_id
