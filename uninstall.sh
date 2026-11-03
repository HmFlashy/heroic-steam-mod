#!/usr/bin/env bash
set -e

# ==============================================================================
# Script de désinstallation de Heroic Steam Input Mod
# ==============================================================================

TARGET_DIR="${HOME}/.local/bin"

echo "=== Désinstallation de Heroic Steam Input Mod ==="

if [[ -f "$TARGET_DIR/heroic" ]]; then
    rm -f "$TARGET_DIR/heroic"
    echo "-> Supprimé : $TARGET_DIR/heroic"
fi

if [[ -f "$TARGET_DIR/heroic-steam-runner" ]]; then
    rm -f "$TARGET_DIR/heroic-steam-runner"
    echo "-> Supprimé : $TARGET_DIR/heroic-steam-runner"
fi

echo "✅ Désinstallation terminée. Le comportement par défaut de Heroic est restauré."
