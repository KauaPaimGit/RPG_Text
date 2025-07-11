"""
Compilador APK para Windows - Alternativa ao WSL
Execute: python compile_windows.py
"""

import subprocess
import sys
import os
import time

def executar_comando(comando, shell=True):
    """Executa comando e retorna resultado"""
    try:
        result = subprocess.run(comando, shell=shell, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def verificar_python():
    """Verifica se Python está instalado"""
    print("🐍 Verificando Python...")
    sucesso, stdout, stderr = executar_comando("python --version")
    if sucesso:
        print(f"✅ Python encontrado: {stdout.strip()}")
        return True
    else:
        print("❌ Python não encontrado!")
        print("💡 Instale Python 3.8+ de: https://python.org")
        return False

def instalar_buildozer():
    """Instala buildozer usando pip"""
    print("📦 Instalando buildozer...")
    
    # Instalar dependências
    comandos = [
        "pip install --upgrade pip",
        "pip install buildozer",
        "pip install cython",
        "pip install kivy[base]"
    ]
    
    for comando in comandos:
        print(f"⚡ Executando: {comando}")
        sucesso, stdout, stderr = executar_comando(comando)
        if not sucesso:
            print(f"⚠️ Aviso: {comando} falhou")
            print(f"Erro: {stderr}")
        else:
            print(f"✅ {comando} - OK")

def compilar_apk():
    """Compila o APK usando buildozer"""
    print("🚀 COMPILANDO APK...")
    print("⏳ Isso pode demorar 15-30 minutos na primeira execução!")
    print("")
    
    # Verificar se está no diretório correto
    if not os.path.exists("main.py"):
        print("❌ Arquivo main.py não encontrado!")
        print("Execute este script no diretório mobile_version")
        return False
    
    if not os.path.exists("buildozer.spec"):
        print("❌ Arquivo buildozer.spec não encontrado!")
        return False
    
    # Compilar APK
    print("🔨 Iniciando compilação...")
    # Usar Python para executar buildozer
    sucesso, stdout, stderr = executar_comando("python -m buildozer android debug", shell=True)
    
    if sucesso:
        print("")
        print("✅✅✅ APK GERADO COM SUCESSO! ✅✅✅")
        print("")
        print("📱 Seu APK está em:")
        print("   📁 bin/rpgepico-1.0.0-arm64-v8a-debug.apk")
        print("")
        print("📲 Para instalar no celular:")
        print("   1. Copie o arquivo .apk para o celular")
        print("   2. Ative 'Fontes desconhecidas' nas configurações")
        print("   3. Toque no arquivo para instalar")
        print("")
        print("🎮 PARABÉNS! Seu RPG épico está pronto!")
        return True
    else:
        print("")
        print("❌ Erro na compilação!")
        print("Saída do erro:")
        print(stderr)
        print("")
        print("💡 Possíveis soluções:")
        print("   1. Instale Android Studio")
        print("   2. Configure ANDROID_HOME")
        print("   3. Use WSL como alternativa")
        return False

def main():
    print("🐲 RPG ÉPICO - COMPILADOR APK WINDOWS 🦄")
    print("=" * 50)
    print("")
    
    # Verificar Python
    if not verificar_python():
        return
    
    # Instalar buildozer
    instalar_buildozer()
    
    # Aguardar confirmação
    print("")
    input("📋 Pressione ENTER para iniciar a compilação APK...")
    print("")
    
    # Compilar APK
    compilar_apk()
    
    print("")
    input("Pressione ENTER para sair...")

if __name__ == "__main__":
    main()
