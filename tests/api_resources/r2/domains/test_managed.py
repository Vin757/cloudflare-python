# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.r2.domains import ManagedUpdateResponse, ManagedListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2.domains import managed_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManaged:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        managed = client.r2.domains.managed.update(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(ManagedUpdateResponse, managed, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.r2.domains.managed.with_raw_response.update(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed = response.parse()
        assert_matches_type(ManagedUpdateResponse, managed, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.r2.domains.managed.with_streaming_response.update(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed = response.parse()
            assert_matches_type(ManagedUpdateResponse, managed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.domains.managed.with_raw_response.update(
                bucket_name="example-bucket",
                account_id="",
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.domains.managed.with_raw_response.update(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                enabled=True,
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        managed = client.r2.domains.managed.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ManagedListResponse, managed, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.r2.domains.managed.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed = response.parse()
        assert_matches_type(ManagedListResponse, managed, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.r2.domains.managed.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed = response.parse()
            assert_matches_type(ManagedListResponse, managed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.domains.managed.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.domains.managed.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncManaged:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        managed = await async_client.r2.domains.managed.update(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(ManagedUpdateResponse, managed, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.domains.managed.with_raw_response.update(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed = await response.parse()
        assert_matches_type(ManagedUpdateResponse, managed, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.domains.managed.with_streaming_response.update(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed = await response.parse()
            assert_matches_type(ManagedUpdateResponse, managed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.domains.managed.with_raw_response.update(
                bucket_name="example-bucket",
                account_id="",
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.domains.managed.with_raw_response.update(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                enabled=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        managed = await async_client.r2.domains.managed.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ManagedListResponse, managed, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.domains.managed.with_raw_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed = await response.parse()
        assert_matches_type(ManagedListResponse, managed, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.domains.managed.with_streaming_response.list(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed = await response.parse()
            assert_matches_type(ManagedListResponse, managed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.domains.managed.with_raw_response.list(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.domains.managed.with_raw_response.list(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )