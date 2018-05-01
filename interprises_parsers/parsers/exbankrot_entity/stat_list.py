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


def download_file():
    if not os.path.exists('interprises_parsers/parsers/exbankrot_entity/files/stat.gov.kz/'):
        os.makedirs('interprises_parsers/parsers/exbankrot_entity/files/stat.gov.kz/')


    file_url = 'http://kgd.gov.kz/sites/default/files/Reabilibankrotstvo/Spicok/spisok_bankrotov_v_otnoshenii_kotoryh_procedura_bankrotstva_zavershena_v_2015_godu.xlsx'
    print("start to download file %s" % file_url)

    temp_filename, headers = urllib.request.urlretrieve(file_url)

    filename = 'spisok_bankrotov_v_otnoshenii_kotoryh_procedura_bankrotstva_zavershena_v_2015_godu.xlsx'
    local_filename = 'interprises_parsers/parsers/exbankrot_entity/files/stat.gov.kz/' + filename
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

    exbankrot_entity_folder = 'interprises_parsers/parsers/exbankrot_entity/'

    for filename in os.listdir(exbankrot_entity_folder + 'files/stat.gov.kz'):
        txt_name = exbankrot_entity_folder + 'files/stat.gov.kz/' + filename.replace(".xlsx", ".txt").replace(".xls", ".txt")
        if not os.path.isfile(txt_name):
            from_excel_to_txt(exbankrot_entity_folder + 'files/stat.gov.kz/' + filename)
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
        for filename in os.listdir(exbankrot_entity_folder + 'files/stat.gov.kz/'):
            if ".txt" not in filename[-4:]:
                continue
            k = 0

            with io.open(exbankrot_entity_folder + 'files/stat.gov.kz/' + filename, 'r', encoding='UTF-8') as f:
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


download_file()
convertFile()
import_to_db()
