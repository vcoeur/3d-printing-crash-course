/* Schematic diagram library for the animated course player.
   Each entry: kind -> function(lang) -> SVG string. Dark-theme palette, bilingual
   labels baked in. Kept deliberately simple + accurate (teaching schematics). */
(function () {
  const C = { line:"#3a4151", ink:"#e8eaf0", mut:"#9aa3b6", acc:"#ff7a2f",
              acc2:"#ffb066", pan:"#1b1f28", good:"#39d98a", warn:"#ffcf5c", bad:"#ff6b6b" };
  const T = (s) => `<text font-family="ui-sans-serif,system-ui,sans-serif" ${s}`;
  const wrap = (inner, vb = "0 0 680 360") =>
    `<svg viewBox="${vb}" width="680" role="img" xmlns="http://www.w3.org/2000/svg">${inner}</svg>`;
  const split2 = (s) => { const m = Math.ceil(s.length / 2); let i = s.lastIndexOf(" ", m);
    if (i < 0) i = s.indexOf(" ", m); if (i < 0) i = m; return [s.slice(0, i).trim(), s.slice(i).trim()]; };

  const D = {};

  // ---- CoreXY belt routing (the showcase) ----
  D.corexy = (lang) => {
    const fr = lang === "fr";
    const L = fr
      ? { t:"CoreXY — routage des courroies", mA:"Moteur A", mB:"Moteur B", head:"Tête",
          gantry:"Portique X", r1:"Les deux moteurs dans le même sens → axe X",
          r2:"Sens opposés → axe Y", eq:"ΔX = (A + B) / 2     ΔY = (A − B) / 2",
          note:"Moteurs fixes au châssis : masses mobiles légères → grande vitesse" }
      : { t:"CoreXY — belt routing", mA:"Motor A", mB:"Motor B", head:"Head",
          gantry:"X gantry", r1:"Both motors same way → X axis",
          r2:"Opposite ways → Y axis", eq:"ΔX = (A + B) / 2     ΔY = (A − B) / 2",
          note:"Motors fixed to the frame: light moving mass → high speed" };
    return wrap(`
      ${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      <!-- frame -->
      <rect x="40" y="48" width="360" height="270" rx="6" fill="none" stroke="${C.line}" stroke-width="2"/>
      <!-- corner idlers -->
      ${[[40,48],[400,48],[40,318],[400,318]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="9" fill="${C.pan}" stroke="${C.mut}" stroke-width="2"/>`).join("")}
      <!-- motors at rear corners -->
      <rect x="22" y="30" width="36" height="36" rx="5" fill="${C.pan}" stroke="${C.acc}" stroke-width="2"/>
      ${T(`x="40" y="53" fill="${C.acc}" font-weight="700" font-size="13" text-anchor="middle">A</text>`)}
      <rect x="382" y="30" width="36" height="36" rx="5" fill="${C.pan}" stroke="${C.acc2}" stroke-width="2"/>
      ${T(`x="400" y="53" fill="${C.acc2}" font-weight="700" font-size="13" text-anchor="middle">B</text>`)}
      ${T(`x="22" y="84" fill="${C.mut}" font-size="11">${L.mA}</text>`)}
      ${T(`x="378" y="84" fill="${C.mut}" font-size="11" >${L.mB}</text>`)}
      <!-- X gantry (moves in Y along the side rails) -->
      <rect x="40" y="170" width="360" height="16" fill="${C.pan}" stroke="${C.line}" stroke-width="1.5"/>
      ${T(`x="44" y="165" fill="${C.mut}" font-size="11">${L.gantry}</text>`)}
      <!-- carriage / head on the gantry -->
      <rect x="196" y="160" width="48" height="36" rx="5" fill="${C.ink}" opacity="0.92"/>
      ${T(`x="220" y="182" fill="#10131a" font-weight="700" font-size="11" text-anchor="middle">${L.head}</text>`)}
      <!-- belt A (orange): motor A around top-left + top-right idlers to carriage -->
      <path d="M40,48 L400,48 L220,178 L40,318 L40,48" fill="none" stroke="${C.acc}" stroke-width="2.4"/>
      <!-- belt B (amber): mirror routing to carriage -->
      <path d="M400,48 L400,318 L220,178 L40,318" fill="none" stroke="${C.acc2}" stroke-width="2.4" stroke-dasharray="2 0" opacity="0.95"/>
      <!-- axes key -->
      <g transform="translate(330,250)">
        <line x1="0" y1="40" x2="0" y2="0" stroke="${C.good}" stroke-width="2" marker-end="url(#ah)"/>
        <line x1="0" y1="40" x2="40" y2="40" stroke="${C.good}" stroke-width="2" marker-end="url(#ah)"/>
        ${T(`x="6" y="10" fill="${C.good}" font-size="11">Y</text>`)}
        ${T(`x="44" y="44" fill="${C.good}" font-size="11">X</text>`)}
      </g>
      <defs><marker id="ah" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 z" fill="${C.good}"/></marker></defs>
      <!-- explanation panel -->
      <g transform="translate(430,60)">
        <rect x="0" y="0" width="232" height="250" rx="8" fill="${C.pan}" stroke="${C.line}"/>
        <circle cx="20" cy="34" r="7" fill="${C.acc}"/><circle cx="36" cy="34" r="7" fill="${C.acc2}"/>
        ${T(`x="52" y="38" fill="${C.ink}" font-size="12">${L.r1}</text>`)}
        <circle cx="20" cy="74" r="7" fill="${C.acc}"/><circle cx="36" cy="74" r="7" fill="${C.acc2}" stroke="${C.bad}" stroke-width="2"/>
        ${T(`x="52" y="78" fill="${C.ink}" font-size="12">${L.r2}</text>`)}
        <rect x="16" y="104" width="200" height="34" rx="6" fill="#10131a"/>
        ${T(`x="116" y="126" fill="${C.acc2}" font-family="ui-monospace,monospace" font-size="12.5" text-anchor="middle">${L.eq}</text>`)}
        ${T(`x="16" y="170" fill="${C.mut}" font-size="11.5"><tspan x="16" dy="0">${split2(L.note)[0]}</tspan><tspan x="16" dy="16">${split2(L.note)[1]}</tspan></text>`)}
      </g>`);
  };

  // ---- Cartesian bed-slinger (contrast to CoreXY) ----
  D.bedslinger = (lang) => {
    const fr = lang === "fr";
    const L = fr
      ? { t:"Cartésienne « bed-slinger »", x:"Tête : axe X", z:"Portique : axe Z",
          y:"Plateau : axe Y (avant/arrière)", note:"Le plateau lourd accélère/décélère → vitesse limitée, risque de fantômes" }
      : { t:"Cartesian bed-slinger", x:"Head: X axis", z:"Gantry: Z axis",
          y:"Bed: Y axis (front/back)", note:"Heavy bed accelerates back and forth → speed limited, ghosting risk" };
    return wrap(`
      ${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      <!-- Z uprights -->
      <rect x="70" y="60" width="14" height="240" fill="${C.pan}" stroke="${C.line}"/>
      <rect x="430" y="60" width="14" height="240" fill="${C.pan}" stroke="${C.line}"/>
      <!-- X gantry beam -->
      <rect x="70" y="96" width="374" height="16" fill="${C.pan}" stroke="${C.acc}" stroke-width="1.5"/>
      <!-- head on gantry -->
      <rect x="230" y="86" width="54" height="34" rx="5" fill="${C.ink}"/>
      <line x1="257" y1="120" x2="257" y2="150" stroke="${C.acc}" stroke-width="3"/>
      <!-- bed -->
      <rect x="150" y="220" width="214" height="14" fill="${C.acc}" opacity="0.85"/>
      <line x1="150" y1="252" x2="364" y2="252" stroke="${C.mut}" stroke-dasharray="4 4"/>
      <path d="M120,252 L150,252" stroke="${C.good}" stroke-width="2" marker-end="url(#bh)"/>
      <path d="M394,252 L364,252" stroke="${C.good}" stroke-width="2" marker-end="url(#bh)"/>
      <defs><marker id="bh" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 z" fill="${C.good}"/></marker></defs>
      <!-- labels -->
      ${T(`x="290" y="80" fill="${C.ink}" font-size="12">${L.x}</text>`)}
      ${T(`x="455" y="180" fill="${C.ink}" font-size="12">${L.z}</text>`)}
      ${T(`x="150" y="278" fill="${C.acc2}" font-size="12">${L.y}</text>`)}
      ${T(`x="20" y="330" fill="${C.mut}" font-size="12">${L.note}</text>`)}`);
  };

  // ---- Hotend cross-section ----
  D.hotend = (lang) => {
    const fr = lang === "fr";
    const L = fr
      ? { t:"Anatomie de la tête chauffante", fil:"Filament (1,75 mm)", cold:"Partie froide + dissipateur",
          fan:"Ventilateur", brk:"Barrière thermique", blk:"Bloc chauffant", noz:"Buse 0,4 mm",
          melt:"Zone de fusion", creep:"La partie froide doit rester froide, sinon : remontée de chaleur" }
      : { t:"Hotend anatomy", fil:"Filament (1.75 mm)", cold:"Cold end + heatsink",
          fan:"Fan", brk:"Heat break", blk:"Heater block", noz:"0.4 mm nozzle",
          melt:"Melt zone", creep:"Keep the cold end cold — otherwise: heat creep" };
    return wrap(`
      ${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      <!-- filament -->
      <rect x="250" y="44" width="16" height="70" fill="${C.acc2}"/>
      ${T(`x="276" y="60" fill="${C.mut}" font-size="11">${L.fil}</text>`)}
      <!-- cold end heatsink (fins) -->
      ${[0,1,2,3,4].map(i=>`<rect x="206" y="${64+i*10}" width="104" height="5" fill="#16202b" stroke="${C.line}"/>`).join("")}
      ${T(`x="320" y="92" fill="#7fd0ff" font-size="11">${L.cold}</text>`)}
      <!-- fan -->
      <circle cx="170" cy="86" r="22" fill="${C.pan}" stroke="${C.line}"/><circle cx="170" cy="86" r="5" fill="${C.mut}"/>
      ${T(`x="148" y="128" fill="${C.mut}" font-size="11">${L.fan}</text>`)}
      <!-- heat break (narrow) -->
      <rect x="246" y="120" width="24" height="34" fill="${C.pan}" stroke="${C.mut}" stroke-width="2"/>
      ${T(`x="320" y="140" fill="${C.mut}" font-size="11">${L.brk}</text>`)}
      <!-- heater block (hot) -->
      <rect x="226" y="154" width="64" height="46" rx="4" fill="#3a1d12" stroke="${C.acc}" stroke-width="2"/>
      ${T(`x="320" y="180" fill="${C.acc}" font-size="11">${L.blk}</text>`)}
      <!-- melt zone label -->
      ${T(`x="150" y="180" fill="${C.warn}" font-size="11">${L.melt}</text>`)}
      <!-- nozzle (triangle) -->
      <path d="M236,200 L280,200 L262,238 L254,238 Z" fill="${C.acc}"/>
      <rect x="255" y="238" width="6" height="10" fill="${C.acc}"/>
      ${T(`x="300" y="226" fill="${C.acc}" font-size="11">${L.noz}</text>`)}
      <!-- deposited bead -->
      <rect x="190" y="250" width="200" height="10" rx="5" fill="${C.acc2}" opacity="0.8"/>
      <!-- heat gradient bar -->
      <rect x="470" y="60" width="18" height="180" rx="4" fill="url(#hg)"/>
      <defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16202b"/><stop offset="1" stop-color="${C.acc}"/></linearGradient></defs>
      ${T(`x="494" y="70" fill="#7fd0ff" font-size="11">cold</text>`)}
      ${T(`x="494" y="236" fill="${C.acc}" font-size="11">~210°C</text>`)}
      ${T(`x="20" y="330" fill="${C.mut}" font-size="12">${L.creep}</text>`)}`);
  };

  // ---- FDM layer-by-layer deposition ----
  D.fdm_layers = (lang) => {
    const fr = lang === "fr";
    const L = fr ? { t:"Dépôt couche par couche", h:"hauteur de couche (0,1–0,3 mm)", plate:"Plateau chauffant", noz:"Buse" }
                 : { t:"Layer-by-layer deposition", h:"layer height (0.1–0.3 mm)", plate:"Heated bed", noz:"Nozzle" };
    let beads = "";
    for (let r = 0; r < 6; r++) for (let c = 0; c < 12; c++)
      beads += `<rect x="${120 + c*32}" y="${250 - r*18}" width="30" height="16" rx="7" fill="${C.acc2}" opacity="${0.55 + r*0.07}"/>`;
    return wrap(`
      ${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      ${beads}
      <!-- current bead being laid -->
      <rect x="120" y="142" width="200" height="16" rx="7" fill="${C.acc}"/>
      <!-- nozzle above -->
      <path d="M300,96 L340,96 L324,138 L316,138 Z" fill="${C.ink}"/>
      <rect x="317" y="138" width="6" height="8" fill="${C.acc}"/>
      ${T(`x="346" y="120" fill="${C.ink}" font-size="11">${L.noz}</text>`)}
      <line x1="80" y1="232" x2="80" y2="160" stroke="${C.mut}" stroke-width="1.5" marker-start="url(#dh)" marker-end="url(#dh)"/>
      ${T(`x="86" y="200" fill="${C.mut}" font-size="11">${L.h}</text>`)}
      <defs><marker id="dh" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto"><path d="M0,3.5 L7,0 L7,7 z" fill="${C.mut}"/></marker></defs>
      <!-- bed -->
      <rect x="100" y="268" width="408" height="14" fill="${C.acc}" opacity="0.5"/>
      ${T(`x="100" y="300" fill="${C.mut}" font-size="12">${L.plate}</text>`)}`);
  };

  // ---- Direct drive vs Bowden ----
  D.extruder = (lang) => {
    const fr = lang === "fr";
    const L = fr
      ? { t:"Entraînement direct ou Bowden", dd:"Direct", bo:"Bowden",
          dd1:"Extrudeur sur la tête", dd2:"Rétraction courte, gère le flexible",
          bo1:"Extrudeur sur le châssis + tube PTFE", bo2:"Tête légère, rétraction longue" }
      : { t:"Direct drive vs Bowden", dd:"Direct", bo:"Bowden",
          dd1:"Extruder on the toolhead", dd2:"Short retraction, handles flexibles",
          bo1:"Extruder on frame + PTFE tube", bo2:"Lighter head, long retraction" };
    return wrap(`
      ${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      <!-- DIRECT -->
      ${T(`x="40" y="58" fill="${C.acc2}" font-weight="700" font-size="13">${L.dd}</text>`)}
      <rect x="40" y="70" width="58" height="44" rx="5" fill="${C.pan}" stroke="${C.acc}" stroke-width="2"/>
      ${T(`x="69" y="96" fill="${C.acc}" font-size="11" text-anchor="middle">⚙</text>`)}
      <rect x="56" y="114" width="26" height="40" fill="${C.pan}" stroke="${C.line}"/>
      <path d="M59,154 L79,154 L71,176 L67,176 Z" fill="${C.acc}"/>
      ${T(`x="110" y="92" fill="${C.ink}" font-size="11.5">${L.dd1}</text>`)}
      ${T(`x="110" y="112" fill="${C.mut}" font-size="11">${L.dd2}</text>`)}
      <!-- BOWDEN -->
      ${T(`x="40" y="216" fill="${C.acc2}" font-weight="700" font-size="13">${L.bo}</text>`)}
      <rect x="40" y="228" width="58" height="40" rx="5" fill="${C.pan}" stroke="${C.acc}" stroke-width="2"/>
      ${T(`x="69" y="252" fill="${C.acc}" font-size="11" text-anchor="middle">⚙</text>`)}
      <path d="M98,248 C200,248 240,300 300,300" fill="none" stroke="${C.mut}" stroke-width="3"/>
      <rect x="300" y="282" width="26" height="36" fill="${C.pan}" stroke="${C.line}"/>
      <path d="M303,318 L323,318 L315,336 L311,336 Z" fill="${C.acc}"/>
      ${T(`x="120" y="244" fill="${C.ink}" font-size="11.5">${L.bo1}</text>`)}
      ${T(`x="340" y="304" fill="${C.mut}" font-size="11">${L.bo2}</text>`)}`);
  };

  // ---- AMS multi-material filament path ----
  D.ams = (lang) => {
    const fr = lang === "fr";
    const L = fr ? { t:"Trajet du filament AMS", spools:"4 bobines", hub:"Sélecteur + tampon", tool:"Tête",
                     note:"Une seule voie vers la tête : un filament à la fois, purge entre couleurs" }
                 : { t:"AMS filament path", spools:"4 spools", hub:"Selector + buffer", tool:"Toolhead",
                     note:"One path to the head: one filament at a time, purge between colors" };
    const cols = [C.acc, C.good, "#7fb0ff", C.warn];
    return wrap(`
      ${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      ${cols.map((c,i)=>`<circle cx="80" cy="${70+i*62}" r="24" fill="none" stroke="${c}" stroke-width="6"/><circle cx="80" cy="${70+i*62}" r="6" fill="${c}"/>
        <path d="M104,${70+i*62} C170,${70+i*62} 200,178 270,178" fill="none" stroke="${c}" stroke-width="3" opacity="0.8"/>`).join("")}
      ${T(`x="56" y="40" fill="${C.mut}" font-size="11">${L.spools}</text>`)}
      <!-- hub -->
      <rect x="270" y="150" width="90" height="56" rx="6" fill="${C.pan}" stroke="${C.acc}" stroke-width="2"/>
      ${T(`x="315" y="182" fill="${C.ink}" font-size="11" text-anchor="middle">${L.hub}</text>`)}
      <!-- single path to toolhead -->
      <path d="M360,178 C440,178 470,150 540,150" fill="none" stroke="${C.acc}" stroke-width="4"/>
      <rect x="540" y="130" width="56" height="44" rx="6" fill="${C.ink}"/>
      ${T(`x="568" y="156" fill="#10131a" font-weight="700" font-size="11" text-anchor="middle">${L.tool}</text>`)}
      ${T(`x="20" y="320" fill="${C.mut}" font-size="12">${L.note}</text>`)}`);
  };

  // ---- First layer / Z-offset ----
  D.first_layer = (lang) => {
    const fr = lang === "fr";
    const L = fr ? { t:"Première couche — réglage du Z", hi:"Trop haut", ok:"Correct", lo:"Trop bas",
                     hiN:"cordons ronds, n'adhèrent pas", okN:"légèrement écrasé, soudé", loN:"transparent, raclé, bouché" }
                 : { t:"First layer — Z-offset", hi:"Too high", ok:"Just right", lo:"Too low",
                     hiN:"round beads, won't stick", okN:"slightly squished, bonded", loN:"see-through, scraped, clogs" };
    const cell = (x, label, note, color, draw) => `
      <g transform="translate(${x},60)">
        ${T(`x="80" y="0" fill="${color}" font-weight="700" font-size="13" text-anchor="middle">${label}</text>`)}
        <!-- nozzle -->
        <path d="M64,18 L96,18 L84,46 L76,46 Z" fill="${C.ink}"/>
        ${draw}
        <rect x="10" y="118" width="140" height="10" fill="${C.acc}" opacity="0.5"/>
        ${T(`x="80" y="150" fill="${C.mut}" font-size="10.5" text-anchor="middle"><tspan x="80">${note.split(",")[0]}</tspan><tspan x="80" dy="14">${note.split(",").slice(1).join(",")}</tspan></text>`)}
      </g>`;
    return wrap(`
      ${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      ${cell(40, L.hi, L.hiN, C.warn, `${[0,1,2,3].map(i=>`<circle cx="${20+i*35}" cy="100" r="9" fill="${C.acc2}"/>`).join("")}`)}
      ${cell(250, L.ok, L.okN, C.good, `${[0,1,2,3].map(i=>`<rect x="${12+i*35}" y="100" width="34" height="14" rx="6" fill="${C.acc2}"/>`).join("")}`)}
      ${cell(460, L.lo, L.loN, C.bad, `${[0,1,2,3].map(i=>`<rect x="${12+i*35}" y="106" width="34" height="6" rx="2" fill="${C.acc2}" opacity="0.5"/>`).join("")}`)}`);
  };

  // ---- Overhang / 45-degree rule ----
  D.overhang = (lang) => {
    const fr = lang === "fr";
    const L = fr ? { t:"Surplombs et règle des 45°", ok:"≤ 45° : imprimable", bad:"> 45° : supports",
                     note:"Chaque couche doit reposer en partie sur la précédente" }
                 : { t:"Overhangs and the 45° rule", ok:"≤ 45°: printable", bad:"> 45°: needs support",
                     note:"Each layer must rest partly on the one below" };
    return wrap(`
      ${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      <!-- good 45 -->
      <g transform="translate(70,70)">
        <polygon points="0,180 0,0 120,180" fill="${C.pan}" stroke="${C.good}" stroke-width="2"/>
        <line x1="0" y1="180" x2="60" y2="180" stroke="${C.mut}"/>
        <path d="M0,150 A30,30 0 0 0 22,170" fill="none" stroke="${C.good}"/>
        ${T(`x="26" y="168" fill="${C.good}" font-size="11">45°</text>`)}
        ${T(`x="0" y="206" fill="${C.good}" font-size="12">${L.ok}</text>`)}
      </g>
      <!-- bad steep -->
      <g transform="translate(380,70)">
        <polygon points="0,180 0,0 150,10 150,40 40,30 40,180" fill="${C.pan}" stroke="${C.bad}" stroke-width="2"/>
        ${[60,80,100,120,140].map(x=>`<line x1="${x}" y1="40" x2="${x}" y2="${40+(x-40)*0.0+(x>40? (x-40):0)}" stroke="${C.bad}" stroke-dasharray="3 3"/>`).join("")}
        ${[60,80,100,120,140].map(x=>`<line x1="${x}" y1="30" x2="${x}" y2="180" stroke="${C.bad}" stroke-width="1" stroke-dasharray="3 4" opacity="0.6"/>`).join("")}
        ${T(`x="0" y="206" fill="${C.bad}" font-size="12">${L.bad}</text>`)}
      </g>
      ${T(`x="20" y="320" fill="${C.mut}" font-size="12">${L.note}</text>`)}`);
  };

  // ---- Infill patterns ----
  D.infill = (lang) => {
    const fr = lang === "fr";
    const names = fr ? ["Grille","Gyroïde","Nid d'abeille","Cubique"] : ["Grid","Gyroid","Honeycomb","Cubic"];
    const t = fr ? "Motifs de remplissage" : "Infill patterns";
    const box = (x, name, draw) => `<g transform="translate(${x},64)">
      <rect x="0" y="0" width="130" height="130" rx="6" fill="${C.pan}" stroke="${C.line}"/>${draw}
      ${T(`x="65" y="156" fill="${C.ink}" font-size="12" text-anchor="middle">${name}</text>`)}</g>`;
    const grid = [0,1,2,3,4].map(i=>`<line x1="${i*32+2}" y1="2" x2="${i*32+2}" y2="128" stroke="${C.acc}" stroke-width="1.5"/><line x1="2" y1="${i*32+2}" x2="128" y2="${i*32+2}" stroke="${C.acc}" stroke-width="1.5"/>`).join("");
    const gyroid = [0,1,2,3].map(i=>`<path d="M2,${16+i*32} q32,-22 64,0 t64,0" fill="none" stroke="${C.acc}" stroke-width="1.8"/>`).join("");
    const honey = [0,1,2,3,4,5,6,7].map(i=>{const cx=20+(i%4)*30+(Math.floor(i/4)%2?15:0);const cy=22+Math.floor(i/4)*40;return `<polygon points="${cx},${cy-13} ${cx+12},${cy-6} ${cx+12},${cy+6} ${cx},${cy+13} ${cx-12},${cy+6} ${cx-12},${cy-6}" fill="none" stroke="${C.acc}" stroke-width="1.5"/>`;}).join("");
    const cubic = [0,1,2].map(i=>`<rect x="${10+i*34}" y="${10+i*8}" width="60" height="60" fill="none" stroke="${C.acc}" stroke-width="1.5" transform="rotate(12 65 65)"/>`).join("");
    return wrap(`${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${t}</text>`)}
      ${box(40,names[0],grid)}${box(200,names[1],gyroid)}${box(360,names[2],honey)}${box(520,names[3],cubic)}`);
  };

  // ---- Bed adhesion: skirt / brim / raft ----
  D.adhesion = (lang) => {
    const fr = lang === "fr";
    const L = fr ? { t:"Adhérence : jupe, bordure, radeau", sk:"Jupe", br:"Bordure", ra:"Radeau",
                     skN:"ligne séparée — amorce le flux", brN:"collée à la pièce — anti-décollement", raN:"socle complet sous la pièce" }
                 : { t:"Adhesion: skirt, brim, raft", sk:"Skirt", br:"Brim", ra:"Raft",
                     skN:"separate line — primes flow", brN:"attached — fights warping", raN:"full base under the part" };
    const cell=(x,label,note,draw)=>`<g transform="translate(${x},64)">
      ${T(`x="80" y="0" fill="${C.acc2}" font-weight="700" font-size="13" text-anchor="middle">${label}</text>`)}
      ${draw}
      ${T(`x="80" y="150" fill="${C.mut}" font-size="10.5" text-anchor="middle"><tspan x="80">${note.split("—")[0]}</tspan><tspan x="80" dy="14">${note.split("—")[1]||""}</tspan></text>`)}</g>`;
    const part=`<rect x="55" y="60" width="50" height="50" rx="3" fill="${C.ink}"/>`;
    return wrap(`${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      ${cell(40,L.sk,L.skN,`${part}<rect x="30" y="35" width="100" height="100" rx="6" fill="none" stroke="${C.acc}" stroke-dasharray="5 5"/>`)}
      ${cell(250,L.br,L.brN,`<rect x="38" y="43" width="84" height="84" rx="5" fill="${C.acc}" opacity="0.35"/>${part}`)}
      ${cell(460,L.ra,L.raN,`<rect x="34" y="52" width="92" height="74" rx="5" fill="${C.acc}" opacity="0.5"/>${part}`)}`);
  };

  // ---- Retraction / stringing ----
  D.retraction = (lang) => {
    const fr = lang === "fr";
    const L = fr ? { t:"Rétraction contre les fils (stringing)", no:"Sans rétraction", yes:"Avec rétraction",
                     noN:"le filament suinte → fils", yesN:"le filament est tiré → propre" }
                 : { t:"Retraction vs stringing", no:"No retraction", yes:"With retraction",
                     noN:"filament oozes → strings", yesN:"filament pulled back → clean" };
    const towers=(c,strings)=>`<rect x="20" y="40" width="26" height="100" fill="${C.pan}" stroke="${C.line}"/><rect x="120" y="40" width="26" height="100" fill="${C.pan}" stroke="${C.line}"/>${strings?[55,75,95].map(y=>`<path d="M46,${y} q40,12 74,0" fill="none" stroke="${C.bad}" stroke-width="1.4"/>`).join(""):`<line x1="46" y1="60" x2="120" y2="60" stroke="${c}" stroke-dasharray="2 6" opacity="0.5"/>`}`;
    return wrap(`${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      <g transform="translate(60,70)">${towers(C.bad,true)}${T(`x="83" y="172" fill="${C.bad}" font-weight="700" font-size="13" text-anchor="middle">${L.no}</text>`)}${T(`x="83" y="192" fill="${C.mut}" font-size="11" text-anchor="middle">${L.noN}</text>`)}</g>
      <g transform="translate(380,70)">${towers(C.good,false)}${T(`x="83" y="172" fill="${C.good}" font-weight="700" font-size="13" text-anchor="middle">${L.yes}</text>`)}${T(`x="83" y="192" fill="${C.mut}" font-size="11" text-anchor="middle">${L.yesN}</text>`)}</g>`);
  };

  // ---- Layer adhesion / Z-axis anisotropy ----
  D.anisotropy = (lang) => {
    const fr = lang === "fr";
    const L = fr ? { t:"Anisotropie : faiblesse en Z", strong:"Fort dans le plan XY", weak:"Faible entre couches (Z)",
                     note:"Orientez les pièces pour que les efforts suivent les couches, pas à travers" }
                 : { t:"Anisotropy: the weak Z axis", strong:"Strong across the XY plane", weak:"Weak between layers (Z)",
                     note:"Orient parts so loads run along layers, not across them" };
    return wrap(`${T(`x="20" y="26" fill="${C.acc}" font-weight="700" font-size="16">${L.t}</text>`)}
      <g transform="translate(80,70)">
        ${[0,1,2,3,4,5,6].map(i=>`<rect x="0" y="${i*22}" width="160" height="18" rx="3" fill="${C.acc2}" opacity="${0.6+i*0.05}"/>`).join("")}
        ${[1,2,3,4,5,6].map(i=>`<line x1="0" y1="${i*22-2}" x2="160" y2="${i*22-2}" stroke="#10131a" stroke-width="2"/>`).join("")}
        <line x1="200" y1="0" x2="200" y2="160" stroke="${C.bad}" stroke-width="3" marker-start="url(#zh)" marker-end="url(#zh)"/>
        ${T(`x="210" y="86" fill="${C.bad}" font-size="12">${L.weak}</text>`)}
        <line x1="0" y1="190" x2="160" y2="190" stroke="${C.good}" stroke-width="3" marker-start="url(#zh)" marker-end="url(#zh)"/>
        ${T(`x="0" y="214" fill="${C.good}" font-size="12">${L.strong}</text>`)}
      </g>
      <defs><marker id="zh" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,4 L8,1 L8,7 z" fill="${C.bad}"/></marker></defs>
      ${T(`x="20" y="330" fill="${C.mut}" font-size="12">${L.note}</text>`)}`);
  };

  window.DIAGRAMS = D;
})();
