# 🛠️ Guide de Configuration Complet

## Vue d'Ensemble du Système

```
┌─────────────────┐
│  Campagne Brevo │
│  (Emails aux    │
│   hôteliers)    │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Formulaire Web │ ◄─── https://USERNAME.github.io/nreservi-hotel-inscription
│  (GitHub Pages) │
└────────┬────────┘
         │
         v
┌─────────────────┐
│  Webhook n8n    │ ◄─── https://nreservi.app.n8n.cloud/webhook/inscription-hotel
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Validation &    │
│ Formatting      │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Script Python   │ ◄─── hotel_creator.py (Playwright)
│ (Playwright)    │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Nreservi Pro    │ ◄─── www.nreservi.pro/cr.admin/
│ (Compte saisie) │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Emails          │
│ - Hôtelier      │
│ - Admin         │
└─────────────────┘
```

---

## 📋 Checklist de Configuration

### Phase 1 : Déploiement du Formulaire

- [ ] **1.1** Créer le repo GitHub `nreservi-hotel-inscription`
- [ ] **1.2** Pousser le code (voir DEPLOY.md)
- [ ] **1.3** Activer GitHub Pages
- [ ] **1.4** Tester l'accès au formulaire

**URL finale :** `https://USERNAME.github.io/nreservi-hotel-inscription/`

---

### Phase 2 : Configuration n8n

#### 2.1 Créer le Webhook

1. Dans n8n, créer un nouveau workflow : "Inscription Hotel Nreservi Pro"
2. Ajouter un nœud Webhook
3. Configuration :
   - **Path:** `inscription-hotel`
   - **Method:** POST
   - **Response Mode:** lastNode

L'URL du webhook sera : `https://nreservi.app.n8n.cloud/webhook/inscription-hotel`

#### 2.2 Mettre à Jour le Formulaire

Dans `index.html`, ligne 274, remplacer par l'URL exacte du webhook :

```javascript
const WEBHOOK_URL = 'https://nreservi.app.n8n.cloud/webhook/inscription-hotel';
```

#### 2.3 Importer le Workflow

1. Copier le contenu de `n8n-workflow.json`
2. Dans n8n : Menu > Import from File > Coller le JSON
3. Ajuster les paramètres :
   - Email admin
   - Chemin du script Python
   - Configuration Gmail OAuth

---

### Phase 3 : Installation du Script Python

#### 3.1 Prérequis

```bash
# Installer Python 3.8+
python3 --version

# Installer Playwright
pip3 install playwright --break-system-packages

# Installer les navigateurs
python3 -m playwright install chromium
```

#### 3.2 Configuration du Script

1. Éditer `hotel_creator.py`
2. Ligne 13, remplacer le mot de passe :

```python
self.password = "YOUR_PASSWORD_HERE"  # Le mot de passe du compte saisie.ia
```

**Note :** Tu as déjà ce mot de passe car c'est le même que pour les stop sales !

#### 3.3 Déployer le Script

```bash
# Créer un dossier pour le script sur ton serveur/machine n8n
mkdir -p /home/node/hotel_creator

# Copier le script
cp hotel_creator.py /home/node/hotel_creator/

# Rendre exécutable
chmod +x /home/node/hotel_creator/hotel_creator.py
```

#### 3.4 Tester le Script Manuellement

```bash
cd /home/node/hotel_creator

# Test avec des données fictives
python3 hotel_creator.py '{
  "nom_hotel": "Hotel Test",
  "ville": "Alger",
  "categorie": "3 étoiles",
  "adresse": "123 Rue Test",
  "localisation": "Centre-ville",
  "tel_commercial": "021123456",
  "email_reservation": "test@test.dz",
  "chambres": "Double, Triple",
  "tarif_affiche": "15000",
  "tarif_accorde": "12000",
  "equipements": "WiFi gratuit, Parking"
}'
```

Si tout fonctionne, tu verras :
- Messages de progression
- Screenshots générés
- JSON de résultat final

---

### Phase 4 : Configuration Gmail (pour les emails)

#### 4.1 OAuth Gmail dans n8n

1. Credentials > New
2. Type : Gmail OAuth2 API
3. Suivre les instructions pour créer les credentials Google
4. Autoriser l'envoi d'emails

#### 4.2 Adapter les Templates d'Email

Dans le workflow n8n, personnaliser :

