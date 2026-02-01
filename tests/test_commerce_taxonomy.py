"""Integration tests for Commerce Taxonomy API.

Spec: https://developer.ebay.com/api-docs/master/commerce/taxonomy/openapi/3/commerce_taxonomy_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient


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

    def test_get_category_suggestions(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        result = ebay.commerce_taxonomy.get_category_suggestions(tree_id, "laptop")
        assert "categorySuggestions" in result


@pytest.mark.integration
class TestAspects:
    def test_get_item_aspects_for_category(self, ebay: EbayClient):
        tree_id_resp = ebay.commerce_taxonomy.get_default_category_tree_id("EBAY_US")
        tree_id = tree_id_resp["categoryTreeId"]
        # 177 = Cell Phones & Smartphones
        result = ebay.commerce_taxonomy.get_item_aspects_for_category(tree_id, "177")
        assert "aspects" in result
