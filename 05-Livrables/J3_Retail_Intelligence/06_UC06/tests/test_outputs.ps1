$root = Join-Path $PSScriptRoot ".."
$silver = Join-Path $root "data\silver\promotion\_SUCCESS"
$gold = Join-Path $root "data\gold\promotion_summary\_SUCCESS"
$quality = Join-Path $root "quality\promotion_quality\_SUCCESS"
if (-not (Test-Path $silver)) { throw "Sortie Silver absente" }
if (-not (Test-Path $gold)) { throw "Sortie Gold absente" }
if (-not (Test-Path $quality)) { throw "Rapport qualite absent" }
Write-Host "Tests UC06 OK : Silver, Gold et qualite presents"
