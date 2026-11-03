# Heroic Steam Input Mod (heroic-steam-runner)

Ce mod résout le problème historique de **Steam Input**, des manettes Bluetooth (PlayStation DualSense, Switch Pro, etc.) et du suivi de jeu lorsque vous ajoutez des jeux de **Heroic Games Launcher** dans **Steam** sur Linux / Steam Deck.

---

## 🎯 Le problème résolu

Par défaut, quand vous cliquez sur **« Ajouter à Steam »** dans Heroic Games Launcher, Heroic génère un raccourci de type :
```bash
/usr/bin/heroic --no-gui --no-sandbox "heroic://launch?appName=...&runner=..."
```
Ce protocole web envoie une requête à l'application Heroic en arrière-plan et **se ferme immédiatement en 0,2 seconde**.

**Conséquences sous Steam :**
1. ❌ Steam croit que le jeu s'est arrêté aussitôt (« Lancer » ➔ « Arrêter » ➔ revient à « Lancer »).
2. ❌ **Steam Input est instantanément désactivé** : le jeu tourne en tâche de fond mais sans l'émulation manette de Steam (les manettes Bluetooth PS4/PS5 ou Nintendo ne répondent pas dans les jeux Windows).
3. ❌ Le temps de jeu et l'overlay Steam ne fonctionnent pas.

---

## 🚀 La solution : `heroic-steam-runner`

Ce mod installe un intercepteur transparent dans `~/.local/bin/heroic` (qui est prioritaire sur `/usr/bin/heroic` dans le `PATH`) :

1. **Quand vous lancez Heroic normalement** : Il ouvre l'interface officielle de Heroic sans rien changer.
2. **Quand Heroic ajoute un jeu dans Steam** : Heroic cible automatiquement cet exécutable.
3. **Quand Steam lance le jeu** : L'intercepteur attrape `heroic://launch`, charge la configuration du jeu depuis Heroic (préfixe Wine, version de Proton, UMU, GameMode, etc.) et lance le jeu **de manière synchrone** via `legendary` / `gogdl` / `nile`.
4. **Résultat** : Steam reste sur « Arrêter » pendant toute la session de jeu, **Steam Input reste actif à 100 %**, la manette Bluetooth est reconnue immédiatement et le temps de jeu est comptabilisé.

---

## 📦 Installation

### En une ligne (recommandé) :

```bash
git clone https://github.com/HmFlashy/heroic-steam-mod.git ~/.local/share/heroic-steam-mod
bash ~/.local/share/heroic-steam-mod/install.sh
```

---

## 🎮 Utilisation

Une fois installé, **vous n'avez rien de spécial à configurer** :

1. Ouvrez **Heroic Games Launcher**.
2. Sur n'importe quel jeu (Epic Games, GOG, etc.), cliquez sur les trois petits points ➔ **Ajouter à Steam**.
3. Ouvrez **Steam** et cliquez sur **Jouer** :
   - Votre manette fonctionne directement grâce à Steam Input.
   - L'overlay Steam (`Shift + Tab`) est disponible.
   - Quand vous quittez le jeu dans ses menus, Steam revient proprement sur « Jouer ».

---

## 🛠️ Utilisation en ligne de commande

Vous pouvez également lancer n'importe quel jeu Heroic directement depuis votre terminal pour tester :

```bash
# Affiche la liste des jeux installés et leurs identifiants
heroic-steam-runner

# Lancer un jeu directement (ex: Rocket League)
heroic-steam-runner Sugar

# Mode test sans démarrer le jeu
heroic-steam-runner Sugar --dry-run
```

---

## 🗑️ Désinstallation

Pour retirer le mod et revenir au comportement par défaut :

```bash
bash ~/.local/share/heroic-steam-mod/uninstall.sh
```

---

## 📄 Licence

MIT License.
