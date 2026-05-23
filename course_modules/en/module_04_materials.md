# Module 4: FDM Materials Complete Guide

> "The material is the message. Choose the right filament, and your design comes to life exactly as imagined. Choose wrong, and even the perfect model becomes a warped, brittle disappointment."

Welcome to the most practical module in this course. Every 3D print you've ever admired -- and every one that's failed -- comes down to two things: the machine settings and the material. In this module, we'll explore the full spectrum of FDM filaments, from the forgiving PLA every beginner starts with to the demanding engineering plastics that rival injection-molded parts. By the end, you'll have a clear decision framework for matching any project to the right material, plus the storage and handling knowledge to keep your filaments performing at their best.

---

## Chapter 1: PLA and Everyday Materials

The journey into 3D printing materials begins with two workhorses: **PLA** (Polylactic Acid) and **PETG** (Polyethylene Terephthalate Glycol). Together, these two materials account for the vast majority of consumer 3D printing worldwide. They are affordable, widely available, and forgiving enough that you can focus on learning your printer rather than fighting your filament.

### PLA (Polylactic Acid) -- The Beginner's Best Friend

PLA is the undisputed champion of beginner 3D printing. Derived from renewable resources like corn starch or sugar cane, it prints at relatively low temperatures, produces minimal odor, and requires no heated chamber or special equipment.^[1]^ If you've seen a 3D print, it was probably PLA.

#### Key Properties

Think of PLA as the craft paper of 3D printing -- easy to work with, capable of beautiful results, but not suited for demanding applications. Its **glass transition temperature** (the point where it begins to soften) sits around 60°C, meaning a PLA part left in a hot car on a summer day will deform into a sad puddle of plastic.^[1]^ It is also somewhat brittle, prone to snapping under sharp impacts rather than flexing.

However, PLA's strengths are substantial: exceptional **dimensional accuracy** (parts come out very close to their designed dimensions), excellent **surface finish**, and virtually zero **warping** (the tendency of corners to lift off the print bed). These qualities make it ideal for prototypes, decorative items, display models, and low-stress functional parts.

#### Optimal Print Settings

| Parameter | Recommended Range |
|-----------|------------------|
| Nozzle Temperature | 190-230°C |
| Bed Temperature | 45-60°C (optional for many prints) |
| Print Speed | 40-60 mm/s |
| Cooling Fan | 100% after first few layers |
| Retraction (Bowden) | 4-6mm at 45-60 mm/s |
| Retraction (Direct Drive) | 0.5-1.5mm at 25-45 mm/s |
| Enclosure | Not required |

Temperature ranges above are drawn from manufacturer datasheets and the Prusa and Polymaker material guides.^[1]^^[2]^

💡 **Pro Tip:** Start every new PLA spool at 200°C and a 60°C bed. If you hear a sizzling sound or see bubbles in the extruded filament, your filament has absorbed moisture -- dry it at 45-50°C for 4-6 hours before continuing.^[1]^

#### The PLA Variants Ecosystem

The "basic" PLA label hides a surprisingly diverse family of formulations. Here are the most common variants you'll encounter:

**PLA+ (Enhanced PLA):** Despite the name, **PLA+** is not a standardized material -- it's a marketing term covering PLA modified with various additives.^[3]^ eSUN PLA+ contains about 2% calcium carbonate; Polymaker PolyMAX PLA uses acrylic polymers; other brands may add TPU or nucleating agents. The result is typically improved toughness, reduced brittleness, and slightly better heat resistance, all while maintaining PLA's easy printability.^[3]^ Manufacturers rarely disclose exact formulations.^[3]^

**Silk PLA:** Contains additives that create a glossy, almost iridescent surface finish. Silk PLA produces stunning visual results -- vases, figurines, and decorative items look almost injection-molded. The tradeoff is weaker **layer adhesion**, making silk PLA unsuitable for structural parts.

**Matte PLA:** The opposite of silk -- matte formulations scatter light to create a diffuse, low-reflection surface that naturally hides **layer lines**. If you want that modern, injection-molded look without post-processing, matte PLA is your best bet.

**Rapid/Speed PLA:** Formulated specifically for high-speed printers (300mm/s+), these PLAs have optimized melt flow characteristics to prevent heat-related issues at extreme speeds. If you own a Bambu Lab X1 or similar high-speed machine, speed PLA will give you the best results when printing fast.

📝 **Note:** Standard PLA works fine on high-speed printers too -- rapid PLA just gives you more headroom. Don't feel you need to buy special filament to go fast.

#### The Biodegradability Myth

⚠️ **Warning:** PLA is frequently marketed as "biodegradable" and "eco-friendly." The reality is far more nuanced. PLA only breaks down under **industrial composting conditions** -- sustained temperatures of around 58-60°C with specific microbial activity.^[4]^ Studies show PLA does not fully disintegrate under normal marine conditions after 428 days in a seawater environment.^[4]^ In your home compost pile, a landfill, or the ocean, PLA persists for decades just like conventional plastic.^[4]^

This doesn't make PLA worse than other plastics -- it's still derived from renewable resources rather than petroleum -- but it does mean you shouldn't choose PLA primarily for environmental reasons. When PLA eventually reaches an industrial composting facility, it performs well, but most communities lack these facilities.

### PETG -- The Functional Upgrade

If PLA is craft paper, **PETG** is cardstock. It's the most capable "everyday" filament, offering a compelling balance of strength, durability, and printability that makes it the go-to material for functional mechanical parts.^[5]^

PETG is chemically similar to the PET used in water bottles but with glycol added to prevent crystallization and make it easier to process. The result is a filament that's tougher than PLA, more temperature resistant, chemically resistant, and far easier to print than ABS.

#### Key Advantages Over PLA

- **Superior layer adhesion:** PETG bonds between layers exceptionally well, making parts stronger in the Z-axis (the direction most 3D prints are weakest)
- **Chemical resistance:** PETG stands up to water, mild acids, and many solvents that would attack PLA
- **Higher temperature resistance:** PETG parts begin to soften around 75-80°C, comfortably above PLA's ~60°C limit^[5]^
- **UV resistance:** Moderate resistance to sun exposure, though ASA is better for prolonged outdoor use
- **Flexibility:** PETG has a slight give that makes it more impact-resistant than the rigid PLA

#### Optimal Print Settings

