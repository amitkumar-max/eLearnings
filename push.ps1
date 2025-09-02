# push.ps1
param (
    [string]$msg = "Deploy ready"
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

# Step 2: Git add, commit, push
git add .
git commit -m $msg
git push origin main

Write-Host "Code pushed to Git successfully!" -ForegroundColor Cyan
