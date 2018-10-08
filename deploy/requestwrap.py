import json
import os
from selenium import webdriver

import logger

def get_json(url):
  logger.info("GET: %s" % url)
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-gpu')
  options.add_argument('--window-size=1280x1696')
  options.add_argument('--user-data-dir=/tmp/user-data')
  options.add_argument('--hide-scrollbars')
  options.add_argument('--enable-logging')
  options.add_argument('--log-level=0')
  options.add_argument('--v=99')
  options.add_argument('--single-process')
  options.add_argument('--data-path=/tmp/data-path')
  options.add_argument('--ignore-certificate-errors')
  options.add_argument('--homedir=/tmp')
  options.add_argument('--disk-cache-dir=/tmp/cache-dir')
  options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
  options.binary_location = os.getcwd() + "/bin/headless-chromium"

  driver = webdriver.Chrome(chrome_options=options)

  driver.get(url)
  pre = driver.find_element_by_tag_name("pre").text

  try:
    return json.loads(pre)
  except Exception as e:
    logger.err(e)
    return None
  finally:
    driver.close()
