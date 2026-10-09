# Starts the Swing desktop client against a running backend.
#   powershell -ExecutionPolicy Bypass -File scripts\run-frontend.ps1 -Url http://localhost:8080
param(
    [string]$Url = "http://localhost:8080"
)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if (-not (Test-Path out\frontend)) { throw "Run scripts\build.ps1 first" }

& java -cp "out\common;out\frontend" com.shopflow.frontend.Main "--url=$Url"
