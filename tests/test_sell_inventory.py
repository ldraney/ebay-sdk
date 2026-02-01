"""Integration tests for Sell Inventory API.

Spec: https://developer.ebay.com/api-docs/master/sell/inventory/openapi/3/sell_inventory_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient


@pytest.mark.integration
class TestInventoryItem:
    def test_get_inventory_items(self, ebay: EbayClient):
        result = ebay.sell_inventory.get_inventory_items(limit=5)
        assert isinstance(result, dict)

    def test_create_and_delete_inventory_item(self, ebay: EbayClient):
        sku = "SDK-TEST-001"
        body = {
            "product": {
                "title": "SDK Integration Test Item",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        ebay.sell_inventory.create_or_replace_inventory_item(sku, body)
        item = ebay.sell_inventory.get_inventory_item(sku)
        assert item["sku"] == sku

        ebay.sell_inventory.delete_inventory_item(sku)


@pytest.mark.integration
class TestInventoryLocation:
    def test_get_inventory_locations(self, ebay: EbayClient):
        result = ebay.sell_inventory.get_inventory_locations(limit=5)
        assert isinstance(result, dict)