| Parameter | Recommended Range |
|-----------|------------------|
| Nozzle Temperature | 230-250°C (start at 240°C) |
| Bed Temperature | 80-90°C |
| Print Speed | 30-50 mm/s (up to 300mm/s with speed formulations) |
| Cooling Fan | 30-50% after first 2-3 layers |
| Retraction (Bowden) | 4-6mm at 45-60 mm/s |
| Retraction (Direct Drive) | 1-2mm at 45 mm/s |
| First Layer Speed | 15-20 mm/s |

Temperature ranges above are drawn from the Prusa Knowledge Base and the Overture filament guide.^[5]^^[6]^

#### Taming Stringing

PETG's biggest weakness is **stringing** -- thin wisps of plastic that stretch between separate parts of a print during travel moves. PETG stays molten longer than PLA, making it prone to oozing from the nozzle when it shouldn't be extruding.

Here's the systematic approach to eliminating stringing:^[6]^

1. **Dry your filament first.** Moisture is the #1 cause of PETG stringing. Dry at 65°C for 7 hours before any troubleshooting.^[6]^
2. **Reduce temperature.** Try 230-235°C if you're currently at 250°C. Lower temperatures mean the plastic solidifies faster.
3. **Increase retraction speed.** Push for 60 mm/s retraction speed.
4. **Enable "Wipe Before Travel."** This feature drags the nozzle across the infill before moving, leaving any ooze behind.
5. **Reduce travel speed slightly.** Slower moves give the plastic less time to ooze.

⚠️ **Warning:** PETG can bond so aggressively to certain bed surfaces -- especially bare borosilicate glass -- that it will pull chunks of glass out of the bed when you remove the print. Always use a PEI sheet, painter's tape, or a thin layer of glue stick as a release agent when printing PETG on glass.^[5]^

#### Food Safety Reality Check

You'll often see PETG described as "food safe" because the base polymer is FDA-approved for food contact. Here's the critical distinction: the **filament** may be food-safe, but a **3D printed object** made from it almost certainly is not.^[7]^

The layer lines in any FDM print create microscopic crevices where bacteria can grow and food residue becomes trapped. These grooves are nearly impossible to clean thoroughly, even with a dishwasher. If you must print something for food contact, use natural (uncolored) PETG and treat the object as disposable. Water bottles for repeated use? Absolutely not. Cookie cutters for occasional single-use? Acceptable, but plan to replace them regularly.^[7]^

### Key Takeaways

- **PLA** is the ideal starting material: low temperature (190-230°C nozzle, 45-60°C bed), minimal warping, great surface finish. Use it for prototypes, decorative items, and anything that won't face heat above 60°C.^[1]^^[2]^
- **PLA+** offers improved toughness with the same printability, but manufacturers rarely disclose what additives they use.^[3]^
- **PETG** is your go-to functional material: tougher than PLA, excellent layer adhesion, and good chemical resistance. Watch out for stringing and aggressive bed adhesion.^[5]^^[6]^
- Neither PLA nor PETG is truly home-compostable or food-safe in practice, despite marketing claims.^[4]^^[7]^
- The recommended progression: master PLA, then expand to PETG for functional parts.

---

## Chapter 2: Engineering Materials

Once you've mastered PLA and PETG, a world of demanding engineering materials opens up. These filaments require higher temperatures, enclosures, and more careful handling -- but they deliver properties that rival injection-molded engineering plastics. This chapter covers ABS, ASA, Nylon, and Polycarbonate: the materials that turn your 3D printer into a tool for serious manufacturing.

### ABS -- The Classic Engineering Plastic

**ABS** (Acrylonitrile Butadiene Styrene) is the same material used in LEGO bricks, automotive interior panels, and countless consumer products. It's tough, impact-resistant, heat-tolerant, and can be chemically smoothed to a glossy finish that hides layer lines entirely. For years, ABS was the default "serious" 3D printing material.

#### Properties and Applications

ABS offers a compelling combination of properties that made it the standard for functional prototyping before PETG became widely available. Its glass transition temperature of ~105°C means it can handle significantly more heat than PLA.^[8]^ It's impact-resistant enough for mechanical parts, can be drilled and tapped, and responds beautifully to **acetone vapor smoothing** -- a chemical process that dissolves the outer layer and leaves an injection-molded appearance.^[9]^

Applications include functional prototypes, automotive parts, electronic enclosures, drone frames, and any component that needs to handle moderate heat and mechanical stress.

#### Optimal Print Settings

| Parameter | Recommended Range |
|-----------|------------------|
| Nozzle Temperature | 230-260°C |
| Bed Temperature | 80-110°C |
| Print Speed | 40-60 mm/s |
| Cooling Fan | Off for first 3 layers, 10-20% maximum |
| Enclosure | Required |
| Chamber Temperature | 40-60°C recommended |

Temperature ranges above are drawn from the Prusa Knowledge Base and multiple manufacturer guides.^[8]^

#### The ABS Challenges

Printing ABS is where 3D printing transitions from hobby to craft. Three major challenges await:

**1. Warping.** ABS contracts significantly as it cools. Without consistent temperature control, corners will lift off the bed, tall features will crack, and large flat surfaces will develop a pronounced curl. An **enclosure** is not optional for ABS -- it's mandatory.^[8]^ Even a simple DIY enclosure (many makers convert IKEA Lack tables) makes the difference between success and frustration.

**2. Fumes.** ABS emits **styrene fumes** during printing -- an irritant with a distinct sharp, chemical smell.^[10]^ Styrene is classified by IARC as a **probable human carcinogen (Group 2A)**, upgraded from Group 2B in 2019.^[11]^ Never print ABS in a living space without ventilation. The ideal setup vents the enclosure outside through a duct and fan, or at minimum uses an enclosure with an activated carbon filter in a well-ventilated room.

**3. Bed Adhesion.** ABS needs a hot bed (80-110°C) and a bed surface it can grip firmly. PEI sheets, ABS slurry (dissolved ABS in acetone painted on the bed), and specialized build plates all work. Too cold, and the print lifts. Too loose, and you get the dreaded "spaghetti" failure.

⚠️ **Warning:** ABS fumes are no joke. Research consistently shows that 3D printing ABS releases volatile organic compounds (VOCs) including styrene, and ultrafine particles.^[10]^ Print in an enclosure with ventilation to the outdoors, or at minimum in a dedicated workshop with a HEPA+carbon air purifier. Never in a bedroom or living area.

#### Acetone Vapor Smoothing

One of ABS's unique superpowers is its solubility in acetone. This enables **acetone vapor smoothing**, which dissolves the outer surface of the print, causing layer lines to flow together and disappear.^[9]^

The cold vapor method (safer): Place your ABS print in a sealed glass container with acetone-soaked paper towels for 30-60 minutes. The fumes gradually soften the surface without the risk of overheating.

