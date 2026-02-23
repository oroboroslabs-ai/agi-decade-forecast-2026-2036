@echo off
REM Full Q3 connection - generate reports with live system integration
cd /d "%~dp0"
echo Connecting to Q3 systems and generating reports...
python q3_integrated_reports.py
echo.
echo Q3-integrated reports generated.
pause