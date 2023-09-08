# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from itemadapter import ItemAdapter

class DatabaseconnPipeline:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Root@123',
            database = 'library'
        )
    
        self.cur = self.conn.cursor()
        
    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS library_books(
            id int NOT NULL auto_increment, 
            category text,
            title text,
            hyperlink VARCHAR(255),
            PRIMARY KEY (id)
        )
        """)
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS trending_books(
            id int NOT NULL auto_increment, 
            category text,
            title text,
            authors_and_num_of_editions VARCHAR(255),
            PRIMARY KEY (id)
        )
        """)
    
    def process_item(self, item, spider):
        self.cur.execute(""" insert into library_books (category, title, hyperlink) values (%s,%s,%s)""", (
            item['book_category'],
            item['book_title'],
            item['hyperlink']
        ))
        
        #self.cur.execute(""" insert into trending_books (category, title, authors_and_num_of_editions) values (%s,%s,%s)""", (
         #   item['trend_category'],
          #  item['trend_book_title'],
           # item['trend_auth_num_editions']
        #))
        ## Execute insert of data into database
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()