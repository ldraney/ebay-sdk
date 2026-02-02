"""Integration tests for Sell Finances API.

Spec: https://developer.ebay.com/api-docs/master/sell/finances/openapi/3/sell_finances_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient
from ebay_sdk.client import EbayApiError


@pytest.mark.integration
class TestPayouts:
    def test_get_payouts(self, ebay: EbayClient):
        result = ebay.sell_finances.get_payouts(limit=5)
        assert isinstance(result, dict)

    def test_get_payouts_with_filter(self, ebay: EbayClient):
        try:
            result = ebay.sell_finances.get_payouts(
                limit=5, sort="payoutDate"
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(f"get_payouts with sort failed: {exc.status_code}")
            raise

    def test_get_payout(self, ebay: EbayClient):
        payouts = ebay.sell_finances.get_payouts(limit=1)
        items = payouts.get("payouts", [])
        if not items:
            pytest.skip("No payouts available in sandbox")
        payout_id = items[0]["payoutId"]
        result = ebay.sell_finances.get_payout(payout_id)
        assert isinstance(result, dict)
        assert result["payoutId"] == payout_id

    def test_get_payout_summary(self, ebay: EbayClient):
        result = ebay.sell_finances.get_payout_summary()
        assert isinstance(result, dict)

    def test_get_payout_summary_with_filter(self, ebay: EbayClient):
        try:
            result = ebay.sell_finances.get_payout_summary(
                filter="payoutDate:[2024-01-01T00:00:00.000Z..2026-12-31T23:59:59.999Z]"
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"get_payout_summary with filter failed: {exc.status_code}"
                )
            raise


@pytest.mark.integration
class TestTransactions:
    def test_get_transactions(self, ebay: EbayClient):
        result = ebay.sell_finances.get_transactions(limit=5)
        assert isinstance(result, dict)

    def test_get_transactions_with_sort(self, ebay: EbayClient):
        try:
            result = ebay.sell_finances.get_transactions(
                limit=5, sort="transactionDate"
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"get_transactions with sort failed: {exc.status_code}"
                )
            raise

    def test_get_transaction_summary(self, ebay: EbayClient):
        result = ebay.sell_finances.get_transaction_summary()
        assert isinstance(result, dict)

    def test_get_transaction_summary_with_filter(self, ebay: EbayClient):
        try:
            result = ebay.sell_finances.get_transaction_summary(
                filter="transactionDate:[2024-01-01T00:00:00.000Z..2026-12-31T23:59:59.999Z]"
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"get_transaction_summary with filter failed: {exc.status_code}"
                )
            raise


@pytest.mark.integration
class TestTransfer:
    def test_get_transfer(self, ebay: EbayClient):
        # Transfers are rare — try a known ID and skip if not found
        try:
            result = ebay.sell_finances.get_transfer("SDK-TEST-TRANSFER-001")
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"get_transfer not available: {exc.status_code}"
                )
            raise


@pytest.mark.integration
class TestSellerFunds:
    def test_get_seller_funds_summary(self, ebay: EbayClient):
        result = ebay.sell_finances.get_seller_funds_summary()
        assert isinstance(result, dict)


@pytest.mark.integration
class TestWithholdingTax:
    def test_get_withholding_tax(self, ebay: EbayClient):
        try:
            result = ebay.sell_finances.get_withholding_tax(limit=5)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"get_withholding_tax not available: {exc.status_code}"
                )
            raise

    def test_get_withholding_tax_with_filter(self, ebay: EbayClient):
        try:
            result = ebay.sell_finances.get_withholding_tax(
                limit=5,
                filter="transactionDate:[2024-01-01T00:00:00.000Z..2026-12-31T23:59:59.999Z]",
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"get_withholding_tax with filter failed: {exc.status_code}"
                )
            raise
