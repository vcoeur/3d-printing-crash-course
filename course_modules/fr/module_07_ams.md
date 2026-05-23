# Module 7 : Impression multi-matériaux avec l'AMS

L'impression multi-matériaux est le moment où votre imprimante 3D transcende le monde monochrome pour entrer dans la couleur. Imaginez imprimer une pièce fonctionnelle avec des sections structurelles rigides *et* des charnières flexibles intégrées, ou créer un prototype détaillé avec du texte et des logos incrustés en couleurs contrastées — le tout en un seul travail automatisé. C'est la promesse de l'**Automatic Material System (AMS)** de Bambu Lab, devenu la référence en matière d'impression multi-matériaux grand public.

Dans ce module, nous explorerons l'écosystème AMS de fond en comble : comment le matériel gère plusieurs filaments, comment concevoir des impressions multi-couleurs dans Bambu Studio, et comment minimiser le gaspillage inhérent à chaque changement de matériau. En chemin, nous aborderons ce que l'on appelle le **paradoxe du multi-matériaux** — la tension entre la commodité éblouissante des changements de couleur automatisés et la réalité inconfortable que jusqu'à 30 % de votre filament peut finir en purge gaspillée.

---

## Chapitre 1 : Présentation du système AMS

L'**Automatic Material System (AMS)** de Bambu Lab est un système de gestion automatisée des filaments permettant à une imprimante 3D à buse unique d'utiliser plusieurs couleurs ou matériaux au cours d'un même travail d'impression.^[1]^ Pensez-y comme à un bibliothécaire robotisé pour vos filaments : il stocke jusqu'à quatre bobines dans un compartiment étanche et régulé en humidité, les alimente vers l'imprimante à la demande, et les permute sans interruption lorsque votre modèle nécessite une couleur ou un matériau différent.

Depuis son lancement avec le X1 Carbon en 2022, l'écosystème AMS s'est élargi pour couvrir plusieurs gammes de prix et cas d'usage. Comprendre les différences entre les variantes est essentiel pour choisir la bonne configuration — et pour tirer le meilleur parti du système que vous possédez.

### L'écosystème AMS : quatre variantes

Bambu Lab propose actuellement quatre produits AMS distincts, chacun ciblant des imprimantes, des budgets et des applications différents. L'AMS d'origine reste le cheval de bataille, tandis que les variantes plus récentes répondent à des problèmes spécifiques comme le séchage actif, les contraintes budgétaires et les matériaux techniques.^[1]^^[2]^^[3]^^[4]^

| Spécification | AMS d'origine | AMS 2 Pro | AMS Lite | AMS HT |
|---|---|---|---|---|
| **Prix (MSRP approx.)** | ~$399 | ~$359 | ~$70 (seul) | ~$169 |
| **Bobines par unité** | 4 | 4 | 4 | **1** |
| **Boîtier** | Fermé, étanche | Fermé, séchage actif | Cadre ouvert | Fermé, séchage haute température |
| **Température de séchage max.** | Passive (dessiccant uniquement) | 65 °C | Aucune | 85 °C |
| **Système d'entraînement** | Moteur de moyeu partagé | Entraînement direct indépendant par emplacement | Porte-bobines rotatifs | Servo sans balais (60 % plus rapide) |
| **Imprimantes compatibles** | X1C, X1E, P1P, P1S | Série H2, séries X1/P1, série A1 (via OTA) | A1 et A1 Mini uniquement | Toutes les imprimantes Bambu Lab |
| **Unités chaînables max.** | 4 (16 filaments) | 4 (16 filaments) | **1 (4 filaments ; pas de hub)** | **8 (8 filaments)** |
| **Capteur d'humidité** | Oui (5 niveaux) | Oui, intelligent | Non | Oui, affichage en temps réel |
| **Idéal pour** | Multi-couleurs général (X1/P1) | Séchage actif, PETG/ABS/PLA | Entrée de gamme, série A1 | Nylon, PC, composites fibres carbone |

Sources du tableau ci-dessus.^[1]^^[2]^^[3]^^[4]^

📝 **Remarque :** Les prix fluctuent selon les promotions — l'AMS 2 Pro, par exemple, se vend à $359 MSRP mais a été proposé à $299 avec des remises. Confirmez toujours les prix actuels sur le site Bambu Lab avant d'acheter.

**AMS d'origine.** L'unité de première génération a établi le modèle : quatre emplacements pour bobines, galets d'entraînement motorisés, un moyeu central qui fusionne les chemins de filament, et un module tampon qui maintient la tension.^[1]^ Son boîtier étanche avec sachets dessiccants et un capteur d'humidité à 5 niveaux maintient les matériaux hygroscopiques au sec pendant le stockage.^[1]^ Les étiquettes RFID sur les bobines de filament Bambu Lab permettent la détection automatique du matériau et la synchronisation de la configuration avec Bambu Studio.^[5]^

**AMS 2 Pro.** La mise à niveau haut de gamme ajoute le **séchage actif des filaments jusqu'à 65 °C** — utile pour le PLA sensible à l'humidité (45 °C), le PETG (55 °C) et l'ABS (65 °C).^[2]^^[6]^ Notez que 65 °C est insuffisant pour le Nylon/PA, qui nécessite généralement 70–90 °C pour sécher correctement ; pour ces matériaux, l'AMS HT est nécessaire.^[6]^ Des entraînements directs indépendants par emplacement et des servomoteurs sans balais **60 % plus rapides** que l'original réduisent les temps de cycle de changement de filament.^[2]^ Un coupe-filament intégré assure des découpes nettes à chaque changement, et les entonnoirs d'alimentation en céramique redessinés améliorent la durabilité.^[2]^ Une limitation importante : il n'est pas possible de sécher et d'imprimer avec la même unité AMS 2 Pro simultanément — les bobines doivent être retirées des orifices d'entrée lors des cycles de séchage, bien que d'autres unités connectées puissent continuer à alimenter l'impression.^[7]^

