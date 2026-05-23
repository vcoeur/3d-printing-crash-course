# Module 5 : Maîtriser les logiciels de tranchage

Votre imprimante 3D ne vaut que ce que valent les instructions que vous lui donnez. Le trancheur est le pont critique entre votre vision créative et l'objet physique qui sort de l'imprimante. Dans ce module, nous allons explorer le flux de travail complet du tranchage — du modèle numérique à la pièce physique —, plonger en profondeur dans Bambu Studio, le trancheur au cœur de l'écosystème Bambu Lab, passer en revue l'ensemble du paysage des trancheurs, notamment OrcaSlicer et PrusaSlicer, et débloquer les fonctionnalités avancées qui séparent les utilisateurs occasionnels des véritables maîtres de l'art.

Que vous imprimiez votre premier Benchy ou que vous affiniez des profils pour des matériaux à usage technique, comprendre en profondeur votre trancheur est la compétence au meilleur rapport résultat/effort que vous puissiez développer en impression 3D.

---

## Chapitre 1 : Comprendre le tranchage

Imaginez que vous essayez de construire une sculpture en empilant des milliers de crêpes ultra-fines, chacune découpée à une forme précise, l'une sur l'autre. C'est fondamentalement ce que fait une **imprimante 3D** — et le **trancheur** est le logiciel qui décide exactement à quoi ressemble chaque crêpe, où va le « glaçage » (filament fondu), et dans quel ordre tout est déposé.

Le tranchage transforme un modèle 3D numérique en **G-code** — le langage précis que votre imprimante comprend.^[1]^ Chaque mouvement, changement de température et commande d'extrusion prend naissance dans le trancheur. Maîtrisez le trancheur, et vous maîtrisez l'impression.

### Le pipeline de tranchage : du modèle au G-code

Le flux de travail complet de tranchage suit une séquence d'étapes bien définie :^[1]^

1. **Importation** — Chargement d'un fichier de modèle 3D (STL, 3MF, OBJ ou STEP) dans le trancheur
2. **Orientation** — Positionnement, rotation et mise à l'échelle du modèle sur le plateau de construction virtuel
3. **Tranchage** — Le logiciel découpe mathématiquement le modèle en centaines ou milliers de couches horizontales
4. **Génération des trajectoires** — Pour chaque couche, le trancheur calcule le chemin exact que doit suivre la buse
5. **Génération du G-code** — Toutes les instructions sont compilées dans un fichier G-code contenant des commandes de déplacement (`G1`), des commandes de température (`M104`/`M109`), des commandes de ventilateur (`M106`), et bien d'autres

Considérez le trancheur comme un traducteur. Vous vous exprimez en modèles 3D ; votre imprimante parle en commandes moteur bas niveau. Le trancheur est le seul qui parle couramment les deux langages.

### Le flux de travail en huit étapes dans la pratique

Parcourons ensemble le flux de travail complet que vous suivrez pour chaque impression :

**Étape 1 : Importer le modèle.** Vous commencez par ouvrir votre fichier de modèle. La plupart des trancheurs prennent en charge le glisser-déposer. Le modèle apparaît sur le plateau de construction virtuel sous forme de maillage 3D.

**Étape 2 : Positionner et orienter.** Le positionnement a plus d'importance que la plupart des débutants ne le réalisent. Les surfaces planes doivent généralement être orientées vers le bas pour assurer la stabilité. Les surplombs doivent être minimisés en réorientant le modèle. Les outils d'orientation automatique du trancheur peuvent aider, mais l'ajustement manuel donne souvent de meilleurs résultats.

**Étape 3 : Mettre à l'échelle si nécessaire.** Vérifiez les dimensions par rapport à l'usage prévu. Les trancheurs offrent une mise à l'échelle uniforme et non uniforme. Une pièce conçue en pouces mais exportée en millimètres arrivera 25,4 fois trop grande — une erreur courante et coûteuse.

**Étape 4 : Configurer les paramètres d'impression.** C'est là que la magie opère. La hauteur de couche, le nombre de parois, le motif de remplissage, les paramètres de support, les températures et les vitesses se combinent ici. Nous couvrirons chacun de ces éléments en détail plus loin dans ce chapitre.

**Étape 5 : Ajouter des supports si nécessaire.** Tout surplomb supérieur à environ 45-55° nécessitera un matériau de support. Les trancheurs modernes peuvent générer automatiquement des supports, mais le contrôle manuel (peinture de supports) donne des résultats supérieurs pour les modèles complexes.

**Étape 6 : Trancher.** Cliquez sur le bouton Trancher, et le logiciel effectue ses calculs. Pour un modèle complexe, cela peut prendre de quelques secondes à plusieurs minutes.

**Étape 7 : Prévisualiser les couches et les trajectoires.** Le mode aperçu est votre point de contrôle qualité. Inspectez couche par couche, observez les déplacements à vide, et vérifiez que les supports sont bien placés. Détecter les problèmes ici vous économise des heures d'impressions ratées.

**Étape 8 : Exporter le G-code ou envoyer à l'imprimante.** La dernière étape produit un fichier `.gcode` (ou l'envoie directement via le réseau) vers votre imprimante. Certains écosystèmes, comme Bambu Lab, permettent l'envoi sans fil ; d'autres nécessitent une carte SD ou une connexion USB.

### Comprendre les formats de fichiers

Tous les fichiers de modèles 3D ne se valent pas. Le format que vous utilisez influence tout, de la taille du fichier à la possibilité de transporter vos paramètres de tranchage avec le modèle.

| Format | Année | Idéal pour | Limitation principale |
|--------|-------|------------|----------------------|
| **STL** | 1987 | Compatibilité universelle | Pas de couleur, pas d'unités, pas de paramètres, sujet aux erreurs de maillage |
| **3MF** | 2015 | Standard moderne ; préserve les paramètres | Non pris en charge par les très anciens logiciels |
| **OBJ** | Années 1990 | Prise en charge des couleurs et textures | Fichiers volumineux, peut nécessiter des fichiers complémentaires |
| **STEP** | 1994 | Géométrie native CAO | Nécessite des trancheurs prenant en charge l'import CAO direct |

Le tableau ci-dessus résume les quatre principaux formats ; les détails suivent.^[2]^^[3]^

**STL (Stereolithography)** a été créé en 1987 par Charles Hull de 3D Systems pour les toutes premières imprimantes stéréolithographiques.^[2]^ Sa seule fonction était de décrire la surface d'un objet 3D à l'aide d'un maillage de triangles. Les fichiers STL ne contiennent aucune information de couleur, aucune donnée de matériau, aucune unité, et sont notoirement sujets aux erreurs de maillage telles que les trous, les normales inversées et les arêtes non-manifold. Malgré ces limitations, le STL reste le format le plus largement pris en charge en raison de son ancienneté et de sa simplicité.

**3MF (3D Manufacturing Format)** a été publié pour la première fois en avril 2015 par le consortium 3MF — un groupe de leaders industriels comprenant Autodesk, Dassault Systèmes, HP, Microsoft et Shapeways — spécifiquement pour résoudre chacun des problèmes du STL.^[3]^ Il a été standardisé sous la norme **ISO/IEC 25422:2025**, consolidant son statut de successeur industriel officiel au STL.^[4]^ Les fichiers 3MF sont plus petits, se compressent automatiquement, stockent les paramètres du trancheur avec le modèle, prennent en charge les données de couleur et de matériau, et sont exempts d'erreurs par conception.^[3]^ PrusaSlicer utilise le 3MF comme format de sauvegarde de projet par défaut, et Bambu Studio s'appuie fortement dessus.^[5]^

