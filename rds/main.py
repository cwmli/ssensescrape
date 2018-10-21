import os
import sys
import logging
import pymysql

#RDS_SETTINGS
RDS_HOST = os.environ['RDS_HOST']
NAME     = os.environ['DB_USER']
PW       = os.environ['DB_PWD']
DB       = os.environ['DB_NAME']

TARGET   = os.environ['DB_TABLE']
SOURCE   = os.environ['SOURCE']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
  rds_con = pymysql.connect(RDS_HOST, user = NAME,
                                      passwd = PW,
                                      db = DB)
except:
  logger.error("ERROR: could not connect to mysql instance")
  sys.exit()

logger.info("SUCCESS: connected to %s" % RDS_HOST)

def handler(event, context):
  try:
    with rds_con.cursor() as cur:
      sql = "COPY %s FROM '%s'" % (TARGET, SOURCE)
      cur.execute(sql)
      logger.info("SUCCESS: appending %s to %s" % (SOURCE, TARGET))
    rds_con.commit()
  finally:
    rds_con.close()