**AMS Lite.** Conçu spécifiquement pour l'A1 et l'A1 Mini, le Lite supprime le boîtier et le contrôle de l'humidité pour atteindre un prix plus bas.^[3]^ Il utilise des porte-bobines rotatifs à cadre ouvert avec des griffes passives et un chemin de filament simplifié qui alimente directement le module de détection d'enchevêtrement de la tête d'impression.^[3]^ Le compromis est significatif : l'absence de protection contre l'humidité signifie qu'il vaut mieux éviter de laisser des filaments sensibles à l'humidité chargés pendant de longues périodes. Contrairement à l'AMS d'origine, l'AMS Lite **ne peut pas être chaîné** — il est limité à une seule unité (4 filaments) par imprimante.^[3]^

**AMS HT.** La variante haute température est conçue expressément pour les filaments techniques et accueille **une bobine par unité**.^[4]^ Là où l'AMS 2 Pro plafonne à 65 °C, le HT atteint **85 °C** — suffisant pour sécher le Nylon, le PC et les matériaux de support PVA.^[4]^ Un évent électromagnétique s'ouvre pendant le séchage pour évacuer l'humidité, puis se scelle pour le stockage. Le HT comprend une **sortie de filament dérivée spécifiquement pour les filaments souples ou flexibles** comme le TPU, qui ne peut pas circuler de manière fiable dans le chemin d'alimentation standard.^[4]^ Jusqu'à 8 unités AMS HT peuvent être connectées avec jusqu'à 4 unités AMS 2 Pro, permettant des configurations de 24 filaments simultanés.^[4]^ Si votre utilisation est centrée sur le Nylon, le polycarbonate ou les supports solubles, le HT est conçu pour vos besoins.

⚠️ **Avertissement :** Lors du chaînage de plusieurs unités AMS via l'AMS Hub, faites très attention à l'orientation du câble à 4 broches. Le brancher à l'envers peut endommager ou détruire les cartes principales de l'imprimante et de l'AMS.^[1]^

### Fonctionnement de l'AMS : le chemin du filament

Comprendre le trajet mécanique du filament dans l'AMS aide à diagnostiquer les problèmes et à optimiser les performances. Le système fonctionne comme un ensemble push-pull coordonné avec des étapes distinctes :

**1. Emplacement bobine avec galets d'entraînement motorisés.** Chacun des quatre emplacements contient une paire de galets d'entraînement motorisés qui saisissent la bobine de filament. Ces galets fournissent la première phase de force d'entraînement, poussant le filament hors de l'AMS et dans le tube de transport.

**2. Détection d'étiquette RFID.** Lorsque vous chargez une bobine de filament Bambu Lab, l'AMS lit l'étiquette RFID MIFARE sur le noyau de la bobine.^[5]^ L'étiquette contient des blocs de données chiffrés spécifiant le type de matériau, la couleur, la date de fabrication, les températures de séchage et d'impression, et plus encore — protégés par une signature numérique RSA 2048 bits que l'imprimante vérifie.^[5]^ Les filaments tiers sans étiquettes RFID nécessitent une configuration manuelle dans Bambu Studio.

**3. Le moyeu de filament.** Situé en bas de l'AMS, le moyeu contient quatre capteurs à effet Hall, un encodeur rotatif magnétique et un moteur sans balais.^[8]^ Son rôle est de fusionner quatre chemins de filament indépendants en un seul tube de sortie. Les capteurs à effet Hall détectent quand le filament atteint des positions spécifiques, déclenchant le moteur du moyeu pour fournir une seconde phase de force d'entraînement.^[8]^

**4. Tube PTFE vers le tampon.** Un tube PTFE à faible friction porte le filament de l'AMS vers l'imprimante. Ce trajet en tube peut mesurer plusieurs dizaines de centimètres, surtout dans les configurations chaînées.

**5. Le tampon de filament.** Monté à l'arrière de l'imprimante, le tampon contient un mécanisme coulissant avec un ressort et un capteur à effet Hall.^[8]^ Lorsque l'AMS pousse le filament, le coulisseau avance sous pression. Le capteur à effet Hall surveille ce déplacement et fournit un retour d'information pour éviter la surtension ou la sous-tension du chemin de filament.

**6. Extrudeur et bloc chauffe.** L'extrudeur à entraînement direct de l'imprimante fournit la force de traction finale, tirant le filament du tampon dans le bloc chauffe pour la fusion et le dépôt.

### Le processus de changement de filament

Lorsque votre impression nécessite une couleur ou un matériau différent, l'AMS exécute une séquence précisément chorégraphiée :

1. **Découpe.** Le filament actuel est sectionné par une lame à la tête d'impression, laissant une extrémité nette.
2. **Rétractation.** L'ancien filament est rétracté à travers le tampon et le moyeu jusqu'à son emplacement d'origine dans l'AMS.
3. **Chargement.** Le nouveau filament est poussé depuis son emplacement, à travers le moyeu, le tampon et l'extrudeur, jusqu'à la buse.
4. **Purge.** Le bloc chauffe extrude un volume calculé du nouveau matériau sur une **tour d'essuyage** (bloc de purge) pour évacuer le résidu du filament précédent.
5. **Reprise.** La buse étant amorcée et propre, la tête d'impression retourne au modèle et continue.

La durée mécanique brute du changement (rétractation + chargement, sans la purge) prend environ **15–25 secondes**.^[9]^ Le temps de cycle total est plus long une fois la purge incluse — les transitions à fort contraste (sombre vers clair) nécessitant 250–300 mm³ de purge s'y ajoutent significativement ; le cycle total par changement dépend fortement du volume de purge et du débit de la buse.

### Chaînage : jusqu'à 16 couleurs

Une seule unité AMS d'origine fournit quatre filaments, mais l'**AMS Hub** remplace le module tampon standard et étend la connectivité à quatre unités AMS simultanément — soit **16 filaments différents** en un seul travail d'impression.^[1]^ L'AMS Lite ne prend pas en charge ce hub ; il est limité à une seule unité par imprimante.^[3]^

Les unités se connectent via des câbles bus à 6 broches en topologie en guirlande. Bambu Lab propose deux longueurs de câble (510 mm et 1500 mm) pour des agencements d'imprimante flexibles.^[10]^

