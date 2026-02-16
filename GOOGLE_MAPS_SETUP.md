# 🗺️ Guide: Obtenir une Clé API Google Maps

## Pourquoi une Clé API ?

Le formulaire V3.0 utilise Google Maps pour permettre aux hôteliers de positionner leur établissement sur une carte interactive. Pour que cette fonctionnalité fonctionne, tu dois obtenir une clé API Google Maps.

---

## 📋 Étapes Détaillées

### Étape 1 : Créer un Projet Google Cloud

1. Va sur https://console.cloud.google.com/
2. Connecte-toi avec ton compte Google (ou crée-en un)
3. Clique sur le sélecteur de projet en haut (à côté de "Google Cloud")
4. Clique sur "**Nouveau projet**"
5. Nom du projet : `Nreservi Hotel Form`
6. Clique sur "**Créer**"
7. Attends quelques secondes que le projet soit créé
8. Sélectionne le nouveau projet

---

### Étape 2 : Activer l'API Maps JavaScript

1. Dans le menu de gauche, va dans "**APIs et services**" → "**Bibliothèque**"
2. Dans la barre de recherche, tape : `Maps JavaScript API`
3. Clique sur "**Maps JavaScript API**"
4. Clique sur le bouton "**Activer**"
5. Attends quelques secondes

---

### Étape 3 : Créer une Clé API

1. Dans le menu de gauche, va dans "**APIs et services**" → "**Identifiants**"
2. En haut, clique sur "**+ Créer des identifiants**"
3. Sélectionne "**Clé API**"
4. Une popup s'affiche avec ta clé : `AIzaSy...`
5. **COPIE cette clé** (tu vas en avoir besoin)
6. Clique sur "**Fermer**" (ne t'inquiète pas, tu pourras la retrouver)

---

### Étape 4 : Restreindre la Clé (IMPORTANT pour la sécurité)

1. Sur la page "Identifiants", tu vois ta clé API dans la liste
2. Clique sur le nom de ta clé
3. **Restrictions relatives aux applications**
   - Sélectionne "**Référents HTTP (sites web)**"
   - Ajouter un élément :
     - `https://[TON-USERNAME].github.io/*`
     - Exemple : `https://musdigital.github.io/*`
   - Clique sur "**Terminé**"

4. **Restrictions relatives aux API**
   - Sélectionne "**Restreindre la clé**"
   - Coche uniquement : `Maps JavaScript API`

5. Clique sur "**Enregistrer**" en bas

---

### Étape 5 : Intégrer la Clé dans le Formulaire

1. Ouvre le fichier `index.html`
2. Trouve la ligne 6 :
   ```html
   <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&libraries=places"></script>
   ```

3. Remplace `YOUR_GOOGLE_MAPS_API_KEY` par ta vraie clé :
   ```html
   <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyXXXXXXXXXXXXXXXXXXXX&libraries=places"></script>
   ```

4. Sauvegarde le fichier

5. Pousse sur GitHub :
   ```bash
   git add index.html
   git commit -m "Ajout clé Google Maps API"
   git push
   ```

---

## 💰 Tarification Google Maps

### Gratuit
- **28 000 chargements de carte par mois** GRATUITS
- Pour 200 inscriptions d'hôtels : largement suffisant !

### Payant (si dépassement)
- $7 pour 1000 chargements supplémentaires
- Mais avec 200 inscriptions, tu ne dépasseras jamais

### Exemple de Calcul
- 200 hôteliers remplissent le formulaire = 200 chargements
- 200 << 28 000 → **100% GRATUIT** ✅

---

## 🔒 Sécurité

### ✅ Restrictions Recommandées

**Référents HTTP :**
- `https://[TON-USERNAME].github.io/*`
- `http://localhost:8000/*` (pour tests en local)

**API :**
- Uniquement "Maps JavaScript API"

**Pourquoi c'est important ?**
- Évite que quelqu'un vole ta clé et l'utilise sur son site
- Limite les coûts en cas d'utilisation non autorisée
- Sécurise ton compte Google Cloud

### ❌ À NE PAS FAIRE

- Ne partage JAMAIS ta clé API publiquement
- Ne la mets pas dans un email
- Ne la commite pas dans GitHub si le repo est public (c'est OK pour un repo privé)

---

## 🧪 Tester la Clé

### Test 1 : Formulaire en Local

1. Ouvre `index.html` dans ton navigateur
2. Scroll jusqu'à la section "Positionnement sur Google Maps"
3. Tu devrais voir une carte centrée sur Alger
4. Clique sur la carte → Un marqueur apparaît
5. Les champs Latitude et Longitude se remplissent automatiquement

✅ **Si ça marche : La clé est bonne !**  
❌ **Si la carte ne s'affiche pas :** Vérifie la clé et les restrictions

### Test 2 : Formulaire sur GitHub Pages

1. Pousse ton code sur GitHub
2. Ouvre l'URL GitHub Pages : `https://[TON-USERNAME].github.io/nreservi-hotel-inscription/`
3. Teste la carte comme ci-dessus

---

## 🐛 Dépannage

### Problème : "This page can't load Google Maps correctly"

**Solution :**
- Vérifie que la clé est bien copiée dans index.html
- Vérifie qu'il n'y a pas d'espace avant ou après la clé
- Vérifie que l'API "Maps JavaScript API" est activée

### Problème : Carte grise avec message d'erreur

**Solution :**
- Vérifie les restrictions de référents HTTP
- Assure-toi que ton domaine GitHub Pages est autorisé
- Exemple : `https://musdigital.github.io/*`

### Problème : "This API project is not authorized to use this API"

**Solution :**
- Va dans "APIs et services" → "Bibliothèque"
- Recherche "Maps JavaScript API"
- Clique dessus et vérifie qu'elle est bien "Activée"

---

## 📊 Monitoring de l'Utilisation

### Suivre la Consommation

1. Va sur https://console.cloud.google.com/
2. Sélectionne ton projet "Nreservi Hotel Form"
3. Menu "**APIs et services**" → "**Tableau de bord**"
4. Tu verras le nombre de requêtes par jour

### Configurer des Alertes (Optionnel)

1. Menu "**Facturation**" → "**Budgets et alertes**"
2. Créer un budget
3. Montant : $0 (pour être alerté dès le premier centime)
4. Ajouter ton email pour les notifications

---

## ✅ Checklist Complète

- [ ] Projet Google Cloud créé
- [ ] Maps JavaScript API activée
- [ ] Clé API créée
- [ ] Restrictions HTTP configurées (github.io)
- [ ] Restrictions API configurées (Maps JavaScript API only)
- [ ] Clé copiée dans index.html ligne 6
- [ ] Fichier sauvegardé et poussé sur GitHub
- [ ] Test en local : Carte s'affiche ✅
- [ ] Test sur GitHub Pages : Carte s'affiche ✅
- [ ] Marqueur positionnable ✅
- [ ] Lat/Long se remplissent ✅

---

## 🆘 Besoin d'Aide ?

Si tu rencontres un problème :

1. Vérifie d'abord la console JavaScript du navigateur (F12)
2. Regarde s'il y a des erreurs liées à Google Maps
3. Vérifie que ta clé est bien formatée (pas d'espaces)
4. Vérifie les restrictions de domaine

---

**Temps estimé :** 10-15 minutes  
**Coût :** $0 (gratuit jusqu'à 28 000 requêtes/mois)  
**Difficulté :** ⭐⭐☆☆☆ (Facile)

Bonne configuration ! 🗺️
