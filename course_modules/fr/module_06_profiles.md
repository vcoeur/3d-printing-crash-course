# Module 6 : Configuration et réglage des profils

> **Aperçu du module :** Chaque impression 3D réussie commence par un profil — une « recette » complète qui indique à votre imprimante exactement comment transformer le filament en objet fini. Dans ce module, vous apprendrez comment les profils sont structurés, comment les configurer pour différents matériaux et objectifs de qualité, et comment étalonner votre imprimante pour obtenir une précision dimensionnelle et une finition de surface irréprochable. À la fin, vous passerez des réglages au hasard à un calibrage systématique et confiant.

---

## Chapitre 1 : Comprendre les profils d'impression

Un **profil d'impression** est la recette complète d'une impression réussie. Il s'agit d'un ensemble complet de paramètres optimisés pour une combinaison spécifique de matériel d'imprimante, de matériau de filament et d'objectif de qualité. Les profils regroupent des centaines de paramètres — des températures et des vitesses au refroidissement et à la rétraction — dans des préréglages réutilisables qui éliminent le besoin de configurer manuellement chaque paramètre pour chaque impression.^[1]^

Imaginez un profil comme une recette dans un livre de cuisine. De même qu'une recette de gâteau spécifie la température du four, le temps de cuisson et les proportions d'ingrédients, un profil d'impression spécifie la température de la buse, la hauteur de couche, la vitesse d'impression et la stratégie de refroidissement. Le même modèle 3D imprimé avec différents profils peut varier considérablement en résistance, finition de surface, durée d'impression et précision dimensionnelle.^[1]^

### La structure à trois niveaux des profils

Tous les grands logiciels de découpe — Cura, PrusaSlicer, Bambu Studio et OrcaSlicer — organisent les profils en trois niveaux fondamentaux qui fonctionnent ensemble comme un système.^[1]^^[2]^ Comprendre cette structure est essentiel, car chaque niveau gère un aspect différent du processus d'impression, et ils interagissent de manière importante.

| Niveau | Aussi appelé | Contient | Exemples de préréglages |
|--------|-------------|----------|------------------------|
| **Imprimante/Machine** | Profil système | Volume de construction, taille de buse, type de firmware, limites d'accélération, G-code de début/fin | « Bambu Lab X1C 0.4mm », « Ender 3 Pro » |
| **Filament/Matériau** | Profil matériau | Températures, vitesses du ventilateur de refroidissement, débit (flow rate), rétraction, pressure advance | « Generic PLA », « PETG Overture » |
| **Processus/Qualité** | Profil qualité | Hauteur de couche, nombre de parois, motif de remplissage, vitesses d'impression, paramètres de supports | « 0.20mm Standard », « 0.12mm Fin » |

#### Niveau 1 : Paramètres de l'imprimante/machine

Le **profil d'imprimante** définit les capacités et les contraintes de votre matériel. Ce sont les limites physiques que votre machine ne peut pas dépasser :^[1]^

- **Spécifications de base :** Dimensions du plateau, forme, diamètre(s) de buse, nombre d'extrudeurs et type de firmware (Marlin, Klipper, etc.)
- **Limites de sécurité :** Valeurs maximales de vitesse, d'accélération et de saccade qui empêchent les dommages mécaniques
- **Séquences de mouvement :** G-code de début, G-code de fin, séquences de mise à zéro et commandes de mise à niveau par maillage (comme `G29` pour le firmware Marlin)
- **Configurations multi-outils :** Décalages d'outils, tours de purge et boucliers anti-suintement pour les configurations multi-matériaux

Ces paramètres changent rarement, sauf si vous modifiez le matériel de votre imprimante. Lorsqu'ils changent — par exemple lors du remplacement d'une buse par un diamètre différent — les conséquences se répercutent sur les autres niveaux de profil.

#### Niveau 2 : Paramètres du filament/matériau

Le **profil de filament** contient les paramètres thermiques et d'extrusion spécifiques au matériau. C'est là que réside la personnalité unique de chaque filament :^[1]^^[3]^

- **Température :** Températures de la buse et du plateau (la première couche est souvent imprimée légèrement plus chaud)
- **Refroidissement :** Courbes de vitesse du ventilateur, incluant les premières couches sans refroidissement et les substitutions pour les ponts
- **Débit et extrusion :** Le multiplicateur d'extrusion et la limite de vitesse volumétrique maximale (max volumetric speed)
- **Rétraction :** Distance, vitesse et paramètres de Z-hop pour éviter le suintement
- **Pressure advance :** La valeur K qui compense le retard d'extrusion dans les virages

💡 **Astuce de pro :** Créez toujours un préréglage de filament séparé pour chaque marque et type que vous utilisez. Même deux filaments PLA de fabricants différents peuvent nécessiter des températures et des débits différents. La charge en pigment affecte le diamètre effectif du filament, ce qui signifie qu'un PLA rouge et un PLA blanc de la même marque peuvent nécessiter des paramètres de débit légèrement différents.^[4]^

#### Niveau 3 : Paramètres de processus/qualité

Le **profil de processus** définit la stratégie de découpe et la géométrie de l'impression elle-même :^[1]^^[5]^

- **Définition des couches :** Hauteur de couche (généralement 25 à 75 % du diamètre de la buse), hauteur de la première couche
- **Parois et enveloppes :** Nombre de périmètres, nombre de couches solides supérieures et inférieures
- **Remplissage :** Pourcentage de densité, type de motif et angle
- **Vitesses :** Vitesses indépendantes pour les périmètres, le remplissage, les déplacements, la première couche et les ponts
- **Supports :** Type, densité, angle seuil de porte-à-faux et couches d'interface
- **Contrôle de la couture :** Stratégie de positionnement (alignée, aléatoire ou la plus proche)
- **Fonctions spéciales :** Repassage (ironing), peau floue (fuzzy skin) et hauteur de couche variable

### Comment les niveaux fonctionnent ensemble

Les profils ne sont pas indépendants — ils forment un système de configuration où les capacités de l'imprimante contraignent les options de filament, et les deux contraignent les paramètres de processus. PrusaSlicer utilise des « dépendances » pour lier les préréglages à des imprimantes et des filaments spécifiques, ce qui peut provoquer la disparition des préréglages système lorsque des configurations d'imprimante incompatibles sont sélectionnées.

