$exclude = @("venv", "web_scraping.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "web_scraping.zip" -Force