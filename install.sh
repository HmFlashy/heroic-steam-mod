#!/usr/bin/env bash
set -e

# ==============================================================================
# Script d'installation de Heroic Steam Input Mod
# ==============================================================================

TARGET_DIR="${HOME}/.local/bin"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Installation de Heroic Steam Input Mod ==="
mkdir -p "$TARGET_DIR"

echo "-> Copie des exécutables dans $TARGET_DIR..."
cp -f "$SCRIPT_DIR/bin/heroic" "$TARGET_DIR/heroic"
cp -f "$SCRIPT_DIR/bin/heroic-steam-runner" "$TARGET_DIR/heroic-steam-runner"
chmod +x "$TARGET_DIR/heroic" "$TARGET_DIR/heroic-steam-runner"

# Vérification du PATH
if [[ ":$PATH:" != *":$TARGET_DIR:"* ]]; then
    echo "ATTENTION: $TARGET_DIR n'est pas présent dans votre variable PATH !"
    echo "Ajoutez la ligne suivante à votre ~/.bashrc ou ~/.zshrc :"
    echo '  export PATH="$HOME/.local/bin:$PATH"'
else
    echo "-> PATH vérifié ($TARGET_DIR est prioritaire)."
fi

echo ""
echo "✅ Installation terminée avec succès !"
echo ""
echo "Utilisation :"
echo "  1. Ouvrez Heroic et cliquez sur 'Ajouter à Steam' sur n'importe quel jeu."
echo "  2. Lancez le jeu depuis Steam : Steam Input et votre manette fonctionneront automatiquement !"
