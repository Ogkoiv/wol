Write-Host("Starting script")
Set-Location -Path C:\Users\Username\wol
python3 wol.py servu #servu is alias for the ssh connection, use your own connection settings here
Write-Host("magic packet was sent waiting for startup")
Start-Sleep -Seconds 180
ssh servu
Set-Location -Path C:\Users\Username
exit(1)