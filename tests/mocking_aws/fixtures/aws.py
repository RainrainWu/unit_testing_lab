import os
from io import BytesIO

import boto3
import pytest
from moto import mock_s3
from unit_testing_lab.s3_user import S3User


@pytest.fixture(scope="session", autouse=True)
def fixture_dummy_aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


@pytest.fixture(scope="session")
def fixture_s3_bucket_name():
    yield "my_s3_bucket"


@pytest.fixture(scope="session")
def fixture_s3_object_key():
    yield "my_s3_object.json"


@pytest.fixture(scope="session")
def fixture_s3_object_content():

    yield "my s3 object fileobj"


@pytest.fixture(scope="session", autouse=True)
def fixture_mock_sqs_resource(fixture_dummy_aws_credentials):
    with mock_s3():
        yield


@pytest.fixture(scope="session")
def fixture_s3_resource(fixture_mock_sqs_resource):
    yield boto3.resource("s3")


@pytest.fixture(scope="session")
def fixture_s3_client(fixture_mock_sqs_resource):
    yield boto3.client("s3")


@pytest.fixture(scope="function")
def fixture_s3_bucket(fixture_s3_resource, fixture_s3_bucket_name):

    yield fixture_s3_resource.create_bucket(Bucket=fixture_s3_bucket_name)
    fixture_s3_resource.Bucket(fixture_s3_bucket_name).delete()


@pytest.fixture(scope="function")
def fixture_s3_object(
    fixture_s3_bucket,
    fixture_s3_object_key,
    fixture_s3_object_content,
):

    fileobj = BytesIO()
    fileobj.write(fixture_s3_object_content.encode())
    fileobj.seek(0)
    yield fixture_s3_bucket.upload_fileobj(
        fileobj,
        fixture_s3_object_key,
    )

    fixture_s3_bucket.delete_objects(
        Delete={"Objects": [{"Key": fixture_s3_object_key}]},
    )


@pytest.fixture(scope="function")
def fixture_s3_user(fixture_s3_bucket_name):

    yield S3User(fixture_s3_bucket_name)
