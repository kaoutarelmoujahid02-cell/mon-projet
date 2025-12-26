# Charge la boîte de dialogue pour choisir le dossier
Add-Type -AssemblyName System.Windows.Forms
$dialog = New-Object System.Windows.Forms.FolderBrowserDialog
$dialog.Description = "CHOISISSEZ LE DOSSIER CONTENANT VOS IMAGES"
$dialog.ShowNewFolderButton = $false

# Si l'utilisateur choisit un dossier
if ($dialog.ShowDialog() -eq 'OK') {
    $dossier = $dialog.SelectedPath
    Write-Host "Traitement des images dans : $dossier" -ForegroundColor Green

    # Récupère les images
    $images = Get-ChildItem -Path $dossier -Include *.jpg, *.jpeg, *.png, *.gif, *.bmp, *.webp, *.tiff -Recurse

    if ($images.Count -eq 0) {
        Write-Warning "Aucune image trouvée (JPG/PNG) dans ce dossier !"
    }
    else {
        # Début du fichier HTML
        $html = @"
<!DOCTYPE html>
<html>
<head>
<style>
    body { font-family: 'Segoe UI', sans-serif; margin: 0; padding: 20px; background: #eee; }
    .page { 
        background: white; width: 210mm; min-height: 297mm; 
        margin: 0 auto; padding: 15mm; box-sizing: border-box; 
    }
    h1 { text-align: center; color: #333; font-size: 16px; text-transform: uppercase; border-bottom: 2px solid #333; padding-bottom: 10px; margin-bottom: 30px; }
    .galerie { 
        display: grid; 
        grid-template-columns: 1fr 1fr; /* 2 images par ligne */
        gap: 20px; 
    }
    .carte {
        border: 1px dashed #ccc;
        padding: 10px;
        background: #fff; text-align: center;
    }
    img {
        width: 100%; height: 220px; /* Taille fixe pour alignement parfait */
        object-fit: cover;
    }
    .legende { margin-top: 5px; color: #999; font-size: 12px; font-style: italic; }
    @media print {
        body { background: white; margin: 0; }
        .page { box-shadow: none; margin: 0; width: 100%; }
        .carte { break-inside: avoid; }
    }
</style>
</head>
<body>
<div class="page">
    <h1>Annexe : Support Iconographique (Action)</h1>
    <div class="galerie">
"@

        # Ajout des images
        foreach ($img in $images) {
            $B64 = [Convert]::ToBase64String([IO.File]::ReadAllBytes($img.FullName))
            $Src = "data:image/jpeg;base64,$B64"
            $html += @"
        <div class="carte">
            <img src="$Src">
            <div class="legende">D&eacute;couper ici</div>
        </div>
"@
        }

        $html += "</div></div></body></html>"

        # Création et ouverture
        $fichierSortie = "$dossier\Resultat_Planche.html"
        $html | Out-File $fichierSortie -Encoding UTF8
        Invoke-Item $fichierSortie
    }
}