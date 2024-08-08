# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DomainEditParams"]


class DomainEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    domain: Optional[str]

    lookback_hops: Optional[int]