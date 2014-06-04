import csv
#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="udevel"
__date__ ="$22 mai 2014 16:03:10$"

# Set the Django env
from django.core.management import setup_environ
from boombike import settings
setup_environ(settings)

# Imports
import os
import sys
import traceback
from csv import reader

from info.models import City, FRANCE_COUNTRY_NAME, SPAIN_COUNTRY_NAME, PORTUGAL_COUNTRY_NAME

CITIES_FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
FRENCH_CITIES_FILE_PATH = os.path.join(CITIES_FILE_PATH, 'villes_france.csv')
SPANISH_CITIES_FILE_PATH = os.path.join(CITIES_FILE_PATH, 'municipios-calles.txt')
PORTUGUESE_CITIES_FILE_PATH = os.path.join(CITIES_FILE_PATH, 'todos_cp.txt')

def load_french_cities():
    with open(FRENCH_CITIES_FILE_PATH, 'r') as cities_file:
        csv_reader = reader(cities_file, delimiter=',', quoting=csv.QUOTE_ALL)

        for row in csv_reader:
            try:
                zip_code = row[7].split('-')[0]
                city = City(name=unicode(row[4], 'utf-8'),
                            zip_code=zip_code,
                            country=FRANCE_COUNTRY_NAME)
                city.save()
            except:
                traceback.print_exc()
                sys.stderr.write(unicode(row[4], 'utf-8') + u' could not be saved\n')


def load_spanish_cities():
    with open(SPANISH_CITIES_FILE_PATH, 'r') as cities_file:
        csv_reader = reader(cities_file, delimiter=';', quoting=csv.QUOTE_NONE)

        for row in csv_reader:
            try:
                if row[2] == "false":
                    zip_code = row[3]
                    city = City(name=unicode(row[4], 'utf-8'),
                                zip_code=zip_code,
                                country=SPAIN_COUNTRY_NAME)
                    city.save()
            except:
                traceback.print_exc()
                sys.stderr.write(unicode(row[4], 'utf-8') + u' could not be saved\n')


def load_portugues_ciies():
    with open(PORTUGUESE_CITIES_FILE_PATH, 'r') as cities_file:
        csv_reader = reader(cities_file, delimiter=';', quoting=csv.QUOTE_NONE)

        for row in csv_reader:
            try:
                zip_code = row[14]

                print zip_code,  unicode(row[16], 'utf-8')

                city = City(name=unicode(row[16], 'utf-8'),
                            zip_code=zip_code,
                            country=PORTUGAL_COUNTRY_NAME)
                city.save()
            except:
#                traceback.print_exc()
                sys.stderr.write(unicode(row[4], 'utf-8') + u' could not be saved\n')


if __name__ == "__main__":
#    load_french_cities()
#    load_spanish_cities()
    load_portugues_ciies()
