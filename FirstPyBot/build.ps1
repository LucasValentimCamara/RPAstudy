$exclude = @("venv", "FirstPyBot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "FirstPyBot.zip" -Force