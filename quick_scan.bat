@echo off
REM Quick run - just generate reports without git push
cd /d "%~dp0"
echo Running quick report generation...
python setup_reports.py --run
echo.
echo Reports updated in auto_runs\
pause