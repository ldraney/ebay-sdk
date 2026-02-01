"""Integration tests for Sell Feed API.

Spec: https://developer.ebay.com/api-docs/master/sell/feed/openapi/3/sell_feed_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient


@pytest.mark.integration
class TestTasks:
    def test_get_tasks(self, ebay: EbayClient):
        result = ebay.sell_feed.get_tasks(limit=5)
        assert isinstance(result, dict)


@pytest.mark.integration
class TestOrderTasks:
    def test_get_order_tasks(self, ebay: EbayClient):
        result = ebay.sell_feed.get_order_tasks(limit=5)
        assert isinstance(result, dict)


@pytest.mark.integration
class TestSchedules:
    def test_get_schedule_templates(self, ebay: EbayClient):
        result = ebay.sell_feed.get_schedule_templates("LMS_ORDER_REPORT")
        assert isinstance(result, dict)
