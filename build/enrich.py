#!/usr/bin/env python3
"""Inject teaching diagrams (and, for HTML, a banner photo) into the course markdown.

Two diagram tiers per module:
  * OVERVIEW[module]  — one big-picture schema shown at module level, just before the
    first chapter (always visible in the HTML module intro).
  * CHAPTERS[module]  — one schema per content chapter, injected right after each chapter
    heading so it lives inside (and collapses with) that chapter in the HTML.

Both tiers are defined once as abstract specs (flow / groups / decision) and rendered two
ways: themed HTML/CSS for the self-contained web app (``enrich_markdown``, theme-adaptive),
and ``mermaid`` for the PDF (``enrich_pdf_markdown`` → md_to_pdf.sh renders the mermaid).
Captions and labels are localised. Run ``enrich.py --pdf <pdfsrc.md> <lang>`` for the PDF
injection; ``enrich_markdown`` is imported by build_html.py for the HTML.
"""

import argparse
import html
import re
from pathlib import Path

# Module index (1-8) -> banner image filename + EN/FR caption (HTML only).
BANNERS = {
    1: ("course-corexy.jpg",
        "CoreXY belt routing — the motion system behind high-speed FDM.",
        "Routage des courroies CoreXY — le système de mouvement des imprimantes FDM rapides."),
    2: ("course-printers.jpg",
        "Exploded view of a modern FDM printer.",
        "Vue éclatée d'une imprimante FDM moderne."),
    3: ("hero-bg.jpg",
        "A modern enclosed FDM printer at work.",
        "Une imprimante FDM moderne fermée en action."),
    4: ("course-materials.jpg",
        "A spectrum of FDM filaments.",
        "Un éventail de filaments FDM."),
    5: ("course-slicing.jpg",
        "A slicer previewing toolpaths layer by layer.",
        "Un trancheur prévisualisant les trajectoires couche par couche."),
    6: ("course-profiles.jpg",
        "Print-profile parameters in a configuration file.",
        "Les paramètres d'un profil d'impression dans un fichier de configuration."),
    7: ("course-printers.jpg",
        "The AMS multi-material unit feeding the printer.",
        "L'unité multi-matériaux AMS alimentant l'imprimante."),
    8: ("course-slicing.jpg",
        "Inspecting a print in progress.",
        "Inspection d'une impression en cours."),
}

# Connective words for the decision diagram, per language.
WORDS = {"en": ("Yes", "No", "Otherwise"), "fr": ("Oui", "Non", "Sinon")}

