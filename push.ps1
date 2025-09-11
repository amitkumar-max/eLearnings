param (
    [string]$msg = "Auto update from PowerShell"
)

# Step 1: Navigate to Project Folder
$ProjectPath = "C:\FULLSTACKS_amit360\E-LEARNINGS"
if (Test-Path $ProjectPath) {
    Set-Location $ProjectPath
    Write-Host "Navigated to project folder: $ProjectPath" -ForegroundColor Cyan
} else {
    Write-Host "Project path not found!" -ForegroundColor Red
    exit
}

# Step 2: Activate Virtual Environment
$VenvPath = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $VenvPath) {
    & $VenvPath
    Write-Host "Virtual Environment Activated" -ForegroundColor Green
} else {
    Write-Host "Virtual Environment not found. Skipping activation." -ForegroundColor Yellow
}

# Step 3: (Optional) Run Migrations
$runMigrations = Read-Host "Do you want to run migrations before push? (y/n)"
if ($runMigrations -eq "y") {
    Write-Host "Running migrations..." -ForegroundColor Cyan
    python manage.py makemigrations
    python manage.py migrate
    Write-Host "Migrations complete." -ForegroundColor Green
} else {
    Write-Host "Skipped migrations." -ForegroundColor Yellow
}

# Step 4: Collect Static Files
Write-Host "Collecting static files..." -ForegroundColor Cyan
python manage.py collectstatic --noinput
Write-Host "Static files collected." -ForegroundColor Green

# Step 5: Git Add, Commit, Push
Write-Host "Pushing code to Git..." -ForegroundColor Cyan
git add .
git commit -m $msg
git push origin main
Write-Host "Code pushed successfully!" -ForegroundColor Green



