"""Integration tests for Sell Marketing API.

Spec: https://developer.ebay.com/api-docs/master/sell/marketing/openapi/3/sell_marketing_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient


@pytest.mark.integration
class TestCampaigns:
    def test_get_campaigns(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_campaigns(limit=5)
        assert isinstance(result, dict)


@pytest.mark.integration
class TestPromotions:
    def test_get_promotions(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_promotions("EBAY_US", limit=5)
        assert isinstance(result, dict)


@pytest.mark.integration
class TestReports:
    def test_get_report_tasks(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_report_tasks(limit=5)
        assert isinstance(result, dict)

    def test_get_report_metadata(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_report_metadata()
        assert isinstance(result, dict)
