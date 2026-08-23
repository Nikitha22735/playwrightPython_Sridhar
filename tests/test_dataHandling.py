import json
import os

from dotenv import load_dotenv
import pytest
from utils.datahandling import clearExcelData, csvData, excelData


def test_jsonHandling():
    with open("testdata/creds.json") as data:
        formattedData = json.load(data)
        print(formattedData["password"])


def test_csvHandling():
     values = csvData("testdata\\credentails.csv")
     print(values[1]["username"])

# pip install openpyxl
# @pytest.mark.dh
def test_excel():
     values = excelData("testdata\\sample_creds.xlsx", "Sheet2")
     print(values)


def test_excel_write():
     clearExcelData("testdata\\sample_creds.xlsx", "sheet1")

# @pytest.mark.dh
def test_cli():
     print(os.getenv('usname_s'))
     print(os.getenv('pw_s'))


# pip install python-dotenv
@pytest.mark.dh
def test_cli():
     load_dotenv(os.getenv("file"))
     print(os.getenv('urls_env'))
     print(os.getenv('us_env'))
     print(os.getenv('pw_env'))
     


