# RPG Épico - Configuração Windows para APK
# Execute este script como Administrador no PowerShell

Write-Host "🚀 Configurando ambiente Windows para compilação APK..." -ForegroundColor Green

# Verificar se está executando como administrador
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{
    Write-Host "❌ Este script precisa ser executado como Administrador!" -ForegroundColor Red
    Write-Host "Clique com botão direito no PowerShell e selecione 'Executar como administrador'" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "✅ Executando como Administrador" -ForegroundColor Green

# 1. Instalar Chocolatey (gerenciador de pacotes Windows)
Write-Host "📦 Instalando Chocolatey..." -ForegroundColor Cyan
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Refresh environment
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# 2. Instalar Python 3.11
Write-Host "🐍 Instalando Python 3.11..." -ForegroundColor Cyan
choco install python311 -y

# 3. Instalar Java JDK 11
Write-Host "☕ Instalando Java JDK 11..." -ForegroundColor Cyan
choco install openjdk11 -y

# 4. Instalar Git
Write-Host "📝 Instalando Git..." -ForegroundColor Cyan
choco install git -y

# 5. Instalar Android Studio (inclui Android SDK)
Write-Host "📱 Instalando Android Studio..." -ForegroundColor Cyan
choco install androidstudio -y

# 6. Refresh environment variables
Write-Host "🔄 Atualizando variáveis de ambiente..." -ForegroundColor Cyan
refreshenv

Write-Host "✅ Instalação básica concluída!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 PRÓXIMOS PASSOS MANUAIS:" -ForegroundColor Yellow
Write-Host "1. Abra o Android Studio e configure o SDK" -ForegroundColor White
Write-Host "2. Instale WSL2 para usar buildozer" -ForegroundColor White
Write-Host "3. Execute setup_wsl.ps1 para configurar WSL" -ForegroundColor White
Write-Host ""
Write-Host "Pressione qualquer tecla para continuar..." -ForegroundColor Gray
pause
