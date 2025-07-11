# RPG Épico - Configuração WSL2 para Buildozer
# Execute após instalar WSL2

Write-Host "🐧 Configurando WSL2 para compilação APK..." -ForegroundColor Green

# 1. Verificar se WSL está instalado
$wslStatus = wsl --status 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "📦 Instalando WSL2..." -ForegroundColor Cyan
    
    # Habilitar WSL
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    
    # Habilitar Virtual Machine Platform
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    
    Write-Host "⚠️  Reinicie o computador e execute este script novamente!" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "✅ WSL2 detectado" -ForegroundColor Green

# 2. Instalar Ubuntu no WSL se não existir
$distros = wsl --list --quiet
if ($distros -notcontains "Ubuntu") {
    Write-Host "📦 Instalando Ubuntu no WSL..." -ForegroundColor Cyan
    wsl --install -d Ubuntu
    Write-Host "Configure sua conta Ubuntu e execute este script novamente" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "✅ Ubuntu WSL configurado" -ForegroundColor Green

# 3. Atualizar Ubuntu e instalar dependências
Write-Host "🔄 Configurando ambiente Ubuntu..." -ForegroundColor Cyan

$ubuntuCommands = @"
#!/bin/bash
echo "🔄 Atualizando sistema Ubuntu..."
sudo apt update
sudo apt upgrade -y

echo "📦 Instalando dependências para buildozer..."
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

echo "🐍 Instalando buildozer..."
pip3 install --user buildozer cython

echo "🔧 Configurando variáveis de ambiente..."
echo 'export PATH=\$PATH:\$HOME/.local/bin' >> ~/.bashrc
source ~/.bashrc

echo "✅ Configuração Ubuntu concluída!"
echo "Agora você pode compilar APKs usando WSL"
"@

# Salvar script no WSL
$ubuntuCommands | wsl -d Ubuntu bash

Write-Host "✅ WSL2 configurado com sucesso!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 COMO COMPILAR APK:" -ForegroundColor Yellow
Write-Host "1. wsl" -ForegroundColor White
Write-Host "2. cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version" -ForegroundColor White
Write-Host "3. buildozer android debug" -ForegroundColor White
Write-Host ""
Write-Host "Pressione qualquer tecla para abrir WSL..." -ForegroundColor Gray
pause

# Abrir WSL no diretório do projeto
wsl -d Ubuntu --cd /mnt/c/Users/Admin/Desktop/RPGText/mobile_version
