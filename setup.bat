@echo off
echo GitHub Repository Visibility Manager - Setup
echo ===========================================

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is required but not installed.
    echo Please install Python and try again.
    exit /b 1
)

REM Create virtual environment
if exist venv (
    echo Virtual environment already exists.
) else (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created successfully.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Setup completed successfully!
echo.
echo To use the GitHub Repository Visibility Manager:
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Run the script:
echo    python main.py
echo.
echo 3. When finished, deactivate the virtual environment:
echo    deactivate