# Per-module OVERVIEW schema (one big-picture diagram per module, shown at module level
# just before the first chapter): type + EN/FR payloads + captions.
OVERVIEW = {
    1: {"type": "flow",
        "en": ["CAD model", "Slice to G-code", "FDM printing", "Post-processing", "Finished part"],
        "fr": ["Modèle CAO", "Tranchage (G-code)", "Impression FDM", "Post-traitement", "Pièce finie"],
        "cap": ("The end-to-end FDM workflow.", "Le flux de travail FDM, de bout en bout.")},
    2: {"type": "groups",
        "en": ("FDM printer", [("Toolhead", ["Hotend + nozzle", "Extruder"]),
                               ("Motion system", ["Stepper motors", "Belts + linear rails"]),
                               ("Bed + frame", ["Heated bed + PEI plate", "Steel chassis"]),
                               ("Electronics", ["Mainboard", "Stepper drivers"])]),
        "fr": ("Imprimante FDM", [("Tête d'impression", ["Hotend + buse", "Extrudeur"]),
                                  ("Système de mouvement", ["Moteurs pas à pas", "Courroies + rails"]),
                                  ("Plateau + châssis", ["Plateau chauffant + PEI", "Châssis acier"]),
                                  ("Électronique", ["Carte mère", "Drivers pas à pas"])]),
        "cap": ("The four subsystems of an FDM printer.", "Les quatre sous-systèmes d'une imprimante FDM.")},
    3: {"type": "groups",
        "en": ("Your printer (X1 / P1 / A1)", [("Bambu Studio / OrcaSlicer", ["Slice and send"]),
                                               ("AMS", ["Multi-material feed"]),
                                               ("MakerWorld", ["Models and profiles"]),
                                               ("Cloud / LAN", ["Monitor and control"])]),
        "fr": ("Votre imprimante (X1 / P1 / A1)", [("Bambu Studio / OrcaSlicer", ["Trancher et envoyer"]),
                                                   ("AMS", ["Alimentation multi-matériaux"]),
                                                   ("MakerWorld", ["Modèles et profils"]),
                                                   ("Cloud / LAN", ["Surveiller et piloter"])]),
        "cap": ("The Bambu Lab ecosystem at a glance.", "L'écosystème Bambu Lab en un coup d'œil.")},
    4: {"type": "decision",
        "en": ([("High heat resistance?", "ABS / ASA / PC"), ("Needs to flex?", "TPU"),
                ("High strength?", "PETG / Nylon")], "PLA"),
        "fr": ([("Résistance à la chaleur ?", "ABS / ASA / PC"), ("Doit être flexible ?", "TPU"),
                ("Haute résistance ?", "PETG / Nylon")], "PLA"),
        "cap": ("A quick material-selection decision tree.", "Un arbre de décision pour choisir son matériau.")},
    5: {"type": "flow",
        "en": ["Import model", "Orient + scale", "Set parameters", "Slice", "Preview layers", "Export G-code"],
        "fr": ["Importer le modèle", "Orienter + dimensionner", "Régler les paramètres", "Trancher",
               "Prévisualiser les couches", "Exporter le G-code"],
        "cap": ("The slicing pipeline, step by step.", "Le pipeline de tranchage, étape par étape.")},
    6: {"type": "flow",
        "en": ["Temperature", "Flow rate", "Pressure advance", "Retraction", "Max volumetric speed", "Input shaping"],
        "fr": ["Température", "Débit", "Pressure advance", "Rétraction", "Vitesse volumétrique max", "Input shaping"],
        "cap": ("The recommended calibration order.", "L'ordre de calibration recommandé.")},
    7: {"type": "flow",
        "en": ["Spool", "AMS slot", "Hub", "Buffer", "Extruder", "Nozzle"],
        "fr": ["Bobine", "Emplacement AMS", "Hub", "Tampon", "Extrudeur", "Buse"],
        "cap": ("The AMS filament path.", "Le trajet du filament dans l'AMS.")},
    8: {"type": "groups",
        "en": ("Print problem?", [("Poor first layer", ["Level bed", "Set Z-offset"]),
                                  ("Stringing", ["Dry filament", "Tune retraction"]),
                                  ("Warping", ["Enclosure", "Adhesion + brim"]),
                                  ("Layer shift", ["Check belts", "Reduce speed"])]),
        "fr": ("Problème d'impression ?", [("Mauvaise 1re couche", ["Niveler le plateau", "Régler le Z-offset"]),
                                           ("Effilage (stringing)", ["Sécher le filament", "Régler la rétraction"]),
                                           ("Gauchissement", ["Caisson", "Adhérence + bordure"]),
                                           ("Décalage de couches", ["Vérifier les courroies", "Réduire la vitesse"])]),
        "cap": ("First moves for common print problems.", "Premiers réflexes face aux problèmes d'impression courants.")},
}

