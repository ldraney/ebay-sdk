"""Sell Fulfillment API — manage orders and shipping.

Spec: https://developer.ebay.com/api-docs/master/sell/fulfillment/openapi/3/sell_fulfillment_v1_oas3.json
Version: v1.20.7
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ebay_sdk.client import EbayClient

_BASE = "/sell/fulfillment/v1"


class SellFulfillmentApi:
    def __init__(self, client: EbayClient) -> None:
        self._c = client

    # -- Orders ----------------------------------------------------------------

    def get_orders(
        self,
        *,
        filter: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        order_ids: str | None = None,
        fieldgroups: str | None = None,
    ) -> Any:
        """Get seller orders with optional filters."""
        params: dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if order_ids is not None:
            params["orderIds"] = order_ids
        if fieldgroups is not None:
            params["fieldGroups"] = fieldgroups
        return self._c.get(f"{_BASE}/order", params=params)

    def get_order(self, order_id: str, *, fieldgroups: str | None = None) -> Any:
        """Get a specific order."""
        params: dict[str, Any] = {}
        if fieldgroups is not None:
            params["fieldGroups"] = fieldgroups
        return self._c.get(f"{_BASE}/order/{order_id}", params=params)

    def issue_refund(self, order_id: str, body: dict[str, Any]) -> Any:
        """Issue a refund for an order."""
        return self._c.post(f"{_BASE}/order/{order_id}/issue_refund", json=body)

    # -- Shipping Fulfillment --------------------------------------------------

    def get_shipping_fulfillments(self, order_id: str) -> Any:
        """Get shipping fulfillments for an order."""
        return self._c.get(f"{_BASE}/order/{order_id}/shipping_fulfillment")

    def get_shipping_fulfillment(
        self, order_id: str, fulfillment_id: str
    ) -> Any:
        """Get a specific shipping fulfillment."""
        return self._c.get(
            f"{_BASE}/order/{order_id}/shipping_fulfillment/{fulfillment_id}"
        )

    def create_shipping_fulfillment(
        self, order_id: str, body: dict[str, Any]
    ) -> Any:
        """Create a shipping fulfillment (mark items as shipped)."""
        return self._c.post(
            f"{_BASE}/order/{order_id}/shipping_fulfillment", json=body
        )

    # -- Payment Dispute -------------------------------------------------------

    def get_payment_disputes(
        self,
        *,
        order_id: str | None = None,
        buyer_username: str | None = None,
        open_date_from: str | None = None,
        open_date_to: str | None = None,
        payment_dispute_status: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """Get payment disputes with optional filters."""
        params: dict[str, Any] = {}
        if order_id is not None:
            params["order_id"] = order_id
        if buyer_username is not None:
            params["buyer_username"] = buyer_username
        if open_date_from is not None:
            params["open_date_from"] = open_date_from
        if open_date_to is not None:
            params["open_date_to"] = open_date_to
        if payment_dispute_status is not None:
            params["payment_dispute_status"] = payment_dispute_status
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/payment_dispute", params=params)

    def get_payment_dispute(self, payment_dispute_id: str) -> Any:
        """Get a specific payment dispute."""
        return self._c.get(f"{_BASE}/payment_dispute/{payment_dispute_id}")

    def accept_payment_dispute(
        self, payment_dispute_id: str, body: dict[str, Any] | None = None
    ) -> Any:
        """Accept a payment dispute."""
        return self._c.post(
            f"{_BASE}/payment_dispute/{payment_dispute_id}/accept", json=body
        )

    def contest_payment_dispute(
        self, payment_dispute_id: str, body: dict[str, Any]
    ) -> Any:
        """Contest a payment dispute."""
        return self._c.post(
            f"{_BASE}/payment_dispute/{payment_dispute_id}/contest", json=body
        )

    def get_payment_dispute_activity(self, payment_dispute_id: str) -> Any:
        """Get activity for a payment dispute."""
        return self._c.get(
            f"{_BASE}/payment_dispute/{payment_dispute_id}/activity"
        )

    def fetch_evidence_content(
        self,
        payment_dispute_id: str,
        evidence_id: str,
        file_id: str,
    ) -> Any:
        """Fetch evidence content for a payment dispute."""
        return self._c.get(
            f"{_BASE}/payment_dispute/{payment_dispute_id}/fetch_evidence_content",
            params={"evidence_id": evidence_id, "file_id": file_id},
        )

    def add_evidence(
        self, payment_dispute_id: str, body: dict[str, Any]
    ) -> Any:
        """Add evidence to a payment dispute."""
        return self._c.post(
            f"{_BASE}/payment_dispute/{payment_dispute_id}/add_evidence", json=body
        )

    def update_evidence(
        self, payment_dispute_id: str, body: dict[str, Any]
    ) -> Any:
        """Update evidence for a payment dispute."""
        return self._c.post(
            f"{_BASE}/payment_dispute/{payment_dispute_id}/update_evidence",
            json=body,
        )
