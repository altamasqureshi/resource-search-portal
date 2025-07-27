@echo off
:: Get the directory where the script is located
set SCRIPT_DIR=%~dp0

:: Navigate to that directory
cd /d "%SCRIPT_DIR%"

:: Add all files to staging
git add .

:: Get current date and time
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do (
    set dd=%%a
    set mm=%%b
    set yyyy=%%c
)
for /f "tokens=1-2 delims=: " %%i in ("%time%") do (
    set hour=%%i
    set minute=%%j
)

:: Optional: zero-pad single-digit hours/minutes
if 1%hour% LSS 20 set hour=0%hour%
if 1%minute% LSS 20 set minute=0%minute%

:: Create commit message
set msg=Auto Sync on %dd%-%mm%-%yyyy% at %hour%:%minute%
git commit -m "%msg%"

:: Push to GitHub (change branch if not main)
git push origin main

echo.
echo ✅ Code synced to GitHub successfully from: %SCRIPT_DIR%
pause
