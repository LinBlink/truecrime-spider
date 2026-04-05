# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open("output.json", "w", encoding="utf-8")
        self.items = []

    def close_spider(self, spider):
        json.dump(
            self.items,
            self.file,
            ensure_ascii=False,
            indent=2
        )
        self.file.close()

    def process_item(self, item, spider):
        self.items.append(
            dict( item )
        )

        return item
