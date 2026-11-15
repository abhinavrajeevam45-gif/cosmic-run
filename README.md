# 🚀 COSMIC RUN – Beyond the Universe
### Premium 3D Space Runner | Hackathon Edition

A professional-grade, single-file **Three.js 3D space runner game** built for hackathon presentation. Navigate a spaceship through stunning procedurally generated cosmic environments, dodge obstacles, collect coins, unlock ships, complete missions, and master 10 progressive galactic sectors.

---

## 🎮 Gameplay Overview

- **Genre:** 3D Endless Space Runner
- **Engine:** Three.js (WebGL) via ES Module importmap
- **Architecture:** Single-file HTML — all CSS, HTML, and JS inline (~219KB)
- **Framework:** Vite 6 (dev + production build)
- **Controls:** Keyboard (WASD/Arrows) + Swipe gestures + On-screen touch buttons

---

## 🪐 NASA Space Exploration Mission System (v4.0)

COSMIC RUN 3D has been upgraded with a NASA-inspired educational space exploration framework:

### 1. Live Mission Distance Engine
- **Live Kilometer Telemetry**: Features real-time simulated astronomical kilometers (`#hudMissionKmVal`) alongside track distance meters (`#hudDistanceVal`).
- **Separation of Metrics**: Game score (points), actual track meters (obstacle dodging distance), and simulated mission kilometers (interplanetary navigation) are strictly separated.
- **Continuous Astronomical Scaling**:
  - 🌍 **Earth Departure / LEO**: 0 m track → 0 km (reference launch)
  - 🌕 **The Moon (Luna)**: 750 m track → 384,400 km mean orbital distance
  - 🟡 **Venus Encounter**: 1,800 m track → ~42,000,000 km closest approach
  - 🔴 **Mars Exploration**: 3,000 m track → ~54,600,000 km closest approach
  - 🪐 **Jupiter Jovian Realm**: 5,500 m track → ~588,500,000 km closest approach
  - ✨ **Saturn Rings Frontier**: 8,000 m track → ~1,200,000,000 km reference
  - 🔷 **Uranus Ice Giant**: 11,000 m track → ~2,600,000,000 km reference
  - 🔵 **Neptune Deep Explorer**: 14,000 m track → ~4,300,000,000 km reference
  - ⭐ **Interstellar Heliopause**: 18,000 m track → ~18,000,000,000 km Voyager boundary

### 2. Visual Solar System Progression Bar
- **HUD System Strip**: Pinned along the flight view (`#hudSolarSystemStrip`), displaying current planetary body, next destination, kilometers remaining, and total system traversed (0–100%).
- **Interactive Celestial Nodes**: 9 planet/boundary nodes (`🌍 🌕 🟡 🔴 🪐 ✨ 🔷 🔵 ⭐`) dynamically light up to `.reached` status as milestones are crossed. Tapping any node displays an on-screen educational science toast with JPL orbital dynamics telemetry.
- **Moving Spacecraft Pin**: Spacecraft glyph (`#hudSolarShipIndicator`) slides in real-time across the solar system progression track.

### 3. Cinematic Planetary Milestone Animation
- **Pop-Up Orbital Banner**: Triggered immediately upon crossing planetary thresholds (`#nasaMilestoneBanner`).
- **Visuals & Dossier**: Glowing golden border, planetary insignia, exact approximate reference distance, and educational science dossier.
- **Rewards**: Grants bonus flight points (+500 × combo) and +350 Pilot XP with custom audio fanfare.

### 4. NASA Mission Control Flight Telemetry Dashboard
- Accessible via the **MISSION CONTROL** button in the main hangar (or press `[M]`).
- Displays lifetime simulated km, total meters, best flight records, solar system completion percentage, and planets explored count.
- **Planetary Milestones Catalog Grid**: 9 high-tech telemetry cards detailing target reference distances, exploration status, and JPL planetary notes. Clicking any card deep-links directly into the NASA Space Encyclopedia.

### 5. Final Mission Summary Report (Game Over)
- Professional space-agency debrief archive screen (`#gameOverModal`).
- Telemetry readouts for total mission kilometers, track distance, points, closest milestone achieved, next target & distance remaining, and system completion percentage.
- **Interactive Milestone Status Pills**: Displays all 9 celestial exploration targets with achieved vs locked states.

