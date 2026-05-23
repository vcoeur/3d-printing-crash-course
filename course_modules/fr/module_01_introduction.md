# Module 1 : Introduction à l'impression 3D

> **Aperçu du module :** Ce module présente les fondamentaux de la technologie d'impression 3D. Vous apprendrez ce qu'est l'impression 3D et en quoi elle diffère de la fabrication traditionnelle, vous découvrirez l'histoire qui a conduit cette technologie d'une expérience de cuisine à des millions de foyers dans le monde entier, vous comprendrez comment fonctionne réellement le dépôt de filament fondu (FDM), et vous verrez pourquoi la cinématique CoreXY est devenue l'architecture dominante pour l'impression haute performance. À la fin de ce module, vous disposerez de bases solides pour comprendre chaque décision technique que vous prendrez avec votre imprimante.

---

## Chapitre 1 : Qu'est-ce que l'impression 3D ?

Imaginez pouvoir tenir dans vos mains un modèle numérique en quelques heures — sans usine, sans outillage, sans quantité de commande minimale. Telle est la promesse transformatrice de l'impression 3D. Que vous ayez besoin d'un support de remplacement pour un appareil en panne, d'un support de téléphone personnalisé ou d'un prototype pour votre prochain projet, l'impression 3D comble le fossé entre l'imagination et la réalité physique. Dans ce chapitre, nous explorons ce qu'est réellement l'impression 3D, comment elle a évolué d'une curiosité industrielle vers une technologie domestique, et les différentes approches qui rendent tout cela possible.

### Fabrication additive ou soustractive

La fabrication traditionnelle est essentiellement **soustractive** : on part d'un bloc de matière et on retire tout ce qui ne fait pas partie de l'objet final. Pensez à un sculpteur taillant le marbre ou à une fraiseuse CNC découpant de l'aluminium. Ces méthodes sont puissantes et précises, mais elles gaspillent de la matière, nécessitent un outillage coûteux, et peinent à réaliser des géométries internes complexes.

**L'impression 3D**, également connue sous le nom de **fabrication additive (FA)**, inverse totalement cette logique. Au lieu de retirer de la matière, on l'ajoute — une fine couche à la fois — en construisant l'objet de toutes pièces.^[1]^ Comme un pâtissier appliquant du glaçage couche par couche pour décorer un gâteau, une imprimante 3D dépose la matière précisément là où elle est nécessaire. Cette approche offre des avantages remarquables :

- **Liberté géométrique** : les canaux internes, les structures en treillis et les formes organiques impossibles à usiner deviennent réalisables sans difficulté
- **Pas d'outillage requis** : du fichier numérique à la pièce physique sans moule, matrice ni outil de coupe
- **Efficacité matière** : on n'utilise que la matière qui compose l'objet final, plus des structures de support minimales
- **Production à la demande** : imprimez une pièce ou cent, sans variation de coût de mise en route
- **Itération rapide** : modifiez votre conception, re-tranchez, et relancez l'impression — souvent en quelques heures

⚠️ **Avertissement :** Ne confondez pas l'impression 3D avec l'impression 2D traditionnelle. Une imprimante 3D n'« imprime » pas à l'encre sur du papier ; elle fabrique des objets solides en trois dimensions. Le terme « impression » s'est imposé parce que les premières technologies utilisaient des mécanismes semblables à ceux des imprimantes jet d'encre, mais le procédé relève fondamentalement de la fabrication, non de la documentation.

### Une brève histoire de l'impression 3D

L'histoire de l'impression 3D est un voyage fascinant, d'un passe-temps de père un week-end à une industrie pesant plusieurs milliards de dollars. Comprendre cette histoire vous aide à saisir pourquoi la technologie actuelle fonctionne comme elle le fait.

#### L'expérience de cuisine (1988)

En 1988, Scott Crump, ingénieur diplômé en génie mécanique à l'Université d'État de Washington, avait un objectif simple : fabriquer une grenouille en jouet pour sa fille.^[2]^ Il chargea un pistolet à colle chaude d'un mélange fait maison de polyéthylène et de cire de bougie, l'appliqua couche par couche, et construisit une forme tridimensionnelle. En travaillant, une idée lui vint à l'esprit : *ce processus pourrait être automatisé si un ordinateur pilotait la buse*.^[2]^

Cette expérience devint le fondement de l'ensemble de l'industrie mondiale de l'impression 3D FDM. Crump et sa femme Lisa co-fondèrent **Stratasys** en 1989, et après des années de développement, ils commercialisèrent leur première machine — le **3D Modeler** — en avril 1992.^[3]^ Le prix était de **130 000 $**.^[3]^

Crump déposa le brevet fondateur du FDM, **US5121329A**, le 30 octobre 1989. Il fut accordé le 9 juin 1992 et contenait 44 revendications couvrant pratiquement tous les aspects de l'impression FDM.^[4]^ Il allait façonner l'industrie pendant les deux décennies suivantes.

#### Le mouvement RepRap (2004–2009)

Tandis que Stratasys s'orientait vers le marché industriel haut de gamme, une vision très différente prenait forme de l'autre côté de l'Atlantique. Le Dr Adrian Bowyer, maître de conférences en génie mécanique à l'Université de Bath au Royaume-Uni, lança le **projet RepRap** en février 2004.^[5]^ Son objectif audacieux : construire une imprimante 3D capable d'imprimer la plupart de ses propres pièces — une machine auto-réplicante.

Les imprimantes RepRap étaient nommées d'après des biologistes pour refléter la philosophie évolutive du projet — les trois générations officielles furent **Darwin** (2007–2008), **Mendel** (2009) et **Huxley** (2010).^[6]^ Darwin atteignit son premier jalon d'auto-réplication le 29 mai 2008, lorsqu'elle produisit un jeu complet de ses propres composants imprimés.^[6]^ Depuis cet écosystème open source, les variantes de Josef Průša donnèrent finalement naissance au Prusa i3, commercialisé en 2015 et déclaré l'imprimante 3D la plus utilisée au monde en 2016.^[7]^

#### L'expiration du brevet et l'essor grand public (2009–aujourd'hui)

Le **30 octobre 2009**, le brevet fondateur FDM de Crump expira.^[4]^ L'effet fut significatif et rapide. MakerBot, fondée en janvier 2009 en s'appuyant directement sur les conceptions open source de RepRap, lança le kit **Cupcake CNC** la même année — parmi les premiers kits d'imprimantes 3D à prix grand public disponibles.^[8]^ Thingiverse, le dépôt de partage de fichiers en ligne qui allait devenir la plus grande communauté de modèles 3D au monde, avait été lancé en novembre 2008 comme prolongement de ce mouvement open source.^[8]^

L'expiration du brevet a été créditée comme ayant permis une baisse spectaculaire du prix de la technologie d'impression FDM.^[1]^ Les imprimantes FDM de bureau tombèrent finalement de plusieurs milliers de dollars à aussi peu que **200 $**.

#### La disruption Bambu Lab (2022)

En 2022, **Bambu Lab** lança la série X1 sur Kickstarter et changea fondamentalement les attentes des consommateurs.^[9]^ En combinant la **cinématique CoreXY**, une **compensation des vibrations** avancée, des chambres closes et une expérience clé en main soignée, Bambu Lab prouva que l'impression 3D haute vitesse n'exigeait plus des semaines de réglage et de calibration.

