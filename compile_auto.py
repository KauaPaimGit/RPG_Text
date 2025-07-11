"""
Compilador APK MELHORADO para Windows
Configura Android SDK automaticamente
"""

import subprocess
import sys
import os
import time
import urllib.request
import zipfile
import shutil

def executar_comando(comando, shell=True, mostrar_output=False):
    """Executa comando e retorna resultado"""
    try:
        if mostrar_output:
            print(f"▶️ {comando}")
            result = subprocess.run(comando, shell=shell, text=True)
            return result.returncode == 0, "", ""
        else:
            result = subprocess.run(comando, shell=shell, capture_output=True, text=True)
            return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def baixar_arquivo(url, destino):
    """Baixa arquivo da internet"""
    try:
        print(f"📥 Baixando: {os.path.basename(destino)}")
        urllib.request.urlretrieve(url, destino)
        return True
    except Exception as e:
        print(f"❌ Erro ao baixar: {e}")
        return False

def configurar_android_sdk():
    """Configura Android SDK automaticamente"""
    print("📱 Configurando Android SDK...")
    
    # Diretório do SDK
    sdk_dir = os.path.expanduser("~/android-sdk")
    
    if os.path.exists(sdk_dir):
        print("✅ Android SDK já existe!")
        return sdk_dir
    
    print("📦 Baixando Android SDK...")
    
    # URL do command line tools
    sdk_url = "https://dl.google.com/android/repository/commandlinetools-win-9477386_latest.zip"
    sdk_zip = "android-sdk.zip"
    
    if baixar_arquivo(sdk_url, sdk_zip):
        print("📂 Extraindo SDK...")
        try:
            os.makedirs(sdk_dir, exist_ok=True)
            
            with zipfile.ZipFile(sdk_zip, 'r') as zip_ref:
                zip_ref.extractall(sdk_dir)
            
            # Mover cmdline-tools para local correto
            cmdline_src = os.path.join(sdk_dir, "cmdline-tools")
            cmdline_dst = os.path.join(sdk_dir, "cmdline-tools", "latest")
            
            if os.path.exists(cmdline_src) and not os.path.exists(cmdline_dst):
                temp_dir = os.path.join(sdk_dir, "temp")
                shutil.move(cmdline_src, temp_dir)
                os.makedirs(cmdline_src, exist_ok=True)
                shutil.move(temp_dir, cmdline_dst)
            
            os.remove(sdk_zip)
            print("✅ Android SDK configurado!")
            return sdk_dir
            
        except Exception as e:
            print(f"❌ Erro ao extrair SDK: {e}")
            return None
    
    return None

def instalar_android_tools(sdk_dir):
    """Instala ferramentas Android necessárias"""
    print("🔧 Instalando ferramentas Android...")
    
    sdkmanager = os.path.join(sdk_dir, "cmdline-tools", "latest", "bin", "sdkmanager.bat")
    
    if not os.path.exists(sdkmanager):
        print("❌ sdkmanager não encontrado!")
        return False
    
    # Aceitar licenças automaticamente
    print("📜 Aceitando licenças...")
    executar_comando(f'echo y | "{sdkmanager}" --licenses', mostrar_output=True)
    
    # Instalar componentes necessários
    componentes = [
        "platform-tools",
        "platforms;android-30",
        "build-tools;30.0.3",
        "ndk;21.4.7075529"
    ]
    
    for componente in componentes:
        print(f"📦 Instalando: {componente}")
        sucesso, _, _ = executar_comando(f'"{sdkmanager}" "{componente}"')
        if sucesso:
            print(f"✅ {componente} instalado!")
        else:
            print(f"⚠️ Falha ao instalar {componente}")
    
    return True

def configurar_buildozer_spec(sdk_dir):
    """Configura buildozer.spec com caminhos corretos"""
    print("⚙️ Configurando buildozer.spec...")
    
    spec_content = f"""[app]
title = RPG Épico
package.name = rpgepico
package.domain = com.rpgepico

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3

version = 1.0.0
requirements = python3,kivy,plyer

[buildozer]
log_level = 2
warn_on_root = 1

[app]
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 30
android.minapi = 21
android.ndk = 21b
android.sdk = 30

android.accept_sdk_license = True

[buildozer]
android.sdk_path = {sdk_dir.replace(os.sep, '/')}
android.ndk_path = {os.path.join(sdk_dir, 'ndk', '21.4.7075529').replace(os.sep, '/')}
"""
    
    with open("buildozer.spec", "w", encoding="utf-8") as f:
        f.write(spec_content)
    
    print("✅ buildozer.spec configurado!")

