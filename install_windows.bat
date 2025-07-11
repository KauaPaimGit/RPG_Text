@echo off
echo 🐲 RPG ÉPICO MOBILE - INSTALADOR WINDOWS 🦄
echo =============================================
echo.

echo 📋 Este script irá instalar o WSL e as dependências necessárias
echo    para compilar o RPG Épico Mobile no Windows.
echo.

pause

echo 🔧 Verificando se WSL está instalado...
wsl --list >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ WSL não está instalado!
    echo 📥 Instalando WSL com Ubuntu...
    wsl --install -d Ubuntu
    echo.
    echo ⚠️  IMPORTANTE: Após a instalação, reinicie o computador
    echo    e execute este script novamente.
    pause
    exit /b 1
)

echo ✅ WSL detectado!
echo.

echo 🐧 Configurando ambiente Linux no WSL...
wsl bash -c "
echo '🔄 Atualizando sistema...'
sudo apt update && sudo apt upgrade -y

echo '📦 Instalando dependências...'
sudo apt install -y python3 python3-pip git zip unzip openjdk-11-jdk \
    autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
    libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev \
    build-essential libltdl-dev

echo '🛠️ Instalando Buildozer...'
pip3 install --user buildozer
echo 'export PATH=\$PATH:~/.local/bin' >> ~/.bashrc

echo '✅ Configuração concluída!'
"

echo.
echo 📁 Copiando arquivos do projeto para WSL...
wsl bash -c "mkdir -p ~/rpg_epico_mobile"

for %%f in (main.py buildozer.spec requirements.txt README.md build_apk.sh) do (
    copy "%%f" "\\wsl$\Ubuntu\home\%USERNAME%\rpg_epico_mobile\" >nul 2>&1
)

echo ✅ Arquivos copiados!
echo.

echo 🚀 Compilando APK no WSL...
wsl bash -c "
cd ~/rpg_epico_mobile
chmod +x build_apk.sh
./build_apk.sh
"

echo.
echo 📱 Copiando APK compilado de volta para Windows...
if exist "\\wsl$\Ubuntu\home\%USERNAME%\rpg_epico_mobile\bin\*.apk" (
    copy "\\wsl$\Ubuntu\home\%USERNAME%\rpg_epico_mobile\bin\*.apk" . >nul 2>&1
    echo ✅ APK copiado para o diretório atual!
    echo.
    echo 🎉 SUCESSO! O APK foi compilado e está pronto para uso!
    echo 📂 Arquivo: %cd%\rpgepico-1.0.0-arm64-v8a-debug.apk
) else (
    echo ❌ Erro: APK não foi encontrado.
    echo 🔧 Verifique os logs acima para identificar o problema.
)

echo.
echo 📲 Para instalar no seu dispositivo Android:
echo    1. Copie o arquivo .apk para o celular
echo    2. Abra o arquivo no celular
echo    3. Permita "Instalar de fontes desconhecidas"
echo    4. Toque em "Instalar"
echo.

pause
