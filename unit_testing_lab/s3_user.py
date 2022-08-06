from io import BytesIO

import boto3
from botocore.exceptions import ClientError


class S3User:
    def __init__(self, bucket_name: str) -> None:

        self.__bucket_name = bucket_name

        self.__resource = boto3.resource("s3")
        self.__client = boto3.client("s3")

        self.__bucket = self.__resource.Bucket(name=self.__bucket_name)

    def check_object_exist(self, key: str) -> bool:

        try:
            self.__client.head_object(Bucket=self.__bucket_name, Key=key)
            return True
        except ClientError:
            return False

    def get_object_content(self, key: str) -> str:

        fileobj = BytesIO()
        self.__bucket.download_fileobj(key, fileobj)

        return fileobj.getvalue().decode()
