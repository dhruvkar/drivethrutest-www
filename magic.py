# -------------------
# STANDARD LIB IMPORTS
# -------------------
import os


# --------------------
# THIRD PARTY IMPORTS
# -------------------
import gspread
from gspread import CellNotFound
from oauth2client.service_account import ServiceAccountCredentials


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
LAYOUTS_DIR = os.path.join(BASE_DIR, "layouts")
STATIC_DIR = os.path.join(BASE_DIR, "static")
GOOGLE_CREDS_FILE = os.path.join(BASE_DIR, "google.json")
GOOGLE_SHEET_KEY = "1_gf7CZ2F-KXURPqpjo6c0wNJl6LcBfyI7CgbVjIUpPM"



class GoogleSheet(object):

    def __init__(self, key=GOOGLE_SHEET_KEY, creds_file=GOOGLE_CREDS_FILE, wks_name="raw"):
        self.key = key
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_file, self.scope)
        gc = gspread.authorize(self.credentials)
        sheet = gc.open_by_key(self.key)
        self.wks = sheet.worksheet(wks_name)





