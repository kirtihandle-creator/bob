# Starts the backend on port 8080 (override with -Port). On first run the user
# store is empty, so a bootstrap admin password is required:
#   powershell -ExecutionPolicy Bypass -File scripts\run-backend.ps1 -AdminPassword "ChangeMe123"
param(
    [int]$Port = 8080,
    [string]$DataDir = "data",
    [string]$AdminPassword = "",
    [string]$Python = "python"
)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if (-not (Test-Path out\backend)) { throw "Run scripts\build.ps1 first" }

$jvmArgs = @(
    "-Dshopflow.port=$Port",
    "-Dshopflow.data=$DataDir",
    "-Dshopflow.python=$Python"
)
if ($AdminPassword -ne "") { $jvmArgs += "-Dshopflow.adminPassword=$AdminPassword" }

& java @jvmArgs -cp "out\common;out\backend" com.shopflow.backend.Main
