# 📝 Changelog - Formulaire Inscription Hôtel

## Version 2.0 - Février 2026

### ✨ Nouvelles Fonctionnalités

#### 1. **Emails de Réservation Multiples**
- ✅ Possibilité d'ajouter plusieurs adresses email de réservation
- ✅ Bouton "Ajouter un autre email" dynamique
- ✅ Suppression individuelle des emails additionnels
- 📊 Données envoyées : `emails_reservation` (array)

#### 2. **Tarifs Détaillés par Type de Chambre**
Au lieu d'un tarif global, chaque type de chambre a maintenant ses propres tarifs :

**Pour chaque type de chambre standard :**
- ✅ Tarif affiché (DZD/nuit)
- ✅ Tarif accordé (DZD/nuit)
- ✅ Capacité minimum (personnes)
- ✅ Capacité maximum (personnes)
- ✅ Possibilité de lit supplémentaire (Oui/Non)

#### 3. **Autres Types de Chambres (Personnalisables)**
- ✅ Bouton "Ajouter un autre type de chambre"
- ✅ Possibilité de nommer des types personnalisés
- ✅ Mêmes détails que les chambres standards

#### 4. **Nouveaux Équipements**
- ✅ Ascenseur
- ✅ Salle de réunion  
- ✅ Cafétéria

---

## 📊 Exemple de Données Envoyées

```json
{
  "nom_hotel": "Hotel Example",
  "ville": "Alger",
  "emails_reservation": ["reservation@hotel.dz", "booking@hotel.dz"],
  "chambres_list": "Double, Triple",
  "chambres_details": {
    "double": {
      "tarif_affiche": 12000,
      "tarif_accorde": 10000,
      "capacite_min": 1,
      "capacite_max": 2,
      "lit_supplementaire": "Oui"
    },
    "triple": {
      "tarif_affiche": 15000,
      "tarif_accorde": 13000,
      "capacite_min": 1,
      "capacite_max": 3,
      "lit_supplementaire": "Non"
    },
    "autres": [
      {
        "nom": "Chambre familiale",
        "tarif_affiche": 18000,
        "tarif_accorde": 16000,
        "capacite_min": 2,
        "capacite_max": 5,
        "lit_supplementaire": "Oui"
      }
    ]
  },
  "equipements": "WiFi gratuit, Parking, Ascenseur, Cafétéria"
}
```

---

## 🔄 Migration Requise

Le script Python `hotel_creator.py` devra être mis à jour pour gérer :
- Les emails multiples
- Les tarifs par chambre
- Les capacités et lits supplémentaires

---

**Version :** 2.0 | **Date :** Février 2026
