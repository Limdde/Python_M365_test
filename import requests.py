import requests
import msal
import openpyxl
from datetime import datetime

# Azure AD OAuth 인증을 위한 변수 설정
CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"
TENANT_ID = "your_tenant_id_here"

# Microsoft Graph API 사용을 위한 엑세스 토큰
ACCESS_TOKEN = "your_access_token_here"

# 가져올 이메일의 ID
MESSAGE_ID = "your_message_id_here"

# Excel 파일에서 데이터를 업데이트할 시트의 이름
SHEET_NAME = "your_sheet_name_here"

# 업데이트할 Excel 파일의 이름
EXCEL_FILE_NAME = "your_file_name_here.xlsx"

# Microsoft Graph API 요청 헤더
headers = {
    "Authorization": "Bearer " + ACCESS_TOKEN,
    "Content-Type": "application/json"
}

# 이메일의 상세 정보 가져오기
response = requests.get(
    f"https://graph.microsoft.com/v1.0/me/messages/{MESSAGE_ID}",
    headers=headers
)

if response.status_code == 200:
    message = response.json()

    # 이메일에서 필요한 정보 가져오기
    sender_email = message["sender"]["emailAddress"]["address"]
    subject = message["subject"]
    received_time = message["receivedDateTime"]
    received_time = datetime.strptime(received_time, "%Y-%m-%dT%H:%M:%SZ")

    # Excel 파일 열기
    workbook = openpyxl.load_workbook(EXCEL_FILE_NAME)
    sheet = workbook[SHEET_NAME]

    # Excel 파일에 데이터 추가
    row = [sender_email, subject, received_time]
    sheet.append(row)

    # Excel 파일 저장 및 닫기
    workbook.save(EXCEL_FILE_NAME)
    workbook.close()

else:
    print("Failed to get message with error code:", response.status_code)