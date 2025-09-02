# # # push.ps1
# # param (
# #     [string]$msg = "Deploy ready"
# # )

# # # Step 1: Go to your project folder
# # $ProjectPath = "C:\FULLSTACKS_amit360\E-LEARNINGS"
# # if (Test-Path $ProjectPath) {
# #     Set-Location $ProjectPath
# #     Write-Host "Navigated to project folder: $ProjectPath" -ForegroundColor Cyan
# # } else {
# #     Write-Host "Project path not found!" -ForegroundColor Red
# #     exit
# # }

# # # Step 2: Git add, commit, push
# # git add .
# # git commit -m $msg
# # git push origin main

# # Write-Host "Code pushed to Git successfully!" -ForegroundColor Cyan



# <#
# .SYNOPSIS
# One-click script to prepare Django project for deployment.
# #>

# param (
#     [string]$commitMsg = "Pre-deploy ready"
# )

# # Step 1: Go to your project folder
# $ProjectPath = "C:\FULLSTACKS_amit360\E-LEARNINGS"
# if (Test-Path $ProjectPath) {
#     Set-Location $ProjectPath
#     Write-Host "📁 Navigated to project folder: $ProjectPath" -ForegroundColor Cyan
# } else {
#     Write-Host "❌ Project path not found!" -ForegroundColor Red
#     exit
# }

# # Step 2: Activate virtual environment
# $VenvPath = ".\.venv\Scripts\Activate.ps1"
# if (Test-Path $VenvPath) {
#     & $VenvPath
#     Write-Host "✅ Virtual Environment Activated" -ForegroundColor Green
# } else {
#     Write-Host "⚠️ Virtual Environment not found. Skipping activation." -ForegroundColor Yellow
# }

# # Step 3: Run migrations
# Write-Host "🔄 Running migrations..." -ForegroundColor Cyan
# python manage.py makemigrations
# python manage.py migrate
# Write-Host "✅ Migrations complete." -ForegroundColor Green

# # Step 4: Collect static files
# Write-Host "🗂️ Collecting static files..." -ForegroundColor Cyan
# python manage.py collectstatic --noinput
# Write-Host "✅ Static files collected." -ForegroundColor Green

# # Step 5: Git add, commit & push
# Write-Host "📤 Pushing code to Git..." -ForegroundColor Cyan
# git add .
# git commit -m $commitMsg
# git push origin main
# Write-Host "🚀 Code pushed successfully!" -ForegroundColor Green


param (
    [string]$msg = "Auto update from PowerShell"
)

# Step 1: Go to your project folder
$ProjectPath = "C:\FULLSTACKS_amit360\E-LEARNINGS"
if (Test-Path $ProjectPath) {
    Set-Location $ProjectPath
    Write-Host "Navigated to project folder: $ProjectPath" -ForegroundColor Cyan
} else {
    Write-Host "Project path not found!" -ForegroundColor Red
    exit
}

# Step 2: Activate virtual environment
$VenvPath = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $VenvPath) {
    & $VenvPath
    Write-Host "Virtual Environment Activated" -ForegroundColor Green
} else {
    Write-Host "Virtual Environment not found. Skipping activation." -ForegroundColor Yellow
}

# Step 3: Run migrations
Write-Host "Running migrations..." -ForegroundColor Cyan
python manage.py makemigrations
python manage.py migrate
Write-Host "Migrations complete." -ForegroundColor Green

# Step 4: Collect static files
Write-Host "Collecting static files..." -ForegroundColor Cyan
python manage.py collectstatic --noinput
Write-Host "Static files collected." -ForegroundColor Green

# Step 5: Git add, commit & push
Write-Host "Pushing code to Git..." -ForegroundColor Cyan
git add .
git commit -m $msg
git push origin main
Write-Host "Code pushed successfully!" -ForegroundColor Green
