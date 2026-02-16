# 🚀 VERSION 3.0 - Améliorations Majeures

## 🆕 Nouvelles Fonctionnalités

### 1. 🗺️ **Positionnement Google Maps** (NOUVEAU!)

**Fonctionnalité :**
- Carte interactive Google Maps intégrée dans le formulaire
- L'hôtelier clique sur la carte pour positionner son hôtel
- Marqueur draggable (déplaçable) pour ajuster la position
- Latitude et longitude capturées automatiquement

**Données retournées :**
```json
{
  "latitude": "36.753768",
  "longitude": "3.058811"
}
```

**Avantages :**
- ✅ Positionnement GPS précis de l'hôtel
- ✅ Plus besoin de saisir manuellement lat/long
- ✅ Interface intuitive et visuelle
- ✅ Géolocalisation exacte pour NIA et clients

**Configuration requise :**
- Clé API Google Maps (ligne 6 de index.html)
- Remplacer `YOUR_GOOGLE_MAPS_API_KEY` par ta vraie clé

---

### 2. 👥 **Capacités Adultes ET Enfants Séparées** (AMÉLIORÉ!)

**AVANT (V2.0) :**
```json
{
  "capacite_min": "1",
  "capacite_max": "2"
}
```

**MAINTENANT (V3.0) :**
```json
{
  "capacite_min_adultes": "1",
  "capacite_max_adultes": "2",
  "capacite_min_enfants": "0",
  "capacite_max_enfants": "1"
}
```

**Pourquoi c'est important :**
- ✅ Distinction claire adultes vs enfants
- ✅ Permet de calculer le prix exact selon la composition
- ✅ Tarification différenciée pour les enfants
- ✅ Gestion précise des réservations familiales

**Exemple réaliste :**
- Chambre Double Standard :
  - Min adultes : 1, Max adultes : 2
  - Min enfants : 0, Max enfants : 2
  - → Peut accueillir 2 adultes + 2 enfants

---

### 3. 🛏️ **Lit Supplémentaire Détaillé** (AMÉLIORÉ!)

**AVANT (V2.0) :**
```json
{
  "lit_supplementaire": true
}
```

**MAINTENANT (V3.0) :**
```json
{
  "lit_supplementaire": true,
  "lit_supp_type": "Clic-clac",
  "lit_supp_prix": "2000"
}
```

**Types de lits disponibles :**
- Matelas
- Lit pliant
- Clic-clac
- Canapé-lit
- Lit bébé
- Autre

**Avantages :**
- ✅ Tarification précise du lit supplémentaire
- ✅ Information claire pour le client
- ✅ Meilleure gestion des surcharges
- ✅ Transparence sur le type de lit

**Exemple :**
- Chambre Triple + Clic-clac (2000 DZD) = 4 personnes possibles

---

### 4. 🏨 **Nouveaux Types de Chambres par Défaut** (CHANGÉ!)

**AVANT (V2.0) :** Simple, Double, Triple, Suite, Appartement

**MAINTENANT (V3.0) :**
- ✅ **Single** (chambre 1 personne)
- ✅ **Double** (chambre 2 personnes)
- ✅ **Triple** (chambre 3 personnes)
- ✅ **Quadruple** (chambre 4 personnes)

**Pourquoi ce changement :**
- Terminologie internationale standard
- Plus clair pour les clients étrangers
- Cohérent avec les plateformes comme Booking.com, Expedia
- Suite et Appartement peuvent être ajoutés comme "Autres types"

---

### 5. 📸 **Upload de Photos** (NOUVEAU!)

**Fonctionnalité :**
- Input file avec support multi-upload (max 10 photos)
- Preview visuel des photos sélectionnées
- Photos converties en base64 et envoyées avec le formulaire
- Numérotation automatique des photos

**Données retournées :**
```json
{
  "photos": [
    {
      "name": "chambre-double.jpg",
      "data": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
    },
    {
      "name": "facade-hotel.jpg",
      "data": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
    }
  ]
}
```

**Avantages :**
- ✅ Photos jointes directement lors de l'inscription
- ✅ Moins d'allers-retours avec l'hôtelier
- ✅ Validation visuelle immédiate par l'équipe
- ✅ Preview pour l'hôtelier avant envoi