# One diagram per content chapter, in chapter order. Injected after each chapter heading
# (inside the chapter). Facts match the fact-checked module text.
CHAPTERS = {
    1: [
        {"type": "groups",
         "en": ("3D printing technologies", [("FDM/FFF", ["Thermoplastic filament", "Lowest cost, most common"]),
                                             ("SLA/MSLA", ["UV-cured resin", "25-50 micron detail"]),
                                             ("SLS", ["Laser-sintered powder", "Isotropic, no supports"]),
                                             ("MJF", ["IR powder fusion", "Industrial volumes"])]),
         "fr": ("Technologies d'impression 3D", [("FDM/FFF", ["Filament thermoplastique", "Le moins cher, le plus répandu"]),
                                                 ("SLA/MSLA", ["Résine UV", "Détail 25-50 microns"]),
                                                 ("SLS", ["Poudre frittée au laser", "Isotrope, sans supports"]),
                                                 ("MJF", ["Fusion poudre IR", "Volumes industriels"])]),
         "cap": ("Four major 3D printing technologies compared.", "Les quatre grandes technologies d'impression 3D comparées.")},
        {"type": "decision",
         "en": ([("Need fine surface detail?", "0.2 mm layer / 0.4 mm nozzle"), ("Printing flexible filament?", "Direct drive extruder"),
                 ("Need high-temp material?", "All-metal hotend, 300 C+")], "Standard PLA / 0.4 mm setup"),
         "fr": ([("Besoin de détails fins ?", "Couche 0,2 mm / buse 0,4 mm"), ("Filament flexible ?", "Extrudeur direct drive"),
                 ("Matériau haute température ?", "Hotend tout métal, 300 °C")], "PLA standard / buse 0,4 mm"),
         "cap": ("Choosing FDM setup parameters by need.", "Choisir les paramètres FDM selon le besoin.")},
        {"type": "flow",
         "en": ["Slicer sends X-Y coords", "Firmware: A = X+Y, B = X-Y", "Both motors turn together", "Crossed belts move toolhead", "Low-mass, high-speed print"],
         "fr": ["Trancheur envoie X-Y", "Firmware : A = X+Y, B = X-Y", "Les deux moteurs tournent", "Courroies croisées bougent la tête", "Impression rapide, faible masse"],
         "cap": ("How CoreXY converts two motor rotations into X-Y motion.", "Comment CoreXY convertit deux rotations moteur en déplacement X-Y.")},
    ],
    2: [
        {"type": "flow",
         "en": ["Heat sink: keeps filament solid", "Heat break: thermal barrier", "Heater block: 30 W melt zone", "Nozzle exit: 0.4 mm orifice", "Molten filament deposited"],
         "fr": ["Dissipateur : filament solide", "Barrière thermique", "Bloc chauffant : zone de fusion 30 W", "Sortie buse : orifice 0,4 mm", "Filament fondu déposé"],
         "cap": ("Heat zones from cold end to nozzle tip.", "Zones thermiques de l'entrée froide à la buse.")},
        {"type": "decision",
         "en": ([("Printing TPU or flexible?", "Direct drive"), ("Need precise retraction?", "Direct drive"),
                 ("Minimising carriage mass?", "Bowden")], "Direct drive - best all-round"),
         "fr": ([("TPU ou filament flexible ?", "Direct drive"), ("Rétraction précise requise ?", "Direct drive"),
                 ("Réduire la masse du chariot ?", "Bowden")], "Direct drive - meilleur polyvalent"),
         "cap": ("Choosing between direct drive and Bowden.", "Choisir entre direct drive et Bowden.")},
        {"type": "groups",
         "en": ("Printer foundation", [("Heated bed", ["PEI magnetic sheet", "24 V DC recommended"]),
                                       ("Frame", ["2040 extrusion for speed", "Square within 0.3 mm"]),
                                       ("Electronics", ["Klipper: input shaping", "Marlin: standalone"]),
                                       ("Enclosure", ["Unlocks ABS/ASA/PC", "HEPA cuts 74-99% UFP"])]),
         "fr": ("Fondation de l'imprimante", [("Plateau chauffant", ["Feuille PEI magnétique", "24 V CC recommandé"]),
                                              ("Châssis", ["Profilé 2040 pour la vitesse", "Équerrage sous 0,3 mm"]),
                                              ("Électronique", ["Klipper : input shaping", "Marlin : autonome"]),
                                              ("Caisson", ["Ouvre ABS/ASA/PC", "HEPA coupe 74-99% UFP"])]),
         "cap": ("The four foundations of a capable FDM printer.", "Les quatre fondations d'une imprimante FDM performante.")},
    ],
    3: [
        {"type": "flow",
         "en": ["5 ex-DJI engineers, 2020", "X1 Carbon Kickstarter 2022", "US$7M raised / 5575 backers", "Promises delivered on time", "CoreXY + AI + AMS integrated"],
         "fr": ["5 ex-ingénieurs DJI, 2020", "Kickstarter X1 Carbon 2022", "7 M$ levés / 5575 soutiens", "Promesses tenues à temps", "CoreXY + IA + AMS intégrés"],
         "cap": ("How Bambu Lab disrupted desktop 3D printing.", "Comment Bambu Lab a bousculé l'impression 3D.")},
        {"type": "groups",
         "en": ("Bambu Lab lineup", [("A series", ["A1 Mini 180mm / $299", "A1 256mm / $399"]),
                                     ("P series", ["P1S 500mm/s enclosed", "P2S 600mm/s + drying"]),
                                     ("X series", ["X1C lidar + AI camera", "X2D dual nozzle $649"]),
                                     ("H2 series", ["H2D IDEX + laser", "H2S large build"])]),
         "fr": ("Gamme Bambu Lab", [("Série A", ["A1 Mini 180mm / 299$", "A1 256mm / 399$"]),
                                    ("Série P", ["P1S 500mm/s fermée", "P2S 600mm/s + séchage"]),
                                    ("Série X", ["X1C lidar + caméra IA", "X2D double buse 649$"]),
                                    ("Série H2", ["H2D IDEX + laser", "H2S grand volume"])]),
         "cap": ("Four series, four user segments.", "Quatre gammes, quatre profils d'utilisateur.")},
        {"type": "groups",
         "en": ("Bambu key technologies", [("Vibration comp.", ["Accelerometer maps frame", "Cancels ringing at 500mm/s"]),
                                           ("Micro lidar (X1)", ["7 micron bed leveling", "Flow + Z-offset check"]),
                                           ("AI camera (X1)", ["86% spaghetti detection", "Local ML, no cloud"]),
                                           ("Chamber heating", ["Passive 45-50°C: P + X1C", "Active 60-65°C: X1E/H2"])]),
         "fr": ("Technologies Bambu Lab", [("Compensation vibration", ["Accéléromètre intégré", "Annule l'effet à 500mm/s"]),
                                           ("Micro lidar (X1)", ["Mesure de plateau 7 microns", "Débit + Z-offset auto"]),
                                           ("Caméra IA (X1)", ["86% de détection spaghetti", "ML local, sans cloud"]),
                                           ("Chauffage du caisson", ["Passif 45-50°C: P + X1C", "Actif 60-65°C: X1E/H2"])]),
         "cap": ("The four technologies that define the Bambu experience.", "Les quatre technologies qui définissent l'expérience Bambu.")},
    ],
    4: [
        {"type": "decision",
         "en": ([("Functional or load-bearing?", "PETG"), ("Heat above 60°C needed?", "PETG or higher"),
                 ("Chemical resistance needed?", "PETG")], "PLA"),
         "fr": ([("Pièce fonctionnelle/chargée ?", "PETG"), ("Chaleur au-dessus de 60°C ?", "PETG ou plus résistant"),
                 ("Résistance chimique requise ?", "PETG")], "PLA"),
         "cap": ("PLA vs PETG: when to upgrade your everyday material.", "PLA ou PETG : quand passer au matériau supérieur.")},
        {"type": "flow",
         "en": ["ABS 105°C / enclosure req.", "ASA: UV-resistant ABS", "Nylon: dry at 75-90°C", "PC 150°C / all-metal hotend"],
         "fr": ["ABS 105°C / caisson requis", "ASA : résistant aux UV", "Nylon : sécher à 75-90°C", "PC 150°C / hotend tout métal"],
         "cap": ("Engineering materials: escalating requirements.", "Matériaux techniques : des exigences croissantes.")},
        {"type": "groups",
         "en": ("Specialty filaments", [("Flexible (TPU/TPE)", ["95A: phone cases / grips", "85A: soft / direct drive"]),
                                        ("Carbon fiber filled", ["Stiffness + less impact", "Hardened nozzle required"]),
                                        ("Soluble supports", ["PVA dissolves in water", "HIPS + d-Limonene solvent"]),
                                        ("Visual specialty", ["Metal, wood, glow-in-dark", "Each needs specific nozzle"])]),
         "fr": ("Filaments spéciaux", [("Souple (TPU/TPE)", ["95A : coques / poignées", "85A : mou / direct drive"]),
                                       ("Fibre de carbone", ["Rigidité + fragilité accrue", "Buse acier trempé requise"]),
                                       ("Supports solubles", ["PVA soluble dans l'eau", "HIPS + solvant d-Limonène"]),
                                       ("Effets visuels", ["Métal, bois, phospho", "Buse spécifique par type"])]),
         "cap": ("Beyond rigid plastics: flexible, composite and specialty filaments.", "Au-delà des plastiques rigides : souples, composites et spéciaux.")},
        {"type": "decision",
         "en": ([("Outdoor UV exposure?", "ASA"), ("Needs to flex?", "TPU 95A"),
                 ("Engineering strength/heat?", "Nylon or PC")], "PLA or PETG"),
         "fr": ([("Exposition UV en extérieur ?", "ASA"), ("Doit être flexible ?", "TPU 95A"),
                 ("Force / chaleur ingénierie ?", "Nylon ou PC")], "PLA ou PETG"),
         "cap": ("Material selection: start simple, upgrade only when needed.", "Choix du matériau : simple par défaut, plus exigeant si besoin.")},
    ],
    5: [
        {"type": "groups",
         "en": ("Slicer settings", [("Quality", ["Layer height", "Wall count"]),
                                    ("Infill", ["Density %", "Pattern (Gyroid/Grid)"]),
                                    ("Supports", ["Tree vs normal", "Overhang angle"]),
                                    ("Adhesion", ["Skirt / Brim / Raft"]),
                                    ("Speed + Temp", ["Nozzle temp", "Print speed"])]),
         "fr": ("Paramètres du trancheur", [("Qualité", ["Hauteur de couche", "Nombre de parois"]),
                                            ("Remplissage", ["Densité %", "Motif (Gyroid/Grille)"]),
                                            ("Supports", ["Arbre vs normal", "Angle de surplomb"]),
                                            ("Adhérence", ["Jupe / Bordure / Radeau"]),
                                            ("Vitesse + Temp", ["Temp. buse", "Vitesse d'impression"])]),
         "cap": ("Five categories of settings every slicer exposes.", "Les cinq catégories de paramètres de tout trancheur.")},
        {"type": "flow",
         "en": ["Prepare", "Preview", "Device", "Project"],
         "fr": ["Préparer", "Prévisualiser", "Appareil", "Projet"],
         "cap": ("The four tabs of the Bambu Studio workflow.", "Les quatre onglets du flux de travail Bambu Studio.")},
        {"type": "decision",
         "en": ([("Bambu Lab printer?", "Bambu Studio"), ("Klipper / mixed fleet?", "OrcaSlicer"),
                 ("Prusa printer / resin?", "PrusaSlicer")], "UltiMaker Cura"),
         "fr": ([("Imprimante Bambu Lab ?", "Bambu Studio"), ("Klipper / parc mixte ?", "OrcaSlicer"),
                 ("Imprimante Prusa / résine ?", "PrusaSlicer")], "UltiMaker Cura"),
         "cap": ("A decision tree for choosing the right slicer.", "Un arbre de décision pour choisir le bon trancheur.")},
        {"type": "groups",
         "en": ("Advanced features", [("Surface finish", ["Fuzzy skin", "Ironing"]),
                                      ("Special geometry", ["Vase mode (spiral)", "Variable layer height"]),
                                      ("Local overrides", ["Modifier meshes"]),
                                      ("Calibration", ["Temp tower", "Flow / PA / Retraction"])]),
         "fr": ("Fonctions avancées", [("Finition de surface", ["Peau floue", "Repassage (ironing)"]),
                                       ("Géométrie spéciale", ["Mode vase (spirale)", "Hauteur de couche variable"]),
                                       ("Paramètres locaux", ["Maillages modificateurs"]),
                                       ("Calibration", ["Tour de température", "Débit / PA / Rétraction"])]),
         "cap": ("Advanced slicer features and what each one does.", "Les fonctions avancées du trancheur et leur rôle.")},
    ],
    6: [
        {"type": "groups",
         "en": ("Print profile system", [("Printer/Machine", ["Build volume", "Nozzle size", "Start/end G-code"]),
                                         ("Filament/Material", ["Temperatures", "Cooling fan", "Pressure advance"]),
                                         ("Process/Quality", ["Layer height", "Infill", "Speeds + supports"])]),
         "fr": ("Système de profils", [("Imprimante/Machine", ["Volume d'impression", "Diamètre buse", "G-code début/fin"]),
                                       ("Filament/Matériau", ["Températures", "Ventilateur", "Pressure advance"]),
                                       ("Procédé/Qualité", ["Hauteur de couche", "Remplissage", "Vitesses + supports"])]),
         "cap": ("The three-tier hierarchy every slicer uses.", "La hiérarchie à trois niveaux de tout trancheur.")},
        {"type": "flow",
         "en": ["Ultra-detail 0.08 mm", "High quality 0.12 mm", "Standard 0.20 mm", "Draft 0.28+ mm"],
         "fr": ["Ultra-détail 0,08 mm", "Haute qualité 0,12 mm", "Standard 0,20 mm", "Brouillon 0,28+ mm"],
         "cap": ("Quality tiers by layer height for a 0.4 mm nozzle.", "Niveaux de qualité par hauteur de couche (buse 0,4 mm).")},
        {"type": "flow",
         "en": ["Select base material", "Temp tower", "Flow calibration", "Configure cooling", "Save preset"],
         "fr": ["Choisir matériau de base", "Tour de température", "Calibration débit", "Régler refroidissement", "Sauvegarder profil"],
         "cap": ("Five steps to create a custom filament profile.", "Cinq étapes pour créer un profil de filament personnalisé.")},
        {"type": "decision",
         "en": ([("New filament or color?", "Recalibrate temp + flow"), ("Hardware change (nozzle)?", "Recalibrate all steps"),
                 ("Quality degraded?", "Start from temperature")], "No change needed"),
         "fr": ([("Nouveau filament ou couleur ?", "Recalibrer temp + débit"), ("Changement matériel (buse) ?", "Recalibrer toutes les étapes"),
                 ("Qualité dégradée ?", "Recommencer par la température")], "Aucun changement nécessaire"),
         "cap": ("When to trigger a full or partial recalibration.", "Quand déclencher une recalibration complète ou partielle.")},
    ],
    7: [
        {"type": "flow",
         "en": ["Cut filament at toolhead", "Retract old filament", "Load new filament", "Purge at wipe tower", "Resume print"],
         "fr": ["Couper à la tête", "Rétracter l'ancien fil", "Charger le nouveau fil", "Purger à la tour", "Reprendre l'impression"],
         "cap": ("The AMS filament-change sequence.", "La séquence de changement de filament AMS.")},
        {"type": "flow",
         "en": ["Define filaments", "Assign colors", "Set purge volumes", "Enable flush options", "Slice + preview", "Print"],
         "fr": ["Définir les filaments", "Assigner les couleurs", "Régler la purge", "Activer le rinçage", "Trancher + prévisualiser", "Imprimer"],
         "cap": ("The multi-material slicing workflow.", "Le flux de tranchage multi-matériaux.")},
        {"type": "groups",
         "en": ("Reduce purge waste", [("Slicer settings", ["Flush multiplier 0.6-0.8x", "Flush into infill"]),
                                       ("Plate strategy", ["Sacrificial flush object", "Batch multi-color parts"]),
                                       ("Color ordering", ["Dark before light", "Group similar colors"])]),
         "fr": ("Réduire les déchets de purge", [("Réglages trancheur", ["Multiplicateur 0.6-0.8x", "Rinçage dans remplissage"]),
                                                 ("Stratégie plateau", ["Objet sacrificiel", "Regrouper les pièces"]),
                                                 ("Ordre des couleurs", ["Sombres avant claires", "Grouper les teintes proches"])]),
         "cap": ("Layered strategies to cut wipe-tower waste.", "Stratégies combinées pour réduire la purge.")},
    ],
    8: [
        {"type": "decision",
         "en": ([("Spaghetti / no stick?", "Lower Z-offset"), ("Lines squished, translucent?", "Raise Z-offset"),
                 ("Corners lifting off bed?", "Add brim + raise bed temp")], "Save working Z-offset"),
         "fr": ([("Spaghetti / pas d'accroche ?", "Baisser le Z-offset"), ("Trop près : translucide ?", "Monter le Z-offset"),
                 ("Coins qui se décollent ?", "Bordure + hausser plateau")], "Sauvegarder le bon Z-offset"),
         "cap": ("Reading the first layer to fix Z-offset.", "Lire la 1re couche pour corriger le Z-offset.")},
        {"type": "decision",
         "en": ([("Stringing / webs?", "Dry + tune retraction"), ("Under-extrusion / gaps?", "Cold pull + check temp"),
                 ("Warping / lifting?", "Enclosure + brim")], "Calibrate flow + e-steps"),
         "fr": ([("Effilage / toiles ?", "Sécher + régler rétraction"), ("Sous-extrusion / lacunes ?", "Cold pull + vérif. temp."),
                 ("Gauchissement / décollage ?", "Caisson + bordure")], "Calibrer débit + pas moteur"),
         "cap": ("Symptom-to-fix decision tree for common problems.", "Arbre symptôme-solution pour les problèmes courants.")},
        {"type": "groups",
         "en": ("Maintenance schedule", [("Daily", ["Wipe PEI with IPA", "Check first layer"]),
                                         ("Weekly", ["Clean nozzle exterior", "Check belt tension"]),
                                         ("Monthly", ["Cold pull + deep clean", "Lubricate lead screws"]),
                                         ("Quarterly", ["Replace nozzle if worn", "Full calibration run"])]),
         "fr": ("Calendrier maintenance", [("Quotidien", ["Nettoyer PEI avec IPA", "Vérifier 1re couche"]),
                                           ("Hebdomadaire", ["Nettoyer buse extérieure", "Vérifier tension courroies"]),
                                           ("Mensuel", ["Cold pull + nettoyage", "Lubrifier vis Z + rails"]),
                                           ("Trimestriel", ["Remplacer buse si usée", "Calibration complète"])]),
         "cap": ("Preventive maintenance by frequency.", "La maintenance préventive par fréquence.")},
        {"type": "flow",
         "en": ["Find model online", "Check watertight mesh", "Orient + scale", "Slice + send", "Remove supports", "Sand + finish", "Finished part"],
         "fr": ["Trouver un modèle", "Vérifier le maillage", "Orienter + dimensionner", "Trancher + envoyer", "Retirer les supports", "Poncer + finir", "Pièce terminée"],
         "cap": ("The complete model-to-finished-part workflow.", "Le flux complet du modèle à la pièce finie.")},
    ],
}

