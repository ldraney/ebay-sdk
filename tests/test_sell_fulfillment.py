"""Integration tests for Sell Fulfillment API.

Spec: https://developer.ebay.com/api-docs/master/sell/fulfillment/openapi/3/sell_fulfillment_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient


@pytest.mark.integration
class TestOrders:
    def test_get_orders(self, ebay: EbayClient):
        result = ebay.sell_fulfillment.get_orders(limit=5)
        assert isinstance(result, dict)
        assert "orders" in result or "total" in result


@pytest.mark.integration
class TestPaymentDisputes:
    def test_get_payment_disputes(self, ebay: EbayClient):
        result = ebay.sell_fulfillment.get_payment_disputes(limit=5)
        assert isinstance(result, dict)
