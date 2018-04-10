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


def convertFile():

    exbankrot_entity_folder = 'interprises_parsers/parsers/exbankrot_entity/'

    for filename in os.listdir(exbankrot_entity_folder + 'files'):
        txt_name = exbankrot_entity_folder + 'files/' + filename.replace(".xlsx", ".txt").replace(".xls", ".txt")
        if not os.path.isfile(txt_name):
            from_excel_to_txt(exbankrot_entity_folder + 'files/' + filename)
            print(filename + " was converted to txt")
            logging.debug(filename + " was converted to txt")



    exbankrot_ids = []
    with open('interprises_parsers/parsers/exbankrot_entity/files/exbankrot_entity.csv', 'w', encoding='UTF-8') as csvfile:
        fieldnames = [
            'number',
            'region',
            'name',
            'bin_iin',
            'rnn',
            'address',
            'ceo_fio',
            'ceo_iin',
            'founder_fio',
            'founder_bin',
            'activity',
            'bankrot_start_date',
            'bankrot_end_date',
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t', quotechar='"', escapechar='\\',
                                quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for filename in os.listdir(exbankrot_entity_folder + 'files'):
            if ".txt" not in filename[-4:]:
                continue
            k = 0

            with io.open(exbankrot_entity_folder + 'files/' + filename, 'r', encoding='UTF-8') as f:
                for line in f:
                    v = line.split('\t')
                    values = []
                    for p in v:
                        values.append(prepare_string(p))

                    if(len(values) >= 13):

                        number = values[0]
                        if len(number) == 0:
                            number = None

                        region = values[1]
                        if len(region) == 0:
                            region = None

                        name = values[2]
                        if len(name) == 0:
                            name = None

                        bin_iin = values[3]
                        if len(bin_iin) == 0:
                            bin_iin = None

                        rnn = values[4]
                        if len(rnn) == 0:
                            rnn = None

                        address = values[5]
                        if len(address) == 0:
                            address = None

                        ceo_fio = values[6]
                        if len(ceo_fio) == 0:
                            ceo_fio = None

                        ceo_iin = values[7]
                        if len(ceo_iin) == 0:
                            ceo_iin = None

                        founder_fio = values[8]
                        if len(founder_fio) == 0:
                            founder_fio = None

                        founder_bin = values[9]
                        if len(founder_bin) == 0:
                            founder_bin = None

                        activity = values[10]
                        if len(activity) == 0:
                            activity = None

                        bankrot_start_date = values[11]
                        if len(bankrot_start_date) == 0:
                            bankrot_start_date = None

                        bankrot_end_date = values[12]
                        if len(bankrot_end_date) == 0:
                            bankrot_end_date = None

                        exbankrot_ids.append((number))
                        writer.writerow({
                            'number': number,
                            'region': region,
                            'name': name,
                            'bin_iin': bin_iin,
                            'rnn': rnn,
                            'address': address,
                            'ceo_fio': ceo_fio,
                            'ceo_iin': ceo_iin,
                            'founder_fio': founder_fio,
                            'founder_bin': founder_bin,
                            'activity': activity,
                            'bankrot_start_date': bankrot_start_date,
                            'bankrot_end_date': bankrot_end_date
                        })
                        k = k + 1



    copyfile(exbankrot_entity_folder + 'files/' + "exbankrot_entity.csv", "interprises_parsers/tmp/exbankrot_entity.csv")
    logging.info('files/' + "exbankrot_entity.csv" + " was copied to interprises_parsers/tmp/ folder")
    print('files/' + "exbankrot_entity.csv" + " was copied to interprises_parsers/tmp/ folder")

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
        print("exbankrot entites were imported to db")
    except Exception as e:
        print("import to db error: %s" % str(e))
    finally:
        connection.close()


def find_branches(company_ids):
    from operator import itemgetter, attrgetter, methodcaller
    ll = sorted(company_ids, key=lambda x: x[0])
    i = 0
    #	head_stat_id = None
    branches = []

    for BIN in ll:
        head_BIN = BIN
        if BIN[5] == '1':
            branches.append([BIN, head_BIN])
        i = i + 1
    return branches

convertFile()
import_to_db()