### 6. Scientific Accuracy & Educational Disclaimers
- All astronomical distances are explicitly labeled as approximate astronomical reference distances derived from NASA/JPL Planetary Fact Sheets.
- Prominently labeled as an interactive educational simulation game.

---

## ✨ Premium Features

### 🌌 3D Space Environments
- **10 Progressive Sectors**: Earth Orbit → Moon → Mars → Asteroid Belt → Jupiter → Saturn → Uranus → Neptune → Nebula → Deep Space Heliopause
- **Procedural Planet Textures**: Each level renders a unique celestial body with custom shaders, atmospheric glow, and dynamic lighting
- **Earth Level**: Procedural continent/ocean canvas texture + cloud sphere + ISS space station with solar panels + Rayleigh atmospheric halo
- **Space Dust Particles**: 180-particle streak system for hyperspeed sensation
- **Hyperspace Warp Gates**: Animated torus portals trigger sector transitions mid-run

### 🛸 Spaceship Fleet (5 Ships)
| Ship | Description | Special |
|------|-------------|---------|
| **Orion X-1** | Classic interceptor | Balanced stats |
| **Valkyrie** | Forward-swept delta wing | +Speed bonus |
| **Aurora** | Faceted lifting body | +Agility |
| **Titan** | Twin-hull catamaran | +Shield pips |
| **Quantum** | Needle + torus rings | +Coin magnet |

- **Dual-layer engine flames**: Outer envelope + white hot core with dynamic scaling on boost
- **Aerodynamic banking**: Realistic tilt on lane changes
- **Pitch animation**: Nose-up on jump, nose-down on dive
- **Hangar drag rotation**: Mouse drag to inspect ships in 3D

### 🎮 Controls
| Key | In-Flight Action | Hangar / Menu Action |
|-----|------------------|----------------------|
| `A` / `←` | Bank Left | Previous Ship |
| `D` / `→` | Bank Right | Next Ship |
| `W` / `↑` | Jump Climb | — |
| `S` / `↓` | Dive Subsonic | — |
| `Space` | Nitro Boost | Launch Expedition |
| `Enter` | — | Quick Launch / Play Again |
| `P` / `Escape` | Tactical Pause | Close Active Modal |
| `R` | — | Quick Restart Flight |
| `M` | — | NASA Mission Control Dashboard |
| `E` | — | NASA Space Encyclopedia |
| `H` | — | Fleet Aerospace Hangar |
| `L` | — | Global Ace Leaderboard |
| `U` | — | Quantum Systems & Upgrades |
| `B` | — | Claim Daily Research Bonus |
| Swipe / Tap | Full Mobile Touch HUD | Button Tap Navigation |

### ⚡ Game Systems

#### Combat & Obstacles
- **3 Obstacle Types**: Rotating asteroids, spinning debris, laser barriers (high/low variants)
- **Energy Gates**: Pass-through for bonus score
- **Collision System**: AABB with per-type hitboxes; shield system absorbs hits

#### Power-Ups (4 Types)
- 🚀 **Nitro Boost** — 2.4× speed + shield immunity + music mode switch
- 🛡️ **Kinetic Shield** — absorbs one collision
- 🧲 **Coin Magnet** — auto-collects nearby coins
- ✨ **Score Doubler** — 2× all scoring

#### Near-Miss & Combo System
- **Near-Miss Detection**: Side-pass within 1.4–2.6 units triggers stunt
- **Combo Multiplier**: 1× → 5× — builds on consecutive near-misses, resets on hit
- **Dynamic Toast**: Shows `⚡ NEAR MISS! +N PTS` with current combo scaling

#### Level Progression
- **Warp Portal System**: Hyperspace gate spawns at distance milestone → passing unlocks next sector
- **Sector Progress Bar**: HUD displays % progress to next warp gate
- **Camera FOV scaling**: Dynamic field-of-view expansion at high speed

### 📊 Progression & Rewards

#### XP & Pilot Ranks (10 Tiers)
Flight Cadet → Solar Ensign → Stellar Pilot → … → Supreme Celestial Legend

XP formula: `runDistance × 0.45 + runCoins × 3 + nearMisses × 25`

#### Missions System
- Random mission per run (distance or coin target)
- Mission tracker visible on HUD during flight
- Reward: +100 Coins & +200 XP on completion

