# google_sheet.py (patched for Test Write API)
import json, os
from google.oauth2 import service_account
from googleapiclient.discovery import build

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

def write_test_row(values: list):
    service = get_sheet_service()
    sheet = service.spreadsheets()

    sheet_id = os.getenv("TEST_SHEET_ID")
    if not sheet_id:
        raise Exception("TEST_SHEET_ID not found")

    body = {"values": [values]}

    result = sheet.values().append(
        spreadsheetId=sheet_id,
        range="RFQ TEST SHEET!A:Z",
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()

    return result
