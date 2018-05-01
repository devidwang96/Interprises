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
    if not os.path.exists('interprises_parsers/parsers/bad_entity/files/stat.gov.kz/'):
        os.makedirs('interprises_parsers/parsers/bad_entity/files/stat.gov.kz/')


    file_url = 'https://www.sk.kz/local/ajax/download.php?id=9095'
    print("start to download file %s" % file_url)

    temp_filename, headers = urllib.request.urlretrieve(file_url)

    filename = 'Файл ненад на 13_04_2017г.xls'
    local_filename = 'interprises_parsers/parsers/bad_entity/files/stat.gov.kz/' + filename
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

    bad_entity_folder = 'interprises_parsers/parsers/bad_entity/'

    for filename in os.listdir(bad_entity_folder + 'files/stat.gov.kz'):
        txt_name = bad_entity_folder + 'files/stat.gov.kz/' + filename.replace(".xlsx", ".txt").replace(".xls", ".txt")
        if not os.path.isfile(txt_name):
            from_excel_to_txt(bad_entity_folder + 'files/stat.gov.kz/' + filename)
            print(filename + " was converted to txt")
            logging.debug(filename + " was converted to txt")


    bad_ids = []
    with open('interprises_parsers/parsers/bad_entity/files/bad_entity.csv', 'w', encoding='UTF-8') as csvfile:
        fieldnames = [
            'number',
            'name',
            'confession',
            'address',
            'bad_fact_date',
            'head_of',
            'bin',
            'bad_start_state',
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t', quotechar='"', escapechar='\\',
                                quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for filename in os.listdir(bad_entity_folder + 'files/stat.gov.kz/'):
            if ".txt" not in filename[-4:]:
                continue
            k = 0

            with io.open(bad_entity_folder + 'files/stat.gov.kz/' + filename, 'r', encoding='UTF-8') as f:
                for line in f:
                    v = line.split('\t')
                    values = []
                    for p in v:
                        values.append(prepare_string(p))

                    if (len(values) >= 8):

                        number = values[0]
                        if len(number) == 0:
                            number = None

                        name = values[1]
                        if len(name) == 0:
                            name = None

                        confession = values[2]
                        if len(confession) == 0:
                            confession = None

                        address = values[3]
                        if len(address) == 0:
                            address = None

                        bad_fact_date = values[4]
                        if len(bad_fact_date) == 0:
                            bad_fact_date = None

                        head_of = values[5]
                        if len(head_of) == 0:
                            head_of = None

                        bin = values[6]
                        if len(bin) == 0:
                            bin = None

                        bad_start_state = values[7]
                        if len(bad_start_state) == 0:
                            bad_start_state = None

                        bad_ids.append((number))
                        writer.writerow({
                            'number': number,
                            'name': name,
                            'confession': confession,
                            'address': address,
                            'bad_fact_date': bad_fact_date,
                            'head_of': head_of,
                            'bin': bin,
                            'bad_start_state': bad_start_state,
                        })
                        k = k + 1

    copyfile(bad_entity_folder + 'files/' + "bad_entity.csv", "interprises_parsers/tmp/bad_entity.csv")
    logging.info('files/' + "bad_entity.csv" + " was copied to interprises_parsers/tmp/ folder")
    print('files/' + "bad_entity.csv" + " was copied to interprises_parsers/tmp/ folder")

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
        print("bad entites were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))
    finally:
        connection.close()


download_file()
convertFile()
import_to_db()
