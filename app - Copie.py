import streamlit as st

# ==============================================================================
# 1. LE CERVEAU (Dictionnaire de correspondance)
# La logique : "Compétence Terrain" -> "Fiche Métier Officielle"
# ==============================================================================
# Chaque compétence pointe vers un "Profil Métier" unique.
# Si on coche 3 compétences qui pointent vers le même profil, il ne s'affichera qu'une fois.

MAPPING_METIERS = {
    # --- ESPACES VERTS ---
    "Tonte et débroussaillage": {"titre": "Ouvrier Paysagiste", "rome": "A1203", "search": "Ouvrier Paysagiste"},
    "Taille de haies et d'arbustes": {"titre": "Ouvrier Paysagiste", "rome": "A1203", "search": "Ouvrier Paysagiste"},
    "Entretien des massifs": {"titre": "Jardinier Espaces Verts", "rome": "A1203", "search": "Jardinier"},
    "Utilisation d'engins (tondeuse/débrou)": {"titre": "Ouvrier Paysagiste", "rome": "A1203", "search": "Ouvrier Paysagiste"},
    
    # --- PROPRETÉ ---
    "Nettoyage industriel et bureaux": {"titre": "Agent d'entretien", "rome": "K2204", "search": "Agent d'entretien"},
    "Utilisation d'autolaveuse / Monobrosse": {"titre": "Agent machiniste propreté", "rome": "K2204", "search": "Agent nettoyage machiniste"},
    "Lavage de vitres": {"titre": "Laveur de vitres", "rome": "K2202", "search": "Laveur de vitres"},
    "Propreté urbaine et voirie": {"titre": "Agent de propreté urbaine", "rome": "K2303", "search": "Agent de voirie"},
    
    # --- BÂTIMENT ---
    "Maçonnerie générale": {"titre": "Maçon", "rome": "F1610", "search": "Maçon"},
    "Montage de murs": {"titre": "Maçon", "rome": "F1610", "search": "Maçon"},
    "Peinture intérieure/extérieure": {"titre": "Peintre en bâtiment", "rome": "F1606", "search": "Peintre bâtiment"},
    "Pose de placo et bandes": {"titre": "Plaquiste", "rome": "F1604", "search": "Plaquiste"},
    "Pose de carrelage": {"titre": "Carreleur", "rome": "F1608", "search": "Carreleur"},
    
    # --- RESTAURATION ---
    "Aide production culinaire": {"titre": "Commis de cuisine", "rome": "G1602", "search": "Commis de cuisine"},
    "Plonge et batterie": {"titre": "Plongeur", "rome": "G1801", "search": "Plongeur restauration"},
    "Service en salle": {"titre": "Serveur", "rome": "G1803", "search": "Serveur"},
    "Normes HACCP": {"titre": "Employé polyvalent restauration", "rome": "G1602", "search": "Employé restauration"},
    
    # --- RESSOURCERIE ---
    "Tri et valorisation": {"titre": "Agent de tri", "rome": "H1902", "search": "Agent de tri déchets"},
    "Vente et conseil": {"titre": "Vendeur en magasin", "rome": "D1211", "search": "Vendeur"},
    "Caisse et encaissement": {"titre": "Hôte de caisse", "rome": "D1505", "search": "Hôte de caisse"},
    "Manutention et stocks": {"titre": "Magasinier", "rome": "N1103", "search": "Magasinier"}
}

# Pour le menu déroulant, on a besoin de la liste des pôles et des compétences par pôle
# On reconstruit une liste simple pour l'affichage
LISTE_PAR_POLE = {
    "🌿 Espaces Verts": ["Tonte et débroussaillage", "Taille de haies et d'arbustes", "Entretien des massifs", "Utilisation d'engins (tondeuse/débrou)"],
    "🧹 Propreté & Hygiène": ["Nettoyage industriel et bureaux", "Utilisation d'autolaveuse / Monobrosse", "Lavage de vitres", "Propreté urbaine et voirie"],
    "🏗️ Bâtiment": ["Maçonnerie générale", "Montage de murs", "Peinture intérieure/extérieure", "Pose de placo et bandes", "Pose de carrelage"],
    "🍽️ Restauration": ["Aide production culinaire", "Plonge et batterie", "Service en salle", "Normes HACCP"],
    "♻️ Ressourcerie": ["Tri et valorisation", "Vente et conseil", "Caisse et encaissement", "Manutention et stocks"]
}

