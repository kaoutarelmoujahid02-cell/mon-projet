# Document de Prototype - Application "GPS EMPLOI"

**Concept :** Une application mobile simple et intuitive qui agit comme un GPS pour la recherche d'emploi, spécialement conçue pour des personnes ayant des freins à la mobilité et souhaitant valoriser des compétences techniques. L'application connecte les compétences de l'utilisateur, ses contraintes de mobilité, et les opportunités d'emploi "cachées" sur le marché local.

---

## Fonctionnalités Clés :

1.  **Profil de Compétences Simplifié :** L'utilisateur peut facilement sélectionner ses compétences techniques à partir d'une liste visuelle (icônes : monobrosse, chariot, protocole d'hygiène...).
2.  **Paramétrage de la Mobilité :** Définition d'un périmètre de recherche basé sur l'adresse, le moyen de transport (à pied, bus, train, voiture) et le temps de trajet maximum.
3.  **Suggestion de "Métiers Cousins" :** L'IA de l'application propose des intitulés de poste variés basés sur les compétences de l'utilisateur.
4.  **Carte Interactive des Opportunités :** Visualisation des entreprises à fort potentiel d'embauche (issues de "La Bonne Boîte") directement sur une carte, filtrées selon le profil et le périmètre de mobilité.
5.  **Calcul d'Itinéraire Intégré :** Pour chaque opportunité, l'application affiche l'itinéraire en transports en commun (ou autre) avec la durée et les correspondances.
6.  **Générateur de "Pitch" :** Un mini-assistant pour aider l'utilisateur à construire et sauvegarder une phrase de présentation percutante.

---

## Parcours Utilisateur (Écran par Écran) :

### **Écran 1 : Bienvenue & Configuration Initiale**

*   **Visuel :** Logo "GPS Emploi" et un message de bienvenue simple : "Trouvez l'emploi qui vous correspond, près de chez vous."
*   **Champs à remplir :**
    *   "Mon adresse de départ :" [Champ de saisie]
    *   "Je me déplace en :" [Boutons : À pied / Bus / Train / Voiture]
    *   "Temps de trajet maximum :" [Curseur : 15 min, 30 min, 45 min, 1h]
*   **Bouton :** "Suivant"

### **Écran 2 : Mon "Kit du Pro"**

*   **Titre :** Cochez tout ce que vous savez faire !
*   **Visuel :** Une grille d'icônes cliquables représentant des compétences.
    *   *Exemples :* icône "Monobrosse", "Autolaveuse", "Protocoles d'hygiène", "Service en chambre", "Aide en cuisine"...
*   **Bouton :** "Voir les métiers correspondants"

### **Écran 3 : La Carte des Opportunités (Écran Principal)**

*   **Visuel :** Une carte (type Google Maps) centrée sur l'adresse de l'utilisateur. Un cercle en surbrillance représente son périmètre de mobilité.
*   **Points sur la carte :** Des points de couleur représentent les entreprises qui recrutent.
    *   *Au-dessus de la carte :* "Nous avons trouvé 15 opportunités dans votre zone."
    *   *L'IA a déjà suggéré des "métiers cousins" et les a inclus dans la recherche.*
*   **Interaction :** L'utilisateur peut cliquer sur un point pour voir le nom de l'entreprise.

### **Écran 4 : Fiche Détail de l'Opportunité**

*   *(Apparaît quand on clique sur un point de la carte)*
*   **Titre :** "Hôtel Ibis Martigues Centre"
*   **Informations :**
    *   **Adresse :** [Adresse complète]
    *   **Potentiel de recrutement pour :** Femme de chambre, Agent d'entretien.
    *   **Votre trajet :** 22 minutes en Bus (Ligne 2).
*   **Boutons :**
    *   **[VOIR L'ITINÉRAIRE]** -> Ouvre une vue détaillée du trajet, avec les arrêts de bus.
    *   **[PRÉPARER MON PITCH]** -> Mène à l'écran 5.
    *   **[AJOUTER À MES FAVORIS]**

### **Écran 5 : Mon Assistant "Pitch"**

*   **Titre :** Préparez votre présentation
*   **Texte pré-rempli (basé sur le profil) :**
    *   "Bonjour, je m'appelle [Nom de l'utilisateur]. Je suis expérimenté(e) en... [compétence principale cochée, ex: 'entretien d'hôtels']. Je suis polyvalent(e) et je maîtrise... [autre compétence]. Je suis très intéressé(e) par votre établissement. Serait-il possible..."
*   **Interaction :** L'utilisateur peut modifier le texte et le sauvegarder.

---
**Monétisation / Modèle Économique (Idées pour plus tard) :**
*   Gratuit pour les chercheurs d'emploi.
*   Modèle freemium avec des fonctionnalités avancées (alertes en temps réel, etc.).
*   Partenariats avec les agences d'intérim ou les structures d'insertion pour un suivi des candidats.