RE_MODULE = re.compile(r"^## Module ")
RE_CHAPTER = re.compile(r"^### ")
RE_SOURCES = re.compile(r"^###\s+Sources\b")


def _e(text: str) -> str:
    return html.escape(text, quote=True)


# ---- HTML (themed CSS) renderers --------------------------------------------------------

def _flow(steps: list) -> str:
    """Horizontal stepper; the final node is accented. Each arrow stays bound to its node."""
    units = []
    last = len(steps) - 1
    for i, step in enumerate(steps):
        cls = "snode accent" if i == last else "snode"
        arrow = "" if i == last else '<span class="sarrow"></span>'
        units.append(f'<span class="sunit"><span class="{cls}">{_e(step)}</span>{arrow}</span>')
    return '<div class="schema-flow">' + "".join(units) + "</div>"


def _groups(payload) -> str:
    """A root node fanning out to titled group cards, each listing items."""
    root, groups = payload
    cards = []
    for title, items in groups:
        lis = "".join(f"<li>{_e(item)}</li>" for item in items)
        cards.append(f'<div class="sgroup"><div class="sgroup-h">{_e(title)}</div><ul>{lis}</ul></div>')
    return (f'<div class="schema-tree"><div class="sroot">{_e(root)}</div>'
            f'<div class="sfan">{"".join(cards)}</div></div>')


