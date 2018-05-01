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

# from parsers import settings
dir_path = os.path.dirname(os.path.realpath(__file__))

# create logger
logging.basicConfig(format='%(levelname)s \t %(asctime)s \t %(module)s \t %(message)s', level=logging.INFO,
                    filename=dir_path + "/logs/load_list.log")

host = argv[1]
username = argv[2]
password = argv[3]
database = argv[4]

if password == 'nopass':
    password = ''

import pymysql.cursors

# Connect to the database

connection = pymysql.connect(host=host,
                             user=username,
                             password=password,
                             db=database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             local_infile=True)

dirs = []

def findFilials():
    for filename in os.listdir(dir_path + '/files/stat.gov.kz/legal_entity'):
        dirs.append(filename)

    dirs.sort(key=lambda x: time.mktime(time.strptime(x, "%d.%m.%y")))
    dirs.reverse()
    current_dir = dirs[0]
    # print(current_dir)

    csv_fields = [
        'BIN',
        'name'
    ]

    with open(dir_path + '/files/stat.gov.kz/legal_entity/'+ current_dir +'/csv/filials.csv', 'w', encoding='UTF-8') as csvfile_write:
        csv_writer = csv.DictWriter(csvfile_write, fieldnames=csv_fields,delimiter='\t', quotechar='"', escapechar='\\',quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        with io.open(dir_path + '/files/stat.gov.kz/legal_entity/' + current_dir + '/csv/legal_entity.csv', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                BIN = row[0]
                name = row[1]
                if(len(BIN) > 11):
                    if(BIN[5] == '1'):
                        csv_writer.writerow({
                            'BIN': BIN,
                            'name': name,
                        })

    copyfile(dir_path + '/files/stat.gov.kz/legal_entity/'+ current_dir +'/csv/filials.csv', "interprises_parsers/tmp/filials.csv")
    logging.info(dir_path + '/files/stat.gov.kz/legal_entity/'+ current_dir +'/csv/filials.csv' + " was copied to interprises_parsers/tmp/ folder")

def import_filials_to_db():
    try:
        with connection.cursor() as cursor:
            sqlfile = dir_path + "/filials.sql"

            for line in open(sqlfile, encoding='UTF-8'):
                if len(line) == 0:
                    continue
                cursor.execute(line)
                result = cursor.fetchone()
        connection.commit()
        print("filials were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))
    finally:
        connection.close()

findFilials()
import_filials_to_db()

