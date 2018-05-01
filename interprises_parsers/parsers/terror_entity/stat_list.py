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
#
host = argv[1]
username = argv[2]
password = argv[3]
database = argv[4]

if password == 'nopass':
    password = ''

import pymysql.cursors

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


def download_file():
    if not os.path.exists('interprises_parsers/parsers/terror_entity/files/stat.gov.kz/'):
        os.makedirs('interprises_parsers/parsers/terror_entity/files/stat.gov.kz/')


    file_url = 'http://kfm.gov.kz/blacklist/export/active/xls'
    print("start to download file %s" % file_url)

    temp_filename, headers = urllib.request.urlretrieve(file_url)

    filename = 'list-active20180425.xls'
    local_filename = 'interprises_parsers/parsers/terror_entity/files/stat.gov.kz/' + filename
    filename, file_extension = os.path.splitext(local_filename)


    if file_extension in ['.zip', '.xls', '.xlsx']:
        if not os.path.isfile(local_filename):
            copyfile(temp_filename, local_filename)
            print("copy file %s" % local_filename)
        else:
            print("%s file from %s is already here" % (local_filename, file_url))
            os.remove(local_filename)
            copyfile(temp_filename, local_filename)
            print("copy file %s" % local_filename)
    else:
        print("%s file from %s unexpected extension" % (local_filename, file_url))


def convertFile():

    terror_entity_folder = 'interprises_parsers/parsers/terror_entity/'

    for filename in os.listdir(terror_entity_folder + 'files/stat.gov.kz'):
        txt_name = terror_entity_folder + 'files/stat.gov.kz/' + filename.replace(".xlsx", ".txt").replace(".xls", ".txt")

        if not os.path.isfile(txt_name):
            from_excel_to_txt(terror_entity_folder + 'files/stat.gov.kz/' + filename)

            print(filename + " was converted to txt")
            logging.debug(filename + " was converted to txt")


    terror_ids = []
    with open('interprises_parsers/parsers/terror_entity/files/terror_entity.csv', 'w', encoding='UTF-8') as csvfile:
        fieldnames = [
            'number',
            'name',
            'birthday',
            'iin',
            'notes',
            'notes_fix',
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t', quotechar='"', escapechar='\\',
                                quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for filename in os.listdir(terror_entity_folder + 'files/stat.gov.kz/'):
            if ".txt" not in filename[-4:]:
                continue
            k = 0

            with io.open(terror_entity_folder + 'files/stat.gov.kz/' + filename, 'r', encoding='UTF-8') as f:
                for line in f:
                    v = line.split('\t')
                    values = []
                    for p in v:
                        values.append(prepare_string(p))

                    if(len(values) >= 8):

                        number = values[0]
                        if len(number) == 0:
                            number = None

                        name = values[1] + " " + values[2] + " " + values[3]
                        if len(name) == 0:
                            name = None

                        birthday = values[4]
                        if len(birthday) == 0:
                            birthday = None

                        iin = values[5]
                        if len(iin) == 0:
                            iin = None

                        notes = values[6]
                        if len(notes) == 0:
                            notes = None

                        notes_fix = values[7]
                        if len(notes_fix) == 0:
                            notes_fix = None

                        terror_ids.append((number))
                        writer.writerow({
                            'number': number,
                            'name': name,
                            'birthday': birthday,
                            'iin': iin,
                            'notes': notes,
                            'notes_fix': notes_fix
                        })
                        k = k + 1



    copyfile(terror_entity_folder + 'files/' + "terror_entity.csv", "interprises_parsers/tmp/terror_entity.csv")
    logging.info('files/' + "terror_entity.csv" + " was copied to interprises_parsers/tmp/ folder")
    print('files/' + "terror_entity.csv" + " was copied to interprises_parsers/tmp/ folder")

def import_to_db():
    try:
        with connection.cursor() as cursor:
            sqlfile = dir_path + "/import.sql"

            for line in open(sqlfile, encoding='UTF-8'):
                if len(line) == 0:
                    continue
                cursor.execute(line)
                result = cursor.fetchone()
        connection.commit()
        print("terror entites were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))
    finally:
        connection.close()


download_file()
convertFile()
import_to_db()
