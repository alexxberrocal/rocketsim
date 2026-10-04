"""Smoke test: the package and its modules import."""

import importlib

import pytest

MODULES = ["atmosphere", "aero", "motor", "dynamics", "sim"]


def test_package_imports():
    import rocketsim

    assert rocketsim.__version__


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name):
    importlib.import_module(f"rocketsim.{name}")
