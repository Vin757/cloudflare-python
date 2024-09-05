# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CustomCreateResponse"]


class CustomCreateResponse(BaseModel):
    domain: str
    """Domain name of the affected custom domain"""

    enabled: bool
    """Whether this bucket is publicly accessible at the specified custom domain"""