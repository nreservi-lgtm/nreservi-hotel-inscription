# 🧪 Guide de Test du Nouveau Formulaire

## 📋 Scénarios de Test

### Test 1 : Hôtel Simple (3 types de chambres)

**Données à saisir :**

**Informations Générales**
- Nom : Hôtel Aurassi
- Ville : Alger
- Catégorie : 5 étoiles
- Description : Hôtel 5 étoiles au cœur d'Alger avec vue panoramique

**Coordonnées**
- Adresse : 1 Avenue Mohamed Khemisti
- Code postal : 16000
- Localisation : Centre-ville
- Tél Commercial : 021748282
- Tél Réception : 021748283
- Email principal : reservation@aurassi.dz
- Cliquer "Ajouter un email" → commercial@aurassi.dz
- Cliquer "Ajouter un email" → groupe@aurassi.dz

**Chambres**
- ☑️ Cocher "Double"
  - Tarif affiché : 15000
  - Tarif accordé : 12000
  - Capacité min : 1
  - Capacité max : 2
  - ☑️ Lit supplémentaire

- ☑️ Cocher "Suite"
  - Tarif affiché : 35000
  - Tarif accordé : 28000
  - Capacité min : 2
  - Capacité max : 4
  - ☐ Lit supplémentaire

- ☑️ Cocher "Appartement"
  - Tarif affiché : 50000
  - Tarif accordé : 42000
  - Capacité min : 2
  - Capacité max : 6
  - ☑️ Lit supplémentaire

**Âges enfants**
- Âge max enfants : 12
- Âge enfants gratuits : 6

**Équipements**
- ☑️ WiFi gratuit
- ☑️ Parking
- ☑️ Restaurant
- ☑️ Piscine
- ☑️ Salle de sport
- ☑️ Spa
- ☑️ Climatisation
- ☑️ Bar
- ☑️ Salle de conférence
- ☑️ Salle de réunion
- ☑️ Ascenseur
- ☑️ Service de chambre
- ☑️ Accès handicapés
- ☑️ Réception 24/7

**Résultat attendu :**
```json
{
  "nom_hotel": "Hôtel Aurassi",
  "ville": "Alger",
  "categorie": "5 étoiles",
  "email_reservation": "reservation@aurassi.dz",
  "emails_supplementaires": "commercial@aurassi.dz, groupe@aurassi.dz",
  "chambres_types": "Double, Suite, Appartement",
  "chambres_details": [
    {
      "type": "Double",
      "tarif_affiche": "15000",
      "tarif_accorde": "12000",
      "capacite_min": "1",
      "capacite_max": "2",
      "lit_supplementaire": true
    },
    {
      "type": "Suite",
      "tarif_affiche": "35000",
      "tarif_accorde": "28000",
      "capacite_min": "2",
      "capacite_max": "4",
      "lit_supplementaire": false
    },
    {
      "type": "Appartement",
      "tarif_affiche": "50000",
      "tarif_accorde": "42000",
      "capacite_min": "2",
      "capacite_max": "6",
      "lit_supplementaire": true
    }
  ],
  "equipements": "WiFi gratuit, Parking, Restaurant, Piscine, Salle de sport, Spa, Climatisation, Bar, Salle de conférence, Salle de réunion, Ascenseur, Service de chambre, Accès handicapés, Réception 24/7"
}
```

---

### Test 2 : Hôtel avec Types Personnalisés

**Données à saisir :**

**Informations Générales**
- Nom : Maison d'Hôtes Dar Dzayer
- Ville : Tlemcen
- Catégorie : 3 étoiles
- Description : Maison d'hôtes authentique style mauresque

**Coordonnées**
- Adresse : 15 Rue Bab El Djiad
- Code postal : 13000
- Localisation : Centre-ville
- Tél Commercial : 043267890
- Email principal : contact@dardzayer.dz

**Chambres**
- ☑️ Cocher "Simple"
  - Tarif affiché : 6000
  - Tarif accordé : 5000
  - Capacité min : 1
  - Capacité max : 1
  - ☐ Lit supplémentaire

- ☑️ Cocher "Double"
  - Tarif affiché : 9000
  - Tarif accordé : 7500
  - Capacité min : 1
  - Capacité max : 2
  - ☑️ Lit supplémentaire

- Cliquer "Ajouter un autre type de chambre"
  - Nom : Chambre Familiale
  - Tarif affiché : 12000
  - Tarif accordé : 10000
  - Capacité min : 3
  - Capacité max : 5
  - ☑️ Lit supplémentaire

- Cliquer "Ajouter un autre type de chambre"
  - Nom : Suite Royale Mauresque
  - Tarif affiché : 20000
  - Tarif accordé : 17000
  - Capacité min : 2
  - Capacité max : 4
  - ☐ Lit supplémentaire

**Équipements**
- ☑️ WiFi gratuit
- ☑️ Parking
- ☑️ Restaurant
- ☑️ Climatisation
- ☑️ Réception 24/7

