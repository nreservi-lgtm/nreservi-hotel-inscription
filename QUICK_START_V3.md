# 🚀 DÉMARRAGE RAPIDE - VERSION 3.0

## ✨ Qu'est-ce qui a changé ?

### 1. 🗺️ Google Maps
- Carte interactive pour positionner l'hôtel
- Clic sur la carte = Latitude + Longitude automatiques
- Plus besoin de chercher les coordonnées GPS !

### 2. 👥 Capacités Adultes ET Enfants
- Au lieu de "min/max personnes" → Maintenant séparé :
  - Min/Max **Adultes**
  - Min/Max **Enfants**
- Exemple: Double = 1-2 adultes + 0-2 enfants

### 3. 🛏️ Lit Supplémentaire Détaillé
- Avant : Checkbox simple
- Maintenant : Type de lit + Prix
  - Matelas / Clic-clac / Canapé-lit / Lit bébé / etc.
  - Prix du supplément en DZD

### 4. 🏨 Nouveaux Types par Défaut
- **Avant :** Simple, Double, Triple, Suite, Appartement
- **Maintenant :** Single, Double, Triple, Quadruple
- (Suite, Appartement peuvent être ajoutés comme "Autres types")

### 5. 📸 Upload de Photos
- Jusqu'à 10 photos directement dans le formulaire
- Preview visuel avant envoi
- Photos converties en base64 et envoyées avec les données

---

## 🎯 Actions Immédiates

### 1. Obtenir Clé Google Maps (10 min)
📄 **Lis : `GOOGLE_MAPS_SETUP.md`**

Résumé ultra-rapide :
1. Va sur https://console.cloud.google.com/
2. Crée un projet "Nreservi Hotel Form"
3. Active "Maps JavaScript API"
4. Créer identifiants → Clé API
5. Copie la clé
6. Restreins aux domaines : `*.github.io/*`
7. Dans `index.html` ligne 6, remplace `YOUR_GOOGLE_MAPS_API_KEY`

**Coût :** GRATUIT (28 000 chargements/mois gratuits)

---

### 2. Tester le Formulaire en Local (5 min)

```bash
# Option 1 : Ouvrir directement dans le navigateur
open index.html

# Option 2 : Serveur local simple
python3 -m http.server 8000
# Puis ouvre: http://localhost:8000
```

**Vérifier :**
- ✅ Carte Google Maps s'affiche
- ✅ Clic sur carte → marqueur apparaît
- ✅ Lat/Long se remplissent automatiquement
- ✅ Cocher "Double" → formulaire apparaît
- ✅ Cocher "Lit supplémentaire" → Type + Prix apparaissent
- ✅ Upload photos → Preview s'affiche

---

### 3. Déployer sur GitHub (5 min)

```bash
cd nreservi-hotel-inscription

# Si première fois
git init
git add .
git commit -m "Version 3.0 - Google Maps, Capacités, Photos"
git remote add origin https://github.com/TON-USERNAME/nreservi-hotel-inscription.git
git push -u origin main

# Si mise à jour
git add .
git commit -m "Version 3.0 - Google Maps, Capacités, Photos"
git push
```

**Activer GitHub Pages :**
1. Settings → Pages
2. Source : Deploy from branch
3. Branch : main / (root)
4. Save

**URL finale :** `https://TON-USERNAME.github.io/nreservi-hotel-inscription/`

---

### 4. Adapter Workflow n8n (30 min)

📄 **Lis : `VERSION_3.0.md`** (section "Impact sur le Système")

**Principales modifications :**

```javascript
// 1. Géolocalisation
const latitude = $json.latitude;
const longitude = $json.longitude;

// 2. Capacités séparées
data.chambres_details.forEach(chambre => {
  const adultes = `${chambre.capacite_min_adultes}-${chambre.capacite_max_adultes}`;
  const enfants = `${chambre.capacite_min_enfants}-${chambre.capacite_max_enfants}`;
  
  // 3. Lit supplémentaire
  if (chambre.lit_supplementaire) {
    const litType = chambre.lit_supp_type;
    const litPrix = chambre.lit_supp_prix;
  }
});

// 4. Photos
if (data.photos && data.photos.length > 0) {
  data.photos.forEach((photo, index) => {
    // Sauvegarder la photo
    // photo.name = nom du fichier
    // photo.data = base64 string
  });
}
```

---

### 5. Adapter Script Python (45 min)

📄 **Le script actuel `hotel_creator.py` doit être mis à jour**

**Principales modifications :**

```python
# 1. Géolocalisation
self._fill_field(page, "latitude", hotel_data.get('latitude'))
self._fill_field(page, "longitude", hotel_data.get('longitude'))

# 2. Capacités séparées (pour chaque type de chambre)
self._fill_field(page, f"{type}_capacite_min_adultes", chambre['capacite_min_adultes'])
self._fill_field(page, f"{type}_capacite_max_adultes", chambre['capacite_max_adultes'])
self._fill_field(page, f"{type}_capacite_min_enfants", chambre['capacite_min_enfants'])
self._fill_field(page, f"{type}_capacite_max_enfants", chambre['capacite_max_enfants'])

# 3. Lit supplémentaire
if chambre.get('lit_supplementaire'):
    self._check_checkbox(page, f"{type}_lit_supp")
    self._select_option(page, f"{type}_lit_supp_type", chambre.get('lit_supp_type'))
    self._fill_field(page, f"{type}_lit_supp_prix", chambre.get('lit_supp_prix'))

# 4. Photos (decode base64 et upload)
if hotel_data.get('photos'):
    for i, photo in enumerate(hotel_data['photos']):
        photo_data = base64.b64decode(photo['data'].split(',')[1])
        # Sauvegarder ou uploader vers Nreservi Pro
```