Chaque unité AMS s'attribue automatiquement un identifiant lors de la connexion. La page périphérique de Bambu Studio synchronise les informations de filament de toutes les unités connectées et mappe automatiquement les couleurs vers la correspondance disponible la plus proche.

### Contrôle de l'humidité et stockage

L'AMS d'origine, l'AMS 2 Pro et l'AMS HT incluent tous des systèmes de gestion de l'humidité. L'original utilise un système passif : des sachets dessiccants absorbent l'humidité, des joints toriques en caoutchouc silicone maintiennent une étanchéité hermétique, et un capteur d'humidité surveille les conditions sur une échelle à 5 niveaux.^[1]^ Le niveau C ou au-dessus indique des conditions nécessitant le remplacement ou le renouvellement du dessiccant.

💡 **Astuce de pro :** Après avoir séché votre dessiccant au four, les relevés d'humidité apparents peuvent temporairement augmenter lorsque le compartiment refroidit. C'est de la physique normale — l'air plus froid a une capacité de rétention d'humidité plus faible, de sorte que l'humidité relative augmente même lorsque la teneur en humidité absolue est constante. Laissez le compartiment s'équilibrer avant d'interpréter les relevés.

---

### Points clés

- L'écosystème AMS comprend quatre variantes : AMS d'origine (~$399, 4 emplacements), AMS 2 Pro (~$359 MSRP, séchage actif à 65 °C), AMS Lite (~$70, A1/A1 Mini uniquement, sans chaînage) et AMS HT (~$169, 1 bobine/unité, séchage à 85 °C pour Nylon/PC).^[1]^^[2]^^[3]^^[4]^
- Le chemin du filament passe par six étapes : emplacement bobine → détection RFID → moyeu (fusion 4→1) → tube PTFE → tampon (contrôle de tension) → extrudeur.^[8]^
- La durée mécanique brute du changement de filament est d'environ 15–25 secondes ; le temps de cycle total incluant la purge dépend du contraste de transition et du volume de purge.^[9]^
- L'AMS d'origine peut être chaîné jusqu'à quatre unités (16 filaments) via l'AMS Hub ; l'AMS Lite ne peut pas être chaîné (maximum 4 filaments).^[1]^^[3]^
- Le contrôle de l'humidité utilise des dessiccants, des joints étanches et des capteurs — critique pour les matériaux hygroscopiques comme le Nylon et le PVA.^[1]^

---

## Chapitre 2 : Découpage et impression multi-matériaux

Disposer d'un AMS connecté à votre imprimante ne représente que la moitié de l'équation. L'autre moitié se passe dans le slicer, où vous concevez quelles parties de votre modèle s'impriment dans quel matériau, configurez le comportement de purge, et prenez des décisions stratégiques qui affectent considérablement la qualité d'impression et le gaspillage. Ce chapitre couvre le flux de travail complet, de l'importation du modèle au G-code multi-matériaux optimisé.

### Configurer le multi-matériaux dans Bambu Studio

Toute impression multi-matériaux commence par la définition de vos filaments disponibles. Dans Bambu Studio, accédez au panneau **Filament** et ajoutez chaque matériau que vous prévoyez d'utiliser au projet en cours. Si vous utilisez des filaments Bambu Lab dans un AMS, ils se rempliront automatiquement via la détection RFID.^[5]^ Pour les filaments tiers, vous devrez sélectionner manuellement le bon profil (ou utiliser un profil générique avec des paramètres ajustés).

Une fois vos filaments définis, vous les attribuez à des objets ou des pièces selon deux approches principales :

**Attribution par objet.** Dans le panneau Objets, chaque modèle ou sous-pièce peut être associé à un filament spécifique. Si vous avez conçu votre modèle en CAO avec des corps séparés par couleur, exportez-le en tant que 3MF ou STL multi-pièces et utilisez la fonction **« Diviser en pièces »** dans Studio pour créer des objets colorisables séparément.^[11]^ Cette approche CAO en amont produit les transitions de couleurs les plus nettes, car les couleurs correspondent à des volumes de maillage distincts plutôt qu'à une peinture de surface.

**Attribution par peinture.** Pour les modèles à corps unique, Bambu Studio fournit des outils de peinture de couleur permettant de brosser, remplir ou sélectionner des zones par région pour différents filaments. C'est plus rapide mais moins précis — les couleurs peintes peuvent affecter de manière imprévisible la géométrie interne du remplissage.

### Outils de peinture de couleur

Bambu Studio propose plusieurs outils pour attribuer des couleurs directement sur la surface du modèle :^[11]^

| Outil | Fonction | Idéal pour |
|---|---|---|
| **Remplir** | Remplissage en pot de peinture des zones de surface connectées | Grandes régions clairement séparées |
| **Plage de hauteur** | Attribuer un filament à une tranche verticale | Couches supérieures/inférieures, texte incrusté |
| **Cercle/Sphère** | Sélection sphérique depuis un point central | Logos, éléments arrondis |
| **Segment** | Peindre des segments géométriques connectés | Formes organiques avec divisions naturelles |
| **Remplissage des espaces** | Détecte et remplit automatiquement les petites zones fermées | Détails fins, lettrage |
| **Peinture de support** | Marquer les zones nécessitant un matériau de support soluble | Surplombs complexes avec PVA/BVOH |

Sources du tableau ci-dessus.^[11]^

L'**outil de plage de hauteur** est particulièrement puissant pour un contrôle précis. Il permet de définir une plage de hauteur Z spécifique (par exemple, de 2 mm à 4 mm) et d'attribuer un filament à tout ce qui se trouve dans cette tranche verticale.^[11]^ C'est la méthode de référence pour le texte incrusté, les couches de base colorées et les motifs en bandes.

📝 **Remarque :** Le flux de travail CAO en amont (corps séparés par couleur) produit généralement des résultats plus nets que les outils de peinture. Lorsque la précision des couleurs est importante pour des pièces fonctionnelles, modélisez vos couleurs comme des corps distincts dans Fusion 360, SolidWorks ou Onshape, puis exportez en tant que 3MF multi-pièces.^[11]^

### La tour d'essuyage : rôle et configuration

