#Requires -Version 5.1
param(
    [Parameter(Position = 0)]
    [ValidateSet('grok', 'claude', 'cursor', 'hermes', 'all')]
    [string]$Platform = 'all'
)

$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot
$SkillSrc = Join-Path $RepoRoot 'SKILL.md'
$ReadmeSrc = Join-Path $RepoRoot 'README.md'
$RefsSrc = Join-Path $RepoRoot 'references'
if (-not (Test-Path -LiteralPath $SkillSrc)) {
    throw "SKILL.md not found at $SkillSrc"
}

function Get-UserHome {
    if ($env:USERPROFILE) { return $env:USERPROFILE }
    return $HOME
}

function Get-Dest([string]$Name) {
    $homeDir = Get-UserHome
    switch ($Name) {
        'grok' {
            $root = if ($env:GROK_HOME) { $env:GROK_HOME } else { Join-Path $homeDir '.grok' }
            return (Join-Path $root 'skills\musk-algorithm')
        }
        'hermes' {
            $root = if ($env:HERMES_HOME) { $env:HERMES_HOME } else { Join-Path $homeDir '.hermes' }
            return (Join-Path $root 'skills\musk-algorithm')
        }
        'claude' { return (Join-Path $homeDir '.claude\skills\musk-algorithm') }
        'cursor' { return (Join-Path $homeDir '.cursor\skills\musk-algorithm') }
        default { throw "Unknown platform $Name" }
    }
}

function Install-To([string]$Name) {
    $dest = Get-Dest $Name
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item -Force -LiteralPath $SkillSrc -Destination (Join-Path $dest 'SKILL.md')
    if (Test-Path -LiteralPath $ReadmeSrc) {
        Copy-Item -Force -LiteralPath $ReadmeSrc -Destination (Join-Path $dest 'README.md')
    }
    if (Test-Path -LiteralPath $RefsSrc) {
        $refsDest = Join-Path $dest 'references'
        if (Test-Path -LiteralPath $refsDest) {
            Remove-Item -LiteralPath $refsDest -Recurse -Force
        }
        Copy-Item -Recurse -LiteralPath $RefsSrc -Destination $refsDest
    }
    Write-Output "Installed $Name -> $dest"
}

$targets = if ($Platform -eq 'all') { @('grok', 'claude', 'cursor', 'hermes') } else { @($Platform) }
foreach ($t in $targets) { Install-To $t }
