# Guide de Déploiement sur Render

## Fichiers nécessaires pour Render

### 1. requirements.txt
Renommez `render_requirements.txt` en `requirements.txt` avant le déploiement :
```
python-telegram-bot==20.8
```

### 2. Commande de démarrage
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

## Étapes de déploiement

1. **Uploadez tous les fichiers** sur votre repository Git
2. **Renommez** `render_requirements.txt` en `requirements.txt`
3. **Connectez** votre repository à Render
4. **Configurez** les variables d'environnement
5. **Déployez** le service

Le bot sera alors hébergé en continu sur Render !