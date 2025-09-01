# run_server.ps1
Write-Host "🚀 Starting E-Learn Django Server..." -ForegroundColor Cyan

# (Optional) Virtual environment activate - update name if venv folder name alag hai
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
    Write-Host "✅ Virtual Environment Activated" -ForegroundColor Green
} else {
    Write-Host "⚠️  Virtual environment not found! Make sure it's created." -ForegroundColor Yellow
}

# Run Django server
python manage.py runserver
