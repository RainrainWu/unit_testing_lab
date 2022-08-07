import pytest

from unit_testing_lab.randomizer import Randomizer


class TestRandomizer:

    def test_pick(self):

        assert 0 <= Randomizer.pick() < 1

    @pytest.mark.parametrize(
        "factor",
        (pytest.param(x) for x in range(10))
    )
    def test_amplify(self, factor, fixture_patched_pick):

        fixture_patched_pick.return_value = 0.5

        assert Randomizer.amplify(factor) == factor * 0.5
        fixture_patched_pick.assert_called_once_with()

    def test_shift(self, fixture_patched_pick_with_return_value):

        for value in range(10):
            assert Randomizer.shift(value) == value * 2

        fixture_patched_pick_with_return_value.assert_called_with()

    def test_shift_error(self, fixture_patched_pick_with_error_raised):

        with pytest.raises(ValueError):
            Randomizer.shift(0)

        fixture_patched_pick_with_error_raised.assert_called_once_with()