📝 **Note :** L'industrie de l'impression 3D suit un cycle de disruption d'environ 5 ans : le mouvement RepRap a démocratisé la technologie (2004–2009), le Prusa i3 (conception 2012, kit commercial 2015) l'a affinée pour la fiabilité et l'accessibilité, et Bambu Lab l'a rendue véritablement grand public (2022). Chaque vague a combiné des innovations jusqu'alors séparées en un ensemble plus intégré.

### Les types de technologies d'impression 3D

Le FDM domine l'environnement de bureau, mais ce n'est qu'une des nombreuses technologies de fabrication additive. Comprendre le paysage vous aide à choisir le bon outil pour vos besoins spécifiques.

| Technologie | Procédé | Matériaux | Idéal pour | Coût |
|------------|---------|-----------|------------|------|
| **FDM/FFF** | Fait fondre et extrude du filament thermoplastique couche par couche | PLA, ABS, PETG, Nylon | Pièces fonctionnelles, prototypes, décors | Faible |
| **SLA/MSLA** | Durcit une résine liquide avec de la lumière UV | Résines photopolymères | Figurines, bijoux, modèles dentaires | Moyen |
| **SLS** | Fritte de la poudre polymère avec un laser | PA12 Nylon, TPU | Pièces fonctionnelles complexes, production en série | Élevé |
| **MJF** | Dépose un agent liant puis fritte la poudre avec de la lumière infrarouge | PA12 Nylon | Volumes de production industriels | Très élevé |
| **DLP** | Projette de la lumière UV pour durcir des couches entières de résine | Résines photopolymères | Modèles détaillés, plus rapide que la SLA | Moyen |

**Le FDM (Fused Deposition Modeling)**, également appelé **FFF (Fused Filament Fabrication)** — la différence est purement juridique, non technique.^[1]^ Le terme FFF a été inventé par la communauté RepRap pour disposer d'un acronyme non contraint légalement par la marque déposée de Stratasys. Les deux noms décrivent un processus identique : chauffer le filament thermoplastique jusqu'à un état semi-liquide et l'extruder à travers une buse sur une plateforme de construction.

**La SLA (stéréolithographie)** et la **MSLA (stéréolithographie masquée)** durcissent de la résine liquide en plastique solide à l'aide de lumière UV. Elles atteignent un niveau de détail bien supérieur à celui du FDM — des couches aussi fines que 25–50 µm contre 100–400 µm pour le FDM — mais produisent des pièces généralement plus fragiles qui nécessitent un post-traitement (lavage et durcissement).^[10]^

**Le SLS (frittage sélectif par laser)** utilise un laser haute puissance pour fritté de la poudre polymère. La poudre non frittée soutient naturellement la pièce, éliminant le besoin de supports dédiés. Les pièces SLS sont largement isotropes — les propriétés mécaniques sont uniformes quelle que soit l'orientation d'impression — un avantage considérable sur les propriétés anisotropes du FDM.^[10]^

### Pourquoi le FDM domine l'impression de bureau

Le FDM représente le plus grand parc installé d'imprimantes 3D dans le monde, dominant le marché grand public et semi-professionnel.^[11]^ Plusieurs facteurs expliquent cette domination :

1. **Coût d'entrée le plus bas** : les imprimantes FDM de qualité débutent autour de 200 $
2. **Accessibilité des matériaux** : une bobine de PLA de 1 kg coûte 15–25 $ et permet des dizaines d'impressions
3. **Post-traitement minimal** : retirez les supports et c'est terminé — pas de lavage ni de durcissement
4. **Variété de matériaux** : des centaines de types de filaments, du PLA de base au PEEK de qualité industrielle
5. **Sécurité** : pas de résines liquides irritantes, pas de matériaux en poudre nécessitant des équipements de protection individuelle
6. **Écosystème ouvert** : filament standardisé à 1,75 mm, buses interchangeables, firmware développé par la communauté

💡 **Astuce de pro :** Si vous débutez, le FDM est presque certainement le bon choix. Maîtrisez-le d'abord. L'impression résine (SLA/MSLA) est un excellent complément pour les figurines détaillées et les bijoux, mais la combinaison de coût, de sécurité et de variété de matériaux du FDM en fait la base idéale.

### Le flux de travail complet : de l'idée à l'objet

Chaque impression 3D suit le même pipeline fondamental. Comprendre ce flux de travail vous aide à diagnostiquer les problèmes, car chaque étape possède ses propres modes de défaillance potentiels.

| Étape | Ce qui se passe | Outils/formats clés |
|-------|----------------|---------------------|
| **1. Conception (CAO)** | Créer ou télécharger un modèle 3D | Fusion 360, Tinkercad, Blender, SolidWorks |
| **2. Export** | Enregistrer dans un format de fichier maillage | STL, 3MF, OBJ |
| **3. Tranchage** | Convertir le maillage en instructions pour l'imprimante | Cura, PrusaSlicer, Bambu Studio, Orca Slicer |
| **4. Impression** | Exécuter les instructions G-code sur l'imprimante | Carte SD, USB, Wi-Fi |
| **5. Post-traitement** | Retirer les supports, poncer, peindre ou traiter | Outils manuels, solvants, apprêt |

📝 **Note :** Ce pipeline n'est pas un transfert linéaire — c'est une **boucle de rétroaction**. Vous pouvez orienter votre modèle dans le trancheur, constater qu'un élément critique reposerait sur des supports, retourner dans votre modèle CAO pour ajouter un chanfrein, ré-exporter et recommencer. Ce n'est pas un échec du processus — c'est le processus qui fonctionne correctement pour maximiser la qualité de la pièce finale.

#### Étape 1 : Conception CAO

Le parcours commence avec un **modèle 3D** créé dans un logiciel de CAO (Conception Assistée par Ordinateur). Pour les débutants, **Tinkercad** offre une interface intuitive basée sur navigateur. Pour des travaux plus avancés, **Fusion 360** (gratuit pour les hobbyistes), **Blender** (gratuit, open source) et **SolidWorks** (standard industriel) fournissent des capacités de modélisation puissantes.

Le modèle doit être **étanche** — sans trou, écart ni arête non-manifold — ou le trancheur aura du mal à l'interpréter correctement.

#### Étape 2 : Export du fichier

