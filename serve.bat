@echo off
setlocal
cd /d "%~dp0gamecenter"

where php >nul 2>nul
if errorlevel 1 (
    if exist "C:\laragon\bin\php\php-8.5.10-Win32-vs16-x64\php.exe" (
        set "PATH=C:\laragon\bin\php\php-8.5.10-Win32-vs16-x64;%PATH%"
    )
)

if not exist artisan (
    echo File artisan tidak ditemukan di folder gamecenter.
    exit /b 1
)

php artisan serve %*
