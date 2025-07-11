# 🚀 RPG Épico - Guia de Instalação Windows

## Você está no Windows! 🪟

Os comandos Linux do README não funcionam no Windows PowerShell. Siga este guia específico para Windows:

## 📋 Opção 1: Setup Automático (Recomendado)

### 1. Execute como Administrador:
```powershell
# Abra PowerShell como Administrador e execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup_windows.ps1
```

### 2. Configure WSL2:
```powershell
# Após reiniciar, execute:
.\setup_wsl.ps1
```

### 3. Compile o APK:

**🚀 OPÇÃO A: GitHub Codespaces (RECOMENDADO)**
```bash
# Método mais fácil - 100% funcional:
# 1. Upload projeto para GitHub
# 2. Abrir GitHub Codespaces
# 3. Executar: ./compile_cloud.sh
# 📖 Veja: COMPILACAO_CLOUD.md
```

**⚡ OPÇÃO B: Solver Automático**
```powershell
# Cria APK demonstração + instruções cloud:
python solve_apk.py
```

**🐧 OPÇÃO C: WSL Ubuntu (Se funcionar)**
```bash
# No WSL Ubuntu:
wsl
cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version
sudo apt update && sudo apt install -y python3-pip build-essential
pip3 install buildozer cython
buildozer android debug
```

**💻 OPÇÃO D: Python Direto (Limitado)**
```powershell
# Pode não funcionar no Windows:
python -m buildozer android debug
```

## 📋 Opção 2: Setup Manual

### 1. Instalar Pré-requisitos:

#### Python 3.11:
- Baixe: https://www.python.org/downloads/
- ✅ Marque "Add Python to PATH"

#### Java JDK 11:
- Baixe: https://adoptopenjdk.net/
- Configure JAVA_HOME

#### Git:
- Baixe: https://git-scm.com/download/win

#### Android Studio:
- Baixe: https://developer.android.com/studio
- Configure Android SDK

### 2. Instalar WSL2:

```powershell
# Execute como Administrador:
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Reinicie o computador
# Depois instale Ubuntu:
wsl --install -d Ubuntu
```

### 3. Configurar Ubuntu WSL:

```bash
# No terminal Ubuntu WSL:
sudo apt update
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

pip3 install --user buildozer cython
echo 'export PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

## 🎯 Compilação Final

```bash
# No WSL Ubuntu:
cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version
buildozer android debug

# APK será gerado em: bin/rpgepico-1.0.0-arm64-v8a-debug.apk
```

## 🔧 Troubleshooting Windows

### Erro "buildozer não encontrado":
```bash
# Verifique instalação:
which buildozer
pip3 install --user buildozer --force-reinstall
```

### Erro de permissão WSL:
```bash
# Ajustar permissões:
chmod +x /mnt/c/Users/Admin/Desktop/RPGText/mobile_version/*
```

### Android SDK não encontrado:
```bash
# Configurar variáveis no WSL:
export ANDROID_HOME=/mnt/c/Users/Admin/AppData/Local/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

## 🚀 Comandos Rápidos

```powershell
# 1. Configurar ambiente (primeira vez):
.\setup_windows.ps1
.\setup_wsl.ps1

# 2. Compilar APK:
wsl
cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version
buildozer android debug

# 3. Instalar no celular:
adb install bin/rpgepico-1.0.0-arm64-v8a-debug.apk
```

## 📱 Resultado

Após seguir estes passos, você terá:
- ✅ Ambiente Windows configurado
- ✅ WSL2 com Ubuntu
- ✅ Buildozer funcionando
- ✅ APK do RPG Épico compilado
- ✅ Pronto para instalar no Android

**Agora você pode jogar seu RPG épico no celular! 🐲📱**
