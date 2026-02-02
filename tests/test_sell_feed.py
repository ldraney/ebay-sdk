"""Integration tests for Sell Feed API.

Spec: https://developer.ebay.com/api-docs/master/sell/feed/openapi/3/sell_feed_v1_oas3.json
"""

import pytest

from ebay_sdk import EbayClient
from ebay_sdk.client import EbayApiError


@pytest.mark.integration
class TestTasks:
    def test_get_tasks(self, ebay: EbayClient):
        result = ebay.sell_feed.get_tasks(limit=5)
        assert isinstance(result, dict)

    def test_create_task(self, ebay: EbayClient):
        body = {
            "feedType": "LMS_ORDER_REPORT",
            "schemaVersion": "1.0",
        }
        try:
            result = ebay.sell_feed.create_task(body)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (403, 409):
                pytest.skip(f"create_task not available: {exc.status_code}")
            raise

    def test_get_task(self, ebay: EbayClient):
        tasks = ebay.sell_feed.get_tasks(limit=1)
        items = tasks.get("tasks", [])
        if not items:
            pytest.skip("No tasks available in sandbox")
        task_id = items[0]["taskId"]
        result = ebay.sell_feed.get_task(task_id)
        assert isinstance(result, dict)
        assert result["taskId"] == task_id

    def test_upload_file(self, ebay: EbayClient):
        tasks = ebay.sell_feed.get_tasks(limit=10)
        items = tasks.get("tasks", [])
        # Find a task in CREATED status that accepts uploads
        target = None
        for t in items:
            if t.get("uploadSummary") is not None or t.get("status") == "CREATED":
                target = t
                break
        if target is None:
            pytest.skip("No task available for file upload in sandbox")
        try:
            result = ebay.sell_feed.upload_file(target["taskId"], {})
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (403, 404, 409):
                pytest.skip(f"upload_file not available: {exc.status_code}")
            raise

    def test_download_result_file(self, ebay: EbayClient):
        tasks = ebay.sell_feed.get_tasks(limit=10)
        items = tasks.get("tasks", [])
        target = None
        for t in items:
            if t.get("status") == "COMPLETED":
                target = t
                break
        if target is None:
            pytest.skip("No completed task available for download in sandbox")
        try:
            result = ebay.sell_feed.download_result_file(target["taskId"])
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (403, 404):
                pytest.skip(f"download_result_file not available: {exc.status_code}")
            raise


@pytest.mark.integration
class TestOrderTasks:
    def test_get_order_tasks(self, ebay: EbayClient):
        result = ebay.sell_feed.get_order_tasks(limit=5)
        assert isinstance(result, dict)

    def test_create_order_task(self, ebay: EbayClient):
        body = {
            "feedType": "LMS_ORDER_REPORT",
            "filterCriteria": {
                "creationDateRange": {
                    "from": "2024-01-01T00:00:00.000Z",
                    "to": "2024-01-02T00:00:00.000Z",
                },
            },
            "schemaVersion": "1.0",
        }
        try:
            result = ebay.sell_feed.create_order_task(body)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (403, 409):
                pytest.skip(f"create_order_task not available: {exc.status_code}")
            raise

    def test_get_order_task(self, ebay: EbayClient):
        tasks = ebay.sell_feed.get_order_tasks(limit=1)
        items = tasks.get("tasks", [])
        if not items:
            pytest.skip("No order tasks available in sandbox")
        task_id = items[0]["taskId"]
        result = ebay.sell_feed.get_order_task(task_id)
        assert isinstance(result, dict)
        assert result["taskId"] == task_id


@pytest.mark.integration
class TestInventoryTasks:
    def test_get_inventory_tasks(self, ebay: EbayClient):
        result = ebay.sell_feed.get_inventory_tasks(limit=5)
        assert isinstance(result, dict)

    def test_create_inventory_task(self, ebay: EbayClient):
        body = {
            "feedType": "LMS_ACTIVE_INVENTORY_REPORT",
            "schemaVersion": "1.0",
        }
        try:
            result = ebay.sell_feed.create_inventory_task(body)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (403, 409):
                pytest.skip(f"create_inventory_task not available: {exc.status_code}")
            raise

    def test_get_inventory_task(self, ebay: EbayClient):
        tasks = ebay.sell_feed.get_inventory_tasks(limit=1)
        items = tasks.get("tasks", [])
        if not items:
            pytest.skip("No inventory tasks available in sandbox")
        task_id = items[0]["taskId"]
        result = ebay.sell_feed.get_inventory_task(task_id)
        assert isinstance(result, dict)
        assert result["taskId"] == task_id