---

## 📊 Exemple de Données Reçues

```json
{
  "nom_hotel": "Hotel Royal",
  "latitude": "36.753768",
  "longitude": "3.058811",
  "email_reservation": "contact@royal.dz",
  "emails_supplementaires": "resa2@royal.dz",
  
  "chambres_details": [
    {
      "type": "Double",
      "tarif_affiche": "12000",
      "tarif_accorde": "10000",
      "capacite_min_adultes": "1",
      "capacite_max_adultes": "2",
      "capacite_min_enfants": "0",
      "capacite_max_enfants": "2",
      "lit_supplementaire": true,
      "lit_supp_type": "Clic-clac",
      "lit_supp_prix": "2000"
    },
    {
      "type": "Suite Royale",
      "tarif_affiche": "30000",
      "tarif_accorde": "25000",
      "capacite_min_adultes": "2",
      "capacite_max_adultes": "4",
      "capacite_min_enfants": "0",
      "capacite_max_enfants": "3",
      "lit_supplementaire": true,
      "lit_supp_type": "Canapé-lit",
      "lit_supp_prix": "3000"
    }
  ],
  
  "photos": [
    {
      "name": "chambre-double.jpg",
      "data": "data:image/jpeg;base64,/9j/4AAQ..."
    },
    {
      "name": "facade.jpg",
      "data": "data:image/jpeg;base64,/9j/4AAQ..."
    }
  ]
}
```

---

## 📱 Temps de Remplissage

- **V1.0 :** 5 minutes
- **V2.0 :** 8-10 minutes
- **V3.0 :** 10-12 minutes (avec photos et carte)

**Pourquoi ?**
- Positionnement GPS sur carte : +1 min
- Upload de photos : +1-2 min
- Capacités détaillées : +30 sec

**Mais :** Données BEAUCOUP plus riches et exploitables !

---

## 📦 Fichiers Importants

### À Lire en Premier
1. **VERSION_3.0.md** ← Vue d'ensemble complète
2. **GOOGLE_MAPS_SETUP.md** ← Obtenir la clé API (10 min)

### Pour Déployer
3. **DEPLOY.md** ← Push sur GitHub
4. **SETUP.md** ← Configuration n8n + Python

### Pour Tester
5. **TEST_GUIDE.md** ← Scénarios de test

### Code
6. **index.html** ← Formulaire V3.0
7. **hotel_creator.py** ← Script Python (à adapter)
8. **n8n-workflow.json** ← Workflow (à adapter)

---

## ⚠️ Points d'Attention

### Google Maps API
- ✅ Gratuit jusqu'à 28 000 chargements/mois
- ✅ Pour 200 inscriptions : largement suffisant
- ⚠️ IMPORTANT : Restreindre la clé aux domaines autorisés

### Photos Base64
- ⚠️ 10 photos = ~26MB de données
- ⚠️ Peut causer des timeouts sur n8n
- ✅ Solution : Limiter à 5 photos OU compresser avant envoi

### Types de Chambres
- ⚠️ **Breaking change** : Simple → Single
- ⚠️ Mettre à jour le script Python avec les nouveaux noms

### Capacités
- ⚠️ **Breaking change** : 4 champs au lieu de 2
- ⚠️ Adapter n8n et Python pour gérer adultes + enfants séparément

---

## 🎯 Plan d'Action Recommandé

### Aujourd'hui
1. ✅ Obtenir clé Google Maps (10 min)
2. ✅ Tester formulaire en local (5 min)
3. ✅ Déployer sur GitHub (5 min)

### Cette Semaine
4. ✅ Adapter workflow n8n (30 min)
5. ✅ Adapter script Python (45 min)
6. ✅ Test end-to-end complet (20 min)

### Semaine Prochaine
7. ✅ Test pilote avec 2-3 hôteliers
8. ✅ Ajuster selon feedback
9. ✅ Lancer campagne Brevo

---

## 📞 Questions Fréquentes

**Q: Dois-je payer pour Google Maps ?**
R: Non, gratuit jusqu'à 28 000 chargements/mois. Avec 200 inscriptions, tu es largement en dessous.

**Q: Que se passe-t-il si je n'ai pas de clé Google Maps ?**
R: La carte ne s'affichera pas, mais le reste du formulaire fonctionnera. Les champs lat/long resteront vides.

**Q: Les photos sont-elles obligatoires ?**
R: Non, c'est optionnel. L'hôtelier peut soumettre sans photos.

**Q: Combien de types de lits supplémentaires ?**
R: 6 types : Matelas, Lit pliant, Clic-clac, Canapé-lit, Lit bébé, Autre

**Q: Les types Single/Double/Triple remplacent Simple/Double/Triple ?**
R: Oui, c'est la terminologie internationale standard. Plus clair pour tout le monde.

---

## ✅ Checklist Finale

- [ ] Clé Google Maps obtenue
- [ ] Clé ajoutée dans index.html
- [ ] Formulaire testé en local
- [ ] Formulaire déployé sur GitHub Pages
- [ ] Workflow n8n adapté
- [ ] Script Python adapté
- [ ] Test end-to-end réussi
- [ ] Prêt pour campagne pilote !

---

**Version :** 3.0  
**Statut :** ✅ Prêt à déployer  
**Prochaine étape :** Obtenir clé Google Maps

Bonne chance ! 🚀
