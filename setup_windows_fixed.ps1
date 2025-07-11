# RPG Épico - Configuração Windows CORRIGIDA
# Execute como Administrador

Write-Host "🚀 Configurando ambiente Windows para APK..." -ForegroundColor Green

# Verificar administrador
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ Execute como Administrador!" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "✅ Executando como Administrador" -ForegroundColor Green

# 1. Instalar Chocolatey
Write-Host "📦 Instalando Chocolatey..." -ForegroundColor Cyan
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
try {
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "✅ Chocolatey instalado!" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Erro ao instalar Chocolatey: $($_.Exception.Message)" -ForegroundColor Red
}

# 2. Refresh PATH
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# 3. Instalar dependências
$packages = @("python311", "openjdk11", "git", "androidstudio")

foreach ($package in $packages) {
    Write-Host "📦 Instalando $package..." -ForegroundColor Cyan
    try {
        choco install $package -y
        Write-Host "✅ $package instalado!" -ForegroundColor Green
    } catch {
        Write-Host "⚠️ Erro ao instalar $package" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "✅ INSTALAÇÃO CONCLUÍDA!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 PRÓXIMOS PASSOS:" -ForegroundColor Yellow
Write-Host "1. Reinicie o PowerShell" -ForegroundColor White
Write-Host "2. Execute: wsl --install" -ForegroundColor White
Write-Host "3. Configure Ubuntu no WSL" -ForegroundColor White
Write-Host "4. Use o comando: build_easy.bat" -ForegroundColor White
Write-Host ""
pause
