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

def setChanges():
    for filename in os.listdir(dir_path + '/files/stat.gov.kz/old_entity'):
        print(filename)


setChanges()