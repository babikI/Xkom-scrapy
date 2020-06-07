# -*- coding: utf-8 -*-
import sqlite3


class XkomPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('products.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS products_tb """)
        self.curr.execute("""create table products_tb(
                        product_name text,
                        product_processor text,
                        product_graphics text,
                        product_RAM text,
                        price text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        print('Pipeline:' + item['product_name'][0])
        return item

    def store_db(self, item):

        for i in range(len(item['product_name']) - 1):
            self.curr.execute("""insert into products_tb values (?, ?, ?, ?, ?)""",(
                item['product_name'][i],
                item['product_processor'][i],
                item['product_graphics'][i],
                item['product_ram'][i],
                item['product_price'][i]
                ))
            self.conn.commit()