La **tour d'essuyage** (également appelée bloc de purge ou tour d'amorçage) est le héros méconnu — et la plus grande source de gaspillage — de l'impression multi-matériaux. Elle remplit deux fonctions essentielles :^[12]^

1. **Purger le matériau résiduel.** À chaque changement de filament, un volume du nouveau matériau doit chasser complètement le matériau précédent hors de la buse. La tour d'essuyage absorbe ce matériau de purge.
2. **Amorcer la buse.** Après le chargement d'un nouveau filament, la buse doit établir un flux stable avant de toucher le modèle. La tour d'essuyage fournit une surface sacrificielle pour cette phase d'amorçage.

Point critique : **la taille de la tour d'essuyage dépend du nombre de changements de couleur, non de la taille de l'objet**.^[12]^ Un porte-clés minuscule avec des centaines de changements de couleur au niveau des couches génèrera une tour d'essuyage massive, tandis qu'un grand vase monochrome n'en a pas besoin.

Le gaspillage peut être considérable. Sur des impressions 4 couleurs typiques, attendez-vous à ce que **15 à 30 % de la consommation totale de filament** aille à la tour d'essuyage.^[12]^

Bambu Studio place la tour automatiquement, mais vous pouvez ajuster sa largeur dans **Paramètres d'impression → Extrudeurs multiples → Tour d'essuyage**. La tour doit être positionnée près de votre modèle pour minimiser les mouvements de déplacement, et elle ne doit pas intersecter les objets imprimés.^[12]^ Pour les tours très hautes et étroites, activez l'option de cône de stabilisation pour éviter qu'elle ne tombe.^[12]^

💡 **Astuce de pro :** Faire pivoter votre modèle de manière à regrouper les changements de couleur dans les couches inférieures peut réduire sensiblement le matériau de la tour d'essuyage. La tour rétrécit parce que les besoins en purge sont concentrés au début plutôt que répartis sur toute la hauteur.

### Calcul du volume de purge

Bambu Studio calcule automatiquement les volumes de purge (« chasse ») requis en fonction de deux facteurs principaux : le **contraste de couleur** entre les filaments sortant et entrant, et les **propriétés du matériau**.^[13]^

| Type de transition | Volume de chasse typique |
|---|---|
| Blanc → Noir | ~44 mm³ |
| Noir → Blanc | 250–300 mm³ |
| Couleurs similaires (rouge → orange) | 60–100 mm³ |
| Matériaux différents | 200–400+ mm³ |

Sources du tableau ci-dessus.^[13]^

L'asymétrie est frappante : passer d'une couleur sombre à une couleur claire nécessite environ 3 à 5 fois plus de purge que l'inverse, parce que même une trace de pigment sombre est visible dans une pièce de couleur claire.^[13]^

Le **Multiplicateur de chasse** dans Bambu Studio fournit un facteur d'échelle global pour toutes les valeurs calculées automatiquement. La valeur par défaut est 1,0×, mais de nombreux utilisateurs expérimentés le réduisent à **0,6–0,8×** pour réduire le gaspillage de 20 à 40 % avec un impact minimal sur la qualité.^[14]^ Réduisez progressivement — trop bas, et vous verrez des saignées de couleur visibles (« fantômes ») dans vos impressions.

Les valeurs individuelles des paires de/vers peuvent également être modifiées dans le tableau des volumes de chasse. Si vous savez que votre combinaison spécifique de filaments fonctionne avec moins de purge, réduisez-la. Cliquer sur **« Recalculer »** réinitialise tout aux valeurs par défaut.

⚠️ **Avertissement :** Régler le multiplicateur de chasse trop bas provoque une contamination visible des couleurs. Testez toujours sur une petite impression sans importance avant de vous engager dans un grand projet multi-jours avec des valeurs de purge réduites.

### Purge dans le remplissage et le support

Bambu Studio fournit des fonctionnalités puissantes de réduction du gaspillage qui redirigent le matériau de purge depuis la tour d'essuyage vers des zones cachées de votre impression :

**Purge dans le remplissage des objets.** Ce paramètre redirige le matériau de purge dans la structure de remplissage interne du modèle plutôt que dans la tour d'essuyage.^[13]^ Comme le remplissage est recouvert par les parois extérieures, les couleurs de transition aléatoires sont invisibles — à condition que vos parois soient suffisamment épaisses et que votre filament soit opaque. Soyez prudent avec le PETG translucide, le PLA de couleur claire avec des parois minces, ou les modèles avec peu de périmètres, car les couleurs peuvent « transparaître ».

**Purge dans les supports des objets.** Comme les supports sont de toute façon retirés après l'impression, ils constituent des cibles idéales pour le matériau de purge. Cette option est **activée par défaut** car il n'y a pratiquement aucun inconvénient.^[13]^ La principale limitation est que beaucoup d'impressions n'ont tout simplement pas assez de volume de support pour absorber une purge significative.

**Purge dans cet objet (objets sacrificiels).** En désignant un objet sacrificiel sur le plateau d'impression, vous pouvez rediriger presque tout le matériau de purge vers un élément fonctionnel plutôt que vers une tour de déchets. Des praticiens de la communauté rapportent des réductions de purge spectaculaires — parfois supérieures à 90 % — en combinant purge vers objet, purge vers remplissage et un multiplicateur de chasse réduit.^[15]^ L'objet sacrificiel reçoit un remplissage aléatoire multicolore mais peut tout de même être fonctionnel : des témoins de test de peinture, des organiseurs de bureau, des cales ou des jouets antistatiques conviennent parfaitement.

### Bonnes pratiques pour le multi-matériaux

Au-delà des paramètres du slicer, les décisions stratégiques prises lors des phases de conception et de préparation ont un impact majeur sur les résultats et le gaspillage :

**Regroupez les mêmes couleurs ensemble.** Dans votre modèle CAO ou dans l'orientation d'impression, disposez les régions de même couleur de façon à ce qu'elles soient contiguës. Chaque limite de couleur est un potentiel changement de filament — minimisez-les dès la phase de conception.

**Utilisez la couleur la plus courante comme base.** La couleur qui couvre la plus grande surface doit généralement être votre filament « d'arrière-plan » ou de base. Cela minimise le nombre total de changements.