Les modèles CAO sont exportés vers des formats de fichier maillage. **STL** (abréviation de « stéréolithographie », l'origine du format) a été développé par 3D Systems en 1987 et reste compatible avec pratiquement tous les trancheurs, mais il ne stocke que la géométrie de surface sous forme de triangles — pas de couleur, de matériau ni d'unités.^[12]^

**3MF** (3D Manufacturing Format), introduit en 2015 par un consortium comprenant Microsoft, HP, Autodesk et Dassault Systèmes, est techniquement supérieur.^[13]^ Il stocke les paramètres du trancheur, les données de couleur, les assemblages multi-pièces et les unités du modèle dans un conteneur XML compressé. En juin 2025, le 3MF a été publié sous le nom **ISO/IEC 25422:2025**, devenant ainsi le premier format de fichier d'impression 3D normalisé à l'échelle internationale.^[13]^

#### Étape 3 : Tranchage

**Le logiciel de tranchage** convertit le maillage de votre modèle 3D en **G-code** — un fichier texte contenant les instructions détaillées que votre imprimante suit ligne par ligne. Le trancheur :

1. Divise le modèle en couches horizontales selon la **hauteur de couche** choisie
2. Génère les **trajectoires d'outil** pour les périmètres (parois externes et internes), le **remplissage** (structure interne), les **supports** (pour les surplombs) et les couches pleines du dessus et du dessous
3. Calcule les **quantités d'extrusion** en fonction de la largeur de ligne, de la hauteur de couche et du diamètre du filament
4. Produit un fichier G-code avec toutes les commandes de déplacement, de température et d'extrusion

#### Étape 4 : Impression

Le fichier G-code est transféré vers l'imprimante via une carte SD, un port USB ou le Wi-Fi. L'imprimante exécute les commandes de manière séquentielle : chauffage de la buse et du plateau, retour aux origines de tous les axes, dépôt de matière couche par couche, puis refroidissement de la pièce terminée.

#### Étape 5 : Post-traitement

Le post-traitement peut comprendre le retrait des structures de support, le ponçage des lignes de couche visibles, la peinture, ou des traitements spécifiques aux matériaux comme le **lissage aux vapeurs d'acétone** pour l'ABS.

### Points clés à retenir

- L'impression 3D est de la **fabrication additive** — construire des objets couche par couche à partir de conceptions numériques, fondamentalement différente des méthodes soustractives.^[1]^
- La technologie trouve ses racines dans l'expérience de 1988 de Scott Crump avec un pistolet à colle chaude chargé de polyéthylène et de cire de bougie, évoluant à travers le mouvement open source RepRap et l'expiration du brevet en 2009 pour devenir accessible aux consommateurs.^[2]^^[4]^^[5]^
- **Le FDM domine l'impression de bureau** grâce à son faible coût, sa variété de matériaux, sa sécurité et ses besoins minimaux en post-traitement.^[11]^
- D'autres technologies comme la SLA, le SLS et le MJF ont chacune des points forts distincts pour des applications spécialisées.^[10]^
- Le flux de travail complet — **CAO → Export → Tranchage → Impression → Post-traitement** — est une boucle de rétroaction itérative, non un pipeline linéaire.
- **La disruption de Bambu Lab en 2022** a combiné la cinématique CoreXY, la compensation des vibrations et une expérience utilisateur soignée pour établir de nouvelles attentes chez les consommateurs.^[9]^

---

## Chapitre 2 : Plongée en profondeur dans la technologie FDM

Maintenant que vous avez compris la vue d'ensemble, levons le voile sur le fonctionnement réel du FDM. Ce chapitre couvre la mécanique centrale de l'extrusion, les systèmes de mouvement qui positionnent la tête d'impression, les paramètres clés qui déterminent la qualité d'impression, et le langage G-code qui contrôle tout. Maîtriser ces concepts est essentiel — chaque réglage que vous ajustez dans votre trancheur renvoie aux principes abordés ici.

### Comment fonctionne le FDM : le « pistolet à colle chaude sophistiqué »

L'analogie la plus courante et la plus efficace pour le FDM est celle d'un **pistolet à colle chaude très précis et robotisé**.^[10]^ Voici le processus étape par étape :

1. **Chargement du filament** : une bobine de filament thermoplastique (généralement 1,75 mm de diamètre) est chargée dans l'imprimante
2. **Chauffage** : la **buse** (hotend) et le **plateau de construction** (lit chauffant) de l'imprimante chauffent jusqu'aux températures spécifiques au matériau
3. **Extrusion** : un moteur appelé **extrudeur** pousse le filament dans la buse chauffée où il fond
4. **Dépôt** : la tête d'extrusion se déplace sur les axes X et Y, déposant la matière fondue en minces cordons suivant une trajectoire d'outil programmée
5. **Refroidissement** : chaque cordon déposé refroidit et se solidifie, fusionnant avec la couche précédente en dessous
6. **Avancement de couche** : après chaque couche terminée, le plateau de construction s'abaisse (ou la tête d'extrusion remonte) sur l'axe Z
7. **Répétition** : le cycle se répète jusqu'à ce que la pièce complète soit produite

Les hauteurs de couche FDM vont typiquement de **0,05 mm à 0,4 mm**, avec **0,2 mm** étant le compromis le plus courant entre qualité et vitesse.^[14]^ La résolution XY est déterminée par le **diamètre de la buse** et la précision du système de mouvement, non par la hauteur de couche — une buse standard de 0,4 mm produit des éléments XY d'environ 400 µm de largeur.

### Le système d'extrusion : anatomie du hotend

Le **hotend** est le cœur de toute imprimante FDM. Comprendre ses composants vous aide à diagnostiquer les problèmes courants comme les bouchons, la sous-extrusion et le fluage thermique.

| Composant | Fonction | Spécifications clés |
|-----------|----------|---------------------|
| **Bloc chauffant** | Contient l'élément chauffant et la thermistance ; maintient la zone de fusion | Généralement en laiton, avec résistance cartouche (30-40 W) |
| **Séparateur thermique** | Isole le bloc chauffant chaud de l'ensemble supérieur froid ; prévient le fluage thermique | Titane ou bimétallique (cuivre + acier inoxydable) pour haute performance |
| **Buse** | L'orifice de taille précise par lequel sort le filament fondu | Standard : 0,4 mm ; plage : 0,25–2,0 mm |
| **Dissipateur thermique** | Refroidit le trajet supérieur du filament via un ventilateur, maintenant le filament solide avant le séparateur thermique | Aluminium avec ventilateur radial ou axial |

La **buse de 0,4 mm** standard offre un équilibre pratique entre détail et vitesse, mais votre choix doit correspondre à votre application :

| Diamètre de buse | Hauteur de couche min. | Hauteur de couche standard | Hauteur de couche max. | Idéal pour |
|-----------------|----------------------|--------------------------|----------------------|------------|
| 0,25 mm | 0,06 mm | 0,13 mm | 0,2 mm | Détails fins, figurines |
| 0,4 mm | 0,1 mm | 0,2 mm | 0,32 mm | Usage général (par défaut) |
| 0,6 mm | 0,15 mm | 0,3 mm | 0,48 mm | Impression plus rapide, grandes pièces |
| 0,8 mm | 0,2 mm | 0,4 mm | 0,64 mm | Prototypage rapide, grandes couches |

💡 **Astuce de pro :** Beaucoup d'utilisateurs restent avec la buse de 0,4 mm fournie avec leur imprimante et n'expérimentent jamais. Essayez une buse de 0,6 mm pour les pièces fonctionnelles — vous pouvez imprimer des couches de 0,3 mm avec une largeur de ligne de 0,5 mm, réduisant le temps d'impression d'environ moitié avec un impact minimal sur la résistance. Gardez une buse de 0,4 mm sous la main pour le travail de détail.

**Les hotends tout métal** remplacent le liner PTFE (Téflon) du séparateur thermique par un composant métallique, permettant des températures de buse de **350–500°C**. C'est indispensable pour les matériaux haute performance comme le Nylon, le Polycarbonate, le PEEK et le PEI. Les hotends standard à revêtement PTFE sont limités à environ **240–260°C** avant que le PTFE ne commence à se dégrader et ne libère potentiellement des vapeurs nocives.

### Systèmes de mouvement : les axes X, Y et Z

Chaque imprimante FDM opère en trois dimensions :

- **Axe X** : déplacement latéral (gauche-droite) de la tête d'impression (ou parfois du plateau)
- **Axe Y** : déplacement avant-arrière
- **Axe Z** : déplacement vertical (avancement de couche)

