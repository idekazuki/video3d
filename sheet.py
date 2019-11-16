import gspread
import json
import datetime

def sheet(data=['nofile','error']):
    from oauth2client.service_account import ServiceAccountCredentials 

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('your private key json file path', scope)

    gc = gspread.authorize(credentials)

    SPREADSHEET_KEY = 'spread sheet key'

    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

    import_value = int(worksheet.acell('A1').value)

    for i, logdata in enumerate(data):
        worksheet.update_cell(import_value, 2+i, logdata)

    time_stamp = str(datetime.datetime.now())
    worksheet.update_cell(import_value, 1, time_stamp)

    export_value = import_value+1
    worksheet.update_cell(1,1, export_value)

