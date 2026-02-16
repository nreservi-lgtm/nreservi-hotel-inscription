# 🏨 Système d'Inscription Automatisée des Hôtels - Nreservi Pro

## 📦 Contenu du Projet

Voici tous les fichiers créés pour ton système d'automatisation :

```
nreservi-hotel-inscription/
│
├── 📄 index.html                    ← Formulaire web (GitHub Pages)
├── 🐍 hotel_creator.py              ← Script Playwright de création
├── ⚙️ n8n-workflow.json             ← Configuration workflow n8n
├── 📧 email-template-brevo.html     ← Template campagne Brevo
│
├── 📖 README.md                     ← Vue d'ensemble du projet
├── 🚀 DEPLOY.md                     ← Instructions déploiement GitHub
├── 🛠️ SETUP.md                      ← Guide configuration complet
└── 🔒 .gitignore                    ← Fichiers à ignorer par Git
```

---

## 🎯 Objectif

Automatiser l'inscription de 200+ hôtels sur Nreservi Pro via :
1. Campagne email Brevo (invitation)
2. Formulaire web GitHub Pages
3. Traitement automatique via n8n + Playwright
4. Validation manuelle (GPS + photos)

---

## 🔄 Workflow Complet

```
1. CAMPAGNE BREVO
   ↓
   Email envoyé à 200+ hôteliers
   ↓
   Lien vers formulaire GitHub Pages

2. FORMULAIRE WEB
   ↓
   Hôtelier remplit le formulaire (5 min)
   ↓
   Soumission → POST vers webhook n8n

3. WORKFLOW N8N
   ↓
   Validation des données
   ↓
   Exécution script Python (Playwright)

4. SCRIPT PLAYWRIGHT
   ↓
   Connexion compte saisie.ia
   ↓
   Remplissage formulaire Nreservi Pro
   ↓
   Création fiche hôtel (en attente validation)

5. EMAILS AUTOMATIQUES
   ↓
   • Hôtelier : Confirmation + prochaines étapes
   • Admin : Notification + lien vers fiche
```

---

## 📋 Checklist de Déploiement Rapide

### 1️⃣ GitHub (5 min)

```bash
# Sur ton ordinateur
cd /path/to/download
git clone <ce-repo>
cd nreservi-hotel-inscription

# Créer repo sur GitHub.com
# Puis :
git remote add origin https://github.com/TON-USERNAME/nreservi-hotel-inscription.git
git push -u origin main

# Activer GitHub Pages dans Settings
```

**Résultat :** Formulaire accessible sur `https://TON-USERNAME.github.io/nreservi-hotel-inscription/`

---

### 2️⃣ n8n (10 min)

1. Créer nouveau workflow "Inscription Hotel"
2. Importer `n8n-workflow.json`
3. Configurer :
   - Gmail OAuth (pour envoi emails)
   - Email admin : ton email
   - Path du script Python
4. Activer le workflow

**Résultat :** Webhook `https://nreservi.app.n8n.cloud/webhook/inscription-hotel` opérationnel

---

### 3️⃣ Script Python (15 min)

```bash
# Sur serveur/machine n8n
pip3 install playwright --break-system-packages
python3 -m playwright install chromium

# Créer dossier
mkdir -p /home/node/hotel_creator
cd /home/node/hotel_creator

# Copier hotel_creator.py
# Éditer ligne 13 : ajouter le mot de passe saisie.ia
nano hotel_creator.py

# Tester
python3 hotel_creator.py '{"nom_hotel":"Test","ville":"Alger",...}'
```

**Résultat :** Script capable de créer des hôtels sur Nreservi Pro

---

### 4️⃣ Brevo (10 min)

1. Créer nouvelle campagne email
2. Copier contenu de `email-template-brevo.html`
3. Personnaliser :
   - URL formulaire
   - Numéro téléphone
4. Importer liste contacts hôteliers

**Résultat :** Campagne prête à envoyer

---

### 5️⃣ Test End-to-End (10 min)

1. Remplir formulaire avec données fictives
2. Vérifier exécution n8n
3. Vérifier création sur Nreservi Pro
4. Vérifier réception emails

**Résultat :** Système 100% fonctionnel ! 🎉

---

## 💡 Points Clés à Retenir

### ✅ Le Compte saisie.ia

- **Username :** `saisie.ia`
- **URL :** `www.nreservi.pro/cr.admin/`
- **Même mot de passe que pour les stop sales**
- Tu l'as déjà ! 👍

### ✅ Ce Qui Est Automatisé

- Envoi emails d'invitation
- Réception des formulaires
- Connexion à Nreservi Pro
- Remplissage du formulaire hôtel
- Envoi confirmations

### ⚠️ Ce Qui Reste Manuel

- Localisation GPS précise (sur Nreservi Pro)
- Upload des photos
- Validation finale de la fiche
- Mise en ligne

---

## 📊 Métriques de Succès

| Métrique | Objectif | Comment Mesurer |
|----------|----------|----------------|
| Taux ouverture email | 30%+ | Brevo Analytics |
| Taux clic formulaire | 10%+ | Brevo Analytics |
| Taux complétion formulaire | 50%+ | n8n Executions |
| Taux création réussie | 90%+ | Screenshots Python |
| Temps traitement/hôtel | < 5 min | n8n Execution time |

---

## 🎬 Prochaines Actions

1. **Aujourd'hui :**
   - [ ] Déployer sur GitHub Pages
   - [ ] Configurer webhook n8n
   - [ ] Tester le script Python

2. **Cette Semaine :**
   - [ ] Collecter 50 emails d'hôteliers
   - [ ] Préparer campagne Brevo
   - [ ] Lancer test pilote (10 hôtels)

3. **Ce Mois :**
   - [ ] Enrichir base à 200+ contacts
   - [ ] Déploiement global par vagues
   - [ ] Optimiser selon feedback

---

## 📞 Support & Assistance

**Fichiers de référence :**
- `DEPLOY.md` → Comment déployer sur GitHub
- `SETUP.md` → Configuration complète étape par étape
- `README.md` → Vue d'ensemble technique

**En cas de problème :**
1. Check logs n8n
2. Regarder screenshots Python
3. Tester chaque composant isolément
4. Ping moi ! 🚀

---

## 🚀 Ready to Launch!

Tous les fichiers sont prêts. Il te suffit de :

1. Pousser sur GitHub → 5 min
2. Configurer n8n → 10 min
3. Installer script Python → 15 min
4. Préparer campagne Brevo → 10 min

**Total : ~40 minutes** pour avoir un système 100% opérationnel qui peut gérer l'inscription de 200+ hôtels automatiquement ! 💪

---

**Créé pour Nreservi FZCO** | Février 2026 | Version 1.0

Bonne chance avec le déploiement ! N'hésite pas si tu as la moindre question 😊
