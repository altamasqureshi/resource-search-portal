@echo off
cd /d %~dp0

echo --------------------------------------
echo Syncing your code to GitHub...
echo --------------------------------------

:: Optional: rename master to main if not already done
git rev-parse --verify master >nul 2>&1
if %errorlevel%==0 (
    git checkout master
    git pull origin master
    git branch -M main
    git push -u origin main
)

:: Add all changes
git add .

:: Create a commit message with date and time
for /f %%i in ('powershell -Command "Get-Date -Format \"yyyy-MM-dd_HH-mm-ss\""') do set timestamp=%%i
git commit -m "Auto sync commit at %timestamp%"

:: Push to main branch
git push origin main

echo --------------------------------------
echo ✅ Sync complete!
pause