**Imprimez ensemble des matériaux à températures similaires.** Une impression multi-matériaux réussie nécessite des matériaux avec des températures d'impression compatibles.^[16]^ Le PLA se marie bien avec le PETG et le PVA. L'ABS fonctionne avec l'ASA et le HIPS. Tenter de combiner du PLA (200 °C) avec du polycarbonate (290 °C) dans un système à buse unique dégradera l'un des matériaux ou ne fera pas fondre l'autre correctement.

**Regroupez les impressions multi-couleurs ensemble.** Lorsque vous imprimez plusieurs objets sur le même plateau, les changements de couleur se produisent simultanément pour tous les objets — sans purge supplémentaire par pièce.^[13]^ Cela réduit considérablement le gaspillage par objet pour les productions en série.

💡 **Astuce de pro :** L'impression multi-matériaux fonctionnelle — comme les supports solubles PVA pour des géométries complexes, ou la combinaison de matériaux rigides et flexibles dans une seule pièce — délivre souvent plus de valeur pratique que les simples changements de couleur esthétiques. Le gaspillage est justifié par des capacités qui seraient impossibles avec une impression mono-matériau.

---

### Points clés

- Bambu Studio propose deux flux de travail principaux : attribution de couleur par objet (transitions plus nettes) et outils de peinture (plus rapide, plus flexible).^[11]^
- La tour d'essuyage est indispensable pour les fonctions de purge et d'amorçage, mais consomme 15 à 30 % du filament total sur des impressions 4 couleurs typiques.^[12]^
- Le volume de chasse varie considérablement selon le type de transition : noir vers blanc nécessite 250–300 mm³, tandis que blanc vers noir n'en nécessite que ~44 mm³.^[13]^
- Réduire le multiplicateur de chasse à 0,6–0,8× peut diminuer le gaspillage de 20 à 40 % avec un impact minimal sur la qualité.^[14]^
- Les techniques de purge dans le remplissage et dans un objet sacrificiel peuvent réduire le gaspillage spectaculairement lorsqu'elles sont combinées stratégiquement.^[15]^
- Les matériaux à températures similaires fonctionnent mieux ensemble ; les grands écarts de température entraînent une dégradation et des problèmes de flux.^[16]^

---

## Chapitre 3 : Astuces, limites et alternatives à l'AMS

Vous comprenez désormais comment fonctionne l'AMS et comment configurer les impressions multi-matériaux dans le slicer. Ce dernier chapitre est plus pratique : réduire le gaspillage avec des stratégies complètes, résoudre les problèmes que vous rencontrerez inévitablement, entretenir votre système pour sa longévité, et savoir quand envisager d'autres solutions que l'AMS.

### Stratégies complètes de réduction du gaspillage

Le **paradoxe du multi-matériaux** est bien réel : l'AMS rend l'impression multi-couleurs sans effort, mais cette commodité a un coût matériel. La bonne nouvelle est que des stratégies de réduction du gaspillage combinées peuvent ramener votre purge de 30 % du filament total à moins de 5 %.^[15]^ Voici la boîte à outils complète :

**Stratégie 1 : Réduire le multiplicateur de chasse.** Commencez prudemment à 0,8×, testez sur un petit modèle, et descendez à 0,6× si vos transitions de couleur sont propres. Les transitions clair vers sombre tolèrent des multiplicateurs bien plus faibles que les transitions sombre vers clair.^[14]^

**Stratégie 2 : Activer la purge dans le remplissage et le support.** La purge dans les supports est activée par défaut — laissez-la. Ajoutez la purge dans le remplissage pour les modèles avec un volume de remplissage généreux et des filaments opaques. Surveillez les fantômes sur les impressions à parois minces ou translucides.^[13]^

**Stratégie 3 : Utiliser des objets sacrificiels de purge.** Ajoutez un objet fonctionnel sur votre plateau d'impression et désignez-le comme cible de purge. L'objet doit être au moins aussi haut que votre dernier changement de couleur. Les organiseurs de bureau, les cubes de calibration et les jouets antistatiques constituent d'excellents objets de purge.^[15]^

**Stratégie 4 : Ordre des couleurs stratégique.** Séquencez vos changements d'outil pour minimiser les transitions à fort contraste. Imprimez les couleurs sombres avant les claires autant que possible (moins de purge nécessaire). Regroupez les couleurs similaires de manière adjacente dans la séquence d'impression.^[13]^

**Stratégie 5 : Regrouper les impressions multi-couleurs.** Imprimer plusieurs objets simultanément signifie des changements de couleur partagés sans pénalité de purge par objet.^[13]^ Une impression 4 couleurs d'une figurine génère la même tour d'essuyage que quatre figurines sur le même plateau.

| Technique | Économies estimées | Niveau d'effort |
|---|---|---|
| Réduire le multiplicateur à 0,8× | 10–20 % | Faible |
| Réduire le multiplicateur à 0,6× | 20–40 % | Faible-Moyen |
| Purge dans le remplissage | 10–30 % | Faible |
| Purge dans les supports | 5–15 % | Faible (activé auto.) |
| Purge dans objet(s) sacrificiel(s) | 50–90 %+ | Moyen |
| Impression groupée de plusieurs pièces | 20–50 % par pièce | Faible |
| Ordre des couleurs stratégique | 10–20 % | Faible (phase de conception) |
| Orientation du modèle pour changements groupés | Jusqu'à 40 % | Faible |
| **Approche combinée** | **80–90 %+** | **Élevé** |

Sources du tableau ci-dessus.^[14]^^[15]^

### Problèmes courants de l'AMS et solutions

Même avec l'expérience utilisateur soignée de l'AMS, certains problèmes reviennent suffisamment fréquemment pour que tout utilisateur connaisse les solutions.

**Bobines en carton.** Les galets d'entraînement de l'AMS saisissent les bobines par leurs bords. Les bords en carton se dégradent sous cette pression, générant des débris qui provoquent des défauts d'alimentation et des bourrages.^[17]^ Les solutions comprennent l'enroulement des bords de bobines en carton avec du ruban électrique, l'impression de rondelles de renforcement 3D depuis MakerWorld, ou le rembobinage du filament sur des bobines réutilisables Bambu Lab.^[17]^ L'AMS Lite gère mieux le carton grâce à ses porte-bobines rotatifs à cadre ouvert.

