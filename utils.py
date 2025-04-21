import gspread
from oauth2client.service_account import ServiceAccountCredentials
def write_xl_file(file , df) :
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('sheet_secret.json', scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open(file) 
    worksheet = spreadsheet.sheet1
    for row in df.values.tolist():
        worksheet.append_row(row)

    print("Les données ont été téléchargées dans Google Sheets.")
    



def clear_google_sheet(file_name, sheet_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('sheet_secret.json', scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open(file_name)
    worksheet = spreadsheet.worksheet(sheet_name)

    num_rows = len(worksheet.get_all_values())
    
    if num_rows > 1:
        worksheet.batch_clear([f"A2:Z{num_rows}"])
        print(f"{num_rows - 1} lignes supprimées (l’en-tête a été conservé).")
    else:
        print("Aucune ligne à supprimer en dehors de l’en-tête.")