The hot vapor method (faster but riskier): Use a heated container at 40-50°C to accelerate the process. **Acetone is extremely flammable with a flash point of -20°C.**^[12]^ Never use an open flame or spark near acetone, and ensure adequate ventilation.

📝 **Note:** ASA and HIPS can also be acetone-smoothed because they contain the same styrene component. PLA, PETG, Nylon, and TPU cannot be smoothed with acetone -- it has little to no effect on them.

### ASA -- The Outdoor-Friendly ABS Alternative

**ASA** (Acrylonitrile Styrene Acrylate) is what ABS wants to be when it grows up. It shares nearly all of ABS's strengths while adding the one thing ABS critically lacks: **UV resistance**.^[13]^

The difference comes down to chemistry. ABS uses butadiene rubber for impact resistance; ASA substitutes acrylate rubber instead. This swap eliminates ABS's vulnerability to sunlight degradation while maintaining similar mechanical properties.^[13]^

#### ASA vs. ABS Comparison

| Property | ABS | ASA |
|----------|-----|-----|
| UV Resistance | Poor -- degrades in sunlight | Excellent -- color-stable outdoors |
| Weather Resistance | Poor | Excellent |
| Heat Resistance | Up to ~105°C Tg | Up to ~100-105°C Tg |
| Fumes/Odor | Significant styrene fumes | Similar styrene content |
| Warping Tendency | High | Moderate (similar to ABS) |
| Surface Finish | Can be smoothed to glossy | Matte (typically) |
| Acetone Smoothing | Yes | Yes |

#### Optimal Print Settings

| Parameter | Recommended Range |
|-----------|------------------|
| Nozzle Temperature | 240-270°C |
| Bed Temperature | 90-110°C |
| Cooling Fan | Off first 3 layers, 10-20% maximum |
| Enclosure | Required (similar to ABS) |
| Print Speed | 40-60 mm/s |

Temperature ranges above are drawn from the Prusa Knowledge Base (260°C nozzle, 105-110°C bed reference) and other manufacturer guides.^[13]^

💡 **Pro Tip:** ASA is the default recommendation over ABS for nearly every application today. The only reasons to choose ABS over ASA are: (1) you specifically need acetone smoothing (both work, though results vary by brand), or (2) ASA is unavailable or significantly more expensive in your region. For outdoor parts, ASA wins on every metric.^[13]^

ASA applications include automotive exterior parts, garden equipment, outdoor signage, marine components, and any functional part exposed to sunlight.

### Nylon (PA6, PA12) -- The Wear-Resistant Workhorse

**Nylon** -- technically **polyamide** (PA) -- represents a major step up in mechanical performance. It is exceptionally strong, highly wear-resistant, naturally low-friction, and has enough flexibility to absorb impacts without breaking. If you need a printed gear, bushing, hinge, or structural component that will see real use, Nylon should be on your shortlist.

#### Types of Nylon for 3D Printing

| Type | Best For | Main Advantage | Main Challenge |
|------|----------|---------------|---------------|
| PA6 | Strong functional parts | Tough, strong, widely available | Absorbs moisture rapidly |
| PA66 | Precision mechanical parts | Higher stiffness, wear resistance | Highly hygroscopic |
| PA12 | Dimensional stability | Lower moisture uptake than PA6 | Usually more expensive |
| PA11 | Impact-resistant parts | Flexible and tough | Less commonly available |
| PA-CF | Stiff engineering parts | Better stiffness, lower warping | Abrasive to nozzles |
| PA-GF | Durable functional parts | Good dimensional stability | Abrasive, rougher surface |

**PA6** is the most common type and offers excellent all-around performance. However, it can absorb up to 3% of its weight in water from the air -- "almost a shot glass of moisture for every spool."^[14]^ **PA12** absorbs only about 0.5% moisture but still prints better when thoroughly dried.^[14]^

#### Critical: Moisture Management

Nylon is among the most moisture-sensitive filaments in existence. A spool left out overnight in a humid room can go from perfect to unprintable. Wet Nylon produces prints with poor layer adhesion, rough surfaces, and a popping/sizzling sound from steam in the hotend.

**Drying is mandatory:** Dry Nylon at 75-90°C for 4-8 hours (some recommend up to 24 hours for heavily saturated spools) before printing.^[15]^ A dedicated filament dryer is strongly recommended -- most food dehydrators top out at around 70°C, which is insufficient for thoroughly drying Nylon.

**Storage is critical:** After drying, store Nylon in an airtight container with fresh desiccant. Better yet, print directly from a **dry box** -- a sealed container with filament feeding through a tube to the printer, maintaining a low-humidity environment throughout the print.

📝 **Note:** Nylon parts change their properties after exposure to ambient moisture. Dry-as-printed Nylon is stiffer and stronger; after absorbing moisture from the environment, it becomes more ductile and impact-resistant.^[14]^ If your application requires specific properties, consider "conditioning" your parts by storing them at a controlled humidity level before use.

#### Optimal Print Settings

| Parameter | Recommended Range |
|-----------|------------------|
| Nozzle Temperature | 250-285°C (varies by type) |
| Bed Temperature | 70-110°C |
| Print Speed | 30-60 mm/s |
| Cooling Fan | Off or minimal |
| Enclosure | Recommended (especially for PA6) |
| Nozzle Type | Hardened steel for fiber-filled variants |

Temperature ranges above are drawn from the Prusa Knowledge Base Nylon guide.^[15]^

### Polycarbonate (PC) -- The Ultimate Challenge

**Polycarbonate** sits at the top of the common-material difficulty pyramid. It offers extreme strength, a glass transition temperature around 150°C, a heat deflection temperature exceeding 115°C, excellent impact resistance, and the ability to be bent without breaking.^[16]^ It is naturally transparent, though most PC filaments contain additives to enable lower-temperature printing.

#### Why PC Is So Difficult

Polycarbonate is among the most challenging common filaments to print successfully.^[17]^ The challenges include:

- **Extreme warping:** Even more severe than ABS. Without a heated enclosure and chamber temperature of 60-70°C, large PC prints are nearly impossible.
- **High temperatures:** Requires 260-310°C nozzle and 90-120°C bed. Only all-metal hotends can handle these temperatures safely -- PTFE-lined hotends degrade and release toxic fumes above ~240°C.^[16]^^[17]^
- **Moisture sensitivity:** PC is hygroscopic and must be thoroughly dried at 70-80°C for 6-8 hours before printing.^[16]^
- **UV sensitivity:** PC degrades under prolonged sun exposure, making it unsuitable for outdoor use without protective coating.