Ces mouvements sont entraînés par des **moteurs pas à pas** — des moteurs CC sans balai qui tournent en incréments précis appelés pas (typiquement 1,8° par pas, soit 200 pas par tour).^[15]^ Des courroies (généralement des **courroies de distribution GT2** au pas de 2 mm), des vis ou des glissières linéaires traduisent ce mouvement rotatif en déplacement linéaire fluide.^[15]^

La façon dont ces axes sont agencés — le **système cinématique** — détermine fondamentalement la vitesse, la précision et les caractéristiques de construction d'une imprimante. Nous explorons les principaux systèmes cinématiques en détail au Chapitre 3.

### Paramètres clés expliqués

Chaque trancheur expose des dizaines de réglages. Voici ceux qui comptent le plus.

#### Température de la buse

**La température de la buse** est le paramètre unique le plus important pour la qualité d'impression FDM.^[10]^ Trop froide, les couches ne se lieront pas correctement ; trop chaude, vous obtiendrez des fils, des gouttes et une dégradation du matériau.

| Matériau | Température de la buse | Notes |
|----------|----------------------|-------|
| PLA | 180-220°C | Le plus facile à imprimer ; commencer à 200°C |
| ABS | 220-250°C | Nécessite une enceinte close ; refroidissement par ventilateur minimal |
| PETG | 230-250°C | Températures plus élevées = meilleure adhérence entre couches |
| TPU | 210-230°C | Vitesses lentes indispensables |
| Nylon | 240-300°C | Hotend tout métal requis |
| ASA | 230-255°C | Alternative à l'ABS résistante aux UV |

⚠️ **Avertissement :** Ces plages sont des points de départ, non des valeurs absolues. Chaque marque de filament et même chaque couleur au sein d'une marque peut se comporter différemment. Une tour de température (impression d'une tour avec différentes températures à chaque niveau) est l'un des meilleurs tests de calibration que vous puissiez effectuer.

#### Température du plateau

Le **plateau chauffant** assure une bonne adhérence de la première couche et prévient le **gauchissement** — lorsque les coins de l'impression se recroquevillent vers le haut en raison d'un refroidissement inégal. Les différents matériaux nécessitent des températures de plateau différentes :

| Matériau | Température du plateau |
|----------|----------------------|
| PLA | 50-60°C (souvent optionnel) |
| ABS | 90-110°C |
| PETG | 65-90°C |
| TPU | 40-60°C |
| Nylon | 70-90°C |

#### Vitesse d'impression

La vitesse d'impression affecte directement la qualité. Des vitesses plus élevées peuvent provoquer une **sous-extrusion** (matière insuffisamment déposée), une mauvaise liaison entre couches, et des artefacts de surface comme le **ringing** (vagues induites par les vibrations près des angles vifs). Pour les pièces fonctionnelles, une impression plus lente maximise généralement la résistance.

| Matériau | Vitesse d'impression recommandée |
|----------|--------------------------------|
| PLA | 40-80 mm/s |
| ABS | 40-60 mm/s |
| PETG | 30-50 mm/s |
| TPU | 15-30 mm/s (doit être lent) |

💡 **Astuce de pro :** Les vitesses annoncées par les fabricants (300-500 mm/s) ne sont atteignables qu'avec des combinaisons spécifiques de hauteur de couche et de largeur de ligne, et souvent uniquement sur certaines parties d'une impression. Le vrai goulot d'étranglement en vitesse FDM est la **Vitesse Volumétrique Maximale (VVM)** du hotend — la quantité de plastique qu'il peut faire fondre par seconde. Un hotend de style V6 standard plafonne à ~10-15 mm³/s, tandis que les hotends à haut débit atteignent 30-60 mm³/s. À une hauteur de couche de 0,2 mm et une largeur de ligne de 0,45 mm, 300 mm/s exige déjà 27 mm³/s. Vérifiez toujours si votre hotend peut réellement fournir la vitesse que vous demandez.

#### Refroidissement par ventilateur

**Les ventilateurs de refroidissement de pièce** accélèrent la solidification de la matière extrudée, améliorant les **surplombs** (surfaces inclinées), le **pontage** (travées horizontales entre supports) et la qualité de surface. Cependant, un refroidissement excessif affaiblit **l'adhérence entre couches** car les couches fusionnent mieux lorsqu'elles sont légèrement chaudes.

| Matériau | Réglage du ventilateur de refroidissement |
|----------|------------------------------------------|
| PLA | 100 % après la première couche |
| ABS | 0-25 % (minimal) |
| PETG | 20-50 % |
| TPU | 20-50 % |

#### Taux de flux (multiplicateur d'extrusion)

Le **multiplicateur d'extrusion** (ou **taux de flux**) est un ajustement en pourcentage appliqué aux calculs théoriques d'extrusion du trancheur. À 100 %, l'imprimante tente d'extruder la quantité exacte calculée. En pratique, une calibration est nécessaire en raison des variations de diamètre du filament, de l'usure des engrenages de l'extrudeur et des différences de comportement du hotend.

**La calibration du taux de flux** est l'une des étapes de réglage les plus rapides et les plus efficaces, capable de résoudre une catégorie entière de problèmes de qualité d'impression en environ 20 minutes pour un filament et une configuration d'imprimante spécifiques.

### Fondamentaux du G-code

**Le G-code** (code géométrique) est le langage de programmation que parle votre imprimante. C'est une série de commandes textuelles qui contrôlent le mouvement, la température, l'extrusion et bien plus encore.^[16]^ La plupart des lignes suivent ce format :

```
N## G## X## Y## Z## F## S## E##
```

Où : **G** = commande de mouvement ; **X, Y, Z** = coordonnées de position ; **F** = taux d'avance (vitesse en mm/min) ; **S** = température ou vitesse du ventilateur ; **E** = quantité d'extrusion (mm de filament).^[16]^

#### Commandes de déplacement essentielles

| Commande | Nom | Fonction |
|----------|-----|---------|
| `G0` | Déplacement rapide | Déplacement de transit rapide sans impression (sans extrusion) |
| `G1` | Déplacement linéaire | Déplacement d'impression contrôlé avec extrusion optionnelle |
| `G28` | Retour à l'origine | Ramener tous les axes à la position zéro (origine) |

Exemple de mouvement d'impression :
```gcode
G1 X-10 Y-4.3 Z0.5 F4000.0 E0.089
```
Ce déplacement va aux coordonnées X=-10, Y=-4.3, Z=0.5 à 4000 mm/min en extrudant 0,089 mm de filament.^[16]^

#### Commandes de température essentielles

| Commande | Description | Exemple |
|----------|-------------|---------|
| `M104 S###` | Définit la température du hotend (non bloquant — continue) | `M104 S200` |
| `M109 S###` | Définit la température du hotend et **attend** qu'elle soit atteinte | `M109 S200` |
| `M140 S###` | Définit la température du plateau (non bloquant) | `M140 S60` |
| `M190 S###` | Définit la température du plateau et **attend** qu'elle soit atteinte | `M190 S60` |
| `M106 S###` | Définit la vitesse du ventilateur de refroidissement (0-255) | `M106 S128` (50 %) |
| `M107` | Éteint le ventilateur de refroidissement | `M107` |

⚠️ **Avertissement :** La différence entre `M104`/`M140` et `M109`/`M190` est cruciale. `M104` définit la température et passe immédiatement à la commande suivante — votre imprimante commencera à se déplacer pendant que la buse chauffe encore. `M109` **met en pause** l'exécution jusqu'à ce que la température cible soit atteinte. Les scripts de démarrage G-code utilisent généralement `M109`/`M190` pour s'assurer que les températures sont atteintes avant que l'impression ne commence.