def _decision(payload, lang: str) -> str:
    """Vertical decision flow: each question routes 'yes' to an outcome, else falls through."""
    rows, fallback = payload
    yes, no, otherwise = WORDS[lang]
    out = []
    for question, outcome in rows:
        out.append(f'<div class="drow"><span class="dq">{_e(question)}</span>'
                   f'<span class="darr">{yes} →</span><span class="dout">{_e(outcome)}</span></div>')
        out.append(f'<div class="dno">{no} ↓</div>')
    out.append(f'<div class="drow dfin"><span class="dlbl">{otherwise} →</span>'
               f'<span class="dout accent">{_e(fallback)}</span></div>')
    return '<div class="schema-dec">' + "".join(out) + "</div>"


def _diagram_block(spec: dict, lang: str) -> list:
    payload = spec[lang]
    if spec["type"] == "flow":
        graphic = _flow(payload)
    elif spec["type"] == "groups":
        graphic = _groups(payload)
    else:
        graphic = _decision(payload, lang)
    caption = spec["cap"][1 if lang == "fr" else 0]
    return ["", "::: {.diagram}", graphic, "", caption, ":::", ""]


# ---- PDF (mermaid) renderers ------------------------------------------------------------

ACCENT = "  classDef accent fill:#ff7a2f,stroke:#c2540a,color:#1a1205,font-weight:bold;"


