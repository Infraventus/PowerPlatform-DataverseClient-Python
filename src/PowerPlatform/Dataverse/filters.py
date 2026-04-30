# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Compatibility imports for composable OData filter expressions.

This module exposes the filter helpers at ``PowerPlatform.Dataverse.filters``
while preserving the original ``PowerPlatform.Dataverse.models.filters`` path.
"""

from __future__ import annotations

from .models.filters import (
    FilterExpression,
    between,
    contains,
    endswith,
    eq,
    filter_in,
    ge,
    gt,
    is_not_null,
    is_null,
    le,
    lt,
    ne,
    not_between,
    not_in,
    raw,
    startswith,
)

__all__ = [
    "FilterExpression",
    "eq",
    "ne",
    "gt",
    "ge",
    "lt",
    "le",
    "contains",
    "startswith",
    "endswith",
    "between",
    "is_null",
    "is_not_null",
    "filter_in",
    "not_in",
    "not_between",
    "raw",
]