#### Un script G-code de démarrage typique

```gcode
G21              ; Sets units to millimeters
G90              ; Sets absolute positioning
M82              ; Sets extruder to absolute positioning
G28              ; Home all axes
M190 S60         ; Heat bed to 60°C and wait
M109 S200        ; Heat extruder to 200°C and wait
G92 E0           ; Reset extruder position to zero
G1 Z5 F3000      ; Lift nozzle slightly before start
```

#### Variations de firmware

Les différents firmwares interprètent le G-code légèrement différemment :
- **Marlin** : le firmware open source le plus largement supporté ; fonctionne avec pratiquement tous les trancheurs
- **Klipper** : permet des vitesses plus élevées, des macros personnalisées et des fonctionnalités avancées comme le **façonnage d'entrée** et l'**avance de pression**
- **RepRap** : prend en charge des commandes uniques comme G10/G11 pour la rétraction gérée par le firmware

📝 **Note :** Les imprimantes Bambu Lab utilisent un firmware propriétaire basé sur du code open source modifié. Bien que les concepts fondamentaux du G-code restent les mêmes, certaines commandes et certains comportements diffèrent des implémentations standard de Marlin ou Klipper.

### Hauteur de couche, épaisseur de paroi et remplissage

Ces trois réglages ont le plus grand impact sur l'apparence, la résistance et le temps d'impression de votre pièce.

#### Hauteur de couche

La hauteur de couche définit la résolution sur l'axe Z. Diviser par deux votre hauteur de couche **double** environ le temps d'impression mais produit des surfaces plus lisses.^[14]^ Pour la plupart des impressions, 0,2 mm avec une buse de 0,4 mm est le point d'équilibre optimal.

#### Épaisseur de paroi / périmètre

Les **parois** (également appelées **périmètres**) sont les coques externes de votre impression. Plus de parois augmentent la résistance et améliorent la qualité de surface sur les faces courbes. Un réglage typique est de **3 parois** (environ 1,2 mm au total avec une buse de 0,4 mm). Pour les pièces structurelles, 4–5 parois sont recommandées.

#### Motifs et densité de remplissage

Le **remplissage** remplit l'intérieur de votre impression avec un motif qui assure un support structurel sans utiliser 100 % de matière. La densité varie typiquement de **10–30 %** pour les pièces non structurelles à **20–50 %** pour les pièces fonctionnelles.

| Motif | Résistance | Vitesse | Idéal pour |
|-------|-----------|---------|------------|
| Grille | Moyenne | Élevée | Usage général, impressions rapides |
| Cubique | Élevée | Moyenne | Résistance isotrope (toutes directions) |
| Gyroïde | Élevée | Moyenne-élevée | Flexibilité, résistance isotrope, efficacité matière |
| Nid d'abeille | Élevée | Faible | Rapport résistance/poids maximal |
| Lignes | Faible | Très élevée | Prototypes rapides, résistance minimale |
| Foudre | Faible | Très élevée | Utilisation de matière minimale (impressions décoratives) |

**Le gyroïde** et le **cubique** offrent la meilleure résistance isotrope — des propriétés mécaniques uniformes dans toutes les directions — ce qui les rend idéaux pour les pièces fonctionnelles soumises à des charges multidirectionnelles.

### Structures de support

Les imprimantes FDM peuvent généralement gérer des **surplombs jusqu'à environ 45°** par rapport à la verticale sans support.^[10]^ Au-delà de cet angle, la gravité fait s'affaisser la matière fondue avant qu'elle ne se solidifie. Les **structures de support** sont de la matière sacrificielle imprimée sous les surplombs pour fournir une base.

**Le pontage** est la capacité à imprimer des travées horizontales entre deux points supportés sans rien en dessous. Un pontage réussi dépend d'un refroidissement rapide, d'une vitesse appropriée et de réglages du trancheur qui maintiennent le cordon de filament tendu avant qu'il ne se solidifie.

💡 **Astuce de pro :** Avant d'ajouter automatiquement des supports partout, envisagez de remodeler votre modèle. Un petit chanfrein ou un congé peut éliminer entièrement le besoin de supports. Le retrait des supports est fastidieux, laisse des marques, et gaspille matière et temps.

### Systèmes d'extrusion direct drive et Bowden

La conception du système d'extrusion a un impact significatif sur ce que vous pouvez imprimer et à quelle vitesse.

| Caractéristique | Direct drive | Bowden |
|----------------|-------------|--------|
| **Emplacement de l'extrudeur** | Monté sur la tête d'impression | Monté sur le châssis |
| **Masse en mouvement** | Plus élevée (moteur sur la tête) | Plus faible (moteur fixe) |
| **Distance de rétraction** | 0,5-2 mm | 3-7 mm |
| **Filament flexible** | Excellent — contrôle précis | Difficile — le filament se comprime dans le tube |
| **Potentiel de vitesse d'impression** | Bon | Meilleur (masse en mouvement plus faible) |
| **Complexité d'installation** | Simple | Nécessite le routage du tube PTFE |

Les systèmes **direct drive** montent le moteur de l'extrudeur directement sur la tête d'impression, poussant le filament directement dans le hotend. Cela offre une rétraction plus rapide et plus précise et une excellente compatibilité avec les filaments flexibles comme le TPU, mais ajoute de la masse en mouvement à la tête d'outil.

Les systèmes **Bowden** montent l'extrudeur sur le châssis de l'imprimante et poussent le filament à travers un long tube PTFE jusqu'au hotend. Cela réduit la masse en mouvement (permettant des vitesses plus élevées) mais nécessite des distances de rétraction plus longues et rend les filaments flexibles nettement plus difficiles à imprimer.

### Comprendre les facteurs de qualité d'impression

La qualité d'impression en FDM est déterminée par l'interaction de multiples facteurs :

1. **Hauteur de couche** : plus basse = surfaces plus lisses, impressions plus longues
2. **Diamètre de buse** : plus petit = détails XY plus fins ; plus grand = impression plus rapide
3. **Orientation d'impression** : la décision la plus déterminante dans le pipeline d'impression — elle détermine simultanément la qualité de surface, la direction de résistance, les besoins en supports et le temps d'impression
4. **Température** : affecte le flux, l'adhérence et le rendu de surface
5. **Vitesse** : plus rapide = plus d'artefacts, liaison entre couches plus faible
6. **Refroidissement** : plus = meilleurs surplombs et pontages, mais adhérence entre couches plus faible
7. **Calibration du taux de flux** : assure la précision dimensionnelle et la qualité de surface

Les modèles imprimés en FDM atteignent généralement une précision dimensionnelle d'environ **±0,1–0,3 mm**, avec des variations selon la géométrie, le matériau et la calibration.

### Points clés à retenir

