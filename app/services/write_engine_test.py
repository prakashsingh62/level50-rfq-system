import os
from datetime import datetime, timedelta
from app.services.google_sheet import get_sheet_service

# Columns that Level-50 must NEVER overwrite
PROTECTED_COLUMNS = {
    "A",  # SALES PERSON
    "B",  # CUSTOMER NAME
    "C",  # LOCATION
    "D",  # RFQ NO
    "E",  # RFQ DATE
    "F",  # PRODUCT
    "G",  # UID NO
    "H",  # UID DATE
    "I",  # DUE DATE
    "J",  # VENDOR
    "K",  # CONCERN PERSON
}

def process_test_sheet():
    service = get_sheet_service()
    sheet_id = os.getenv("TEST_SHEET_ID")

    # Load sheet
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range="RFQ TEST SHEET!A:Z"
    ).execute()

    rows = result.get("values", [])

    # If sheet empty
    if not rows:
        return {"updated": False, "message": "Sheet empty"}

    header = rows[0]
    updated_rows = []
    now = datetime.now()

    # Process each row (Level-50 logic simplified for test mode)
    for index, row in enumerate(rows[1:], start=2):
        updated_row = row.copy()

        # Example: Vendor Pending Aging
        try:
            vendor_status = row[12].strip().upper() if len(row) > 12 else ""
            days_pending = row[13] if len(row) > 13 else ""

            if vendor_status == "PENDING":
                if str(days_pending).isdigit():
                    updated_days = int(days_pending) + 1
                else:
                    updated_days = 1

                # Write updated value
                if "M" not in PROTECTED_COLUMNS:  # Column M is 13th index (0-based)
                    while len(updated_row) <= 13:
                        updated_row.append("")
                    updated_row[13] = str(updated_days)

        except:
            pass

        updated_rows.append(updated_row)

    # Write back to sheet
    body = {"values": [header] + updated_rows}

    write_result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range="RFQ TEST SHEET!A:Z",
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()

    return {
        "updated": True,
        "rows_written": len(updated_rows),
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "write_result": write_result
    }
