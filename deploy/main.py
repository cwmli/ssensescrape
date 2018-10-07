import os
import boto3
import botocore

import scrape_d

def lambda_handler(event, context):
    file = scrape_d.get_content(os.environ['TARGET_URL'])
    
    # upload the csv to s3
    session = boto3.Session(
        aws_access_key_id = os.environ['AWS_KEY'],
        aws_secret_access_key = os.environ['AWS_SECRET'],
        region_name = os.environ['REGION_NAME']
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket(os.environ['S3_BUCKET'])
    exists = True
    
    try:
        s3.meta.client.head_bucket(Bucket = os.environ['S3_BUCKET'])
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = e.response['Error']['Code']
        if error_code == '404':
            exists = False
            
    if exists:
        s3.meta.client.upload_file(
            '/tmp/%s.csv' % file, 
            os.environ['S3_BUCKET'], 
            '%s.csv' % file)
