import streamlit as st

# ==============================================================================
# 1. CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Mon GPS Emploi",
    page_icon="boussole_GPS_Emploi.jpg", # L'image de la boussole
    layout="centered"
)

# Petit style pour faire joli (boutons rouges et boîtes bleues)
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
    </style>
    """, unsafe_allow_html=True)

# --- RESTAURATION DE LA BANDEROLE ---
try:
    st.image("fond.png", use_container_width=True)
except:
    pass # Si l'image n'est pas là, ça ne plante pas

st.title("🧭 MON GPS EMPLOI")
st.write("Trouvez le métier qui matche avec vos compétences !")

# ==============================================================================
# 2. LE CERVEAU (Dictionnaire de correspondance FALC)
# ==============================================================================
MAPPING_METIERS = {
    # --- BÂTIMENT ---
    "Préparer les murs et sols (ponçage, nettoyage)": {"titre": "Peintre en bâtiment", "rome": "F1606", "search": "Peintre en bâtiment"},
    "Monter des cloisons et petits murets": {"titre": "Maçon", "rome": "F1610", "search": "Maçon"},
    "Poser du placo et faire les joints": {"titre": "Plaquiste", "rome": "F1604", "search": "Plaquiste"},
    "Peindre (Intérieur et Façade)": {"titre": "Peintre en bâtiment", "rome": "F1606", "search": "Peintre en bâtiment"},
    "Rénover des bâtiments anciens": {"titre": "Maçon bâti ancien", "rome": "F1610", "search": "Maçon renovation"},
    "Sécuriser et nettoyer le chantier": {"titre": "Aide-Maçon / Manœuvre", "rome": "F1610", "search": "Manoeuvre batiment"},

    # --- ENTRETIEN & PROPRETÉ ---
    "Désinfecter et nettoyer (Hygiène stricte)": {"titre": "Agent de propreté et d'hygiène", "rome": "K2204", "search": "Agent de propreté"},
    "Utiliser les machines (Monobrosse, Autolaveuse)": {"titre": "Agent machiniste propreté", "rome": "K2204", "search": "Agent nettoyage machiniste"},
    "Gérer les stocks de produits": {"titre": "Chef d'équipe propreté", "rome": "K2204", "search": "Chef equipe nettoyage"},
    "Faire du Bio-nettoyage hospitalier": {"titre": "Agent de service hospitalier (ASH)", "rome": "J1301", "search": "ASH Agent de service hospitalier"},
    "Respecter le planning et les consignes": {"titre": "Agent d'entretien polyvalent", "rome": "K2204", "search": "Agent entretien"},
    "Travailler en sécurité (Gestes et Postures)": {"titre": "Laveur de vitres / Surfaces", "rome": "K2202", "search": "Laveur de vitres"},

    # --- SNACKING & RESTAURATION ---
    "Accueillir les clients et prendre les commandes": {"titre": "Employé polyvalent de restauration", "rome": "G1603", "search": "Employé polyvalent restauration"},
    "Cuisiner (Sandwichs, Salades, Crêpes)": {"titre": "Préparateur en restauration rapide", "rome": "G1603", "search": "Equipier restauration rapide"},
    "Servir en salle ou au comptoir": {"titre": "Serveur", "rome": "G1803", "search": "Serveur"},
    "Tenir la caisse et encaisser": {"titre": "Hôte de caisse / Vendeur", "rome": "D1505", "search": "Hote de caisse"},
    "Respecter la chaîne du froid et l'hygiène": {"titre": "Aide de cuisine", "rome": "G1602", "search": "Aide de cuisine"},
    "Nettoyer la cuisine et le matériel": {"titre": "Plongeur / Commis", "rome": "G1801", "search": "Plongeur restauration"},

    # --- ESPACES VERTS ---
    "Tondre et débroussailler": {"titre": "Ouvrier Paysagiste", "rome": "A1203", "search": "Ouvrier Paysagiste"},
    "Utiliser les machines (Tondeuse, Taille-haie)": {"titre": "Ouvrier Paysagiste", "rome": "A1203", "search": "Ouvrier Paysagiste"},
    "Tailler les haies et les arbres": {"titre": "Jardinier Espaces Verts", "rome": "A1203", "search": "Jardinier espaces verts"},
    "Planter et engazonner": {"titre": "Jardinier Paysagiste", "rome": "A1203", "search": "Jardinier paysagiste"},
    "Préparer la terre (Bêchage, engrais)": {"titre": "Ouvrier des espaces verts", "rome": "A1203", "search": "Ouvrier espaces verts"},
    "Ramasser et évacuer les déchets verts": {"titre": "Aide-jardinier", "rome": "A1203", "search": "Aide jardinier"},

    # --- RESSOURCERIE ---
    "Trier les objets (Réemploi ou Recyclage)": {"titre": "Agent de tri", "rome": "K2304", "search": "Agent de tri déchets"},
    "Nettoyer et réparer les objets": {"titre": "Agent valoriste", "rome": "K2304", "search": "Agent valoriste"},
    "Ranger le magasin et les rayons": {"titre": "Employé de rayon", "rome": "D1507", "search": "Employé libre service"},
    "Conseiller les clients et donateurs": {"titre": "Vendeur en magasin", "rome": "D1211", "search": "Vendeur"},
    "Vendre en boutique": {"titre": "Vendeur polyvalent", "rome": "D1211", "search": "Vendeur polyvalent"},
    "Gérer le stock et les arrivages": {"titre": "Magasinier", "rome": "N1103", "search": "Magasinier"}
}

# Liste simplifiée pour le menu déroulant
LISTE_PAR_POLE = {
    "🏗️ Bâtiment (Second Œuvre)": ["Préparer les murs et sols (ponçage, nettoyage)", "Monter des cloisons et petits murets", "Poser du placo et faire les joints", "Peindre (Intérieur et Façade)", "Rénover des bâtiments anciens", "Sécuriser et nettoyer le chantier"],
    "🧹 Entretien & Propreté": ["Désinfecter et nettoyer (Hygiène stricte)", "Utiliser les machines (Monobrosse, Autolaveuse)", "Gérer les stocks de produits", "Faire du Bio-nettoyage hospitalier", "Respecter le planning et les consignes", "Travailler en sécurité (Gestes et Postures)"],
    "🍔 Snacking & Restauration": ["Accueillir les clients et prendre les commandes", "Cuisiner (Sandwichs, Salades, Crêpes)", "Servir en salle ou au comptoir", "Tenir la caisse et encaisser", "Respecter la chaîne du froid et l'hygiène", "Nettoyer la cuisine et le matériel"],
    "🌿 Espaces Verts": ["Tondre et débroussailler", "Utiliser les machines (Tondeuse, Taille-haie)", "Tailler les haies et les arbres", "Planter et engazonner", "Préparer la terre (Bêchage, engrais)", "Ramasser et évacuer les déchets verts"],
    "♻️ Ressourcerie & Recyclage": ["Trier les objets (Réemploi ou Recyclage)", "Nettoyer et réparer les objets", "Ranger le magasin et les rayons", "Conseiller les clients et donateurs", "Vendre en boutique", "Gérer le stock et les arrivages"]
}

# ==============================================================================
# 3. INTERFACE
# ==============================================================================
with st.container(border=True):
    
    st.header("👤 MON PROFIL")
    
    # 1. Pôle
    pole = st.selectbox("1️⃣ Votre Pôle d'activité :", [""] + list(LISTE_PAR_POLE.keys()))
    
    # 2. Compétences (Si un pôle est choisi)
    if pole:
        competences = st.multiselect(
            "2️⃣ Cochez tout ce que vous savez faire :",
            LISTE_PAR_POLE[pole],
            placeholder="Sélectionnez vos savoir-faire ici..."
        )
    else:
        competences = []
    
    # 3. Ville
    ville = st.text_input("3️⃣ Ville de recherche :", placeholder="ex: Martigues")

    st.divider()

    # ==============================================================================
    # 4. MOTEUR DE RÉSULTAT
    # ==============================================================================
    if ville and competences:
        
        # --- ÉTAPE A : DÉDOUBLONNAGE ---
        metiers_identifies = {}
        
        for comp in competences:
            infos_metier = MAPPING_METIERS[comp]
            cle_unique = infos_metier["titre"] 
            
            if cle_unique not in metiers_identifies:
                metiers_identifies[cle_unique] = {
                    "rome": infos_metier["rome"],
                    "search": infos_metier["search"],
                    "sources": [comp]
                }
            else:
                metiers_identifies[cle_unique]["sources"].append(comp)

        # --- ÉTAPE B : AFFICHAGE ---
        st.success(f"✅ Analyse terminée : **{len(metiers_identifies)} métier(s) identifié(s)**.")
        
        # BOUCLE D'AFFICHAGE
        for titre_metier, details in metiers_identifies.items():
            
            with st.expander(f"🎯 Métier Cible : {titre_metier} (Code ROME {details['rome']})", expanded=True):
                
                # Petit texte dynamique
                liste_sources = ", ".join(details['sources'])
                st.markdown(f"""
                <div class="info-metier">
                    <b>Pourquoi ce métier ?</b><br>
                    Car vous avez validé : <i>{liste_sources}</i>.
                </div>
                """, unsafe_allow_html=True)
                
                st.write("👇 **Cliquez pour lancer votre recherche :**")

                # --- CORRECTIF MOBILE & LIENS ---
                terme = details['search']
                terme_url = terme.replace(" ", "+")
                ville_url = ville.replace(" ", "+")

                # --- CORRECTIF AFFICHAGE BOUTONS ---
                c1, c2, c3, c4 = st.columns(4)
                
                with c1:
                    st.link_button("📍 Carte", f"https://www.google.com/maps/search/{terme_url}+near+{ville_url}")
                with c2:
                    st.link_button("💼 Indeed", f"https://fr.indeed.com/emplois?q={terme_url}&l={ville_url}")
                with c3:
                    st.link_button("🇫🇷 Fr.Travail", f"https://candidat.francetravail.fr/offres/recherche?motsCles={terme_url}&lieux={ville_url}&rayon=10")
                with c4:
                    st.link_button("🔍 BonneBoîte", f"https://labonneboite.francetravail.fr/recherche?metier={terme_url}&lieu={ville_url}")

    elif not ville and competences:
        st.warning("⚠️ Merci d'indiquer une ville pour lancer l'analyse.")
    elif ville and not competences:
        st.info("👆 Cochez vos savoir-faire ci-dessus.")