# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.gateway.custom_certificate_settings import CustomCertificateSettings

from ....._base_client import make_request_options

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params

__all__ = ["CustomCertificateResource", "AsyncCustomCertificateResource"]


class CustomCertificateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomCertificateResourceWithRawResponse:
        return CustomCertificateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomCertificateResourceWithStreamingResponse:
        return CustomCertificateResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateSettings:
        """
        Fetches the current Zero Trust certificate configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/configuration/custom_certificate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCertificateSettings,
        )


class AsyncCustomCertificateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomCertificateResourceWithRawResponse:
        return AsyncCustomCertificateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomCertificateResourceWithStreamingResponse:
        return AsyncCustomCertificateResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateSettings:
        """
        Fetches the current Zero Trust certificate configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/configuration/custom_certificate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCertificateSettings,
        )


class CustomCertificateResourceWithRawResponse:
    def __init__(self, custom_certificate: CustomCertificateResource) -> None:
        self._custom_certificate = custom_certificate

        self.get = to_raw_response_wrapper(
            custom_certificate.get,
        )


class AsyncCustomCertificateResourceWithRawResponse:
    def __init__(self, custom_certificate: AsyncCustomCertificateResource) -> None:
        self._custom_certificate = custom_certificate

        self.get = async_to_raw_response_wrapper(
            custom_certificate.get,
        )


class CustomCertificateResourceWithStreamingResponse:
    def __init__(self, custom_certificate: CustomCertificateResource) -> None:
        self._custom_certificate = custom_certificate

        self.get = to_streamed_response_wrapper(
            custom_certificate.get,
        )


class AsyncCustomCertificateResourceWithStreamingResponse:
    def __init__(self, custom_certificate: AsyncCustomCertificateResource) -> None:
        self._custom_certificate = custom_certificate

        self.get = async_to_streamed_response_wrapper(
            custom_certificate.get,
        )