#### 12 Achievements
| Achievement | Condition |
|------------|-----------|
| First Flight | Complete first run |
| Distance Runner | Fly 1,000 M in one run |
| Coin Hoarder | Collect 150 coins in one run |
| Shield Bearer | Absorb hit with active shield |
| Sector Jumper | Complete a hyperspace warp jump |
| Combo Master | Reach 4× combo in one run |
| Near-Miss Artist | 5 near-misses in one run |
| Multi-Sector | Visit 3 sectors in one run |
| Speed Racer | Complete boost level |
| Ship Collector | Unlock 2 ships |
| Veteran Pilot | Fly 10 total expeditions |
| Planet Scanner | Discover 5 planetary bodies |

#### Leaderboard
- 9 simulated global pilots + player row (live-merged and sorted by score)
- Player callsign customizable in real-time

#### Career Dashboard
- Lifetime Distance, Total Coins, Expeditions, Near-Misses, Warp Jumps, Max Combo

#### Daily Research Bonus
- Streak-based daily reward (coins + XP) with 24-hour cooldown

### 🎵 Audio System

#### Sound Engine (Web Audio API — no external files)
- `playCoin()` — harmonic coin pickup with combo pitch scaling
- `playNearMiss()` — adrenaline sweep effect
- `playLaneSwitch()` — subtle directional click
- `playJump()` — ascending sweep
- `playDive()` — descending plunge
- `playPowerup()` — power chord activation
- `playWarpJump()` — hyperspace transition
- `playShieldDeflect()` — metallic shield impact
- `playCrash()` — collision impact noise
- `updateEngine()` — continuous engine rumble (speed-scaled)

#### Music Engine (Procedural Synthwave)
- **Game Mode**: Synthwave with kick drum, hi-hat, bassline, cosmic arpeggio
- **Boost Mode**: Tempo and frequency modulation for speed sensation
- **Hangar Mode**: Ambient atmospheric pad
- Low-pass filter during pause for muffled cinematic effect
- SFX and music volume independently controlled via pause menu sliders

### 🖥️ UI System

#### Main Menu
- Animated shimmer title with neon flicker effect
- 3D rotating ship preview (drag to rotate)
- Quick-launch with ship carousel selector
- Coin count + best score + pilot rank display

#### Flight HUD
- Level pill + sector icon
- Sector warp progress bar (% to next portal)
- Live score (gradient shimmer display)
- Distance telemetry
- Coin counter
- Speed gauge (KM/S)
- Shield pips (3–4 depending on ship)
- Combo badge (2× → 5×)
- Active power-up stack icons
- Mission tracker
- Near-miss toast

#### Pause Menu (Tactical)
- Current sector, distance, score stats
- SFX volume slider (0–100%)
- Music volume slider (0–100%)
- Graphics quality toggle (High/Medium)
- Resume / Restart / Return to Hangar

#### Game Over Screen
- Run reason display
- NEW PERSONAL BEST badge (shown on new high score)
- 4-stat grid: Distance / Coins / Near-Misses / Score
- XP earned display
- XP bar progress to next rank
- Rank promotion detection
- Achievement unlock toasts
- Play Again / Return to Hangar

#### Modals
- **Fleet Hangar** — Ship selection, stats, unlock with coins
- **10 Sectors** — Level grid showing unlock requirements
- **Upgrade Bay** — 4 upgrade trees (Boost/Shield/Magnet/Doubler), 5 levels each
- **Achievements** — 12 achievement cards with progress
- **Leaderboard** — 10-pilot global board with callsign editor
- **Career Dashboard** — 6-stat career overview + NASA research challenges
- **NASA Encyclopedia** — Detailed planetary fact sheets for all 10 sectors

#### NASA Science Toasts
- Periodic in-flight science facts (every 28 seconds) from active sector's data
- Facts pulled from authentic NASA/JPL planetary encyclopedia data
- 4 fact categories: Discovery, Dossier, Atmosphere, Orbital Mechanics

### 📱 Responsive Design
- **Desktop**: Full widescreen layout optimized for 1080p+
- **Mobile**: Touch controls visible on `pointer: coarse` or ≤900px viewport
- **On-screen buttons**: Left/Right lane, Jump, Dive, Boost
- **Swipe gestures**: Full 4-direction swipe support
- **CSS breakpoints**: 768px and 650px height with scaled fonts and layout

