"""Sell Finances API — payouts, transactions, and transfer details.

Spec: https://developer.ebay.com/api-docs/master/sell/finances/openapi/3/sell_finances_v1_oas3.json
Version: v1.18.0
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ebay_sdk.client import EbayClient

_BASE = "/sell/finances/v1"


class SellFinancesApi:
    def __init__(self, client: EbayClient) -> None:
        self._c = client

    # -- Payout ----------------------------------------------------------------

    def get_payouts(
        self,
        *,
        filter: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """Get seller payouts."""
        params: dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/payout", params=params)

    def get_payout(self, payout_id: str) -> Any:
        """Get a specific payout."""
        return self._c.get(f"{_BASE}/payout/{payout_id}")

    def get_payout_summary(self, *, filter: str | None = None) -> Any:
        """Get summary of payouts."""
        params: dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        return self._c.get(f"{_BASE}/payout_summary", params=params)

    # -- Transaction -----------------------------------------------------------

    def get_transactions(
        self,
        *,
        filter: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """Get seller transactions."""
        params: dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/transaction", params=params)

    def get_transaction_summary(
        self, *, filter: str | None = None
    ) -> Any:
        """Get summary of transactions."""
        params: dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        return self._c.get(f"{_BASE}/transaction_summary", params=params)

    # -- Transfer --------------------------------------------------------------

    def get_transfer(self, transfer_id: str) -> Any:
        """Get a specific transfer."""
        return self._c.get(f"{_BASE}/transfer/{transfer_id}")

    # -- Seller Funds ----------------------------------------------------------

    def get_seller_funds_summary(self) -> Any:
        """Get seller funds summary (available, processing, on hold)."""
        return self._c.get(f"{_BASE}/seller_funds_summary")

    # -- Withholding Tax -------------------------------------------------------

    def get_withholding_tax(
        self,
        *,
        filter: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """Get withholding tax details."""
        params: dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/withholding_tax", params=params)
