"""Base eBay API client — handles auth and HTTP requests."""

from __future__ import annotations

from typing import Any

import httpx
from ebay_oauth import EbayOAuthClient


class EbayApiError(Exception):
    """Raised when the eBay API returns a non-2xx response."""

    def __init__(self, status_code: int, detail: Any, url: str) -> None:
        self.status_code = status_code
        self.detail = detail
        self.url = url
        super().__init__(f"eBay API error {status_code} for {url}: {detail}")


class EbayClient:
    """Thin wrapper around eBay REST APIs.

    Uses ``ldraney-ebay-oauth`` for token management and ``httpx`` for HTTP.

    Parameters
    ----------
    oauth_client:
        An authenticated ``EbayOAuthClient`` instance.
    sandbox:
        If *True*, hit the eBay sandbox environment instead of production.
    timeout:
        HTTP request timeout in seconds.
    """

    PRODUCTION_BASE = "https://api.ebay.com"
    SANDBOX_BASE = "https://api.sandbox.ebay.com"

    def __init__(
        self,
        oauth_client: EbayOAuthClient,
        *,
        sandbox: bool = False,
        timeout: float = 30.0,
    ) -> None:
        self._oauth = oauth_client
        self._base_url = self.SANDBOX_BASE if sandbox else self.PRODUCTION_BASE
        self._http = httpx.Client(base_url=self._base_url, timeout=timeout)

    # -- helpers ---------------------------------------------------------------

    def _headers(self, extra: dict[str, str] | None = None) -> dict[str, str]:
        token = self._oauth.get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if extra:
            headers.update(extra)
        return headers

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
        headers: dict[str, str] | None = None,
    ) -> Any:
        resp = self._http.request(
            method,
            path,
            params=params,
            json=json,
            headers=self._headers(headers),
        )
        if resp.status_code == 204:
            return None
        body = resp.json() if resp.content else None
        if not resp.is_success:
            raise EbayApiError(resp.status_code, body, str(resp.url))
        return body

    def get(self, path: str, *, params: dict[str, Any] | None = None, headers: dict[str, str] | None = None) -> Any:
        return self._request("GET", path, params=params, headers=headers)

    def post(self, path: str, *, json: Any | None = None, params: dict[str, Any] | None = None, headers: dict[str, str] | None = None) -> Any:
        return self._request("POST", path, json=json, params=params, headers=headers)

    def put(self, path: str, *, json: Any | None = None, params: dict[str, Any] | None = None, headers: dict[str, str] | None = None) -> Any:
        return self._request("PUT", path, json=json, params=params, headers=headers)

    def delete(self, path: str, *, params: dict[str, Any] | None = None, headers: dict[str, str] | None = None) -> Any:
        return self._request("DELETE", path, params=params, headers=headers)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> EbayClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    # -- sub-API accessors (lazy) ---------------------------------------------

    @property
    def buy_browse(self):
        from ebay_sdk.buy.browse import BuyBrowseApi
        return BuyBrowseApi(self)

    @property
    def sell_inventory(self):
        from ebay_sdk.sell.inventory import SellInventoryApi
        return SellInventoryApi(self)

    @property
    def sell_fulfillment(self):
        from ebay_sdk.sell.fulfillment import SellFulfillmentApi
        return SellFulfillmentApi(self)

    @property
    def sell_account(self):
        from ebay_sdk.sell.account import SellAccountApi
        return SellAccountApi(self)

    @property
    def sell_finances(self):
        from ebay_sdk.sell.finances import SellFinancesApi
        return SellFinancesApi(self)

    @property
    def sell_marketing(self):
        from ebay_sdk.sell.marketing import SellMarketingApi
        return SellMarketingApi(self)

    @property
    def sell_feed(self):
        from ebay_sdk.sell.feed import SellFeedApi
        return SellFeedApi(self)

    @property
    def commerce_taxonomy(self):
        from ebay_sdk.commerce.taxonomy import CommerceTaxonomyApi
        return CommerceTaxonomyApi(self)
