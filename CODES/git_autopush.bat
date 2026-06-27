@echo off
:: Navigate automatically to the folder where this batch file lives
cd /d "%~dp0"

:: Check if there are any new or modified files
git status --porcelain | findstr /R "^" >nul
if %errorlevel% equ 0 (
    echo [🤖 BOT] Changes detected. Preparing upload...
    
    :: Stage all changes
    git add .
    
    :: Commit changes with a clean, dynamic timestamp
    git commit -m "Automated Sync: %date% %time%"
    
    :: Push safely to your main remote branch
    git push origin main
    
    echo [🤖 BOT] Daily code successfully pushed to GitHub!
) else (
    echo [🤖 BOT] No new code changes found today. Skipping push.
)