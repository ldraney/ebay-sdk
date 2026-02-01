"""Buy Browse API — search and retrieve item details.

Spec: https://developer.ebay.com/api-docs/master/buy/browse/openapi/3/buy_browse_v1_oas3.json
Version: v1.20.4
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ebay_sdk.client import EbayClient

_BASE = "/buy/browse/v1"


class BuyBrowseApi:
    def __init__(self, client: EbayClient) -> None:
        self._c = client

    # -- Item Summary ----------------------------------------------------------

    def search(
        self,
        *,
        q: str | None = None,
        category_ids: str | None = None,
        epid: str | None = None,
        gtin: str | None = None,
        charity_ids: str | None = None,
        filter: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        aspect_filter: str | None = None,
        fieldgroups: str | None = None,
    ) -> Any:
        """Search for items by keyword, category, GTIN, ePID, etc."""
        params: dict[str, Any] = {}
        if q is not None:
            params["q"] = q
        if category_ids is not None:
            params["category_ids"] = category_ids
        if epid is not None:
            params["epid"] = epid
        if gtin is not None:
            params["gtin"] = gtin
        if charity_ids is not None:
            params["charity_ids"] = charity_ids
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if aspect_filter is not None:
            params["aspect_filter"] = aspect_filter
        if fieldgroups is not None:
            params["fieldgroups"] = fieldgroups
        return self._c.get(f"{_BASE}/item_summary/search", params=params)

    def search_by_image(
        self,
        image: dict[str, Any],
        *,
        filter: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        aspect_filter: str | None = None,
        category_ids: str | None = None,
    ) -> Any:
        """Search for items using an image."""
        params: dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if aspect_filter is not None:
            params["aspect_filter"] = aspect_filter
        if category_ids is not None:
            params["category_ids"] = category_ids
        return self._c.post(
            f"{_BASE}/item_summary/search_by_image",
            json=image,
            params=params,
        )

    # -- Item ------------------------------------------------------------------

    def get_item(self, item_id: str, *, fieldgroups: str | None = None) -> Any:
        """Retrieve details for a specific item."""
        params: dict[str, Any] = {}
        if fieldgroups is not None:
            params["fieldgroups"] = fieldgroups
        return self._c.get(f"{_BASE}/item/{item_id}", params=params)

    def get_item_by_legacy_id(
        self,
        legacy_item_id: str,
        *,
        legacy_variation_id: str | None = None,
        legacy_variation_sku: str | None = None,
        fieldgroups: str | None = None,
    ) -> Any:
        """Retrieve item details using a legacy item ID."""
        params: dict[str, Any] = {"legacy_item_id": legacy_item_id}
        if legacy_variation_id is not None:
            params["legacy_variation_id"] = legacy_variation_id
        if legacy_variation_sku is not None:
            params["legacy_variation_sku"] = legacy_variation_sku
        if fieldgroups is not None:
            params["fieldgroups"] = fieldgroups
        return self._c.get(f"{_BASE}/item/get_item_by_legacy_id", params=params)

    def get_items(self, item_ids: str, *, fieldgroups: str | None = None) -> Any:
        """Retrieve details for multiple items (pipe-separated IDs)."""
        params: dict[str, Any] = {"item_ids": item_ids}
        if fieldgroups is not None:
            params["fieldgroups"] = fieldgroups
        return self._c.get(f"{_BASE}/item/", params=params)

    def get_items_by_item_group(
        self, item_group_id: str, *, fieldgroups: str | None = None
    ) -> Any:
        """Retrieve items in a group (multi-variation listing)."""
        params: dict[str, Any] = {"item_group_id": item_group_id}
        if fieldgroups is not None:
            params["fieldgroups"] = fieldgroups
        return self._c.get(f"{_BASE}/item/get_items_by_item_group", params=params)

    def check_compatibility(
        self, item_id: str, compatibility_properties: list[dict[str, str]]
    ) -> Any:
        """Check item compatibility with a product."""
        return self._c.post(
            f"{_BASE}/item/{item_id}/check_compatibility",
            json={"compatibilityProperties": compatibility_properties},
        )
