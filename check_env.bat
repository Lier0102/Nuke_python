@echo off
REM 렘은 주석이야!
REM echo off는 앞으로 어떤 명령어를 썼는지 일일이 화면에 출력하지 않기 위해서 썼어!
REM 출력을 하게 되면 화면이 더러워지기 때문이지!
title PYTHON CHECKING...
python --version 3>nul
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
python -m pip install -r requirements.txt
cls
Title MODULE CHECKING...
echo python main.py is about to run!
start main_start.bat