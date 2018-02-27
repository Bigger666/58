# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class City58Pipeline(object):

    def open_spider(self,spider):
        self.file=open('58_chuzu.txt','w',encoding='utf-8')
        print('亲要打开文件了哦！')


    def process_item(self, item, spider):
        line='{}\n'.format(json.dumps(dict(item)))
        self.file.write(line)
        return item


    def close_spider(self,spider):
        self.file.close()
        print('亲要关闭文件了哦！')
