"""Integration tests for Buy Browse API.

Spec: https://developer.ebay.com/api-docs/master/buy/browse/openapi/3/buy_browse_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient
from ebay_sdk.client import EbayApiError


@pytest.mark.integration
class TestSearch:
    def test_search_returns_items(self, ebay: EbayClient):
        result = ebay.buy_browse.search(q="laptop", limit=3)
        assert "itemSummaries" in result or "total" in result

    def test_search_by_category(self, ebay: EbayClient):
        # 177 = Cell Phones & Smartphones
        result = ebay.buy_browse.search(category_ids="177", limit=3)
        assert "itemSummaries" in result or "total" in result

    def test_search_with_filter(self, ebay: EbayClient):
        result = ebay.buy_browse.search(
            q="phone", limit=2, sort="price", filter="price:[50..200]"
        )
        assert isinstance(result, dict)

    def test_search_with_aspect_filter(self, ebay: EbayClient):
        result = ebay.buy_browse.search(
            q="laptop", limit=2, aspect_filter="categoryId:177"
        )
        assert isinstance(result, dict)

    def test_search_with_fieldgroups(self, ebay: EbayClient):
        result = ebay.buy_browse.search(
            q="test", limit=1, fieldgroups="MATCHING_ITEMS"
        )
        assert isinstance(result, dict)

    def test_search_by_image(self, ebay: EbayClient):
        try:
            result = ebay.buy_browse.search_by_image(
                {"imageUrl": "https://i.ebayimg.com/images/g/test/s-l1600.jpg"},
                limit=3,
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409, 500):
                pytest.skip(
                    f"search_by_image not available in sandbox: {exc.status_code}"
                )
            raise


@pytest.mark.integration
class TestItem:
    def test_get_item(self, ebay: EbayClient):
        search = ebay.buy_browse.search(q="test", limit=1)
        if not search.get("itemSummaries"):
            pytest.skip("No items found in sandbox")
        item_id = search["itemSummaries"][0]["itemId"]
        item = ebay.buy_browse.get_item(item_id)
        assert item["itemId"] == item_id

    def test_get_item_with_fieldgroups(self, ebay: EbayClient):
        search = ebay.buy_browse.search(q="test", limit=1)
        if not search.get("itemSummaries"):
            pytest.skip("No items found in sandbox")
        item_id = search["itemSummaries"][0]["itemId"]
        try:
            item = ebay.buy_browse.get_item(item_id, fieldgroups="PRODUCT")
            assert item["itemId"] == item_id
        except EbayApiError as exc:
            if exc.status_code in (400, 404):
                pytest.skip(f"get_item with fieldgroups failed: {exc.status_code}")
            raise

    def test_get_item_by_legacy_id(self, ebay: EbayClient):
        search = ebay.buy_browse.search(q="test", limit=1)
        if not search.get("itemSummaries"):
            pytest.skip("No items found in sandbox")
        item_id = search["itemSummaries"][0]["itemId"]
        # Extract the numeric legacy ID from the v1 item ID (format: v1|<legacyId>|0)
        parts = item_id.split("|")
        if len(parts) < 2:
            pytest.skip("Cannot extract legacy ID from item ID format")
        legacy_id = parts[1]
        try:
            item = ebay.buy_browse.get_item_by_legacy_id(legacy_id)
            assert isinstance(item, dict)
            assert "itemId" in item
        except EbayApiError as exc:
            if exc.status_code in (400, 404):
                pytest.skip(f"get_item_by_legacy_id failed: {exc.status_code}")
            raise

    def test_get_items(self, ebay: EbayClient):
        search = ebay.buy_browse.search(q="test", limit=2)
        summaries = search.get("itemSummaries", [])
        if len(summaries) < 2:
            pytest.skip("Need at least 2 items for get_items test")
        ids = "|".join(s["itemId"] for s in summaries[:2])
        result = ebay.buy_browse.get_items(ids)
        assert isinstance(result, dict)
        assert "items" in result

    def test_get_items_by_item_group(self, ebay: EbayClient):
        search = ebay.buy_browse.search(q="shirt", limit=5)
        summaries = search.get("itemSummaries", [])
        if not summaries:
            pytest.skip("No items found in sandbox")
        # Look for an item with an itemGroupId (multi-variation listing)
        group_id = None
        for s in summaries:
            if "itemGroupId" in s:
                group_id = s["itemGroupId"]
                break
        if not group_id:
            pytest.skip("No multi-variation item found in sandbox")
        try:
            result = ebay.buy_browse.get_items_by_item_group(group_id)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 404):
                pytest.skip(
                    f"get_items_by_item_group failed: {exc.status_code}"
                )
            raise

    def test_check_compatibility(self, ebay: EbayClient):
        # Category 6000 = eBay Motors parts — need an item from that category
        search = ebay.buy_browse.search(category_ids="6000", limit=1)
        summaries = search.get("itemSummaries", [])
        if not summaries:
            pytest.skip("No auto parts items found in sandbox")
        item_id = summaries[0]["itemId"]
        try:
            result = ebay.buy_browse.check_compatibility(
                item_id,
                [
                    {"name": "Year", "value": "2020"},
                    {"name": "Make", "value": "Toyota"},
                    {"name": "Model", "value": "Camry"},
                ],
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 404, 409):
                pytest.skip(
                    f"check_compatibility not available: {exc.status_code}"
                )
            raise
