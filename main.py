import win32com.client
from datetime import datetime
import os

def extract_10_digit_numbers(text):
    import re
    return re.findall(r'\b\d{10}\b', text)

def main():
    # Outlook 애플리케이션에 연결
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    
    # 기본 받은 편지함 폴더 가져오기
    inbox = outlook.GetDefaultFolder(6)  # 6은 받은 편지함을 나타냄
    
    # 받은 편지함에서 'Wargaming\Data Deletion Request' 폴더를 찾기
    wargaming_folder = inbox.Folders.Item("Wargaming").Folders.Item("Data Deletion Request")
    
    # 폴더의 모든 메일 아이템을 가져오기
    messages = wargaming_folder.Items
    
    # 안 읽은 메일 필터링
    unread_messages = messages.Restrict("[Unread] = True")
    
    first_loop = True  # 첫 번째 루프 여부를 확인하는 변수
    
    output_lines = []

    chkFirst = True
    for message in unread_messages:
        subject = message.Subject
        body = message.Body
        
        # 제목과 본문에서 10자리 숫자를 추출
        numbers_in_subject = extract_10_digit_numbers(subject)
        numbers_in_body = extract_10_digit_numbers(body)
        
        if numbers_in_subject or numbers_in_body:
            if first_loop:
                output_lines.append("use WARGAMING_BILL_DB")
                output_lines.append("--drop table #tmp_twgnlogmst_2024")
                output_lines.append("")
                output_lines.append("select USERNO")
                output_lines.append("into #tmp_twgnlogmst_2024")
                output_lines.append("from TWGNLogMst with(nolock)")
                output_lines.append("where SPA_ID in (")
                first_loop = False

            first_number_printed = False

            if numbers_in_body:
                if not first_number_printed:
                    if chkFirst:
                        output_lines.append(f"'{numbers_in_body[0]}'")
                        chkFirst = False
                    else:
                        output_lines.append(f",'{numbers_in_body[0]}'")
                    first_number_printed = True

    if not first_loop:
        output_lines.append(")")
        output_lines.append("")
        output_lines.append("/*")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERNAME = ''")
        output_lines.append("      ,UPDDATE  = GETDATE()")
        output_lines.append("FROM   TAccountInfoMst A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.MUserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERID   = ''")
        output_lines.append("      ,USERNAME = ''")
        output_lines.append("      ,UPDDATE  = GETDATE()")
        output_lines.append("FROM   TAccountMst A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.MUserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERID   = ''")
        output_lines.append("      ,USERNAME = ''")
        output_lines.append("      ,UPDDATE  = GETDATE()")
        output_lines.append("FROM  TCashMst A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.MUserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERID   = ''")
        output_lines.append("      ,USERNAME = ''")
        output_lines.append("      ,UPDDATE  = GETDATE()")
        output_lines.append("FROM  TCashReceiptMst A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.UserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERID   = ''")
        output_lines.append("      ,USERNAME = ''")
        output_lines.append("      ,UPDDATE  = GETDATE()")
        output_lines.append("FROM  TPartCashMst A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.MUserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERID   = ''")
        output_lines.append("      ,USERNAME = ''")
        output_lines.append("FROM  TPGLogMst A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.UserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERID   = ''")
        output_lines.append("      ,USERNAME = ''")
        output_lines.append("      ,UPDDATE  = GETDATE()")
        output_lines.append("FROM  TWGNLogMst A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.UserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERID   = ''")
        output_lines.append("      ,UPDDATE  = GETDATE()")
        output_lines.append("FROM  TVAccountMst A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.MUserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("UPDATE A")
        output_lines.append("SET    USERID   = ''")
        output_lines.append("      ,UPDDATE  = GETDATE()")
        output_lines.append("FROM  TVAccountHist A")
        output_lines.append("JOIN   #tmp_twgnlogmst_2024 B ON A.MUserNo = b.UserNo")
        output_lines.append("")
        output_lines.append("*/")

    # 오늘 날짜를 파일명에 포함
    today_date = datetime.today().strftime('%Y%m%d')
    file_name = f"{today_date}_output.txt"
    file_path = fr"C:\Users\yjseong\Documents\wargamingMail\wargamingDeletion\{file_name}"
    
    # 기존 파일이 있으면 삭제
    if os.path.exists(file_path):
        os.remove(file_path)

    # 파일에 쓰기
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(f"{line}\n")

if __name__ == "__main__":
    main()
