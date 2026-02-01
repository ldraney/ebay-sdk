"""Shared fixtures for integration tests.

All tests hit the real eBay sandbox API — no mocks.
Requires sandbox credentials configured for ``ldraney-ebay-oauth``.
"""

import os

import pytest
from ebay_oauth import EbayOAuthClient

from ebay_sdk import EbayClient


@pytest.fixture(scope="session")
def oauth_client() -> EbayOAuthClient:
    """Return a real EbayOAuthClient using sandbox credentials.

    Expects the standard env vars used by ``ldraney-ebay-oauth``.
    Skip the entire test session if credentials are missing.
    """
    required_vars = [
        "EBAY_CLIENT_ID",
        "EBAY_CLIENT_SECRET",
    ]
    missing = [v for v in required_vars if not os.environ.get(v)]
    if missing:
        pytest.skip(f"Missing eBay sandbox credentials: {', '.join(missing)}")

    return EbayOAuthClient(
        client_id=os.environ["EBAY_CLIENT_ID"],
        client_secret=os.environ["EBAY_CLIENT_SECRET"],
        sandbox=True,
    )


@pytest.fixture(scope="session")
def ebay(oauth_client: EbayOAuthClient) -> EbayClient:
    """Return a real EbayClient pointed at the sandbox."""
    client = EbayClient(oauth_client, sandbox=True)
    yield client
    client.close()
