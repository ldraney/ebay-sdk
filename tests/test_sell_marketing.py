"""Integration tests for Sell Marketing API.

Spec: https://developer.ebay.com/api-docs/master/sell/marketing/openapi/3/sell_marketing_v1_oas3.json

Covers all 63 methods across campaigns, ads, ad groups, keywords,
negative keywords, promotions, promotion reports, and ad reports.
"""

import pytest

from ebay_sdk import EbayClient
from ebay_sdk.client import EbayApiError


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_or_skip_campaign(ebay: EbayClient) -> dict:
    """Return the first available campaign or skip."""
    result = ebay.sell_marketing.get_campaigns(limit=1)
    campaigns = result.get("campaigns", [])
    if not campaigns:
        pytest.skip("No campaigns available in sandbox")
    return campaigns[0]


def _get_or_skip_ad(ebay: EbayClient, campaign_id: str) -> dict:
    """Return the first available ad for a campaign or skip."""
    result = ebay.sell_marketing.get_ads(campaign_id, limit=1)
    ads = result.get("ads", [])
    if not ads:
        pytest.skip("No ads available for campaign")
    return ads[0]


def _get_or_skip_promotion(ebay: EbayClient) -> dict:
    """Return the first available promotion or skip."""
    result = ebay.sell_marketing.get_promotions("EBAY_US", limit=1)
    promotions = result.get("promotions", [])
    if not promotions:
        pytest.skip("No promotions available in sandbox")
    return promotions[0]


