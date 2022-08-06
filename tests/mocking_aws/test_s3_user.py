import pytest
from botocore.exceptions import ClientError


class TestS3User:
    @pytest.mark.xfail
    def test_check_object_exist_failed(self, fixture_s3_user, fixture_s3_object_key):

        assert fixture_s3_user.check_object_exist(fixture_s3_object_key)

    def test_check_object_exist(
        self,
        fixture_s3_object,
        fixture_s3_user,
        fixture_s3_object_key,
    ):

        assert fixture_s3_user.check_object_exist(fixture_s3_object_key)

    def test_get_object_content_failed_no_bucket(
        self,
        fixture_s3_user,
        fixture_s3_object_key,
    ):

        with pytest.raises(ClientError):
            fixture_s3_user.get_object_content(fixture_s3_object_key)

    def test_get_object_content_failed_no_object(
        self,
        fixture_s3_bucket,
        fixture_s3_user,
        fixture_s3_object_key,
    ):

        with pytest.raises(ClientError):
            fixture_s3_user.get_object_content(fixture_s3_object_key)

    def test_get_object_content(
        self,
        fixture_s3_object,
        fixture_s3_user,
        fixture_s3_object_key,
        fixture_s3_object_content,
    ):

        content = fixture_s3_user.get_object_content(fixture_s3_object_key)
        assert content == fixture_s3_object_content