# ==============================================================================
# 2. CONFIGURATION
# ==============================================================================
st.set_page_config(page_title="MON GPS EMPLOI", page_icon="📍", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #D32F2F;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
    }
    .info-metier {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #2196F3;
        margin-bottom: 10px;
    }
    h3 { font-size: 18px !important; margin-bottom: 5px !important; }
    </style>
    """, unsafe_allow_html=True)

try:
    st.image("fond.png", use_container_width=True)
except:
    pass

st.title("📍 MON GPS EMPLOI")

# ==============================================================================
# 3. INTERFACE
# ==============================================================================
with st.container(border=True):
    
    # 1. Pôle
    pole = st.selectbox("1️⃣ Votre Pôle d'activité :", list(LISTE_PAR_POLE.keys()))
    
    # 2. Compétences (Choix multiple)
    competences = st.multiselect("2️⃣ Vos compétences acquises (Cochez tout ce que vous savez faire) :", LISTE_PAR_POLE[pole])
    
    # 3. Ville
    ville = st.text_input("3️⃣ Ville de recherche :", placeholder="ex: Martigues")

    st.divider()

    # ==============================================================================
    # 4. MOTEUR DE RÉSULTAT (L'INTELLIGENCE EST ICI)
    # ==============================================================================
    if ville and competences:
        
        # --- ÉTAPE A : DÉDOUBLONNAGE ---
        # On regarde toutes les compétences cochées et on liste les MÉTIERS correspondants
        # On utilise un dictionnaire pour éviter les doublons (si 2 compétences mènent au même métier)
        metiers_identifies = {}
        
        for comp in competences:
            infos_metier = MAPPING_METIERS[comp]
            cle_unique = infos_metier["titre"] # C'est notre identifiant unique (ex: "Ouvrier Paysagiste")
            
            # Si le métier n'est pas encore listé, on l'ajoute
            if cle_unique not in metiers_identifies:
                metiers_identifies[cle_unique] = {
                    "rome": infos_metier["rome"],
                    "search": infos_metier["search"],
                    "sources": [comp] # On garde en mémoire quelle compétence a mené ici
                }
            else:
                # Si le métier existe déjà, on ajoute juste la compétence à la liste "sources"
                metiers_identifies[cle_unique]["sources"].append(comp)

        # --- ÉTAPE B : AFFICHAGE ---
        st.success(f"✅ Analyse terminée : **{len(metiers_identifies)} métier(s) identifié(s)** correspondant à vos compétences.")
        
        for titre_metier, details in metiers_identifies.items():
            
            # On affiche une belle carte par MÉTIER (et non par compétence)
            with st.expander(f"🎯 Métier Cible : {titre_metier} (Code ROME {details['rome']})", expanded=True):
                
                # Petit texte explicatif dynamique
                liste_sources = ", ".join(details['sources'])
                st.markdown(f"""
                <div class="info-metier">
                    <b>Pourquoi ce métier ?</b><br>
                    Car vous avez validé les compétences : <i>{liste_sources}</i>.
                </div>
                """, unsafe_allow_html=True)
                
          # Les boutons (avec le terme de recherche propre)
        terme = details['search']
        
        # --- ETAPE DE NETTOYAGE POUR LE MOBILE ---
        # On remplace les espaces par des "+" pour que le téléphone comprenne le lien
        terme_url = terme.replace(" ", "+")
        ville_url = ville.replace(" ", "+")
        # -----------------------------------------

        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
            # J'ai corrigé le lien Google Maps pour utiliser le standard sécurisé (https)
            st.link_button("📍 Carte", f"https://www.google.com/maps/search/{terme_url}+{ville_url}")
        with c2:
            st.link_button("💼 Indeed", f"https://fr.indeed.com/emplois?q={terme_url}&l={ville_url}")
        with c3:
            st.link_button("🇫🇷 Fr.Travail", f"https://candidat.francetravail.fr/offres/recherche?motsCles={terme_url}&lieux={ville_url}&rayon=10")
        with c4:
            st.link_button("🔍 BonneBoîte", f"https://labonneboite.francetravail.fr/recherche?metier={terme_url}&lieu={ville_url}")