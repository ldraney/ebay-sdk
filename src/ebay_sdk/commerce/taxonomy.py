"""Commerce Taxonomy API — category trees, aspects, and compatibility.

Spec: https://developer.ebay.com/api-docs/master/commerce/taxonomy/openapi/3/commerce_taxonomy_v1_oas3.json
Version: v1.1.1
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ebay_sdk.client import EbayClient

_BASE = "/commerce/taxonomy/v1"


class CommerceTaxonomyApi:
    def __init__(self, client: EbayClient) -> None:
        self._c = client

    def get_default_category_tree_id(self, marketplace_id: str) -> Any:
        """Get the default category tree ID for a marketplace."""
        return self._c.get(
            f"{_BASE}/get_default_category_tree_id",
            params={"marketplace_id": marketplace_id},
        )

    def get_category_tree(self, category_tree_id: str) -> Any:
        """Get an entire category tree."""
        return self._c.get(f"{_BASE}/category_tree/{category_tree_id}")

    def get_category_subtree(
        self, category_tree_id: str, category_id: str
    ) -> Any:
        """Get a category subtree."""
        return self._c.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_category_subtree",
            params={"category_id": category_id},
        )

    def get_category_suggestions(
        self, category_tree_id: str, q: str
    ) -> Any:
        """Get suggested categories for a query."""
        return self._c.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_category_suggestions",
            params={"q": q},
        )

    def get_item_aspects_for_category(
        self, category_tree_id: str, category_id: str
    ) -> Any:
        """Get item aspects for a category."""
        return self._c.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_item_aspects_for_category",
            params={"category_id": category_id},
        )

    def get_compatibility_properties(
        self, category_tree_id: str, category_id: str
    ) -> Any:
        """Get compatibility properties for a category."""
        return self._c.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_compatibility_properties",
            params={"category_id": category_id},
        )

    def get_compatibility_property_values(
        self,
        category_tree_id: str,
        compatibility_property: str,
        category_id: str,
        *,
        filter: str | None = None,
    ) -> Any:
        """Get values for a compatibility property."""
        params: dict[str, Any] = {
            "compatibility_property": compatibility_property,
            "category_id": category_id,
        }
        if filter is not None:
            params["filter"] = filter
        return self._c.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_compatibility_property_values",
            params=params,
        )

    def get_expired_categories(self, category_tree_id: str) -> Any:
        """Get mappings of expired categories to active replacements."""
        return self._c.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_expired_categories"
        )

    def fetch_item_aspects(self, category_tree_id: str) -> Any:
        """Download a complete list of aspects for all leaf categories."""
        return self._c.get(
            f"{_BASE}/category_tree/{category_tree_id}/fetch_item_aspects"
        )