**Résultat attendu :**
```json
{
  "nom_hotel": "Maison d'Hôtes Dar Dzayer",
  "ville": "Tlemcen",
  "categorie": "3 étoiles",
  "chambres_types": "Simple, Double",
  "chambres_details": [
    {
      "type": "Simple",
      "tarif_affiche": "6000",
      "tarif_accorde": "5000",
      "capacite_min": "1",
      "capacite_max": "1",
      "lit_supplementaire": false
    },
    {
      "type": "Double",
      "tarif_affiche": "9000",
      "tarif_accorde": "7500",
      "capacite_min": "1",
      "capacite_max": "2",
      "lit_supplementaire": true
    },
    {
      "type": "Chambre Familiale",
      "tarif_affiche": "12000",
      "tarif_accorde": "10000",
      "capacite_min": "3",
      "capacite_max": "5",
      "lit_supplementaire": true
    },
    {
      "type": "Suite Royale Mauresque",
      "tarif_affiche": "20000",
      "tarif_accorde": "17000",
      "capacite_min": "2",
      "capacite_max": "4",
      "lit_supplementaire": false
    }
  ]
}
```

---

### Test 3 : Hôtel Minimal (validation)

**Objectif :** Tester que les champs obligatoires fonctionnent

**Données à saisir :**
- Nom : Hotel Test
- Ville : Alger
- Catégorie : 3 étoiles
- Adresse : Test Address
- Localisation : Centre-ville
- Tél Commercial : 021123456
- Email : test@test.dz
- ☑️ Cocher au moins "Double" (sans remplir les détails)

**Cliquer sur "Envoyer"**

**Résultat attendu :**
- Le formulaire s'envoie avec succès
- Les champs de tarifs vides sont acceptés (valeurs vides ou 0)

---

## 🔍 Points de Vérification

### Affichage Dynamique

1. **Détails des chambres**
   - ✅ Les sections de détails n'apparaissent QUE si la checkbox est cochée
   - ✅ Si on décoche, la section disparaît et les champs sont réinitialisés

2. **Emails supplémentaires**
   - ✅ Chaque clic sur "Ajouter un email" crée un nouveau champ
   - ✅ Les emails sont numérotés (email2@, email3@, etc.)

3. **Autres types de chambres**
   - ✅ Chaque clic sur "Ajouter" crée un nouveau bloc complet
   - ✅ Le bouton "Supprimer" enlève le bloc correspondant
   - ✅ Les numéros s'incrémentent (#1, #2, #3...)

### Collecte des Données

4. **Structure chambres_details**
   - ✅ C'est un array d'objets
   - ✅ Chaque objet contient : type, tarif_affiche, tarif_accorde, capacite_min, capacite_max, lit_supplementaire
   - ✅ Les checkboxes lit_supplementaire sont des booléens (true/false)

5. **Emails**
   - ✅ email_reservation = email principal
   - ✅ emails_supplementaires = string avec emails séparés par ", "

### Responsive

6. **Mobile**
   - ✅ Les form-row (2 colonnes) passent en 1 colonne sur mobile
   - ✅ Les boutons sont cliquables facilement
   - ✅ Pas de débordement horizontal

7. **Desktop**
   - ✅ Largeur maximale 800px
   - ✅ Centré sur la page
   - ✅ Espacement correct entre les éléments

---

## 📊 Validation n8n

Une fois le formulaire soumis, vérifier dans n8n :

1. **Webhook reçoit les données**
   ```json
   {
     "nom_hotel": "...",
     "chambres_details": [...],
     "emails_supplementaires": "...",
     ...
   }
   ```

2. **Structure chambres_details**
   - Vérifier que c'est bien un array
   - Vérifier que chaque objet a tous les champs
   - Vérifier que lit_supplementaire est un boolean

3. **Emails**
   - Vérifier format correct
   - Vérifier séparation par virgules

---

## 🐛 Tests d'Erreur

### Test 4 : Champs Obligatoires Manquants

**Action :** Ne pas remplir "Nom de l'hôtel"
**Résultat attendu :** Message d'erreur du navigateur avant envoi

### Test 5 : Aucune Chambre Sélectionnée

**Action :** Tout remplir SAUF cocher un type de chambre
**Résultat attendu :** Le formulaire s'envoie (car ce n'est pas un champ obligatoire côté HTML, mais le workflow n8n devrait rejeter)

### Test 6 : Email Invalide

**Action :** Mettre "test" au lieu de "test@test.dz"
**Résultat attendu :** Message d'erreur du navigateur

---

## 📝 Checklist de Test

Avant de déployer en production :

- [ ] Test 1 réussi (hôtel complet avec 3 types standards)
- [ ] Test 2 réussi (hôtel avec types personnalisés)
- [ ] Test 3 réussi (hôtel minimal)
- [ ] Affichage dynamique fonctionne
- [ ] Ajout/suppression d'emails fonctionne
- [ ] Ajout/suppression d'autres chambres fonctionne
- [ ] Données arrivent correctement sur n8n
- [ ] Structure chambres_details est correcte
- [ ] Responsive fonctionne (mobile + desktop)
- [ ] Tests d'erreur passent

---

## 🚀 Prochaine Étape

Une fois tous les tests validés :

1. ✅ Pousser le nouveau formulaire sur GitHub
2. ⏳ Adapter le workflow n8n pour traiter `chambres_details`
3. ⏳ Adapter le script Python `hotel_creator.py`
4. ⏳ Tester le flow complet end-to-end
5. ⏳ Lancer la campagne pilote

---

**Bon test ! 🎯**