An innovative technique involves using extremely wide extrusion lines (0.75mm width at 0.2mm layer height) to apply pressure-based bonding rather than relying solely on temperature.^[17]^ This approach can dramatically improve layer adhesion.

#### Optimal Print Settings

| Parameter | Recommended Range |
|-----------|------------------|
| Nozzle Temperature | 260-310°C |
| Bed Temperature | 90-120°C |
| Print Speed | 30-60 mm/s |
| Cooling Fan | Minimal or off |
| Enclosure | Required (60-70°C chamber ideal) |
| Hotend Type | All-metal required |

Temperature ranges above are drawn from Polymaker's PC guide and the Simplify3D materials guide.^[16]^^[17]^

💡 **Pro Tip:** Before attempting PC, ensure your printer is fully capable: all-metal hotend, heated bed that can reliably reach 110°C, and an enclosure that maintains a warm chamber. If your printer can't provide these, stick with PETG or Nylon for high-performance parts. Printing PC on an under-spec machine will produce weak, delaminated parts that waste expensive filament.

### Key Takeaways

- **ABS** requires an enclosure, high bed temperatures, and ventilation for styrene fumes. Consider whether ASA might be a better choice for your application.^[8]^^[10]^
- **ASA** is the preferred outdoor material: UV-resistant and acetone-smoothable; its styrene content is similar to ABS so ventilation still applies.^[13]^
- **Nylon** demands meticulous moisture management -- dry before every print, store in airtight containers, and print from a dry box when possible.^[14]^^[15]^
- **Polycarbonate** is the most demanding common material, requiring all-metal hotends, heated enclosures, and precise temperature control. It rewards successful printing with exceptional strength and heat resistance.^[16]^^[17]^
- The enclosure is not optional for these materials -- it is a capability gate that determines whether you can print engineering plastics at all.

---

## Chapter 3: Flexible and Specialty Materials

The materials in this chapter break the rigid-plastic paradigm. Flexible filaments let you print rubber-like parts. Composite filaments embed fibers for engineering-grade stiffness. Specialty filaments add unique visual and functional properties. And support materials enable geometries that would be impossible to print otherwise. This is where 3D printing gets creative -- and occasionally demanding.

### TPU and TPE -- Flexible Filaments

**TPU** (Thermoplastic Polyurethane) and **TPE** (Thermoplastic Elastomer) are the rubber of the 3D printing world. They can bend, stretch, compress, and return to their original shape. If you've ever held a 3D printed phone case, drone bumper, or shoe insole, it was likely TPU.

#### Understanding Shore Hardness

TPU flexibility is measured on the **Shore A scale**, where lower numbers mean softer, more flexible material:

| Hardness | Feel Comparison | Printability | Applications |
|----------|----------------|--------------|-------------|
| 60A-70A | Extra soft (rubber band) | Extremely difficult | Specialized wearables |
| 85A | Very soft (shoe insole, leather belt) | Challenging | Gaskets, seals, wearables |
| 90A | Medium-soft | Moderate | Functional rubber parts |
| 95A | Firm flexible (standard eraser) | Good | Phone cases, drone bumpers, grips |
| 98A+ | Nearly rigid | Easy (prints like stiff PETG) | Structural flexible parts |

💡 **Pro Tip:** For 95% of applications, **95A TPU** is the sweet spot. It offers enough flexibility for vibration dampening, grip surfaces, and impact protection while remaining printable on most machines. 85A TPU is extremely challenging to extrude consistently -- it requires a well-tuned direct drive extruder and patience.^[18]^

#### Print Settings by Hardness

| Parameter | 95A TPU | 85A TPU |
|-----------|---------|---------|
| Nozzle Temperature | 210-240°C | 210-230°C |
| Bed Temperature | 30-60°C | 25-60°C |
| Print Speed | 20-30 mm/s | 15-20 mm/s |
| Retraction | 0.5-1.5mm at 20-30 mm/s | Turn OFF (0mm) |
| Cooling Fan | On | On |
| Extruder Type | Direct drive preferred | Direct drive required |

Temperature ranges above are drawn from the Siraya Tech TPU user guides.^[18]^

#### The Direct Drive Requirement

Here's the critical thing about flexible filaments: **they compress.** When the extruder gears push a rigid filament, it moves forward predictably. When they push a soft, flexible filament, it can buckle and compress inside the extruder assembly or Bowden tube rather than pushing through the nozzle. This leads to inconsistent extrusion, gaps in prints, and outright jams.

**Direct drive extruders** -- where the motor and gears sit right above the hotend with a very short filament path -- handle TPU far better than **Bowden extruders**, which push filament through a long tube. You can print 95A TPU on a Bowden system with careful tuning, but 85A essentially requires direct drive.^[18]^

⚠️ **Warning:** TPU is hygroscopic. Wet TPU produces extreme stringing, rough surface texture, and weak layer bonds. Dry your TPU at 60-70°C for 4-6 hours before printing, and store it in an airtight container with desiccant between uses.^[19]^

**Applications:** Phone cases, drone bumpers, RC tire treads, vibration dampening feet, protective covers, gaskets, seals, watch bands, shoe insoles, ergonomic grips, and anywhere you need impact absorption or flexibility.

### Carbon Fiber Filled Filaments

**Carbon fiber filled filaments** blend chopped carbon fibers into a base polymer (PLA, PETG, Nylon, etc.) to dramatically increase stiffness, dimensional stability, and heat resistance. The fibers act like rebar in concrete -- they don't make the material tougher, but they make it much more rigid and warp-resistant.^[20]^

#### What's Actually in CF Filaments?

The "carbon fiber" in 3D printing filaments consists of short chopped fibers mixed throughout the base plastic. These are not continuous fibers -- they don't create the ultra-high strength of aerospace carbon fiber composites. What they do provide is significant improvement in:

- **Stiffness:** CF-filled parts resist bending much better than their unfilled counterparts
- **Dimensional stability:** Less warping and shrinkage during cooling
- **Heat resistance:** Slightly higher temperature tolerance
- **Surface finish:** A distinctive matte, textured appearance that hides layer lines

#### The Critical Tradeoffs

Carbon fiber giveth, and carbon fiber taketh away:^[20]^

| Advantage | Disadvantage |
|-----------|-------------|
| Increased stiffness | Increased brittleness (less impact resistance) |
| Reduced warping | Reduced layer-to-layer adhesion |
| Higher heat resistance | Requires hardened nozzles (abrasive) |
| Matte, professional finish | More expensive (~$40-60/kg) |
| Lighter weight (for stiffness) | Rougher surface finish |

