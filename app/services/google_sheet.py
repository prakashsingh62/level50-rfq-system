# google_sheet.py (FINAL – TEST WRITE READY)

import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Import new write engine
from app.services.write_engine_test import write_row_to_test_sheet


# -------------------------------------------------------------------
# 1) Create Google Sheets service
# -------------------------------------------------------------------
def get_sheet_service():
    sa_json = os.getenv("SERVICE_ACCOUNT_JSON")
    if not sa_json:
        raise Exception("SERVICE_ACCOUNT_JSON is missing")

    info = json.loads(sa_json)

    creds = service_account.Credentials.from_service_account_info(
        info,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    return build("sheets", "v4", credentials=creds)


# -------------------------------------------------------------------
# 2) Read Test Sheet (GET)
# -------------------------------------------------------------------
def read_test_sheet():
    service = get_sheet_service()
    sheet = service.spreadsheets()

    sheet_id = os.getenv("TEST_SHEET_ID")
    if not sheet_id:
        raise Exception("TEST_SHEET_ID not found")

    result = sheet.values().get(
        spreadsheetId=sheet_id,
        range="RFQ TEST SHEET!A:Z"
    ).execute()

    return result


# -------------------------------------------------------------------
# 3) Write Test Row (POST)
# -------------------------------------------------------------------
def write_test_row(values: list):
    """
    Redirects writing to the new write engine.
    """
    return write_row_to_test_sheet(values)

