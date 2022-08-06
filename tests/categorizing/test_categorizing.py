import pytest


@pytest.mark.pre_commit
@pytest.mark.ci
class TestCategorizingGroupA:
    def test_categorizing_a(self):

        pass

    def test_categorizing_b(self):

        pass

    def test_categorizing_c(self):

        pass


class TestCategorizingGroupB:
    @pytest.mark.pre_commit
    @pytest.mark.benchmark
    def test_categorizing_d(self):

        pass

    @pytest.mark.benchmark
    @pytest.mark.integration("redis")
    def test_categorizing_e(self):

        pass

    @pytest.mark.integration("postgresql")
    def test_categorizing_f(self):

        pass