**Email Hôtelier (succès) :**
- Subject : ✅ Inscription confirmée sur Nreservi Pro
- Inclure : nom hôtel, ville, prochaines étapes

**Email Admin :**
- Subject : 🏨 Nouveau hôtel à valider
- Inclure : toutes les infos + lien vers fiche

---

### Phase 5 : Campagne Brevo

#### 5.1 Créer la Campagne Email

1. Brevo > Campaigns > Create an email campaign
2. Template : HTML
3. Copier le contenu de `email-template-brevo.html`
4. Personnaliser :
   - Remplacer `[VOTRE NUMERO]` par ton numéro de téléphone
   - Remplacer l'URL du formulaire

#### 5.2 Configuration de l'Envoi

- **Nom de campagne :** "Inscription Nreservi Pro - Hôteliers"
- **De :** Nreservi <noreply@nreservi.com>
- **Objet :** 🎯 Rejoignez Nreservi Pro - La plateforme N°1 en Algérie

#### 5.3 Liste de Contacts

**Stratégie :**
1. **Semaine 1 :** Collecter 50-100 emails d'hôtels via :
   - Annuaires en ligne
   - Pages Jaunes
   - Google Maps
   - Réseaux sociaux

2. **Semaine 2 :** Enrichir avec infos complémentaires
3. **Semaine 3 :** Première vague (20 hôtels pilote)
4. **Semaine 4+** : Déploiement global (50 emails/jour max)

---

## 🧪 Tests Avant Lancement

### Test 1 : Formulaire → n8n

1. Remplir le formulaire avec des données fictives
2. Vérifier que le webhook n8n reçoit les données
3. Vérifier les logs n8n

### Test 2 : Script Python

1. Exécuter manuellement avec données de test
2. Vérifier la connexion à Nreservi Pro
3. Vérifier la création d'hôtel (ou tentative)

### Test 3 : Emails

1. Tester l'envoi d'email de confirmation
2. Tester l'email de notification admin
3. Vérifier le formatage et les liens

### Test 4 : Flow Complet

1. Remplir le formulaire
2. Attendre le traitement n8n
3. Vérifier la création sur Nreservi Pro
4. Vérifier la réception des emails

---

## 🚨 Troubleshooting

### Problème : Webhook n8n ne reçoit pas les données

**Solution :**
- Vérifier que le workflow est activé
- Vérifier l'URL du webhook dans index.html
- Tester avec curl :

```bash
curl -X POST https://nreservi.app.n8n.cloud/webhook/inscription-hotel \
  -H "Content-Type: application/json" \
  -d '{"nom_hotel":"Test","ville":"Alger"}'
```

### Problème : Script Python échoue

**Solution :**
- Vérifier que Playwright est installé
- Vérifier le mot de passe du compte saisie.ia
- Regarder les screenshots générés pour debug
- Vérifier les URLs de Nreservi Pro

### Problème : Emails non envoyés

**Solution :**
- Vérifier les credentials Gmail OAuth
- Vérifier les quotas d'envoi
- Vérifier les templates d'email

---

## 📊 Monitoring

### Métriques à Suivre

1. **Taux d'ouverture emails** : objectif 30%+
2. **Taux de clic** : objectif 10%+
3. **Taux de complétion formulaire** : objectif 50%+
4. **Taux de création réussie** : objectif 90%+

### Logs à Monitorer

- **n8n :** Executions > Voir les erreurs
- **Python :** Screenshots + logs console
- **Nreservi Pro :** Vérifier les nouvelles fiches

---

## 🔄 Maintenance

### Hebdomadaire

- [ ] Vérifier les hôtels en attente de validation
- [ ] Compléter les localisations GPS et photos
- [ ] Mettre en ligne les fiches validées
- [ ] Envoyer email de mise en ligne aux hôteliers

### Mensuel

- [ ] Analyser les métriques de la campagne
- [ ] Optimiser le template email si besoin
- [ ] Enrichir la base de données d'hôteliers
- [ ] Ajuster le script si changements sur Nreservi Pro

---

## 📞 Support

En cas de problème ou question, tu peux :

1. Vérifier les logs n8n
2. Regarder les screenshots Python
3. Tester manuellement chaque composant
4. Ping moi pour assistance ! 🚀

---

**Version :** 1.0
**Dernière mise à jour :** Février 2026