**TPU et filaments flexibles.** Le TPU standard (dureté Shore 95A) est **officiellement incompatible** avec l'AMS. Le matériau souple et flexible flambe et se bloque dans les longs tubes PTFE sous la force de poussée de l'AMS.^[18]^ Si vous avez besoin d'un matériau flexible dans un travail multi-matériaux, Bambu Lab vend un **TPU pour AMS** spécial (dureté 68D, moins flexible) spécifiquement conçu pour fonctionner avec le système d'alimentation.^[18]^ Pour le TPU standard, utilisez plutôt le porte-bobine externe.

**Filaments abrasifs.** Les filaments en fibres de carbone, en fibres de verre et phosphorescents sont abrasifs et usent progressivement les tubes PTFE internes de l'AMS.^[17]^ Sur l'AMS d'origine et l'AMS 2 Pro, envisagez de placer les filaments abrasifs sur le porte-bobine externe pour protéger vos tubes PTFE. La sortie dérivée de l'AMS HT est conçue pour les filaments **souples ou flexibles**, pas spécifiquement comme dérivation pour abrasifs.^[4]^

**Filament humide.** L'humidité dans le filament provoque des bruits de claquement, des bulles de vapeur, une mauvaise adhérence des couches et une surface rugueuse. Même avec le contrôle d'humidité de l'AMS, le pré-séchage des matériaux hygroscopiques avant le chargement est indispensable. L'AMS 2 Pro et le HT peuvent sécher activement le filament chargé, mais l'AMS d'origine repose sur un dessiccant passif — dont la capacité de séchage est limitée pour les filaments déjà saturés.^[1]^

### Maintenance de l'AMS

Une maintenance régulière maintient votre AMS en fonctionnement fiable et prévient les pannes en cours d'impression qui gaspillent des heures et du filament.

**Nettoyer les galets d'entraînement et les entonnoirs.** La poussière de filament et les débris s'accumulent sur les galets d'entraînement et dans les entonnoirs d'alimentation. Nettoyez-les mensuellement (ou hebdomadairement pour une impression à fort volume) avec de l'air comprimé ou une brosse souple. Les entonnoirs en céramique de l'AMS 2 Pro sont plus durables que les conceptions précédentes mais nécessitent toujours une attention.^[2]^

**Remplacer les tubes PTFE.** Les tubes PTFE internes sont des consommables. En utilisation normale, remplacez-les tous les deux mois ; pour les filaments abrasifs (fibres de carbone, fibres de verre, phosphorescents), remplacez-les mensuellement.^[17]^ Des tubes usés augmentent la friction, provoquant une sous-extrusion et des changements de filament manqués.

**Renouveler le dessiccant.** Remplacez ou re-séchez les sachets dessiccants lorsque le capteur d'humidité indique le niveau C ou au-dessus — généralement toutes les 4 à 6 semaines d'utilisation active. Séchez le dessiccant usagé dans un four à la température spécifiée par le fabricant (généralement 65–80 °C pendant plusieurs heures).

**Vérifier le tampon et le moyeu.** Assurez-vous que le coulisseau du tampon se déplace librement et que le ressort n'est pas comprimé ou endommagé. Vérifiez que le moyeu ne présente pas d'accumulation de débris de filament, surtout après des chargements manqués ou des bourrages.

**Mettre à jour le firmware.** Bambu Lab publie régulièrement des mises à jour du firmware qui améliorent la fiabilité de l'AMS, les séquences de changement et la gestion des erreurs. Maintenez à jour le firmware de votre imprimante et de votre AMS.

### Alternatives à l'AMS

L'AMS n'est pas la seule voie vers l'impression multi-matériaux. Selon votre imprimante, votre budget et votre tolérance au bricolage, ces alternatives peuvent valoir la peine d'être envisagées :^[9]^^[19]^^[20]^^[21]^^[22]^

| Système | Matériaux max. | Mécanisme | Complexité d'installation | Idéal pour |
|---|---|---|---|---|
| **Bambu AMS** | 16 (4 unités) | Galets motorisés + moyeu | Plug and play | Utilisateurs Bambu Lab, facilité d'utilisation |
| **Prusa MMU3** | 5 | Barre sélectrice + Bowden partagé | Assemblage modéré | Utilisateurs Prusa MK-series, préférence open source |
| **Mosaic Palette 3** | 4–8 | Épisseur externe | Modéré | Toute imprimante FDM, agnostique vis-à-vis de l'imprimante |
| **ERCF** | 8+ | Sélecteur + coupe-filament DIY | Élevé (build auto-sourcé) | Utilisateurs Klipper/Voron, bricoleurs |
| **Changement manuel** | Illimité (séquentiel) | Pause par couche, changement à la main | Aucun | Changements de couleur occasionnels, débutants |

Sources du tableau ci-dessus.^[9]^^[19]^^[20]^^[21]^^[22]^

**Prusa MMU3.** Le Multi-Material Upgrade 3 supporte cinq matériaux sur les imprimantes Prusa MK4/S, MK3.9/S, MK3.5/S, MK3S+ et CORE One — la MINI+ n'est pas compatible.^[19]^ Contrairement aux moteurs d'alimentation individuels de l'AMS, le MMU3 utilise une barre sélectrice unique avec un tube Bowden partagé.^[19]^ L'installation nécessite un assemblage mécanique modéré, mais le système est entièrement open source et bénéficie d'un fort soutien communautaire. Les supports solubles PVA sont un point fort particulier. Les temps de changement se sont améliorés significativement avec les récentes mises à jour du firmware — désormais environ 42 secondes par changement — contre environ 52 secondes précédemment.^[20]^

