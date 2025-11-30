from google.oauth2 import service_account
from googleapiclient.discovery import build

def read_test_sheet():
    creds = service_account.Credentials.from_service_account_file(
        "config/service_account.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    sheet_id = "PASTE_TEST_SHEET_ID_HERE"
    range_name = "RFQ TEST SHEET!A1:Z200"

    service = build("sheets", "v4", credentials=creds)
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=range_name
    ).execute()

    values = result.get("values", [])
    return values