- Le FDM fonctionne comme un **pistolet à colle chaude robotisé de précision**, faisant fondre le filament thermoplastique et le déposant couche par couche.^[10]^
- Le **hotend** (bloc chauffant, séparateur thermique, buse, dissipateur thermique) est le cœur du système d'extrusion ; les hotends tout métal permettent d'utiliser des matériaux haute température.
- **La température de la buse** est le paramètre d'impression unique le plus important, les différents matériaux nécessitant des plages allant de 180°C (PLA) à 300°C (Nylon).^[10]^
- **Le G-code** est le langage que parle votre imprimante ; maîtriser les commandes essentielles (G0, G1, G28, M104, M109, M190, M106) vous aide à comprendre et à dépanner vos impressions.^[16]^
- **La hauteur de couche**, le **nombre de parois**, le **motif/la densité de remplissage** et les **supports** sont vos principaux leviers pour équilibrer qualité, résistance et vitesse.^[14]^
- Le **direct drive** excelle avec les filaments flexibles ; le **Bowden** permet des vitesses plus élevées avec une masse en mouvement plus faible.
- **L'orientation d'impression** est la décision unique la plus déterminante, affectant simultanément la qualité de surface, la résistance, les supports et le temps d'impression.
- La vraie limite de vitesse est le **débit volumétrique** — la capacité de votre hotend à faire fondre le plastique — non la vitesse de déplacement XY annoncée.

---

## Chapitre 3 : CoreXY — Le système cinématique haute performance

Au Chapitre 2, nous avons mentionné que l'agencement des axes d'une imprimante — son **système cinématique** — détermine fondamentalement ses performances. Dans ce chapitre, nous plongeons en profondeur dans le **CoreXY**, l'architecture cinématique qui est devenue la conception dominante pour l'impression FDM haute performance. Comprendre le CoreXY est essentiel car il équipe non seulement les constructions open source de passionnés, mais aussi les imprimantes grand public qui établissent de nouveaux points de référence en matière de vitesse et de qualité aujourd'hui.

### Qu'est-ce que le CoreXY et pourquoi est-il important

**CoreXY** est un **système de mouvement cinématique parallèle** 2D qui déplace une tête d'outil dans le plan X-Y à l'aide de deux moteurs fixes et d'une paire de courroies croisées arrangées de sorte que chaque moteur contribue simultanément aux deux axes.^[17]^

Pour comprendre pourquoi c'est important, considérez l'alternative. Dans une conception **Cartésienne** ou **bedslinger** traditionnelle (comme le classique Ender 3 ou le Prusa i3), la tête d'impression se déplace en X tandis que le **plateau d'impression entier** se déplace en Y. Cet ensemble plateau pèse typiquement **1–3 kg**. Chaque fois que l'imprimante doit changer de direction en Y, elle doit accélérer et décélérer cette plateforme massive. L'inertie limite la vitesse, provoque des vibrations et réduit la précision.

CoreXY résout ce problème en maintenant les deux moteurs X et Y **fixés au châssis**. Seule la tête d'outil légère se déplace.^[17]^ Cette réduction dramatique de la masse en mouvement permet des vitesses et des accélérations que les conceptions bedslinger ne peuvent tout simplement pas atteindre.

