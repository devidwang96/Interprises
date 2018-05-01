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

host = "localhost"
username = "root"
password = ""
database = "alldata2"

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


def prepare_string(col):
    if col is None:
        return ''
    return col.replace('\\', "\\\\").strip().strip('\n\r').replace('\n', '').replace('\r', '')


def from_excel_to_txt(filename):
    if ".xls" not in filename[-5:]:
        return 0
    wb = open_workbook(filename)
    f = io.open(filename.replace(".xls", ".txt"), 'w', encoding='utf8')
    for s in wb.sheets():
        ok = False
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                value = s.cell(row, col).value
                if type(value) is int or type(value) is float:
                    values.append(str(value))
                else:
                    value = value.strip().strip('\n\r\t').replace('\t', '').replace('\n', '').replace('\r', '')
                    values.append(value)
            if ok and len(values[0]) > 0:
                f.write('\t'.join(values) + '\n\r')
            if row == 3:
                ok = True
    f.close()


def download_files():
    # проверяем все ли необходимые папки существуют
    previous = "old19.06.17"
    previous_folder = previous + "/"

def import_to_db_date():
    try:
        with connection.cursor() as cursor:
            sqlfile = dir_path + "/date.sql"

            for line in open(sqlfile, encoding='UTF-8'):
                if len(line) == 0:
                    continue
                cursor.execute(line)
                result = cursor.fetchone()
        connection.commit()
        print("dates were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))

def import_to_db():
    try:
        with connection.cursor() as cursor:
            sqlfile = dir_path + "/second_last.sql"

            for line in open(sqlfile, encoding='UTF-8'):
                if len(line) == 0:
                    continue
                cursor.execute(line)
                result = cursor.fetchone()
        connection.commit()
        print("old entites were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))
    finally:
        connection.close()


download_files()
import_to_db_date()
import_to_db()
