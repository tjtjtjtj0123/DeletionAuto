# DeletionAuto
outlook 수신 메일 취합 프로그램

# main.py
outlook 메일 취합 프로그램
: Wargmaing에서 사용자 삭제 요청 메일이 들어온 경우, 메일에 포함된 10자리의 숫자 추출후, 삭제 sql 코드 출력하는 프로그램

# 사용 방법
## 0. 공통
1) 파이썬 다운로드
2) outlook에 접근할 수 있도록 설치
  > cmd에서 pip install pywin32 실행

## 1. 직접 실행하는 방법
3) 파일 위치에서 명령어 실행하여 프로그램 실행
  > 터미널에서 python main.py
4) 명령어 실행한 경우, wargamingDeletion 폴더 내에 사용자 정보 삭제 sql문 생성됨
- 사용하고 싶은 경우, outlook 메일 경로 설정 필수!
  -> 현재 경로의 경우, 받은 편지함\Wargaming\Data Deletion Request 안에 있음

## 2. exe 파일로 생성해 실행하는 방법
3) Pyinstaller 설치
> pip install pyinstaller
4) 실행 파일 생성: main.py가 있는 디렉토리로 이동한 후, 다음 명령어를 입력
> pyinstaller --onefile main.py
5) 생성된 main.exe 파일 더블 클릭 후, 사용
