#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 12:46:00 2018

Introduction
input pdf's url and locate absolute path,
program will download it auto

@author: fangyucheng
yxf321@miami.edu
"""

import argparse
import urllib

parser = argparse.ArgumentParser()

parser.add_argument('-u', '--url', default=[], action='append',
                    help=('input url to download'))
parser.add_argument('-fp', '--file_path', default='', type=str,
                    help=('path of the pdfs'))
args = parser.parse_args()

URL_LIST = args.url
FILE_PATH = args.file_path

if FILE_PATH == '':
    FILE_PATH = None

def download(url, file_path):
    file_name = url.split('/')[-1]
    if file_path is not None:
        file_name = file_path + '/' + file_name
    opener = urllib.request.build_opener()
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, file_name)
    print('download %s successfully' % file_name)


for url in URL_LIST:
    download(url, file_path=FILE_PATH)    
