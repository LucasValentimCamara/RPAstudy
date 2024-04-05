$exclude = @("venv", "database_automation.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "database_automation.zip" -Force