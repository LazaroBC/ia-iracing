@echo off
setlocal enabledelayedexpansion
set "DEST=C:\Users\LLATZER\Documents\iRacing\setups\ferrari488gte\setupClaude"

if not exist "%DEST%" (
    mkdir "%DEST%"
    echo Carpeta creada: %DEST%
) else (
    echo La carpeta ya existia: %DEST%
)

if "%~1"=="" (
    echo.
    echo No has arrastrado ningun archivo.
    echo Para usarlo: arrastra uno o varios archivos .sto sobre este .bat
    echo (o sobre un acceso directo a este .bat) y se copiaran a setupClaude.
    pause
    exit /b
)

:loop
if "%~1"=="" goto done
copy /Y "%~1" "%DEST%\" >nul
echo Copiado: %~nx1
shift
goto loop

:done
echo.
echo Listo. Archivos guardados en:
echo %DEST%
pause
