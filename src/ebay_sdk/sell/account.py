"""Sell Account API — manage seller policies, programs, and privileges.

Spec: https://developer.ebay.com/api-docs/master/sell/account/openapi/3/sell_account_v1_oas3.json
Version: v1.9.3
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ebay_sdk.client import EbayClient

_BASE = "/sell/account/v1"


class SellAccountApi:
    def __init__(self, client: EbayClient) -> None:
        self._c = client

    # -- Custom Policy ---------------------------------------------------------

    def get_custom_policies(self, *, policy_types: str | None = None) -> Any:
        """List custom policies."""
        params: dict[str, Any] = {}
        if policy_types is not None:
            params["policy_types"] = policy_types
        return self._c.get(f"{_BASE}/custom_policy/", params=params)

    def create_custom_policy(self, body: dict[str, Any]) -> Any:
        """Create a custom policy."""
        return self._c.post(f"{_BASE}/custom_policy/", json=body)

    def get_custom_policy(self, custom_policy_id: str) -> Any:
        """Get a specific custom policy."""
        return self._c.get(f"{_BASE}/custom_policy/{custom_policy_id}")

    def update_custom_policy(
        self, custom_policy_id: str, body: dict[str, Any]
    ) -> Any:
        """Update a custom policy."""
        return self._c.put(f"{_BASE}/custom_policy/{custom_policy_id}", json=body)

    # -- Fulfillment Policy ----------------------------------------------------

    def get_fulfillment_policies(self, marketplace_id: str) -> Any:
        """List fulfillment policies for a marketplace."""
        return self._c.get(
            f"{_BASE}/fulfillment_policy",
            params={"marketplace_id": marketplace_id},
        )

    def create_fulfillment_policy(self, body: dict[str, Any]) -> Any:
        """Create a fulfillment policy."""
        return self._c.post(f"{_BASE}/fulfillment_policy", json=body)

    def get_fulfillment_policy(self, fulfillment_policy_id: str) -> Any:
        """Get a specific fulfillment policy."""
        return self._c.get(
            f"{_BASE}/fulfillment_policy/{fulfillment_policy_id}"
        )

    def update_fulfillment_policy(
        self, fulfillment_policy_id: str, body: dict[str, Any]
    ) -> Any:
        """Update a fulfillment policy."""
        return self._c.put(
            f"{_BASE}/fulfillment_policy/{fulfillment_policy_id}", json=body
        )

    def delete_fulfillment_policy(self, fulfillment_policy_id: str) -> Any:
        """Delete a fulfillment policy."""
        return self._c.delete(
            f"{_BASE}/fulfillment_policy/{fulfillment_policy_id}"
        )

    def get_fulfillment_policy_by_name(
        self, marketplace_id: str, name: str
    ) -> Any:
        """Get a fulfillment policy by name."""
        return self._c.get(
            f"{_BASE}/fulfillment_policy/get_by_policy_name",
            params={"marketplace_id": marketplace_id, "name": name},
        )

    # -- Payment Policy --------------------------------------------------------

    def get_payment_policies(self, marketplace_id: str) -> Any:
        """List payment policies for a marketplace."""
        return self._c.get(
            f"{_BASE}/payment_policy",
            params={"marketplace_id": marketplace_id},
        )

    def create_payment_policy(self, body: dict[str, Any]) -> Any:
        """Create a payment policy."""
        return self._c.post(f"{_BASE}/payment_policy", json=body)

    def get_payment_policy(self, payment_policy_id: str) -> Any:
        """Get a specific payment policy."""
        return self._c.get(f"{_BASE}/payment_policy/{payment_policy_id}")

    def update_payment_policy(
        self, payment_policy_id: str, body: dict[str, Any]
    ) -> Any:
        """Update a payment policy."""
        return self._c.put(
            f"{_BASE}/payment_policy/{payment_policy_id}", json=body
        )

    def delete_payment_policy(self, payment_policy_id: str) -> Any:
        """Delete a payment policy."""
        return self._c.delete(f"{_BASE}/payment_policy/{payment_policy_id}")

    def get_payment_policy_by_name(
        self, marketplace_id: str, name: str
    ) -> Any:
        """Get a payment policy by name."""
        return self._c.get(
            f"{_BASE}/payment_policy/get_by_policy_name",
            params={"marketplace_id": marketplace_id, "name": name},
        )

    # -- Return Policy ---------------------------------------------------------

    def get_return_policies(self, marketplace_id: str) -> Any:
        """List return policies for a marketplace."""
        return self._c.get(
            f"{_BASE}/return_policy",
            params={"marketplace_id": marketplace_id},
        )

    def create_return_policy(self, body: dict[str, Any]) -> Any:
        """Create a return policy."""
        return self._c.post(f"{_BASE}/return_policy", json=body)

    def get_return_policy(self, return_policy_id: str) -> Any:
        """Get a specific return policy."""
        return self._c.get(f"{_BASE}/return_policy/{return_policy_id}")

    def update_return_policy(
        self, return_policy_id: str, body: dict[str, Any]
    ) -> Any:
        """Update a return policy."""
        return self._c.put(
            f"{_BASE}/return_policy/{return_policy_id}", json=body
        )

    def delete_return_policy(self, return_policy_id: str) -> Any:
        """Delete a return policy."""
        return self._c.delete(f"{_BASE}/return_policy/{return_policy_id}")

    def get_return_policy_by_name(
        self, marketplace_id: str, name: str
    ) -> Any:
        """Get a return policy by name."""
        return self._c.get(
            f"{_BASE}/return_policy/get_by_policy_name",
            params={"marketplace_id": marketplace_id, "name": name},
        )

    # -- Payments Program ------------------------------------------------------

    def get_payments_program(
        self, marketplace_id: str, payments_program_type: str
    ) -> Any:
        """Get seller enrollment status in a payments program."""
        return self._c.get(
            f"{_BASE}/payments_program/{marketplace_id}/{payments_program_type}"
        )

    def get_payments_program_onboarding(
        self, marketplace_id: str, payments_program_type: str
    ) -> Any:
        """Get seller onboarding status for a payments program."""
        return self._c.get(
            f"{_BASE}/payments_program/{marketplace_id}/{payments_program_type}/onboarding"
        )

    # -- Privilege -------------------------------------------------------------

    def get_privileges(self) -> Any:
        """Get seller privileges."""
        return self._c.get(f"{_BASE}/privilege")

    # -- Program ---------------------------------------------------------------

    def get_opted_in_programs(self) -> Any:
        """List programs the seller has opted into."""
        return self._c.get(f"{_BASE}/program/get_opted_in_programs")

    def opt_in_to_program(self, body: dict[str, Any]) -> Any:
        """Opt into a seller program."""
        return self._c.post(f"{_BASE}/program/opt_in", json=body)

    def opt_out_of_program(self, body: dict[str, Any]) -> Any:
        """Opt out of a seller program."""
        return self._c.post(f"{_BASE}/program/opt_out", json=body)

    # -- KYC -------------------------------------------------------------------

    def get_kyc(self) -> Any:
        """Get KYC (Know Your Customer) checks for the seller."""
        return self._c.get(f"{_BASE}/kyc")

    # -- Rate Table ------------------------------------------------------------

    def get_rate_tables(self, *, country_code: str | None = None) -> Any:
        """Get shipping rate tables."""
        params: dict[str, Any] = {}
        if country_code is not None:
            params["country_code"] = country_code
        return self._c.get(f"{_BASE}/rate_table", params=params)

    # -- Subscription ----------------------------------------------------------

    def get_subscription(
        self, *, limit: int | None = None, offset: int | None = None
    ) -> Any:
        """Get seller subscriptions."""
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/subscription", params=params)

    # -- Sales Tax (legacy) ----------------------------------------------------

    def get_sales_taxes(self, country_code: str) -> Any:
        """Get sales tax jurisdictions."""
        return self._c.get(
            f"{_BASE}/sales_tax",
            params={"country_code": country_code},
        )

    def get_sales_tax(self, country_code: str, jurisdiction_id: str) -> Any:
        """Get a specific sales tax entry."""
        return self._c.get(
            f"{_BASE}/sales_tax/{country_code}/{jurisdiction_id}"
        )

    def create_or_replace_sales_tax(
        self, country_code: str, jurisdiction_id: str, body: dict[str, Any]
    ) -> Any:
        """Create or replace a sales tax entry."""
        return self._c.put(
            f"{_BASE}/sales_tax/{country_code}/{jurisdiction_id}", json=body
        )

    def delete_sales_tax(self, country_code: str, jurisdiction_id: str) -> Any:
        """Delete a sales tax entry."""
        return self._c.delete(
            f"{_BASE}/sales_tax/{country_code}/{jurisdiction_id}"
        )
