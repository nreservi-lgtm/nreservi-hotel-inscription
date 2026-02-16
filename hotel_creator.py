#!/usr/bin/env python3
"""
Script de création automatique d'hôtels sur Nreservi Pro
Utilisé par le workflow n8n pour traiter les inscriptions du formulaire
"""

from playwright.sync_api import sync_playwright
import json
import sys
import time
from datetime import datetime

class NreserviHotelCreator:
    def __init__(self):
        self.base_url = "https://www.nreservi.pro"
        self.username = "saisie.ia"
        # Le mot de passe doit être dans une variable d'environnement ou config
        self.password = "YOUR_PASSWORD_HERE"  # À remplacer
        
    def create_hotel(self, hotel_data):
        """
        Crée un hôtel sur Nreservi Pro via le formulaire web
        
        Args:
            hotel_data (dict): Données du formulaire d'inscription
            
        Returns:
            dict: Résultat de la création (success, hotel_id, message)
        """
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            
            try:
                # 1. Connexion
                print(f"🔐 Connexion à Nreservi Pro... ({datetime.now().strftime('%H:%M:%S')})")
                page.goto(f"{self.base_url}/cr.admin/")
                page.wait_for_load_state('networkidle')
                
                # Remplir le formulaire de connexion
                page.fill("input[name='username']", self.username)
                page.fill("input[name='password']", self.password)
                page.click("button[type='submit']")
                page.wait_for_load_state('networkidle')
                time.sleep(2)
                
                print("✅ Connecté avec succès")
                
                # 2. Navigation vers création hôtel
                print("📝 Accès au formulaire de création d'hôtel...")
                # URL à adapter selon l'interface réelle de Nreservi Pro
                page.goto(f"{self.base_url}/cr.admin/hotels/nouveau")
                page.wait_for_load_state('networkidle')
                
                # 3. Remplissage du formulaire
                print(f"✍️ Remplissage des informations pour {hotel_data.get('nom_hotel')}...")
                
                # Informations générales
                self._fill_field(page, "nom", hotel_data.get('nom_hotel'))
                self._select_option(page, "ville", hotel_data.get('ville'))
                self._select_option(page, "categorie", hotel_data.get('categorie'))
                
                if hotel_data.get('description'):
                    self._fill_field(page, "description", hotel_data.get('description'))
                
                # Coordonnées
                self._fill_field(page, "adresse", hotel_data.get('adresse'))
                self._fill_field(page, "code_postal", hotel_data.get('code_postal', ''))
                self._select_option(page, "localisation", hotel_data.get('localisation'))
                
                self._fill_field(page, "tel_commercial", hotel_data.get('tel_commercial'))
                self._fill_field(page, "tel_reception", hotel_data.get('tel_reception', ''))
                self._fill_field(page, "email_reservation", hotel_data.get('email_reservation'))
                
                # Types de chambres (checkboxes)
                if hotel_data.get('chambres'):
                    chambres_list = hotel_data['chambres'].split(', ')
                    for chambre in chambres_list:
                        self._check_checkbox(page, f"chambre_{chambre.lower()}")
                
                # Tarifs
                self._fill_field(page, "tarif_affiche", str(hotel_data.get('tarif_affiche')))
                self._fill_field(page, "tarif_accorde", str(hotel_data.get('tarif_accorde')))
                
                # Enfants
                if hotel_data.get('age_max_enfants'):
                    self._fill_field(page, "age_max_enfants", str(hotel_data.get('age_max_enfants')))
                
                if hotel_data.get('age_enfants_gratuits'):
                    self._fill_field(page, "age_enfants_gratuits", str(hotel_data.get('age_enfants_gratuits')))
                
                # Équipements
                if hotel_data.get('equipements'):
                    equipements_list = hotel_data['equipements'].split(', ')
                    for equipement in equipements_list:
                        self._check_checkbox(page, f"eq_{self._normalize_name(equipement)}")
                
                # Marquer comme "en attente de validation" (photos et localisation à compléter)
                try:
                    page.check("input[name='en_attente_validation']")
                except:
                    pass  # Si le champ n'existe pas
                
                # 4. Capture d'écran avant soumission
                screenshot_name = f"screenshot_avant_{self._normalize_name(hotel_data.get('nom_hotel', 'hotel'))}_{int(time.time())}.png"
                page.screenshot(path=screenshot_name)
                print(f"📸 Screenshot sauvegardé: {screenshot_name}")
                
                # 5. Soumission du formulaire
                print("💾 Soumission du formulaire...")
                page.click("button[type='submit']")
                page.wait_for_load_state('networkidle')
                time.sleep(3)
                
                # 6. Capture d'écran après soumission
                screenshot_name_after = f"screenshot_apres_{self._normalize_name(hotel_data.get('nom_hotel', 'hotel'))}_{int(time.time())}.png"
                page.screenshot(path=screenshot_name_after)
                print(f"📸 Screenshot sauvegardé: {screenshot_name_after}")
                
                # 7. Vérification du succès
                page_content = page.content().lower()
                success_keywords = ['succès', 'créé', 'enregistré', 'success', 'ajouté']
                
                if any(keyword in page_content for keyword in success_keywords):
                    print("✅ Hôtel créé avec succès !")
                    hotel_id = self._extract_hotel_id(page)
                    return {
                        'success': True,
                        'hotel_id': hotel_id,
                        'hotel_name': hotel_data.get('nom_hotel'),
                        'message': f"Hôtel {hotel_data.get('nom_hotel')} créé avec succès",
                        'email_hotelier': hotel_data.get('email_reservation'),
                        'screenshot_before': screenshot_name,
                        'screenshot_after': screenshot_name_after
                    }
                else:
                    print("⚠️ Statut de création incertain")
                    return {
                        'success': False,
                        'hotel_name': hotel_data.get('nom_hotel'),
                        'message': "Statut de création incertain - vérifier manuellement",
                        'email_hotelier': hotel_data.get('email_reservation'),
                        'screenshot_before': screenshot_name,
                        'screenshot_after': screenshot_name_after
                    }
                    
            except Exception as e:
                print(f"❌ Erreur: {str(e)}")
                try:
                    error_screenshot = f"screenshot_erreur_{self._normalize_name(hotel_data.get('nom_hotel', 'hotel'))}_{int(time.time())}.png"
                    page.screenshot(path=error_screenshot)
                    print(f"📸 Screenshot erreur sauvegardé: {error_screenshot}")
                except:
                    error_screenshot = None
                    
                return {
                    'success': False,
                    'error': str(e),
                    'hotel_name': hotel_data.get('nom_hotel'),
                    'message': f"Erreur lors de la création: {str(e)}",
                    'email_hotelier': hotel_data.get('email_reservation'),
                    'screenshot_error': error_screenshot
                }
            finally:
                browser.close()
    
    def _fill_field(self, page, field_name, value):
        """Remplit un champ de texte"""
        if value:
            try:
                selectors = [
                    f"input[name='{field_name}']",
                    f"input[id='{field_name}']",
                    f"textarea[name='{field_name}']",
                    f"textarea[id='{field_name}']"
                ]
                for selector in selectors:
                    try:
                        page.fill(selector, str(value), timeout=2000)
                        return
                    except:
                        continue
            except Exception as e:
                print(f"⚠️ Impossible de remplir {field_name}: {e}")
    
    def _select_option(self, page, field_name, value):
        """Sélectionne une option dans un select"""
        if value:
            try:
                selectors = [
                    f"select[name='{field_name}']",
                    f"select[id='{field_name}']"
                ]
                for selector in selectors:
                    try:
                        page.select_option(selector, value, timeout=2000)
                        return
                    except:
                        continue
            except Exception as e:
                print(f"⚠️ Impossible de sélectionner {field_name}: {e}")
    
    def _check_checkbox(self, page, field_id):
        """Coche une checkbox"""
        try:
            selectors = [
                f"input[id='{field_id}']",
                f"input[name='{field_id}']",
                f"input[value='{field_id}']"
            ]
            for selector in selectors:
                try:
                    page.check(selector, timeout=2000)
                    return
                except:
                    continue
        except Exception as e:
            print(f"⚠️ Impossible de cocher {field_id}: {e}")
    
    def _normalize_name(self, name):
        """Normalise un nom pour l'utiliser comme ID ou filename"""
        if not name:
            return "unknown"
        import re
        # Remplacer les caractères spéciaux
        name = re.sub(r'[àáâãäå]', 'a', name.lower())
        name = re.sub(r'[èéêë]', 'e', name.lower())
        name = re.sub(r'[ìíîï]', 'i', name.lower())
        name = re.sub(r'[òóôõö]', 'o', name.lower())
        name = re.sub(r'[ùúûü]', 'u', name.lower())
        name = re.sub(r'[^a-z0-9]', '_', name)
        return name
    
    def _extract_hotel_id(self, page):
        """Extrait l'ID du nouveau hôtel créé"""
        try:
            url = page.url
            # Adapter selon la structure de l'URL de Nreservi Pro
            if '/hotel/' in url:
                return url.split('/hotel/')[-1].split('/')[0]
            elif '/id=' in url:
                return url.split('id=')[-1].split('&')[0]
        except:
            return None

# Point d'entrée CLI
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Recevoir les données en JSON
        hotel_data = json.loads(sys.argv[1])
        creator = NreserviHotelCreator()
        result = creator.create_hotel(hotel_data)
        # Retourner le résultat en JSON
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("Usage: python3 hotel_creator.py '<json_data>'")
        print("\nExemple:")
        print('python3 hotel_creator.py \'{"nom_hotel": "Hotel Test", "ville": "Alger", ...}\'')
