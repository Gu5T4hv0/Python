Write-Host "Teste bloco if"
if (-not (Test-Path "node_modules")) {
    Write-Host "node_modules NAO existe"
} else {
    Write-Host "node_modules existe"
}
Write-Host "Fim do teste"

# Script PowerShell para iniciar o servidor Next.js
Write-Host "Iniciando servidor MicroMentor..."

# Verificar se está no diretório correto
if (-not (Test-Path "package.json")) {
    Write-Host "Erro: package.json nao encontrado!"
    Write-Host "Certifique-se de estar no diretorio apps/web"
    exit 1
}

# Verificar se node_modules existe
if (-not (Test-Path "node_modules")) {
    Write-Host "Instalando dependencias..."
    npm install
} else {
    Write-Host "node_modules ja existe. Pulando instalacao."
}

# Verificar variaveis de ambiente
if (-not (Test-Path ".env.local")) {
    Write-Host "AVISO: Arquivo .env.local nao encontrado!"
    Write-Host "Crie um arquivo .env.local com as variaveis necessarias"
}

Write-Host "Iniciando servidor de desenvolvimento..."
Write-Host "Acesse: http://localhost:3000"
Write-Host "Pressione Ctrl+C para parar o servidor"

npm run dev