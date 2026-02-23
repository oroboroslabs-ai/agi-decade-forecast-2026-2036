@echo off
REM ============================================================
REM QUICK REPORT - No Q3 Connection Required
REM ============================================================

echo.
echo ============================================================
echo   DECADE FORECAST - QUICK REPORT
echo ============================================================
echo.

cd /d "%~dp0"

echo [1/2] Generating reports...
python setup_reports.py --run

echo.
echo [2/2] Reports generated.
echo --------------------------------------------------------
echo.
echo   Reports saved to:
echo   - auto_runs\seer\latest.md
echo   - auto_runs\agi\latest.md
echo   - auto_runs\convergence\latest.md
echo.
echo ============================================================
pause