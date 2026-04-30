# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Tests for public filter import compatibility paths."""

from PowerPlatform.Dataverse import filters
from PowerPlatform.Dataverse.filters import FilterExpression, eq, filter_in
from PowerPlatform.Dataverse.models.filters import eq as models_eq


def test_top_level_filters_module_imports_helpers():
    expr = filters.eq("statecode", 0)

    assert isinstance(expr, FilterExpression)
    assert expr.to_odata() == "statecode eq 0"


def test_direct_top_level_filter_imports_match_models_imports():
    assert eq is models_eq
    assert filter_in("statecode", [0, 1]).to_odata() == (
        'Microsoft.Dynamics.CRM.In(PropertyName=\'statecode\',PropertyValues=["0","1"])'
    )
