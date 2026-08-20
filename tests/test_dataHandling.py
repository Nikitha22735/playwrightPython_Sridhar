import csv
import json

from openpyxl import load_workbook
import pytest


def test_jsonHandling():
    with open("testdata/creds.json") as data:
        formattedData = json.load(data)
        print(formattedData["password"])


def test_csvHandling():
     with open("testdata\\credentails.csv") as data:
            formattedData = csv.DictReader(data)
            values=[]
            for i in formattedData:
                 values.append(i)

            print(values[1]["username"])

# pip install openpyxl
@pytest.mark.dh
def test_excel():
     workbook = load_workbook("testdata\\sample_creds.xlsx")
     sheet = workbook["Sheet2"]
     values=[]
     for i in sheet.iter_rows(min_row=2, values_only=True):
          values.append(i)
     print(values)


