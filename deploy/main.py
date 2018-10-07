import os
import boto3
from botocore.exceptions import ClientError

import scrape_d
import logger

# Environment variables
TARGET_URL = os.environ['TARGET_URL']
AWS_KEY = os.environ['AWS_KEY']
AWS_SECRET = os.environ['AWS_SECRET']
REGION_NAME = os.environ['REGION_NAME']
S3_BUCKET = os.environ['S3_BUCKET']

def lambda_handler(event, context):
  file = scrape_d.get_content(TARGET_URL)

  # upload the csv to s3
  session = boto3.Session(
    aws_access_key_id     = AWS_KEY,
    aws_secret_access_key = AWS_SECRET,
    region_name           = REGION_NAME
  )
  s3 = session.resource('s3')
  bucket = s3.Bucket(S3_BUCKET)

  try:
    s3.meta.client.head_bucket(Bucket = S3_BUCKET)

    logger.info('Uploading result of scrape to S3')
    bucket.upload_file(
      '/tmp/%s.csv' % file,
      '%s.csv' % file)
    
    logger.success('Uploaded %s.csv to S3' % file)
  except ClientError as e:
    # 404 error, bucket does not exist.
    error_code = e.response['Error']['Code']
    if error_code == '404':
      logger.err('Bucket(%s) does not exist' % S3_BUCKET)
    else:
      logger.err(e)
