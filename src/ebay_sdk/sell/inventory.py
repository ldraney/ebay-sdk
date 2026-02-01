"""Sell Inventory API — manage inventory items, offers, and locations.

Spec: https://developer.ebay.com/api-docs/master/sell/inventory/openapi/3/sell_inventory_v1_oas3.json
Version: v1.18.4
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ebay_sdk.client import EbayClient

_BASE = "/sell/inventory/v1"


class SellInventoryApi:
    def __init__(self, client: EbayClient) -> None:
        self._c = client

    # -- Inventory Item --------------------------------------------------------

    def get_inventory_item(self, sku: str) -> Any:
        """Retrieve a single inventory item by SKU."""
        return self._c.get(f"{_BASE}/inventory_item/{sku}")

    def create_or_replace_inventory_item(self, sku: str, body: dict[str, Any]) -> Any:
        """Create or replace a single inventory item."""
        return self._c.put(f"{_BASE}/inventory_item/{sku}", json=body)

    def delete_inventory_item(self, sku: str) -> Any:
        """Delete an inventory item by SKU."""
        return self._c.delete(f"{_BASE}/inventory_item/{sku}")

    def get_inventory_items(
        self, *, limit: int | None = None, offset: int | None = None
    ) -> Any:
        """List all inventory items with pagination."""
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/inventory_item", params=params)

    def bulk_create_or_replace_inventory_item(self, body: dict[str, Any]) -> Any:
        """Bulk create or replace up to 25 inventory items."""
        return self._c.post(f"{_BASE}/bulk_create_or_replace_inventory_item", json=body)

    def bulk_get_inventory_item(self, body: dict[str, Any]) -> Any:
        """Bulk retrieve up to 25 inventory items by SKU."""
        return self._c.post(f"{_BASE}/bulk_get_inventory_item", json=body)

    def bulk_update_price_quantity(self, body: dict[str, Any]) -> Any:
        """Bulk update price/quantity for inventory offers."""
        return self._c.post(f"{_BASE}/bulk_update_price_quantity", json=body)

    # -- Offer -----------------------------------------------------------------

    def get_offers(
        self,
        *,
        sku: str | None = None,
        marketplace_id: str | None = None,
        format: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """Get offers for inventory items."""
        params: dict[str, Any] = {}
        if sku is not None:
            params["sku"] = sku
        if marketplace_id is not None:
            params["marketplace_id"] = marketplace_id
        if format is not None:
            params["format"] = format
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/offer", params=params)

    def get_offer(self, offer_id: str) -> Any:
        """Get a specific offer."""
        return self._c.get(f"{_BASE}/offer/{offer_id}")

    def create_offer(self, body: dict[str, Any]) -> Any:
        """Create an offer for an inventory item."""
        return self._c.post(f"{_BASE}/offer", json=body)

    def update_offer(self, offer_id: str, body: dict[str, Any]) -> Any:
        """Update an existing offer."""
        return self._c.put(f"{_BASE}/offer/{offer_id}", json=body)

    def delete_offer(self, offer_id: str) -> Any:
        """Delete an offer."""
        return self._c.delete(f"{_BASE}/offer/{offer_id}")

    def publish_offer(self, offer_id: str) -> Any:
        """Publish an offer to create an eBay listing."""
        return self._c.post(f"{_BASE}/offer/{offer_id}/publish")

    def withdraw_offer(self, offer_id: str) -> Any:
        """Withdraw an offer (end the listing)."""
        return self._c.post(f"{_BASE}/offer/{offer_id}/withdraw")

    def publish_offer_by_inventory_item_group(self, body: dict[str, Any]) -> Any:
        """Publish offers for an inventory item group."""
        return self._c.post(f"{_BASE}/offer/publish_by_inventory_item_group", json=body)

    def withdraw_offer_by_inventory_item_group(self, body: dict[str, Any]) -> Any:
        """Withdraw offers for an inventory item group."""
        return self._c.post(f"{_BASE}/offer/withdraw_by_inventory_item_group", json=body)

    def get_listing_fees(self, body: dict[str, Any] | None = None) -> Any:
        """Retrieve estimated listing fees for offers."""
        return self._c.post(f"{_BASE}/offer/get_listing_fees", json=body)

    # -- Inventory Item Group --------------------------------------------------

    def get_inventory_item_group(self, inventory_item_group_key: str) -> Any:
        """Get an inventory item group."""
        return self._c.get(f"{_BASE}/inventory_item_group/{inventory_item_group_key}")

    def create_or_replace_inventory_item_group(
        self, inventory_item_group_key: str, body: dict[str, Any]
    ) -> Any:
        """Create or replace an inventory item group."""
        return self._c.put(
            f"{_BASE}/inventory_item_group/{inventory_item_group_key}", json=body
        )

    def delete_inventory_item_group(self, inventory_item_group_key: str) -> Any:
        """Delete an inventory item group."""
        return self._c.delete(
            f"{_BASE}/inventory_item_group/{inventory_item_group_key}"
        )

    # -- Inventory Location ----------------------------------------------------

    def get_inventory_location(self, merchant_location_key: str) -> Any:
        """Get an inventory location."""
        return self._c.get(f"{_BASE}/location/{merchant_location_key}")

    def create_inventory_location(
        self, merchant_location_key: str, body: dict[str, Any]
    ) -> Any:
        """Create an inventory location."""
        return self._c.post(f"{_BASE}/location/{merchant_location_key}", json=body)

    def update_inventory_location(
        self, merchant_location_key: str, body: dict[str, Any]
    ) -> Any:
        """Update an inventory location."""
        return self._c.post(
            f"{_BASE}/location/{merchant_location_key}/update_location_details",
            json=body,
        )

    def delete_inventory_location(self, merchant_location_key: str) -> Any:
        """Delete an inventory location."""
        return self._c.delete(f"{_BASE}/location/{merchant_location_key}")

    def get_inventory_locations(
        self, *, limit: int | None = None, offset: int | None = None
    ) -> Any:
        """List all inventory locations."""
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/location", params=params)

    def enable_inventory_location(self, merchant_location_key: str) -> Any:
        """Enable an inventory location."""
        return self._c.post(f"{_BASE}/location/{merchant_location_key}/enable")

    def disable_inventory_location(self, merchant_location_key: str) -> Any:
        """Disable an inventory location."""
        return self._c.post(f"{_BASE}/location/{merchant_location_key}/disable")

    # -- Product Compatibility -------------------------------------------------

    def get_product_compatibility(self, sku: str) -> Any:
        """Get product compatibility for an inventory item."""
        return self._c.get(f"{_BASE}/inventory_item/{sku}/product_compatibility")

    def create_or_replace_product_compatibility(
        self, sku: str, body: dict[str, Any]
    ) -> Any:
        """Create or replace product compatibility for an inventory item."""
        return self._c.put(
            f"{_BASE}/inventory_item/{sku}/product_compatibility", json=body
        )

    def delete_product_compatibility(self, sku: str) -> Any:
        """Delete product compatibility for an inventory item."""
        return self._c.delete(f"{_BASE}/inventory_item/{sku}/product_compatibility")
