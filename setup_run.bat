@echo off

:: Create virtual environment
python -m venv venv
call venv\Scripts\activate

:: Install required packages
pip install -r requirements.txt

:: Run the bot
python main.py
pause
