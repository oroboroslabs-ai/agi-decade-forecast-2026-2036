@echo off
REM Start Q3 Docker services if not running
echo Checking Q3 Docker services...
echo.

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not running. Please start Docker Desktop.
    pause
    exit /b 1
)

echo Starting Q3 services...
echo.

REM Start Q3 Superintelligence
docker ps | findstr Q3_SUPERINTELLIGENCE >nul
if errorlevel 1 (
    echo Starting Q3_SUPERINTELLIGENCE_CORE...
    docker start Q3_SUPERINTELLIGENCE_CORE 2>nul || echo Container not found
) else (
    echo [OK] Q3_SUPERINTELLIGENCE_CORE already running
)

REM Start Q3 Sovereign Node
docker ps | findstr Q3_SOVEREIGN_NODE >nul
if errorlevel 1 (
    echo Starting Q3_SOVEREIGN_NODE...
    docker start Q3_SOVEREIGN_NODE 2>nul || echo Container not found
) else (
    echo [OK] Q3_SOVEREIGN_NODE already running
)

REM Start Q3 Memory Bank (Redis)
docker ps | findstr Q3_MEMORY_BANK >nul
if errorlevel 1 (
    echo Starting Q3_MEMORY_BANK...
    docker start Q3_MEMORY_BANK 2>nul || echo Container not found
) else (
    echo [OK] Q3_MEMORY_BANK already running
)

echo.
echo Q3 Services Status:
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | findstr Q3

echo.
echo Services started. Run run_system.bat to generate reports.
pause