"""Sell Feed API — bulk download/upload via tasks and schedules.

Spec: https://developer.ebay.com/api-docs/master/sell/feed/openapi/3/sell_feed_v1_oas3.json
Version: v1.3.1
"""

from __future__ import annotations

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ebay_sdk.client import EbayClient

_BASE = "/sell/feed/v1"


class SellFeedApi:
    def __init__(self, client: EbayClient) -> None:
        self._c = client

    # -- Task ------------------------------------------------------------------

    def get_tasks(
        self,
        *,
        feed_type: str | None = None,
        schedule_id: str | None = None,
        look_back_days: int | None = None,
        date_range: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List feed tasks."""
        params: dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if schedule_id is not None:
            params["schedule_id"] = schedule_id
        if look_back_days is not None:
            params["look_back_days"] = look_back_days
        if date_range is not None:
            params["date_range"] = date_range
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/task", params=params)

    def create_task(self, body: dict[str, Any]) -> Any:
        """Create a feed task."""
        return self._c.post(f"{_BASE}/task", json=body)

    def get_task(self, task_id: str) -> Any:
        """Get a specific task."""
        return self._c.get(f"{_BASE}/task/{task_id}")

    def upload_file(self, task_id: str, body: Any) -> Any:
        """Upload a file for a task."""
        return self._c.post(f"{_BASE}/task/{task_id}/upload_file", json=body)

    def download_result_file(self, task_id: str) -> Any:
        """Download the result file for a completed task."""
        return self._c.get(f"{_BASE}/task/{task_id}/download_result_file")

    # -- Order Task ------------------------------------------------------------

    def get_order_tasks(
        self,
        *,
        feed_type: str | None = None,
        schedule_id: str | None = None,
        look_back_days: int | None = None,
        date_range: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List order download tasks."""
        params: dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if schedule_id is not None:
            params["schedule_id"] = schedule_id
        if look_back_days is not None:
            params["look_back_days"] = look_back_days
        if date_range is not None:
            params["date_range"] = date_range
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/order_task", params=params)

    def create_order_task(self, body: dict[str, Any]) -> Any:
        """Create an order download task."""
        return self._c.post(f"{_BASE}/order_task", json=body)

    def get_order_task(self, task_id: str) -> Any:
        """Get a specific order task."""
        return self._c.get(f"{_BASE}/order_task/{task_id}")

    # -- Inventory Task --------------------------------------------------------

    def get_inventory_tasks(
        self,
        *,
        feed_type: str | None = None,
        schedule_id: str | None = None,
        look_back_days: int | None = None,
        date_range: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List inventory tasks."""
        params: dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if schedule_id is not None:
            params["schedule_id"] = schedule_id
        if look_back_days is not None:
            params["look_back_days"] = look_back_days
        if date_range is not None:
            params["date_range"] = date_range
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/inventory_task", params=params)

    def create_inventory_task(self, body: dict[str, Any]) -> Any:
        """Create an inventory task."""
        return self._c.post(f"{_BASE}/inventory_task", json=body)

    def get_inventory_task(self, task_id: str) -> Any:
        """Get a specific inventory task."""
        return self._c.get(f"{_BASE}/inventory_task/{task_id}")

    # -- Customer Service Metric Task ------------------------------------------

    def get_customer_service_metric_tasks(
        self,
        *,
        feed_type: str | None = None,
        date_range: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List customer service metric tasks."""
        params: dict[str, Any] = {}
        if feed_type is not None:
            params["feed_type"] = feed_type
        if date_range is not None:
            params["date_range"] = date_range
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/customer_service_metric_task", params=params)

    def create_customer_service_metric_task(self, body: dict[str, Any]) -> Any:
        """Create a customer service metric task."""
        return self._c.post(f"{_BASE}/customer_service_metric_task", json=body)

    def get_customer_service_metric_task(self, task_id: str) -> Any:
        """Get a specific customer service metric task."""
        return self._c.get(f"{_BASE}/customer_service_metric_task/{task_id}")

    # -- Schedule --------------------------------------------------------------

    def get_schedules(
        self,
        feed_type: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List schedules for a feed type."""
        params: dict[str, Any] = {"feed_type": feed_type}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/schedule", params=params)

    def create_schedule(self, body: dict[str, Any]) -> Any:
        """Create a schedule."""
        return self._c.post(f"{_BASE}/schedule", json=body)

    def get_schedule(self, schedule_id: str) -> Any:
        """Get a specific schedule."""
        return self._c.get(f"{_BASE}/schedule/{schedule_id}")

    def update_schedule(self, schedule_id: str, body: dict[str, Any]) -> Any:
        """Update a schedule."""
        return self._c.put(f"{_BASE}/schedule/{schedule_id}", json=body)

    def delete_schedule(self, schedule_id: str) -> Any:
        """Delete a schedule."""
        return self._c.delete(f"{_BASE}/schedule/{schedule_id}")

    def get_latest_result_file(self, schedule_id: str) -> Any:
        """Download the latest result file for a schedule."""
        return self._c.get(
            f"{_BASE}/schedule/{schedule_id}/download_result_file"
        )

    # -- Schedule Template -----------------------------------------------------

    def get_schedule_templates(
        self,
        feed_type: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
    ) -> Any:
        """List schedule templates for a feed type."""
        params: dict[str, Any] = {"feed_type": feed_type}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self._c.get(f"{_BASE}/schedule_template", params=params)

    def get_schedule_template(self, schedule_template_id: str) -> Any:
        """Get a specific schedule template."""
        return self._c.get(f"{_BASE}/schedule_template/{schedule_template_id}")
