"""
Ce fichier contient la logique de mapping entre les compétences techniques
et les pistes de métiers suggérées, avec des mots-clés de recherche optimisés.
"""

# Dictionnaire de mapping amélioré :
# Clé : ID de la compétence
# Valeur : Liste de dictionnaires {'titre': 'Titre officiel (ROME)', 'rome_code': 'Code ROME', 'recherche': 'Mot-clé Google Maps'}
MAPPING_COMPETENCES_JOBS = {
    # Pôle Entretien & Propreté
    'machines_nettoyage': [{'titre': 'Agent de propreté mécanisée (K2204)', 'rome_code': 'K2204', 'recherche': 'Entreprise de nettoyage industriel'}],
    'protocoles_hygiene': [
        {'titre': 'Agent de propreté mécanisée (K2204)', 'rome_code': 'K2204', 'recherche': 'Entreprise de nettoyage industriel'},
        {'titre': 'Agent hôtelier hospitalier (J1301)', 'rome_code': 'J1301', 'recherche': 'Clinique Hôpital EHPAD'}
    ],
    'vitrerie': [{'titre': 'Laveur de vitres (K2204)', 'rome_code': 'K2204', 'recherche': 'Entreprise nettoyage vitres'}],

    # Pôle BTP & Second Œuvre
    'peinture_finitions': [{'titre': 'Peintre en bâtiment (F1606)', 'rome_code': 'F1606', 'recherche': 'Entreprise de peinture bâtiment'}],
    'pose_revetement': [{'titre': 'Solier-Moquettiste (F1609)', 'rome_code': 'F1609', 'recherche': 'Entreprise revêtement de sols'}],

    # Pôle Espaces Verts
    'taille_vegetaux': [{'titre': 'Ouvrier Paysagiste (A1203)', 'rome_code': 'A1203', 'recherche': 'Paysagiste entretien jardins'}],
    'tonte_debroussaillage': [{'titre': 'Ouvrier Paysagiste (A1203)', 'rome_code': 'A1203', 'recherche': 'Paysagiste entretien jardins'}],

    # Pôle Restauration & Snacking
    'plonge': [{'titre': 'Plongeur en restauration (G1602)', 'rome_code': 'G1602', 'recherche': 'Restaurant traditionnel'}],
    'prepa_froide': [{'titre': 'Employé polyvalent de restauration (G1603)', 'rome_code': 'G1603', 'recherche': 'Restauration rapide'}],
    'service_rapide': [{'titre': 'Employé polyvalent de restauration (G1603)', 'rome_code': 'G1603', 'recherche': 'Restauration rapide'}],

    # Pôle Ressourcerie & Vente
    'tri_valorisation': [{'titre': 'Employé de libre-service (D1507)', 'rome_code': 'D1507', 'recherche': 'Supermarché Grande distribution'}],
    'accueil_client': [{'titre': 'Employé de libre-service (D1507)', 'rome_code': 'D1507', 'recherche': 'Supermarché Grande distribution'}]
}

def get_jobs_from_skills(selected_skills_ids):
    """
    Prend une liste d'IDs de compétences et renvoie une liste unique de dictionnaires 
    contenant le titre du métier, le code ROME et le mot-clé de recherche.
    """
    suggested_jobs = []
    seen_titles = set()  # Pour éviter les doublons de métiers

    for skill_id in selected_skills_ids:
        if skill_id in MAPPING_COMPETENCES_JOBS:
            jobs_for_skill = MAPPING_COMPETENCES_JOBS[skill_id]
            for job in jobs_for_skill:
                # Ajoute le métier seulement si on ne l'a pas déjà ajouté
                if job['titre'] not in seen_titles:
                    suggested_jobs.append(job)
                    seen_titles.add(job['titre'])
    
    # Trie la liste finale par ordre alphabétique du titre pour un affichage cohérent
    return sorted(suggested_jobs, key=lambda x: x['titre'])