| Métrique | CoreXY | Cartésien bedslinger |
|---------|--------|---------------------|
| Vitesse pratique maximale | 500 mm/s (Bambu X1) | ~150 mm/s (limité par l'inertie du plateau) |
| Masse en mouvement (tête d'outil seule) | Faible | Tête d'outil + 1-3 kg de plateau |
| Accélération maximale | 10 000-20 000 mm/s² | 2 000-5 000 mm/s² |
| Exigence d'équerrage du châssis | ≤0,3 mm en diagonale | ≤1,0 mm en diagonale |

### Comment fonctionne le CoreXY : les mathématiques derrière le mouvement

La brillance du CoreXY réside dans la simplicité de son concept. Deux moteurs fixes (appelons-les A et B) entraînent deux courroies indépendantes qui se croisent en motif X sur des **plans empilés** (typiquement 8–12 mm d'écart vertical).^[17]^

Les courroies sont fixées au chariot de la tête d'outil. Le firmware convertit les deux rotations moteur en mouvement cartésien à l'aide de deux équations élégantes :

```
dx = 0.5 × (da + db)
dy = 0.5 × (da - db)
```

Où :
- **dx** = déplacement de la tête d'outil en X
- **dy** = déplacement de la tête d'outil en Y
- **da** = déplacement de courroie du moteur A
- **db** = déplacement de courroie du moteur B

Dans le firmware (Klipper, Marlin), cela s'exprime généralement comme suit :

```
stepper_a_position = cartesian_x_position + cartesian_y_position
stepper_b_position = cartesian_x_position - cartesian_y_position
```

Ce que cela signifie en pratique :
- **Mouvement X pur** : les deux moteurs se déplacent de la même quantité dans la **même** direction
- **Mouvement Y pur** : les deux moteurs se déplacent de la même quantité dans des directions **opposées**
- **Mouvement diagonal** : un seul moteur se déplace

Ni l'un ni l'autre des moteurs ne déplace seul la tête d'outil sur un seul axe. Ils travaillent toujours ensemble — d'où la dénomination **cinématique parallèle**. C'est fondamentalement différent des systèmes Cartésiens où un moteur contrôle X et un autre contrôle Y indépendamment.^[17]^

### Avantages du CoreXY en détail

#### Faible masse en mouvement

L'avantage principal est que seul le chariot de la tête d'outil se déplace. Cette faible inertie se traduit directement par la capacité d'accélérer et de décélérer rapidement sans vibrations secouant le châssis.

#### Haute vitesse (300–500 mm/s)

Avec une faible masse en mouvement, les imprimantes CoreXY atteignent des vitesses impossibles avec les conceptions bedslinger.^[9]^

| Imprimante | Vitesse max. | Accélération max. |
|-----------|-------------|------------------|
| Bambu Lab X1 Carbon | 500 mm/s | 20 000 mm/s² |
| Bambu Lab P1P/P1S | 500 mm/s | 20 000 mm/s² |
| Creality K1/K1C | 600 mm/s | 20 000 mm/s² |
| Voron 2.4 (réglé) | 500 mm/s | 25 000 mm/s² |
| Prusa XL | 400 mm/s | 5 000 mm/s² |

📝 **Note :** Ce sont des maximums annoncés, atteignables uniquement dans des conditions spécifiques. Les vitesses d'impression réelles et durables dépendent de la capacité volumétrique de votre hotend, du matériau et des exigences de qualité. Un Bambu Lab X1 peut atteindre 500 mm/s en déplacements de transit et en remplissage, mais ralentira à 100–200 mm/s pour les périmètres détaillés.

#### Haute accélération (10 000–20 000 mm/s²)

La haute accélération est là où le CoreXY brille vraiment. L'accélération détermine avec quelle rapidité l'imprimante peut atteindre sa vitesse maximale et à quelle vitesse elle peut négocier les changements de direction.

#### Stabilité de l'axe Z

Dans les conceptions CoreXY, le plateau de construction ne se déplace que verticalement (axe Z). Il ne se translate jamais en X ou en Y, ce qui signifie que votre pièce reste parfaitement immobile par rapport au châssis pendant l'impression.^[17]^ Cela élimine l'oscillation du plateau qui peut affliger les conceptions Cartésiennes, en particulier à des vitesses plus élevées.

#### Compatible avec les enceintes

Comme le plateau ne balaie pas l'extérieur du châssis, les imprimantes CoreXY sont naturellement compactes et faciles à fermer complètement.^[17]^ Les enceintes sont essentielles pour les matériaux de qualité industrielle comme l'ABS, l'ASA et le Nylon, faisant du CoreXY l'architecture préférée pour l'impression multi-matériaux sérieuse.

### Comparaison avec les autres systèmes cinématiques

| Caractéristique | CoreXY | Cartésien (bedslinger) | Delta |
|----------------|--------|----------------------|-------|
| **Masse en mouvement** | Très faible (tête d'outil seule) | Élevée (1-3 kg + tête) | Moyenne (effecteur + bras) |
| **Vitesse max.** | 300-500 mm/s | 100-200 mm/s | 200-300 mm/s |
| **Accélération max.** | 10 000-25 000 mm/s² | 2 000-5 000 mm/s² | 5 000-10 000 mm/s² |
| **Forme du volume de construction** | Cubique | Cubique | Cylindrique (en hauteur) |
| **Complexité de calibration** | Modérée | Faible | Élevée (trigonométrique) |
| **Précision aux bords** | Constante | Constante | Diminue aux bords |
| **Meilleure application** | Impression haute vitesse et qualité | Débutants, constructions économiques | Impressions hautes et cylindriques |

Les imprimantes **Delta** utilisent trois tours verticales et des bras parallèles pour positionner l'effecteur. Elles offrent un mouvement rapide et fluide et un plateau fixe, mais souffrent d'une calibration complexe (rayon delta, angles des tours) et d'une précision décroissante aux bords du plateau de construction. Leurs longs bras peuvent également fléchir à haute vitesse, limitant la précision dynamique.

💡 **Astuce de pro :** Pour les débutants, une imprimante Cartésienne moderne (comme un Ender 3 bien réglé ou un Bambu Lab A1) est parfaitement adéquate. Le CoreXY devient précieux lorsque vous souhaitez imprimer plus vite tout en maintenant la qualité, ou lorsque vous avez besoin de la stabilité de l'axe Z et de la compatibilité avec les enceintes pour les matériaux de qualité industrielle.

### Détails du trajet des courroies

Les systèmes CoreXY utilisent universellement des **courroies de distribution GT2** au **pas de 2 mm**.^[18]^ Ces courroies ont des dents qui s'engrènent précisément avec les poulies GT2, assurant un engagement positif sans glissement.

#### Largeurs de courroie

- **Courroies de 6 mm** : standard pour la plupart des constructions. Plus légères et plus flexibles. Utilisées sur le Voron 2.4
- **Courroies de 9 mm** : 50 % de surface d'engagement des dents en plus. Rigidité accrue. Utilisées sur le Rat Rig V-Core 3

#### Matériau de l'âme de la courroie

Les courroies GT2 sont renforcées soit avec de la fibre de verre, soit avec des câbles d'acier. **L'âme en fibre de verre** est plus flexible et standard pour la plupart des imprimantes 3D. **L'âme en acier** offre une rigidité plus élevée mais peut souffrir de rupture par fatigue autour des petites poulies.

### Tension des courroies et maintenance

Une tension correcte est essentielle pour les performances CoreXY. Une tension inégale entre les courroies A et B est la cause la plus fréquente de distorsion géométrique.

| Spécification | Cible |
|--------------|-------|
| Cible de tension standard | 110 ± 5 Hz sur une portée de 150 mm |
| Minimum (éviter le saut de dent) | 95 Hz |
| Maximum (protéger les roulements) | 125 Hz |

Même une petite différence entre la tension des courroies gauche et droite fera incliner le portique de manière visible sous accélération.^[17]^ La façon la plus simple de mesurer : pincez la courroie comme une corde de guitare et utilisez une application d'accordage sur smartphone pour mesurer la fréquence.

⚠️ **Avertissement :** En dessous de 95 Hz, les courroies peuvent sauter des dents sur la poulie moteur lors de virages serrés. Au-dessus de 125 Hz, vous commencez à soumettre les roulements de l'arbre moteur à des charges latérales, entraînant une usure prématurée.^[17]^

#### Liste de contrôle de maintenance

1. **Inspection des courroies** : vérifier l'usure, l'effilochage ou l'étirement mensuellement
2. **Inspection des poulies** : s'assurer que les poulies ne vacillent pas ; vérifier les vis sans tête
3. **Lubrification des glissières** : les glissières linéaires nécessitent une lubrification périodique avec une graisse de qualité
4. **Contrôle de la tension des courroies** : re-mesurer la fréquence tous les trimestres ou après avoir déplacé l'imprimante
5. **Équerrage du châssis** : vérifier les mesures diagonales annuellement

### Équerrage du châssis : l'exigence non négociable

Le CoreXY amplifie les erreurs de châssis car le portique repose sur des rails parallèles qui dépendent du parallélisme. Le châssis doit être **équerre à 0,3 mm sur la diagonale** — c'est non négociable.^[17]^ Si le châssis n'est pas équerre, les impressions seront déformées en **formes de losange** plutôt qu'en carrés.

**Test d'équerrage rapide** : imprimez un grand carré et mesurez ses diagonales. Si elles correspondent, votre alignement est correct.

### CoreXY dans les imprimantes modernes

#### Écosystème open source

- **Voron 2.4** : la conception CoreXY open source la plus influente. Une machine de volume de construction de 350 mm construite à partir d'un kit complet. Très configurable, extrêmement capable, mais nécessite un temps d'assemblage et de réglage significatif.
- **Rat Rig V-Core 3** : un kit CoreXY commercialisé avec une documentation et un support professionnels. Réputé pour son excellente qualité de construction et sa fiabilité.

#### Offres commerciales

- **Bambu Lab X1 Carbon (2022)** : la première imprimante CoreXY grand public à combiner une cinématique haute vitesse avec une calibration en boucle fermée avancée. Dispose d'un châssis en acier soudé, d'une compensation active des vibrations, d'un micro lidar pour l'inspection de la première couche et d'une surveillance de qualité assistée par IA.^[9]^
- **Bambu Lab P1P/P1S** : partage le système de mouvement CoreXY du X1 à un prix inférieur.
- **Creality K1 Series** : CoreXY avec des revendications de vitesse agressives (600 mm/s) à un prix accessible.
- **Prusa XL** : l'entrée de Prusa dans le CoreXY, dotée d'un changeur d'outil avec jusqu'à 5 têtes d'outils indépendantes.
- **Prusa Core One (2024)** : le CoreXY entièrement fermé de Prusa avec un contrôle actif de la température de chambre (jusqu'à 55°C) et un cadre supérieur en acier coulé pour l'alignement XY.

📝 **Note :** Le succès de Bambu Lab démontre que le CoreXY, combiné aux fonctionnalités modernes de firmware (façonnage d'entrée, avance de pression) et à la calibration en boucle fermée (lidars, accéléromètres), peut offrir une expérience grand public sans nécessiter les connaissances mécaniques approfondies que demandent les constructions CoreXY en kit.

### Considérations pratiques

#### Complexité de montage

Construire une imprimante CoreXY de toutes pièces ou à partir d'un kit est nettement plus complexe que d'assembler une machine Cartésienne. Les deux courroies doivent être acheminées à travers plusieurs galets, sur deux plans séparés, tout en maintenant un parallélisme parfait avec les guides linéaires.^[17]^ Chaque segment de la courroie dont la longueur change pendant le mouvement doit être parfaitement parallèle aux guides linéaires.

#### Configuration du firmware

Le firmware doit être explicitement configuré pour la cinématique CoreXY. Dans **Klipper**, cela signifie ajouter `kinematics: corexy` à la configuration de l'imprimante. Dans **Marlin**, le firmware doit être compilé avec le support CoreXY activé.

Si une imprimante CoreXY est mécaniquement construite correctement mais que le firmware est mal configuré, des erreurs spectaculaires surviennent. Une discordance dans le nombre de pas par mm entre les moteurs A et B se manifeste sous la forme d'une **inclinaison à 45 degrés** plutôt que d'une erreur uniquement en X ou uniquement en Y.^[17]^

#### Coût

Les imprimantes CoreXY coûtent généralement plus cher que les machines Cartésiennes équivalentes. Cependant, les gains de performance — notamment en vitesse d'impression et en accélération — justifient l'investissement pour les utilisateurs sérieux.

### Points clés à retenir

- **CoreXY** est un système cinématique parallèle utilisant deux moteurs fixes et des courroies croisées sur des plans empilés pour atteindre une masse en mouvement extrêmement faible.^[17]^
- Les équations fondamentales **dx = 0,5(da + db)** et **dy = 0,5(da - db)** régissent la façon dont deux rotations moteur se combinent pour produire un mouvement X-Y.^[17]^
- CoreXY permet des **vitesses de 300–500 mm/s** et des **accélérations de 10 000–20 000 mm/s²** — dépassant de loin ce que peuvent atteindre les conceptions bedslinger.^[9]^
- Comparé aux systèmes Cartésiens et Delta, CoreXY offre la meilleure combinaison de vitesse, précision et volume de construction pour l'impression FDM de bureau.
- **La tension des courroies** doit être soigneusement équilibrée (110 ± 5 Hz) et **l'équerrage du châssis** doit être à moins de 0,3 mm en diagonale — ce sont des exigences non négociables.^[17]^
- CoreXY équipe les imprimantes modernes les plus performantes, du Voron 2.4 open source aux séries Bambu Lab X1/P1 grand public.^[9]^
- Les vitesses maximales annoncées diffèrent des vitesses durables réelles ; la **capacité de débit volumétrique** du hotend et vos exigences de qualité sont les vraies limites de vitesse.
- La contrepartie des performances du CoreXY est sa **complexité mécanique** — il exige un assemblage précis, une tension de courroie soigneuse et un châssis rigide et équerre.^[17]^

---

> **Fin du Module 1.** Vous disposez maintenant d'une base complète en technologie d'impression 3D, de son histoire et de ses principes fondamentaux aux mécanismes détaillés de l'extrusion FDM et de la cinématique CoreXY. Dans le Module 2, nous construirons sur cette base pour explorer en profondeur les logiciels de tranchage — là où la conception numérique devient véritablement des instructions imprimables.

---

## Sources

Les spécifications et les prix évoluent ; vérifiez toujours auprès de la documentation du fabricant ou de l'organisme de normalisation avant d'acheter du matériel.

1. Wikipedia — Fused filament fabrication (terminologie FDM vs FFF ; FFF créé par la communauté RepRap ; expiration du brevet créditée pour la baisse des prix) : <https://en.wikipedia.org/wiki/Fused_filament_fabrication>
2. WhiteClouds — Crump, Scott (histoire d'origine de la grenouille en jouet ; polyéthylène et cire de bougie ; génie mécanique à l'Université d'État de Washington) : <https://www.whiteclouds.com/3dpedia/crump-scott/>
3. Stratasys Wikipedia (3D Modeler commercialisé en avril 1992 ; prix de 130 000 $) : <https://en.wikipedia.org/wiki/Stratasys>
4. Google Patents — US5121329A (déposé le 30 octobre 1989 ; accordé le 9 juin 1992 ; expiration le 30 octobre 2009 ; 44 revendications) : <https://patents.google.com/patent/US5121329A/en>
5. 3D Printing Journal — « 02-02-2004 : Adrian Bowyer a lancé le projet RepRap » (date de fondation ; Université de Bath) : <https://www.3dprintingjournal.com/p/02-02-2004-adrian-bowyer-launched>
6. Wikipedia — RepRap (générations Darwin, Mendel, Huxley ; titre de maître de conférences ; auto-réplication du 29 mai 2008) : <https://en.wikipedia.org/wiki/RepRap>
7. Wikipedia — Prusa i3 (conception 2012 ; kit commercial 2015 ; imprimante 3D la plus utilisée au monde en 2016) : <https://en.wikipedia.org/wiki/Prusa_i3>
8. Wikipedia — MakerBot (fondée en janvier 2009 ; Cupcake CNC 2009 ; Thingiverse lancé en novembre 2008) : <https://en.wikipedia.org/wiki/MakerBot>
9. Kickstarter — Bambu Lab X1 : CoreXY Color 3D Printer with Lidar and AI (campagne du 31 mai au 30 juin 2022 ; 5 575 contributeurs) : <https://www.kickstarter.com/projects/bambulab/bambu-lab-x1-corexy-color-3d-printer-with-lidar-and-ai>
10. Formlabs — FDM vs SLA vs SLS : Comment choisir la bonne technologie d'impression 3D (épaisseurs de couche ; isotropie SLS ; règle des 45° pour les surplombs) : <https://formlabs.com/blog/fdm-vs-sla-vs-sls-how-to-choose-the-right-3d-printing-technology/>
11. Mordor Intelligence — Marché des imprimantes 3D à technologie FDM (domination du FDM dans le segment grand public/bureau) : <https://www.mordorintelligence.com/industry-reports/fused-deposition-modeling-technology-3d-printer-market>
12. Wikipedia — STL (format de fichier) (développé par 3D Systems en 1987 ; abréviation de « stéréolithographie ») : <https://en.wikipedia.org/wiki/STL_(file_format)>
13. ISO — ISO/IEC 25422:2025 Technologies de l'information — Suite de spécifications du format de fabrication 3D (3MF) (publié en juin 2025 ; historique du consortium) : <https://www.iso.org/standard/90283.html>
14. Raise3D — Hauteur de couche en impression 3D (plage 0,05–0,4 mm ; point d'équilibre à 0,2 mm ; la hauteur de couche double le temps d'impression) : <https://www.raise3d.com/blog/3d-printing-layer-height/>
15. MatterHackers — Paramètres du firmware d'imprimante 3D : Configuration des moteurs pas à pas (1,8°/pas ; 200 pas/tour ; spécifications des courroies GT2) : <https://www.matterhackers.com/news/3d-printer-firmware-settings-stepper-motor-configuration>
16. RepRap Wiki — G-code (commandes G0, G1, G28, M104, M109, M190, M106 ; format et utilisation) : <https://reprap.org/wiki/G-code>
17. RepRap Wiki — CoreXY (cinématique parallèle ; calcul des courroies ; spécifications de tension des courroies ; équerrage du châssis à 0,3 mm ; stabilité de l'axe Z) : <https://reprap.org/wiki/CoreXY>
18. Adafruit — Courroie de distribution GT2, pas de 2 mm, largeur 6 mm (spécification GT2 au pas de 2 mm) : <https://www.adafruit.com/product/1184>

### Pour aller plus loin

- Hackaday — « Hackers, Patents, And 3D Printing » (historique des brevets FDM et impact sur la communauté) : <https://hackaday.com/2024/11/16/hackers-patents-and-3d-printing/>
- E3D Online — « 3D Printing History: The RepRap Project » (rôle de RepRap dans la démocratisation du FDM) : <https://e3d-online.com/blogs/news/history-of-reprap>
- Formlabs — « What Does Resolution Mean in 3D Printing? » (hauteur de couche, résolution XY et précision expliquées) : <https://formlabs.com/blog/3d-printer-resolution-meaning/>
- Hackaday — « Core XY Explained » (introduction technique claire à la cinématique CoreXY) : <https://hackaday.com/2019/11/12/core-xy-explained/>