Lorsque vous changez votre profil d'imprimante — par exemple, d'une buse 0,4 mm à une buse 0,6 mm — les préréglages de processus disponibles se mettent automatiquement à jour. La documentation de Bambu Studio précise : « Lorsque vous sélectionnez "Bambu Lab X1C 0.4 nozzle", vous verrez les paramètres de processus… Lorsque vous passez à "Bambu Lab X1C 0.2 nozzle", vous verrez [d'autres] paramètres de processus. »^[6]^ Cet ajustement automatique aide à éviter les paramètres inadaptés, mais peut être déroutant si vous ne comprenez pas le système d'héritage.

### Le système de profils Bambu Lab

Bambu Studio organise les préréglages en trois catégories selon leur propriété et leur modifiabilité :^[6]^

Les **préréglages système** sont des configurations intégrées, spécifiques à l'imprimante, fournies par Bambu Lab. Ils sont verrouillés pour l'édition directe et servent de bases de référence fiables. Bambu Studio précise explicitement : « Les préréglages système ne peuvent pas être modifiés directement. Cependant, vous pouvez en faire des copies, modifier les paramètres souhaités et enregistrer le résultat en tant que préréglage utilisateur. »^[6]^

Les **préréglages utilisateur** sont vos configurations personnalisées, créées en copiant et en modifiant les préréglages système. Ils peuvent être synchronisés avec Bambu Cloud pour être utilisés sur plusieurs ordinateurs. Des limites de compte s'appliquent : 20 préréglages d'imprimante, 100 préréglages de processus et 200 préréglages de filament par compte.^[7]^

Les **préréglages de projet** sont enregistrés dans un fichier de projet .3MF spécifique. Ils se déplacent avec ce fichier et sont utiles lorsqu'un modèle particulier nécessite des paramètres uniques que vous ne souhaitez pas appliquer globalement.

### Le système de profils OrcaSlicer

OrcaSlicer suit la même structure à trois niveaux que Bambu Studio, dont il est un fork, mais avec une prise en charge d'imprimante plus large — en particulier pour les machines basées sur Klipper.^[2]^ La différence principale est l'indépendance vis-à-vis de Bambu Cloud, ce qui en fait un choix populaire pour les utilisateurs ayant des flux de travail multi-imprimantes.

La communauté OrcaSlicer recommande une approche disciplinée de la gestion des profils :^[1]^

1. **Conserver les profils d'origine intacts** — dupliquer avant de modifier
2. **Créer des profils de filament par marque et type** — enregistrer les préréglages avec les températures, le refroidissement, le débit (flow rate) et le pressure advance pré-étalonnés
3. **Maintenir deux versions du profil machine** — une version « Stock » et une version « Tuned », avec les modifications matérielles documentées dans les notes du profil

### Importer, exporter et partager des profils

Bambu Studio et OrcaSlicer prennent tous deux en charge l'exportation des préréglages utilisateur vers des fichiers locaux pour la sauvegarde ou le partage.^[6]^^[8]^ Les profils OrcaSlicer peuvent être exportés sous forme de bundles `.orca_printer` ou `.orca_filament`.^[8]^^[9]^

📝 **Note :** Le transfert de préréglages entre différents modèles d'imprimantes nécessite de prêter attention au champ « inherits » dans la structure JSON sous-jacente. Le profil parent hérité doit exister sur la machine cible, sinon le préréglage ne se chargera pas correctement.^[9]^

La migration entre logiciels de découpe est partiellement prise en charge : les profils PrusaSlicer fonctionnent dans OrcaSlicer avec des ajustements mineurs. Les profils Bambu Studio sont pour la plupart compatibles avec OrcaSlicer. Les profils Cura, en revanche, ne migrent pas proprement en raison d'une architecture de profil fondamentalement différente.^[2]^

### L'importance d'une base de référence fiable

La règle d'or du réglage de profil est simple : **commencer par une base de référence fonctionnelle et ne modifier qu'un élément à la fois**. Commencez par un préréglage générique correspondant à votre imprimante et votre matériau (par exemple, « Generic PLA @ BBL X1C »), vérifiez qu'il produit des impressions acceptables, puis étalonnez systématiquement. Passer directement à des valeurs personnalisées sans point de départ éprouvé transforme un processus de réglage gérable en exercice de frustration.

⚠️ **Avertissement :** Ne commencez jamais le réglage avec plusieurs modifications personnalisées simultanément. Si votre impression échoue, vous ne saurez pas quelle modification en est la cause. L'approche de débogage classique — modifier une variable, tester, observer, puis passer à la suivante — est le seul chemin fiable vers un profil bien réglé.

### Points clés à retenir

- Les profils d'impression sont organisés en trois niveaux : paramètres **Imprimante/Machine**, **Filament/Matériau** et **Processus/Qualité**, chacun gérant un aspect différent de l'impression.^[1]^
- Les niveaux sont interdépendants : modifier un profil d'imprimante (comme la taille de la buse) affecte les préréglages de processus et de filament disponibles.^[6]^
- **Bambu Studio** propose des préréglages système (intégrés), des préréglages utilisateur (vos configurations personnalisées synchronisées avec le cloud, avec des limites de 20 imprimantes / 100 processus / 200 filaments) et des préréglages de projet (enregistrés dans des fichiers .3MF).^[6]^^[7]^
- **OrcaSlicer** utilise la même structure à trois niveaux avec une prise en charge d'imprimante plus large et sans dépendance au cloud.^[2]^
- Dupliquez toujours les profils d'origine avant de les modifier, et documentez vos modifications matérielles dans les notes du profil.
- Commencez le réglage à partir d'un préréglage générique de référence fiable et modifiez **un seul paramètre à la fois**.

---

## Chapitre 2 : Configuration des profils génériques

La structure des profils étant comprise, il est temps de configurer les paramètres qui déterminent la qualité d'impression, la vitesse et la compatibilité des matériaux. Ce chapitre couvre les profils génériques qui s'appliquent à toutes les imprimantes FDM — quelle que soit la marque — et explique comment les adapter à vos besoins spécifiques.

### Profils de qualité par hauteur de couche

Les profils de qualité se différencient principalement par la **hauteur de couche**, qui détermine directement la visibilité des lignes de couche et la durée d'impression.^[1]^ Pensez à la hauteur de couche comme à la « résolution » de votre impression sur l'axe Z — des couches plus petites signifient plus de détails, mais des durées d'impression considérablement plus longues.

| Profil | Hauteur de couche | Cas d'utilisation | Durée d'impression relative |
|--------|------------------|------------------|-----------------------------|
| **Ultra-détail** | 0,06-0,10 mm | Figurines, bijoux, maquettes architecturales fines | 3-4x la base |
| **Haute qualité** | 0,10-0,16 mm | Pièces fonctionnelles détaillées, prototypes visibles | ~2x la base |
| **Standard** | 0,16-0,24 mm | Impression polyvalente, équilibre qualité/vitesse | 1x (base) |
| **Brouillon** | 0,25-0,32 mm | Prototypes rapides, grands objets structurels, vérifications d'ajustement | ~0,7x la base |

Une buse standard de 0,4 mm peut imprimer de manière fiable des hauteurs de couche allant d'environ 0,08 mm (soit 25 % du diamètre de la buse) jusqu'à environ 0,32 mm (80 % du diamètre de la buse). Tenter de dépasser cette plage risque d'entraîner une consistance d'extrusion médiocre et des dommages potentiels à la buse.^[10]^

**Ultra-détail (0,08 mm)** est le domaine de la peinture de figurines, des modèles dentaires et des patrons de bijoux. À cette hauteur de couche, les couches individuelles deviennent presque invisibles à l'œil nu, mais une impression standard de 4 heures devient un marathon de 12 à 16 heures. Ces profils s'associent mieux à des diamètres de buse plus petits (0,2 mm ou 0,25 mm) où la buse peut résoudre des détails plus fins.

**Haute qualité (0,12 mm)** atteint le point idéal pour les pièces fonctionnelles qui nécessitent encore une apparence professionnelle. Les lignes de couche sont minimales, les durées d'impression restent raisonnables, et la plupart des buses de 0,4 mm gèrent confortablement cette hauteur.

**Standard (0,20 mm)** est le profil de référence. Les lignes de couche sont visibles mais nettes, les durées d'impression sont prévisibles, et c'est là que la plupart des débutants devraient commencer.

**Brouillon (0,28 mm+)** privilégie la vitesse à la beauté. Parfait pour vérifier l'ajustement, imprimer de grands objets où les lignes de couche importent peu, ou itérer rapidement sur des prototypes de conception.

### Profils de vitesse : trouver le bon rythme

Les imprimantes Bambu Lab intègrent quatre modes de vitesse sélectionnables qui ajustent tous les paramètres de mouvement proportionnellement.^[11]^^[12]^ Bien que les noms soient propres à Bambu, les principes sous-jacents s'appliquent à toute imprimante.

| Mode | Variation de vitesse | Idéal pour | Compromis |
|------|---------------------|-----------|-----------|
| **Silent** | ≈50 % du standard | Impressions nocturnes, environnements de bureau | Plus silencieux, durée d'impression la plus longue |
| **Standard** | Vitesses de base (100 %) | Impression quotidienne polyvalente | Bon équilibre qualité/vitesse |
| **Sport** | ≈124 % du standard | Itération plus rapide quand la qualité le permet | Légère réduction de qualité |
| **Ludicrous** | ≈166 % du standard | Impressions urgentes, grands objets riches en remplissage | Bruit le plus élevé, artefacts potentiels |

Selon l'analyse de la communauté du code source de Bambu Studio, « pratiquement tout change » entre les modes de vitesse : les limites de vitesse, la vitesse de déplacement, les valeurs d'accélération, le pressure advance et les paramètres de look-ahead changent tous.^[11]^ Notamment, les températures de buse ne s'ajustent pas automatiquement, ce qui signifie que des modes de vitesse plus élevés peuvent nécessiter d'augmenter manuellement les températures pour maintenir le débit.

⚠️ **Avertissement :** Des vitesses plus élevées nécessitent des températures plus élevées pour maintenir une extrusion constante, ce qui peut dégrader les performances des porte-à-faux et des ponts. Pour l'impression axée sur la qualité sur les imprimantes Bambu, rester en dessous de 100 mm/s pour les parois extérieures est une recommandation courante de la communauté, environ 80 mm/s offrant un bon équilibre entre vitesse, qualité d'impression et résistance.^[13]^

### Paramètres de température par matériau

La **température de buse** est l'un des paramètres les plus influents de l'impression 3D.^[14]^ Elle affecte la viscosité du filament, la résistance d'adhérence des couches, le brillant de la surface, la tendance au filage et la qualité des ponts et des porte-à-faux. Le tableau suivant fournit des plages de départ pour les matériaux courants ; vérifiez toujours la fiche technique du fabricant et validez avec une tour de température pour votre filament spécifique :^[15]^

| Matériau | Temp. buse | Temp. plateau | Enceinte | Ventilateur de refroidissement |
|----------|-----------|--------------|----------|-------------------------------|
| **PLA** | 190-220°C | 45-60°C | Ouverte | 100 % |
| **PETG** | 230-250°C | 70-90°C | Ouverte | 30-50 % |
| **ABS** | 240-260°C | 90-110°C | 45-55°C | 0-20 % |
| **ASA** | 250-270°C | 90-110°C | 45-55°C | 0-20 % |
| **TPU** | 210-240°C | 30-60°C | Ouverte | 50 % |
| **Nylon** | 250-300°C | 70-110°C | 45-60°C | 30-50 % |
| **PC (Polycarbonate)** | 260-310°C | 100-120°C | 55-65°C | 30-50 % |

Ces plages constituent des points de départ standards de la communauté ; les valeurs optimales réelles varient selon la marque et la couleur du filament.^[15]^

📝 **Note :** La colonne de température d'enceinte fait référence aux enceintes chauffées activement. Pour l'ABS, l'ASA, le Nylon et le PC, maintenir une température d'enceinte élevée est essentiel pour éviter le gauchissement et la séparation des couches sur les impressions de grande taille.^[16]^

Pour chaque matériau, commencez toujours par la température recommandée par le fabricant et utilisez une **tour de température** (abordée au Chapitre 4) pour trouver la valeur optimale pour votre rouleau de filament spécifique. Même les filaments du même type et de la même marque peuvent varier de ±10°C entre les couleurs en raison de la charge en pigment.

### Configuration du refroidissement : pourquoi la vitesse du ventilateur est importante

Différents matériaux nécessitent des stratégies de refroidissement radicalement différentes. Comprendre pourquoi vous rendra un opérateur d'imprimante nettement meilleur.^[17]^^[18]^

Le **PLA** aime le refroidissement. C'est un matériau à basse température qui se solidifie rapidement, et l'utilisation intensive du ventilateur (80-100 % après les 2 à 3 premières couches) améliore la qualité des porte-à-faux, des ponts et la finition de surface.^[19]^

Le **PETG** occupe un terrain intermédiaire. Trop de refroidissement produit des couches faibles et fragiles car le filament ne se soude pas correctement. Trop peu de refroidissement entraîne un affaissement sur les porte-à-faux. La plage de 30 à 50 % est un point de départ courant.^[20]^

**L'ABS et l'ASA** nécessitent un refroidissement minimal. Ces matériaux se rétractent considérablement lors du refroidissement, et les soumettre au flux d'un ventilateur provoque un gauchissement et des fissures de couche. L'enceinte chauffée de l'imprimante se charge du maintien de la température, pas le ventilateur de refroidissement des pièces.^[16]^

Le **TPU** utilise très peu de ventilateur car c'est un matériau flexible qui a besoin de temps pour se lier entre les couches. Un refroidissement excessif peut provoquer une délamination.

Les logiciels de découpe modernes mettent également en œuvre un **refroidissement dynamique** — ajustant automatiquement la vitesse du ventilateur en fonction de la durée d'impression des couches et du pourcentage de porte-à-faux. Lorsqu'une couche s'imprime très rapidement (petite section transversale), le logiciel peut ralentir la vitesse d'impression ou augmenter la vitesse du ventilateur pour assurer un refroidissement adéquat avant que la couche suivante ne soit déposée.^[17]^

### Paramètres de support

La configuration des supports équilibre l'imprimabilité par rapport à la difficulté de retrait des supports :

- **Angle seuil de porte-à-faux :** L'angle auquel les supports sont générés automatiquement. 45° est une valeur par défaut courante dans les logiciels de découpe comme Cura et PrusaSlicer, ce qui signifie que les surfaces inclinées à plus de 45° par rapport à la verticale recevront des supports.^[21]^ Les imprimantes bien réglées avec un bon refroidissement des pièces peuvent souvent pousser ce seuil à 55-60° avant que les supports ne deviennent nécessaires.
- **Couches d'interface :** 2 à 3 couches de matériau de support dense entre la structure de support et le modèle créent une surface de séparation propre. Plus de couches d'interface signifie un retrait plus facile mais plus de matériau utilisé.
- **Motif de support :** Les motifs en grille offrent les supports les plus solides ; les supports arborescents utilisent moins de matériau et sont plus faciles à retirer, mais prennent plus de temps à découper.

### Avancé : paramètres de la première couche

La première couche est le fondement de chaque impression. La réussir n'est pas négociable.^[22]^

**Vitesse plus lente :** Les premières couches doivent s'imprimer à vitesse réduite — Simplify3D recommande de réduire de 30 à 50 % la vitesse normale pour donner au filament le temps supplémentaire de se lier avec le plateau d'impression.^[22]^ En termes absolus, cela correspond généralement à environ 15-25 mm/s pour les paramètres standard.

**Température plus élevée :** Augmentez la température de la buse de 5 à 10°C pour la première couche. La chaleur supplémentaire améliore l'adhérence et le débit.

**Pas de refroidissement des pièces :** Le ventilateur de refroidissement des pièces doit être éteint pour les 2 à 4 premières couches. Un refroidissement précoce empêche une adhérence correcte et peut provoquer un gauchissement.

**Compensation du pied d'éléphant :** Le pied d'éléphant est le léger renflement à la base d'une impression, causé par un écrasement excessif de la première couche ou une température de plateau élevée. Les logiciels de découpe offrent des paramètres de compensation — « Elephant Foot Compensation » dans PrusaSlicer/OrcaSlicer réduit automatiquement les dimensions des périmètres de la première couche. Les valeurs recommandées sont de 0,1 à 0,2 mm pour la correction d'un léger renflement. Les solutions alternatives comprennent la réduction de la température du plateau de 5 à 10°C, l'augmentation légère du décalage Z ou la réduction du débit de la première couche à 90-95 %.

💡 **Astuce de pro :** Pour une hauteur de couche de 0,2 mm, de nombreux opérateurs expérimentés définissent un décalage Z d'environ -0,05 mm, créant environ 25 % d'écrasement. Comme l'explique Simplify3D, cela force l'extrusion « dans un espace de 75 % de la hauteur de couche » — cette légère compression maximise l'adhérence au plateau sans provoquer de pied d'éléphant excessif.^[22]^

### Points clés à retenir

- La **hauteur de couche** est le principal contrôle de qualité : 0,08 mm pour les figurines, 0,12 mm pour les pièces détaillées, 0,20 mm pour un usage général, 0,28 mm+ pour les brouillons rapides. Une buse de 0,4 mm couvre environ 25–80 % de son diamètre (0,08–0,32 mm).^[10]^
- Les **profils de vitesse** arbitrent entre bruit et durée d'une part, et qualité d'autre part. Restez en dessous de 100 mm/s pour les parois extérieures importantes pour la qualité, quelle que soit la vitesse maximale annoncée par votre imprimante.^[13]^
- La **température varie considérablement selon le matériau :** le PLA à 190-220°C nécessite 100 % de ventilateur, tandis que l'ABS à 240-260°C nécessite 0-20 % de ventilateur avec une enceinte chauffée.^[15]^^[16]^
- La **stratégie de refroidissement dépend du matériau :** le PLA veut un refroidissement intensif ; l'ABS n'en veut presque pas. Une mauvaise approche de refroidissement ruine des impressions par ailleurs parfaites.^[17]^
- Les **paramètres de la première couche** sont sacrés : imprimez plus lentement (30-50 % de la vitesse normale), plus chaud, gardez le ventilateur éteint et utilisez la compensation du pied d'éléphant si nécessaire.^[22]^

---

## Chapitre 3 : Profils spécifiques à Bambu Lab

📝 **Note :** Ce chapitre se concentre sur les fonctionnalités et les flux de travail spécifiques à l'écosystème Bambu Lab (Bambu Studio, imprimantes Bambu et AMS). Les concepts sont utiles pour tous les opérateurs d'imprimantes, mais les interfaces et les fonctionnalités décrites ici sont propres à Bambu.

L'écosystème Bambu Lab intègre le matériel, le logiciel et les services cloud d'une manière qui simplifie la gestion des profils, mais introduit également des flux de travail uniques. Comprendre ces fonctionnalités spécifiques au système vous aidera à tirer le meilleur parti de votre imprimante Bambu.

### Préréglages système par modèle d'imprimante

Lorsque vous lancez Bambu Studio pour la première fois, il télécharge des « bundles de configuration » pour chaque imprimante prise en charge. Ces bundles contiennent des préréglages de processus, de filament et d'imprimante pré-réglés et optimisés pour chaque modèle spécifique.^[6]^ Les préréglages disponibles dépendent entièrement de l'imprimante et de la buse que vous avez sélectionnées.

| Imprimante | Volume de construction | Enceinte | Temp. buse max | Caractéristiques clés des profils |
|-----------|----------------------|----------|----------------|----------------------------------|
| **X1 Carbon** | 256 × 256 × 256 mm | Oui | 300°C | Lidar, compensation de vibrations, compatible AMS |
| **P1S** | 256 × 256 × 256 mm | Oui | 300°C | Similaire au X1C sans lidar |
| **P1P** | 256 × 256 × 256 mm | En option | 300°C | Cadre ouvert, enceinte requise pour ABS/ASA |
| **A1** | 256 × 256 × 256 mm | Non | 300°C | Plateau mobile, axé sur PLA/PETG |
| **A1 Mini** | 180 × 180 × 180 mm | Non | 300°C | Compact, profils de niveau entrée |

Lorsque vous sélectionnez un modèle d'imprimante ou un diamètre de buse différent, les préréglages système se mettent automatiquement à jour. Cela vous empêche d'appliquer accidentellement des valeurs d'accélération spécifiques au X1C à un A1 Mini, par exemple. Cependant, cela signifie également que vous devez faire attention à l'imprimante actuellement sélectionnée lors de la création ou de la modification de préréglages.

### Profils de filament génériques vs. Bambu Lab

Bambu Studio propose deux catégories de préréglages de filament :

Les **profils de filament génériques** sont des configurations de point de départ pour les types de matériaux courants (Generic PLA, Generic PETG, Generic ABS). Ils fonctionnent avec n'importe quelle marque de filament mais ne sont pas optimisés pour une marque spécifique. Ce sont vos bases de référence.

Les **profils de filament Bambu Lab** sont spécifiquement réglés pour les propres produits de filament de Bambu. Ces profils incluent des **données d'étiquette RFID** — lorsque vous chargez une bobine de filament Bambu dans un AMS, l'imprimante lit l'étiquette et sélectionne automatiquement le profil correct. Cette sélection automatique élimine les devinettes et assure des résultats constants.

Les tests de la communauté montrent que les paramètres fournis par le fabricant peuvent être aléatoires. Des utilisateurs ont signalé que les profils Bambu Lab génériques peuvent surpasser les profils fournis par des fabricants tiers pour le même type de matériau.^[23]^ Cela souligne un principe important : **la marque du filament sur la bobine importe moins que l'étalonnage que vous effectuez**.

### Création de profils de filament personnalisés

Pour les filaments tiers non couverts par les préréglages de Bambu, vous devez créer un profil personnalisé. Bambu Studio propose deux méthodes :^[24]^

**Méthode 1 : Filaments personnalisés (recommandée pour les utilisateurs AMS)**

Cette approche crée un préréglage au niveau système qui apparaît comme une option sélectionnable sur les emplacements AMS de votre imprimante :

1. Accédez à **Paramètres → Filaments personnalisés → Créer nouveau**
2. Renseignez le fournisseur, le type de filament et un nom descriptif
3. Sélectionnez un filament de base dont hériter (ex. : « Generic PLA »)
4. Sélectionnez les imprimantes pour lesquelles créer des préréglages (la création par lot fait gagner du temps)
5. Le filament personnalisé devient disponible pour être attribué aux emplacements AMS

Cette méthode nécessite le firmware 1.6.6 ou ultérieur sur les imprimantes X1 et X1C.^[24]^ L'avantage principal est l'intégration AMS — votre filament personnalisé apparaît sur l'écran tactile de l'imprimante comme les filaments Bambu officiels.

**Méthode 2 : Enregistrer comme préréglage utilisateur**

1. Modifiez un préréglage de filament existant (réglez les températures, le débit, etc.)
2. Cliquez sur **Enregistrer** et choisissez soit **Préréglage utilisateur** (réutilisable entre projets, peut être synchronisé avec le cloud) soit **Préréglage de projet** (enregistré uniquement dans le fichier .3MF courant)

### Flux de travail pour filament personnalisé : les cinq étapes

Pour tout nouveau filament, suivez ce flux de travail systématique :

1. **Sélectionnez le type de matériau de base** — Commencez par le profil générique correspondant à votre matériau (Generic PLA pour le PLA, etc.).
2. **Ajustez les températures à l'aide d'une tour de température** — Imprimez votre propre tour de température et sélectionnez la température la plus basse qui donne de bons résultats. Nous couvrirons cela en détail au Chapitre 4.
3. **Définissez le débit (flow rate) en fonction de l'étalonnage** — Mesurez et ajustez à l'aide de la méthode du cube à paroi unique ou de la méthode visuelle d'OrcaSlicer. Différents pigments affectent le diamètre effectif.^[4]^
4. **Configurez le refroidissement pour votre matériau** — Adaptez les vitesses de ventilateur aux exigences du matériau (référez-vous au tableau de refroidissement du Chapitre 2).
5. **Enregistrez comme préréglage personnalisé** — Utilisez la Méthode 1 ci-dessus pour la compatibilité AMS, ou la Méthode 2 pour de simples préréglages utilisateur.

### Profils AMS vs. profils mono-matériau

Lors de l'utilisation du **système de matériaux automatique (AMS)**, les profils acquièrent des dimensions supplémentaires :

- **Mappage des filaments :** Chaque emplacement AMS est associé à un profil de filament. Le logiciel de découpe utilise ces attributions pour générer les tours de purge et les trajectoires d'outil spécifiques aux couleurs.
- **Volumes de purge :** Lors du changement entre les couleurs, le logiciel calcule la quantité de filament à purger pour éviter la contamination des couleurs. Cela dépend du profil, car les filaments opaques nécessitent plus de purge que les filaments translucides.
- **Compatibilité des températures :** Tous les filaments dans une impression multi-matériaux doivent utiliser des températures suffisamment similaires pour que la tête d'impression partagée puisse les accommoder. PLA + ABS dans la même impression est problématique car leurs plages de températures se chevauchent à peine.

### Profils de diamètre de buse

Bambu Studio ajuste automatiquement les préréglages disponibles lorsque vous changez le diamètre de la buse. La buse standard de 0,4 mm est la valeur par défaut, mais les imprimantes Bambu Lab prennent en charge une gamme de tailles :

| Diamètre de buse | Idéal pour | Ajustement de la largeur de ligne | Considérations de vitesse |
|-----------------|-----------|----------------------------------|--------------------------|
| **0,2 mm** | Détails ultra-fins, figurines, textes | 0,2-0,25 mm | Impression lente ; fragile, sujette aux bouchons |
| **0,4 mm** | Usage général, par défaut | 0,4-0,5 mm | Vitesse et qualité équilibrées |
| **0,6 mm** | Pièces plus solides, impression plus rapide, grands objets | 0,6-0,72 mm | ~1,5x plus rapide pour la même hauteur de couche ; lignes de couche visibles |
| **0,8 mm** | Pièces structurelles, vases, prototypage rapide | 0,8-1,0 mm | Le plus rapide ; finition de surface rugueuse |

Les buses plus grandes nécessitent des profils de vitesse ajustés. Une buse de 0,6 mm extrude significativement plus de plastique par seconde qu'une buse de 0,4 mm à la même vitesse, ce qui signifie que votre limite de **vitesse volumétrique maximale (max volumetric speed)** devient le facteur limitant. Nous explorerons ce concept critique au Chapitre 4.

### Synchronisation des profils entre Studio et l'imprimante

Les préréglages utilisateur peuvent être téléversés sur Bambu Cloud et automatiquement téléchargés lorsque vous vous connectez à Bambu Studio sur un autre ordinateur.^[6]^ C'est inestimable si vous utilisez plusieurs postes de travail. Gardez à l'esprit les limites de compte : 20 préréglages d'imprimante, 100 préréglages de processus et 200 préréglages de filament.^[7]^

📝 **Note :** « En raison des ressources cloud limitées, les préréglages pour les imprimantes non-Bambu Lab ne sont actuellement pas pris en charge pour la synchronisation cloud. »^[6]^ Si vous utilisez Bambu Studio avec des imprimantes tierces, conservez des sauvegardes locales de vos préréglages.

### Profils de la communauté

La communauté de l'impression 3D maintient d'importants dépôts de profils. Lors de l'évaluation d'un profil communautaire :

1. **Vérifiez la source** — Les profils de membres bien connus de la communauté avec un historique de tests documenté sont plus fiables.
2. **Vérifiez la compatibilité** — Assurez-vous que le profil correspond exactement à votre modèle d'imprimante et à votre taille de buse.
3. **Examinez le champ inherits** — Lors de l'importation de profils OrcaSlicer, « faites très attention au contenu des fichiers .json, en particulier aux champs inherits… vous devez vous assurer que le profil parent hérité est également placé à son emplacement correct. »^[9]^
4. **Testez avant de faire confiance** — Même les profils communautaires très bien notés doivent être vérifiés avec une impression d'étalonnage avant de s'engager dans une longue production.

### Points clés à retenir

- Les **préréglages système** sont des bases de référence verrouillées, spécifiques à l'imprimante. Copiez-les vers des préréglages utilisateur avant de les modifier.^[6]^
- Les **filaments personnalisés** pour une utilisation AMS doivent être créés via Paramètres → Filaments personnalisés (requiert le firmware 1.6.6+) pour l'intégration sur l'écran tactile.^[24]^
- Le **diamètre de la buse** affecte tous les préréglages disponibles. La largeur de ligne et les limites de vitesse s'adaptent à la taille de la buse.
- Les **profils Bambu génériques** surpassent souvent les paramètres fournis par le fabricant — testez et étalonnez toujours.^[23]^
- La **synchronisation cloud** maintient la cohérence des préréglages entre les ordinateurs, mais ne prend pas en charge les imprimantes non-Bambu et a des limites (20/100/200 préréglages).^[7]^
- Les **profils communautaires** sont des ressources précieuses, mais vérifiez toujours la compatibilité et testez avant de faire confiance.^[9]^

---

## Chapitre 4 : Étalonnage et réglage fin

C'est ici que les bonnes impressions deviennent excellentes. L'étalonnage est le processus systématique qui consiste à mesurer le comportement réel de votre imprimante et à ajuster les profils en conséquence. Ce n'est pas facultatif — même une imprimante parfaitement assemblée avec des profils d'usine par défaut produira des résultats sous-optimaux tant qu'elle n'aura pas été étalonnée pour votre filament et votre environnement spécifiques.

### La chaîne d'interdépendance des étalonnages

⚠️ **Avertissement :** Les paramètres d'étalonnage forment une chaîne de dépendance. Modifier un paramètre sans re-vérifier les paramètres en aval est la cause la plus fréquente de problèmes de qualité d'impression « mystérieux ».^[25]^ La température affecte le débit (flow rate) ; le débit affecte le pressure advance ; le pressure advance affecte la rétraction ; la qualité de la rétraction détermine le filage ; et le filage plus le débit déterminent la qualité de la surface.

L'ordre correct est critique car « de nombreux paramètres sont interdépendants. Commencer par les paramètres fondamentaux garantit des résultats précis pour les ajustements suivants, plus nuancés. »^[25]^ Par exemple, le débit doit être étalonné avant le pressure advance car « si le débit est incorrect, le PA compensera de manière inexacte. »^[25]^

### L'ordre d'étalonnage

Suivez cette séquence exactement :

| Étape | Étalonnage | Ce qu'il optimise | Pourquoi l'ordre est important |
|-------|-----------|------------------|---------------------------------|
| 1 | **Tour de température** | Comportement de fusion et de liaison | Doit être défini en premier car la température affecte la viscosité du débit |
| 2 | **Débit (flow rate)** | Quantité d'extrusion correcte | Dépend de la température ; doit être précis avant l'étalonnage du PA |
| 3 | **Pressure advance** | Qualité des angles et retard d'extrusion | Dépend d'un débit correct ; un débit incorrect fait compenser le PA de manière inexacte |
| 4 | **Rétraction** | Contrôle du filage et du suintement | Dépend du PA ; la rétraction fonctionne mieux quand la pression d'extrusion est déjà gérée |
| 5 | **Vitesse volumétrique maximale** | La vraie limite de vitesse de votre tête d'impression | Dépend de la température et du débit ; définit le plafond pour tous les paramètres de vitesse |

### Étape 1 : Tour de température

Une **tour de température** est un modèle d'étalonnage divisé en sections verticales, chacune imprimée à une température de buse différente.^[26]^ Elle « concentre une étude complète de température en une seule impression contrôlée » avec des segments typiquement par pas de 5°C.^[27]^

**Comment imprimer et interpréter :**

1. Générez un fichier STL de tour de température avec des éléments de test intégrés (ponts, porte-à-faux, fines tiges)
2. Configurez le logiciel de découpe pour changer la température à des hauteurs de couche spécifiques à l'aide d'un G-code personnalisé (`M104 Sxxx`)
3. Ajoutez une pause de 20 à 30 secondes ou purgez 3 à 5 mm de filament après chaque changement de température pour stabiliser les conditions de fusion^[27]^
4. Imprimez la tour et attendez un refroidissement complet avant de la manipuler

Évaluez chaque section selon plusieurs critères :

| Critère | Trop froid | Optimal | Trop chaud |
|---------|-----------|---------|-----------|
| **Finition de surface** | Mate, rugueuse | Lisse, satinée | Brillante, inégale |
| **Filage** | Minimal | Minimal à nul | Filaments excessifs |
| **Adhérence des couches** | Faible, les couches peuvent se séparer | Solide, couches fusionnées | Bonne mais peut perdre des détails |
| **Ponts** | Peut échouer en raison d'un mauvais débit | Plats, bien soutenus | Affaissement dû à la chaleur excessive |
| **Porte-à-faux** | Mauvaise liaison | Bords nets | Affaissement dû à la mollesse |

💡 **Astuce de pro :** Effectuez un test de flexion sur les parois minces de la tour de température. Les sections imprimées trop froid produisent des couches fragiles qui se fendent sous une légère flexion ; les sections trop chaud montrent des affaissements et du filage.^[27]^ Sélectionnez la **température la plus basse qui donne de bons résultats** — cela minimise le filage et maximise les détails tout en assurant une adhérence adéquate des couches.

**Plages de test recommandées :**

| Matériau | Plage de test | Optimal typique |
|----------|--------------|----------------|
| PLA | 185-220°C | 200-210°C |
| PETG | 230-250°C | 240°C |
| ABS | 230-260°C | 245°C |
| TPU | 210-230°C | 220°C |

Séchez toujours votre filament avant les tests de température. L'humidité provoque des bulles et du filage qui peuvent être confondus avec des problèmes liés à la température.^[27]^

### Étape 2 : Étalonnage du débit (flow rate)

« Si le débit est mauvais, chaque paroi de chaque impression est incorrecte dans la même proportion. Les dimensions sont fausses, les parois sont faibles ou rugueuses. »^[4]^ Le débit (aussi appelé **multiplicateur d'extrusion**) contrôle la quantité de filament extrudée par rapport au calcul théorique du logiciel de découpe.

**Méthode du cube à paroi unique (la plus précise) :**

1. **Configuration du slicer :** Configurer une paroi unique, 0 % de remplissage, 0 couche supérieure, avec une largeur de ligne égale au diamètre de la buse (ex. : 0,4 mm)
2. **Impression :** Un cube de 20 × 20 × 20 mm (ou en mode vase/spirale)
3. **Mesure :** Épaisseur de la paroi avec un pied à coulisse numérique au centre de chaque paroi, en évitant les coins
4. **Calcul :** Prenez 3 à 4 mesures par paroi et faites la moyenne de toutes les lectures
5. **Appliquez la formule :**

```
Nouveau débit = Ancien débit × (Épaisseur cible / Épaisseur mesurée)
```

Exemple : si cible = 0,4 mm et mesuré = 0,36 mm :
```
New Flow = 1.00 × (0.4 / 0.36) = 1.11
```
Augmentez le débit d'environ 11 %.^[4]^

**Méthode visuelle OrcaSlicer :**

OrcaSlicer propose une approche visuelle intégrée en deux passes :^[25]^^[28]^

- **Passe 1 (grossière) :** 9 blocs avec des modificateurs de débit. Sélectionnez le bloc avec la surface supérieure la plus lisse.
- **Passe 2 (fine) :** 10 blocs avec des modificateurs de -9 à 0. Sélectionnez à nouveau la meilleure surface.
- Calculez : `NouveauDébit = AncienDébit × (100 + modificateur) / 100`

⚠️ **Avertissement :** Utilisateurs de Bambu Lab X1/X1C — lorsque vous utilisez l'étalonnage d'OrcaSlicer, assurez-vous de **ne pas** sélectionner l'option « Calibration du débit » intégrée de l'imprimante. Les exécuter simultanément produit des résultats peu fiables.^[28]^

### Étape 3 : Pressure Advance

Le **pressure advance (PA)** compense le retard de la pression d'extrusion lorsque la tête d'impression change de vitesse. Selon la documentation Klipper, il « fait deux choses utiles — il réduit le suintement pendant les déplacements sans extrusion et il réduit les bavures dans les virages. »^[29]^ Sans PA, les coins gonflent en raison d'une pression excessive lors de la décélération et sous-extrudent lors de l'accélération.

Différents firmwares utilisent des noms différents pour le même concept :

| Firmware | Nom | Plage de valeurs typique |
|----------|-----|--------------------------|
| Marlin | Linear Advance (facteur K) | 0,0 - 2,0+ (v1.5 ; entraînement direct généralement < 0,2)^[30]^ |
| Klipper | Pressure Advance | 0,050 - 1,000 (entraînement direct généralement 0,02–0,08)^[29]^ |
| Bambu Lab | Flow Dynamics | Auto-étalonné par l'imprimante^[31]^ |

**Méthode par motif OrcaSlicer (recommandée) :**

La méthode par motif d'OrcaSlicer imprime un prisme avec des valeurs PA croissantes. Vous identifiez visuellement la section avec les coins les plus nets et le moins d'artefacts.^[25]^ Cette méthode est plus robuste que la méthode en ligne, qui est sensible à la qualité de la première couche.

**Méthode de la tour Klipper :^[29]^**

1. Imprimez un carré creux à haute vitesse avec 0 % de remplissage
2. Définissez des limites conservatrices : `SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500`
3. Exécutez la tour de réglage :
   - Entraînement direct : `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.005`
   - Bowden : `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.020`
4. Inspectez les coins et calculez : `pressure_advance = début + (hauteur mesurée × facteur)`
   - Exemple : `0 + 12,90 × .020 = 0,258`^[29]^

| Configuration | Plage typique de PA |
|--------------|-------------------|
| Entraînement direct | 0,020 — 0,080 |
| Bowden | 0,150 — 1,000+ |

Les valeurs de PA nécessitent un ajustement lors de changements significatifs de vitesse d'impression — le même PA qui fonctionne à 60 mm/s peut ne pas fonctionner à 200 mm/s.

### Étape 4 : Étalonnage de la rétraction

La **rétraction** tire le filament vers l'arrière avant les déplacements, créant une pression négative pour éviter le suintement et le filage.^[32]^ Une rétraction correcte dépend du type d'extrudeur :

| Paramètre | Entraînement direct | Tube Bowden |
|-----------|--------------------|-----------  |
| **Distance de rétraction** | 0,5-2,0 mm | 4-6 mm |
| **Vitesse de rétraction** | 25-45 mm/s | 40-45 mm/s |

^[33]^

**Comment étalonner :**

1. Utilisez Calibration → Retraction Test d'OrcaSlicer (ou un fichier STL de tour de rétraction)
2. Définissez la longueur de départ, la longueur de fin et l'incrément
3. Pour l'entraînement direct : commencez à 0,5 mm, incrémentez de 0,25 mm
4. Pour Bowden : commencez à 1,0 mm, incrémentez de 0,5 mm
5. Évaluez : recherchez la **distance de rétraction la plus courte** qui produit un filage minimal sans provoquer de bouchons ou de sous-extrusion au démarrage des lignes^[32]^^[33]^

Au-delà de la distance et de la vitesse, gardez à l'esprit ces facteurs en interaction :

- **Des températures plus élevées** augmentent le suintement et nécessitent une rétraction plus agressive
- **Une vitesse de déplacement plus rapide** (120-250 mm/s) réduit le filage en donnant moins de temps à la buse pour suinter pendant les déplacements
- **Le Z-hop** soulève la buse pendant les déplacements (0,2-0,5 mm) pour éviter les traînées, mais peut aggraver le suintement
- **Le filament humide** provoque du filage quels que soient les paramètres de rétraction — séchez d'abord votre filament^[33]^

### Étape 5 : Vitesse volumétrique maximale (MVS)

Voici le concept le plus important dans l'étalonnage de vitesse — et celui que les débutants ignorent le plus souvent.

La **vitesse volumétrique maximale (max volumetric speed, MVS)** est le débit auquel votre tête d'impression peut fondre et extruder le filament de manière fiable, mesurée en mm³/s. C'est la limite de vitesse fondamentale de toute imprimante 3D.^[34]^ Quelle que soit la rapidité du système de déplacement de votre imprimante, votre tête d'impression ne peut fondre qu'une certaine quantité de plastique par seconde.

C'est ce qui crée **l'illusion de vitesse** : les fabricants annoncent des vitesses de 500 mm/s voire 1 000 mm/s, mais ces chiffres ne sont atteignables que dans des conditions très spécifiques. À une hauteur de couche de 0,2 mm et une largeur de ligne de 0,45 mm, 300 mm/s exige déjà 27 mm³/s de capacité de fusion — au-delà de ce que même de nombreuses têtes d'impression à haut débit peuvent soutenir en continu.

**La formule :^[34]^**

```
Vitesse d'impression (mm/s) = MVS (mm³/s) / (Hauteur de couche (mm) × Largeur de ligne (mm))
```

**Exemple :** À une hauteur de couche de 0,2 mm, une largeur de ligne de 0,4 mm et une MVS de 10 mm³/s :
```
Speed = 10 / (0.2 × 0.4) = 10 / 0.08 = 125 mm/s
```

Mais à une hauteur de couche de 0,3 mm avec la même largeur de ligne et la même MVS :
```
Speed = 10 / (0.3 × 0.4) = 10 / 0.12 = 83 mm/s
```

C'est pourquoi la MVS est plus robuste qu'une simple limite de vitesse linéaire — elle tient automatiquement compte des combinaisons de hauteur de couche et de largeur de ligne.^[34]^

**Limites typiques de MVS par tête d'impression :^[35]^**

| Tête d'impression | Vitesse volumétrique maximale | Remarques |
|------------------|------------------------------|-----------|
| V6 standard (PLA) | ~11,5-15 mm³/s | PLA ; descend à ~8 mm³/s pour le PETG |
| E3D Volcano | ~25 mm³/s | Zone de fusion plus grande |
| Bambu Lab X1C standard | ~20-22 mm³/s | Limite pratique testée par la communauté pour le PLA |

📝 **Note :** Les conceptions SuperVolcano et CHT à haut débit dépassent largement ces valeurs, mais les plages pratiques spécifiques varient considérablement selon la configuration et sont mieux déterminées par un étalonnage individuel plutôt qu'assumées à partir des fiches techniques.

**Comment étalonner la MVS avec OrcaSlicer :^[36]^**

1. Utilisez les valeurs par défaut : départ à 5 mm³/s, fin à 20 mm³/s, pas de 0,5
2. Imprimez le modèle de test et observez où les couches commencent à montrer une sous-extrusion (couches minces avec des lacunes)
3. Mesurez la hauteur au point de défaillance avec un pied à coulisse
4. Calculez : `MVS = départ + (hauteur mesurée × pas)`
5. Réduisez de 5 à 10 % pour une marge de sécurité

Définissez votre MVS étalonnée comme limite dans votre profil de filament. Le logiciel de découpe plafonnera alors automatiquement les vitesses pour s'assurer que votre tête d'impression ne dépasse jamais sa capacité de fusion.

### Quand recalibrer

L'étalonnage n'est pas « réglé et oublié ». Un recalibrage est nécessaire quand :^[25]^

- **Un nouveau filament** est introduit — même différentes couleurs de la même marque peuvent nécessiter des températures et des débits différents
- **Des modifications matérielles** se produisent — une nouvelle tête d'impression, un extrudeur, un tube Bowden ou une buse changent tous la dynamique du système
- **La qualité d'impression se dégrade** de manière inattendue — cela indique souvent qu'un paramètre a dérivé
- **Les objectifs de vitesse changent significativement** — les valeurs de PA en particulier nécessitent un ajustement à différentes vitesses

💡 **Astuce de pro :** Tenez un journal d'étalonnage — une simple feuille de calcul avec les dates, les marques de filament et vos valeurs étalonnées. Lorsque vous revenez à un filament après des mois, vous aurez vos paramètres éprouvés à disposition au lieu de recommencer de zéro.

### Points clés à retenir

- **L'ordre d'étalonnage est critique :** Température → Débit → Pressure Advance → Rétraction → Vitesse volumétrique maximale. Chaque étape dépend de la précision de la précédente.^[25]^
- Les **tours de température** trouvent le point de fusion optimal. Choisissez la température la plus basse qui produit de bons résultats sur les ponts, les porte-à-faux et la finition de surface.^[27]^
- Le **débit (flow rate)** affecte chaque dimension de chaque impression. Utilisez la méthode du cube à paroi unique pour la précision ou la méthode visuelle d'OrcaSlicer pour la commodité.^[4]^^[28]^
- Le **pressure advance** élimine les bavures dans les virages. Étalonnez-le seulement après que le débit est correct. Valeurs typiques Klipper : 0,050–1,000 ; l'entraînement direct se situe généralement entre 0,02 et 0,08.^[29]^
- La **rétraction** prévient le filage. Entraînement direct : 0,5-2,0 mm à 25-45 mm/s. Bowden : 4-6 mm à 40-45 mm/s. Commencez de manière conservatrice et augmentez juste assez pour éliminer le suintement.^[33]^
- La **vitesse volumétrique maximale** est la vraie limite de vitesse — pas le maximum annoncé par l'imprimante. Une tête V6 standard plafonne à ~11,5-15 mm³/s pour le PLA (moins pour le PETG). C'est pourquoi les vitesses annoncées de 500+ mm/s ne sont atteignables que dans des conditions très spécifiques.^[35]^
- **Recalibrez** chaque fois que vous changez de filament, de buse ou de matériel, ou lorsque la qualité d'impression se dégrade mystérieusement.^[25]^

---

## Résumé du Module 6

Ce module vous a accompagné depuis la compréhension de ce qu'est un profil d'impression jusqu'à l'étalonnage systématique pour obtenir des résultats optimaux. Les fils conducteurs qui traversent les quatre chapitres sont :

1. **Les profils sont des systèmes hiérarchiques** — les niveaux imprimante, filament et processus interagissent et se contraignent mutuellement. Comprendre cette structure fait de vous un diagnostiqueur plus efficace.

2. **Partez de bases éprouvées** — les préréglages génériques de sources réputées sont vos meilleurs alliés. Modifiez-les systématiquement, un paramètre à la fois.

3. **La chaîne d'étalonnage est interdépendante** — la température affecte le débit, le débit affecte le pressure advance, le pressure advance affecte la rétraction. Respectez l'ordre.

4. **La vitesse volumétrique maximale est la vraie limite de vitesse** — pas le chiffre marketing sur la boîte. Comprendre la MVS vous permet de définir des attentes réalistes et d'éviter la sous-extrusion à haute vitesse.

5. **L'étalonnage est continu** — les nouveaux filaments, les modifications matérielles et même les variations saisonnières de température dans votre salle d'impression peuvent affecter les paramètres optimaux. Tenez un journal et recalibrez quand nécessaire.

Avec ces principes intégrés, vous êtes désormais équipé pour obtenir des impressions constantes et de haute qualité avec n'importe quel matériau et n'importe quel niveau de qualité de votre choix.

---

## Sources

Les sources ci-dessous correspondent aux références citées dans ce module. Les numéros, URL, dates et noms propres sont identiques à la version anglaise.

1. OrcaSlicer / Obico — « Guide de démarrage avec OrcaSlicer » (structure de profil à trois niveaux, préréglages processus/filament/imprimante) — <https://www.obico.io/blog/orcaslicer-comprehensive-calibration-guide/>
2. 3DPrinting.com — « Meilleurs logiciels de découpe 3D 2026 » (OrcaSlicer issu de Bambu Studio ; large prise en charge d'imprimantes ; compatibilité entre logiciels) — <https://3dprinting.com/best-3d-printer-slicers/>
3. Obico — « Le guide complet d'étalonnage OrcaSlicer » (niveau profil filament : températures, refroidissement, rétraction, débit, valeur K du pressure advance) — <https://www.obico.io/blog/orcaslicer-comprehensive-calibration-guide/>
4. Obico — « Étalonnage du débit dans OrcaSlicer : un guide complet » (formule méthode cube à paroi unique ; la charge en pigment affecte le débit ; « chaque paroi de chaque impression est incorrecte ») — <https://www.obico.io/blog/flow-rate-calibration-orca-slicer-comprehensive-guide/>
5. Prusa Knowledge Base — « Paramètres d'impression » (contenu du profil processus : hauteur de couche, parois, remplissage, vitesses, supports) — <https://help.prusa3d.com/article/print-settings_177225>
6. Bambu Lab Wiki — « Comment créer un préréglage personnalisé » (préréglages système/utilisateur/projet ; « ne peuvent pas être modifiés directement » ; sélection de préréglages selon la buse ; synchronisation cloud pour imprimantes non-Bambu) — <https://wiki.bambulab.com/en/software/bambu-studio/create-preset>
7. Forum communautaire Bambu Lab — « Comprendre la limite des préréglages utilisateur cloud » (limite cloud : 20 imprimantes / 100 processus / 200 filaments) — <https://forum.bambulab.com/t/understanding-cloud-user-presets-limit-custom-filament-setup/181259>
8. Obico — « Gestion des profils OrcaSlicer : le guide ultime » (export/import ; bundles `.orca_printer` / `.orca_filament`) — <https://www.obico.io/blog/orcaslicer-profile-management/>
9. GitHub OrcaSlicer Wiki — « Gestion des profils » (champ « inherits » ; emplacement correct du profil parent pour un chargement correct) — <https://github.com/OrcaSlicer/OrcaSlicer/wiki/profile-management>
10. Kingroon — « La hauteur de couche en impression 3D » (règle 25 %–80 % du diamètre de la buse ; buse 0,4 mm max ~0,32 mm) — <https://kingroon.com/blogs/3d-print-101/layer-height-in-3d-printing>
11. Forum communautaire Bambu Lab — « AVC : COMMENCEZ ICI ! Calibrage simplifié » (analyse communautaire : « pratiquement tout change » entre les modes de vitesse — vitesse, accélération, PA, look-ahead) — <https://forum.bambulab.com/t/psa-start-here-calibration-made-simple-please-share-user-tips/10932>
12. Forum communautaire Bambu Lab — « Ordre des calibrages Bambu Lab X1 Carbon » (ordre de calibrage confirmé par la communauté pour les imprimantes Bambu) — <https://forum.bambulab.com/t/order-of-calibrations-bambu-lab-x1-carbon/32349>
13. Forum communautaire Bambu Lab — « Paramètres Polymaker PLA Pro » (recommandation communautaire : rester en dessous de 100 mm/s pour la qualité ; ~80 mm/s meilleur compromis) — <https://forum.bambulab.com/t/polymaker-pla-pro-settings/>
14. FlashForge Wiki — « Introduction aux paramètres de découpe » (la température de buse comme facteur principal de qualité d'impression) — <https://wiki.flashforge.com/en/Orca-Flashforge-and-Flashmaker/Introduction_to_Slicing_Parameters>
15. 3d4create — « Températures d'impression 3D optimales pour PLA, ABS, PETG, TPU, Nylon » (plages de températures par matériau : PLA 190-220°C, PETG 230-250°C, ABS 240-260°C, PC 260-310°C) — <https://3d4create.com/3d-printing-temperatures-for-pla-abs-petg-tpu-nylon/>
16. Siraya Tech — « Température d'impression ABS » (ventilateur minimal pour ABS/ASA ; enceinte chauffée essentielle pour les grandes impressions) — <https://siraya.tech/blogs/news/abs-3d-printer-temperature>
17. Prusa Knowledge Base — « Refroidissement » (stratégie de refroidissement dynamique ; logique de ventilateur selon le matériau ; exceptions ABS/PC) — <https://help.prusa3d.com/article/cooling_127569>
18. JLC3DP — « Guide de refroidissement en impression 3D » (aperçu du refroidissement matériau par matériau) — <https://jlc3dp.com/blog/3d-printing-cooling-guide>
19. Sovol — « Optimiser le refroidissement du filament » (PLA ventilateur intensif 80-100 % après les premières couches) — <https://www.sovol3d.com/blogs/news/optimize-filament-cooling>
20. Overture — « Paramètres d'impression PETG » (PETG ventilateur 30-50 % ; trop de refroidissement affaiblit la liaison entre couches) — <https://overture3d.com/blogs/overture-blogs/petg-print-settings-guide>
21. Snapmaker — « Le guide ultime de la règle des 45 degrés en impression 3D » (seuil de porte-à-faux par défaut 45° dans les logiciels courants ; les imprimantes bien réglées peuvent pousser à 55-60°+) — <https://www.snapmaker.com/blog/45-degree-rule-3d-printing/>
22. Simplify3D — « Perfectionner la première couche » (vitesse réduite de 30-50 % ; décalage Z -0,05 mm = 25 % d'écrasement ; « forcée dans 75 % de la hauteur de couche ») — <https://www.simplify3d.com/resources/articles/perfecting-the-first-layer/>
23. Forum communautaire Bambu Lab — « Paramètres eSUN vs préréglages génériques » (preuve communautaire que les profils BBL génériques surpassent certains paramètres fournis par le fabricant) — <https://forum.bambulab.com/t/esun-parameters-vs-generic-presets/>
24. Bambu Lab Wiki — « Créer des filaments personnalisés dans Bambu Studio » (flux de travail filament personnalisé ; exigence firmware 1.6.6 ; intégration emplacement AMS) — <https://wiki.bambulab.com/en/bambu-studio/create-filament>
25. Obico — « Le guide complet d'étalonnage OrcaSlicer » (chaîne d'interdépendance des calibrages ; dépendance « débit avant PA » ; déclencheurs de recalibrage) — <https://www.obico.io/blog/orcaslicer-comprehensive-calibration-guide/>
26. Creality — « Qu'est-ce qu'une tour de température en impression 3D ? » (définition de la tour de température ; changements de température par G-code) — <https://www.creality.com/blog/temperature-tower>
27. The Virtual Foundry — « Optimiser les impressions 3D avec les tours de température » (pas de 5°C ; pause de 20-30 s ; test de flexion sur parois minces ; « affaissement de pont, gonflement de couture Z, enroulement de bord de porte-à-faux ») — <https://thevirtualfoundry.com/temp-tower-3d-printing/>
28. OrcaSlicer Wiki — « Étalonnage du rapport de débit » (Passe 1 : 9 blocs ; Passe 2 : 10 blocs, modificateurs -9 à 0 ; avertissement Bambu Lab « ne pas sélectionner Calibration du débit ») — <https://github.com/OrcaSlicer/OrcaSlicer/wiki/flow_ratio_calib>
29. Documentation Klipper — « Pressure Advance » (réduit le suintement + les bavures de virages ; commandes de la tour de réglage ; plage typique 0,050–1,000 ; exemple 0 + 12,90 × .020 = ,258) — <https://www.klipper3d.org/Pressure_Advance.html>
30. Prusa Knowledge Base — « Linear Advance » (valeurs K de LA Marlin par matériau avec buse 0,4 mm ; plage v1.5) — <https://help.prusa3d.com/article/linear-advance_2252>
31. BabaBuilds — « Calibrage de la dynamique de débit Bambu Lab — valeur K » (Flow Dynamics Bambu = pressure advance ; X1 auto-étalonné par lidar ; A1 par capteur à courants de Foucault ; K typique 0,005–0,030 pour plastiques rigides) — <https://bababuilds.com/blog/bambu-lab-flow-dynamics-calibration-k-value/>
32. Obico — « Test de rétraction dans OrcaSlicer » (la rétraction réduit le suintement ; calibrage par test de rétraction ; distance minimale qui élimine le filage) — <https://www.obico.io/blog/retraction-test-orca-slicer/>
33. Polymaker Wiki — « Déplacement et rétraction » (entraînement direct 0,5-1 mm / 25-45 mm/s ; Bowden 4-6 mm / 40-45 mm/s ; le filament humide provoque du filage quels que soient les paramètres) — <https://wiki.polymaker.com/the-basics/3d-slicers/travel-and-retraction>
34. Polymaker Wiki — « La vitesse volumétrique maximale limite votre vitesse d'impression » (formule MVS : Vitesse = MVS / (Hauteur de couche × Largeur de ligne) ; la vitesse linéaire seule ne tient pas compte du volume de matériau) — <https://wiki.polymaker.com/the-basics/fun-3d-printing-facts/max-volumetric-speed-limits-your-print-speed>
35. Prusa Knowledge Base — « Vitesse volumétrique maximale » (E3D V6 annoncé 15 mm³/s, sûr ~11,5 mm³/s pour PLA, ~8 mm³/s pour PETG ; Volcano ~25 mm³/s) — <https://help.prusa3d.com/article/max-volumetric-speed_127176>
36. OrcaSlicer Wiki — « Étalonnage de la vitesse volumétrique maximale » (valeurs par défaut : départ 5 mm³/s, fin 20 mm³/s, pas 0,5 ; calculer MVS = départ + hauteur × pas) — <https://github.com/OrcaSlicer/OrcaSlicer/wiki/volumetric-speed-calib>

### Pour aller plus loin

- Documentation Klipper — référence complète d'étalonnage incluant l'input shaping : <https://www.klipper3d.org/Overview.html>
- Prusa Knowledge Base — documentation complète des paramètres du logiciel de découpe : <https://help.prusa3d.com/category/print-settings_282>
- OrcaSlicer Wiki — guide d'étalonnage officiel avec ordre de test recommandé : <https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration>
- Ellis' Print Tuning Guide — réglage approfondi du pressure advance, de l'écrasement de la première couche et du refroidissement pour Klipper/Marlin : <https://ellis3dp.com/Print-Tuning-Guide/>
