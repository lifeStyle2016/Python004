# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class MoivespiderPipeline:

    def __init__(self):
        movie_title = [('电影名称', '电影类型', '上映时间')]
        pd_title = pd.DataFrame(data=movie_title)
        pd_title.to_csv('./movie_detail.csv', sep=',', mode='w', encoding='utf_8_sig', index=False, header=False)


    def process_item(self, item, spider):
        movie_detail = [(item['movie_name'], item['movie_type'], item['movie_time'])]
        print(movie_detail)
        pd_title = pd.DataFrame(data=movie_detail)
        pd_title.to_csv('./movie_detail.csv', sep=',', mode='a', encoding='utf_8_sig', index=False, header=False)
        return item
