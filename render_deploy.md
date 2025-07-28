# Guide de Déploiement sur Render

## Problème de compatibilité résolu

Le bot utilise maintenant des versions compatibles pour Render.

## Fichiers nécessaires pour Render

### 1. requirements.txt
Utilisez `requirements_render.txt` (renommez-le en `requirements.txt`) :
```
python-telegram-bot==20.3
```

### 2. Fichier principal
Utilisez `main_render.py` (renommez-le en `main.py`)

### 3. Commande de démarrage
Dans les paramètres Render, utilisez :
```
python main.py
```

### 3. Variables d'environnement
Ajoutez ces variables dans les paramètres Render :
- `TELEGRAM_TOKEN` : Votre token de bot Telegram

### 4. Configuration Render
- **Runtime** : Python 3.11
- **Build Command** : `pip install -r requirements.txt`
- **Start Command** : `python main.py`
- **Port** : 5000 (pour le serveur keep-alive)

## Structure des fichiers
```
projet/
├── main.py              # Point d'entrée principal
├── bot.py               # Logique du bot Telegram
├── transliterator.py    # Moteur de translittération
├── config.py            # Configuration
├── keep_alive.py        # Serveur HTTP pour maintenir le service actif
├── requirements.txt     # Dépendances Python (renommé depuis render_requirements.txt)
└── README.md            # Documentation
```

## Étapes de déploiement corrigées

### Correction pour l'erreur Render

L'erreur `'Updater' object has no attribute '_Updater__polling_cleanup_cb'` est résolue avec les nouveaux fichiers.

1. **Uploadez tous les fichiers** sur votre repository Git
2. **Remplacez** :
   - `requirements.txt` par le contenu de `requirements_render.txt`
   - `main.py` par le contenu de `main_render.py`
3. **Connectez** votre repository à Render
4. **Configurez** les variables d'environnement (`TELEGRAM_TOKEN`)
5. **Déployez** le service

### Fichiers pour Render

- ✅ `main_render.py` → renommez en `main.py`
- ✅ `requirements_render.txt` → renommez en `requirements.txt`
- ✅ `bot_render.py` → renommez en `bot.py`
- ✅ `config.py` (gardez tel quel)
- ✅ `transliterator.py` (gardez tel quel)
- ✅ `keep_alive.py` (gardez tel quel)

Le bot fonctionnera parfaitement sur Render !