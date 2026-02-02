"""Integration tests for Sell Account API.

Spec: https://developer.ebay.com/api-docs/master/sell/account/openapi/3/sell_account_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient
from ebay_sdk.client import EbayApiError


# ---------------------------------------------------------------------------
# Custom Policy (4 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestCustomPolicy:
    def test_get_custom_policies(self, ebay: EbayClient):
        result = ebay.sell_account.get_custom_policies()
        assert isinstance(result, dict)

    def test_get_custom_policies_with_type_filter(self, ebay: EbayClient):
        result = ebay.sell_account.get_custom_policies(
            policy_types="PRODUCT_COMPLIANCE"
        )
        assert isinstance(result, dict)

    def test_custom_policy_crud(self, ebay: EbayClient):
        """create -> get -> update for custom policy (no delete endpoint)."""
        body = {
            "name": "SDK-TEST-CUSTOM-001",
            "policyType": "PRODUCT_COMPLIANCE",
            "description": "Integration test custom policy",
            "label": "SDK Test Label",
        }
        try:
            created = ebay.sell_account.create_custom_policy(body)
            assert isinstance(created, dict)
            policy_id = created.get("customPolicyId") or created.get("custom_policy_id")
            assert policy_id is not None

            # get
            fetched = ebay.sell_account.get_custom_policy(str(policy_id))
            assert isinstance(fetched, dict)

            # update
            body["description"] = "Updated by integration test"
            updated = ebay.sell_account.update_custom_policy(
                str(policy_id), body
            )
            # update may return 200 with body or 204 empty
            assert updated is None or isinstance(updated, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(f"Custom policy CRUD not available: {exc.status_code}")
            raise

    def test_get_custom_policy_from_list(self, ebay: EbayClient):
        """Fetch list and get first policy by ID (state-dependent)."""
        policies = ebay.sell_account.get_custom_policies()
        items = policies.get("customPolicies") or policies.get("custom_policies", [])
        if not items:
            pytest.skip("No custom policies exist to fetch by ID")
        policy_id = str(
            items[0].get("customPolicyId") or items[0].get("custom_policy_id")
        )
        result = ebay.sell_account.get_custom_policy(policy_id)
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Fulfillment Policy (6 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestFulfillmentPolicy:
    def test_get_fulfillment_policies(self, ebay: EbayClient):
        result = ebay.sell_account.get_fulfillment_policies("EBAY_US")
        assert isinstance(result, dict)

    def test_fulfillment_policy_crud(self, ebay: EbayClient):
        """create -> get -> get_by_name -> update -> delete."""
        policy_name = "SDK-TEST-FULFILL-001"
        body = {
            "name": policy_name,
            "marketplaceId": "EBAY_US",
            "categoryTypes": [{"name": "ALL_EXCLUDING_MOTORS_VEHICLES"}],
            "handlingTime": {"unit": "DAY", "value": 1},
            "shippingOptions": [
                {
                    "optionType": "DOMESTIC",
                    "costType": "FLAT_RATE",
                    "shippingServices": [
                        {
                            "shippingCarrierCode": "USPS",
                            "shippingServiceCode": "USPSPriorityFlatRateBox",
                            "shippingCost": {"value": "5.00", "currency": "USD"},
                            "sortOrder": 1,
                        }
                    ],
                }
            ],
        }
        created = None
        try:
            created = ebay.sell_account.create_fulfillment_policy(body)
            assert isinstance(created, dict)
            policy_id = str(
                created.get("fulfillmentPolicyId")
                or created.get("fulfillment_policy_id")
            )
            assert policy_id

            # get by ID
            fetched = ebay.sell_account.get_fulfillment_policy(policy_id)
            assert isinstance(fetched, dict)

            # get by name
            by_name = ebay.sell_account.get_fulfillment_policy_by_name(
                "EBAY_US", policy_name
            )
            assert isinstance(by_name, dict)

            # update
            body["handlingTime"] = {"unit": "DAY", "value": 2}
            updated = ebay.sell_account.update_fulfillment_policy(policy_id, body)
            assert updated is None or isinstance(updated, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(
                    f"Fulfillment policy CRUD not available: {exc.status_code}"
                )
            raise
        finally:
            if created:
                pid = str(
                    created.get("fulfillmentPolicyId")
                    or created.get("fulfillment_policy_id")
                )
                try:
                    ebay.sell_account.delete_fulfillment_policy(pid)
                except EbayApiError:
                    pass

    def test_delete_fulfillment_policy_nonexistent(self, ebay: EbayClient):
        """Deleting a non-existent policy should raise an error."""
        with pytest.raises(EbayApiError) as exc_info:
            ebay.sell_account.delete_fulfillment_policy("0")
        assert exc_info.value.status_code in (400, 404)

    def test_get_fulfillment_policy_by_name_existing(self, ebay: EbayClient):
        """Fetch by name from an existing policy (state-dependent)."""
        policies = ebay.sell_account.get_fulfillment_policies("EBAY_US")
        items = policies.get("fulfillmentPolicies", [])
        if not items:
            pytest.skip("No fulfillment policies to look up by name")
        name = items[0]["name"]
        result = ebay.sell_account.get_fulfillment_policy_by_name("EBAY_US", name)
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Payment Policy (6 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestPaymentPolicy:
    def test_get_payment_policies(self, ebay: EbayClient):
        result = ebay.sell_account.get_payment_policies("EBAY_US")
        assert isinstance(result, dict)

    def test_payment_policy_crud(self, ebay: EbayClient):
        """create -> get -> get_by_name -> update -> delete."""
        policy_name = "SDK-TEST-PAY-001"
        body = {
            "name": policy_name,
            "marketplaceId": "EBAY_US",
            "categoryTypes": [{"name": "ALL_EXCLUDING_MOTORS_VEHICLES"}],
            "paymentMethods": [{"paymentMethodType": "PERSONAL_CHECK"}],
        }
        created = None
        try:
            created = ebay.sell_account.create_payment_policy(body)
            assert isinstance(created, dict)
            policy_id = str(
                created.get("paymentPolicyId")
                or created.get("payment_policy_id")
            )
            assert policy_id

            # get by ID
            fetched = ebay.sell_account.get_payment_policy(policy_id)
            assert isinstance(fetched, dict)

            # get by name
            by_name = ebay.sell_account.get_payment_policy_by_name(
                "EBAY_US", policy_name
            )
            assert isinstance(by_name, dict)

            # update
            body["description"] = "Updated by SDK integration test"
            updated = ebay.sell_account.update_payment_policy(policy_id, body)
            assert updated is None or isinstance(updated, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(
                    f"Payment policy CRUD not available: {exc.status_code}"
                )
            raise
        finally:
            if created:
                pid = str(
                    created.get("paymentPolicyId")
                    or created.get("payment_policy_id")
                )
                try:
                    ebay.sell_account.delete_payment_policy(pid)
                except EbayApiError:
                    pass

    def test_delete_payment_policy_nonexistent(self, ebay: EbayClient):
        """Deleting a non-existent policy should raise an error."""
        with pytest.raises(EbayApiError) as exc_info:
            ebay.sell_account.delete_payment_policy("0")
        assert exc_info.value.status_code in (400, 404)

    def test_get_payment_policy_by_name_existing(self, ebay: EbayClient):
        """Fetch by name from an existing policy (state-dependent)."""
        policies = ebay.sell_account.get_payment_policies("EBAY_US")
        items = policies.get("paymentPolicies", [])
        if not items:
            pytest.skip("No payment policies to look up by name")
        name = items[0]["name"]
        result = ebay.sell_account.get_payment_policy_by_name("EBAY_US", name)
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Return Policy (6 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestReturnPolicy:
    def test_get_return_policies(self, ebay: EbayClient):
        result = ebay.sell_account.get_return_policies("EBAY_US")
        assert isinstance(result, dict)

    def test_return_policy_crud(self, ebay: EbayClient):
        """create -> get -> get_by_name -> update -> delete."""
        policy_name = "SDK-TEST-RETURN-001"
        body = {
            "name": policy_name,
            "marketplaceId": "EBAY_US",
            "categoryTypes": [{"name": "ALL_EXCLUDING_MOTORS_VEHICLES"}],
            "returnsAccepted": True,
            "returnPeriod": {"unit": "DAY", "value": 30},
            "refundMethod": "MONEY_BACK",
            "returnShippingCostPayer": "BUYER",
        }
        created = None
        try:
            created = ebay.sell_account.create_return_policy(body)
            assert isinstance(created, dict)
            policy_id = str(
                created.get("returnPolicyId")
                or created.get("return_policy_id")
            )
            assert policy_id

            # get by ID
            fetched = ebay.sell_account.get_return_policy(policy_id)
            assert isinstance(fetched, dict)

            # get by name
            by_name = ebay.sell_account.get_return_policy_by_name(
                "EBAY_US", policy_name
            )
            assert isinstance(by_name, dict)

            # update
            body["returnPeriod"] = {"unit": "DAY", "value": 60}
            updated = ebay.sell_account.update_return_policy(policy_id, body)
            assert updated is None or isinstance(updated, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(
                    f"Return policy CRUD not available: {exc.status_code}"
                )
            raise
        finally:
            if created:
                pid = str(
                    created.get("returnPolicyId")
                    or created.get("return_policy_id")
                )
                try:
                    ebay.sell_account.delete_return_policy(pid)
                except EbayApiError:
                    pass

    def test_delete_return_policy_nonexistent(self, ebay: EbayClient):
        """Deleting a non-existent policy should raise an error."""
        with pytest.raises(EbayApiError) as exc_info:
            ebay.sell_account.delete_return_policy("0")
        assert exc_info.value.status_code in (400, 404)

    def test_get_return_policy_by_name_existing(self, ebay: EbayClient):
        """Fetch by name from an existing policy (state-dependent)."""
        policies = ebay.sell_account.get_return_policies("EBAY_US")
        items = policies.get("returnPolicies", [])
        if not items:
            pytest.skip("No return policies to look up by name")
        name = items[0]["name"]
        result = ebay.sell_account.get_return_policy_by_name("EBAY_US", name)
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Payments Program (2 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestPaymentsProgram:
    def test_get_payments_program(self, ebay: EbayClient):
        try:
            result = ebay.sell_account.get_payments_program(
                "EBAY_US", "EBAY_PAYMENTS"
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"Payments program not available: {exc.status_code}"
                )
            raise

    def test_get_payments_program_onboarding(self, ebay: EbayClient):
        try:
            result = ebay.sell_account.get_payments_program_onboarding(
                "EBAY_US", "EBAY_PAYMENTS"
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"Payments program onboarding not available: {exc.status_code}"
                )
            raise


# ---------------------------------------------------------------------------
# Privilege (1 method)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestPrivilege:
    def test_get_privileges(self, ebay: EbayClient):
        result = ebay.sell_account.get_privileges()
        assert isinstance(result, dict)

    def test_get_privileges_has_fields(self, ebay: EbayClient):
        result = ebay.sell_account.get_privileges()
        # Response typically includes sellingLimit or sellerRegistrationCompleted
        assert isinstance(result, dict)
        assert len(result) > 0


# ---------------------------------------------------------------------------
# Program (3 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestProgram:
    def test_get_opted_in_programs(self, ebay: EbayClient):
        result = ebay.sell_account.get_opted_in_programs()
        assert isinstance(result, dict)

    def test_opt_in_to_program(self, ebay: EbayClient):
        """Attempt to opt in to a program; skip on 400/403."""
        try:
            result = ebay.sell_account.opt_in_to_program(
                {"programType": "SELLING_POLICY_MANAGEMENT"}
            )
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(f"Opt-in not available: {exc.status_code}")
            raise

    def test_opt_out_of_program(self, ebay: EbayClient):
        """Attempt to opt out of a program; skip on 400/403."""
        try:
            result = ebay.sell_account.opt_out_of_program(
                {"programType": "SELLING_POLICY_MANAGEMENT"}
            )
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(f"Opt-out not available: {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# KYC (1 method)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestKyc:
    def test_get_kyc(self, ebay: EbayClient):
        try:
            result = ebay.sell_account.get_kyc()
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"KYC not available: {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# Rate Table (1 method)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestRateTable:
    def test_get_rate_tables(self, ebay: EbayClient):
        result = ebay.sell_account.get_rate_tables()
        assert isinstance(result, dict)

    def test_get_rate_tables_with_country(self, ebay: EbayClient):
        result = ebay.sell_account.get_rate_tables(country_code="US")
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Subscription (1 method)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestSubscription:
    def test_get_subscription(self, ebay: EbayClient):
        result = ebay.sell_account.get_subscription()
        assert isinstance(result, dict)

    def test_get_subscription_with_pagination(self, ebay: EbayClient):
        result = ebay.sell_account.get_subscription(limit=10, offset=0)
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Sales Tax (4 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestSalesTax:
    def test_get_sales_taxes(self, ebay: EbayClient):
        result = ebay.sell_account.get_sales_taxes("US")
        assert isinstance(result, dict)

    def test_sales_tax_crud(self, ebay: EbayClient):
        """create_or_replace -> get -> delete for a sales tax entry."""
        country_code = "US"
        jurisdiction_id = "WA"
        body = {
            "salesTaxPercentage": "9.5",
            "shippingAndHandlingTaxed": True,
        }
        try:
            # create or replace
            result = ebay.sell_account.create_or_replace_sales_tax(
                country_code, jurisdiction_id, body
            )
            # 200/204 depending on create vs replace
            assert result is None or isinstance(result, dict)

            # get
            fetched = ebay.sell_account.get_sales_tax(
                country_code, jurisdiction_id
            )
            assert isinstance(fetched, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(f"Sales tax CRUD not available: {exc.status_code}")
            raise
        finally:
            try:
                ebay.sell_account.delete_sales_tax(country_code, jurisdiction_id)
            except EbayApiError:
                pass

    def test_get_sales_tax_nonexistent(self, ebay: EbayClient):
        """Getting a sales tax for a jurisdiction with no entry."""
        try:
            result = ebay.sell_account.get_sales_tax("US", "XX")
            # Could succeed with empty data or raise 404
            assert isinstance(result, dict)
        except EbayApiError as exc:
            assert exc.status_code in (400, 404)

    def test_delete_sales_tax_nonexistent(self, ebay: EbayClient):
        """Deleting a non-existent sales tax entry."""
        try:
            ebay.sell_account.delete_sales_tax("US", "XX")
        except EbayApiError as exc:
            assert exc.status_code in (400, 404)
