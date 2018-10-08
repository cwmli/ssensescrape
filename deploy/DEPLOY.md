# AWS Lambda Deployment
## Setting up AWS Lambda
1. Create a lambda function on the console
  - Create an execution role that has access to the destination S3 bucket
  - Add a *CloudWatch Event* trigger to set a `cron`
  
2. Environment Variables
  - Add `AWS_KEY, AWS_SECRET, REGION_NAME, S3_BUCKET, BRAND_LIST` under the environment variables section (these values should be self explanatory)
  - Add another environment variable called `PATH` that points to `/var/task/bin` which is where selenium will locate chromedriver
  - Add an environment variable called `PYTHONPATH` that points to `/var/task/lib` which is where python will locate lib files
3. Add `main.lambda_handler` to the handler section under Function code
4. Additional Settings
  - Set timeout to 5 mins and memory to 256mb (adjust as necessary)
***
## Creating deployment package
1. Download headless-chromium and chromedriver, extract these into the `bin` folder
2. Copy required lib files and store these into the `lib` folder
3. Zip all necessary files and the `bin` and `lib` folders
4. Upload to the lambda function and hit **TEST** for a sanity check
