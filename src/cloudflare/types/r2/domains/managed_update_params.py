# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ManagedUpdateParams"]


class ManagedUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    enabled: Required[bool]
    """Whether to enable public bucket access at the r2.dev domain"""