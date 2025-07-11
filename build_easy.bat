@echo off
echo 🚀 RPG Épico - Compilação Fácil de APK
echo.

echo 📋 OPÇÃO 1: WSL (Recomendado)
echo ====================================
echo 1. wsl
echo 2. cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version
echo 3. sudo apt update
echo 4. sudo apt install -y python3-pip python3-venv
echo 5. pip3 install buildozer cython
echo 6. buildozer android debug
echo.

echo 📋 OPÇÃO 2: Automático
echo ====================================
set /p choice="Tentar instalação automática via WSL? (s/n): "
if /i "%choice%"=="s" goto auto_install
if /i "%choice%"=="y" goto auto_install
goto manual

:auto_install
echo 🔄 Verificando WSL...
wsl --list --quiet >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ WSL não encontrado! Instalando...
    wsl --install -d Ubuntu
    echo ⚠️ Reinicie o computador e execute novamente!
    pause
    exit /b
)

echo ✅ WSL encontrado! Configurando...
wsl bash -c "sudo apt update && sudo apt install -y python3-pip python3-venv build-essential"
wsl bash -c "pip3 install --user buildozer cython"
wsl bash -c "cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version && buildozer android debug"

if %errorlevel% equ 0 (
    echo.
    echo ✅ APK GERADO COM SUCESSO!
    echo 📱 Arquivo: bin/rpgepico-1.0.0-arm64-v8a-debug.apk
    echo.
) else (
    echo ❌ Erro na compilação!
)
goto end

:manual
echo.
echo 📋 PASSOS MANUAIS:
echo 1. Abra WSL: wsl
echo 2. Navegue: cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version
echo 3. Atualize: sudo apt update
echo 4. Instale: sudo apt install -y python3-pip python3-venv build-essential
echo 5. Buildozer: pip3 install --user buildozer cython
echo 6. Compile: buildozer android debug
echo.

:end
pause
