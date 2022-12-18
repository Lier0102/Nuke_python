@echo off
title 디버그를 시작합니다!
REM 아 맞다 그리고 인코딩 ANSI로 저장해야 한글 안 깨짐

title chceck_env.bat 실행중...
cmd /k main_start.bat

echo 작업이 끝난후 아무키나 눌러주세요!
pause>nul
exit