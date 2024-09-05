# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar.ai.gateway import (
    TimeseriesGroupModelResponse,
    TimeseriesGroupProviderResponse,
    TimeseriesGroupTaskResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.ai.gateway import timeseries_group_model_params
from cloudflare.types.radar.ai.gateway import timeseries_group_provider_params
from cloudflare.types.radar.ai.gateway import timeseries_group_task_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseriesGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_model(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.gateway.timeseries_groups.model()
        assert_matches_type(TimeseriesGroupModelResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_model_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.gateway.timeseries_groups.model(
            agg_interval="15m",
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit_per_group=4,
            name=["string", "string", "string"],
        )
        assert_matches_type(TimeseriesGroupModelResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_model(self, client: Cloudflare) -> None:
        response = client.radar.ai.gateway.timeseries_groups.with_raw_response.model()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupModelResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_model(self, client: Cloudflare) -> None:
        with client.radar.ai.gateway.timeseries_groups.with_streaming_response.model() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupModelResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_provider(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.gateway.timeseries_groups.provider()
        assert_matches_type(TimeseriesGroupProviderResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_provider_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.gateway.timeseries_groups.provider(
            agg_interval="15m",
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit_per_group=4,
            name=["string", "string", "string"],
        )
        assert_matches_type(TimeseriesGroupProviderResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_provider(self, client: Cloudflare) -> None:
        response = client.radar.ai.gateway.timeseries_groups.with_raw_response.provider()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupProviderResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_provider(self, client: Cloudflare) -> None:
        with client.radar.ai.gateway.timeseries_groups.with_streaming_response.provider() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupProviderResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_task(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.gateway.timeseries_groups.task()
        assert_matches_type(TimeseriesGroupTaskResponse, timeseries_group, path=["response"])

    @parametrize
    def test_method_task_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.ai.gateway.timeseries_groups.task(
            agg_interval="15m",
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit_per_group=4,
            name=["string", "string", "string"],
        )
        assert_matches_type(TimeseriesGroupTaskResponse, timeseries_group, path=["response"])

    @parametrize
    def test_raw_response_task(self, client: Cloudflare) -> None:
        response = client.radar.ai.gateway.timeseries_groups.with_raw_response.task()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupTaskResponse, timeseries_group, path=["response"])

    @parametrize
    def test_streaming_response_task(self, client: Cloudflare) -> None:
        with client.radar.ai.gateway.timeseries_groups.with_streaming_response.task() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupTaskResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseriesGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_model(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.gateway.timeseries_groups.model()
        assert_matches_type(TimeseriesGroupModelResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_model_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.gateway.timeseries_groups.model(
            agg_interval="15m",
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit_per_group=4,
            name=["string", "string", "string"],
        )
        assert_matches_type(TimeseriesGroupModelResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_model(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.gateway.timeseries_groups.with_raw_response.model()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupModelResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_model(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.gateway.timeseries_groups.with_streaming_response.model() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupModelResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_provider(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.gateway.timeseries_groups.provider()
        assert_matches_type(TimeseriesGroupProviderResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_provider_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.gateway.timeseries_groups.provider(
            agg_interval="15m",
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit_per_group=4,
            name=["string", "string", "string"],
        )
        assert_matches_type(TimeseriesGroupProviderResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_provider(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.gateway.timeseries_groups.with_raw_response.provider()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupProviderResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_provider(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.gateway.timeseries_groups.with_streaming_response.provider() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupProviderResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_task(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.gateway.timeseries_groups.task()
        assert_matches_type(TimeseriesGroupTaskResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_method_task_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.ai.gateway.timeseries_groups.task(
            agg_interval="15m",
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["7d", "7d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit_per_group=4,
            name=["string", "string", "string"],
        )
        assert_matches_type(TimeseriesGroupTaskResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_raw_response_task(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.gateway.timeseries_groups.with_raw_response.task()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupTaskResponse, timeseries_group, path=["response"])

    @parametrize
    async def test_streaming_response_task(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.gateway.timeseries_groups.with_streaming_response.task() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupTaskResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True