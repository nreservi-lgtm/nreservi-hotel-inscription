# 🏨 Formulaire d'Inscription Hôtel - Nreservi Pro

Formulaire web pour l'inscription automatisée des hôtels sur la plateforme Nreservi Pro.

## 🌐 URL du Formulaire

Une fois déployé sur GitHub Pages, le formulaire sera accessible à :
`https://[votre-username].github.io/nreservi-hotel-inscription/`

## 📋 Fonctionnalités

- ✅ Formulaire responsive (mobile & desktop)
- ✅ Validation des champs obligatoires
- ✅ Design moderne avec dégradés
- ✅ Envoi automatique vers n8n webhook
- ✅ Messages de confirmation/erreur
- ✅ Collecte complète des informations hôtelières

## 🔧 Configuration

### 1. Webhook n8n

Modifier l'URL du webhook dans `index.html` ligne 274 :

```javascript
const WEBHOOK_URL = 'https://nreservi.app.n8n.cloud/webhook/inscription-hotel';
```

### 2. GitHub Pages

1. Aller dans Settings > Pages
2. Source: Deploy from a branch
3. Branch: main / root
4. Sauvegarder

## 📊 Champs Collectés

### Informations Générales
- Nom de l'hôtel *
- Ville *
- Catégorie (étoiles) *
- Description

### Coordonnées
- Adresse complète *
- Code postal
- Localisation (centre-ville/aéroport/zone touristique) *
- Téléphone commercial *
- Téléphone réception
- Email de réservation *

### Chambres et Tarifs
- Types de chambres (Simple, Double, Triple, Suite, Appartement)
- Tarif affiché *
- Tarif accordé *
- Âge maximum des enfants
- Âge des enfants gratuits

### Équipements
- WiFi gratuit
- Parking
- Restaurant
- Piscine
- Salle de sport
- Spa
- Climatisation
- Bar
- Salle de conférence
- Service de chambre
- Accès handicapés
- Réception 24/7

## 🎯 Workflow Complet

```
Formulaire → Webhook n8n → Validation → Script Playwright → Création sur Nreservi Pro → Emails
```

## 📧 Campagne Brevo

Le formulaire est conçu pour être partagé via campagne email Brevo.

## 📝 Notes

- Les champs marqués d'un * sont obligatoires
- La localisation GPS et les photos seront complétées manuellement par l'équipe Nreservi
- Chaque inscription génère un email de confirmation à l'hôtelier et une notification à l'admin

## 🚀 Déploiement

```bash
git add .
git commit -m "Initial commit - Formulaire inscription hôtel"
git push origin main
```

## 📞 Support

Pour toute question : contact@nreservi.com
