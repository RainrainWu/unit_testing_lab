import logging

import pytest

LOGGER = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--dependency",
        type=str,
        action="append",
        help="only run integration tests if dependency is provided.",
    )


def pytest_runtest_setup(item):

    if dependencies_required := set(
        map(lambda m: m.args[0], item.iter_markers(name="integration"))
    ):
        LOGGER.info(f"dependencies required: {dependencies_required!r}")

        dependencies_provided = set(item.config.getoption("--dependency") or ())
        LOGGER.info(f"dependencies provided: {dependencies_provided!r}")

        if missing := dependencies_required - dependencies_provided:
            pytest.skip(f"dependencies missing: {missing!r}")
