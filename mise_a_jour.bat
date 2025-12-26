@echo off
:: Script pour envoyer automatiquement les modifications vers GitHub

echo =======================================================
echo   ENVOI AUTOMATIQUE DES MISES A JOUR VERS GITHUB
echo =======================================================
echo.

:: 1. Se deplacer dans le dossier de ton projet.
:: Ce chemin est deja configure pour le projet actuel.
cd "C:\Users\kawet\Documents\Projet_IA"
if %ERRORLEVEL% neq 0 (
    echo [ERREUR] Impossible de trouver le dossier du projet : C:\Users\kawet\Documents\Projet_IA
    goto end
)

echo Etape 1/4 : Ajout de tous les fichiers en attente...
git add .
if %ERRORLEVEL% neq 0 (
    echo [ERREUR] La commande 'git add' a echoue.
    goto end
)

echo Etape 2/4 : Verification des changements...
:: On verifie s'il y a quelque chose a commiter pour eviter une erreur
git diff --staged --quiet
if %ERRORLEVEL% equ 0 (
    echo [INFO] Aucun changement a envoyer. Tout est deja a jour.
    goto end
)

echo Etape 3/4 : Creation du "commit" (la sauvegarde locale)...
git commit -m "Mise a jour automatique du %date% a %time%"
if %ERRORLEVEL% neq 0 (
    echo [ERREUR] La commande 'git commit' a echoue.
    goto end
)

echo Etape 4/4 : Envoi des modifications vers GitHub...
git push
if %ERRORLEVEL% neq 0 (
    echo [ERREUR] La commande 'git push' a echoue. Verifiez votre connexion et vos identifiants.
    goto end
)

echo.
echo === MISE A JOUR REUSSIE ! Les modifications ont ete envoyees. ===
echo.

:end
echo Appuyez sur une touche pour fermer cette fenetre.
pause > nul
