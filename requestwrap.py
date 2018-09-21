import json
from selenium import webdriver


def get_json(url):
  print("GET: %s" % url)
  options = webdriver.ChromeOptions()
  options.add_argument('headless')

  driver = webdriver.Chrome(chrome_options=options)

  driver.get(url)
  pre = driver.find_element_by_tag_name("pre").text

  try:
    return json.loads(pre)
  except Exception as e:
    log_err(e)
    return None
  finally:
    driver.close()

def log_err(e):
  print(e)