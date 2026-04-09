@echo off
chcp 65001 >nul
set "LOCAL_VAULT=D:\Obsidian\bilgi-llm-wiki"

cd /d "%LOCAL_VAULT%"
if %errorlevel% neq 0 (
    echo [HATA] Dizine gidilemedi
    pause
    exit /b 1
)

echo [OK] %cd%
git status --short

for /f "delims=" %%i in ('git status --short') do set "HAS_CHANGES=%%i"
if "%HAS_CHANGES%"=="" (
    echo [OK] Guncel.
    pause
    exit /b 0
)

echo [OK] Commit...
git add -A
git commit -m "Wiki sync"
git fetch origin
git merge origin/main
git push origin main

echo [OK] TAMAMLANDI!
git log --oneline -3
pause
