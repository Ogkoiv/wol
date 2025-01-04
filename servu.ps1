Write-Host("Starting script")
Set-Location -Path C:\Users\Username\wol
python3 wol.py #MACADDR HERE
Write-Host("magic packet was sent waiting for startup")
Start-Sleep -Seconds 60
ssh #IPADDRHERE
Set-Location -Path C:\Users\Username
exit(1)