> 💡 **Astuce de pro :** Faites du 3MF votre format par défaut pour tout. N'utilisez le STL que lorsqu'une plateforme spécifique ou un collaborateur vous y oblige. Si vous rencontrez des fichiers STL comportant des erreurs de maillage, faites-les passer par un outil de réparation (Microsoft 3D Builder, l'intégration Netfabb de PrusaSlicer, ou Meshmixer) avant de trancher.

**OBJ** prend en charge les textures, les couleurs et les propriétés de matériau, et permet un rendu de haute qualité, bien qu'il puisse produire des fichiers volumineux et nécessite parfois la gestion de plusieurs fichiers complémentaires pour les textures. Les fichiers **STEP** sont fondamentalement différents — ils contiennent une géométrie mathématique précise (surfaces NURBS) plutôt que des maillages triangulés. Certains trancheurs modernes, notamment PrusaSlicer 2.5 et versions ultérieures, peuvent importer des fichiers STEP directement, contournant entièrement l'étape de conversion en maillage et produisant des résultats plus nets.^[6]^

### Aperçu des paramètres clés

Le trancheur contrôle des dizaines de paramètres. Voici les plus importants, organisés par catégorie :

#### Paramètres de qualité

- **Hauteur de couche :** Le principal déterminant de la résolution verticale et du temps d'impression. Des valeurs plus faibles produisent des détails plus fins mais prennent plus de temps. Une buse standard de 0,4 mm peut imprimer des hauteurs de couche d'environ 0,08 mm (ultra-fin) à 0,32 mm (mode brouillon). La hauteur de couche doit généralement rester en dessous de 80 % du diamètre de la buse.^[7]^
- **Largeur de ligne :** La largeur de chaque ligne extrudée. Les trancheurs modernes utilisent le générateur de périmètres **Arachne**, qui ajuste automatiquement la largeur d'extrusion pour une meilleure qualité — il a été développé à l'origine par l'équipe Cura et introduit dans PrusaSlicer en version 2.5 (septembre 2022).^[6]^^[8]^
- **Nombre de parois/périmètres :** Le nombre de coques solides autour de l'extérieur. Plus de parois signifie des pièces plus solides.
- **Couches supérieures/inférieures :** Couches pleines en haut et en bas de l'impression. Typiquement 3 à 5 couches de chaque côté.

#### Paramètres de remplissage

- **Densité de remplissage :** Pourcentage de l'intérieur qui est rempli. 15-20 % est standard pour les pièces générales ; 0 % pour les vases ; 40 % et plus pour les pièces fonctionnelles portant des charges.
- **Motif de remplissage :** Le motif géométrique de la structure interne. Les options courantes incluent **Gyroid** (résistance quasi-isotrope — égale dans toutes les directions — et bonne absorption d'énergie), **Honeycomb**, **Grid** et **Cubic**. Le remplissage gyroid surpasse généralement le grid en termes de résistance multidirectionnelle ; le cubic est généralement supérieur pour la résistance à la compression.^[9]^

| Motif de remplissage | Résistance relative | Notes |
|----------------------|---------------------|-------|
| Grid | Modérée | Rapide ; idéal pour les charges simples du haut vers le bas |
| Gyroid | Élevée (multidirectionnelle) | Résistance égale dans toutes les directions ; bonne résistance au cisaillement |
| Cubic | Élevée (compression) | Idéal pour les charges compressives verticales |
| Honeycomb | Modérée | Classique ; plus lent que le grid |

#### Paramètres de support

- **Type de support :** Les **supports en arbre** utilisent significativement moins de matériau que les supports standard (jusqu'à 25-50 % sur les modèles complexes), sont plus faciles à retirer, et laissent moins de marques sur la surface.^[10]^ Ils se ramifient organiquement depuis le plateau d'impression comme les branches d'un arbre. Les **supports standard** utilisent une structure de grille rigide et conviennent mieux aux surplombs importants ou aux géométries simples.
- **Seuil de surplomb :** L'angle auquel les supports sont générés automatiquement. Pour le PLA, 55-60° fonctionne bien avec un refroidissement actif ; l'ABS/ASA nécessite des seuils plus bas de 40-45°.
- **Interface de support :** Une couche supérieure lisse sur le support qui améliore la finition de la surface supportée. Deux couches d'interface est une bonne valeur par défaut.

#### Aides à l'adhérence au plateau

Trois outils répondent aux défis d'adhérence de la première couche :

| Fonctionnalité | Jupe | Bordure | Radeau |
|----------------|------|---------|--------|
| **Connexion au modèle** | Aucune (contour séparé) | Connectée aux bords | Sous toute la base |
| **Couches** | 1 contour | 1 couche | Plusieurs (3+) |
| **Idéal pour** | Amorçage de la buse, vérification du niveau | Prévention du gauchissement, pièces hautes/minces | Problèmes graves d'adhérence au plateau |
| **Post-traitement** | Aucun | Léger rognage | Ponçage nécessaire |

#### Température, vitesse et refroidissement

- **Température de la buse :** Contrôle comment le filament fond et s'écoule. Trop froid provoque une sous-extrusion ; trop chaud provoque le suintement et les fils.
- **Température du plateau :** Assure l'adhérence de la première couche. Spécifique au matériau — PLA à 50-60 °C, ABS à 100-110 °C.
- **Vitesse d'impression :** Pas une valeur unique mais une hiérarchie — les parois extérieures sont les plus lentes pour la qualité, le remplissage est le plus rapide pour le débit, la première couche est la plus lente de toutes.
- **Ventilateur de refroidissement :** Essentiel pour le PLA (80-100 % après les couches initiales) ; minimal pour l'ABS (0-20 %) pour éviter le gauchissement.

#### Contrôles d'extrusion avancés

- **Rétraction :** Retire le filament avant les déplacements à vide pour éviter les fils. Les extrudeurs à entraînement direct utilisent typiquement 1-2 mm ; les systèmes Bowden nécessitent 4-6 mm.^[11]^
- **Z-Hop :** Lève la buse lors des déplacements à vide (typiquement 0,2-0,5 mm) pour éviter les collisions avec les pièces imprimées, bien que cela puisse légèrement augmenter les fils.
- **Peigne (Combing) :** Maintient les déplacements à vide à l'intérieur du modèle pour minimiser les fils sur les surfaces extérieures.

### Comprendre l'aperçu des couches

L'aperçu des couches est votre dernier point de contrôle avant de dépenser du filament et du temps. Voici ce qu'il faut rechercher :

- **Codage couleur :** La plupart des trancheurs codent par couleur les types de fonctionnalités — parois, remplissage, supports, déplacements à vide. Apprenez la légende de votre trancheur.
- **Déplacements à vide :** Surveillez les longs trajets qui traversent des zones ouvertes. Ce sont des occasions de formation de fils. Activez la rétraction ou le peigne si vous observez des trajets problématiques.
- **Points de contact des supports :** Vérifiez que les supports ne touchent que là où c'est nécessaire. Les supports en arbre doivent avoir des points de contact minimaux.
- **Transitions de couche :** Vérifiez les premières couches pour les éléments d'adhérence (jupe, bordure). Vérifiez que les supports commencent sur le plateau, pas en l'air.
- **Placement de la couture :** La **couture en Z** est la ligne verticale visible où chaque couche commence et se termine. Les trancheurs peuvent la placer aléatoirement, alignée sur un coin, ou cachée à l'arrière.

### Estimer le temps d'impression et la consommation de filament

Les trancheurs modernes fournissent des estimations précises du temps d'impression et de la consommation de filament avant même de démarrer une impression. Ces estimations tiennent compte de l'accélération, du jerk et des déplacements à vide — pas seulement des calculs de distance simples. Utilisez ces chiffres pour planifier votre programme d'impression et vérifier que vous avez suffisamment de filament sur la bobine. Une bonne règle empirique : ajoutez 10-15 % de marge à l'estimation de filament pour les déchets, les supports et le matériau de jupe/bordure.

> ⚠️ **Avertissement :** Les estimations de temps des trancheurs supposent des conditions optimales. Les impressions réelles prennent souvent 10-30 % de temps supplémentaire en raison du temps de chauffe, du nivellement automatique du plateau, des événements de pause et des inévitables ajustements de la première couche.

### Points clés à retenir

- Le tranchage transforme un modèle 3D en G-code à travers un pipeline d'importation, d'orientation, de génération de couches, de calcul de trajectoires et de compilation d'instructions.^[1]^
- **Le 3MF a remplacé le STL comme standard moderne** (ISO/IEC 25422:2025) — utilisez-le autant que possible pour ses fichiers plus petits, ses maillages sans erreur, et sa capacité à préserver les paramètres du trancheur.^[3]^^[4]^
- Les cinq catégories de paramètres clés sont : **Qualité** (hauteur de couche, parois), **Remplissage** (motif, densité), **Supports** (arbre vs. standard), **Adhérence au plateau** (jupe, bordure, radeau), et **Température/Vitesse** (température de buse, vitesse d'impression, refroidissement).
- Inspectez toujours l'**aperçu des couches** avant d'imprimer. C'est votre dernière et meilleure chance de détecter les problèmes.
- Le **remplissage Gyroid** offre une résistance quasi-isotrope (uniforme dans toutes les directions), ce qui en fait un choix polyvalent solide.^[9]^
- Les **supports en arbre** utilisent significativement moins de matériau que les supports standard et sont plus faciles à retirer.^[10]^

---

## Chapitre 2 : Plongée en profondeur dans Bambu Studio

Bambu Studio est le trancheur officiel développé par Bambu Lab, forké à partir de PrusaSlicer en 2022.^[12]^ Il représente une évolution significative dans l'arbre généalogique des trancheurs — héritant de la base de code mature et éprouvée de PrusaSlicer tout en ajoutant une interface moderne, une intégration matérielle transparente et des fonctionnalités connectées au cloud qui en font le trancheur de référence pour les propriétaires d'imprimantes Bambu Lab.^[13]^

Si vous possédez une imprimante Bambu Lab X1, P1P, P1S ou A1, Bambu Studio est conçu spécifiquement pour vous. Sa disposition en trois panneaux — paramètres à gauche, vue 3D au centre, aperçu à droite — est claire, intuitive et largement considérée comme l'une des interfaces les plus soignées et les plus accessibles aux débutants parmi les trancheurs modernes.^[13]^

> 📝 **Note :** Bambu Studio est **spécifique à Bambu Lab**. Bien qu'il prenne en charge certaines imprimantes tierces, la prise en charge des imprimantes non-Bambu est secondaire et moins soignée.^[13]^ Si vous possédez plusieurs marques d'imprimantes, OrcaSlicer (couvert au chapitre 3) pourrait être plus adapté.

### Présentation de l'interface : les quatre onglets principaux

Bambu Studio organise son flux de travail en quatre onglets principaux :^[13]^

| Onglet | Objectif | Actions clés |
|--------|----------|--------------|
| **Prepare** | Configuration et manipulation des modèles | Importer, orienter, peindre les supports, configurer les paramètres |
| **Preview** | Inspection couche par couche | Vérifier les trajectoires, contrôler les supports, estimer le temps |
| **Device** | Contrôle et surveillance de l'imprimante | Envoyer des impressions, voir la caméra, vérifier l'état |
| **Project** | Gestion multi-plateau | Organiser plusieurs plateaux de construction, mise en page par lots |

#### Onglet Prepare

L'onglet Prepare est là où vous passez la majeure partie de votre temps. Le panneau gauche présente vos sélections **Imprimante**, **Filament** et **Processus** sous forme de listes déroulantes simples avec des valeurs par défaut bien choisies.^[13]^ Sous ces sélecteurs, les paramètres de processus sont organisés en catégories extensibles : Quality, Strength, Support et Others.

Les outils clés dans la barre d'outils supérieure comprennent :
- **Auto-Arrange :** Positionne intelligemment plusieurs modèles sur le plateau de construction
- **Auto-Orient :** Trouve l'orientation optimale pour les surplombs et l'adhérence au plateau
- **Support Painting :** Définir manuellement où les supports sont imposés ou bloqués
- **Text Shape :** Embosser ou graver du texte directement sur les modèles
- **Measure :** Vérifier les dimensions sans quitter le trancheur
- **Cut :** Découper les modèles en parties séparées pour les impressions multicolores ou d'assemblage

#### Onglet Preview

Après le tranchage, l'onglet Preview devient votre centre de contrôle qualité. Le curseur de couche vertical vous permet de faire défiler chaque couche de l'impression. La légende montre différentes couleurs pour les parois, le remplissage, les déplacements à vide et les supports. Portez une attention particulière à :

- **Les déplacements à vide** (généralement affichés dans une couleur distincte comme le rouge ou l'orange) — minimisez les longs déplacements traversant des zones ouvertes
- **Les points de contact des supports** — vérifiez qu'ils sont minimaux et stratégiquement placés
- **Le placement de la couture** — vérifiez que la couture en Z est cachée à l'arrière ou à l'intérieur du modèle

#### Onglet Device

L'onglet Device se connecte à votre imprimante via votre réseau local ou Bambu Cloud. Depuis là, vous pouvez :
- Surveiller le flux de la caméra en direct pendant l'impression
- Voir la progression de l'impression, les températures et le temps restant
- Mettre en pause, reprendre ou annuler des impressions à distance
- Gérer l'AMS (Automatic Material System) et le chargement du filament

#### Onglet Project

Pour les travaux complexes, l'onglet Project permet la **gestion multi-plateau** — organiser différents modèles sur plusieurs plateaux de construction virtuels, chacun avec des paramètres indépendants. C'est indispensable pour les fermes d'impression ou la production en série.

### Sélection et configuration de l'imprimante

Lors du premier lancement de Bambu Studio, vous sélectionnez votre modèle d'imprimante (par ex., « Bambu Lab X1 Carbon 0.4mm »). Cette sélection charge un **ensemble de configuration** contenant des préréglages de processus, de filament et d'imprimante pré-réglés, optimisés pour ce matériel spécifique.^[13]^

Lorsque vous changez de taille de buse (par ex., de 0,4 mm à 0,2 mm), les paramètres de processus disponibles se mettent automatiquement à jour.^[13]^ Les préréglages de qualité, les paramètres de vitesse, et même les hauteurs de couche recommandées changent tous pour correspondre aux capacités de la nouvelle buse.

### Flux de travail de sélection des filaments et des profils

Le système de profils à trois niveaux dans Bambu Studio fonctionne comme suit :^[13]^

1. **Profil Imprimante/Machine** — Définit les dimensions du plateau, la taille de la buse, le type de firmware, le G-code de début/fin, et les limites de sécurité (vitesse max, accélération)
2. **Profil Filament** — Contient les paramètres thermiques et d'extrusion spécifiques au matériau : températures, courbes du ventilateur de refroidissement, débit, rétraction et pressure advance
3. **Profil Processus** — Contrôle la stratégie de tranchage : hauteur de couche, nombre de parois, remplissage, vitesses, supports et fonctionnalités spéciales

Bambu Studio fournit des **préréglages système** pour chaque imprimante prise en charge — ceux-ci sont verrouillés à l'édition mais peuvent être dupliqués et modifiés en **préréglages utilisateur**.^[13]^ Le flux de travail est simple : sélectionnez votre imprimante, choisissez un filament, choisissez un préréglage de processus, puis affinez selon vos besoins.

#### Filaments personnalisés

Pour les filaments tiers (eSUN, Overture, Sunlu, etc.), Bambu Studio offre deux approches :^[13]^

**Méthode 1 : Filaments personnalisés (recommandée pour les utilisateurs AMS)**
Naviguez vers Settings → Custom Filaments → Create New. Sélectionnez le fournisseur, le type de filament et le nom. Choisissez un filament de base dont hériter, puis sélectionnez les imprimantes pour lesquelles créer des préréglages.

**Méthode 2 : Enregistrer comme préréglage utilisateur**
Modifiez un préréglage de filament existant, puis enregistrez-le comme préréglage utilisateur ou préréglage de projet. Les préréglages utilisateur se synchronisent entre les appareils via Bambu Cloud ; les préréglages de projet ne vivent que dans le fichier `.3MF` actuel.

> 💡 **Astuce de pro :** Les paramètres fournis par les fabricants peuvent être inégaux avec les filaments tiers. En cas de doute, commencez avec les préréglages génériques de Bambu Lab pour le même type de matériau et calibrez à partir de là — l'expérience communautaire montre systématiquement que cela donne de meilleurs résultats de base que les paramètres spécifiques à la marque des fournisseurs moins connus.

### Exploration approfondie des paramètres de processus

Bambu Studio organise les paramètres de processus en catégories logiques. Voici ce que chacune contrôle :

#### Catégorie Quality

| Paramètre | Description | Plage typique |
|-----------|-------------|---------------|
| **Layer Height** | Résolution verticale | 0,08-0,32 mm (buse 0,4 mm) |
| **Line Width** | Largeur d'extrusion | 0,4-0,6 mm |
| **Wall Loops** | Nombre de périmètres | 2-4 (plus pour la résistance) |
| **Top/Bottom Shells** | Couches de surface pleines | 3-5 couches |
| **Seam Position** | Placement de la couture en Z | Alignée, la plus proche, aléatoire |

#### Catégorie Strength

| Paramètre | Description | Valeurs recommandées |
|-----------|-------------|---------------------|
| **Infill Pattern** | Géométrie interne | Gyroid (meilleure résistance multidirectionnelle), Grid, Honeycomb |
| **Infill Density** | Pourcentage de remplissage interne | 15-20 % général, 40 %+ fonctionnel |
| **Wall Order** | Séquence paroi intérieure/extérieure | Intérieur d'abord (résistance), extérieur d'abord (qualité) |
| **Solid Infill Direction** | Angle pour les couches supérieures/inférieures | 45° par défaut |

Le remplissage gyroid offre une résistance quasi-isotrope (uniforme dans toutes les directions) — un bon choix par défaut pour les pièces devant supporter des charges multidirectionnelles.^[9]^

#### Catégorie Speed

Les imprimantes Bambu Lab implémentent un système de **modes de vitesse** sélectionnable pendant l'impression.^[14]^ Les quatre modes appliquent un multiplicateur par rapport à la référence Standard (100 %) :

| Mode | Multiplicateur de vitesse | Idéal pour |
|------|--------------------------|-----------|
| **Silent** | 50 % | Impression silencieuse, impressions nocturnes |
| **Standard** | 100 % (référence) | Usage quotidien, bonne qualité |
| **Sport** | 124 % | Impressions plus rapides, légère compromise de qualité |
| **Ludicrous** | 166 % | Tests de vitesse, prototypes |

Entre les modes, la vitesse, le déplacement, l'accélération, les valeurs de pressure advance et les valeurs de look-ahead changent tous.^[14]^ Les températures de buse ne changent pas entre les modes.

Bambu Studio implémente également **« Slow Down for Overhangs »** — une fonctionnalité qui réduit automatiquement la vitesse d'impression en fonction du pourcentage de surplomb.^[15]^ Le degré de surplomb est calculé comme le pourcentage de largeur de filament non soutenu par la couche inférieure.

#### Catégorie Support

| Paramètre | Description |
|-----------|-------------|
| **Support Type** | Arbre (organique) ou Normal (grille) |
| **Overhang Threshold** | Angle pour la génération automatique de supports (par défaut : 55° pour PLA) |
| **Top Z Distance** | Espace entre le support et le modèle (plus grand = retrait plus facile) |
| **Interface Layers** | Couches supérieures lisses sur le support (par défaut : 2) |
| **Interface Pattern** | Lignes (la plupart des cas) ou Concentrique (surfaces irrégulières) |

Les supports en arbre sont généralement préférés pour leur efficacité matérielle et leur retrait plus facile.^[10]^ Cependant, les supports standard restent préférables pour les surplombs importants ou lorsqu'une stabilité maximale est requise.

#### Catégorie Others

- **Brim :** Extension d'adhérence monocouche, utile pour les matériaux sujets au gauchissement
- **Prime/Purge Tower :** Pour les impressions multi-matériaux, un bloc de matériau purgé lors des changements de filament
- **Arc Fitting :** Convertit de courts segments de ligne en véritables commandes d'arc G2/G3, produisant des courbes plus lisses et des fichiers G-code plus petits

### Peinture de supports : contrôle manuel pour les géométries complexes

La **peinture de supports** est l'une des fonctionnalités les plus puissantes de Bambu Studio. Elle vous permet de définir manuellement exactement où les supports doivent ou ne doivent pas être générés.^[16]^

La barre d'outils de peinture propose plusieurs outils :^[16]^
- **Crayon circulaire :** Dessiner des courbes sur les surfaces du modèle ; ne peint que les facettes visibles en surface
- **Sphère :** Colore toutes les facettes à l'intérieur d'un volume sphérique — utile pour les zones internes difficiles d'accès
- **Remplissage :** Remplit en cascade les facettes connectées avec contrôle du seuil d'angle — le plus rapide pour les grands surplombs plats
- **Remplissage des espaces :** Traite les zones d'espace pouvant résulter de la peinture avec les autres outils

Les zones peintes sont marquées comme régions **d'imposition** (support requis) ou **de blocage** (support interdit).^[16]^ Ce niveau de contrôle est essentiel pour les géométries complexes où les supports auto-générés seraient excessifs ou mal placés.

> 💡 **Astuce de pro :** Pour les modèles avec des détails fins et de grands surplombs, utilisez l'outil Remplissage pour les grandes zones et le crayon circulaire pour le travail de détail fin. Vérifiez toujours l'aperçu après la peinture — les régions d'imposition et de blocage peuvent se chevaucher, et le trancheur a des règles spécifiques sur laquelle prend la priorité.

### Configuration multi-matériaux et peinture de couleurs

L'intégration **AMS (Automatic Material System)** de Bambu Studio change la donne pour l'impression multicolore.^[13]^ L'AMS contient jusqu'à 4 bobines de filament par unité, extensible à 16 couleurs avec 4 unités AMS. Il dispose d'une identification automatique du filament par RFID pour les filaments Bambu Lab, d'un capteur d'humidité intégré avec des sachets de dessiccant, et d'une sauvegarde automatique de bobine lorsque le filament est épuisé.^[17]^

L'**outil de peinture de couleurs** fonctionne de manière similaire à la peinture de supports — utilisez un pinceau pour peindre différentes couleurs directement sur la surface du modèle. Le trancheur génère ensuite des trajectoires avec des commandes automatiques de changement de filament aux couches appropriées. Chaque changement de couleur déclenche une purge dans la tour de purge pour éviter la contamination des couleurs.

### Envoi des impressions : Cloud, LAN et carte SD

Bambu Studio offre trois façons d'envoyer des impressions à votre imprimante :

| Méthode | Connexion | Idéal pour | Note de confidentialité |
|---------|-----------|-----------|------------------------|
| **Bambu Cloud** | Internet via compte Bambu | Impression à distance, accès caméra | Nécessite une connexion au compte ; certaines fonctionnalités communiquent avec les serveurs Bambu Lab |
| **Mode LAN** | Réseau local uniquement | Utilisateurs soucieux de la confidentialité, fiabilité réseau | Pas de dépendance au cloud ; limité au réseau local |
| **Export carte SD** | Support physique | Confidentialité maximale, flux de travail hors ligne | Pas de réseau requis ; transfert de fichiers manuel |

> 📝 **Note :** Bambu Studio nécessite une connexion à un compte Bambu pour être utilisé, et les fonctionnalités cloud communiquent avec les serveurs Bambu Lab.^[13]^ Pour les utilisateurs soucieux de la confidentialité, c'est une considération importante. Bambu Lab a répondu avec d'importants investissements en sécurité, obtenant trois certifications indépendantes : ISO/IEC 27001 (gestion de la sécurité de l'information), ISO/IEC 27701 (gestion de la confidentialité) et TRUSTe Enterprise Privacy.^[18]^ Le mode LAN offre une alternative qui maintient toutes les communications sur votre réseau local.

### Sauvegarde de projets et gestion des profils

L'une des fonctionnalités les plus puissantes du 3MF est la **sauvegarde basée sur les projets**. Lorsque vous sauvegardez un projet en tant que fichier `.3mf`, il préserve :^[5]^
- Les modèles 3D eux-mêmes
- Les données de peinture de supports personnalisés
- Tous les paramètres de processus (hauteur de couche, remplissage, vitesses)
- Les informations de hauteur de couche variable
- Les maillages modificateurs et leurs paramètres
- Les positions et orientations des modèles sur le plateau de construction

Cela signifie que vous pouvez revenir à un projet des mois plus tard, ouvrir le fichier 3MF, et chaque paramètre est exactement tel que vous l'avez laissé. C'est l'outil de reproductibilité ultime.

Bambu Studio organise les préréglages de manière hiérarchique :^[13]^
- **Préréglages système :** Intégrés, fournis par le fabricant, verrouillés à l'édition
- **Préréglages utilisateur :** Vos configurations personnalisées, peuvent se synchroniser sur Bambu Cloud (20 préréglages d'imprimante, 100 préréglages de processus, 200 préréglages de filament maximum par compte)^[19]^
- **Préréglages de projet :** Paramètres sauvegardés uniquement dans le fichier 3MF actuel

> ⚠️ **Avertissement :** La synchronisation Bambu Cloud ne prend pas en charge les préréglages pour les imprimantes non-Bambu Lab.^[13]^ Si vous utilisez Bambu Studio avec des imprimantes tierces, sauvegardez vos préréglages localement via des fichiers d'exportation.

### Tranchage en mode sans tête : l'interface en ligne de commande de Bambu Studio

Tout ce qui précède s'effectue dans l'interface graphique, mais Bambu Studio propose également une **interface en ligne de commande** pour le tranchage *sans tête* — sans fenêtre, sans souris. C'est ainsi que l'on tranche sur un serveur, dans un script de traitement par lots, ou au sein d'un pipeline automatisé : une ferme d'impression, un service web « déposer et trancher », ou une intégration continue qui valide des modèles imprimables. Comme **OrcaSlicer est un fork de Bambu Studio**, les deux partagent la même interface en ligne de commande, de sorte que les options ci-dessous fonctionnent de façon quasi identique dans l'un et dans l'autre.^[20]^

Le principe : fournir au trancheur trois éléments exportés depuis l'interface graphique en `.json` — un profil **machine**, un profil de **processus** et un ou plusieurs profils de **filament** — ainsi qu'un modèle, puis lui demander de produire un **3MF** tranché contenant le G-code.

| Option | Rôle |
|--------|------|
| `--slice N` | Trancher le plateau N (`0` = tous les plateaux) |
| `--load-settings "machine.json;process.json"` | Charger la configuration imprimante + processus |
| `--load-filaments "filament.json;..."` | Charger un profil de filament par extrudeur/emplacement |
| `--export-3mf out.3mf` | Écrire le résultat en 3MF (le G-code est contenu à l'intérieur) |
| `--outputdir DIR` | Répertoire de destination des fichiers exportés |
| `--orient` | Auto-orientation avant le tranchage |
| `--arrange 1` | Auto-arrangement avant le tranchage |
| `--debug N` | Verbosité des journaux (0=fatal … 5=trace) |

Une commande minimale de bout en bout :

```bash
bambu-studio \
  --load-settings "machine.json;process.json" \
  --load-filaments "filament.json" \
  --slice 0 \
  --export-3mf output.3mf \
  model.3mf
```

La priorité des paramètres suit l'ordre suivant : **options en ligne de commande > `--load-settings` / `--load-filaments` > ce qui est intégré dans le 3MF d'entrée**.^[20]^ Le fichier `output.gcode.3mf` exporté peut être envoyé directement à une imprimante Bambu, qui accepte nativement le G-code encapsulé dans un 3MF.

> 💡 **Astuce de pro :** Pour les pipelines de traitement par lots ou de fermes d'impression, deux options supplémentaires sont importantes. `--skip-useless-pick` désactive la génération de miniatures afin d'accélérer le tranchage lorsque les aperçus sont inutiles, et `--mstpp 300` interrompt tout plateau dont le tranchage dépasse cinq minutes — sans cette option, un modèle pathologique peut bloquer l'interface en ligne de commande indéfiniment, car il n'existe pas de délai d'expiration natif.^[21]^

> ⚠️ **Avertissement :** Commencez toujours par **exporter vos profils depuis l'interface graphique**. Affinez le réglage visuellement (imprimante, filament, processus), exportez ces trois profils en `.json`, puis indiquez-les à l'interface en ligne de commande. Rédiger manuellement le JSON des profils depuis zéro est source d'erreurs et n'est pas pris en charge.

### Points clés à retenir

- Bambu Studio est le **trancheur officiel pour les imprimantes Bambu Lab**, forké à partir de PrusaSlicer en 2022, offrant l'intégration matérielle la plus étroite et une interface soignée.^[12]^^[13]^
- Le flux de travail en quatre onglets (**Prepare, Preview, Device, Project**) guide les utilisateurs de l'import du modèle jusqu'à l'impression terminée de manière efficace.^[13]^
- Le **système de profils à trois niveaux** (Imprimante, Filament, Processus) organise des centaines de paramètres en préréglages gérables et réutilisables.^[13]^
- La **peinture de supports** offre un contrôle chirurgical sur l'emplacement des supports — essentiel pour les géométries complexes.^[16]^
- L'**intégration AMS** permet une impression multicolore avec jusqu'à 16 couleurs et une identification automatique du filament.^[17]^
- Les **fichiers de projet 3MF** préservent chaque paramètre avec le modèle, garantissant une reproductibilité complète.^[5]^
- Choisissez le **mode LAN** si la dépendance au cloud est une préoccupation ; les fonctionnalités cloud de Bambu Lab nécessitent un compte et communiquent avec leurs serveurs.^[13]^^[18]^

---

## Chapitre 3 : OrcaSlicer et l'écosystème élargi

Bambu Studio est peut-être le trancheur de choix pour les propriétaires de Bambu Lab, mais il existe dans un riche écosystème de logiciels de tranchage avec une fascinante histoire évolutive. Comprendre les relations entre les trancheurs — leur ascendance commune, leurs philosophies divergentes et leurs forces uniques — vous permet de choisir le bon outil pour votre configuration spécifique et de transférer vos connaissances entre plateformes.

### L'arbre généalogique des trancheurs

Tous les principaux trancheurs FDM (avec une exception notable) partagent un lignage commun. Cette **convergence des trancheurs** signifie que les connaissances se transfèrent presque directement entre eux :^[22]^^[23]^

```
Slic3r (septembre 2011, Alessandro Ranellucci / RepRap community)
    |
    +---> PrusaSlicer (novembre 2016 sous le nom « Slic3r Prusa Edition » ; renommé en mai 2019)
    |         |
    |         +---> Bambu Studio (2022, fork Bambu Lab)
    |         |           |
    |         |           +---> OrcaSlicer (première version juillet 2022, SoftFever)
    |         |
    |         +---> SuperSlicer (fork communautaire avec réglages avancés)
    |
    +---> [Autres forks de Slic3r]

CuraEngine (moteur C++ indépendant, UltiMaker)
```

Cet arbre généalogique révèle quelque chose de remarquable : le paradigme PrusaSlicer a effectivement remporté une large adoption dans le monde du tranchage FDM. Cura, la seule base de code indépendante majeure, a connu un développement de fonctionnalités plus lent en 2024-2026 par rapport à cette famille.^[22]^ La convergence signifie que si vous apprenez un trancheur dans cette famille, vous pouvez passer à n'importe quel autre avec un minimum d'effort — les concepts, paramètres et flux de travail sont presque identiques.

### OrcaSlicer : la puissance communautaire

OrcaSlicer a été publié pour la première fois en juillet 2022 par le développeur communautaire SoftFever comme un fork de Bambu Studio, ajoutant initialement des outils de calibration et un support plus large des imprimantes.^[23]^ Il est depuis devenu l'un des trancheurs les plus utilisés dans la communauté maker.^[22]^

#### Pourquoi OrcaSlicer existe

OrcaSlicer répond à trois limitations de Bambu Studio :
1. **Pas de dépendance au cloud** — OrcaSlicer ne nécessite pas de compte Bambu
2. **Support plus large des imprimantes** — Profils optimisés pour Voron, Creality, et des dizaines d'autres marques d'imprimantes^[22]^
3. **Outils de calibration de premier ordre** — Une suite de calibration intégrée complète sans équivalent parmi les trancheurs gratuits^[22]^

#### Interface et flux de travail

OrcaSlicer hérite de la disposition en trois panneaux de Bambu Studio mais ajoute une plus grande densité de fonctionnalités. Le côté gauche dispose d'onglets pour les paramètres d'impression, de filament et d'imprimante. Un **onglet de calibration** dédié dans le menu est la fonctionnalité phare.^[22]^

OrcaSlicer cache intelligemment les paramètres avancés derrière un sélecteur de mode **Simple → Avancé → Expert**, le rendant accessible aux débutants tout en donnant aux utilisateurs avancés accès à chaque paramètre.^[22]^

#### Outils de calibration de premier ordre

C'est là qu'OrcaSlicer devance clairement tous ses concurrents. Le menu Calibration inclut des impressions de test intégrées et une analyse automatisée pour :^[25]^

| Test de calibration | Objectif | Ce qu'il faut observer |
|--------------------|---------|----------------------|
| **Temperature Tower** | Optimiser la fusion et la liaison | Moins de fils, meilleure adhérence des couches |
| **Flow Rate** | Assurer une extrusion correcte | Surface supérieure la plus lisse |
| **Pressure Advance** | Réduire les artefacts de pression | Coins les plus nets |
| **Retraction** | Minimiser les fils | Distance de rétraction la plus courte avec des résultats propres |
| **Tolerance** | Précision dimensionnelle | Ajustement optimal entre pièces complémentaires |
| **Max Volumetric Speed** | Trouver le plafond de vitesse | Vitesse maximale avant sous-extrusion |
| **Input Shaping / VFA** | Réduire les artefacts de vibration | Surfaces verticales les plus nettes |

Le tableau couvre tous les tests ; voir ci-dessous l'ordre de calibration et les détails de méthode.^[25]^

L'ordre de calibration est crucial : **Temperature → Flow Rate → Pressure Advance → Retraction → Tolerance → Max Volumetric Speed**.^[25]^ Chaque calibration s'appuie sur la précédente — le débit doit être correct avant que le pressure advance puisse être calibré avec précision, car un débit incorrect fera compenser le PA de manière inexacte.

#### Qui devrait utiliser OrcaSlicer ?

- **Utilisateurs du firmware Klipper** — Contrôle direct depuis le trancheur, y compris la surveillance par webcam
- **Ménages multi-imprimantes** — Meilleur support pour les flottes d'imprimantes mixtes
- **Utilisateurs avancés** qui veulent un contrôle maximum
- **Utilisateurs soucieux de la confidentialité** qui préfèrent ne pas dépendre du cloud
- **Utilisateurs Bambu Lab** qui veulent la flexibilité open-source et les outils de calibration

#### Limitations

- Les mises à jour sont pilotées par la communauté — les versions majeures sont moins fréquentes que Bambu Studio
- Pas de support du fabricant d'imprimante en première partie
- Peut être écrasant pour les débutants absolus en raison de la densité des fonctionnalités^[22]^

### PrusaSlicer : le standard open-source original

PrusaSlicer est la base mature et stable sur laquelle sont construits à la fois Bambu Studio et OrcaSlicer. Initialement forké depuis Slic3r en novembre 2016 sous le nom « Slic3r Prusa Edition » et rebaptisé PrusaSlicer en mai 2019, il a le plus long historique de développement continu dans cette famille.^[22]^

#### Points forts

- **Implémentation la plus soignée de la hauteur de couche variable** — Dispose d'un éditeur de courbe graphique pour affiner la hauteur de couche dans différentes régions d'un modèle^[22]^
- **Excellente peinture de supports** — Affinée au fil de nombreuses versions, outils de pinceau très intuitifs^[22]^
- **Import de fichiers STEP** — Depuis la version 2.5 (septembre 2022), PrusaSlicer importe les fichiers STEP directement, contournant la conversion en maillage pour des résultats plus nets^[6]^
- **Support SLA/MSLA** — Le seul trancheur de cette famille avec une prise en charge complète de l'impression résine
- **Entièrement open-source** — Sous licence AGPL, avec le processus de développement le plus transparent

#### Limitations

- Pas d'impressions de calibration intégrées — vous devez télécharger séparément des fichiers STL de calibration^[22]^
- Les profils d'imprimantes tierces sont moins complets que ceux d'OrcaSlicer
- L'interface est plus ancienne et visuellement moins soignée que Bambu Studio^[22]^

#### Qui devrait utiliser PrusaSlicer ?

- **Propriétaires d'imprimantes Prusa** — Optimisation native pour MK4, MK3.5, Mini+, XL
- **Utilisateurs qui font aussi de l'impression résine** — Prise en charge SLA/MSLA unique dans cette famille
- **Utilisateurs orientés stabilité** qui valorisent la base de code la plus mature
- **Amateurs de hauteur de couche variable** — L'éditeur graphique est le meilleur de sa catégorie^[22]^

### UltiMaker Cura : le géant indépendant

UltiMaker Cura est un trancheur gratuit largement utilisé avec un large support d'imprimantes de nombreux fabricants.^[24]^ Contrairement à la famille PrusaSlicer, Cura utilise une base de code entièrement indépendante : l'interface est écrite principalement en Python et QML, tandis que le calcul de tranchage s'exécute dans **CuraEngine**, une application séparée écrite en C++.^[24]^

#### Points forts

- **Large support d'imprimantes** — Profils préconfigurés pour les imprimantes de nombreux fabricants^[24]^
- **Vaste écosystème de plugins** — Le Marketplace Cura propose des plugins pour l'intégration OctoPrint, les scripts de post-traitement, les couches adaptatives, et plus encore
- **Grande communauté** — Des décennies de connaissances accumulées, tutoriels et publications de forum
- **Scripts de post-traitement** — Puissants outils de modification du G-code pour les flux de travail avancés

#### Limitations

- **Développement de fonctionnalités plus lent** — A pris du retard sur la famille PrusaSlicer en 2024-2026 dans des domaines comme les outils de calibration et les flux de travail multi-matériaux^[22]^
- **Incompatibilité avec l'arbre généalogique** — Les profils et paramètres Cura ne se transfèrent pas aux trancheurs de la famille PrusaSlicer
- Certaines fonctionnalités utiles disponibles via le niveau payant « Cura Enterprise »^[22]^

> 💡 **Astuce de pro :** Si vous utilisez Cura, des plugins comme Adaptive Layers et les scripts de post-traitement G-code peuvent améliorer significativement votre flux de travail. Consultez le Marketplace Cura pour les plugins pertinents à votre marque d'imprimante.

#### Qui devrait utiliser Cura ?

- Les utilisateurs qui ont besoin d'un **support d'imprimantes étendu** au-delà de ce qu'offre OrcaSlicer
- Les **amateurs de plugins** qui dépendent d'extensions spécifiques du marketplace
- Ceux qui privilégient la **plus grande base de connaissances communautaires**

### SuperSlicer : le laboratoire de l'enthousiaste

SuperSlicer est un fork de PrusaSlicer qui ajoute de nombreuses options de personnalisation et des outils de calibration.^[26]^ Il a été une influence majeure sur l'approche de calibration d'OrcaSlicer — plusieurs fonctionnalités de SuperSlicer ont inspiré la suite de calibration d'OrcaSlicer.^[23]^ Depuis mi-2024, SuperSlicer reste disponible et périodiquement mis à jour, bien que son rythme de développement soit plus lent que celui d'OrcaSlicer.^[26]^

Les fonctionnalités clés incluent des outils de calibration améliorés, le repassage pour la finition de surface, les options de périmètre unique pour les surfaces supérieures, la gestion des parois fines, la hauteur de couche adaptative, et un sélecteur de difficulté qui ajuste la complexité de l'interface.^[26]^

> 📝 **Note :** De nombreuses innovations de SuperSlicer ont été absorbées par OrcaSlicer. Il est généralement conseillé aux nouveaux utilisateurs de choisir OrcaSlicer, sauf s'ils ont besoin d'une fonctionnalité spécifique à SuperSlicer qui n'est pas encore présente dans Orca.

### Compatibilité des profils entre trancheurs

En raison de l'arbre généalogique commun, les profils se transfèrent entre les trancheurs avec des degrés variables de facilité :^[23]^

| Chemin de migration | Compatibilité | Notes |
|--------------------|--------------|-------|
| PrusaSlicer → OrcaSlicer | Bonne | Des renommages mineurs de paramètres peuvent être nécessaires |
| Bambu Studio → OrcaSlicer | Excellente | Principalement compatible, changements minimaux |
| OrcaSlicer → Bambu Studio | Bonne | Certaines fonctionnalités spécifiques à Orca non prises en charge |
| Cura → Famille PrusaSlicer | Mauvaise | Base de code indépendante, pas de migration propre |
| N'importe lequel → Cura | Mauvaise | Les profils doivent être recréés de zéro |

Lors de la migration, portez une attention particulière aux champs **inherits** dans les fichiers de profil JSON — le profil parent hérité doit également être présent dans le trancheur de destination.

### Comment choisir : tableau de décision

Utilisez ce tableau pour sélectionner le bon trancheur selon votre situation :

| Votre situation | Trancheur recommandé | Pourquoi |
|-----------------|---------------------|---------|
| Propriétaire d'imprimante Bambu Lab | **Bambu Studio** | Intégration la plus étroite, flux de travail le plus simple^[13]^ |
| Utilisateur du firmware Klipper | **OrcaSlicer** | Meilleure intégration Klipper, calibration intégrée^[22]^ |
| Propriétaire d'imprimante Prusa | **PrusaSlicer** | Optimisation native, support SLA^[22]^ |
| Plusieurs marques d'imprimantes | **OrcaSlicer** | Meilleur support multi-imprimantes^[22]^ |
| Besoin de plugins Cura spécifiques | **UltiMaker Cura** | Écosystème de plugins le plus vaste^[24]^ |
| Confidentialité, pas de cloud | **OrcaSlicer** ou **PrusaSlicer** | Pas de compte requis^[22]^ |
| Débutant, n'importe quelle imprimante | **OrcaSlicer** (mode Simple) | Meilleur équilibre facilité/puissance^[22]^ |
| Besoins avancés de calibration | **OrcaSlicer** | Suite de calibration intégrée sans équivalent^[25]^ |

### Points clés à retenir

- Le monde des trancheurs a **convergé autour du paradigme PrusaSlicer** — Slic3r → PrusaSlicer → Bambu Studio → OrcaSlicer.^[23]^ Les connaissances se transfèrent directement entre les membres de la famille.
- **OrcaSlicer** est le trancheur polyvalent dominant en 2025-2026 grâce à ses outils de calibration complets, son large support d'imprimantes et l'absence de dépendance au cloud.^[22]^
- **Bambu Studio** reste le meilleur choix pour les propriétaires d'imprimantes Bambu Lab grâce à son intégration matérielle transparente.^[13]^
- **PrusaSlicer** offre la base de code la plus mature et est la seule option avec une prise en charge complète de l'impression résine dans cette famille.^[22]^
- **Cura** a une grande base d'utilisateurs et un vaste écosystème de plugins, mais a connu un développement de fonctionnalités plus lent par rapport à la famille PrusaSlicer.^[22]^^[24]^
- **La migration des profils** est simple au sein de la famille PrusaSlicer, mais pratiquement impossible avec Cura en raison de sa base de code indépendante.^[23]^

---

## Chapitre 4 : Fonctionnalités avancées des trancheurs

Une fois que vous avez maîtrisé les fondamentaux, un monde de fonctionnalités avancées vous attend. Ces outils vous permettent de repousser les limites de ce que l'impression FDM peut accomplir — des surfaces supérieures lisses comme du verre aux vases à paroi unique sans couture visible, des substitutions de paramètres spécifiques à une région aux flux de travail de calibration entièrement automatisés.

### Hauteur de couche variable

La **hauteur de couche variable (HCV)** est la technique consistant à utiliser des couches plus fines sur les surfaces courbes ou détaillées tout en utilisant des couches plus épaisses sur les sections plates et verticales. Cela produit le meilleur des deux mondes : des courbes lisses sans le temps d'impression excessif de couches uniformément fines.

PrusaSlicer offre l'implémentation la plus soignée avec un **éditeur de courbe graphique** — vous dessinez une courbe directement sur le profil du modèle, et le trancheur ajuste les hauteurs de couche pour correspondre.^[22]^ Dans Bambu Studio et OrcaSlicer, des outils similaires vous permettent de peindre des régions pour des couches plus fines ou plus épaisses.

**Quand l'utiliser :** Formes organiques, figurines, maquettes architecturales, ou toute pièce où les surfaces courbes sont importantes et des surfaces plates sont également présentes. Une figurine détaillée pourrait utiliser des couches de 0,08 mm sur le visage et des couches de 0,24 mm sur la base.

**Compromis :** La HCV augmente la complexité du tranchage et peut produire des transitions visibles si elle n'est pas configurée avec soin. Le paramètre de lissage contrôle la progressivité des changements de hauteur de couche entre les régions.

### Peau floue (Fuzzy Skin)

La **peau floue** est un paramètre du trancheur qui ajoute une texture aléatoire aux surfaces du modèle, créant une finition légèrement rugueuse et mate.^[27]^ Elle fonctionne en décalant aléatoirement les points du périmètre vers l'extérieur d'une quantité configurable.

Paramètres clés :^[27]^
- **Épaisseur de peau floue :** Distance maximale de décalage de chaque point (plus élevée = texture plus rugueuse)
- **Distance entre points de peau floue :** Distance moyenne entre les points de décalage aléatoires (plus faible = texture plus dense et plus détaillée)

La peau floue est exceptionnellement efficace pour masquer les lignes de couche et les imperfections d'impression. Elle est populaire pour les poignées fonctionnelles, la fabrication de props, et toute application où une surface mate et antidérapante est souhaitable.

### Repassage (Ironing)

Le **repassage** passe la buse chaude sur la surface supérieure à faible vitesse avec une extrusion minimale, refondant et lissant la surface pour créer une finition brillante.^[28]^ Il combine trois actions : chauffer la couche supérieure existante, la lisser physiquement avec la buse chaude, et extruder une petite quantité de filament supplémentaire pour combler les éventuels vides.

- Ajoute typiquement 10-30 % au temps d'impression mais ne nécessite aucun outil supplémentaire^[28]^
- **PLA** est le matériau le plus facile à repasser — produit d'excellents résultats
- **PETG** peut créer des fils pendant le repassage ; maintenez le taux de débit du repassage bas
- **ABS** nécessite un refroidissement contrôlé pour éviter le gauchissement pendant les passes de repassage

Activez le repassage pour les surfaces supérieures visibles sur les pièces d'exposition, les boîtiers, ou toute pièce où une face supérieure lisse est importante. Il n'a aucun effet sur les parois verticales ni sur les surfaces inférieures.

> 💡 **Astuce de pro :** Pour de meilleurs résultats de repassage, assurez-vous d'abord que votre débit est correctement calibré. Le repassage amplifie les erreurs d'extrusion — si vous sur-extrudez, le repassage créera des crêtes surélevées plutôt qu'une surface lisse.

### Mode vase (Spiralize)

Le **mode vase** — techniquement appelé **contour spiralisé** ou **vase spirale** selon le trancheur — transforme un modèle solide en un récipient creux à paroi unique sans couture en Z visible.^[29]^ Au lieu d'imprimer en couches discrètes, l'imprimante se déplace en une spirale continue montant progressivement — comme une machine à glace à l'italienne. Parce que la buse ne s'arrête jamais d'extruder et ne saute jamais vers une nouvelle couche, il n'y a pas de point de départ/arrêt et donc pas de couture.^[29]^

Lorsque le mode vase est activé, le trancheur impose automatiquement : 1 périmètre, 0 % de remplissage, 0 couche pleine supérieure, et supports désactivés.^[29]^

Le mode vase est parfait pour les récipients décoratifs, les jardinières, les abat-jours et tout objet creux où la résistance n'est pas la préoccupation principale. Tous les modèles ne sont pas adaptés — la géométrie doit permettre une progression ascendante continue sans îlots internes ni surplombs.

### Impression séquentielle

L'**impression séquentielle** (aussi appelée « imprimer un à la fois ») complète entièrement un objet avant de passer au suivant, plutôt que d'imprimer tous les objets couche par couche simultanément.^[22]^ C'est utile pour :

- **Les fermes d'impression :** Retirer les pièces terminées sans arrêter le travail d'impression
- **Les objets hauts et délicats :** Évite les collisions de la buse avec les pièces déjà imprimées
- **Différents paramètres par objet :** Chaque objet peut être imprimé avec des paramètres légèrement différents

La contrainte principale est la **hauteur de dégagement** — le portique et l'ensemble buse de l'imprimante ne doivent pas entrer en collision avec les objets déjà imprimés. Cela limite l'impression séquentielle aux objets moins hauts que le dégagement du portique, disposés de sorte que l'extrudeur puisse atteindre chacun sans passer au-dessus des pièces terminées.

### Maillages modificateurs

Les **maillages modificateurs** sont des formes géométriques invisibles placées sur des régions de votre modèle pour substituer des paramètres spécifiques uniquement dans cette zone. Considérez-les comme des outils d'édition locale de vos paramètres d'impression.

Cas d'utilisation courants :
- **Renforcer une zone spécifique** avec une densité de remplissage plus élevée ou plus de parois
- **Ajouter un support uniquement à un surplomb spécifique** sans activer les supports pour l'ensemble du modèle
- **Changer la hauteur de couche** pour une région détaillée tout en maintenant le reste à la résolution standard
- **Ajuster la vitesse d'impression** pour une section délicate

Les modificateurs sont définis en créant une forme simple (cube, cylindre, sphère) et en la positionnant sur la zone cible. Tous les paramètres appliqués au modificateur remplacent les paramètres de processus globaux dans cette région.

> 💡 **Astuce de pro :** Les maillages modificateurs sont souvent plus rapides à mettre en place que la division d'un modèle dans un logiciel CAO. Si vous avez juste besoin d'une modification locale — un remplissage plus dense autour d'un trou de boulon, par exemple — un maillage modificateur peut vous faire économiser des heures de travail CAO.

### Outils de calibration dans OrcaSlicer

La suite de calibration intégrée d'OrcaSlicer est la plus complète de tous les trancheurs gratuits.^[22]^ Voici comment utiliser chaque outil efficacement :

#### Tour de température (Temperature Tower)

Une tour de température compresse une étude complète de température en une seule impression contrôlée, avec des segments par paliers de 5 °C.^[25]^ Pour l'utiliser :

1. Ouvrez Calibration → Temperature Tower dans OrcaSlicer
2. Définissez votre plage de test (par ex., 190-230 °C pour PLA)
3. Imprimez le modèle généré
4. Évaluez chaque section pour la finition de surface, les fils, l'adhérence des couches et la qualité des surplombs

| Critère | Trop froid | Optimal | Trop chaud |
|---------|------------|---------|-----------|
| Finition de surface | Mate, rugueuse | Lisse, satinée | Brillante, inégale |
| Fils | Minimaux | Minimaux à aucun | Filaments excessifs |
| Adhérence des couches | Faible, couches se séparant | Forte, couches fusionnées | Bonne mais peut suinter |

Températures optimales typiques comme points de départ : PLA environ 205 °C, PETG environ 240 °C, ABS environ 245 °C — celles-ci varient selon la marque et la couleur, donc calibrez toujours.^[25]^

> 📝 **Note :** Séchez toujours votre filament avant la calibration de température. L'humidité provoque des bulles et des fils qui seront incorrectement attribués à la température.

#### Test de débit (Flow Rate Test)

La calibration du débit dans OrcaSlicer utilise une approche visuelle en deux passes :^[30]^

**Passe 1 (grossière) :** Neuf blocs avec des modificateurs de débit d'environ -9 % à +9 %. Sélectionnez le bloc avec la surface supérieure la plus lisse. Calcul : `NouveauDébit = AncienDébit × (100 + modificateur) / 100`.

**Passe 2 (fine) :** Dix blocs avec des modificateurs de -9 à 0. Sélectionnez à nouveau la meilleure surface et appliquez le même calcul.

#### Motif de pressure advance (Pressure Advance Pattern)

La calibration du pressure advance doit toujours être effectuée **après** la calibration du débit.^[25]^ OrcaSlicer propose trois méthodes :

1. **Méthode par ligne :** Rapide — génère des lignes avec des valeurs PA incrémentales. Sélectionnez la ligne la plus uniforme.
2. **Méthode par motif :** Évaluation visuelle d'un motif de prisme. Trouvez les coins les plus nets avec le moins d'artefacts.
3. **Méthode par tour :** Le PA augmente avec la hauteur. Examinez les coins à chaque hauteur.

> 📝 **Note :** Les valeurs de PA varient significativement selon l'imprimante, le type d'extrudeur et le filament. Comme point de départ approximatif, le PLA sur les configurations à entraînement direct se situe souvent autour de 0,04-0,06 ; le PETG légèrement plus haut. Calibrez toujours pour votre combinaison spécifique plutôt que de vous fier à des valeurs génériques.

#### Test de rétraction (Retraction Test)

Le test de rétraction trouve la distance de rétraction optimale pour minimiser les fils :^[11]^
- **Extrudeurs à entraînement direct :** Commencez à 1 mm, testez jusqu'à 2 mm
- **Extrudeurs Bowden :** Commencez à 4 mm, testez jusqu'à 6 mm

Évaluez la distance de rétraction la plus courte produisant un minimum de fils sans provoquer de bouchons ni de cratères.

#### Test de tolérance (Tolerance Test)

Le test de tolérance imprime une série de tenons et de trous aux dimensions connues. Après l'impression, testez quel tenon s'insère dans quel trou pour déterminer la précision dimensionnelle de votre imprimante. Essentiel pour les impressions fonctionnelles avec des pièces complémentaires.

### Points clés à retenir

- La **hauteur de couche variable** vous permet d'utiliser des couches fines sur les surfaces courbes et des couches épaisses sur les sections plates — le meilleur des deux mondes pour la qualité et la vitesse.^[22]^
- La **peau floue** masque les lignes de couche et les imperfections d'impression avec une surface texturée aléatoire.^[27]^
- Le **repassage** crée des surfaces supérieures brillantes en les refondant avec la buse chaude ; ajoute typiquement 10-30 % au temps d'impression.^[28]^
- Le **mode vase** produit des objets creux sans couture avec une extrusion spirale continue unique — pas de couture en Z visible.^[29]^
- L'**impression séquentielle** complète les objets un à la fois, utile pour les fermes d'impression et les pièces délicates.^[22]^
- Les **maillages modificateurs** permettent des substitutions de paramètres spécifiques à une région sans modifier le modèle dans un logiciel CAO.
- La **suite de calibration d'OrcaSlicer** est la plus complète disponible — suivez l'ordre Temperature → Flow Rate → Pressure Advance → Retraction pour de meilleurs résultats.^[25]^

---

## Résumé du module

Dans ce module, vous avez parcouru le chemin des fondamentaux du tranchage jusqu'aux flux de travail de calibration avancés. Vous comprenez maintenant :

- Le pipeline de tranchage complet du modèle 3D au G-code
- Comment choisir entre les formats de fichiers (3MF > STL pour tous les flux de travail modernes)
- L'interface de Bambu Studio, son système de profils et les considérations de confidentialité cloud/LAN
- L'arbre généalogique des trancheurs et pourquoi le paradigme PrusaSlicer domine le tranchage FDM
- Comment sélectionner le bon trancheur pour votre imprimante et votre flux de travail spécifiques
- Les fonctionnalités avancées comme la hauteur de couche variable, la peau floue, le repassage et le mode vase
- La suite de calibration complète d'OrcaSlicer et l'ordre critique de calibration

Le trancheur est votre levier principal pour la qualité d'impression. Le matériel a son importance, mais la différence entre une impression médiocre et une impression exceptionnelle réside presque toujours dans les paramètres du trancheur. Investissez du temps pour apprendre votre trancheur en profondeur, effectuez les tests de calibration, et sauvegardez vos profils affinés. Les retours se mesurent en heures économisées et en qualité gagnée sur chaque impression.

> 💡 **Astuce de pro :** Créez un préréglage utilisateur « calibré » dans votre trancheur pour chaque filament que vous possédez, avec des valeurs affinées de température, de débit, de pressure advance et de rétraction. Les 30 minutes consacrées à la calibration de chaque nouvelle bobine de filament vous feront économiser des heures d'impressions ratées et de dépannage.

---

## Sources

Les sources ci-dessous sont les références du module d'origine en langue anglaise ; les titres descriptifs courts ont été traduits en français.

1. 3D Mag — « Guide complet du tranchage 3D : comment fonctionne le logiciel de tranchage » (pipeline de tranchage ; instructions G-code) : <https://www.3dmag.com/3d-wikipedia/3d-slicing-slicing-software-how-slicers-work/>
2. Library of Congress — « STL (STereoLithography) File Format Family » (créé en 1987 par Charles Hull / 3D Systems ; maillage triangulé) : <https://www.loc.gov/preservation/digital/formats/fdd/fdd000504.shtml>
3. Wikipedia — « 3D Manufacturing Format » (fondé en 2015 ; Autodesk, Dassault Systèmes, HP, Microsoft, Shapeways parmi les membres fondateurs ; ISO/IEC 25422:2025) : <https://en.wikipedia.org/wiki/3D_Manufacturing_Format>
4. 3MF Consortium — « 3MF : une norme ISO pour l'avenir de la fabrication additive » (annonce ISO/IEC 25422:2025) : <https://3mf.io/announcement/2025/07/3mf-an-iso-standard-for-the-future-of-additive-manufacturing/>
5. Prusa Blog — « PrusaSlicer 2.5 : nouveau générateur de périmètres, support des fichiers STEP » (3MF comme format de projet par défaut ; Arachne introduit en 2.5) : <https://blog.prusa3d.com/prusaslicer-2-5-is-here-new-perimeter-generator-step-file-support-lightning-infill-and-more_70562/>
6. Prusa Blog — « PrusaSlicer 2.5 : support des fichiers STEP » (import STEP et générateur de périmètres Arachne introduits dans PrusaSlicer 2.5, septembre 2022) : <https://blog.prusa3d.com/prusaslicer-2-5-is-here-new-perimeter-generator-step-file-support-lightning-infill-and-more_70562/>
7. 3D Solved — « Meilleure hauteur de couche pour l'impression 3D » (règle des 80 % : la hauteur de couche ne doit pas dépasser 80 % du diamètre de la buse) : <https://3dsolved.com/best-layer-height-for-3d-printing/>
8. Prusa Knowledge Base — « Générateur de périmètres Arachne » (largeur d'extrusion variable ; par défaut depuis PrusaSlicer 2.5 ; développé à l'origine par l'équipe Cura) : <https://help.prusa3d.com/article/arachne-perimeter-generator_352769>
9. BigRep — « Remplissage gyroid en impression 3D : résistance, efficacité, précision » (le gyroid offre une résistance multidirectionnelle quasi-isotrope ; bonne absorption d'énergie) : <https://bigrep.com/posts/gyroid-infill-3d-printing/>
10. Snapmaker — « Supports en arbre pour l'impression 3D : guide pour des impressions plus propres » (les supports en arbre réduisent le matériau de 25-50 % par rapport aux supports standard sur les modèles complexes ; retrait plus facile) : <https://www.snapmaker.com/blog/tree-supports-3d-printing/>
11. Sovol3D — « Comment ajuster les paramètres de rétraction de l'imprimante 3D » (entraînement direct 1-2 mm ; Bowden 4-6 mm distances de rétraction typiques) : <https://www.sovol3d.com/blogs/news/adjust-3d-printer-retraction-settings-for-optimal-print-quality>
12. ADP Industries — « Bambu Studio vs OrcaSlicer vs PrusaSlicer » (Bambu Studio forké depuis PrusaSlicer par Bambu Lab en 2022) : <https://adpindustries.com/blog/bambu-studio-vs-orcaslicer-vs-prusaslicer/>
13. Automatic3D — « Glossaire Bambu Studio » (fonctionnalités de Bambu Studio, système de profils, onglets Prepare/Preview/Device/Project, modes cloud/LAN) : <https://www.automatic3d.com/glossary/bambu-studio>
14. Bambu Lab Community Forum — « Silent-Standard-Sport-Ludicrous : qu'est-ce qui change réellement ? » (multiplicateurs de vitesse : Silent=50 %, Standard=100 %, Sport=124 %, Ludicrous=166 %) : <https://forum.bambulab.com/t/silent-standard-sport-ludicrous-what-actually-is-changed/94976>
15. Bambu Lab Wiki — « Slow Down for Overhangs » (calcul du degré de surplomb ; fonctionnalité de réduction de vitesse) : <https://wiki.bambulab.com/en/software/bambu-studio/slow-down-for-overhang>
16. How-To Geek — « Ne négligez pas ces 7 fonctionnalités de Bambu Studio » (outils de peinture de supports : cercle, sphère, remplissage ; régions d'imposition/blocage) : <https://www.howtogeek.com/dont-overlook-these-bambu-studio-features-theyre-the-key-to-better-prints/>
17. Bambu Lab Wiki — « Introduction aux fonctions principales et au flux de travail de l'AMS » (identification RFID ; capteur d'humidité + dessiccant ; sauvegarde/commutation automatique de bobine) : <https://wiki.bambulab.com/en/ams/manual/ams-function-introduction>
18. Bambu Lab Blog — « Le Bambu Lab Trust Center pour une transparence complète en matière de sécurité et de confidentialité » (certifications ISO/IEC 27001, ISO/IEC 27701, TRUSTe Enterprise Privacy) : <https://blog.bambulab.com/the-bambu-lab-trust-center-for-complete-security-and-privacy-transparency/>
19. Bambu Lab Community Forum — « Comprendre la limite des préréglages utilisateur cloud » (limites de synchronisation cloud : 20 préréglages d'imprimante, 100 préréglages de processus, 200 préréglages de filament) : <https://forum.bambulab.com/t/understanding-cloud-user-presets-limit-custom-filament-setup/181259>
20. Bambu Studio Wiki — « Utilisation en ligne de commande » (options CLI : --slice, --load-settings, --load-filaments, --export-3mf, --outputdir, --orient, --arrange, --debug ; priorité des paramètres) : <https://github.com/bambulab/BambuStudio/wiki/Command-Line-Usage>
21. Printago — « Référence CLI de Bambu Studio » (--skip-useless-pick désactive la génération de miniatures ; --mstpp N interrompt le tranchage après N secondes) : <https://printago.io/blog/bambu-studio-cli-reference>
22. ADP Industries — « Bambu Studio vs OrcaSlicer vs PrusaSlicer : quel trancheur devriez-vous utiliser ? » (comparaison des trancheurs ; points forts et faiblesses ; suite de calibration OrcaSlicer) : <https://adpindustries.com/blog/bambu-studio-vs-orcaslicer-vs-prusaslicer/>
23. OctoEverywhere Blog — « Qui a créé Orca Slicer ? Histoire, sécurité, téléchargements et plus » (première version le 16 juillet 2022 par SoftFever ; fork de Bambu Studio → PrusaSlicer → lignée Slic3r) : <https://blog.octoeverywhere.com/who-created-orca-slicer-history-saftey-downloads-more/>
24. GitHub — Ultimaker/Cura (interface Python/QML) ; GitHub — Ultimaker/CuraEngine (moteur de tranchage C++, « 98,9 % C++ ») : <https://github.com/Ultimaker/Cura>
25. Obico — « Maîtriser vos impressions : le guide complet de calibration OrcaSlicer » (ordre de calibration : Temperature → Flow Rate → Pressure Advance → Retraction → Tolerance → MVS ; températures optimales typiques : PLA ~205 °C, PETG ~240 °C, ABS ~245 °C) : <https://www.obico.io/blog/orcaslicer-comprehensive-calibration-guide/>
26. GitHub — supermerill/SuperSlicer (fork de PrusaSlicer ; dernière version 2.5.59.12-bis, juillet 2024 ; actif mais ralentissant) : <https://github.com/supermerill/SuperSlicer>
27. Prusa Knowledge Base — « Peau floue (Fuzzy skin) » (épaisseur de peau floue = décalage latéral max ; distance entre points = espacement moyen entre points aléatoires) : <https://help.prusa3d.com/article/fuzzy-skin_246186>
28. Snapmaker — « Qu'est-ce que le repassage en impression 3D ? » (le repassage refond la surface supérieure ; ajoute 10-30 % au temps d'impression ; PLA le plus facile, PETG/ABS plus difficiles) : <https://www.snapmaker.com/blog/ironing-in-3d-printing/>
29. The 3D Printer Bee — « Bases et paramètres du mode vase Cura "Spiralize Outer Contour" » (spirale continue ; pas de couture en Z ; impose 1 paroi, 0 remplissage, 0 couche supérieure) : <https://the3dprinterbee.com/cura-vase-mode-spiralize-outer-contour-basics-settings/>
30. OrcaSlicer Wiki — « Calibration du débit » (passe 1 : neuf blocs ; passe 2 : dix blocs, modificateurs de -9 à 0 ; formule : AncienDébit × (100 + modificateur) / 100) : <https://github.com/OrcaSlicer/OrcaSlicer/wiki/flow_ratio_calib>

### Pour aller plus loin

- Prusa Knowledge Base — documentation complète PrusaSlicer et tutoriels : <https://help.prusa3d.com/>
- OrcaSlicer Wiki — guides de calibration et profils spécifiques aux imprimantes : <https://github.com/OrcaSlicer/OrcaSlicer/wiki>
- Bambu Lab Wiki — guide utilisateur Bambu Studio et documentation des fonctionnalités : <https://wiki.bambulab.com/en/software/bambu-studio>
- All3DP — « Orca Slicer : Pressure Advance — explication simple » (guide pratique de calibration PA) : <https://all3dp.com/2/orca-slicer-pressure-advance-explained/>
