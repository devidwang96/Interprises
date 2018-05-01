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
from pyunpack import Archive
import io
import csv
import logging
from sys import argv

# from parsers import settings
dir_path = os.path.dirname(os.path.realpath(__file__))

# create logger

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

if not os.path.exists('interprises_parsers/parsers/jur_exist_entity/files/csv'):
    os.makedirs('interprises_parsers/parsers/jur_exist_entity/files/csv')

def prepare_string(col):
    if col is None:
        return ''
    return col.replace('\\', "\\\\").strip().strip('\n\r').replace('\n', '').replace('\r', '')


def from_excel_to_txt(filename):
    if ".xls" not in filename[-5:]:
        return 0
    wb = open_workbook(filename)
    f = io.open(filename.replace(".xlsx", ".txt"), 'w', encoding='utf8')
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


def getJur_exist_entity():
    for filename in os.listdir('interprises_parsers/parsers/jur_exist_entity/files'):
        if ".xls" in filename[-5:]:
            txt_name = 'interprises_parsers/parsers/jur_exist_entity/files' + filename.replace(".xlsx", ".txt").replace(".xls", ".txt")
            if not os.path.isfile(txt_name):
                from_excel_to_txt('interprises_parsers/parsers/jur_exist_entity/files/' + filename)
                logging.debug(filename + " was converted to txt")


    with open('interprises_parsers/parsers/jur_exist_entity/files/csv/' + "jur_exist_entity.csv", 'w', encoding='UTF-8') as csvfile:
        fieldnames = [
            'BIN',
            'name',
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t', quotechar='"', escapechar='\\',
                                quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for filename in os.listdir('interprises_parsers/parsers/jur_exist_entity/files'):
            if ".txt" not in filename[-4:]:
                continue

            with io.open('interprises_parsers/parsers/jur_exist_entity/files/' + filename, 'r', encoding='UTF-8') as f:
                for line in f:
                    v = line.split('\t')
                    values = []
                    for p in v:
                        values.append(prepare_string(p))
                    if(len(values) == 1):
                        continue

                    BIN = values[1]
                    name = values[3]

                    writer.writerow({
                        'BIN' : BIN,
                        'name' : name
                    })

    copyfile('interprises_parsers/parsers/jur_exist_entity/files/csv/jur_exist_entity.csv', "interprises_parsers/tmp/jur_exist.csv")
    print('interprises_parsers/parsers/jur_exist_entity/files/csv/jur_exist_entity.csv' + " was copied to interprises_parsers/tmp/ folder")

def jur_exist_entity_to_db():
    try:
        with connection.cursor() as cursor:
            sqlfile = dir_path + "/jur_exist.sql"
            for line in open(sqlfile, encoding='UTF-8'):
                if len(line) == 0:
                    continue
                cursor.execute(line)
                result = cursor.fetchone()
        connection.commit()
        print("jur_exist_entity were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))
    finally:
        connection.close()



getJur_exist_entity()
jur_exist_entity_to_db()