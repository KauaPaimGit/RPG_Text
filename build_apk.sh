#!/bin/bash

# Script automatizado para compilar RPG Épico Mobile
# Execute este script no Linux/WSL para gerar o APK

echo "🐲 RPG ÉPICO MOBILE - COMPILADOR AUTOMÁTICO 🦄"
echo "================================================"

# Verificar se está no Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "❌ Este script deve ser executado no Linux ou WSL!"
    echo "💡 Instale o WSL no Windows: wsl --install"
    exit 1
fi

echo "📋 Verificando dependências..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado! Instalando..."
    sudo apt update
    sudo apt install -y python3 python3-pip
fi

# Verificar Java
if ! command -v java &> /dev/null; then
    echo "❌ Java não encontrado! Instalando..."
    sudo apt install -y openjdk-11-jdk
fi

# Verificar Buildozer
if ! command -v buildozer &> /dev/null; then
    echo "🔧 Instalando Buildozer..."
    
    # Instalar dependências do sistema
    sudo apt update
    sudo apt install -y git zip unzip autoconf libtool pkg-config \
        zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 \
        cmake libffi-dev libssl-dev build-essential \
        libltdl-dev libffi-dev libssl-dev python3-dev

    # Instalar Buildozer
    pip3 install --user buildozer
    echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
    export PATH=$PATH:~/.local/bin
fi

echo "✅ Dependências verificadas!"

# Aceitar licenças do Android
echo "📱 Configurando Android SDK..."
yes | buildozer android debug 2>/dev/null || echo "⚠️ Primeira execução - baixando dependências..."

# Compilar APK
echo "🔨 Compilando RPG Épico Mobile..."
echo "⏳ Este processo pode demorar 10-30 minutos na primeira vez..."

if buildozer android debug; then
    echo ""
    echo "🎉 SUCESSO! APK compilado com êxito!"
    echo "📱 APK localizado em: bin/rpgepico-1.0.0-arm64-v8a-debug.apk"
    echo ""
    echo "📲 Para instalar no dispositivo:"
    echo "   1. Conecte o celular via USB"
    echo "   2. Ative 'Depuração USB' nas opções de desenvolvedor"
    echo "   3. Execute: adb install bin/rpgepico-1.0.0-arm64-v8a-debug.apk"
    echo ""
    echo "🌟 Ou transfira o arquivo .apk para o celular e instale manualmente!"
    
    # Mostrar tamanho do APK
    APK_SIZE=$(du -h bin/*.apk 2>/dev/null | cut -f1 | head -1)
    if [ ! -z "$APK_SIZE" ]; then
        echo "📦 Tamanho do APK: $APK_SIZE"
    fi
    
else
    echo ""
    echo "❌ ERRO na compilação!"
    echo "🔧 Tente os seguintes passos:"
    echo "   1. buildozer android clean"
    echo "   2. buildozer android debug"
    echo ""
    echo "📖 Para mais ajuda, consulte o README.md"
    exit 1
fi

echo ""
echo "🚀 Próximos passos:"
echo "   • Teste o APK no seu dispositivo"
echo "   • Para versão de produção: buildozer android release"
echo "   • Para publicar: assine o APK com sua chave de desenvolvedor"
echo ""
echo "🐲 Divirta-se com o RPG Épico Mobile! 🦄"
