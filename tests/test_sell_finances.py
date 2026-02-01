"""Integration tests for Sell Finances API.

Spec: https://developer.ebay.com/api-docs/master/sell/finances/openapi/3/sell_finances_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient


@pytest.mark.integration
class TestPayouts:
    def test_get_payouts(self, ebay: EbayClient):
        result = ebay.sell_finances.get_payouts(limit=5)
        assert isinstance(result, dict)


@pytest.mark.integration
class TestTransactions:
    def test_get_transactions(self, ebay: EbayClient):
        result = ebay.sell_finances.get_transactions(limit=5)
        assert isinstance(result, dict)


@pytest.mark.integration
class TestSellerFunds:
    def test_get_seller_funds_summary(self, ebay: EbayClient):
        result = ebay.sell_finances.get_seller_funds_summary()
        assert isinstance(result, dict)
