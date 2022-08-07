import pytest

from unittest.mock import patch

from unit_testing_lab.randomizer import Randomizer


@pytest.fixture(scope="function")
def fixture_patched_pick():

    with patch.object(Randomizer, "pick") as patched_pick:
        yield patched_pick

@pytest.fixture(scope="function")
def fixture_patched_pick_with_return_value(fixture_patched_pick):

    fixture_patched_pick.side_effect = range(10)
    yield fixture_patched_pick

@pytest.fixture(scope="function")
def fixture_patched_pick_with_error_raised(fixture_patched_pick):

    fixture_patched_pick.side_effect = ValueError
    yield fixture_patched_pick