def compilar_apk_melhorado():
    """Compila APK com configuração melhorada"""
    print("🚀 COMPILANDO APK MELHORADO...")
    print("⏳ Primeira compilação pode demorar 30-60 minutos!")
    print("")
    
    # Verificar arquivos necessários
    if not os.path.exists("main.py"):
        print("❌ main.py não encontrado!")
        return False
    
    # Configurar Android SDK
    sdk_dir = configurar_android_sdk()
    if not sdk_dir:
        print("❌ Falha ao configurar Android SDK!")
        return False
    
    # Instalar ferramentas Android
    instalar_android_tools(sdk_dir)
    
    # Configurar buildozer.spec
    configurar_buildozer_spec(sdk_dir)
    
    # Configurar variáveis de ambiente
    os.environ["ANDROID_HOME"] = sdk_dir
    os.environ["ANDROID_SDK_ROOT"] = sdk_dir
    os.environ["PATH"] = os.environ["PATH"] + ";" + os.path.join(sdk_dir, "platform-tools")
    
    # Limpar build anterior se existir
    if os.path.exists(".buildozer"):
        print("🧹 Limpando build anterior...")
        shutil.rmtree(".buildozer", ignore_errors=True)
    
    # Compilar APK
    print("🔨 Iniciando compilação final...")
    sucesso, stdout, stderr = executar_comando("python -m buildozer android debug", mostrar_output=True)
    
    if sucesso or os.path.exists("bin"):
        # Verificar se APK foi gerado
        bin_dir = "bin"
        if os.path.exists(bin_dir):
            apks = [f for f in os.listdir(bin_dir) if f.endswith('.apk')]
            if apks:
                print("")
                print("✅✅✅ APK GERADO COM SUCESSO! ✅✅✅")
                print("")
                print("📱 Seu APK está em:")
                for apk in apks:
                    print(f"   📁 bin/{apk}")
                print("")
                print("📲 Para instalar no celular:")
                print("   1. Copie o arquivo .apk para o celular")
                print("   2. Ative 'Fontes desconhecidas' nas configurações")
                print("   3. Toque no arquivo para instalar")
                print("")
                print("🎮 PARABÉNS! Seu RPG épico está pronto!")
                return True
    
    print("")
    print("❌ Erro na compilação!")
    print("💡 Tente usar WSL como alternativa:")
    print("   wsl --install Ubuntu")
    print("   Depois siga o WINDOWS_SETUP.md")
    return False

def main():
    print("🐲 RPG ÉPICO - COMPILADOR APK MELHORADO 🦄")
    print("=" * 55)
    print("")
    
    # Verificar Python
    print("🐍 Verificando Python...")
    try:
        import sys
        print(f"✅ Python {sys.version}")
    except:
        print("❌ Python não encontrado!")
        return
    
    # Verificar e instalar dependências
    print("📦 Verificando dependências...")
    deps = ["buildozer", "cython", "kivy"]
    for dep in deps:
        try:
            __import__(dep)
            print(f"✅ {dep} OK")
        except ImportError:
            print(f"📦 Instalando {dep}...")
            executar_comando(f"pip install {dep}")
    
    print("")
    print("🔧 CONFIGURAÇÃO AUTOMÁTICA:")
    print("   ✅ Android SDK será baixado automaticamente")
    print("   ✅ NDK será configurado automaticamente") 
    print("   ✅ buildozer.spec será criado automaticamente")
    print("")
    
    # Aguardar confirmação
    input("📋 Pressione ENTER para iniciar a compilação automática...")
    print("")
    
    # Compilar APK
    compilar_apk_melhorado()
    
    print("")
    input("Pressione ENTER para sair...")

if __name__ == "__main__":
    main()
