@echo off
title RPG Épico - Compilador APK Simples

echo.
echo 🐲 RPG ÉPICO - GERADOR DE APK 🦄
echo ================================
echo.

echo 📋 AGUARDE: Ubuntu está sendo instalado no WSL...
echo ⏳ Isso pode demorar alguns minutos.
echo.

:check_wsl
wsl --list --quiet | findstr Ubuntu >nul 2>&1
if %errorlevel% neq 0 (
    echo ⏳ Aguardando instalação do Ubuntu...
    timeout /t 10 /nobreak >nul
    goto check_wsl
)

echo ✅ Ubuntu WSL instalado!
echo.

echo 🔄 Configurando ambiente Python...
wsl -d Ubuntu -e bash -c "sudo apt update -y"
wsl -d Ubuntu -e bash -c "sudo apt install -y python3-pip python3-venv build-essential git"

echo.
echo 📦 Instalando Buildozer...
wsl -d Ubuntu -e bash -c "pip3 install --user buildozer cython"
wsl -d Ubuntu -e bash -c "echo 'export PATH=\$PATH:\$HOME/.local/bin' >> ~/.bashrc"

echo.
echo 🚀 COMPILANDO APK...
echo ⚡ Isso pode demorar 15-30 minutos na primeira vez!
echo.

wsl -d Ubuntu -e bash -c "cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version && ~/.local/bin/buildozer android debug"

if %errorlevel% equ 0 (
    echo.
    echo ✅✅✅ APK GERADO COM SUCESSO! ✅✅✅
    echo.
    echo 📱 Seu APK está em:
    echo    📁 bin\rpgepico-1.0.0-arm64-v8a-debug.apk
    echo.
    echo 📲 Para instalar no celular:
    echo    1. Copie o arquivo .apk para o celular
    echo    2. Ative "Fontes desconhecidas" nas configurações
    echo    3. Toque no arquivo para instalar
    echo.
    echo 🎮 PARABÉNS! Seu RPG épico está pronto para mobile!
) else (
    echo.
    echo ❌ Erro na compilação!
    echo 💡 Tente executar manualmente:
    echo    wsl
    echo    cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version
    echo    buildozer android debug
)

echo.
pause
