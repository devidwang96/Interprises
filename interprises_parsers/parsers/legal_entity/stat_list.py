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
    today = date.today().strftime("%d.%m.%y")
    today_folder = "interprises_parsers/parsers/legal_entity/files/stat.gov.kz/legal_entity/" + today + "/"
    if not os.path.exists(today_folder):
        os.makedirs(today_folder)

    if not os.path.exists('interprises_parsers/tmp'):
        os.makedirs('interprises_parsers/tmp')

    today_zip_folder = today_folder + "zip/"
    if not os.path.exists(today_zip_folder):
        os.makedirs(today_zip_folder)

    today_unzip_folder = today_folder + "unzip/"
    if not os.path.exists(today_unzip_folder):
        os.makedirs(today_unzip_folder)

    today_csv_folder = today_folder + "csv/"
    if not os.path.exists(today_csv_folder):
        os.makedirs(today_csv_folder)

    if not os.path.isfile(today_csv_folder + "legal_entity.csv"):
        i = 17
        while i <= 34:
            file_url = 'http://stat.gov.kz/getImg?id=ESTAT0861' + str(i)
            logging.debug("start to download file %s" % file_url)
            # скачиваем файл и копируем в необходимую папку
            temp_filename, headers = urllib.request.urlretrieve(file_url)
            ff = re.findall("filename=(\S+)", headers['Content-Disposition'])
            if len(ff) > 0:
                filename = ff[0].replace('"', '').replace("''", "");
            local_filename = today_zip_folder + filename
            #			'stat_id',
            filename, file_extension = os.path.splitext(local_filename)
            logging.info("%s was downloaded" % filename)
            if file_extension in ['.zip', '.xls', '.xlsx']:
                if not os.path.isfile(local_filename):
                    copyfile(temp_filename, local_filename)
                    logging.debug("copy file %s" % local_filename)
                else:
                    logging.debug("%s file from %s is already here" % (local_filename, file_url))
            else:
                logging.warning("%s file from %s unexpected extension" % (local_filename, file_url))
            i = i + 1

        # разархивируем zip архивы
        for filename in os.listdir(today_zip_folder):
            if ".zip" in filename[-4:]:
                with zipfile.ZipFile(today_zip_folder + filename, "r") as z:
                    z.extractall(today_unzip_folder)
                    logging.debug(filename + " was unzipped")

        # конвертируем xls в txt
        for filename in os.listdir(today_unzip_folder):
            if ".xls" in filename[-5:]:
                txt_name = today_unzip_folder + filename.replace(".xlsx", ".txt").replace(".xls", ".txt")
                if not os.path.isfile(txt_name):
                    from_excel_to_txt(today_unzip_folder + filename)
                    logging.debug(filename + " was converted to txt")

    company_ids = []
    with open(today_csv_folder + "legal_entity.csv", 'w', encoding='UTF-8') as csvfile:
        fieldnames = [
            'BIN',
            'name_ru',
            'name_kk',
            'register_date',
            'economic_activity_code',

            'activity_kk',
            'activity_ru',

            'economic_activity_codes',
            'company_size_code',


            'size_kk',
            'size_ru',


            'territory_code',


            'locality_kk',
            'locality_ru',



            'address',
            'CEO',
            'active',
            'resident'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t', quotechar='"', escapechar='\\',
                                quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for filename in os.listdir(today_unzip_folder):
            if ".txt" not in filename[-4:]:
                continue
            k = 0
            with io.open(today_unzip_folder + filename, 'r', encoding='UTF-8') as f:
                for line in f:
                    v = line.split('\t')
                    values = []
                    for p in v:
                        values.append(prepare_string(p))

                    BIN = values[0][:12]
                    values[0] = BIN
                    if len(BIN) == 0:
                        continue

                    #					stat_id = values[1]

                    name_kk = values[1].replace("\"", "'")
                    if len(name_kk) == 0:
                        name_kk = None

                    name_ru = values[2].replace("\"", "'")
                    if len(name_ru) == 0:
                        name_ru = None

                    try:
                        register_date = datetime.strptime(values[3], '%d.%m.%Y')
                    except ValueError:
                        y = int(BIN[:2])
                        if y < 50:
                            register_str = "01.%s.20%s" % (BIN[2:4].zfill(2), BIN[:2].zfill(2))
                        else:
                            register_str = "01.%s.19%s" % (BIN[2:4].zfill(2), BIN[:2].zfill(2))
                        register_date = datetime.strptime(register_str, '%d.%m.%Y')

                    economic_activity_code = values[4]
                    if len(economic_activity_code) == 0:
                        economic_activity_code = None




                    activity_kk = values[5]
                    if len(activity_kk) == 0:
                        activity_kk = None

                    activity_ru = values[6]
                    if len(activity_ru) == 0:
                        activity_ru = None




                    economic_activity_codes = values[7]
                    if len(economic_activity_codes) == 0:
                        economic_activity_codes = None

                    company_size_code = values[8]
                    if len(company_size_code) == 0:
                        company_size_code = None



                    size_kk = values[9]
                    if len(size_kk) == 0:
                        size_kk = None

                    size_ru = values[10]
                    if len(size_ru) == 0:
                        size_ru = None



                    territory_code = values[11]
                    if len(territory_code) == 0:
                        territory_code = None





                    locality_kk = values[12]
                    if len(locality_kk) == 0:
                        locality_kk = None

                    locality_ru = values[13]
                    if len(locality_ru) == 0:
                        locality_ru = None




                    address = values[14]
                    if len(address) == 0:
                        address = None

                    CEO = values[15]
                    if len(CEO) == 0:
                        CEO = None

                    company_ids.append((BIN))
                    writer.writerow({
                        'BIN': BIN,
                        'name_ru': name_ru,
                        'name_kk': name_kk,
                        'register_date': register_date,
                        'economic_activity_code': economic_activity_code,

                        'activity_kk': activity_kk,
                        'activity_ru': activity_ru,

                        'economic_activity_codes': economic_activity_codes,
                        'company_size_code': company_size_code,

                        'size_kk': size_kk,
                        'size_ru': size_ru,

                        'territory_code': territory_code,

                        'locality_kk': locality_kk,
                        'locality_ru': locality_ru,


                        'address': address,
                        'CEO': CEO,
                        'active': 1,
                        'resident': 1 if BIN[4] == '4' else 0})
                    k = k + 1



    copyfile(today_csv_folder + "legal_entity.csv", "interprises_parsers/tmp/legal_entity.csv")
    print(today_csv_folder + "legal_entity.csv" + " was copied to interprises_parsers/tmp/ folder")

    if not os.path.exists('interprises_parsers/parsers/old_entity/files/' + today):
        os.makedirs('interprises_parsers/parsers/old_entity/files/' + today)

    copyfile(today_csv_folder + "legal_entity.csv", "interprises_parsers/parsers/old_entity/files/" + today + '/legal_entity.csv')
    print(today_csv_folder + "legal_entity.csv" + "was copied to interprises_parsers/parsers/old_entity/files/" + today + '/' + "folder")

    branches = find_branches(company_ids)
    with open(today_csv_folder + "legal_branche.csv", 'w', encoding='UTF-8') as csvfile:
        fieldnames = [
            'BIN',
            'head_BIN'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t', quotechar='"', escapechar='\\',
                                quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        writer.writeheader()
        for BIN, head_BIN in branches:
            writer.writerow({
                'BIN': BIN,
                'head_BIN': head_BIN})

    copyfile(today_csv_folder + "legal_branche.csv", "interprises_parsers/tmp/legal_branche.csv")
    logging.info(today_csv_folder + "legal_branche.csv" + " was copied to interprises_parsers/tmp/ folder")


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
        print("legal entites were imported to db")
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

download_files()
import_to_db()
