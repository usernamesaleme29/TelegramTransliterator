# Telegram Latin-to-Cyrillic Transliteration Bot

Un bot Telegram qui convertit automatiquement les caractères latins en caractères cyrilliques visuellement similaires.

## 🚀 Fonctionnalités

- **Translittération automatique** : Convertit les caractères latins en cyrilliques visuellement similaires
- **Respect de la casse** : Préserve les majuscules et minuscules
- **Gestion des erreurs** : Traitement robuste des erreurs avec messages explicites
- **Logging complet** : Surveillance de l'activité du bot
- **Hébergement continu** : Déployé sur Replit pour un fonctionnement 24h/24

## 📋 Prérequis

- Python 3.7+
- Token de bot Telegram (obtenu via @BotFather)
- Compte Replit pour l'hébergement

## 🛠️ Installation

1. **Cloner le projet sur Replit**
2. **Configurer le token Telegram** :
   - Aller dans les "Secrets" de Replit
   - Ajouter une nouvelle clé : `TELEGRAM_TOKEN`
   - Valeur : votre token de bot Telegram

3. **Lancer le bot** :
   ```bash
   python main.py
   ```

## 🔧 Configuration

Le bot utilise les variables d'environnement suivantes :

- `TELEGRAM_TOKEN` : Token du bot Telegram (obligatoire)
- `LOG_LEVEL` : Niveau de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `MAX_MESSAGE_LENGTH` : Longueur maximale des messages (défaut: 4096)

## 📖 Utilisation

1. **Démarrer une conversation** avec le bot
2. **Utiliser les commandes** :
   - `/start` : Message de bienvenue
   - `/help` : Aide et exemples
3. **Envoyer du texte** : Le bot répond automatiquement avec la translittération

## 🔤 Exemples de Translittération

| Latin | Cyrillique |
|-------|-----------|
| hello | неӏӏо |
| WORLD | ШОГӀԂ |
| Test123 | Теѕт123 |
| Mixed CaSe | Міхеԃ СаЅе |

## 📊 Table de Correspondance

Le bot utilise une table de correspondance visuelle :

