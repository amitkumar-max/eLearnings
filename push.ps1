# # # run_server.ps1
# # Write-Host "🚀 Starting E-Learn Django Server..." -ForegroundColor Cyan

# # # (Optional) Virtual environment activate - update name if venv folder name alag hai
# # if (Test-Path ".\venv\Scripts\Activate.ps1") {
# #     & .\venv\Scripts\Activate.ps1
# #     Write-Host "✅ Virtual Environment Activated" -ForegroundColor Green
# # } else {
# #     Write-Host "⚠️  Virtual environment not found! Make sure it's created." -ForegroundColor Yellow
# # }

# # # Run Django server
# # python manage.py runserver



# # update-project.ps1
# param (
#     [string]$msg = "Auto update from PowerShell"
# )

# # Step 1: Go to project folder (agar script same folder me hai to skip kar sakta hai)
# Set-Location "C:\path\to\your\project"

# # Step 2: Git add, commit, push
# git add .
# git commit -m $msg
# git push origin main




# push.ps1
param (
    [string]$msg = "Auto update from PowerShell"
)

# Go to your project folder (actual path)
Set-Location "C:\FULLSTACKS_amit360\E-LEARNINGS"

# Git add, commit, push
git add .
git commit -m $msg
git push origin main
