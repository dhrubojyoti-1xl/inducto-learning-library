param([string]$Destination = 'C:\Users\Dhrubo\Desktop\INDUCTO_VISUAL_ASSETS')
$source = Get-Content -LiteralPath (Join-Path (Get-Location) 'build_asset_library.ps1') -Raw
$source = $source.Replace([string][char]96, '')
$source = [regex]::Replace($source, '[^\x00-\x7F]', '-')
Invoke-Expression $source
