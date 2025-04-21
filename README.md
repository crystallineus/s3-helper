# S3 Helper Library (Python)

A lightweight Python helper library for uploading and downloading files to and from AWS S3 using `boto3`.

## Features

- Upload local files to an S3 bucket
- Download files from an S3 bucket
- Uses `.env` for AWS credentials
- Clean class-based design

## Installation

1. **Clone this repo**

   ```bash
   git clone https://github.com/your-username/s3-helper.git
   cd s3-helper
   ```

2. **Install dependencies**

   ```bash
   pip install boto3 python-dotenv
   ```

3. **Create a `.env` file**
   ```env
    AWS_ACCESS_KEY_ID=your-access-key-id
    AWS_SECRET_ACCESS_KEY=your-secret-access-key
    AWS_DEFAULT_REGION=us-east-1
    AWS_BUCKET_NAME=my-bucket
   ```
4. Run the script
   Make sure your bucket is created before running:

   ```bash
   python3 main.py
   ```
