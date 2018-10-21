# AWS Lambda Deployment
This is used to trigger an append to a destination database table on RDS
## Setting up AWS Lambda
1. Environment Variables
  - Add `RDS_HOST, DB_USER, DB_PWD, DB_NAME` under the environment variables section (these values should be self explanatory)
  - `DB_TABLE, SOURCE` are used to specify the table to append to from a source
2. Add `main.handler` to the handler section under Function code
***
## Creating deployment package
1. `pip install pymysql` package this in the same location as main.py
2. Zip all necessary files
3. Upload to the lambda function