**Mosaic Palette 3.** Cet épisseur externe agnostique vis-à-vis de l'imprimante découpe et soude thermiquement des segments de filament en un seul brin avant qu'il n'entre dans votre imprimante.^[21]^ Il fonctionne avec pratiquement n'importe quelle imprimante FDM, ce qui le rend attrayant si vous souhaitez du multi-matériaux sans remplacer votre machine. Le logiciel Canvas offre un flux de travail de peinture de texture intuitif. Cependant, le gaspillage de purge peut être substantiel, et à ~$799–$899 pour la version Pro, il coûte autant qu'une imprimante Bambu complète avec AMS.^[21]^

**ERCF (Enraged Rabbit Carrot Feeder).** Un système DIY open source populaire pour les imprimantes basées sur Klipper (Voron, RatRig, etc.). La version 2 ajoute un coupe-filament à la tête d'impression qui élimine les exigences de mise en forme de la pointe de la V1, et s'intègre directement au firmware Klipper avec une fonctionnalité de « bobine sans fin » pour des impressions longues sans surveillance.^[22]^ L'ERCF est un projet d'auto-sourcing et de réglage significatif — gratifiant pour les utilisateurs avancés, décourageant pour les débutants.

**Changement manuel de filament.** L'approche la plus simple : utilisez la fonction de pause par couche de Bambu Studio (clic droit sur le « + » du curseur de couche après le découpage) pour faire une pause à des hauteurs spécifiques, puis changez le filament à la main.^[23]^ Cela fonctionne avec les commandes de changement de filament M600 et ne nécessite aucun matériel supplémentaire. Cette méthode est limitée aux changements à la hauteur des couches (pas de changements de couleur en milieu de couche) et nécessite une présence physique, mais elle est totalement gratuite et ne génère aucun déchet de purge.

### Quand le multi-matériaux est-il justifié ?

Compte tenu du gaspillage, de la complexité et du coût matériel, il vaut la peine de se demander : quand le multi-matériaux en vaut-il vraiment la peine ?

**Les applications fonctionnelles** délivrent systématiquement plus de valeur que les applications esthétiques. Les supports solubles avec PVA ou BVOH permettent des géométries qui seraient impossibles avec des supports à casser — canaux internes, surplombs complexes et structures en treillis délicates. La combinaison de matériaux structuraux rigides avec des sections flexibles (PLA + TPU) crée des charnières intégrées, des poignées et des amortisseurs en une seule impression. Ces capacités justifient le coût de purge car elles permettent des conceptions qui n'ont aucun équivalent mono-matériau.

**Les applications esthétiques** — logos multi-couleurs, éléments décoratifs, incrustations de texte — sont visuellement impressionnantes, mais doivent être évaluées honnêtement. Une impression 4 couleurs vaut-elle 30 % de gaspillage matériel et un temps d'impression doublé ? Parfois oui (présentation de prototype, cadeaux, modèles d'exposition), mais la nouveauté s'estompe rapidement pour les impressions fonctionnelles du quotidien.

Les praticiens du multi-matériaux les plus efficaces suivent une règle simple : **utiliser le nombre minimum de matériaux qui permet d'atteindre l'objectif de conception**. Une impression 2 couleurs avec un placement de couleur stratégique et des paramètres de purge optimisés peut être aussi belle qu'une impression 4 couleurs avec les paramètres par défaut — tout en utilisant deux fois moins de matériau et en se terminant deux fois plus vite.

📝 **Remarque :** Le paradoxe du multi-matériaux ne signifie pas que vous devez éviter l'impression multi-couleurs. Il signifie que vous devez l'aborder stratégiquement : minimiser les changements à la phase de conception, optimiser les paramètres de purge, et réserver les travaux multi-matériaux complexes aux cas où la capacité permet véritablement quelque chose d'impossible autrement.

---

### Points clés

