"""Tests for `bucky_testing` module."""
from typing import Generator

import pytest

import bucky_testing


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield bucky_testing.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert True  # version == "0.7.0"
