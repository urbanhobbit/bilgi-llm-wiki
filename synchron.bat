@echo off
REM =====================================================
REM BILGI-LLM-WIKI GITHUB SENKRONIZASYON BAT Dosyasi
REM =====================================================
echo.
echo =====================================================
echo  BILGI-LLM-WIKI SENKRONIZASYON ARACI
echo =====================================================
echo.

set "LOCAL_VAULT=D:\One Drive\OneDrive - Infakto Research Workshop\Masaüstü\Obsidian\bilgi-llm-wiki"
set "REMOTE_REPO=https://github.com/urbanhobbit/bilgi-llm-wiki.git"

cd /d "%LOCAL_VAULT%"
if %errorlevel% neq 0 (
    echo [HATA] Vault dizinine gidilemedi: %LOCAL_VAULT%
    pause
    exit /b 1
)

echo [1/4] Git status kontrol ediliyor...
git status --short

for /f "delims=" %%i in ('git status --short') do set "HAS_CHANGES=%%i"
if "%HAS_CHANGES%"=="" (
    echo.
    echo [BILGI] Degisiklik bulunamadi.
    pause
    exit /b 0
)

echo [2/4] Commit ediliyor...
git add -A
git commit -m "Wiki sync: automatic update"

echo [3/4] Remote guncelleniyor...
git fetch origin
git merge origin/main

echo [4/4] Push ediliyor...
git push origin main

echo.
echo =====================================================
echo  SENKRONIZASYON TAMAMLANDI!
echo =====================================================
git log --oneline -3
echo.
pause