def _mm(label: str) -> str:
    """A label for a mermaid quoted node. Specs avoid []{}| and "; guard the quote anyway."""
    return label.replace('"', "'")


def _mermaid_flow(steps: list) -> str:
    chain = " --> ".join(f'n{i}["{_mm(s)}"]' for i, s in enumerate(steps))
    last = len(steps) - 1
    return f"flowchart LR\n  {chain}\n{ACCENT}\n  class n{last} accent;"


def _mermaid_groups(payload) -> str:
    root, groups = payload
    lines = ["flowchart TD", f'  root["{_mm(root)}"]']
    for gi, (title, items) in enumerate(groups):
        lines.append(f'  root --> g{gi}["{_mm(title)}"]')
        for ii, item in enumerate(items):
            lines.append(f'  g{gi} --> g{gi}_{ii}["{_mm(item)}"]')
    lines.append(ACCENT)
    lines.append("  class root accent;")
    return "\n".join(lines)


def _mermaid_decision(payload, lang: str) -> str:
    rows, fallback = payload
    yes, no, otherwise = WORDS[lang]
    lines = ["flowchart TD"]
    last = len(rows) - 1
    for i, (question, outcome) in enumerate(rows):
        lines.append(f'  q{i}{{"{_mm(question)}"}} -->|{yes}| m{i}["{_mm(outcome)}"]')
        nxt = f"q{i + 1}" if i < last else f'fb["{_mm(fallback)}"]'
        lines.append(f"  q{i} -->|{no}| {nxt}")
    lines.append(ACCENT)
    lines.append("  class fb accent;")
    return "\n".join(lines)


