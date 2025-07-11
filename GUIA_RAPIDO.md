# 🚀 GUIA RÁPIDO - APK em 5 Minutos

## ⚡ MÉTODO MAIS FÁCIL

### 1. Instalar WSL2:
```powershell
wsl --install
```
*Reinicie o computador se necessário*

### 2. Configurar Ubuntu:
```bash
# No WSL Ubuntu:
sudo apt update
sudo apt install -y python3-pip python3-venv build-essential
pip3 install --user buildozer cython
```

### 3. Compilar APK:
```bash
cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version
buildozer android debug
```

### 4. Resultado:
✅ APK estará em: `bin/rpgepico-1.0.0-arm64-v8a-debug.apk`

## 🎯 COMANDO ÚNICO

Execute isso no **WSL Ubuntu**:
```bash
cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version && sudo apt update && sudo apt install -y python3-pip build-essential && pip3 install --user buildozer cython && buildozer android debug
```

## 📱 INSTALAR NO CELULAR

```bash
# Via USB:
adb install bin/rpgepico-1.0.0-arm64-v8a-debug.apk

# Ou copie o arquivo .apk para o celular e instale manualmente
```

## 🔧 Se Der Erro

### Erro "buildozer not found":
```bash
echo 'export PATH=$PATH:$HOME/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

### Erro de permissão:
```bash
chmod +x main.py
chmod +x buildozer.spec
```

### SDK Android não encontrado:
```bash
# Buildozer baixa automaticamente na primeira execução
# Aguarde o download (pode demorar 15-30 minutos)
```

## ⚡ Script Automático

Execute: `build_easy.bat` para instalação automática!

---

**Seu RPG épico estará rodando no Android em minutos! 🐲📱**
