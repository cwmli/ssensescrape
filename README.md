# Setup
## Local
- Install python (working on 3.6)
- `pip install selenium`
- Install `chromium-chromedriver` and add it to `$PATH`

   `export PATH=$PATH:/usr/lib/chromium-browser/`
- Run `python scrape.py TARGET_URL`

## Deploying on AWS Lambda
- See `deploy` directory