def _mermaid_block(spec: dict, lang: str) -> list:
    payload = spec[lang]
    if spec["type"] == "flow":
        graph = _mermaid_flow(payload)
    elif spec["type"] == "groups":
        graph = _mermaid_groups(payload)
    else:
        graph = _mermaid_decision(payload, lang)
    caption = spec["cap"][1 if lang == "fr" else 0]
    return ["", "```mermaid", graph, "```", "", f"*{caption}*", ""]


# ---- Banner (HTML only) -----------------------------------------------------------------

def _banner_block(index: int, lang: str, assets_dir: Path) -> list:
    filename, cap_en, cap_fr = BANNERS[index]
    caption = cap_fr if lang == "fr" else cap_en
    return ["", "::: {.module-banner}", f"![]({assets_dir / filename})", "", caption, ":::", ""]


def _walk(text, on_overview, on_chapter):
    """Walk *text* line by line, calling on_overview(module) just before each module's first
    chapter and on_chapter(module, chapter_idx) right after each content chapter heading.
    Both callbacks return a list of lines to insert; the chapter heading line is appended
    between an overview insert (before) and a chapter insert (after)."""
    out, module_index, chapter_index, overview_done = [], 0, 0, True
    for line in text.split("\n"):
        if RE_MODULE.match(line):
            module_index += 1
            chapter_index = 0
            overview_done = False
            out.append(line)
            continue
        if module_index and RE_CHAPTER.match(line) and not RE_SOURCES.match(line):
            if not overview_done:
                out.extend(on_overview(module_index))
                overview_done = True
            out.append(line)
            out.extend(on_chapter(module_index, chapter_index))
            chapter_index += 1
            continue
        out.append(line)
    return "\n".join(out)