⚠️ **Warning:** Carbon fiber filaments are **abrasive.** The tiny carbon fibers act like sandpaper inside your hotend. A standard brass nozzle will be worn through quickly. You need a **hardened steel**, **tungsten carbide**, or **ruby-tipped nozzle** for any CF-filled filament. A 0.6mm nozzle diameter is also recommended to reduce clogging risk.^[20]^

#### Types of CF-Filled Filaments

| Base Material | Nozzle Temp | Best For |
|--------------|-------------|---------|
| PLA-CF | 200-230°C | Stiff prototypes, RC parts, decorative technical parts |
| PETG-CF | 240-265°C | Functional stiff parts, drone frames |
| PA-CF (Nylon) | 260-285°C | Engineering-grade stiffness, gears, structural components |

Temperature ranges above are drawn from the Prusa composite materials guide and Simplify3D.^[20]^^[21]^

📝 **Note:** In some testing, standard PETG has outperformed PLA-CF in load-bearing capacity. Carbon fiber increases stiffness but not necessarily strength. Choose CF-filled filaments when you need rigidity and dimensional stability, not when you need maximum toughness.^[21]^

### Glass Fiber and Kevlar Filled Filaments

**Glass fiber filled** filaments offer a different tradeoff than carbon fiber. Research shows that glass fiber reinforcement in PLA significantly increases tensile strength and stiffness, while also improving impact resistance.^[22]^ Glass fiber filaments are available in PCTG, Nylon, and PA bases. Like CF, they require hardened nozzles.^[20]^

**Kevlar/aramid fiber filled** filaments are less common but offer unique properties. Unlike carbon and glass fibers, Kevlar fibers don't fracture easily under stress -- instead, they experience shear fracture and tearing, providing exceptional damage resistance.^[20]^ Kevlar fibers also exhibit less nozzle abrasion than carbon fibers, making them gentler on your equipment.^[20]^

### Metal Filled and Specialty Filaments

The world of specialty filaments is vast and creative. Here's a quick reference:

| Filament Type | What It Does | Special Considerations |
|--------------|-------------|----------------------|
| Metal filled (iron, copper, bronze) | Metallic weight, appearance, can be patinated/rust | Hardened nozzle; higher density |
| Magnetic iron PLA | Ferromagnetic -- responds to magnets | Can be rusted for antique effects |
| Wood filled | Real wood fibers; can be sanded and stained | Requires 0.5-0.6mm+ nozzle; higher risk of clogging |
| Glow-in-the-dark | Phosphorescent additives; glows after charging | Abrasive -- requires hardened nozzle |
| Color-changing (thermochromic) | Changes color with temperature | Print at standard PLA temperatures |
| Marble/stone look | Mineral particles for speckled surface | Hides layer lines beautifully |
| Conductive PLA | Carbon additives; electrically conductive | For sensors, not power transmission |

**Metal filled filaments** are particularly interesting for post-processing. A print in iron-filled filament can be sanded smooth, then exposed to moisture to develop a genuine rust patina. Copper-filled prints can be polished and treated with vinegar/salt solutions to develop a green verdigris. These techniques bridge the gap between 3D printing and traditional metalworking aesthetics.

**Conductive PLA** deserves a reality check: it is millions of times less conductive than copper. You won't be printing circuit boards or power cables. What you can do is create touch sensors, simple circuit prototypes, antistatic enclosures, and interactive objects that respond to capacitive touch.

### Support Materials

Complex geometries -- overhangs beyond 45-60°, internal cavities, arches, and bridges -- require **support structures** that hold up the printed plastic during construction and are removed afterward. But what if the support is inside a cavity you can't reach with pliers? That's where soluble support materials come in.

#### PVA (Water-Soluble Supports)

**PVA** (Polyvinyl Alcohol) is the standard water-soluble support material. It dissolves in room-temperature water, making it ideal for complex internal geometries. PVA pairs best with PLA (similar print temperatures) and can work with PETG with tuning. PVA demonstrates over 90% biodegradation within 56 days in water (ISO 14851).^[23]^

| Parameter | Value |
|-----------|-------|
| Nozzle Temperature | 180-220°C |
| Bed Temperature | 45-60°C |
| Drying | 45-50°C for 8-12 hours (required!) |
| Compatibility | Best with PLA |
| Cooling Fan | 100% |

Temperature ranges above are drawn from manufacturer documentation and the Prusa filament drying guide.^[24]^^[23]^

PVA is extremely moisture-sensitive -- more so than Nylon. A spool left out in humid air can become a gummy, unprintable mess in hours.^[24]^ Store PVA in vacuum-sealed bags with desiccant, and only remove it immediately before printing.

#### HIPS (Limonene-Soluble Supports)

**HIPS** (High Impact Polystyrene) dissolves in **d-Limonene** (a citrus oil extract), not water.^[25]^ HIPS is commonly paired as a support material with models where the build material is not attacked by limonene; note that ABS and ASA also partially dissolve in limonene, so material compatibility should be verified before using HIPS in a specific pairing.^[25]^ HIPS can be acetone-smoothed and has mechanical properties similar to ABS.

HIPS nozzle temperature: 225-255°C; bed temperature: 100-110°C.^[25]^

#### Bambu Lab Breakaway Supports

📝 **Note:** The following section references a Bambu Lab-specific feature. Similar breakaway support materials exist from other manufacturers.

Bambu Lab offers dedicated **breakaway support filaments** designed to separate cleanly from the primary material by hand, without chemical dissolution. These are available in formulations for PLA and for PA/PET engineering materials.^[26]^ Breakaway supports are faster than soluble supports (no waiting for dissolution) but may not work as well for complex internal geometries where you can't reach the support material.

### Key Takeaways

- **TPU 95A** is the most printable flexible filament, suitable for phone cases, bumpers, and grips. Direct drive extruders are strongly preferred.^[18]^
- **Carbon fiber filled** filaments dramatically increase stiffness but require hardened nozzles and are more brittle than unfilled versions. They're for rigidity, not toughness.^[20]^^[21]^
- **Specialty filaments** (wood, metal, glow, conductive) add unique aesthetics and limited functionality. Each has specific nozzle and print requirements.
- **Support materials** enable impossible geometries: PVA for water-soluble supports (best with PLA), HIPS for limonene-soluble supports (verify build material compatibility with limonene before use).^[23]^^[25]^
- The general material progression for difficulty: PLA -> PETG -> TPU 95A -> ABS/ASA -> Nylon -> CF-filled -> PC.

