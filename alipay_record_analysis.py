#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import datetime
import sqlite3

input_fname = 'alipay_record_2years_full.csv'
input_file = csv.DictReader(open(input_fname, 'r'), skipinitialspace=True)
k_set = {"交易创建时间", "交易对方", "商品名称", "金额（元）", "收/支", "交易状态"}

def print_list(l):
  print "(",
  for i in l: print i , ",",
  print ")"

def print_dict(d):
  for i in d: print "'" + i + "' : '" + d[i] + "'"

def clean_dict(d):
  return {k.strip():d[k].strip().decode('utf-8') for k in d if k.strip() in k_set}

order_list = [clean_dict(item) for item in input_file]
for k in k_set:
  print k, order_list[0][k]
print "==========================================="

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''create table data (shop text, product text, price real, month integer)''')
conn.commit()

for order in order_list:
	price = order["金额（元）"]
	if not price:
		continue
	price = float(price)
	if order["收/支"] == u"收入":
		price = -1 * price
	elif order["收/支"] != u"支出":
		continue
	month = datetime.datetime.strptime(order["交易创建时间"], "%m/%d/%Y %H:%M:%S").month
	c.execute("""insert into data values (?,?,?,?)""", (order["交易对方"], order["商品名称"].replace(u"退款-",""), price, month))

conn.commit()

c.execute('''select * from (select shop, sum(price) as price, GROUP_CONCAT(product) from data group by shop) where price > 1 or price < -1 order by price desc''')
#c.execute('''select * from (select shop, product, sum(price) as price, min(month) as month from data group by shop, product) where price > 1 or price < -1 order by price desc''')
#c.execute('''select sum(price) as price from data''')

with open(input_fname[:-4]+"_result"+'.csv', 'wb') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['shop', 'price', 'products'])
  for row in c:
    #print_list(row)
    writer.writerow([unicode(i).encode('utf-8') for i in row])
