@echo off

cd /d "G:\gs\c programming\FSV_C"


:loop

git add .

git diff --cached --quiet
if errorlevel 1 (
    git commit -m "Auto backup"
    git push
)

timeout /t 20 >nul

goto loop