---

## Chapter 4: Material Selection and Storage

You've now met the major families of FDM materials. But how do you actually choose which one to use? And once you've bought a dozen spools, how do you keep them all in print-ready condition? This chapter gives you a practical framework for both questions.

### Material Selection Decision Matrix

The most common question in 3D printing is simple: "What material should I use for this project?" Here's a decision matrix that covers the most common scenarios:

| Use Case | Recommended Material | Why |
|----------|---------------------|-----|
| Beginner first prints | **PLA** | Easiest to print, most forgiving, excellent results with minimal tuning |
| Decorative/display pieces | **Silk/Matte PLA** | Superior surface aesthetics |
| Functional indoor parts | **PETG** | Tough, excellent layer adhesion, chemical resistant |
| Parts handled regularly | **PETG or PLA+** | Impact resistance and durability |
| Outdoor parts | **ASA** | UV resistant, weather stable, good mechanical properties |
| High heat applications (>80°C) | **ABS, ASA, or PC** | High glass transition temperatures |
| Flexible/rubber-like parts | **TPU 95A** | Excellent flexibility with good printability |
| Wearables (in direct contact) | **TPU 85A** | Soft, skin-safe, comfortable |
| Engineering prototypes | **Nylon PA12** | Strong, wear resistant, lower moisture uptake |
| Gears, bushings, bearings | **Nylon PA6 or PA12** | Self-lubricating, low friction |
| Stiff technical parts | **PA-CF** | Carbon fiber reinforcement, engineering-grade stiffness |
| Lightweight RC/drone frames | **PLA-CF or PETG-CF** | Good stiffness-to-weight ratio |
| Food contact (disposable only) | **Natural PETG** | Best chemical profile, but still needs sealing |
| Transparent parts | **Clear PETG** | Best optical clarity among common filaments |

#### The Selection Hierarchy

A practical hierarchy emerges from the community's collective experience:^[1]^^[5]^

1. **Start with PLA** for anything that doesn't need special properties. It's the default.
2. **Move to PETG** for functional parts, anything handled regularly, or when you need better strength and chemical resistance.
3. **Choose ASA** for outdoor parts that will see UV exposure.
4. **Consider ABS** only if you specifically need acetone smoothing or if ASA is unavailable.
5. **Select TPU** when flexibility is the primary requirement.
6. **Use Nylon or PC** for serious engineering applications demanding maximum strength, wear resistance, or heat tolerance.

The proliferation of PLA variants (Silk, Matte, Rapid) mostly serves marketing rather than creating genuinely new material categories. A good PLA+ or quality standard PLA will handle 90% of your printing needs.

### Filament Storage: The Moisture Battle

Almost all 3D printing filaments are **hygroscopic** -- they actively absorb moisture from the air. This moisture doesn't just sit inside the plastic; it turns to steam in your hotend, creating bubbles that disrupt melt flow, weaken layer adhesion, cause stringing, and leave rough, inconsistent surfaces.

Some materials absorb moisture so rapidly that leaving a spool out overnight in a humid room noticeably affects print quality. Nylon, PVA, and TPU are the worst offenders. Even PLA, which is relatively resistant, will degrade over weeks of exposure.

#### Signs Your Filament Is Wet

- **Popping or sizzling** sounds from the hotend during printing
- **Bubbling** visible in the extruded filament
- **Excessive stringing** that doesn't improve with retraction tuning
- **Weak, brittle layer adhesion** -- parts snap along layer lines
- **Rough, uneven surface finish** on what should be smooth surfaces
- **Steam or smoke** visible from the nozzle (not normal)

#### Storage Solutions

| Solution | Cost | Effectiveness | Best For |
|----------|------|--------------|----------|
| Vacuum-sealed bags with desiccant | $ | Excellent | Long-term storage of rarely-used spools |
| Airtight plastic bins with desiccant | $$ | Very good | Active spool storage |
| Filament dry boxes (print-while-stored) | $$ | Very good | Printing directly from dry storage |
| Electronic filament dryers | $$-$$$ | Excellent | Active drying before printing |
| Camera dry cabinets | $$$ | Excellent | Large collections, professional use |
| Bambu Lab AMS/AMS 2 Pro | $$$ | Very good | Integrated multi-material with active drying |

**Best practices for storage:**

- Keep humidity below 20% for most filaments, below 15% for Nylon and PVA
- Use airtight containers with real sealing gaskets (not just snap lids)
- Include desiccant packs: 50-100g of silica gel per container
- Monitor with a hygrometer (digital humidity meter)
- Store in cool, dark places away from direct sunlight
- Use color-changing silica gel so you know when desiccant needs refreshing
- Print directly from a dry box when possible, especially for moisture-sensitive materials

💡 **Pro Tip:** Activated alumina desiccant is superior to standard silica gel for humidity-critical materials. It absorbs more moisture and can be dried and reused at higher temperatures.^[27]^ Look for it at industrial supply stores or online.

#### Drying Temperatures and Times

| Material | Drying Temperature | Drying Time | Max Storage Humidity |
|----------|-------------------|-------------|---------------------|
| PLA | 45-50°C | 6+ hours | <30% |
| PETG | 55-65°C | 6-7 hours | <25% |
| TPU | 60-70°C | 4-6 hours | <20% |
| ABS | 75-85°C | 4 hours | <25% |
| ASA | 75-80°C | 4 hours | <25% |
| Nylon | 75-90°C | 4-24 hours | <15% |
| Polycarbonate | 70-80°C | 6-8 hours | <20% |
| PVA | 45-50°C | 8-12 hours | <10% |
| CF/GF-filled | Match base material | Match base material | Match base material |

Drying temperatures and times above are drawn from the Prusa Knowledge Base filament drying guide and the Overture drying guide.^[24]^^[28]^

⚠️ **Warning:** PLA will soften and physically deform on the spool if dried above 55°C -- it begins to soften at around 60°C (its glass transition temperature).^[28]^ Nylon requires the highest drying temperatures; most food dehydrators top out at around 70°C and are insufficient for thoroughly drying Nylon, which needs up to 90°C.^[15]^^[24]^

**Popular filament dryers:** SUNLU S2, EIBOS Filadryer, and PrintDry are popular options. The AMS 2 Pro offers integrated drying up to 65°C for Bambu Lab users. For a budget option, a basic food dehydrator works for PLA and PETG (stay under 55°C) but won't reach the temperatures needed for Nylon.

