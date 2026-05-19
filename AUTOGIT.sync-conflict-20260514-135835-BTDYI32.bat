@echo off

cd /d "D:\YourProjectFolder"

:loop

git add .

git diff --cached --quiet
if errorlevel 1 (
    git commit -m "Auto backup"
    git push
)

timeout /t 120 >nul

goto loop