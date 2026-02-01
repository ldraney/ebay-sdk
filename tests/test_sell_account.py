"""Integration tests for Sell Account API.

Spec: https://developer.ebay.com/api-docs/master/sell/account/openapi/3/sell_account_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient


@pytest.mark.integration
class TestFulfillmentPolicy:
    def test_get_fulfillment_policies(self, ebay: EbayClient):
        result = ebay.sell_account.get_fulfillment_policies("EBAY_US")
        assert isinstance(result, dict)


@pytest.mark.integration
class TestPaymentPolicy:
    def test_get_payment_policies(self, ebay: EbayClient):
        result = ebay.sell_account.get_payment_policies("EBAY_US")
        assert isinstance(result, dict)


@pytest.mark.integration
class TestReturnPolicy:
    def test_get_return_policies(self, ebay: EbayClient):
        result = ebay.sell_account.get_return_policies("EBAY_US")
        assert isinstance(result, dict)


@pytest.mark.integration
class TestPrivilege:
    def test_get_privileges(self, ebay: EbayClient):
        result = ebay.sell_account.get_privileges()
        assert isinstance(result, dict)


@pytest.mark.integration
class TestProgram:
    def test_get_opted_in_programs(self, ebay: EbayClient):
        result = ebay.sell_account.get_opted_in_programs()
        assert isinstance(result, dict)
