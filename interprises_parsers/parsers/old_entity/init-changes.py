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

# host = argv[1]
# username = argv[2]
# password = argv[3]
# database = argv[4]
#
# if password == 'nopass':
#     password = ''
#
# import pymysql.cursors
#
# connection = pymysql.connect(host=host, user=username, password=password, db=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, local_infile=True)

old_dirs = []


def setChanges():
    for filename in os.listdir(dir_path + '/files/stat.gov.kz/old_entity'):
        old_dirs.append(filename)

    old_dirs.sort(key=lambda x: time.mktime(time.strptime(x, "%d.%m.%y")))
    old_dirs.reverse()

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
        'address',
        'CEO'
    ]

    csv_fields = [
        'BIN',
        'field_name',
        'old_value',
        'new_value',
        'date_of_change',
    ]

    with open(dir_path + '/history.csv', 'w', encoding='UTF-8') as csvfile_write:

        csv_writer = csv.DictWriter(csvfile_write, fieldnames=csv_fields, delimiter='\t', quotechar='"',
                                    escapechar='\\', quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        csv_writer.writerow({
            'BIN': 'BIN',
            'field_name': 'field_name',
            'old_value': 'old_value',
            'new_value': 'new_value',
            'date_of_change': 'date_of_change'
        })

        if (os.path.isfile(dir_path + '/files/stat.gov.kz/old_entity/' + old_dirs[0] + '/csv/legal_entity.csv')):
            with io.open(dir_path + '/files/stat.gov.kz/old_entity/' + old_dirs[0] + '/csv/legal_entity.csv',
                         encoding='utf-8') as parent_file:
                parent_reader = csv.reader(parent_file, delimiter='\t')
                for row_parent in parent_reader:
                    # print(row_parent)

                    if (len(row_parent) == 18):
                        parent_count_array = new_standard
                    else:
                        parent_count_array = old_standard

                    for j in range(len(parent_count_array)):
                        # print(row_parent[parent_count_array[i]])
                        for k in range(len(old_dirs)):
                            print('finding in path: ' + old_dirs[k])
                            if (os.path.isfile(dir_path + '/files/stat.gov.kz/old_entity/' + old_dirs[
                                k] + '/csv/legal_entity.csv')):
                                with io.open(dir_path + '/files/stat.gov.kz/old_entity/' + old_dirs[
                                    k] + '/csv/legal_entity.csv', encoding='utf-8') as child_file:
                                    child_reader = csv.reader(child_file, delimiter='\t')
                                    for row_child in child_reader:
                                        # print(row_child)
                                        if row_parent[0] == row_child[0]:
                                            if (len(row_child) == 18):
                                                clild_count_array = new_standard
                                                fields = new_fields
                                            else:
                                                clild_count_array = old_standard
                                                fields = old_fields
                                            print('============')
                                            print(old_dirs[k])

                                            print(row_parent[0])
                                            print(fields[clild_count_array[j]])
                                            print(row_parent[parent_count_array[j]])
                                            print(row_child[clild_count_array[j]])
                                            print('============')

                                            if (row_parent[parent_count_array[j]] != row_child[clild_count_array[j]]):
                                                print('---------------')
                                                print('CHANGE DETECTED')

                                                if (row_child[clild_count_array[j]] == '') or (
                                                        row_parent[parent_count_array[j]] == ''):
                                                    break

                                                with io.open(dir_path + '/history.csv', encoding='utf-8') as csvfile:
                                                    history = csv.reader(csvfile, delimiter='\t')

                                                    for row_history in history:
                                                        if (row_history[0] == row_parent[0]):
                                                            if (row_history[2] == row_child[clild_count_array[j]]):
                                                                break

                                                print('writing...')

                                                csv_writer.writerow({
                                                    'BIN': 'test1',
                                                    'field_name': 'test2',
                                                    'old_value': 'test3',
                                                    'new_value': 'test4',
                                                    'date_of_change': 'test5'
                                                })
                                                print('CHANGE WRITED')
                                                print('---------------')


setChanges()