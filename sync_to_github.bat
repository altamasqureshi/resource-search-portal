@echo off
cd /d %~dp0

set GIT_PATH="C:\Users\Petpooja-567\AppData\Local\GitHubDesktop\app-3.5.4\resources\app\git\cmd\git.exe"

echo --------------------------------------
echo Syncing your code to GitHub...
echo --------------------------------------

:: Optional: rename master to main if not already done
%GIT_PATH% rev-parse --verify master >nul 2>&1
if %errorlevel%==0 (
    %GIT_PATH% checkout master
    %GIT_PATH% pull origin master
    %GIT_PATH% branch -M main
    %GIT_PATH% push -u origin main
)

:: Add all changes
%GIT_PATH% add .

:: Create a commit message with date and time
for /f "tokens=*" %%i in ('powershell -Command "Get-Date -Format \"yyyy-MM-dd_HH-mm-ss\""') do set timestamp=%%i     
%GIT_PATH% commit -m "Auto sync commit at %timestamp%"

:: Push to main branch
%GIT_PATH% push origin main

echo --------------------------------------
echo ✅ Sync complete!
pause
