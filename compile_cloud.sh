#!/bin/bash
# Script para GitHub Codespaces - Compilação APK na Nuvem

echo "🐲 RPG ÉPICO - COMPILAÇÃO CLOUD 🦄"
echo "=================================="
echo ""

# Atualizar sistema
echo "📦 Atualizando sistema..."
sudo apt update
sudo apt install -y python3-pip python3-venv git zip unzip

# Instalar dependências Java/Android
echo "☕ Instalando Java..."
sudo apt install -y openjdk-11-jdk

# Configurar JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> ~/.bashrc

# Instalar buildozer
echo "🔧 Instalando buildozer..."
pip3 install --user buildozer cython
echo 'export PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc
source ~/.bashrc

# Compilar APK
echo "🚀 COMPILANDO APK..."
echo "⏳ Isso pode demorar 15-30 minutos..."

# Aceitar licenças Android automaticamente
mkdir -p ~/.android
echo 'count=0' > ~/.android/repositories.cfg

# Compilar
$HOME/.local/bin/buildozer android debug

echo ""
if [ -f "bin/*.apk" ]; then
    echo "✅✅✅ APK GERADO COM SUCESSO! ✅✅✅"
    echo ""
    echo "📱 APK disponível em: bin/"
    ls -la bin/*.apk
    echo ""
    echo "📥 Para baixar:"
    echo "   1. Clique com botão direito no arquivo APK"
    echo "   2. Selecione 'Download'"
    echo "   3. Instale no seu celular Android"
else
    echo "❌ Erro na compilação. Verifique os logs acima."
fi

echo ""
echo "🎮 Seu RPG épico está quase pronto para mobile!"
