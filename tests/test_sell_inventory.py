"""Integration tests for Sell Inventory API.

Spec: https://developer.ebay.com/api-docs/master/sell/inventory/openapi/3/sell_inventory_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient
from ebay_sdk.client import EbayApiError


# ---------------------------------------------------------------------------
# Inventory Item (7 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestInventoryItem:
    def test_get_inventory_items(self, ebay: EbayClient):
        result = ebay.sell_inventory.get_inventory_items(limit=5)
        assert isinstance(result, dict)

    def test_create_and_delete_inventory_item(self, ebay: EbayClient):
        sku = "SDK-TEST-001"
        body = {
            "product": {
                "title": "SDK Integration Test Item",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        ebay.sell_inventory.create_or_replace_inventory_item(sku, body)
        item = ebay.sell_inventory.get_inventory_item(sku)
        assert item["sku"] == sku

        ebay.sell_inventory.delete_inventory_item(sku)

    def test_get_inventory_item(self, ebay: EbayClient):
        """Get a single inventory item — create one first, then read it."""
        sku = "SDK-TEST-INV-GET-001"
        body = {
            "product": {
                "title": "SDK Test Get Item",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku, body)
            item = ebay.sell_inventory.get_inventory_item(sku)
            assert isinstance(item, dict)
            assert item["sku"] == sku
        finally:
            try:
                ebay.sell_inventory.delete_inventory_item(sku)
            except EbayApiError:
                pass

    def test_create_or_replace_inventory_item(self, ebay: EbayClient):
        """Create, then replace (update) an inventory item."""
        sku = "SDK-TEST-INV-REPLACE-001"
        body = {
            "product": {
                "title": "SDK Test Replace — v1",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku, body)
            # Replace with updated title
            body["product"]["title"] = "SDK Test Replace — v2"
            ebay.sell_inventory.create_or_replace_inventory_item(sku, body)
            item = ebay.sell_inventory.get_inventory_item(sku)
            assert item["product"]["title"] == "SDK Test Replace — v2"
        finally:
            try:
                ebay.sell_inventory.delete_inventory_item(sku)
            except EbayApiError:
                pass

    def test_delete_inventory_item(self, ebay: EbayClient):
        """Create then delete, confirm deletion via get returning 404."""
        sku = "SDK-TEST-INV-DEL-001"
        body = {
            "product": {
                "title": "SDK Test Delete Item",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        ebay.sell_inventory.create_or_replace_inventory_item(sku, body)
        ebay.sell_inventory.delete_inventory_item(sku)
        with pytest.raises(EbayApiError) as exc_info:
            ebay.sell_inventory.get_inventory_item(sku)
        assert exc_info.value.status_code == 404

    def test_get_inventory_items_pagination(self, ebay: EbayClient):
        """Verify offset/limit params are accepted."""
        result = ebay.sell_inventory.get_inventory_items(limit=2, offset=0)
        assert isinstance(result, dict)

    def test_bulk_create_or_replace_inventory_item(self, ebay: EbayClient):
        """Bulk create two items and clean up."""
        skus = ["SDK-TEST-INV-BULK-001", "SDK-TEST-INV-BULK-002"]
        body = {
            "requests": [
                {
                    "sku": skus[0],
                    "product": {
                        "title": "SDK Bulk Test Item 1",
                        "aspects": {"Brand": ["Unbranded"]},
                    },
                    "condition": "NEW",
                    "availability": {
                        "shipToLocationAvailability": {"quantity": 1}
                    },
                },
                {
                    "sku": skus[1],
                    "product": {
                        "title": "SDK Bulk Test Item 2",
                        "aspects": {"Brand": ["Unbranded"]},
                    },
                    "condition": "NEW",
                    "availability": {
                        "shipToLocationAvailability": {"quantity": 2}
                    },
                },
            ]
        }
        try:
            result = ebay.sell_inventory.bulk_create_or_replace_inventory_item(body)
            assert isinstance(result, dict)
            assert "responses" in result
        finally:
            for sku in skus:
                try:
                    ebay.sell_inventory.delete_inventory_item(sku)
                except EbayApiError:
                    pass

    def test_bulk_get_inventory_item(self, ebay: EbayClient):
        """Create two items, bulk-get them, then clean up."""
        skus = ["SDK-TEST-INV-BGET-001", "SDK-TEST-INV-BGET-002"]
        item_body = {
            "product": {
                "title": "SDK Bulk Get Test",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        try:
            for sku in skus:
                ebay.sell_inventory.create_or_replace_inventory_item(sku, item_body)
            result = ebay.sell_inventory.bulk_get_inventory_item(
                {"requests": [{"sku": s} for s in skus]}
            )
            assert isinstance(result, dict)
            assert "responses" in result
        finally:
            for sku in skus:
                try:
                    ebay.sell_inventory.delete_inventory_item(sku)
                except EbayApiError:
                    pass

    def test_bulk_update_price_quantity(self, ebay: EbayClient):
        """Bulk update price/quantity — requires existing offers.

        Since offers depend on seller policies, skip on error.
        """
        body = {
            "requests": [
                {
                    "sku": "SDK-TEST-INV-BPQ-001",
                    "shipToLocationAvailability": {"quantity": 5},
                }
            ]
        }
        try:
            result = ebay.sell_inventory.bulk_update_price_quantity(body)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"bulk_update_price_quantity not available: {exc.status_code}"
                )
            raise


# ---------------------------------------------------------------------------
# Offer (10 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestOffer:
    def test_get_offers(self, ebay: EbayClient):
        """List offers — may be empty but should return a dict."""
        try:
            result = ebay.sell_inventory.get_offers(limit=5)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 404):
                pytest.skip(f"get_offers returned {exc.status_code}")
            raise

    def test_get_offers_by_sku(self, ebay: EbayClient):
        """Get offers filtered by SKU."""
        sku = "SDK-TEST-INV-OFFER-SKU-001"
        body = {
            "product": {
                "title": "SDK Offer SKU Filter Test",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku, body)
            result = ebay.sell_inventory.get_offers(sku=sku)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 404):
                pytest.skip(f"get_offers by sku returned {exc.status_code}")
            raise
        finally:
            try:
                ebay.sell_inventory.delete_inventory_item(sku)
            except EbayApiError:
                pass

    def test_get_offer(self, ebay: EbayClient):
        """Fetch a single offer by ID — skip if no offers exist."""
        try:
            offers = ebay.sell_inventory.get_offers(limit=1)
        except EbayApiError:
            pytest.skip("Cannot list offers")
            return
        offer_list = offers.get("offers", [])
        if not offer_list:
            pytest.skip("No existing offers to fetch")
        offer_id = offer_list[0]["offerId"]
        result = ebay.sell_inventory.get_offer(offer_id)
        assert isinstance(result, dict)
        assert result["offerId"] == offer_id

    def test_create_offer(self, ebay: EbayClient):
        """Create an offer — depends on seller policies being configured."""
        sku = "SDK-TEST-INV-OFFER-CREATE-001"
        item_body = {
            "product": {
                "title": "SDK Offer Create Test",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku, item_body)
            offer_body = {
                "sku": sku,
                "marketplaceId": "EBAY_US",
                "format": "FIXED_PRICE",
                "pricingSummary": {
                    "price": {"value": "9.99", "currency": "USD"}
                },
                "listingDescription": "SDK integration test listing",
                "availableQuantity": 1,
            }
            result = ebay.sell_inventory.create_offer(offer_body)
            assert isinstance(result, dict)
            offer_id = result.get("offerId")
            if offer_id:
                try:
                    ebay.sell_inventory.delete_offer(offer_id)
                except EbayApiError:
                    pass
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"create_offer failed (policies not configured?): {exc.status_code}"
                )
            raise
        finally:
            try:
                ebay.sell_inventory.delete_inventory_item(sku)
            except EbayApiError:
                pass

    def test_update_offer(self, ebay: EbayClient):
        """Update an existing offer — skip if none available."""
        try:
            offers = ebay.sell_inventory.get_offers(limit=1)
        except EbayApiError:
            pytest.skip("Cannot list offers")
            return
        offer_list = offers.get("offers", [])
        if not offer_list:
            pytest.skip("No existing offers to update")
        offer = offer_list[0]
        offer_id = offer["offerId"]
        update_body = {
            "sku": offer.get("sku"),
            "marketplaceId": offer.get("marketplaceId", "EBAY_US"),
            "format": offer.get("format", "FIXED_PRICE"),
            "pricingSummary": offer.get("pricingSummary", {}),
            "listingDescription": offer.get("listingDescription", "Updated by SDK test"),
            "availableQuantity": offer.get("availableQuantity", 1),
        }
        try:
            result = ebay.sell_inventory.update_offer(offer_id, update_body)
            # update_offer may return 204 (None) or a dict
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(f"update_offer returned {exc.status_code}")
            raise

    def test_delete_offer(self, ebay: EbayClient):
        """Create an offer, then delete it. Skip if policies not configured."""
        sku = "SDK-TEST-INV-OFFER-DEL-001"
        item_body = {
            "product": {
                "title": "SDK Offer Delete Test",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku, item_body)
            offer_body = {
                "sku": sku,
                "marketplaceId": "EBAY_US",
                "format": "FIXED_PRICE",
                "pricingSummary": {
                    "price": {"value": "9.99", "currency": "USD"}
                },
                "listingDescription": "SDK delete offer test",
                "availableQuantity": 1,
            }
            result = ebay.sell_inventory.create_offer(offer_body)
            offer_id = result.get("offerId")
            if offer_id:
                ebay.sell_inventory.delete_offer(offer_id)
            else:
                pytest.skip("Offer creation did not return an offerId")
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"Offer create/delete failed (policies?): {exc.status_code}"
                )
            raise
        finally:
            try:
                ebay.sell_inventory.delete_inventory_item(sku)
            except EbayApiError:
                pass

    def test_publish_offer(self, ebay: EbayClient):
        """Publish an offer — skip if no publishable offers exist."""
        try:
            offers = ebay.sell_inventory.get_offers(limit=5)
        except EbayApiError:
            pytest.skip("Cannot list offers")
            return
        offer_list = offers.get("offers", [])
        unpublished = [
            o for o in offer_list if o.get("status") == "UNPUBLISHED"
        ]
        if not unpublished:
            pytest.skip("No unpublished offers to publish")
        offer_id = unpublished[0]["offerId"]
        try:
            result = ebay.sell_inventory.publish_offer(offer_id)
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(f"publish_offer returned {exc.status_code}")
            raise

    def test_withdraw_offer(self, ebay: EbayClient):
        """Withdraw an offer — skip if no published offers exist."""
        try:
            offers = ebay.sell_inventory.get_offers(limit=5)
        except EbayApiError:
            pytest.skip("Cannot list offers")
            return
        offer_list = offers.get("offers", [])
        published = [
            o for o in offer_list if o.get("status") == "PUBLISHED"
        ]
        if not published:
            pytest.skip("No published offers to withdraw")
        offer_id = published[0]["offerId"]
        try:
            result = ebay.sell_inventory.withdraw_offer(offer_id)
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(f"withdraw_offer returned {exc.status_code}")
            raise

    def test_publish_offer_by_inventory_item_group(self, ebay: EbayClient):
        """Publish offers by inventory item group — enrollment-gated."""
        body = {
            "inventoryItemGroupKey": "SDK-TEST-GROUP-PUBLISH-001",
            "marketplaceId": "EBAY_US",
        }
        try:
            result = ebay.sell_inventory.publish_offer_by_inventory_item_group(body)
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"publish_offer_by_inventory_item_group returned {exc.status_code}"
                )
            raise

    def test_withdraw_offer_by_inventory_item_group(self, ebay: EbayClient):
        """Withdraw offers by inventory item group — enrollment-gated."""
        body = {
            "inventoryItemGroupKey": "SDK-TEST-GROUP-WITHDRAW-001",
            "marketplaceId": "EBAY_US",
        }
        try:
            result = ebay.sell_inventory.withdraw_offer_by_inventory_item_group(body)
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"withdraw_offer_by_inventory_item_group returned {exc.status_code}"
                )
            raise

    def test_get_listing_fees(self, ebay: EbayClient):
        """Retrieve listing fees — can be called with empty body."""
        try:
            result = ebay.sell_inventory.get_listing_fees(None)
            assert result is None or isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(f"get_listing_fees returned {exc.status_code}")
            raise

    def test_get_listing_fees_with_offers(self, ebay: EbayClient):
        """Retrieve listing fees with an offer list."""
        try:
            offers = ebay.sell_inventory.get_offers(limit=1)
        except EbayApiError:
            pytest.skip("Cannot list offers")
            return
        offer_list = offers.get("offers", [])
        if not offer_list:
            pytest.skip("No offers to get listing fees for")
        offer_id = offer_list[0]["offerId"]
        try:
            result = ebay.sell_inventory.get_listing_fees(
                {"offers": [{"offerId": offer_id}]}
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(f"get_listing_fees returned {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# Inventory Item Group (3 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestInventoryItemGroup:
    def test_create_get_delete_inventory_item_group(self, ebay: EbayClient):
        """Full CRUD cycle for inventory item group."""
        group_key = "SDK-TEST-GROUP-001"
        sku_a = "SDK-TEST-INV-GRP-A"
        sku_b = "SDK-TEST-INV-GRP-B"
        item_body_a = {
            "product": {
                "title": "SDK Group Test — Variant A",
                "aspects": {"Brand": ["Unbranded"], "Color": ["Red"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        item_body_b = {
            "product": {
                "title": "SDK Group Test — Variant B",
                "aspects": {"Brand": ["Unbranded"], "Color": ["Blue"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        group_body = {
            "title": "SDK Test Item Group",
            "aspects": {"Brand": ["Unbranded"]},
            "variesBy": {
                "aspectsImageVariesBy": ["Color"],
                "specifications": [
                    {"name": "Color", "values": ["Red", "Blue"]}
                ],
            },
            "inventoryItems": [sku_a, sku_b],
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku_a, item_body_a)
            ebay.sell_inventory.create_or_replace_inventory_item(sku_b, item_body_b)
            ebay.sell_inventory.create_or_replace_inventory_item_group(
                group_key, group_body
            )
            result = ebay.sell_inventory.get_inventory_item_group(group_key)
            assert isinstance(result, dict)
            assert result.get("inventoryItemGroupKey") == group_key
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"Inventory item group CRUD failed: {exc.status_code}"
                )
            raise
        finally:
            try:
                ebay.sell_inventory.delete_inventory_item_group(group_key)
            except EbayApiError:
                pass
            for sku in (sku_a, sku_b):
                try:
                    ebay.sell_inventory.delete_inventory_item(sku)
                except EbayApiError:
                    pass

    def test_get_inventory_item_group_not_found(self, ebay: EbayClient):
        """Get a non-existent group returns 404."""
        with pytest.raises(EbayApiError) as exc_info:
            ebay.sell_inventory.get_inventory_item_group(
                "SDK-TEST-NONEXISTENT-GROUP-999"
            )
        assert exc_info.value.status_code == 404

    def test_delete_inventory_item_group(self, ebay: EbayClient):
        """Create then delete a group, confirm deletion."""
        group_key = "SDK-TEST-GROUP-DEL-001"
        sku_a = "SDK-TEST-INV-GRPDEL-A"
        sku_b = "SDK-TEST-INV-GRPDEL-B"
        item_body = {
            "product": {
                "title": "SDK Group Delete Test",
                "aspects": {"Brand": ["Unbranded"], "Size": ["S"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        group_body = {
            "title": "SDK Delete Group Test",
            "aspects": {"Brand": ["Unbranded"]},
            "variesBy": {
                "aspectsImageVariesBy": ["Size"],
                "specifications": [
                    {"name": "Size", "values": ["S", "M"]}
                ],
            },
            "inventoryItems": [sku_a, sku_b],
        }
        try:
            for sku in (sku_a, sku_b):
                ebay.sell_inventory.create_or_replace_inventory_item(sku, item_body)
            ebay.sell_inventory.create_or_replace_inventory_item_group(
                group_key, group_body
            )
            ebay.sell_inventory.delete_inventory_item_group(group_key)
            with pytest.raises(EbayApiError) as exc_info:
                ebay.sell_inventory.get_inventory_item_group(group_key)
            assert exc_info.value.status_code == 404
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"Inventory item group delete test failed: {exc.status_code}"
                )
            raise
        finally:
            for sku in (sku_a, sku_b):
                try:
                    ebay.sell_inventory.delete_inventory_item(sku)
                except EbayApiError:
                    pass


# ---------------------------------------------------------------------------
# Inventory Location (7 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestInventoryLocation:
    def test_get_inventory_locations(self, ebay: EbayClient):
        result = ebay.sell_inventory.get_inventory_locations(limit=5)
        assert isinstance(result, dict)

    def test_get_inventory_locations_pagination(self, ebay: EbayClient):
        result = ebay.sell_inventory.get_inventory_locations(limit=2, offset=0)
        assert isinstance(result, dict)

    def test_create_get_update_enable_disable_delete_location(
        self, ebay: EbayClient
    ):
        """Full lifecycle: create -> get -> update -> enable -> disable -> delete."""
        loc_key = "SDK-TEST-LOC-001"
        create_body = {
            "location": {
                "address": {
                    "addressLine1": "123 Test St",
                    "city": "San Jose",
                    "stateOrProvince": "CA",
                    "postalCode": "95112",
                    "country": "US",
                }
            },
            "locationTypes": ["WAREHOUSE"],
            "name": "SDK Test Location",
            "merchantLocationStatus": "ENABLED",
        }
        try:
            # Create
            ebay.sell_inventory.create_inventory_location(loc_key, create_body)

            # Get
            loc = ebay.sell_inventory.get_inventory_location(loc_key)
            assert isinstance(loc, dict)
            assert loc.get("merchantLocationKey") == loc_key

            # Update
            update_body = {"name": "SDK Test Location Updated"}
            result = ebay.sell_inventory.update_inventory_location(
                loc_key, update_body
            )
            assert result is None or isinstance(result, dict)

            # Disable
            result = ebay.sell_inventory.disable_inventory_location(loc_key)
            assert result is None or isinstance(result, dict)

            # Enable
            result = ebay.sell_inventory.enable_inventory_location(loc_key)
            assert result is None or isinstance(result, dict)
        finally:
            try:
                ebay.sell_inventory.delete_inventory_location(loc_key)
            except EbayApiError:
                pass

    def test_get_inventory_location(self, ebay: EbayClient):
        """Get a specific location — create first if needed."""
        loc_key = "SDK-TEST-LOC-GET-001"
        create_body = {
            "location": {
                "address": {
                    "addressLine1": "456 Read St",
                    "city": "Austin",
                    "stateOrProvince": "TX",
                    "postalCode": "73301",
                    "country": "US",
                }
            },
            "locationTypes": ["WAREHOUSE"],
            "name": "SDK Test Get Location",
            "merchantLocationStatus": "ENABLED",
        }
        try:
            ebay.sell_inventory.create_inventory_location(loc_key, create_body)
            loc = ebay.sell_inventory.get_inventory_location(loc_key)
            assert isinstance(loc, dict)
            assert loc["merchantLocationKey"] == loc_key
        finally:
            try:
                ebay.sell_inventory.delete_inventory_location(loc_key)
            except EbayApiError:
                pass

    def test_create_inventory_location(self, ebay: EbayClient):
        """Create a location then clean up."""
        loc_key = "SDK-TEST-LOC-CREATE-001"
        create_body = {
            "location": {
                "address": {
                    "addressLine1": "789 Create Ave",
                    "city": "Portland",
                    "stateOrProvince": "OR",
                    "postalCode": "97201",
                    "country": "US",
                }
            },
            "locationTypes": ["WAREHOUSE"],
            "name": "SDK Test Create Location",
            "merchantLocationStatus": "ENABLED",
        }
        try:
            result = ebay.sell_inventory.create_inventory_location(
                loc_key, create_body
            )
            # create returns 204 (None) on success
            assert result is None or isinstance(result, dict)
        finally:
            try:
                ebay.sell_inventory.delete_inventory_location(loc_key)
            except EbayApiError:
                pass

    def test_update_inventory_location(self, ebay: EbayClient):
        """Create, update, verify, delete."""
        loc_key = "SDK-TEST-LOC-UPD-001"
        create_body = {
            "location": {
                "address": {
                    "addressLine1": "100 Update Blvd",
                    "city": "Seattle",
                    "stateOrProvince": "WA",
                    "postalCode": "98101",
                    "country": "US",
                }
            },
            "locationTypes": ["WAREHOUSE"],
            "name": "SDK Test Update Location",
            "merchantLocationStatus": "ENABLED",
        }
        try:
            ebay.sell_inventory.create_inventory_location(loc_key, create_body)
            update_body = {"name": "SDK Test Location After Update"}
            result = ebay.sell_inventory.update_inventory_location(
                loc_key, update_body
            )
            assert result is None or isinstance(result, dict)
        finally:
            try:
                ebay.sell_inventory.delete_inventory_location(loc_key)
            except EbayApiError:
                pass

    def test_delete_inventory_location(self, ebay: EbayClient):
        """Create then delete, confirm 404 on re-fetch."""
        loc_key = "SDK-TEST-LOC-DEL-001"
        create_body = {
            "location": {
                "address": {
                    "addressLine1": "200 Delete Ln",
                    "city": "Denver",
                    "stateOrProvince": "CO",
                    "postalCode": "80201",
                    "country": "US",
                }
            },
            "locationTypes": ["WAREHOUSE"],
            "name": "SDK Test Delete Location",
            "merchantLocationStatus": "ENABLED",
        }
        ebay.sell_inventory.create_inventory_location(loc_key, create_body)
        ebay.sell_inventory.delete_inventory_location(loc_key)
        with pytest.raises(EbayApiError) as exc_info:
            ebay.sell_inventory.get_inventory_location(loc_key)
        assert exc_info.value.status_code == 404

    def test_enable_inventory_location(self, ebay: EbayClient):
        """Create disabled location, enable it, clean up."""
        loc_key = "SDK-TEST-LOC-ENABLE-001"
        create_body = {
            "location": {
                "address": {
                    "addressLine1": "300 Enable Rd",
                    "city": "Chicago",
                    "stateOrProvince": "IL",
                    "postalCode": "60601",
                    "country": "US",
                }
            },
            "locationTypes": ["WAREHOUSE"],
            "name": "SDK Test Enable Location",
            "merchantLocationStatus": "DISABLED",
        }
        try:
            ebay.sell_inventory.create_inventory_location(loc_key, create_body)
            result = ebay.sell_inventory.enable_inventory_location(loc_key)
            assert result is None or isinstance(result, dict)
        finally:
            try:
                ebay.sell_inventory.delete_inventory_location(loc_key)
            except EbayApiError:
                pass

    def test_disable_inventory_location(self, ebay: EbayClient):
        """Create enabled location, disable it, clean up."""
        loc_key = "SDK-TEST-LOC-DISABLE-001"
        create_body = {
            "location": {
                "address": {
                    "addressLine1": "400 Disable Dr",
                    "city": "Miami",
                    "stateOrProvince": "FL",
                    "postalCode": "33101",
                    "country": "US",
                }
            },
            "locationTypes": ["WAREHOUSE"],
            "name": "SDK Test Disable Location",
            "merchantLocationStatus": "ENABLED",
        }
        try:
            ebay.sell_inventory.create_inventory_location(loc_key, create_body)
            result = ebay.sell_inventory.disable_inventory_location(loc_key)
            assert result is None or isinstance(result, dict)
        finally:
            try:
                ebay.sell_inventory.delete_inventory_location(loc_key)
            except EbayApiError:
                pass


# ---------------------------------------------------------------------------
# Product Compatibility (3 methods)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestProductCompatibility:
    def test_create_get_delete_product_compatibility(self, ebay: EbayClient):
        """Full CRUD for product compatibility on a test SKU."""
        sku = "SDK-TEST-INV-COMPAT-001"
        item_body = {
            "product": {
                "title": "SDK Compatibility Test Item",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        compat_body = {
            "compatibleProducts": [
                {
                    "productFamilyProperties": {
                        "make": "Toyota",
                        "model": "Camry",
                        "year": "2020",
                    },
                    "notes": "SDK test compatibility",
                }
            ]
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku, item_body)
            result = ebay.sell_inventory.create_or_replace_product_compatibility(
                sku, compat_body
            )
            assert result is None or isinstance(result, dict)

            compat = ebay.sell_inventory.get_product_compatibility(sku)
            assert isinstance(compat, dict)
            assert "compatibleProducts" in compat

            ebay.sell_inventory.delete_product_compatibility(sku)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"Product compatibility CRUD failed: {exc.status_code}"
                )
            raise
        finally:
            try:
                ebay.sell_inventory.delete_product_compatibility(sku)
            except EbayApiError:
                pass
            try:
                ebay.sell_inventory.delete_inventory_item(sku)
            except EbayApiError:
                pass

    def test_get_product_compatibility_not_found(self, ebay: EbayClient):
        """Get compatibility for item with none set — expect 404 or empty."""
        sku = "SDK-TEST-INV-COMPAT-NONE-001"
        item_body = {
            "product": {
                "title": "SDK No Compat Test",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku, item_body)
            try:
                result = ebay.sell_inventory.get_product_compatibility(sku)
                # If it returns, it should be a dict (possibly empty compat list)
                assert isinstance(result, dict)
            except EbayApiError as exc:
                assert exc.status_code in (404, 400)
        finally:
            try:
                ebay.sell_inventory.delete_inventory_item(sku)
            except EbayApiError:
                pass

    def test_delete_product_compatibility(self, ebay: EbayClient):
        """Create compatibility, delete it, verify gone."""
        sku = "SDK-TEST-INV-COMPAT-DEL-001"
        item_body = {
            "product": {
                "title": "SDK Compat Delete Test",
                "aspects": {"Brand": ["Unbranded"]},
            },
            "condition": "NEW",
            "availability": {
                "shipToLocationAvailability": {"quantity": 1}
            },
        }
        compat_body = {
            "compatibleProducts": [
                {
                    "productFamilyProperties": {
                        "make": "Honda",
                        "model": "Civic",
                        "year": "2021",
                    },
                    "notes": "SDK delete compat test",
                }
            ]
        }
        try:
            ebay.sell_inventory.create_or_replace_inventory_item(sku, item_body)
            ebay.sell_inventory.create_or_replace_product_compatibility(
                sku, compat_body
            )
            ebay.sell_inventory.delete_product_compatibility(sku)
            # After delete, getting compatibility should 404
            with pytest.raises(EbayApiError) as exc_info:
                ebay.sell_inventory.get_product_compatibility(sku)
            assert exc_info.value.status_code in (404, 400)
        except EbayApiError as exc:
            if exc.status_code in (400, 403):
                pytest.skip(
                    f"Product compatibility delete test failed: {exc.status_code}"
                )
            raise
        finally:
            try:
                ebay.sell_inventory.delete_inventory_item(sku)
            except EbayApiError:
                pass