### 🏆 Hackathon Demo Tour
- Auto-runs a scripted 7-stage demonstration with narration overlay
- Demonstrates: lane switching, jumps, power-ups, science discovery, combat
- Ends with auto game-over for clean loop

---

## 🛠️ Project Structure

```
COSMIC_RUN_PREMIUM/
├── index.html                  ← GENERATED OUTPUT (~219KB, do not edit directly)
├── generate_premium_game.py    ← MASTER SOURCE (edit this, regenerate HTML)
├── build_cosmic_run.py         ← Thin wrapper — delegates to generator
├── package.json                ← Vite + Three.js dependencies
├── vite.config.js              ← Vite build config
├── dist/                       ← Production build output (npm run build)
├── README.md                   ← This file
└── UPDATE_NOTES.txt            ← Detailed change log
```

### Workflow
```bash
# Edit source
nano generate_premium_game.py

# Regenerate HTML
python3 generate_premium_game.py

# Dev server (live reload)
npx vite --port 5173

# Production build
npm run build

# Test modes (in browser)
# http://localhost:5173/?test=flight
# http://localhost:5173/?test=gameover
# http://localhost:5173/?test=pause
# http://localhost:5173/?test=leaderboard
# http://localhost:5173/?test=hangar
# http://localhost:5173/?test=achievements
# http://localhost:5173/?test=worlds
```

---

## 📦 Dependencies

```json
{
  "three": "^0.170.0",    // 3D engine (CDN importmap)
  "vite": "^6.4.6"        // Dev server + build tool
}
```

Three.js is loaded via importmap from CDN (`esm.sh`), so no bundling needed for the core 3D engine. Vite handles the HTML/JS transformation.

---

## 🎯 Performance

| Metric | Value |
|--------|-------|
| HTML size | ~219 KB |
| Production JS (minified) | ~564 KB (Three.js included) |
| Production JS (gzipped) | ~147 KB |
| Target FPS | 60 FPS (requestAnimationFrame) |
| Max delta clamp | 50ms (prevents spiral of death) |
| Obstacle pool | Dynamically spawned/despawned |
| Particle system | 180-point space dust + star field |

---

## 🏗️ Architecture

```
Single HTML file
├── <style>              CSS (~450 lines) — responsive, animated, glassmorphism UI
├── <body>               HTML (~400 lines) — HUD, modals, canvas
└── <script type="module">
    ├── Three.js scene setup (renderer, camera, lights, fog)
    ├── Procedural planet textures (canvas 2D → Three.js texture)
    ├── 5 ship models (parametric geometry, no external assets)
    ├── ENCYCLOPEDIA_DATA (10 planetary fact sheets)
    ├── LEVELS_CONFIG (10 sector configurations)
    ├── SHIPS_DATA (5 ships with stats)
    ├── PILOT_RANKS (10 XP tiers)
    ├── DEFAULT_ACHIEVEMENTS (12 achievements)
    ├── GLOBAL_LEADERBOARD (9 simulated pilots)
    ├── Web Audio SoundEngine (8 procedural SFX)
    ├── MusicEngine (procedural synthwave)
    ├── GameState (localStorage persistence)
    ├── Animate loop (rAF — ~60fps target)
    │   ├── Hangar mode (ship preview)
    │   └── Flight mode (obstacles, physics, HUD)
    └── UI Controller (modals, menus, events)
```

---

## 📸 Screenshots

Run the game at `http://localhost:5173` and use these test URLs:

| View | URL |
|------|-----|
| Main Menu | `http://localhost:5173/` |
| Flight HUD | `http://localhost:5173/?test=flight` |
| Game Over | `http://localhost:5173/?test=gameover` |
| Pause Menu | `http://localhost:5173/?test=pause` |
| Leaderboard | `http://localhost:5173/?test=leaderboard` |
| Hangar | `http://localhost:5173/?test=hangar` |
| Worlds Grid | `http://localhost:5173/?test=worlds` |

---

*Built with ❤️ using Three.js, Web Audio API, and pure JavaScript. No external assets.*
*All planetary data sourced from NASA Goddard, JPL, ESA, and JWST mission archives.*