### Food Safety: The Uncomfortable Truth

No guide to 3D printing materials would be complete without addressing food safety honestly. Despite what marketing might suggest, **no FDM 3D printed part is truly food-safe without significant post-processing.** Here's why:^[7]^

**Three Barriers to Food Safety:**

1. **Layer Lines:** The microscopic grooves between printed layers are a "seedbed for bacteria" -- impossible to clean properly and ideal for trapping food residue.^[7]^ Even dishwasher cycles can't reach into these crevices.

2. **Material Additives:** Even "food-safe" base polymers like PETG contain pigments, flow aids, and other additives that manufacturers don't disclose. Some filaments have FDA-approved base resins, but that approval often excludes colored variants.^[7]^

3. **Printer Contamination:** Standard brass nozzles are not food-safe due to wear particles entering the printed material; brass nozzles also typically contain lead.^[7]^^[29]^ If you've ever printed ABS, carbon fiber, or any non-food material through your hotend, residue from those prints can contaminate subsequent "food-safe" prints.

#### Practical Food Safety Guidance

| Application | Recommendation |
|-------------|---------------|
| Cookie cutters | Acceptable; treat as disposable after some use^[7]^ |
| Kitchen tools (spatulas, spoons) | Not recommended unless sealed with food-safe epoxy |
| Water bottles / drink containers | No -- impossible to clean, risk of bacterial growth^[7]^ |
| Decorative serving pieces | Acceptable if only decorative (not in food contact) |
| Garden markers | Fine -- not food contact |

**Mitigation strategies** (if you must print for food contact):

- Use **natural/uncolored PETG** -- it has the best chemical safety profile of common filaments
- Apply a **food-safe epoxy coating** (such as ArtResin or Smooth-On XTC) to seal layer lines completely
- Use a **stainless steel nozzle** (avoid brass due to wear particles and lead content)^[29]^
- Thoroughly clean the hotend before any food-related print
- Treat food-contact prints as **disposable** -- plan to replace them
- Never use 3D printed parts for long-term liquid storage

### Environmental Considerations

The environmental impact of 3D printing is a topic that deserves honest discussion:

**PLA is not home-compostable.** As discussed in Chapter 1, PLA requires industrial composting conditions at around 58-60°C to break down.^[4]^ Most communities lack these facilities. Studies show PLA shows no meaningful degradation in marine environments after 428 days.^[4]^ PLA is made from renewable resources, which is a genuine advantage over petroleum-based plastics, but its end-of-life story is more complex than "it's biodegradable."

**Failed prints are a significant source of waste.** Support material, failed prototypes, calibration prints, and misprints all accumulate. Most discarded filament won't break down naturally.

**Recycling options exist but are limited:**

- **ProtoCycler** and similar devices can shred and re-extrude failed prints and scrap into new filament
- **Community recycling programs** are emerging in maker spaces and universities
- **Filament recycling services** accept scrap in some regions
- **Mechanical recycling** -- failed PLA prints can be downcycled into less demanding applications

**Practical steps to reduce waste:**

- Use flush-into-infill techniques to reduce purge waste on multi-material prints
- Save and properly store partial spools rather than letting them go to waste
- Print infill-only models for calibration rather than solid cubes
- Choose the right material for the job -- a failed ABS print because you didn't have an enclosure is wasted material

### Key Takeaways

- **Use the decision matrix** as your starting point: PLA for ease, PETG for function, ASA for outdoors, TPU for flexibility, Nylon for engineering, PC for extreme demands.
- **Moisture is the enemy of every filament.** Invest in proper storage -- airtight containers with desiccant are the minimum. Dry your filament before printing, especially Nylon, PVA, and TPU.^[24]^^[28]^
- **No FDM print is food-safe without coating.** Layer lines, material additives, and printer contamination create three insurmountable barriers.^[7]^^[29]^ Use natural PETG, seal with epoxy, or better yet, don't use 3D prints for food contact.
- **PLA is not home-compostable.** It requires industrial facilities. Be realistic about the environmental claims of 3D printing materials.^[4]^
- **Material selection is a hierarchy.** Start simple and only move up the difficulty ladder when your application genuinely demands it. Mastering PETG well is more useful than struggling with PC.

---

## Module Summary

This module has covered the full spectrum of FDM materials, from the forgiving PLA that welcomes every beginner to the demanding polycarbonate that rewards experienced makers with engineering-grade parts. The key principles to remember:

1. **Match material to application**, not to what sounds impressive. A well-printed PETG part beats a poorly-printed PC part every time.

2. **Respect the hierarchy:** PLA -> PETG -> ASA/ABS -> TPU -> Nylon -> PC. Each step up brings new capabilities but also new requirements.

3. **Enclosures and ventilation are safety equipment**, not optional upgrades, when printing ABS, ASA, PC, or Nylon.

4. **Dry your filament.** Moisture ruins more prints than bad slicer settings.

5. **Be skeptical of marketing claims.** PLA+ is unstandardized, PLA is not home-compostable, and no FDM print is truly food-safe without coating.

The next time you stand in front of a wall of filament spools at your favorite retailer, you'll know exactly what each one offers -- and more importantly, what each one demands from you and your printer.

---

## Sources

1. Prusa Knowledge Base — PLA material guide (nozzle 215 °C first layer, 210 °C other layers; bed 60 °C; Tg ~60°C; no enclosure required): <https://help.prusa3d.com/article/pla_2062>

2. Polymaker Wiki — PLA printing parameters (nozzle 190–230°C, bed 40–60°C, 100% cooling): <https://wiki.polymaker.com/the-basics/3d-printing-materials/pla>

3. Wevolver — PLA vs PLA+: A Comprehensive Comparison (PLA+ unstandardized; eSUN 2% CaCO₃; Polymaker acrylic polymers; improved toughness): <https://www.wevolver.com/article/pla-vs-pla-plus>

4. Wikipedia — Polylactic acid (biodegradation requires ~58–60°C; no meaningful marine degradation after 428 days; industrial composting required): <https://en.wikipedia.org/wiki/Polylactic_acid>

5. Prusa Knowledge Base — PETG material guide (nozzle 230–240°C; bed 85–90°C; glass transition ~75–85°C; no bare glass bed): <https://help.prusa3d.com/article/petg_2059>

6. Overture 3D — PETG Print Settings Guide (nozzle 230–250°C; bed 80–90°C; dry at 65°C / 7 h; stringing troubleshooting): <https://overture3d.com/blogs/overture-blogs/petg-print-settings-guide>

