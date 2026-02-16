# 🚀 Instructions de Déploiement GitHub

## Étape 1 : Créer le Repo sur GitHub

1. Va sur https://github.com
2. Clique sur le bouton "New repository" (vert)
3. Nom du repo : `nreservi-hotel-inscription`
4. Description : "Formulaire d'inscription pour hôteliers - Nreservi Pro"
5. Public (pour GitHub Pages gratuit)
6. **NE COCHE PAS** "Add a README file"
7. **NE COCHE PAS** "Add .gitignore"
8. Clique sur "Create repository"

## Étape 2 : Pousser le Code

GitHub va afficher les commandes. Tu vas utiliser la section "…or push an existing repository from the command line" :

```bash
cd /home/claude/nreservi-hotel-inscription

# Remplace USERNAME par ton username GitHub
git remote add origin https://github.com/USERNAME/nreservi-hotel-inscription.git

git branch -M main
git push -u origin main
```

**Note :** Tu devras peut-être t'authentifier avec un Personal Access Token (PAT) au lieu du mot de passe.

### Créer un Personal Access Token si besoin :
1. GitHub → Settings (ton profil) → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token (classic)
4. Cocher : `repo` (Full control of private repositories)
5. Generate token
6. Copier le token (tu ne le reverras plus !)
7. Utiliser ce token comme mot de passe lors du push

## Étape 3 : Activer GitHub Pages

1. Va sur ton repo : `https://github.com/USERNAME/nreservi-hotel-inscription`
2. Clique sur "Settings" (en haut)
3. Dans le menu de gauche, clique sur "Pages"
4. Sous "Source" :
   - Sélectionne "Deploy from a branch"
   - Branch : `main`
   - Folder : `/ (root)`
5. Clique sur "Save"
6. Attends 1-2 minutes

## Étape 4 : Vérifier le Déploiement

Ton formulaire sera accessible à :
```
https://USERNAME.github.io/nreservi-hotel-inscription/
```

GitHub Pages affichera l'URL exacte dans Settings > Pages.

## Étape 5 : Tester le Formulaire

1. Ouvre l'URL dans ton navigateur
2. Remplis le formulaire
3. Vérifie que le webhook n8n est bien configuré :
   - Dans `index.html`, ligne 274
   - URL : `https://nreservi.app.n8n.cloud/webhook/inscription-hotel`

## 🔧 Modifications Futures

Pour modifier le formulaire :

```bash
cd /home/claude/nreservi-hotel-inscription

# Faire tes modifications dans index.html

git add .
git commit -m "Description de tes modifications"
git push
```

Le site se mettra à jour automatiquement en 1-2 minutes.

## 📧 Prochaines Étapes

1. ✅ Créer le webhook n8n `/webhook/inscription-hotel`
2. ✅ Configurer le workflow n8n (fichier `n8n-workflow.json` fourni)
3. ✅ Tester le script Playwright de création d'hôtel
4. ✅ Préparer le template Brevo (fichier `email-template-brevo.html` fourni)
5. ✅ Lancer la campagne pilote (20 hôtels)

---

**Besoin d'aide ?** Ping moi ! 🚀
