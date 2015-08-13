import sys
import psycopg2

from psycopg2 import DatabaseError
from scrapy.exceptions import DropItem

class ArticlePipeline(object):
  
  def open_spider(self, spider):
    connection = None
    
    try:
      self.conn = psycopg2.connect(
        user='spider', 
        password='nhibTKRcELTg',
        host='frankfurt-data.cfjkmsuocwwo.eu-central-1.rds.amazonaws.com',
        database='analysisdata',
        port='5432'
      )
      self.cursor = self.conn.cursor()
    
    except DatabaseError, e:
      print 'Error %s' % e
      sys.exit(1)
  
  def process_item(self, item, spider):
    
    # Prepare variables for insertion into sql.
    date   = item['Date'].strftime('%Y-%m-%d %H:%M:%S')
    outlet = item['Outlet']
    title  = item['Title']
    lead   = item['Lead']
    
    # Test for uniqueness.
    selectSql  = """
      SELECT count(*)
      FROM News_Financial
      WHERE Date = %s
        AND Outlet = %s
        AND Title = %s
        AND Lead = %s;
    """    
    self.cursor.execute(selectSql, (date, outlet, title, lead,))
    
    if self.cursor.fetchone()[0] > 0:
      raise DropItem('This article is already stored in the database') 
    
    # Insert the new article and commit.
    insertSql = 'INSERT INTO News_Financial VALUES (%s, %s, %s, %s)'
    self.cursor.execute(insertSql, (date, outlet, title, lead)) 
    self.conn.commit()

  def close_spider(self, spider):
    self.cursor.close()
