"""Sell Marketing API — campaigns, ads, promotions, keywords, and reports.

Spec: https://developer.ebay.com/api-docs/master/sell/marketing/openapi/3/sell_marketing_v1_oas3.json
Version: v1.22.2
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ebay_sdk.client import EbayClient

_BASE = "/sell/marketing/v1"


class SellMarketingApi:
    def __init__(self, client: EbayClient) -> None:
        self._c = client

    # -- Campaign --------------------------------------------------------------

    def get_campaigns(
        self,
        *,
        campaign_name: str | None = None,
        campaign_status: str | None = None,
        funding_strategy: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List campaigns."""
        params: dict[str, Any] = {}
        if campaign_name is not None:
            params["campaign_name"] = campaign_name
        if campaign_status is not None:
            params["campaign_status"] = campaign_status
        if funding_strategy is not None:
            params["funding_strategy"] = funding_strategy
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/ad_campaign", params=params)

    def get_campaign(self, campaign_id: str) -> Any:
        """Get a specific campaign."""
        return self._c.get(f"{_BASE}/ad_campaign/{campaign_id}")

    def create_campaign(self, body: dict[str, Any]) -> Any:
        """Create a campaign."""
        return self._c.post(f"{_BASE}/ad_campaign", json=body)

    def update_campaign(self, campaign_id: str, body: dict[str, Any]) -> Any:
        """Update campaign identification (name, start/end date)."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/update_campaign_identification",
            json=body,
        )

    def delete_campaign(self, campaign_id: str) -> Any:
        """Delete a campaign."""
        return self._c.delete(f"{_BASE}/ad_campaign/{campaign_id}")

    def pause_campaign(self, campaign_id: str) -> Any:
        """Pause a campaign."""
        return self._c.post(f"{_BASE}/ad_campaign/{campaign_id}/pause")

    def resume_campaign(self, campaign_id: str) -> Any:
        """Resume a paused campaign."""
        return self._c.post(f"{_BASE}/ad_campaign/{campaign_id}/resume")

    def end_campaign(self, campaign_id: str) -> Any:
        """End a campaign."""
        return self._c.post(f"{_BASE}/ad_campaign/{campaign_id}/end")

    def clone_campaign(self, campaign_id: str, body: dict[str, Any]) -> Any:
        """Clone a campaign."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/clone", json=body
        )

    def get_campaign_by_name(
        self, campaign_name: str, *, marketplace_id: str | None = None
    ) -> Any:
        """Find campaign by name."""
        params: dict[str, Any] = {"campaign_name": campaign_name}
        if marketplace_id is not None:
            params["marketplace_id"] = marketplace_id
        return self._c.get(
            f"{_BASE}/ad_campaign/get_campaign_by_name", params=params
        )

    def suggest_budget(self, campaign_id: str) -> Any:
        """Get suggested budget for a campaign."""
        return self._c.get(f"{_BASE}/ad_campaign/{campaign_id}/suggest_budget")

    def update_campaign_budget(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Update campaign budget."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/update_campaign_budget",
            json=body,
        )

    def suggest_items(self, campaign_id: str, **kwargs: Any) -> Any:
        """Get suggested items for a campaign."""
        return self._c.get(
            f"{_BASE}/ad_campaign/{campaign_id}/suggest_items", params=kwargs
        )

    # -- Ad (by inventory reference) -------------------------------------------

    def bulk_create_ads_by_inventory_reference(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk create ads by inventory reference."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference",
            json=body,
        )

    def bulk_create_ads_by_listing_id(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk create ads by listing ID."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id",
            json=body,
        )

    def bulk_delete_ads_by_inventory_reference(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk delete ads by inventory reference."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference",
            json=body,
        )

    def bulk_delete_ads_by_listing_id(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk delete ads by listing ID."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id",
            json=body,
        )

    def bulk_update_ads_bid_by_inventory_reference(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk update ad bids by inventory reference."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference",
            json=body,
        )

    def bulk_update_ads_bid_by_listing_id(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk update ad bids by listing ID."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id",
            json=body,
        )

    def bulk_update_ads_status(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk update ad status."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_update_ads_status",
            json=body,
        )

    def bulk_update_ads_status_by_listing_id(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk update ad status by listing ID."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id",
            json=body,
        )

    def get_ads(
        self,
        campaign_id: str,
        *,
        ad_group_ids: str | None = None,
        ad_status: str | None = None,
        limit: int | None = None,
        listing_ids: str | None = None,
        offset: int | None = None,
    ) -> Any:
        """List ads for a campaign."""
        params: dict[str, Any] = {}
        if ad_group_ids is not None:
            params["ad_group_ids"] = ad_group_ids
        if ad_status is not None:
            params["ad_status"] = ad_status
        if limit is not None:
            params["limit"] = limit
        if listing_ids is not None:
            params["listing_ids"] = listing_ids
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/ad_campaign/{campaign_id}/ad", params=params)

    def get_ad(self, campaign_id: str, ad_id: str) -> Any:
        """Get a specific ad."""
        return self._c.get(f"{_BASE}/ad_campaign/{campaign_id}/ad/{ad_id}")

    def create_ad_by_listing_id(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Create an ad from a listing ID."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/ad", json=body
        )

    def delete_ad(self, campaign_id: str, ad_id: str) -> Any:
        """Delete an ad."""
        return self._c.delete(
            f"{_BASE}/ad_campaign/{campaign_id}/ad/{ad_id}"
        )

    def update_bid(
        self, campaign_id: str, ad_id: str, body: dict[str, Any]
    ) -> Any:
        """Update an ad's bid."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid",
            json=body,
        )

    # -- Ad Group --------------------------------------------------------------

    def get_ad_groups(
        self,
        campaign_id: str,
        *,
        ad_group_status: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List ad groups for a campaign."""
        params: dict[str, Any] = {}
        if ad_group_status is not None:
            params["ad_group_status"] = ad_group_status
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(
            f"{_BASE}/ad_campaign/{campaign_id}/ad_group", params=params
        )

    def get_ad_group(self, campaign_id: str, ad_group_id: str) -> Any:
        """Get a specific ad group."""
        return self._c.get(
            f"{_BASE}/ad_campaign/{campaign_id}/ad_group/{ad_group_id}"
        )

    def create_ad_group(self, campaign_id: str, body: dict[str, Any]) -> Any:
        """Create an ad group."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/ad_group", json=body
        )

    def update_ad_group(
        self, campaign_id: str, ad_group_id: str, body: dict[str, Any]
    ) -> Any:
        """Update an ad group."""
        return self._c.put(
            f"{_BASE}/ad_campaign/{campaign_id}/ad_group/{ad_group_id}",
            json=body,
        )

    # -- Keyword ---------------------------------------------------------------

    def get_keywords(
        self,
        campaign_id: str,
        ad_group_id: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List keywords for an ad group."""
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(
            f"{_BASE}/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/keyword",
            params=params,
        )

    def get_keyword(
        self, campaign_id: str, keyword_id: str
    ) -> Any:
        """Get a specific keyword."""
        return self._c.get(
            f"{_BASE}/ad_campaign/{campaign_id}/keyword/{keyword_id}"
        )

    def create_keyword(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Create a keyword."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/keyword", json=body
        )

    def bulk_create_keyword(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk create keywords."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_create_keyword", json=body
        )

    def bulk_update_keyword(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk update keywords."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_update_keyword", json=body
        )

    def update_keyword(
        self, campaign_id: str, keyword_id: str, body: dict[str, Any]
    ) -> Any:
        """Update a keyword."""
        return self._c.put(
            f"{_BASE}/ad_campaign/{campaign_id}/keyword/{keyword_id}",
            json=body,
        )

    # -- Negative Keyword ------------------------------------------------------

    def get_negative_keywords(
        self,
        campaign_id: str,
        *,
        ad_group_ids: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List negative keywords."""
        params: dict[str, Any] = {}
        if ad_group_ids is not None:
            params["ad_group_ids"] = ad_group_ids
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(
            f"{_BASE}/ad_campaign/{campaign_id}/negative_keyword", params=params
        )

    def get_negative_keyword(
        self, campaign_id: str, negative_keyword_id: str
    ) -> Any:
        """Get a specific negative keyword."""
        return self._c.get(
            f"{_BASE}/ad_campaign/{campaign_id}/negative_keyword/{negative_keyword_id}"
        )

    def create_negative_keyword(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Create a negative keyword."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/negative_keyword", json=body
        )

    def bulk_create_negative_keyword(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk create negative keywords."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_create_negative_keyword",
            json=body,
        )

    def bulk_update_negative_keyword(
        self, campaign_id: str, body: dict[str, Any]
    ) -> Any:
        """Bulk update negative keywords."""
        return self._c.post(
            f"{_BASE}/ad_campaign/{campaign_id}/bulk_update_negative_keyword",
            json=body,
        )

    def update_negative_keyword(
        self, campaign_id: str, negative_keyword_id: str, body: dict[str, Any]
    ) -> Any:
        """Update a negative keyword."""
        return self._c.put(
            f"{_BASE}/ad_campaign/{campaign_id}/negative_keyword/{negative_keyword_id}",
            json=body,
        )

    # -- Promotion (Item) ------------------------------------------------------

    def get_promotions(
        self,
        marketplace_id: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
        promotion_status: str | None = None,
        promotion_type: str | None = None,
        q: str | None = None,
        sort: str | None = None,
    ) -> Any:
        """List item promotions."""
        params: dict[str, Any] = {"marketplace_id": marketplace_id}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if promotion_status is not None:
            params["promotion_status"] = promotion_status
        if promotion_type is not None:
            params["promotion_type"] = promotion_type
        if q is not None:
            params["q"] = q
        if sort is not None:
            params["sort"] = sort
        return self._c.get(f"{_BASE}/promotion", params=params)

    def get_promotion(self, promotion_id: str) -> Any:
        """Get a specific promotion."""
        return self._c.get(f"{_BASE}/promotion/{promotion_id}")

    def create_item_price_markdown_promotion(
        self, body: dict[str, Any]
    ) -> Any:
        """Create an item price markdown promotion."""
        return self._c.post(f"{_BASE}/item_price_markdown", json=body)

    def update_item_price_markdown_promotion(
        self, promotion_id: str, body: dict[str, Any]
    ) -> Any:
        """Update an item price markdown promotion."""
        return self._c.put(
            f"{_BASE}/item_price_markdown/{promotion_id}", json=body
        )

    def get_item_price_markdown_promotion(self, promotion_id: str) -> Any:
        """Get an item price markdown promotion."""
        return self._c.get(f"{_BASE}/item_price_markdown/{promotion_id}")

    def delete_item_price_markdown_promotion(self, promotion_id: str) -> Any:
        """Delete an item price markdown promotion."""
        return self._c.delete(f"{_BASE}/item_price_markdown/{promotion_id}")

    def create_item_promotion(self, body: dict[str, Any]) -> Any:
        """Create an item promotion (order discount)."""
        return self._c.post(f"{_BASE}/item_promotion", json=body)

    def update_item_promotion(
        self, promotion_id: str, body: dict[str, Any]
    ) -> Any:
        """Update an item promotion."""
        return self._c.put(f"{_BASE}/item_promotion/{promotion_id}", json=body)

    def get_item_promotion(self, promotion_id: str) -> Any:
        """Get an item promotion."""
        return self._c.get(f"{_BASE}/item_promotion/{promotion_id}")

    def delete_item_promotion(self, promotion_id: str) -> Any:
        """Delete an item promotion."""
        return self._c.delete(f"{_BASE}/item_promotion/{promotion_id}")

    def pause_promotion(self, promotion_id: str) -> Any:
        """Pause a promotion."""
        return self._c.post(f"{_BASE}/promotion/{promotion_id}/pause")

    def resume_promotion(self, promotion_id: str) -> Any:
        """Resume a paused promotion."""
        return self._c.post(f"{_BASE}/promotion/{promotion_id}/resume")

    # -- Promotion Report ------------------------------------------------------

    def get_promotion_reports(
        self,
        marketplace_id: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
        promotion_status: str | None = None,
        q: str | None = None,
    ) -> Any:
        """Get promotion performance reports."""
        params: dict[str, Any] = {"marketplace_id": marketplace_id}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if promotion_status is not None:
            params["promotion_status"] = promotion_status
        if q is not None:
            params["q"] = q
        return self._c.get(f"{_BASE}/promotion_report", params=params)

    def get_promotion_summary_report(self, marketplace_id: str) -> Any:
        """Get promotion summary report."""
        return self._c.get(
            f"{_BASE}/promotion_summary_report",
            params={"marketplace_id": marketplace_id},
        )

    # -- Ad Report -------------------------------------------------------------

    def create_report_task(self, body: dict[str, Any]) -> Any:
        """Create an ad report task."""
        return self._c.post(f"{_BASE}/ad_report_task", json=body)

    def get_report_tasks(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        report_task_statuses: str | None = None,
    ) -> Any:
        """List ad report tasks."""
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if report_task_statuses is not None:
            params["report_task_statuses"] = report_task_statuses
        return self._c.get(f"{_BASE}/ad_report_task", params=params)

    def get_report_task(self, report_task_id: str) -> Any:
        """Get a specific report task."""
        return self._c.get(f"{_BASE}/ad_report_task/{report_task_id}")

    def delete_report_task(self, report_task_id: str) -> Any:
        """Delete a report task."""
        return self._c.delete(f"{_BASE}/ad_report_task/{report_task_id}")

    def get_report(self, report_task_id: str) -> Any:
        """Download a completed report."""
        return self._c.get(f"{_BASE}/ad_report_task/{report_task_id}/report")

    def get_report_metadata(self) -> Any:
        """Get report metadata (available report types)."""
        return self._c.get(f"{_BASE}/ad_report_metadata")

    def get_report_metadata_for_report_type(self, report_type: str) -> Any:
        """Get metadata for a specific report type."""
        return self._c.get(f"{_BASE}/ad_report_metadata/{report_type}")