@pytest.mark.integration
class TestCustomerServiceMetricTasks:
    def test_get_customer_service_metric_tasks(self, ebay: EbayClient):
        result = ebay.sell_feed.get_customer_service_metric_tasks(limit=5)
        assert isinstance(result, dict)

    def test_create_customer_service_metric_task(self, ebay: EbayClient):
        body = {
            "feedType": "CUSTOMER_SERVICE_METRICS_REPORT",
            "schemaVersion": "1.0",
        }
        try:
            result = ebay.sell_feed.create_customer_service_metric_task(body)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (403, 409):
                pytest.skip(
                    f"create_customer_service_metric_task not available: "
                    f"{exc.status_code}"
                )
            raise

    def test_get_customer_service_metric_task(self, ebay: EbayClient):
        tasks = ebay.sell_feed.get_customer_service_metric_tasks(limit=1)
        items = tasks.get("tasks", [])
        if not items:
            pytest.skip("No customer service metric tasks available in sandbox")
        task_id = items[0]["taskId"]
        result = ebay.sell_feed.get_customer_service_metric_task(task_id)
        assert isinstance(result, dict)
        assert result["taskId"] == task_id


@pytest.mark.integration
class TestSchedules:
    def test_get_schedules(self, ebay: EbayClient):
        try:
            result = ebay.sell_feed.get_schedules("LMS_ORDER_REPORT", limit=5)
            assert isinstance(result, dict)
        except EbayApiError as exc:
            if exc.status_code in (403,):
                pytest.skip(f"get_schedules not available: {exc.status_code}")
            raise

    def test_create_get_update_delete_schedule(self, ebay: EbayClient):
        body = {
            "feedType": "LMS_ORDER_REPORT",
            "preferredTriggerHour": 10,
            "preferredTriggerDayOfWeek": "MONDAY",
            "scheduleTemplateId": "",
            "schemaVersion": "1.0",
        }
        # Try to find a valid schedule template ID first
        try:
            templates = ebay.sell_feed.get_schedule_templates("LMS_ORDER_REPORT")
            tmpl_list = templates.get("scheduleTemplates", [])
            if tmpl_list:
                body["scheduleTemplateId"] = tmpl_list[0]["scheduleTemplateId"]
        except EbayApiError:
            pass

        schedule_id = None
        try:
            create_result = ebay.sell_feed.create_schedule(body)
            assert isinstance(create_result, dict)
            schedule_id = create_result.get("scheduleId")
            if schedule_id is None:
                pytest.skip("create_schedule returned no scheduleId")

            # get_schedule
            get_result = ebay.sell_feed.get_schedule(schedule_id)
            assert isinstance(get_result, dict)
            assert get_result["scheduleId"] == schedule_id

            # update_schedule
            update_body = {"preferredTriggerHour": 12}
            update_result = ebay.sell_feed.update_schedule(schedule_id, update_body)
            # update may return empty or dict
            assert update_result is None or isinstance(update_result, dict)

        except EbayApiError as exc:
            if exc.status_code in (403, 409):
                pytest.skip(f"Schedule CRUD not available: {exc.status_code}")
            raise
        finally:
            if schedule_id is not None:
                try:
                    ebay.sell_feed.delete_schedule(schedule_id)
                except EbayApiError:
                    pass

    def test_get_schedule(self, ebay: EbayClient):
        try:
            schedules = ebay.sell_feed.get_schedules("LMS_ORDER_REPORT", limit=1)
        except EbayApiError as exc:
            if exc.status_code in (403,):
                pytest.skip(f"get_schedules not available: {exc.status_code}")
            raise
        items = schedules.get("schedules", [])
        if not items:
            pytest.skip("No schedules available in sandbox")
        schedule_id = items[0]["scheduleId"]
        result = ebay.sell_feed.get_schedule(schedule_id)
        assert isinstance(result, dict)
        assert result["scheduleId"] == schedule_id

    @pytest.mark.skip(reason="delete_schedule covered by CRUD lifecycle test")
    def test_delete_schedule(self, ebay: EbayClient):
        pass

    @pytest.mark.skip(reason="update_schedule covered by CRUD lifecycle test")
    def test_update_schedule(self, ebay: EbayClient):
        pass

    def test_get_latest_result_file(self, ebay: EbayClient):
        try:
            schedules = ebay.sell_feed.get_schedules("LMS_ORDER_REPORT", limit=5)
        except EbayApiError as exc:
            if exc.status_code in (403,):
                pytest.skip(f"get_schedules not available: {exc.status_code}")
            raise
        items = schedules.get("schedules", [])
        if not items:
            pytest.skip("No schedules available for latest result file")
        schedule_id = items[0]["scheduleId"]
        try:
            result = ebay.sell_feed.get_latest_result_file(schedule_id)
            assert result is not None
        except EbayApiError as exc:
            if exc.status_code in (403, 404):
                pytest.skip(
                    f"get_latest_result_file not available: {exc.status_code}"
                )
            raise

    def test_get_schedule_templates(self, ebay: EbayClient):
        result = ebay.sell_feed.get_schedule_templates("LMS_ORDER_REPORT")
        assert isinstance(result, dict)

    def test_get_schedule_template(self, ebay: EbayClient):
        templates = ebay.sell_feed.get_schedule_templates("LMS_ORDER_REPORT")
        items = templates.get("scheduleTemplates", [])
        if not items:
            pytest.skip("No schedule templates available in sandbox")
        template_id = items[0]["scheduleTemplateId"]
        result = ebay.sell_feed.get_schedule_template(template_id)
        assert isinstance(result, dict)
        assert result["scheduleTemplateId"] == template_id