7. Prusa Knowledge Base — Food safe FDM printing (layer lines "seedbed for bacteria"; brass nozzle wear; natural PETG; epoxy coating; cookie cutters disposable): <https://help.prusa3d.com/article/food-safe-fdm-printing_112313>

8. Prusa Knowledge Base — ABS material guide (nozzle 255 °C reference; bed 80–110°C; enclosure required; styrene fumes): <https://help.prusa3d.com/article/abs_2058>

9. Zbotic — 3D Print Acetone Smoothing: ABS Vapor Bath Guide (cold and hot vapor methods; process description): <https://zbotic.in/3d-print-acetone-smoothing-abs-vapor-bath-guide/>

10. PMC / Environmental Science & Technology — Emissions of Ultrafine Particles and VOCs from Desktop 3D Printers with Multiple Filaments (ABS emits 3–4× higher VOCs than PLA; styrene principal VOC): <https://pubs.acs.org/doi/10.1021/acs.est.5b04983>

11. IARC Monographs Vol. 121 — Evaluation of styrene (upgraded Group 2B → Group 2A "probably carcinogenic to humans," September 2019): <https://www.ncbi.nlm.nih.gov/books/n/iarcmono121/a006.sec6/>

12. NOAA CAMEO Chemicals — Acetone (flash point −20°C; flammable): <https://cameochemicals.noaa.gov/chemical/8>

13. Prusa Knowledge Base — ASA material guide (nozzle 260°C; bed 105–110°C; enclosure required; UV resistant; heat resistance up to 93°C): <https://help.prusa3d.com/article/asa_1809>

14. CNC Kitchen — Carbon Fiber Nylon in 3D Printing: PA6 vs PA12 Tested (PA6 up to 3% moisture "shot glass per spool"; PA12 ~0.5%; moisture changes strength/ductility): <https://www.cnckitchen.com/blog/carbon-fiber-nylon-in-3d-printing-pa6-vs-pa12-tested>

15. Prusa Knowledge Base — Polyamide (Nylon) material guide (nozzle 285°C; bed 110°C; dry below 90°C for at least 4 hours; enclosure recommended): <https://help.prusa3d.com/article/polyamide-nylon_167188>

16. Polymaker Wiki — PC material guide (nozzle 260–310°C; bed 90–120°C; Tg ~150°C; HDT >115°C; dry 70–80°C 6–8 h): <https://wiki.polymaker.com/the-basics/3d-printing-materials/pc>

17. Simplify3D — Ultimate Materials Guide: Polycarbonate (260–310°C; bed 80–120°C; HDT ~150°C; all-metal hotend; enclosed chamber; PTFE liner unsuitable): <https://www.simplify3d.com/resources/materials-guide/polycarbonate/>

18. Siraya Tech — TPU Shore Hardness Guide: 85A vs 95A (Shore hardness scale; direct drive requirement; print settings; 85A retraction off): <https://siraya.tech/blogs/news/tpu-shore-hardness>

19. Prusa Knowledge Base — Drying filament (TPU dry at 60°C; drying temps table; PLA max 45°C): <https://help.prusa3d.com/article/drying-filament_332086>

20. Prusa Knowledge Base — Composite Materials (carbon, Kevlar, glass fiber; hardened nozzle required; fibers abrasive; Kevlar less abrasive than CF; CF increases stiffness, reduces impact resistance): <https://help.prusa3d.com/article/composite-materials-filled-with-carbon-kevlar-or-glass_167387>

21. Simplify3D — Ultimate Materials Guide: Carbon Fiber Filled (PLA-CF 200–230°C; CF harder than brass; stiffness + brittleness tradeoff): <https://www.simplify3d.com/resources/materials-guide/carbon-fiber-filled/>

22. MDPI Polymers — Deformation Characterization of Glass Fiber and Carbon Fiber-Reinforced 3D Printing Filaments (GF reinforcement raises tensile strength and stiffness; impact resistance improvement): <https://www.mdpi.com/2073-4360/17/7/934>

23. 3D Mag — Comprehensive Guide to PVA Filament (nozzle 180–220°C; bed 45–60°C; >90% biodegradation in 56 days ISO 14851; pairs best with PLA): <https://www.3dmag.com/3d-wikipedia/pva-filament-water-soluble-support-material-3d-printing/>

24. Prusa Knowledge Base — Drying filament (PLA 45°C/6 h max; PETG 55°C/6 h; TPU 60°C/4–6 h; PVA 45°C/8 h; Nylon below 90°C): <https://help.prusa3d.com/article/drying-filament_332086>

25. Prusa Knowledge Base — HIPS material guide (nozzle 225–255°C; bed 100–110°C; d-Limonene solvent; NOT suitable for ABS/ASA supports as those also dissolve in limonene): <https://help.prusa3d.com/article/hips_167118>

26. SolidPrint3D — Bambu Lab Breakaway Support for PA/PET (breakaway support filaments; clean hand-removal; available for PLA and PA/PET): <https://www.solidprint3d.co.uk/shop/consumables/filament/breakaway-support-for-pa-pet/>

27. Prusa Forum — Humidity Control for Filament Storage Discussion (desiccant comparison; activated alumina vs silica gel; container sealing): <https://forum.prusa3d.com/forum/english-forum-general-discussion-announcements-and-releases/humidity-control-for-filament-storage-how-tight-does-a-container-have-to-be/>

28. Overture 3D — How to Dry 3D Printer Filament (PLA max 50°C / 7 h; "begins to deform at 64°C"; PETG 65°C/7 h; ABS 75°C/7 h; Nylon 95°C/7 h): <https://overture3d.com/blogs/overture-blogs/how-to-dry-3d-printer-filament>

29. Multiple sources — Brass nozzles and food safety (standard brass contains lead; worn particles enter filament; stainless steel nozzle recommended for food contact): <https://help.prusa3d.com/article/food-safe-fdm-printing_112313>

### Further reading

- Prusa Knowledge Base — full filament material guide index: <https://help.prusa3d.com/filament-material-guide>
- Polymaker Wiki — material overviews for all Polymaker filaments including PLA, PETG, PA, PC: <https://wiki.polymaker.com/the-basics/3d-printing-materials>
- All3DP — "The Best 3D Printer Filament: The Ultimate Guide" (broad overview of materials, brands, and use cases): <https://all3dp.com/1/3d-printer-filament-types-3d-printing-1-75mm-abs-pla-more/>
- CNC Kitchen (Stefan Hermann) — material testing videos and articles with real mechanical test data for PLA, PETG, Nylon, CF composites: <https://www.cnckitchen.com>
