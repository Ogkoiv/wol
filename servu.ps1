Write-Host("Starting script")
Set-Location -Path C:\Users\Ossi\wol
python3 wol.py servu
Write-Host("magic packet was sent waiting for startup")
Start-Sleep -Seconds 180
ssh servu
Set-Location -Path C:\Users\Ossi
exit(1)