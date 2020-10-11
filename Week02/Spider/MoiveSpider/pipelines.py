# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pymysql

class MoivespiderPipeline:

    # 创建数据库
    def open_spider(self, spider):
        try:
            self.conn = pymysql.connect(host='hadoop100',
                                   user='root',
                                   password='123456',
                                   db='test',
                                   charset='utf8mb4')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f'数据库连接异常:{e}')


    # 插入数据
    def process_item(self, item, spider):
        try:
            sql = 'insert into maoyan_movie_detail(movie_name,movie_type,movie_time) values (%s,%s,%s)'
            movie_detail = (item['movie_name'],item['movie_type'],item['movie_time'])
            self.cursor.execute(sql, movie_detail)
            self.conn.commit()
        except Exception as e:
            print(f'数据库操作异常:{e}')

    # 关闭连接
    def close_spider(self, spider):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f'数据库连接关闭异常：{e}')