- Une approche combinée de réduction du gaspillage (multiplicateur réduit + purge dans le remplissage/objet + impression groupée + ordre stratégique) peut diminuer les déchets de purge de 80–90 %+.^[15]^
- Les bobines en carton nécessitent du ruban adhésif ou des rondelles de renforcement ; le TPU standard (95A) bourre dans l'AMS — utilisez le TPU pour AMS (68D) ou une bobine externe ; les filaments abrasifs usent les tubes PTFE et nécessitent un remplacement mensuel.^[17]^^[18]^
- Maintenance régulière : nettoyer les galets mensuellement, remplacer les tubes PTFE tous les 1 à 2 mois (plus tôt pour les abrasifs), renouveler le dessiccant toutes les 4 à 6 semaines.^[17]^
- Les alternatives comprennent le Prusa MMU3 (open source, 5 matériaux, série MK uniquement), le Palette 3 (agnostique vis-à-vis de l'imprimante, ~$800), l'ERCF (DIY Klipper) et le changement manuel par pause par couche (gratuit mais limité).^[19]^^[20]^^[21]^^[22]^
- Le multi-matériaux fonctionnel (supports solubles, combinaisons de matériaux) délivre généralement plus de valeur pratique que les simples changements de couleur esthétiques.

---

## Sources

Les spécifications et les prix changent à chaque génération de produit ; confirmez toujours les données actuelles sur la fiche technique du fabricant avant d'acheter.

1. MatterHackers — Page produit Bambu Lab AMS (4 emplacements ; boîtier étanche ; dessiccant + capteur d'humidité 5 niveaux ; compatible X1C, X1E, P1S, P1P ; jusqu'à 4 unités via AMS Hub = 16 filaments ; ~$399) : <https://www.matterhackers.com/store/l/bambu-lab-ams-automatic-material-system/sk/M72GRQTC>
2. Dynamism — Page produit Bambu Lab AMS 2 Pro (4 emplacements ; séchage actif 65 °C ; servo sans balais 60 % plus rapide ; $359 MSRP ; compatible H2 series, X1/P1, A1 via OTA) : <https://www.dynamism.com/bambu-lab/bambu-lab-ams-2-pro.html>
3. 3DPros — Comparaison Bambu AMS vs AMS Lite (AMS Lite : A1/A1 Mini uniquement ; cadre ouvert ; sans contrôle d'humidité ; sans chaînage ; max 4 filaments) : <https://3dpros.com/printer-content/bambu-lab-ams-vs-ams-lite>
4. SwingDesign — Page produit Bambu Lab AMS HT (1 bobine par unité ; séchage max 85 °C ; sortie dérivée pour filaments souples/flexibles ; jusqu'à 8 AMS HT + 4 AMS 2 Pro = 24 filaments ; compatible X1C, X1E, P1S, P1C, P2S, H2D, H2C, H2S, X2D, A1 ; ~$169) : <https://www.swingdesign.com/products/bambu-lab-single-spool-automatic-material-system-ams-ht-with-filament-dryer>
5. Bambu Research Group — Guide des étiquettes RFID (étiquette MIFARE ; blocs de données chiffrés ; signature RSA 2048 bits ; type de matériau, couleur, températures, données bobine) : <https://github.com/Bambu-Research-Group/RFID-Tag-Guide/blob/main/BambuLabRfid.md>
6. How-To Geek — « I Love Bambu Lab's AMS 2 Pro, But These 6 Things Annoy Me » (65 °C insuffisant pour le nylon qui nécessite ~80 °C ; prix $359) : <https://www.howtogeek.com/i-love-bambu-labs-ams-2-pro-but-these-things-annoy-me/>
7. Forum communautaire Bambu Lab — Limitation du séchage AMS 2 Pro (impossible de sécher et imprimer sur la même unité simultanément) : <https://forum.bambulab.com/t/ams-2-pro-ridiculous-limitation/159895>
8. Wiki Bambu Lab — Introduction à l'AMS / Présentation des fonctions AMS (moyeu : 4 capteurs à effet Hall, encodeur rotatif magnétique, moteur sans balais ; tampon : coulisseau, ressort, capteur à effet Hall) : <https://wiki.bambulab.com/en/ams/manual/ams-function-introduction>
9. Zbotic — « Multi-Material 3D Printing: Bambu AMS vs Prusa MMU3 » (changement brut AMS ~15–25 secondes ; comparaison MMU3) : <https://zbotic.in/multi-material-3d-printing-bambu-ams-vs-prusa-mmu3-guide/>
10. Boutique Bambu Lab US — Page produit câble Bambu Bus (câble bus 6 broches ; longueurs 510 mm et 1500 mm) : <https://us.store.bambulab.com/products/bambu-bus-cable>
11. ADP Industries — Guide complet d'impression multi-couleurs Bambu Lab avec AMS (flux de travail par objet vs peinture ; outil de plage de hauteur ; approche CAO en amont) : <https://adpindustries.com/blog/bambu-lab-multi-color-printing-guide/>
12. stlDenise3D — « No More Printer Poop! Banish Bambu Purge Waste » (fonction de la tour d'essuyage ; 15–30 % de gaspillage sur les impressions 4 couleurs ; multiplicateur de chasse) : <https://stldenise3d.com/no-more-printer-poop-banish-bambu-purge-waste-with-these-hot-tips/>
13. stlDenise3D — ibid. (blanc→noir ~44 mm³ ; noir→blanc 250–300 mm³ ; purge dans le remplissage ; purge dans les supports activée par défaut ; changements partagés en impression groupée)
14. stlDenise3D — ibid. (multiplicateur de chasse 0,6–0,8× réduit le gaspillage de 20–40 %)
15. MakerWorld — Page modèle « Reduce purge by up to 45% » (technique de l'objet sacrificiel de purge ; stratégies combinées) : <https://makerworld.com/en/models/91241-reduce-purge-by-up-to-45-obsolete>
16. ADP Industries — ibid. (températures d'impression compatibles ; PLA + PETG ; ABS + ASA ; les écarts de température entraînent une dégradation)
17. ADP Industries — Guide de dépannage Bambu Lab AMS (poussière/débris des bobines en carton ; tubes PTFE consommables, remplacement tous les 2 mois normal / 1 mois pour les filaments abrasifs CF/GF) : <https://www.adpindustries.com/blog/bambu-lab-ams-troubleshooting-guide/>
18. Bambu Lab — Produit TPU pour AMS (dureté 68D ; compatible AMS ; TPU standard 95A incompatible — flambe dans le tube PTFE) : <https://us.store.bambulab.com/products/tpu-for-ams>
19. Base de connaissances Prusa — Compatibilité MMU3 (compatible MK4/S, MK3.9/S, MK3.5/S, MK3S+, CORE One ; MINI+ non compatible ; 5 matériaux) : <https://help.prusa3d.com/article/mmu3-compatibility_470808>
20. Blog Prusa — « Massive MMU3 Speed Boost » (nouveau firmware réduit le temps de changement à ~42 secondes, contre ~52 secondes précédemment) : <https://blog.prusa3d.com/massive-mmu3-speed-boost-new-fw-slashes-filament-change-times-core-one-l-mmu3-news_132957/>
21. Mosaic Manufacturing — Page produit Palette 3 Pro (agnostique vis-à-vis de l'imprimante ; épisseur externe ; logiciel Canvas ; ~$799 Pro) : <https://www.mosaicmfg.com/products/palette-3-pro>
22. Zbotic — « Multi-Material 3D Printing: AMS, MMU & Palette Explained » (coupe-filament ERCF V2 à la tête d'impression ; intégration Klipper ; bobine sans fin) : <https://zbotic.in/multi-material-3d-printing-ams-mmu-palette-explained/>
23. ADP Industries — ibid. (pause par couche via clic droit sur le curseur de couche ; commande M600 de changement de filament ; zéro déchet de purge ; changements à la hauteur des couches uniquement)

### Pour aller plus loin

- Wiki Bambu Lab — Introduction et présentation du flux de travail AMS : <https://wiki.bambulab.com/en/x1/manual/intro-ams>
- Wiki Bambu Lab — Recommandations de séchage des filaments (températures par type de matériau) : <https://wiki.bambulab.com/en/filament-acc/filament/dry-filament>
- Forum communautaire Bambu Lab — Calibration des volumes de chasse AMS et réduction de purge (tests communautaires, paramètres optimisés) : <https://forum.bambulab.com/t/ams-flushing-volumes-calibration-purge-reduction/37062>
- All3DP — Vue d'ensemble de l'impression 3D multi-matériaux et comparaison des systèmes : <https://all3dp.com/2/multi-color-3d-printing/>
