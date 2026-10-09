# Compiles all three modules into out/. Run from the shopflow directory:
#   powershell -ExecutionPolicy Bypass -File scripts\build.ps1
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

New-Item -ItemType Directory -Force -Path out\common, out\backend, out\frontend | Out-Null

function Compile($name, $classpath) {
    $sources = Get-ChildItem -Recurse -Filter *.java -Path "$name\src" | ForEach-Object { $_.FullName }
    Write-Host "Compiling $name ($($sources.Count) files)..."
    $listFile = "out\$name-sources.txt"
    $sources | Set-Content -Encoding ascii $listFile
    # serial/this-escape are noise for Swing classes that are never serialized.
    $lint = "-Xlint:all,-serial,-this-escape"
    if ($classpath) {
        & javac $lint -Werror -cp $classpath -d "out\$name" "@$listFile"
    } else {
        & javac $lint -Werror -d "out\$name" "@$listFile"
    }
    if ($LASTEXITCODE -ne 0) { throw "$name failed to compile" }
}

Compile "common" $null
Compile "backend" "out\common"
Compile "frontend" "out\common"
Write-Host "Build OK."
