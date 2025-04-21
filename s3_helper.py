import boto3
import os

class S3Helper:
    def __init__(self, aws_access_key=None, aws_secret_key=None, region_name="us-east-1"):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key or os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=aws_secret_key or os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=region_name or os.getenv("AWS_REGION", "us-east-1")
        )

    def upload_file(self, bucket_name, file_path, key=None):
        key = key or os.path.basename(file_path)
        self.s3.upload_file(file_path, bucket_name, key)
        print(f"✅ Uploaded '{file_path}' to 's3://{bucket_name}/{key}'")

    def download_file(self, bucket_name, key, dest_path):
        self.s3.download_file(bucket_name, key, dest_path)
        print(f"⬇️ Downloaded 's3://{bucket_name}/{key}' to '{dest_path}'")
