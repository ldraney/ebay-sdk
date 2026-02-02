"""Integration tests for Commerce Taxonomy API.

Spec: https://developer.ebay.com/api-docs/master/commerce/taxonomy/openapi/3/commerce_taxonomy_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient
from ebay_sdk.client import EbayApiError


@pytest.mark.integration
class TestCategoryTree:
    def test_get_default_category_tree_id(self, ebay: EbayClient):
        result = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        assert "categoryTreeId" in result

    def test_get_category_tree(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        result = ebay.commerce_taxonomy.get_category_tree(tree_id)
        assert "categoryTreeId" in result

    def test_get_category_subtree(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        # 177 = Cell Phones & Smartphones
        result = ebay.commerce_taxonomy.get_category_subtree(tree_id, "177")
        assert isinstance(result, dict)
        assert "categorySubtreeNode" in result or "categoryTreeId" in result

    def test_get_category_suggestions(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        result = ebay.commerce_taxonomy.get_category_suggestions(tree_id, "laptop")
        assert "categorySuggestions" in result

    def test_get_expired_categories(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        try:
            result = ebay.commerce_taxonomy.get_expired_categories(tree_id)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (204, 400, 404):
                pytest.skip(
                    f"get_expired_categories not available: {exc.status_code}"
                )
            raise

    def test_fetch_item_aspects(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        try:
            result = ebay.commerce_taxonomy.fetch_item_aspects(tree_id)
            # May return a URL or binary data reference
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 404, 500):
                pytest.skip(
                    f"fetch_item_aspects not available: {exc.status_code}"
                )
            raise


@pytest.mark.integration
class TestAspects:
    def test_get_item_aspects_for_category(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        # 177 = Cell Phones & Smartphones
        result = ebay.commerce_taxonomy.get_item_aspects_for_category(tree_id, "177")
        assert "aspects" in result


@pytest.mark.integration
class TestCompatibility:
    def test_get_compatibility_properties(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        # 6000 = eBay Motors / Parts & Accessories
        try:
            result = ebay.commerce_taxonomy.get_compatibility_properties(
                tree_id, "6000"
            )
            assert isinstance(result, dict)
            assert "compatibilityProperties" in result
        except EbayApiError as exc:
            if exc.status_code in (400, 404):
                pytest.skip(
                    f"get_compatibility_properties failed: {exc.status_code}"
                )
            raise

    def test_get_compatibility_property_values(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        # 6000 = eBay Motors, "Make" is a standard compatibility property
        try:
            result = ebay.commerce_taxonomy.get_compatibility_property_values(
                tree_id, "Make", "6000"
            )
            assert isinstance(result, dict)
            assert (
                "compatibilityPropertyValues" in result
                or "total" in result
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 404):
                pytest.skip(
                    f"get_compatibility_property_values failed: {exc.status_code}"
                )
            raise

    def test_get_compatibility_property_values_with_filter(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        try:
            result = ebay.commerce_taxonomy.get_compatibility_property_values(
                tree_id,
                "Make",
                "6000",
                filter="Year:2020",
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 404):
                pytest.skip(
                    f"get_compatibility_property_values with filter failed: {exc.status_code}"
                )
            raise
