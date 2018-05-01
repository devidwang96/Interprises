# -*- coding: utf-8 -*-
__author__ = 'yesdauren'
import urllib.request
import re
from shutil import copyfile
import time
import datetime
from datetime import date
from datetime import datetime
import os.path
import zipfile
import xlrd
from xlrd import open_workbook
import sys
import io
import csv
import logging
from sys import argv

dir_path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(format='%(levelname)s \t %(asctime)s \t %(module)s \t %(message)s', level=logging.INFO,
                    filename=dir_path + "/logs/load_list.log")

host = argv[1]
username = argv[2]
password = argv[3]
database = argv[4]

if password == 'nopass':
    password = ''

import pymysql.cursors

connection = pymysql.connect(host=host, user=username, password=password, db=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, local_infile=True)

old_dirs = []

def firstDate(date):
    print('Creating history ' + date + ' ...')
    try:
        with connection.cursor() as cursor:
            sqlfile = "interprises_parsers/parsers/old_entity/FirstCreation.sql"
            for line in open(sqlfile, encoding='UTF-8'):
                if len(line) == 0:
                    continue
                query = line.replace('&&path&&', 'interprises_parsers/parsers/old_entity/files/' + date + '/legal_entity.csv', 1)
                query = query.replace('&&date&&', date, 1)
                cursor.execute(query)
                result = cursor.fetchone()
        connection.commit()
        print("History date "+date+" were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))
    finally:
        connection.close()

def dates(date):
    print('Creating history ' + date + ' ...')
    connection = pymysql.connect(host=host, user=username, password=password, db=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, local_infile=True)
    try:
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS dates;")
            result = cursor.fetchone()

            cursor.execute("CREATE TABLE IF NOT EXISTS dates(id int NOT NULL PRIMARY KEY AUTO_INCREMENT, date VARCHAR(30) DEFAULT NULL);")
            result = cursor.fetchone()

            cursor.execute("INSERT INTO dates (date) VALUES ('"+ date +"');")
            result = cursor.fetchone()

            if(
                    (time.strptime(date, "%d.%m.%y")) >
                    (time.strptime("01.04.18", "%d.%m.%y"))
            ):
                sqlfile = "interprises_parsers/parsers/old_entity/new_second_last.sql"
                for line in open(sqlfile, encoding='UTF-8'):
                    if len(line) == 0:
                        continue

                    query = line.replace('&&path&&', 'interprises_parsers/parsers/old_entity/files/' + date + '/legal_entity.csv', 1)
                    cursor.execute(query)
                    result = cursor.fetchone()

            else :
                sqlfile = "interprises_parsers/parsers/old_entity/second_last.sql"
                for line in open(sqlfile, encoding='UTF-8'):
                    if len(line) == 0:
                        continue

                    query = line.replace('&&path&&', 'interprises_parsers/parsers/old_entity/files/' + date + '/legal_entity.csv', 1)
                    cursor.execute(query)
                    result = cursor.fetchone()

        connection.commit()
        print("History date "+date+" were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))
    finally:
        connection.close()

def setChanges():
    for filename in os.listdir(dir_path + '/files'):
        old_dirs.append(filename)

    old_dirs.sort(key=lambda x: time.mktime(time.strptime(x, "%d.%m.%y")))
    # old_dirs.reverse()

    old_standard = [2, 9, 10]
    new_standard = [1, 14,15]

    old_fields = ['BIN', 'stat_id', 'name_ru', 'name_kk', 'register_date', 'economic_activity_code',
                  'economic_activity_codes', 'company_size_code', 'territory_code', 'address', 'CEO', 'active',
                  'resident']
    new_fields = ['BIN', 'name_ru', 'name_kk', 'register_date', 'economic_activity_code', 'activity_kk', 'activity_ru',
                  'economic_activity_codes', 'company_size_code', 'size_kk', 'size_ru', 'territory_code', 'locality_kk',
                  'locality_ru', 'address', 'CEO', 'active', 'resident']

    fieldnames = [
        'name_ru',
        'register_date'
        'address',
        'company_size_code',
        'economic_activity_codes',
        'economic_activity_code',
        'territory_code',
        'active',
        'resident',
        'CEO'
    ]

    csv_fields = [
        'BIN',
        'field_name',
        'old_value',
        'new_value',
        'date_of_change',
    ]

    firstDate(old_dirs[0])
    #
    # old_dirs.remove(old_dirs[0])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])
    # old_dirs.remove(old_dirs[1])

    for i in old_dirs:
        dates(i)
        # print(i)


    connection.close()

setChanges()