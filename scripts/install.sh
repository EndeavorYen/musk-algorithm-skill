#!/usr/bin/env bash
set -euo pipefail

platform="${1:-all}"
case "$platform" in
  grok|claude|cursor|hermes|all) ;;
  *)
    echo "usage: $0 [grok|claude|cursor|hermes|all]" >&2
    exit 2
    ;;
esac

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
skill_src="$repo_root/SKILL.md"
backlog_src="$repo_root/musk-backlog/SKILL.md"
readme_src="$repo_root/README.md"
refs_src="$repo_root/references"
if [[ ! -f "$skill_src" ]]; then
    echo "SKILL.md not found at $skill_src" >&2
    exit 1
fi
if [[ ! -f "$backlog_src" ]]; then
    echo "musk-backlog/SKILL.md not found at $backlog_src" >&2
    exit 1
fi

skills_root_for() {
  local name="$1"
  local home="${HOME}"
  case "$name" in
    grok)
      local root="${GROK_HOME:-$home/.grok}"
      printf '%s\n' "$root/skills"
      ;;
    hermes)
      local root="${HERMES_HOME:-$home/.hermes}"
      printf '%s\n' "$root/skills"
      ;;
    claude) printf '%s\n' "$home/.claude/skills" ;;
    cursor) printf '%s\n' "$home/.cursor/skills" ;;
    *)
      echo "Unknown platform $name" >&2
      return 1
      ;;
  esac
}

install_to() {
  local name="$1"
  local skills dest_algo dest_backlog
  skills="$(skills_root_for "$name")"
  dest_algo="$skills/musk-algorithm"
  dest_backlog="$skills/musk-backlog"
  mkdir -p "$dest_algo"
  cp "$skill_src" "$dest_algo/SKILL.md"
  if [[ -f "$readme_src" ]]; then
    cp "$readme_src" "$dest_algo/README.md"
  fi
  if [[ -d "$refs_src" ]]; then
    rm -rf "$dest_algo/references"
    cp -R "$refs_src" "$dest_algo/references"
  fi
  mkdir -p "$dest_backlog"
  cp "$backlog_src" "$dest_backlog/SKILL.md"
  if [[ -f "$readme_src" ]]; then
    cp "$readme_src" "$dest_backlog/README.md"
  fi
  echo "Installed $name -> $dest_algo"
  echo "Installed $name -> $dest_backlog"
}

if [[ "$platform" == "all" ]]; then
  for t in grok claude cursor hermes; do
    install_to "$t"
  done
else
  install_to "$platform"
fi
