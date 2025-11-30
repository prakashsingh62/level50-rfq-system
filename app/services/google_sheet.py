import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build


def get_sheet_service():
    sa_json = os.getenv("SERVICE_ACCOUNT_JSON")
    if not sa_json:
        raise Exception("SERVICE_ACCOUNT_JSON is missing in Railway variables")

    info = json.loads(sa_json)

    creds = service_account.Credentials.from_service_account_info(
        info,
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )

    return build("sheets", "v4", credentials=creds)


def read_test_sheet():
    service = get_sheet_service()
    sheet = service.spreadsheets()

    sheet_id = os.getenv("TEST_SHEET_ID")
    if not sheet_id:
        raise Exception("TEST_SHEET_ID not found in Railway variables")

    result = sheet.values().get(
        spreadsheetId=sheet_id,
        range="RFQ TEST SHEET!A:Z"
    ).execute()

    return result.get("values", [])
