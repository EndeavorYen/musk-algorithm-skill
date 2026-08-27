#Requires -Version 5.1
param(
    [Parameter(Position = 0)]
    [ValidateSet('grok', 'claude', 'cursor', 'hermes', 'all')]
    [string]$Platform = 'all'
)

$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot
$SkillSrc = Join-Path $RepoRoot 'SKILL.md'
$BacklogSrc = Join-Path $RepoRoot 'musk-backlog\SKILL.md'
$ReadmeSrc = Join-Path $RepoRoot 'README.md'
$RefsSrc = Join-Path $RepoRoot 'references'
if (-not (Test-Path -LiteralPath $SkillSrc)) {
    throw "SKILL.md not found at $SkillSrc"
}
if (-not (Test-Path -LiteralPath $BacklogSrc)) {
    throw "musk-backlog/SKILL.md not found at $BacklogSrc"
}

function Get-UserHome {
    if ($env:USERPROFILE) { return $env:USERPROFILE }
    return $HOME
}

function Get-SkillsRoot([string]$Name) {
    $homeDir = Get-UserHome
    switch ($Name) {
        'grok' {
            $root = if ($env:GROK_HOME) { $env:GROK_HOME } else { Join-Path $homeDir '.grok' }
            return (Join-Path $root 'skills')
        }
        'hermes' {
            $root = if ($env:HERMES_HOME) { $env:HERMES_HOME } else { Join-Path $homeDir '.hermes' }
            return (Join-Path $root 'skills')
        }
        'claude' { return (Join-Path $homeDir '.claude\skills') }
        'cursor' { return (Join-Path $homeDir '.cursor\skills') }
        default { throw "Unknown platform $Name" }
    }
}

function Install-To([string]$Name) {
    $skills = Get-SkillsRoot $Name
    $algo = Join-Path $skills 'musk-algorithm'
    $backlog = Join-Path $skills 'musk-backlog'
    New-Item -ItemType Directory -Force -Path $algo | Out-Null
    Copy-Item -Force -LiteralPath $SkillSrc -Destination (Join-Path $algo 'SKILL.md')
    if (Test-Path -LiteralPath $ReadmeSrc) {
        Copy-Item -Force -LiteralPath $ReadmeSrc -Destination (Join-Path $algo 'README.md')
    }
    if (Test-Path -LiteralPath $RefsSrc) {
        $refsDest = Join-Path $algo 'references'
        if (Test-Path -LiteralPath $refsDest) {
            Remove-Item -LiteralPath $refsDest -Recurse -Force
        }
        Copy-Item -Recurse -LiteralPath $RefsSrc -Destination $refsDest
    }
    New-Item -ItemType Directory -Force -Path $backlog | Out-Null
    Copy-Item -Force -LiteralPath $BacklogSrc -Destination (Join-Path $backlog 'SKILL.md')
    if (Test-Path -LiteralPath $ReadmeSrc) {
        Copy-Item -Force -LiteralPath $ReadmeSrc -Destination (Join-Path $backlog 'README.md')
    }
    Write-Output "Installed $Name -> $algo"
    Write-Output "Installed $Name -> $backlog"
}

$targets = if ($Platform -eq 'all') { @('grok', 'claude', 'cursor', 'hermes') } else { @($Platform) }
foreach ($t in $targets) { Install-To $t }
