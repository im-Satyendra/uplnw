
import gspread
credentials = {
  "type": "service_account",
  "project_id": "gdriveuserge",
  "private_key_id": "bc3247c8d7fe901a4d9a76c915abc1b06e9c3128",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDLasLp57ad3KuZ\nOSdtx76sH8q4eTvpp/9JSa8iD5GivZA8/iRQrFeQyJ77PdkCcr52Igy1Bw9OthT0\nbTsqGmY3vo1DEKt+n5TAHSU5jsJz61TQzMwDq3eY2IUdwUU/j7LTEaoOaqIzCjcC\noWImWIH1kM8eWRMgKjGU6QdE5LYyV0LE/7wmZGrLzggGlDELzvz6v5psnPXu9ffA\n02DmgDD4UbT9HA1IR4oidySlVIlelbH0kSHDgH1+B7DApc1xjNXPggIuERKFdkyy\nBR5d5Wkms2pY+aGNQnWQpfITd1TjgDd5FbxffjnpIb36CU6J9JaNoaMJZRczRfAV\n23hT5C7RAgMBAAECggEAAbcCMqed7gHEvpNxRicnb9sKwfhfrW4ZpFwHKnHYJ/eS\nJjl8Q+PYDyPp1zNjx3YBLgzGb6ZCFkdJsO/UzluPnguwtC6JS5V70wzL2grej8yd\nl+8KD0PcS8ETijctZsZG2ymsddenS2fcI90Jb0pSuifA30Af/abtaRR317hX4t++\nmtT27MqVSdkmSvNanakrrXI5zyiNymzXxfWt7muH2ie5/SLJ7iDcq8N90wpzvEFG\nGgBwt/ZGbJIPlBwXnP0pHzzA9peAjDVhGieqNl/WO68s9IZMhNfBB6Fj/Kldhrsq\nPzBxnmAkwQLFoh5dINhvBKXxVE8SnecR3vBUAsE++QKBgQDl4AxHzoX6Q3ZtDBW+\ncKcMLTLKZbNerQWScz0500174eFoiUViMzjZmVUsxQbHoYBy9ARY9IFHuauQku5x\ndQIYW1bZ//UZix87HpEdmidmnjgOKUkmKOPQibxdmlc27ADLPRh8rOVjM65nYTlB\naDcfKKkz37UsdkgRHCa8lbkCLQKBgQDiiPG2txVPNAqfzBdSZYGsZ6h+w1O4oN0T\nJnScQYzvJtngF7w6EEncCD8eUbIs6GbcpQTr1i6GOsCabGu673D5CpUrug54iGPm\nAV/opv3m9ECukc0wfuLCCjFYNrQR4AKPhC7qhnUZ0qEkmyF8eFuICXoupA55dgNN\n8YFTOCRZtQKBgB3KLC0+EVS+W2GEWGkGlk9YqCVciqMxTvCMqJmOzZLJUfnHGEvC\nkZJ5cXVMzzUds9Sx1MJmZT6TTC1/LRFc9XmMlLPJnMzDn7d8nZe1e3er9122cflV\nATjsMJH8x2KhsPSlpT+69Dsn3mkdS1szkzkhftPvIL5zUaGOAWMdEA29AoGBAKYb\nUlnu/4IXH98ycLtrUN1RGNzybtZHpjNflEvrSOMncsT9wng072OW7GlX8DU7qAkM\nO4KOh4jHVeklrQzie80w9Fae0/OP1uiVg3T91dleqnsW0AVKVQ2BGdOcMQeWYWpI\nu3oeY4kuyBgmZDR3sG4cvOmsRCzN2vhxKKoT1ZutAoGAa1Bvzdhpx1DzhzkTuCcv\nM2NmmZ1/4m1DzVngPCBhtkrKYwPQY7Dq6gmc40udnBV/GRfI365RpQqKcUGNA/jw\nBdrxkPmYgG1M45vcCNV/FzkFPE+9EDiET92UrcgQavKwPkFfLbhWt/IdRQ6SdvZG\nZa8vm7hTF9xa6DCMtFhN/1g=\n-----END PRIVATE KEY-----\n",
  "client_email": "satuserge@gdriveuserge.iam.gserviceaccount.com",
  "client_id": "102675144284628656477",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/satuserge%40gdriveuserge.iam.gserviceaccount.com"
}

#sa = gspread.service_account(filename="service_account.json")
#sa = gspread.service_account()
sa = gspread.service_account_from_dict(credentials)
#sh= sa.open("JEE ULTIMATE 2022")
si = "1Iuz971A-HmOQBf3y005XBO3XCEpsJZly2GL8Cc6Gar0"
si = "1Iuz971A-HmOQBf3y005XBO3XCEpsJZly2GL8Cc6Gar0"
sh = sa.open_by_key(si)
worksheet_list = sh.worksheets()
#for sheet in worksheet_list:
 #   print('sheetName: {}, sheetId(GID): {}'.format(sheet.title, sheet.id))

l = sh.worksheet("JEE ULTIMATE")
#print("Rows: ",l.row_count)
#print("Coulumns: ",l.col_count)
#print(l.acell('C101'))
#print(l.cell(7,8).value)
#print(l.get('A7:E9'))
#print(l.get_all_values())
k = l.update('A116', 'test')
#l.delete_rows(116)
import requests
import urllib.parse

 # Please set the Spreadsheet ID.
cellRange = "A129"#str(input("id?"))  # Please set the range with A1Notation. In this case, the hyperlink of the cell "A1" of "Sheet1" is retrieved.
#val = l.acell(cellRange).value
h = "jgjh"
val = h

# 1. Retrieve the access token.
access_token = sa.auth.token

# 2. Request to the method of spreadsheets.get in Sheets API using `requests` module.
fields = "sheets(data(rowData(values(hyperlink))))"
url = "https://sheets.googleapis.com/v4/spreadsheets/" + si + "?ranges=" + urllib.parse.quote(cellRange) + "&fields=" + urllib.parse.quote(fields)
res = requests.get(url, headers={"Authorization": "Bearer " + access_token})

# 3. Retrieve the hyperlink.
obj = res.json()
#print(obj)
#ob = obj["sheets"][0]['data'][0]['rowData'][0]['values'][0]['hyperlink']
#print(ob)
l.update_acell(cellRange, '=HYPERLINK("https://gmail.com","ok")')
#print(val)