def enrich_markdown(text: str, lang: str, assets_dir: Path) -> str:
    """HTML enrichment: a banner after each module title, the module-overview diagram before
    the first chapter, and a per-chapter diagram inside each chapter (themed CSS)."""
    def on_overview(m):
        return _banner_block(m, lang, assets_dir) + _diagram_block(OVERVIEW[m], lang)

    def on_chapter(m, idx):
        specs = CHAPTERS.get(m, [])
        return _diagram_block(specs[idx], lang) if idx < len(specs) else []

    # The banner belongs right after the module title; the walk emits the overview just
    # before chapter 1, so fold the banner into the overview insert (still module-level).
    return _walk(text, on_overview, on_chapter)


def enrich_pdf_markdown(text: str, lang: str) -> str:
    """PDF enrichment: the module-overview diagram before the first chapter and a per-chapter
    diagram inside each chapter, as mermaid blocks (rendered by md_to_pdf.sh). No banner."""
    def on_overview(m):
        return _mermaid_block(OVERVIEW[m], lang)

    def on_chapter(m, idx):
        specs = CHAPTERS.get(m, [])
        return _mermaid_block(specs[idx], lang) if idx < len(specs) else []

    return _walk(text, on_overview, on_chapter)


def main() -> None:
    parser = argparse.ArgumentParser(description="Inject mermaid diagrams into a PDF source markdown, in place.")
    parser.add_argument("--pdf", action="store_true", required=True, help="PDF (mermaid) injection mode.")
    parser.add_argument("src", type=Path)
    parser.add_argument("lang", choices=sorted(WORDS))
    args = parser.parse_args()
    enriched = enrich_pdf_markdown(args.src.read_text(encoding="utf-8"), args.lang)
    args.src.write_text(enriched, encoding="utf-8")
    print(f"injected diagrams (mermaid) into {args.src}")


if __name__ == "__main__":
    main()