**Limitation :**
- Maximum 10 photos par inscription
- Limite de poids gérée par le navigateur
- Format : image/* (jpg, png, webp, etc.)

---

## 📊 Exemple Complet de Données V3.0

```json
{
  "nom_hotel": "Hotel Royal",
  "ville": "Alger",
  "categorie": "4 étoiles",
  "description": "Hôtel moderne au cœur d'Alger",
  "adresse": "123 Rue Didouche Mourad",
  "code_postal": "16000",
  "localisation": "Centre-ville",
  
  "latitude": "36.753768",
  "longitude": "3.058811",
  
  "tel_commercial": "021123456",
  "tel_reception": "021654321",
  "email_reservation": "reservation@royal.dz",
  "emails_supplementaires": "resa2@royal.dz, groupe@royal.dz",
  
  "chambres_types": "Double, Triple, Quadruple",
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
      "type": "Triple",
      "tarif_affiche": "15000",
      "tarif_accorde": "12500",
      "capacite_min_adultes": "2",
      "capacite_max_adultes": "3",
      "capacite_min_enfants": "0",
      "capacite_max_enfants": "2",
      "lit_supplementaire": false
    },
    {
      "type": "Quadruple",
      "tarif_affiche": "18000",
      "tarif_accorde": "15000",
      "capacite_min_adultes": "2",
      "capacite_max_adultes": "4",
      "capacite_min_enfants": "0",
      "capacite_max_enfants": "2",
      "lit_supplementaire": true,
      "lit_supp_type": "Matelas",
      "lit_supp_prix": "1500"
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
  
  "age_max_enfants": "12",
  "age_enfants_gratuits": "6",
  
  "equipements": "WiFi gratuit, Parking, Restaurant, Piscine, Ascenseur, Salle de réunion, Climatisation, Réception 24/7",
  
  "photos": [
    {
      "name": "chambre-double.jpg",
      "data": "data:image/jpeg;base64,..."
    },
    {
      "name": "facade.jpg",
      "data": "data:image/jpeg;base64,..."
    },
    {
      "name": "piscine.jpg",
      "data": "data:image/jpeg;base64,..."
    }
  ],
  
  "date_inscription": "2026-02-16T11:00:00.000Z",
  "statut": "En attente de validation"
}
```

---

## 🔄 Évolution des Versions

### V1.0 → V2.0
- ✅ Emails multiples
- ✅ Tarifs par type de chambre
- ✅ Autres types personnalisés
- ✅ Nouveaux équipements

### V2.0 → V3.0
- ✅ Google Maps (lat/long)
- ✅ Capacités adultes ET enfants séparées
- ✅ Lit supplémentaire détaillé (type + prix)
- ✅ Types par défaut: Single/Double/Triple/Quadruple
- ✅ Upload de photos

---

## 🎯 Impact sur le Système

### Workflow n8n

**Nouvelles données à traiter :**
1. **Latitude/Longitude** : Stocker dans la fiche hôtel
2. **Capacités séparées** : 4 champs au lieu de 2 par chambre
3. **Lit supplémentaire** : Type + Prix (conditionnels)
4. **Photos** : Array de fichiers base64 à sauvegarder

**Code n8n mis à jour nécessaire :**
```javascript
// Traiter les chambres
data.chambres_details.forEach(chambre => {
  // Capacités
  console.log(`Adultes: ${chambre.capacite_min_adultes}-${chambre.capacite_max_adultes}`);
  console.log(`Enfants: ${chambre.capacite_min_enfants}-${chambre.capacite_max_enfants}`);
  
  // Lit supp
  if (chambre.lit_supplementaire) {
    console.log(`Lit supp: ${chambre.lit_supp_type} (+${chambre.lit_supp_prix} DZD)`);
  }
});

// Traiter les photos
if (data.photos && data.photos.length > 0) {
  data.photos.forEach((photo, index) => {
    // Sauvegarder la photo (decode base64, upload vers serveur, etc.)
    console.log(`Photo ${index + 1}: ${photo.name}`);
  });
}

// Géolocalisation
console.log(`Position: ${data.latitude}, ${data.longitude}`);
```

---

### Script Python

**Adaptations nécessaires :**

1. **Capacités séparées**
```python
# Au lieu de
self._fill_field(page, "capacite_min", chambre['capacite_min'])

# Maintenant
self._fill_field(page, "capacite_min_adultes", chambre['capacite_min_adultes'])
self._fill_field(page, "capacite_max_adultes", chambre['capacite_max_adultes'])
self._fill_field(page, "capacite_min_enfants", chambre['capacite_min_enfants'])
self._fill_field(page, "capacite_max_enfants", chambre['capacite_max_enfants'])
```

2. **Lit supplémentaire**
```python
if chambre.get('lit_supplementaire'):
    self._check_checkbox(page, f"{type}_lit_supp")
    self._select_option(page, f"{type}_lit_supp_type", chambre.get('lit_supp_type'))
    self._fill_field(page, f"{type}_lit_supp_prix", chambre.get('lit_supp_prix'))
```

3. **Géolocalisation**
```python
self._fill_field(page, "latitude", hotel_data.get('latitude'))
self._fill_field(page, "longitude", hotel_data.get('longitude'))
```

4. **Photos**
```python
# Sauvegarder les photos sur le serveur
if hotel_data.get('photos'):
    for i, photo in enumerate(hotel_data['photos']):
        # Decoder base64
        photo_data = base64.b64decode(photo['data'].split(',')[1])
        # Sauvegarder
        with open(f"/tmp/{hotel_data['nom_hotel']}_photo_{i+1}.jpg", 'wb') as f:
            f.write(photo_data)
        # Upload vers Nreservi Pro (selon leur système)
```

---

## ⚙️ Configuration Requise

### Google Maps API Key

**Étape 1 : Obtenir une clé API**
1. Aller sur https://console.cloud.google.com/
2. Créer un nouveau projet ou sélectionner un projet existant
3. Activer "Maps JavaScript API"
4. Créer des identifiants → Clé API
5. Copier la clé

**Étape 2 : Configurer dans le formulaire**
Fichier `index.html`, ligne 6 :
```html
<script src="https://maps.googleapis.com/maps/api/js?key=VOTRE_CLE_ICI&libraries=places"></script>
```

**Étape 3 : Restreindre l'utilisation (optionnel mais recommandé)**
- Restriction par domaine : *.github.io/*
- Restriction par API : Maps JavaScript API

---

## 📱 Expérience Utilisateur

### Temps de Remplissage
- **V1.0 :** 5 minutes
- **V2.0 :** 8-10 minutes
- **V3.0 :** 10-12 minutes (avec photos et positionnement GPS)

**Pourquoi plus long ?**
- Positionnement sur la carte : +1 min
- Upload de photos : +1-2 min
- Capacités détaillées : +30 sec
- Mais BEAUCOUP plus complet et précis !

### Nouveautés UX

✅ **Carte interactive**
- Zoom, déplacement
- Clic pour placer le marqueur
- Drag & drop du marqueur
- Mise à jour auto des coordonnées

✅ **Upload photos**
- Drag & drop (si navigateur supporté)
- Preview avant envoi
- Numérotation automatique
- Limite visuelle à 10 photos

✅ **Lit supplémentaire conditionnel**
- Section masquée par défaut
- Apparaît seulement si checkbox cochée
- Type + Prix dans une sous-section claire

---

## 🚀 Déploiement V3.0

### Checklist

**1. Configuration Google Maps** (5 min)
- [ ] Obtenir clé API Google Maps
- [ ] Remplacer dans index.html ligne 6
- [ ] Tester la carte

**2. Push GitHub** (2 min)
- [ ] Pousser la nouvelle version
- [ ] Vérifier GitHub Pages

**3. Adapter n8n** (30 min)
- [ ] Traiter latitude/longitude
- [ ] Traiter capacités adultes/enfants
- [ ] Traiter lit_supp_type et lit_supp_prix
- [ ] Traiter les photos (base64 → fichiers)

**4. Adapter Script Python** (45 min)
- [ ] Champs capacités séparées
- [ ] Champs lit supplémentaire détaillés
- [ ] Géolocalisation
- [ ] Gestion des photos

**5. Tests** (20 min)
- [ ] Test complet formulaire
- [ ] Test Google Maps
- [ ] Test upload photos
- [ ] Test flow end-to-end

---

## 📞 Points d'Attention

### ⚠️ Google Maps API

**Coût :**
- Gratuit jusqu'à 28 000 chargements de carte/mois
- Au-delà : $7 pour 1000 chargements
- Pour 200 inscriptions : largement dans le gratuit

**Fallback si pas de clé :**
- La carte ne s'affichera pas
- Les champs lat/long seront vides
- Le reste du formulaire fonctionnera normalement

### ⚠️ Photos Base64

**Taille :**
- Photos base64 ≈ +33% de taille
- 10 photos de 2MB chacune = ~26MB en base64
- Peut causer des timeouts sur n8n

**Solution :**
- Compresser les photos côté client avant base64
- Ou limiter à 5 photos
- Ou passer par un upload serveur direct (plus complexe)

### ⚠️ Compatibilité Navigateurs

**Google Maps :** Tous les navigateurs modernes  
**File Upload :** Tous les navigateurs modernes  
**Drag & Drop photos :** Chrome, Firefox, Safari (pas IE11)

---

## 📈 Prochaines Améliorations Possibles (V4.0)

1. **Compression photos client-side** (avant base64)
2. **Recherche d'adresse** dans Google Maps (autocomplete)
3. **Drag & drop pour upload photos**
4. **Validation temps réel** (tarifs cohérents, capacités logiques)
5. **Sauvegarde brouillon** (localStorage pour ne pas perdre les données)
6. **Multi-langues** (FR/EN/AR)

---

**Version :** 3.0  
**Date :** 16 Février 2026  
**Statut :** ✅ Prêt à tester  
**Breaking Changes :** Oui (capacités, types de chambres, lit supp)  
**Nécessite :** Clé Google Maps API
