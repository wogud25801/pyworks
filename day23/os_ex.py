# os 모듈 - 환경변수나 디렉터리, 파일 등의 OS 자원을 제어하는 모듈

import os

os.chdir('c:/pyworks/day26')  # 경로 이동

dir = os.popen('dir')         # dir 명령 실행

print(dir.read())