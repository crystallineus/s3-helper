from s3_helper import S3Helper
from dotenv import load_dotenv
import os

load_dotenv()

s3 = S3Helper()
s3.upload_file(os.getenv("AWS_BUCKET_NAME"), "local.txt")
s3.download_file(os.getenv("AWS_BUCKET_NAME"), "local.txt", "downloaded.txt")