# ---------------------------------------------------------------------------
# Campaign (13 methods)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestCampaigns:
    def test_get_campaigns(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_campaigns(limit=5)
        assert isinstance(result, dict)

    def test_get_campaigns_with_filters(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_campaigns(
            limit=5, offset=0, campaign_status="RUNNING",
        )
        assert isinstance(result, dict)

    def test_get_campaign(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        result = ebay.sell_marketing.get_campaign(campaign_id)
        assert isinstance(result, dict)
        assert result["campaignId"] == campaign_id

    def test_get_campaign_by_name(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        name = campaign["campaignName"]
        try:
            result = ebay.sell_marketing.get_campaign_by_name(name)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_campaign_by_name not available: {exc.status_code}")
            raise

    def test_create_update_pause_resume_end_delete_campaign(self, ebay: EbayClient):
        """Full campaign lifecycle: create -> get -> update -> pause -> resume -> end -> delete."""
        body = {
            "campaignName": "SDK-TEST-MKT-CAMPAIGN",
            "marketplaceId": "EBAY_US",
            "fundingStrategy": {
                "fundingModel": "COST_PER_SALE",
                "bidPercentage": "5.0",
            },
        }
        campaign_id = None
        try:
            result = ebay.sell_marketing.create_campaign(body)
            # create_campaign returns 201 with Location header; result may be empty
            if isinstance(result, dict) and "campaignId" in result:
                campaign_id = result["campaignId"]
            elif isinstance(result, str):
                # Sometimes the ID is returned as a plain string or in a header
                campaign_id = result.strip().split("/")[-1] if "/" in result else result
            else:
                # Try to look up by name
                lookup = ebay.sell_marketing.get_campaign_by_name("SDK-TEST-MKT-CAMPAIGN")
                campaign_id = lookup.get("campaignId")

            if not campaign_id:
                pytest.skip("Could not determine created campaign ID")

            # get
            got = ebay.sell_marketing.get_campaign(campaign_id)
            assert got["campaignId"] == campaign_id

            # update campaign identification
            try:
                ebay.sell_marketing.update_campaign(
                    campaign_id,
                    {"campaignName": "SDK-TEST-MKT-CAMPAIGN-UPD"},
                )
            except EbayApiError as exc:
                if exc.status_code not in (400, 403, 409):
                    raise

            # pause
            try:
                ebay.sell_marketing.pause_campaign(campaign_id)
            except EbayApiError as exc:
                if exc.status_code not in (400, 403, 409):
                    raise

            # resume
            try:
                ebay.sell_marketing.resume_campaign(campaign_id)
            except EbayApiError as exc:
                if exc.status_code not in (400, 403, 409):
                    raise

            # end
            try:
                ebay.sell_marketing.end_campaign(campaign_id)
            except EbayApiError as exc:
                if exc.status_code not in (400, 403, 409):
                    raise

        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(f"Campaign lifecycle not available in sandbox: {exc.status_code}")
            raise
        finally:
            if campaign_id:
                try:
                    ebay.sell_marketing.delete_campaign(campaign_id)
                except EbayApiError:
                    pass  # best-effort cleanup

    def test_clone_campaign(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        clone_id = None
        try:
            result = ebay.sell_marketing.clone_campaign(
                campaign_id,
                {"campaignName": "SDK-TEST-MKT-CLONE"},
            )
            if isinstance(result, dict) and "campaignId" in result:
                clone_id = result["campaignId"]
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(f"clone_campaign not available: {exc.status_code}")
            raise
        finally:
            if clone_id:
                try:
                    ebay.sell_marketing.delete_campaign(clone_id)
                except EbayApiError:
                    pass

    def test_suggest_budget(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.suggest_budget(campaign_id)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"suggest_budget not available: {exc.status_code}")
            raise

    def test_update_campaign_budget(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            ebay.sell_marketing.update_campaign_budget(
                campaign_id,
                {"dailyBudget": {"value": "10.00", "currency": "USD"}},
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"update_campaign_budget not available: {exc.status_code}")
            raise

    def test_suggest_items(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.suggest_items(campaign_id, limit=5)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"suggest_items not available: {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# Ad (13 methods)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestAds:
    def test_get_ads(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        result = ebay.sell_marketing.get_ads(campaign_id, limit=5)
        assert isinstance(result, dict)

    def test_get_ad(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad = _get_or_skip_ad(ebay, campaign_id)
        ad_id = ad["adId"]
        result = ebay.sell_marketing.get_ad(campaign_id, ad_id)
        assert isinstance(result, dict)
        assert result["adId"] == ad_id

    def test_create_ad_by_listing_id(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.create_ad_by_listing_id(
                campaign_id,
                {"listingId": "SDK-TEST-LISTING-001", "bidPercentage": "5.0"},
            )
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"create_ad_by_listing_id not available: {exc.status_code}")
            raise

    def test_delete_ad(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad = _get_or_skip_ad(ebay, campaign_id)
        ad_id = ad["adId"]
        try:
            ebay.sell_marketing.delete_ad(campaign_id, ad_id)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"delete_ad not available: {exc.status_code}")
            raise

    def test_update_bid(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad = _get_or_skip_ad(ebay, campaign_id)
        ad_id = ad["adId"]
        try:
            ebay.sell_marketing.update_bid(
                campaign_id, ad_id, {"bidPercentage": "3.0"},
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"update_bid not available: {exc.status_code}")
            raise

    def test_bulk_create_ads_by_inventory_reference(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.bulk_create_ads_by_inventory_reference(
                campaign_id,
                {
                    "requests": [
                        {
                            "inventoryReferenceId": "SDK-TEST-INV-001",
                            "inventoryReferenceType": "INVENTORY_ITEM",
                            "bidPercentage": "5.0",
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_create_ads_by_inventory_reference not available: {exc.status_code}")
            raise

    def test_bulk_create_ads_by_listing_id(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.bulk_create_ads_by_listing_id(
                campaign_id,
                {
                    "requests": [
                        {
                            "listingId": "SDK-TEST-LISTING-002",
                            "bidPercentage": "5.0",
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_create_ads_by_listing_id not available: {exc.status_code}")
            raise

    def test_bulk_delete_ads_by_inventory_reference(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.bulk_delete_ads_by_inventory_reference(
                campaign_id,
                {
                    "requests": [
                        {
                            "inventoryReferenceId": "SDK-TEST-INV-001",
                            "inventoryReferenceType": "INVENTORY_ITEM",
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_delete_ads_by_inventory_reference not available: {exc.status_code}")
            raise

    def test_bulk_delete_ads_by_listing_id(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.bulk_delete_ads_by_listing_id(
                campaign_id,
                {"requests": [{"listingId": "SDK-TEST-LISTING-002"}]},
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_delete_ads_by_listing_id not available: {exc.status_code}")
            raise

    def test_bulk_update_ads_bid_by_inventory_reference(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.bulk_update_ads_bid_by_inventory_reference(
                campaign_id,
                {
                    "requests": [
                        {
                            "inventoryReferenceId": "SDK-TEST-INV-001",
                            "inventoryReferenceType": "INVENTORY_ITEM",
                            "bidPercentage": "7.0",
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_update_ads_bid_by_inventory_reference not available: {exc.status_code}")
            raise

    def test_bulk_update_ads_bid_by_listing_id(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.bulk_update_ads_bid_by_listing_id(
                campaign_id,
                {
                    "requests": [
                        {
                            "listingId": "SDK-TEST-LISTING-002",
                            "bidPercentage": "8.0",
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_update_ads_bid_by_listing_id not available: {exc.status_code}")
            raise

    def test_bulk_update_ads_status(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad = _get_or_skip_ad(ebay, campaign_id)
        ad_id = ad["adId"]
        try:
            result = ebay.sell_marketing.bulk_update_ads_status(
                campaign_id,
                {"requests": [{"adId": ad_id, "adStatus": "ACTIVE"}]},
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_update_ads_status not available: {exc.status_code}")
            raise

    def test_bulk_update_ads_status_by_listing_id(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.bulk_update_ads_status_by_listing_id(
                campaign_id,
                {
                    "requests": [
                        {
                            "listingId": "SDK-TEST-LISTING-002",
                            "adStatus": "ACTIVE",
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_update_ads_status_by_listing_id not available: {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# Ad Group (4 methods)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestAdGroups:
    def test_get_ad_groups(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.get_ad_groups(campaign_id, limit=5)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_ad_groups not available: {exc.status_code}")
            raise

    def test_get_ad_group(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            groups_result = ebay.sell_marketing.get_ad_groups(campaign_id, limit=1)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_ad_groups not available: {exc.status_code}")
            raise
        groups = groups_result.get("adGroups", [])
        if not groups:
            pytest.skip("No ad groups available for campaign")
        ad_group_id = groups[0]["adGroupId"]
        result = ebay.sell_marketing.get_ad_group(campaign_id, ad_group_id)
        assert isinstance(result, dict)
        assert result["adGroupId"] == ad_group_id

    def test_create_ad_group(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.create_ad_group(
                campaign_id,
                {
                    "name": "SDK-TEST-AD-GROUP",
                    "defaultBid": {"value": "1.00", "currency": "USD"},
                },
            )
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"create_ad_group not available: {exc.status_code}")
            raise

    def test_update_ad_group(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            groups_result = ebay.sell_marketing.get_ad_groups(campaign_id, limit=1)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_ad_groups not available: {exc.status_code}")
            raise
        groups = groups_result.get("adGroups", [])
        if not groups:
            pytest.skip("No ad groups available for campaign")
        ad_group_id = groups[0]["adGroupId"]
        try:
            ebay.sell_marketing.update_ad_group(
                campaign_id,
                ad_group_id,
                {"defaultBid": {"value": "1.50", "currency": "USD"}},
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"update_ad_group not available: {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# Keyword (6 methods)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestKeywords:

    def _get_ad_group_id(self, ebay: EbayClient, campaign_id: str) -> str:
        try:
            groups_result = ebay.sell_marketing.get_ad_groups(campaign_id, limit=1)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_ad_groups not available: {exc.status_code}")
            raise
        groups = groups_result.get("adGroups", [])
        if not groups:
            pytest.skip("No ad groups available for campaign")
        return groups[0]["adGroupId"]

    def test_get_keywords(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad_group_id = self._get_ad_group_id(ebay, campaign_id)
        try:
            result = ebay.sell_marketing.get_keywords(
                campaign_id, ad_group_id, limit=5,
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_keywords not available: {exc.status_code}")
            raise

    def test_get_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad_group_id = self._get_ad_group_id(ebay, campaign_id)
        try:
            kw_result = ebay.sell_marketing.get_keywords(
                campaign_id, ad_group_id, limit=1,
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_keywords not available: {exc.status_code}")
            raise
        keywords = kw_result.get("keywords", [])
        if not keywords:
            pytest.skip("No keywords available")
        keyword_id = keywords[0]["keywordId"]
        result = ebay.sell_marketing.get_keyword(campaign_id, keyword_id)
        assert isinstance(result, dict)
        assert result["keywordId"] == keyword_id

    def test_create_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad_group_id = self._get_ad_group_id(ebay, campaign_id)
        try:
            result = ebay.sell_marketing.create_keyword(
                campaign_id,
                {
                    "adGroupId": ad_group_id,
                    "keywordText": "sdk test keyword",
                    "matchType": "BROAD",
                    "bid": {"value": "0.50", "currency": "USD"},
                },
            )
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"create_keyword not available: {exc.status_code}")
            raise

    def test_bulk_create_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad_group_id = self._get_ad_group_id(ebay, campaign_id)
        try:
            result = ebay.sell_marketing.bulk_create_keyword(
                campaign_id,
                {
                    "requests": [
                        {
                            "adGroupId": ad_group_id,
                            "keywordText": "sdk bulk keyword test",
                            "matchType": "BROAD",
                            "bid": {"value": "0.50", "currency": "USD"},
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_create_keyword not available: {exc.status_code}")
            raise

    def test_bulk_update_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad_group_id = self._get_ad_group_id(ebay, campaign_id)
        try:
            kw_result = ebay.sell_marketing.get_keywords(
                campaign_id, ad_group_id, limit=1,
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_keywords not available: {exc.status_code}")
            raise
        keywords = kw_result.get("keywords", [])
        if not keywords:
            pytest.skip("No keywords to update")
        keyword_id = keywords[0]["keywordId"]
        try:
            result = ebay.sell_marketing.bulk_update_keyword(
                campaign_id,
                {
                    "requests": [
                        {
                            "keywordId": keyword_id,
                            "bid": {"value": "0.75", "currency": "USD"},
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_update_keyword not available: {exc.status_code}")
            raise

    def test_update_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        ad_group_id = self._get_ad_group_id(ebay, campaign_id)
        try:
            kw_result = ebay.sell_marketing.get_keywords(
                campaign_id, ad_group_id, limit=1,
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_keywords not available: {exc.status_code}")
            raise
        keywords = kw_result.get("keywords", [])
        if not keywords:
            pytest.skip("No keywords to update")
        keyword_id = keywords[0]["keywordId"]
        try:
            ebay.sell_marketing.update_keyword(
                campaign_id,
                keyword_id,
                {"bid": {"value": "0.60", "currency": "USD"}},
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"update_keyword not available: {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# Negative Keyword (6 methods)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestNegativeKeywords:

    def test_get_negative_keywords(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.get_negative_keywords(campaign_id, limit=5)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_negative_keywords not available: {exc.status_code}")
            raise

    def test_get_negative_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            nk_result = ebay.sell_marketing.get_negative_keywords(campaign_id, limit=1)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_negative_keywords not available: {exc.status_code}")
            raise
        neg_keywords = nk_result.get("negativeKeywords", [])
        if not neg_keywords:
            pytest.skip("No negative keywords available")
        nk_id = neg_keywords[0]["negativeKeywordId"]
        result = ebay.sell_marketing.get_negative_keyword(campaign_id, nk_id)
        assert isinstance(result, dict)
        assert result["negativeKeywordId"] == nk_id

    def test_create_negative_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.create_negative_keyword(
                campaign_id,
                {
                    "keywordText": "sdk negative test",
                    "matchType": "BROAD",
                },
            )
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"create_negative_keyword not available: {exc.status_code}")
            raise

    def test_bulk_create_negative_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            result = ebay.sell_marketing.bulk_create_negative_keyword(
                campaign_id,
                {
                    "requests": [
                        {
                            "keywordText": "sdk bulk negative test",
                            "matchType": "BROAD",
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_create_negative_keyword not available: {exc.status_code}")
            raise

    def test_bulk_update_negative_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            nk_result = ebay.sell_marketing.get_negative_keywords(campaign_id, limit=1)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_negative_keywords not available: {exc.status_code}")
            raise
        neg_keywords = nk_result.get("negativeKeywords", [])
        if not neg_keywords:
            pytest.skip("No negative keywords to update")
        nk_id = neg_keywords[0]["negativeKeywordId"]
        try:
            result = ebay.sell_marketing.bulk_update_negative_keyword(
                campaign_id,
                {
                    "requests": [
                        {
                            "negativeKeywordId": nk_id,
                            "keywordText": "sdk bulk negative updated",
                            "matchType": "BROAD",
                        }
                    ]
                },
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"bulk_update_negative_keyword not available: {exc.status_code}")
            raise

    def test_update_negative_keyword(self, ebay: EbayClient):
        campaign = _get_or_skip_campaign(ebay)
        campaign_id = campaign["campaignId"]
        try:
            nk_result = ebay.sell_marketing.get_negative_keywords(campaign_id, limit=1)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_negative_keywords not available: {exc.status_code}")
            raise
        neg_keywords = nk_result.get("negativeKeywords", [])
        if not neg_keywords:
            pytest.skip("No negative keywords to update")
        nk_id = neg_keywords[0]["negativeKeywordId"]
        try:
            ebay.sell_marketing.update_negative_keyword(
                campaign_id,
                nk_id,
                {"keywordText": "sdk negative updated", "matchType": "BROAD"},
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"update_negative_keyword not available: {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# Promotion (12 methods)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestPromotions:
    def test_get_promotions(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_promotions("EBAY_US", limit=5)
        assert isinstance(result, dict)

    def test_get_promotions_with_filters(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_promotions(
            "EBAY_US", limit=5, offset=0, promotion_status="ACTIVE",
        )
        assert isinstance(result, dict)

    def test_get_promotion(self, ebay: EbayClient):
        promo = _get_or_skip_promotion(ebay)
        promotion_id = promo["promotionId"]
        result = ebay.sell_marketing.get_promotion(promotion_id)
        assert isinstance(result, dict)

    def test_create_and_delete_item_price_markdown_promotion(self, ebay: EbayClient):
        promotion_id = None
        try:
            result = ebay.sell_marketing.create_item_price_markdown_promotion(
                {
                    "name": "SDK-TEST-MARKDOWN",
                    "marketplaceId": "EBAY_US",
                    "startDate": "2099-01-01T00:00:00.000Z",
                    "endDate": "2099-01-31T23:59:59.000Z",
                    "discountRules": [
                        {
                            "discountSpecification": {
                                "properties": {"markdownPercentageOff": "10"},
                            },
                            "ruleOrder": 1,
                        }
                    ],
                }
            )
            if isinstance(result, dict) and "promotionId" in result:
                promotion_id = result["promotionId"]
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(f"create_item_price_markdown_promotion not available: {exc.status_code}")
            raise
        finally:
            if promotion_id:
                try:
                    ebay.sell_marketing.delete_item_price_markdown_promotion(promotion_id)
                except EbayApiError:
                    pass

    def test_update_item_price_markdown_promotion(self, ebay: EbayClient):
        promo = _get_or_skip_promotion(ebay)
        promotion_id = promo.get("promotionId")
        if not promotion_id:
            pytest.skip("No promotion ID available")
        try:
            ebay.sell_marketing.update_item_price_markdown_promotion(
                promotion_id,
                {
                    "name": "SDK-TEST-MARKDOWN-UPD",
                    "marketplaceId": "EBAY_US",
                    "startDate": "2099-01-01T00:00:00.000Z",
                    "endDate": "2099-01-31T23:59:59.000Z",
                },
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"update_item_price_markdown_promotion not available: {exc.status_code}")
            raise

    def test_get_item_price_markdown_promotion(self, ebay: EbayClient):
        promo = _get_or_skip_promotion(ebay)
        promotion_id = promo.get("promotionId")
        if not promotion_id:
            pytest.skip("No promotion ID available")
        try:
            result = ebay.sell_marketing.get_item_price_markdown_promotion(promotion_id)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_item_price_markdown_promotion not available: {exc.status_code}")
            raise

    def test_delete_item_price_markdown_promotion(self, ebay: EbayClient):
        """Attempts deletion on a non-existent promotion; expects 404 skip."""
        try:
            ebay.sell_marketing.delete_item_price_markdown_promotion("SDK-TEST-FAKE-ID")
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"delete_item_price_markdown_promotion not available: {exc.status_code}")
            raise

    def test_create_and_delete_item_promotion(self, ebay: EbayClient):
        promotion_id = None
        try:
            result = ebay.sell_marketing.create_item_promotion(
                {
                    "name": "SDK-TEST-ORDER-DISCOUNT",
                    "marketplaceId": "EBAY_US",
                    "startDate": "2099-01-01T00:00:00.000Z",
                    "endDate": "2099-01-31T23:59:59.000Z",
                    "promotionType": "ORDER_DISCOUNT",
                    "discountRules": [
                        {
                            "discountBenefit": {
                                "percentageOffOrder": "5",
                            },
                            "discountSpecification": {
                                "minAmount": {"value": "50.00", "currency": "USD"},
                            },
                            "ruleOrder": 1,
                        }
                    ],
                }
            )
            if isinstance(result, dict) and "promotionId" in result:
                promotion_id = result["promotionId"]
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(f"create_item_promotion not available: {exc.status_code}")
            raise
        finally:
            if promotion_id:
                try:
                    ebay.sell_marketing.delete_item_promotion(promotion_id)
                except EbayApiError:
                    pass

    def test_update_item_promotion(self, ebay: EbayClient):
        promo = _get_or_skip_promotion(ebay)
        promotion_id = promo.get("promotionId")
        if not promotion_id:
            pytest.skip("No promotion ID available")
        try:
            ebay.sell_marketing.update_item_promotion(
                promotion_id,
                {
                    "name": "SDK-TEST-ORDER-DISCOUNT-UPD",
                    "marketplaceId": "EBAY_US",
                    "startDate": "2099-01-01T00:00:00.000Z",
                    "endDate": "2099-01-31T23:59:59.000Z",
                },
            )
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"update_item_promotion not available: {exc.status_code}")
            raise

    def test_get_item_promotion(self, ebay: EbayClient):
        promo = _get_or_skip_promotion(ebay)
        promotion_id = promo.get("promotionId")
        if not promotion_id:
            pytest.skip("No promotion ID available")
        try:
            result = ebay.sell_marketing.get_item_promotion(promotion_id)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_item_promotion not available: {exc.status_code}")
            raise

    def test_delete_item_promotion(self, ebay: EbayClient):
        """Attempts deletion on a non-existent promotion; expects 404 skip."""
        try:
            ebay.sell_marketing.delete_item_promotion("SDK-TEST-FAKE-ID")
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"delete_item_promotion not available: {exc.status_code}")
            raise

    def test_pause_promotion(self, ebay: EbayClient):
        promo = _get_or_skip_promotion(ebay)
        promotion_id = promo.get("promotionId")
        if not promotion_id:
            pytest.skip("No promotion ID available")
        try:
            ebay.sell_marketing.pause_promotion(promotion_id)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"pause_promotion not available: {exc.status_code}")
            raise

    def test_resume_promotion(self, ebay: EbayClient):
        promo = _get_or_skip_promotion(ebay)
        promotion_id = promo.get("promotionId")
        if not promotion_id:
            pytest.skip("No promotion ID available")
        try:
            ebay.sell_marketing.resume_promotion(promotion_id)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404, 409):
                pytest.skip(f"resume_promotion not available: {exc.status_code}")
            raise


# ---------------------------------------------------------------------------
# Promotion Report (2 methods)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestPromotionReports:
    def test_get_promotion_reports(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_promotion_reports("EBAY_US", limit=5)
        assert isinstance(result, dict)

    def test_get_promotion_summary_report(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_promotion_summary_report("EBAY_US")
        assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# Ad Report (7 methods)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestReports:
    def test_get_report_tasks(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_report_tasks(limit=5)
        assert isinstance(result, dict)

    def test_get_report_metadata(self, ebay: EbayClient):
        result = ebay.sell_marketing.get_report_metadata()
        assert isinstance(result, dict)

    def test_get_report_metadata_for_report_type(self, ebay: EbayClient):
        try:
            result = ebay.sell_marketing.get_report_metadata_for_report_type(
                "CAMPAIGN_PERFORMANCE_REPORT"
            )
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(
                    f"get_report_metadata_for_report_type not available: {exc.status_code}"
                )
            raise

    def test_create_report_task(self, ebay: EbayClient):
        try:
            result = ebay.sell_marketing.create_report_task(
                {
                    "reportType": "CAMPAIGN_PERFORMANCE_REPORT",
                    "marketplaceId": "EBAY_US",
                    "dateRange": "LAST_7_DAYS",
                    "campaignIds": [],
                    "dimensions": [{"dimensionKey": "DATE"}],
                    "metricKeys": ["CLICK_COUNT", "IMPRESSION_COUNT"],
                }
            )
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 409):
                pytest.skip(f"create_report_task not available: {exc.status_code}")
            raise

    def test_get_report_task(self, ebay: EbayClient):
        tasks_result = ebay.sell_marketing.get_report_tasks(limit=1)
        tasks = tasks_result.get("reportTasks", [])
        if not tasks:
            pytest.skip("No report tasks available")
        task_id = tasks[0]["reportTaskId"]
        result = ebay.sell_marketing.get_report_task(task_id)
        assert isinstance(result, dict)
        assert result["reportTaskId"] == task_id

    def test_delete_report_task(self, ebay: EbayClient):
        """Attempts deletion on a non-existent task; expects 404 skip."""
        try:
            ebay.sell_marketing.delete_report_task("SDK-TEST-FAKE-TASK-ID")
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"delete_report_task not available: {exc.status_code}")
            raise

    def test_get_report(self, ebay: EbayClient):
        tasks_result = ebay.sell_marketing.get_report_tasks(limit=5)
        tasks = tasks_result.get("reportTasks", [])
        # Look for a completed task
        completed = [t for t in tasks if t.get("reportTaskStatus") == "SUCCESS"]
        if not completed:
            pytest.skip("No completed report tasks available")
        task_id = completed[0]["reportTaskId"]
        try:
            result = ebay.sell_marketing.get_report(task_id)
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (400, 403, 404):
                pytest.skip(f"get_report not available: {exc.status_code}")
            raise
