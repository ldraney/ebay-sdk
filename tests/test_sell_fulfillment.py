"""Integration tests for Sell Fulfillment API.

Spec: https://developer.ebay.com/api-docs/master/sell/fulfillment/openapi/3/sell_fulfillment_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient
from ebay_sdk.client import EbayApiError


@pytest.mark.integration
class TestOrders:
    def test_get_orders(self, ebay: EbayClient):
        result = ebay.sell_fulfillment.get_orders(limit=5)
        assert isinstance(result, dict)
        assert "orders" in result or "total" in result

    def test_get_order(self, ebay: EbayClient):
        orders = ebay.sell_fulfillment.get_orders(limit=1)
        items = orders.get("orders", [])
        if not items:
            pytest.skip("No orders available in sandbox")
        order_id = items[0]["orderId"]
        result = ebay.sell_fulfillment.get_order(order_id)
        assert isinstance(result, dict)
        assert result["orderId"] == order_id

    def test_issue_refund(self, ebay: EbayClient):
        orders = ebay.sell_fulfillment.get_orders(limit=1)
        items = orders.get("orders", [])
        if not items:
            pytest.skip("No orders available for refund test in sandbox")
        order_id = items[0]["orderId"]
        body = {
            "reasonForRefund": "BUYER_CANCEL",
            "comment": "SDK integration test — not a real refund",
            "orderLevelRefundAmount": {
                "value": "0.01",
                "currency": "USD",
            },
        }
        try:
            result = ebay.sell_fulfillment.issue_refund(order_id, body)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"issue_refund not available: {exc.status_code}")
            raise


@pytest.mark.integration
class TestShippingFulfillment:
    def test_get_shipping_fulfillments(self, ebay: EbayClient):
        orders = ebay.sell_fulfillment.get_orders(limit=1)
        items = orders.get("orders", [])
        if not items:
            pytest.skip("No orders available for shipping fulfillment test")
        order_id = items[0]["orderId"]
        try:
            result = ebay.sell_fulfillment.get_shipping_fulfillments(order_id)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"get_shipping_fulfillments not available: {exc.status_code}"
                )
            raise

    def test_get_shipping_fulfillment(self, ebay: EbayClient):
        orders = ebay.sell_fulfillment.get_orders(limit=5)
        items = orders.get("orders", [])
        if not items:
            pytest.skip("No orders available in sandbox")
        # Look for an order that has fulfillments
        for order in items:
            order_id = order["orderId"]
            try:
                fulfillments = ebay.sell_fulfillment.get_shipping_fulfillments(
                    order_id
                )
                ff_list = fulfillments.get("fulfillments", [])
                if ff_list:
                    ff_id = ff_list[0]["fulfillmentId"]
                    result = ebay.sell_fulfillment.get_shipping_fulfillment(
                        order_id, ff_id
                    )
                    assert isinstance(result, dict)
                    assert result["fulfillmentId"] == ff_id
                    return
            except EbayApiError:
                continue
        pytest.skip("No shipping fulfillments found on any order in sandbox")

    def test_create_shipping_fulfillment(self, ebay: EbayClient):
        orders = ebay.sell_fulfillment.get_orders(limit=5)
        items = orders.get("orders", [])
        if not items:
            pytest.skip("No orders available for create_shipping_fulfillment")
        # Find an order with line items to attempt fulfillment
        for order in items:
            line_items = order.get("lineItems", [])
            if not line_items:
                continue
            order_id = order["orderId"]
            body = {
                "lineItems": [
                    {
                        "lineItemId": line_items[0]["lineItemId"],
                        "quantity": 1,
                    }
                ],
                "shippedDate": "2024-01-15T00:00:00.000Z",
                "shippingCarrierCode": "USPS",
                "trackingNumber": "SDK-TEST-TRACK-001",
            }
            try:
                result = ebay.sell_fulfillment.create_shipping_fulfillment(
                    order_id, body
                )
                assert isinstance(result, dict)
                return
            except EbayApiError as exc:
                if exc.status_code in (400, 403, 404, 409):
                    pytest.skip(
                        f"create_shipping_fulfillment not available: "
                        f"{exc.status_code}"
                    )
                    return
                raise
        pytest.skip("No orders with line items found in sandbox")


@pytest.mark.integration
class TestPaymentDisputes:
    def test_get_payment_disputes(self, ebay: EbayClient):
        result = ebay.sell_fulfillment.get_payment_disputes(limit=5)
        assert isinstance(result, dict)

    def test_get_payment_dispute(self, ebay: EbayClient):
        disputes = ebay.sell_fulfillment.get_payment_disputes(limit=1)
        items = disputes.get("paymentDisputeSummaries", [])
        if not items:
            pytest.skip("No payment disputes available in sandbox")
        dispute_id = items[0]["paymentDisputeId"]
        result = ebay.sell_fulfillment.get_payment_dispute(dispute_id)
        assert isinstance(result, dict)
        assert result["paymentDisputeId"] == dispute_id

    def test_accept_payment_dispute(self, ebay: EbayClient):
        disputes = ebay.sell_fulfillment.get_payment_disputes(limit=5)
        items = disputes.get("paymentDisputeSummaries", [])
        if not items:
            pytest.skip("No payment disputes available for accept test")
        dispute_id = items[0]["paymentDisputeId"]
        try:
            result = ebay.sell_fulfillment.accept_payment_dispute(
                dispute_id, {"revision": 1}
            )
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(
                    f"accept_payment_dispute not available: {exc.status_code}"
                )
            raise

    def test_contest_payment_dispute(self, ebay: EbayClient):
        disputes = ebay.sell_fulfillment.get_payment_disputes(limit=5)
        items = disputes.get("paymentDisputeSummaries", [])
        if not items:
            pytest.skip("No payment disputes available for contest test")
        dispute_id = items[0]["paymentDisputeId"]
        body = {
            "revision": 1,
            "note": "SDK integration test contest",
        }
        try:
            result = ebay.sell_fulfillment.contest_payment_dispute(
                dispute_id, body
            )
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(
                    f"contest_payment_dispute not available: {exc.status_code}"
                )
            raise

    def test_get_payment_dispute_activity(self, ebay: EbayClient):
        disputes = ebay.sell_fulfillment.get_payment_disputes(limit=1)
        items = disputes.get("paymentDisputeSummaries", [])
        if not items:
            pytest.skip("No payment disputes available for activity test")
        dispute_id = items[0]["paymentDisputeId"]
        try:
            result = ebay.sell_fulfillment.get_payment_dispute_activity(
                dispute_id
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"get_payment_dispute_activity not available: "
                    f"{exc.status_code}"
                )
            raise

    def test_fetch_evidence_content(self, ebay: EbayClient):
        disputes = ebay.sell_fulfillment.get_payment_disputes(limit=5)
        items = disputes.get("paymentDisputeSummaries", [])
        if not items:
            pytest.skip("No payment disputes available for evidence content test")
        # Need a dispute with evidence to fetch content
        for item in items:
            dispute_id = item["paymentDisputeId"]
            try:
                dispute = ebay.sell_fulfillment.get_payment_dispute(dispute_id)
                evidence_list = dispute.get("evidence", [])
                if not evidence_list:
                    continue
                evidence = evidence_list[0]
                evidence_id = evidence.get("evidenceId", "")
                files = evidence.get("files", [])
                if not files:
                    continue
                file_id = files[0].get("fileId", "")
                result = ebay.sell_fulfillment.fetch_evidence_content(
                    dispute_id, evidence_id, file_id
                )
                assert result is not None
                return
            except EbayApiError:
                continue
        pytest.skip("No disputes with evidence found in sandbox")

    def test_add_evidence(self, ebay: EbayClient):
        disputes = ebay.sell_fulfillment.get_payment_disputes(limit=5)
        items = disputes.get("paymentDisputeSummaries", [])
        if not items:
            pytest.skip("No payment disputes available for add_evidence test")
        dispute_id = items[0]["paymentDisputeId"]
        body = {
            "evidenceType": "PROOF_OF_DELIVERY",
            "lineItems": [],
        }
        try:
            result = ebay.sell_fulfillment.add_evidence(dispute_id, body)
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"add_evidence not available: {exc.status_code}")
            raise

    def test_update_evidence(self, ebay: EbayClient):
        disputes = ebay.sell_fulfillment.get_payment_disputes(limit=5)
        items = disputes.get("paymentDisputeSummaries", [])
        if not items:
            pytest.skip("No payment disputes available for update_evidence test")
        dispute_id = items[0]["paymentDisputeId"]
        body = {
            "evidenceType": "PROOF_OF_DELIVERY",
            "lineItems": [],
        }
        try:
            result = ebay.sell_fulfillment.update_evidence(dispute_id, body)
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(
                    f"update_evidence not available: {exc.status_code}"
                )
            raise
