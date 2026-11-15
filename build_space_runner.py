#!/usr/bin/env python3
"""
Build script for SPACE RUNNER 3D - Endless 3D Space Runner & Planetary Exploration Game.
Generates a complete, highly optimized, and self-contained index.html.
"""

def generate_html():
    return r'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SPACE RUNNER 3D - Endless Interplanetary Odyssey</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
            -webkit-user-select: none;
        }

        :root {
            --cyan-glow: #00f0ff;
            --cyan-dim: #009bb3;
            --purple-glow: #b042ff;
            --purple-dim: #7928ca;
            --gold-glow: #ffd000;
            --green-glow: #00ff88;
            --red-alert: #ff3344;
            --panel-bg: rgba(4, 14, 28, 0.85);
            --panel-border: rgba(0, 240, 255, 0.35);
            --font-ui: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
            --font-mono: "SF Mono", "Consolas", "Courier New", monospace;
        }

        body {
            overflow: hidden;
            background: #01040a;
            color: #dffaff;
            font-family: var(--font-ui);
            width: 100vw;
            height: 100vh;
        }

        canvas#webgl {
            display: block;
            position: fixed;
            inset: 0;
            width: 100vw;
            height: 100vh;
            z-index: 1;
        }

        /* -------------------------------------------------------------
           MAIN MENU & HANGAR SCREEN
           ------------------------------------------------------------- */
        #mainMenu {
            position: fixed;
            inset: 0;
            z-index: 50;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 24px 32px;
            pointer-events: none;
            transition: opacity 0.4s ease, visibility 0.4s ease;
        }

        #mainMenu.hidden {
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
        }

        .menu-top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            pointer-events: auto;
        }

        .menu-logo-group {
            display: flex;
            flex-direction: column;
        }

        .menu-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(0, 240, 255, 0.12);
            border: 1px solid rgba(0, 240, 255, 0.4);
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 2px;
            color: var(--cyan-glow);
            width: fit-content;
            margin-bottom: 6px;
        }

        .menu-badge span.accent {
            background: linear-gradient(135deg, #b042ff, #00f0ff);
            color: #ffffff;
            padding: 1px 6px;
            border-radius: 3px;
        }

        .menu-title-main {
            font-size: clamp(32px, 5.5vw, 64px);
            font-weight: 900;
            letter-spacing: 6px;
            color: #ffffff;
            text-shadow: 0 0 30px rgba(0, 240, 255, 0.8), 0 0 60px rgba(176, 66, 255, 0.4);
            line-height: 1;
        }

        .menu-title-sub {
            font-size: 12px;
            font-family: var(--font-mono);
            letter-spacing: 3px;
            color: #8be5ff;
            margin-top: 6px;
        }

        .menu-stats-pill-group {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .stat-pill {
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-radius: 24px;
            padding: 6px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font-mono);
            font-size: 13px;
            font-weight: 800;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
        }

        .stat-pill.coins {
            color: var(--gold-glow);
            border-color: rgba(255, 208, 0, 0.4);
        }

        .stat-pill.best {
            color: var(--cyan-glow);
        }

        .stat-pill.level {
            color: var(--purple-glow);
            border-color: rgba(176, 66, 255, 0.4);
        }

        .menu-bottom-controls {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 16px;
            pointer-events: auto;
            margin-bottom: 12px;
        }

        .btn-launch {
            background: linear-gradient(135deg, #00f0ff, #b042ff);
            color: #010914;
            font-size: 20px;
            font-weight: 900;
            letter-spacing: 4px;
            padding: 16px 54px;
            border-radius: 8px;
            border: 1px solid #ffffff;
            cursor: pointer;
            box-shadow: 0 0 35px rgba(0, 240, 255, 0.7), inset 0 0 12px rgba(255, 255, 255, 0.5);
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .btn-launch:hover {
            transform: scale(1.05);
            background: #ffffff;
            color: #011422;
            box-shadow: 0 0 50px rgba(0, 240, 255, 0.95);
        }

        .menu-nav-row {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .btn-menu-tab {
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            color: #cbeeff;
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 1.5px;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
            backdrop-filter: blur(8px);
        }

        .btn-menu-tab:hover {
            border-color: var(--cyan-glow);
            background: rgba(0, 240, 255, 0.2);
            color: #ffffff;
            box-shadow: 0 0 16px rgba(0, 240, 255, 0.4);
            transform: translateY(-2px);
        }

        .hangar-ship-selector {
            position: absolute;
            bottom: 120px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            gap: 16px;
            pointer-events: auto;
        }

        .btn-ship-arrow {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--panel-bg);
            border: 1px solid var(--cyan-glow);
            color: var(--cyan-glow);
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
        }

        .btn-ship-arrow:hover {
            background: var(--cyan-glow);
            color: #01040a;
            box-shadow: 0 0 15px var(--cyan-glow);
        }

        .hangar-ship-title {
            text-align: center;
            background: rgba(4, 16, 32, 0.75);
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 6px;
            padding: 6px 18px;
            backdrop-filter: blur(8px);
        }

        .hangar-ship-title h3 {
            font-size: 14px;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 2px;
        }

        .hangar-ship-title p {
            font-size: 10px;
            color: var(--cyan-glow);
            font-family: var(--font-mono);
        }

        /* -------------------------------------------------------------
           IN-GAME RUNNER HUD
           ------------------------------------------------------------- */
        #gameHud {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 20;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 16px 20px;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease;
        }

        #gameHud.active {
            opacity: 1;
            visibility: visible;
        }

        .hud-top-bar {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            pointer-events: auto;
        }

        .hud-left-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .hud-world-pill {
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-left: 3px solid var(--cyan-glow);
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 11px;
            font-family: var(--font-mono);
            color: #8be5ff;
            letter-spacing: 1px;
            backdrop-filter: blur(8px);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .hud-distance-card {
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-radius: 6px;
            padding: 6px 12px;
            backdrop-filter: blur(8px);
        }

        .hud-distance-num {
            font-size: 22px;
            font-weight: 900;
            font-family: var(--font-mono);
            color: #ffffff;
            text-shadow: 0 0 10px var(--cyan-glow);
        }

        .hud-distance-unit {
            font-size: 10px;
            color: #8be5ff;
            letter-spacing: 1px;
            font-family: var(--font-mono);
        }

        /* Center Score */
        .hud-center-score {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .score-hero {
            font-size: clamp(34px, 5vw, 48px);
            font-weight: 900;
            font-family: var(--font-mono);
            color: #ffffff;
            text-shadow: 0 0 20px rgba(0, 240, 255, 0.7);
            line-height: 1;
        }

        .score-multiplier-badge {
            background: linear-gradient(135deg, #ffd000, #ff8800);
            color: #01121d;
            font-size: 10px;
            font-weight: 900;
            padding: 2px 8px;
            border-radius: 10px;
            letter-spacing: 1px;
            margin-top: 4px;
            box-shadow: 0 0 10px rgba(255, 208, 0, 0.6);
            display: none;
        }

        .score-multiplier-badge.active {
            display: inline-block;
        }

        /* Right Group (Coins, Shield Pips, Pause) */
        .hud-right-group {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 8px;
        }

        .hud-coin-pill {
            background: var(--panel-bg);
            border: 1px solid rgba(255, 208, 0, 0.4);
            border-radius: 20px;
            padding: 5px 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 15px;
            font-weight: 900;
            font-family: var(--font-mono);
            color: var(--gold-glow);
            backdrop-filter: blur(8px);
            box-shadow: 0 0 12px rgba(255, 208, 0, 0.25);
        }

        .hud-shield-container {
            display: flex;
            align-items: center;
            gap: 5px;
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            padding: 4px 10px;
            border-radius: 12px;
            backdrop-filter: blur(8px);
        }

        .shield-pip {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--cyan-glow);
            box-shadow: 0 0 8px var(--cyan-glow);
            transition: all 0.2s;
        }

        .shield-pip.depleted {
            background: #1a2c3a;
            box-shadow: none;
            border: 1px solid rgba(0, 240, 255, 0.2);
        }

        .hud-btn-icon {
            width: 36px;
            height: 36px;
            border-radius: 6px;
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            color: var(--cyan-glow);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
        }

        .hud-btn-icon:hover {
            background: var(--cyan-glow);
            color: #01040a;
            box-shadow: 0 0 12px var(--cyan-glow);
        }

        /* Active Power-Ups Area */
        .hud-powerup-stack {
            position: absolute;
            top: 110px;
            left: 20px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .powerup-pill {
            background: rgba(4, 18, 36, 0.85);
            border-radius: 6px;
            padding: 6px 10px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: var(--font-mono);
            font-size: 11px;
            font-weight: 800;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(6px);
            min-width: 140px;
        }

        .powerup-pill.boost { border: 1px solid #00f0ff; color: #00f0ff; }
        .powerup-pill.shield { border: 1px solid #00ff88; color: #00ff88; }
        .powerup-pill.magnet { border: 1px solid #b042ff; color: #b042ff; }
        .powerup-pill.double { border: 1px solid #ffd000; color: #ffd000; }

        .powerup-bar-bg {
            flex: 1;
            height: 4px;
            background: #081a2c;
            border-radius: 2px;
            overflow: hidden;
        }

        .powerup-bar-fill {
            height: 100%;
            width: 100%;
            transition: width 0.1s linear;
        }

        .powerup-pill.boost .powerup-bar-fill { background: #00f0ff; }
        .powerup-pill.shield .powerup-bar-fill { background: #00ff88; }
        .powerup-pill.magnet .powerup-bar-fill { background: #b042ff; }
        .powerup-pill.double .powerup-bar-fill { background: #ffd000; }

        /* Floating Science Discovery Card */
        #scienceToast {
            position: absolute;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%) translateY(30px);
            background: rgba(3, 16, 36, 0.92);
            border: 1px solid var(--cyan-glow);
            border-left: 4px solid var(--purple-glow);
            border-radius: 6px;
            padding: 8px 18px;
            max-width: 520px;
            width: 90%;
            text-align: center;
            backdrop-filter: blur(14px);
            box-shadow: 0 4px 25px rgba(0, 240, 255, 0.4);
            opacity: 0;
            transition: all 0.35s ease;
            pointer-events: none;
        }

        #scienceToast.show {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }

        .science-toast-tag {
            font-size: 9px;
            font-family: var(--font-mono);
            letter-spacing: 2px;
            color: var(--purple-glow);
            font-weight: 800;
        }

        .science-toast-body {
            font-size: 11.5px;
            color: #ffffff;
            margin-top: 2px;
            line-height: 1.4;
        }

        /* Mobile Touch Controls */
        #mobileControls {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 25;
            display: none;
        }

        @media (max-width: 900px), (pointer: coarse) {
            #mobileControls {
                display: block;
            }
        }

        .mobile-lane-btns {
            position: absolute;
            bottom: 30px;
            left: 20px;
            display: flex;
            gap: 12px;
            pointer-events: auto;
        }

        .mobile-jump-dive-btns {
            position: absolute;
            bottom: 30px;
            right: 20px;
            display: flex;
            gap: 12px;
            pointer-events: auto;
        }

        .touch-btn {
            width: 52px;
            height: 52px;
            border-radius: 12px;
            background: rgba(3, 16, 36, 0.75);
            border: 1.5px solid var(--cyan-glow);
            color: var(--cyan-glow);
            font-size: 20px;
            font-weight: 900;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 0 12px rgba(0, 240, 255, 0.3);
            touch-action: manipulation;
        }

        .touch-btn:active {
            background: var(--cyan-glow);
            color: #01040a;
        }

        /* -------------------------------------------------------------
           MODALS (WORLDS, HANGAR, UPGRADES, MISSIONS, ACHIEVEMENTS, GAME OVER)
           ------------------------------------------------------------- */
        .modal-overlay {
            position: fixed;
            inset: 0;
            z-index: 100;
            background: radial-gradient(circle at center, rgba(3, 14, 30, 0.94) 0%, rgba(1, 4, 10, 0.98) 100%);
            backdrop-filter: blur(16px);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 24px;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: all 0.3s ease;
        }

        .modal-overlay.active {
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }

        .modal-dialog {
            background: rgba(4, 18, 38, 0.94);
            border: 1px solid var(--panel-border);
            border-radius: 12px;
            max-width: 820px;
            width: 100%;
            max-height: 85vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 0 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 240, 255, 0.2);
        }

        .modal-header {
            padding: 16px 24px;
            border-bottom: 1px solid rgba(0, 240, 255, 0.2);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(3, 14, 30, 0.8);
        }

        .modal-header h2 {
            font-size: 18px;
            font-weight: 900;
            letter-spacing: 2px;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .modal-close-btn {
            background: transparent;
            border: none;
            color: #8be5ff;
            font-size: 18px;
            font-weight: 800;
            cursor: pointer;
            padding: 4px 8px;
            border-radius: 4px;
            transition: all 0.2s;
        }

        .modal-close-btn:hover {
            color: #ffffff;
            background: rgba(0, 240, 255, 0.2);
        }

        .modal-body {
            padding: 20px 24px;
            overflow-y: auto;
            flex: 1;
        }

        /* Worlds Grid */
        .worlds-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
        }

        @media (max-width: 768px) {
            .worlds-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .world-card {
            background: rgba(2, 12, 26, 0.85);
            border: 1px solid rgba(0, 240, 255, 0.25);
            border-radius: 8px;
            padding: 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            cursor: pointer;
            transition: all 0.22s ease;
            position: relative;
        }

        .world-card:hover {
            border-color: var(--cyan-glow);
            transform: translateY(-3px);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.35);
        }

        .world-card.active {
            border-color: var(--green-glow);
            background: rgba(0, 255, 136, 0.12);
            box-shadow: 0 0 24px rgba(0, 255, 136, 0.4);
        }

        .world-card.locked {
            opacity: 0.55;
            cursor: not-allowed;
            border-color: rgba(255, 255, 255, 0.15);
        }

        .world-card-icon {
            font-size: 32px;
            margin-bottom: 8px;
        }

        .world-card-title {
            font-size: 13px;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 1px;
        }

        .world-card-desc {
            font-size: 10px;
            color: #8be5ff;
            font-family: var(--font-mono);
            margin: 4px 0 8px 0;
            line-height: 1.35;
        }

        .world-status-tag {
            font-size: 9.5px;
            font-family: var(--font-mono);
            padding: 2px 8px;
            border-radius: 10px;
            font-weight: 800;
        }

        .world-status-tag.active {
            background: rgba(0, 255, 136, 0.25);
            color: var(--green-glow);
        }

        .world-status-tag.unlocked {
            background: rgba(0, 240, 255, 0.2);
            color: var(--cyan-glow);
        }

        .world-status-tag.locked {
            background: rgba(255, 255, 255, 0.1);
            color: #8a99a8;
        }

        /* Ships Grid */
        .ships-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 14px;
        }

        .ship-card {
            background: rgba(2, 12, 26, 0.85);
            border: 1px solid rgba(0, 240, 255, 0.25);
            border-radius: 8px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            transition: all 0.22s ease;
        }

        .ship-card:hover {
            border-color: var(--cyan-glow);
            transform: translateY(-2px);
        }

        .ship-card.equipped {
            border-color: var(--cyan-glow);
            background: rgba(0, 240, 255, 0.12);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.35);
        }

        .ship-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .ship-card-header h3 {
            font-size: 14px;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 1px;
        }

        .ship-perk {
            font-size: 10.5px;
            color: var(--cyan-glow);
            font-family: var(--font-mono);
        }

        .ship-stat-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 10px;
            font-family: var(--font-mono);
            color: #8be5ff;
        }

        .btn-card-action {
            margin-top: 6px;
            background: linear-gradient(135deg, #00b4c8, #007c8a);
            border: 1px solid #7effff;
            color: #00121d;
            font-weight: 900;
            font-size: 11px;
            letter-spacing: 1.5px;
            padding: 8px 12px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
        }

        .btn-card-action:hover {
            background: #ffffff;
            color: #001a2b;
            box-shadow: 0 0 14px var(--cyan-glow);
        }

        .btn-card-action.equipped {
            background: rgba(0, 255, 136, 0.2);
            border: 1px solid var(--green-glow);
            color: var(--green-glow);
            cursor: default;
        }

        /* Upgrades Grid */
        .upgrades-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .upgrade-item {
            background: rgba(2, 12, 26, 0.85);
            border: 1px solid rgba(0, 240, 255, 0.25);
            border-radius: 8px;
            padding: 14px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
        }

        .upgrade-info {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .upgrade-icon {
            font-size: 28px;
        }

        .upgrade-meta h4 {
            font-size: 13.5px;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 1px;
        }

        .upgrade-meta p {
            font-size: 10.5px;
            color: #8be5ff;
            font-family: var(--font-mono);
            margin-top: 2px;
        }

        .upgrade-pips {
            display: flex;
            gap: 4px;
            margin-top: 6px;
        }

        .upgrade-pip {
            width: 14px;
            height: 6px;
            background: #0d2238;
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 2px;
        }

        .upgrade-pip.filled {
            background: var(--cyan-glow);
            box-shadow: 0 0 6px var(--cyan-glow);
        }

        /* Missions & Achievements List */
        .missions-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .mission-card {
            background: rgba(2, 12, 26, 0.85);
            border: 1px solid rgba(0, 240, 255, 0.25);
            border-radius: 8px;
            padding: 12px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .mission-card.completed {
            border-color: rgba(0, 255, 136, 0.4);
            background: rgba(0, 255, 136, 0.08);
        }

        .mission-meta h4 {
            font-size: 13px;
            font-weight: 800;
            color: #ffffff;
        }

        .mission-reward {
            font-size: 10px;
            font-family: var(--font-mono);
            color: var(--gold-glow);
            margin-top: 3px;
        }

        /* Game Over Dialog */
        .gameover-dialog {
            background: rgba(4, 16, 36, 0.95);
            border: 2px solid var(--red-alert);
            border-radius: 12px;
            max-width: 480px;
            width: 100%;
            padding: 32px 36px;
            text-align: center;
            box-shadow: 0 0 60px rgba(255, 51, 68, 0.4);
        }

        .gameover-title {
            font-size: 26px;
            font-weight: 900;
            letter-spacing: 4px;
            color: #ffffff;
            text-shadow: 0 0 20px var(--red-alert);
            margin-bottom: 4px;
        }

        .gameover-sub {
            font-size: 11px;
            font-family: var(--font-mono);
            color: #8be5ff;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }

        .gameover-stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 22px;
        }

        .gameover-stat-box {
            background: rgba(0, 240, 255, 0.08);
            border: 1px solid rgba(0, 240, 255, 0.25);
            border-radius: 6px;
            padding: 10px;
        }

        .gameover-stat-box .label {
            font-size: 9.5px;
            color: #72a4be;
            font-family: var(--font-mono);
            letter-spacing: 1px;
        }

        .gameover-stat-box .val {
            font-size: 20px;
            font-weight: 900;
            font-family: var(--font-mono);
            color: #ffffff;
            margin-top: 2px;
        }

        .gameover-xp-card {
            background: rgba(176, 66, 255, 0.1);
            border: 1px solid rgba(176, 66, 255, 0.4);
            border-radius: 6px;
            padding: 10px;
            margin-bottom: 24px;
        }

        .gameover-xp-bar {
            height: 6px;
            background: #081a2c;
            border-radius: 3px;
            overflow: hidden;
            margin-top: 6px;
        }

        .gameover-xp-fill {
            height: 100%;
            background: linear-gradient(90deg, #b042ff, #00f0ff);
            width: 0%;
            transition: width 0.6s ease;
        }

        .gameover-btn-stack {
            display: flex;
            gap: 10px;
            justify-content: center;
        }
    </style>
</head>

<body>

    <canvas id="webgl"></canvas>

    <!-- 1. MAIN MENU SCREEN -->
    <div id="mainMenu">
        <div class="menu-top-bar">
            <div class="menu-logo-group">
                <div class="menu-badge">
                    <span class="accent">AAA 3D</span>
                    <span>INTERPLANETARY RUNNER</span>
                </div>
                <div class="menu-title-main">SPACE RUNNER 3D</div>
                <div class="menu-title-sub">REAL-TIME SOLAR SYSTEM HIGH-SPEED ODYSSEY</div>
            </div>

            <div class="menu-stats-pill-group">
                <div class="stat-pill coins">
                    <span>🪙</span> <span id="menuCoinCount">0</span>
                </div>
                <div class="stat-pill best">
                    <span>🏆</span> <span id="menuBestScore">0</span>
                </div>
                <div class="stat-pill level">
                    <span>LVL</span> <span id="menuPlayerLevel">1</span>
                </div>
                <button class="hud-btn-icon" id="menuAudioBtn" title="Toggle Audio">🔊</button>
            </div>
        </div>

        <!-- Central Hangar Spacecraft Selector -->
        <div class="hangar-ship-selector">
            <button class="btn-ship-arrow" id="prevShipBtn">◄</button>
            <div class="hangar-ship-title">
                <h3 id="hangarShipName">ORION SCOUT</h3>
                <p id="hangarShipPerk">AGILE EXPLORATION CRAFT</p>
            </div>
            <button class="btn-ship-arrow" id="nextShipBtn">►</button>
        </div>

        <div class="menu-bottom-controls">
            <button class="btn-launch" id="btnLaunchGame">
                <span>▶ LAUNCH MISSION</span>
            </button>

            <div class="menu-nav-row">
                <button class="btn-menu-tab" id="btnOpenWorlds">
                    <span>🪐</span> <span>WORLDS</span>
                </button>
                <button class="btn-menu-tab" id="btnOpenHangar">
                    <span>🚀</span> <span>GARAGE</span>
                </button>
                <button class="btn-menu-tab" id="btnOpenUpgrades">
                    <span>⚡</span> <span>UPGRADES</span>
                </button>
                <button class="btn-menu-tab" id="btnOpenMissions">
                    <span>📋</span> <span>MISSIONS</span>
                </button>
                <button class="btn-menu-tab" id="btnOpenAchievements">
                    <span>🏆</span> <span>BADGES</span>
                </button>
                <button class="btn-menu-tab" id="btnDailyReward">
                    <span>🎁</span> <span>DAILY BONUS</span>
                </button>
            </div>
        </div>
    </div>

    <!-- 2. IN-GAME HUD -->
    <div id="gameHud">
        <div class="hud-top-bar">
            <div class="hud-left-group">
                <div class="hud-world-pill" id="hudWorldPill">
                    <span id="hudWorldIcon">🌍</span>
                    <span id="hudWorldTitle">EARTH ORBIT</span>
                </div>
                <div class="hud-distance-card">
                    <span class="hud-distance-num" id="hudDistanceVal">0</span>
                    <span class="hud-distance-unit">METERS</span>
                </div>
            </div>

            <div class="hud-center-score">
                <div class="score-hero" id="hudScoreVal">0</div>
                <div class="score-multiplier-badge" id="hudMultiplierBadge">2X SCORE</div>
            </div>

            <div class="hud-right-group">
                <div class="hud-coin-pill">
                    <span>🪙</span>
                    <span id="hudCoinVal">0</span>
                </div>
                <div class="hud-shield-container" id="hudShieldPips">
                    <div class="shield-pip" id="pip1"></div>
                    <div class="shield-pip" id="pip2"></div>
                    <div class="shield-pip" id="pip3"></div>
                </div>
                <div style="display:flex; gap:6px;">
                    <button class="hud-btn-icon" id="inGameAudioBtn">🔊</button>
                    <button class="hud-btn-icon" id="inGamePauseBtn">⏸</button>
                </div>
            </div>
        </div>

        <!-- Active Power-Up Timers Stack -->
        <div class="hud-powerup-stack" id="hudPowerupStack">
            <!-- Dynamically populated when active -->
        </div>

        <!-- Floating Science Discovery Toast -->
        <div id="scienceToast">
            <div class="science-toast-tag" id="scienceToastTag">✦ PLANETARY DISCOVERY</div>
            <div class="science-toast-body" id="scienceToastBody">Scanning celestial target...</div>
        </div>
    </div>

    <!-- 3. MOBILE ON-SCREEN TOUCH CONTROLS -->
    <div id="mobileControls">
        <div class="mobile-lane-btns">
            <button class="touch-btn" id="touchLaneLeft">◄</button>
            <button class="touch-btn" id="touchLaneRight">►</button>
        </div>
        <div class="mobile-jump-dive-btns">
            <button class="touch-btn" id="touchJump">▲</button>
            <button class="touch-btn" id="touchDive">▼</button>
            <button class="touch-btn" id="touchBoost" style="color:var(--gold-glow); border-color:var(--gold-glow);">⚡</button>
        </div>
    </div>

    <!-- 4. WORLDS MODAL -->
    <div class="modal-overlay" id="worldsModal">
        <div class="modal-dialog">
            <div class="modal-header">
                <h2><span>🪐</span> EXPLORE PLANETARY WORLDS</h2>
                <button class="modal-close-btn" id="closeWorldsModal">✕</button>
            </div>
            <div class="modal-body">
                <div class="worlds-grid" id="worldsGrid">
                    <!-- Populated dynamically -->
                </div>
            </div>
        </div>
    </div>

    <!-- 5. HANGAR / SPACECRAFT GARAGE MODAL -->
    <div class="modal-overlay" id="garageModal">
        <div class="modal-dialog">
            <div class="modal-header">
                <h2><span>🚀</span> SPACECRAFT FLEET GARAGE</h2>
                <button class="modal-close-btn" id="closeGarageModal">✕</button>
            </div>
            <div class="modal-body">
                <div class="ships-grid" id="shipsGrid">
                    <!-- Populated dynamically -->
                </div>
            </div>
        </div>
    </div>

    <!-- 6. UPGRADES SHOP MODAL -->
    <div class="modal-overlay" id="upgradesModal">
        <div class="modal-dialog">
            <div class="modal-header">
                <h2><span>⚡</span> SHIP SYSTEMS & POWER-UP UPGRADES</h2>
                <button class="modal-close-btn" id="closeUpgradesModal">✕</button>
            </div>
            <div class="modal-body">
                <div class="upgrades-list" id="upgradesList">
                    <!-- Populated dynamically -->
                </div>
            </div>
        </div>
    </div>

    <!-- 7. MISSIONS MODAL -->
    <div class="modal-overlay" id="missionsModal">
        <div class="modal-dialog">
            <div class="modal-header">
                <h2><span>📋</span> ACTIVE FLIGHT MISSIONS</h2>
                <button class="modal-close-btn" id="closeMissionsModal">✕</button>
            </div>
            <div class="modal-body">
                <div class="missions-list" id="missionsList">
                    <!-- Populated dynamically -->
                </div>
            </div>
        </div>
    </div>

    <!-- 8. ACHIEVEMENTS MODAL -->
    <div class="modal-overlay" id="achievementsModal">
        <div class="modal-dialog">
            <div class="modal-header">
                <h2><span>🏆</span> PILOT BADGES & ACHIEVEMENTS</h2>
                <button class="modal-close-btn" id="closeAchievementsModal">✕</button>
            </div>
            <div class="modal-body">
                <div class="missions-list" id="achievementsList">
                    <!-- Populated dynamically -->
                </div>
            </div>
        </div>
    </div>

    <!-- 9. GAME OVER SCREEN -->
    <div class="modal-overlay" id="gameOverModal">
        <div class="gameover-dialog">
            <div class="gameover-title">MISSION TERMINATED</div>
            <div class="gameover-sub" id="gameoverReason">COLLISION DETECTED // FLIGHT TELEMETRY LOST</div>

            <div class="gameover-stats-grid">
                <div class="gameover-stat-box">
                    <div class="label">DISTANCE</div>
                    <div class="val" id="goDistance">0 M</div>
                </div>
                <div class="gameover-stat-box">
                    <div class="label">COINS COLLECTED</div>
                    <div class="val" id="goCoins" style="color:var(--gold-glow);">🪙 0</div>
                </div>
                <div class="gameover-stat-box" style="grid-column: span 2;">
                    <div class="label">FINAL SCORE</div>
                    <div class="val" id="goScore" style="color:var(--cyan-glow); font-size:26px;">0</div>
                </div>
            </div>

            <div class="gameover-xp-card">
                <div style="display:flex; justify-content:space-between; font-size:11px; font-family:var(--font-mono);">
                    <span>XP EARNED: <strong id="goXpEarned" style="color:var(--purple-glow);">+250 XP</strong></span>
                    <span id="goLevelDisplay">LEVEL 1</span>
                </div>
                <div class="gameover-xp-bar">
                    <div class="gameover-xp-fill" id="goXpFill"></div>
                </div>
            </div>

            <div class="gameover-btn-stack">
                <button class="btn-card-action" id="btnPlayAgain" style="font-size:13px; padding:10px 24px;">▶ PLAY AGAIN</button>
                <button class="btn-card-action" id="btnGoHome" style="background:rgba(4,24,48,0.8); border-color:var(--cyan-glow); color:#fff; font-size:13px; padding:10px 20px;">🏠 MENU</button>
            </div>
        </div>
    </div>

    <script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js"
  }
}
</script>

    <script type="module">
        import * as THREE from 'three';

        /* -------------------------------------------------------------
           PROCEDURAL WEB AUDIO SYNTHESIZER
           ------------------------------------------------------------- */
        class SoundEngine {
            constructor() {
                this.ctx = null;
                this.enabled = true;
                this.engineGain = null;
                this.engineOsc = null;
                this.initialized = false;
            }

            init() {
                if (this.initialized) return;
                try {
                    const AudioCtx = window.AudioContext || window.webkitAudioContext;
                    if (!AudioCtx) return;
                    this.ctx = new AudioCtx();

                    this.engineOsc = this.ctx.createOscillator();
                    this.engineOsc.type = 'sawtooth';
                    this.engineOsc.frequency.setValueAtTime(45, this.ctx.currentTime);

                    const filter = this.ctx.createBiquadFilter();
                    filter.type = 'lowpass';
                    filter.frequency.setValueAtTime(110, this.ctx.currentTime);

                    this.engineGain = this.ctx.createGain();
                    this.engineGain.gain.setValueAtTime(0.01, this.ctx.currentTime);

                    this.engineOsc.connect(filter);
                    filter.connect(this.engineGain);
                    this.engineGain.connect(this.ctx.destination);
                    this.engineOsc.start();

                    this.initialized = true;
                } catch (e) {
                    console.warn("Audio init bypassed", e);
                }
            }

            playCoin() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(987.77, this.ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(1318.51, this.ctx.currentTime + 0.08);
                    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.12);
                    osc.connect(gain);
                    gain.connect(this.ctx.destination);
                    osc.start();
                    osc.stop(this.ctx.currentTime + 0.13);
                } catch (e) { }
            }

            playLaneSwitch() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(220, this.ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(440, this.ctx.currentTime + 0.07);
                    gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
                    gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.08);
                    osc.connect(gain);
                    gain.connect(this.ctx.destination);
                    osc.start();
                    osc.stop(this.ctx.currentTime + 0.09);
                } catch (e) { }
            }

            playJump() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(300, this.ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(750, this.ctx.currentTime + 0.15);
                    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
                    gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.16);
                    osc.connect(gain);
                    gain.connect(this.ctx.destination);
                    osc.start();
                    osc.stop(this.ctx.currentTime + 0.17);
                } catch (e) { }
            }

            playDive() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(600, this.ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(220, this.ctx.currentTime + 0.14);
                    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
                    gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.15);
                    osc.connect(gain);
                    gain.connect(this.ctx.destination);
                    osc.start();
                    osc.stop(this.ctx.currentTime + 0.16);
                } catch (e) { }
            }

            playPowerup() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const now = this.ctx.currentTime;
                    [523.25, 659.25, 783.99, 1046.5].forEach((f, idx) => {
                        const osc = this.ctx.createOscillator();
                        const gain = this.ctx.createGain();
                        osc.type = 'sine';
                        osc.frequency.setValueAtTime(f, now + idx * 0.06);
                        gain.gain.setValueAtTime(0.1, now + idx * 0.06);
                        gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.06 + 0.2);
                        osc.connect(gain);
                        gain.connect(this.ctx.destination);
                        osc.start(now + idx * 0.06);
                        osc.stop(now + idx * 0.06 + 0.22);
                    });
                } catch (e) { }
            }

            playCrash() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const bufLen = this.ctx.sampleRate * 0.4;
                    const noiseBuf = this.ctx.createBuffer(1, bufLen, this.ctx.sampleRate);
                    const out = noiseBuf.getChannelData(0);
                    for (let i = 0; i < bufLen; i++) {
                        out[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufLen * 0.25));
                    }
                    const noise = this.ctx.createBufferSource();
                    noise.buffer = noiseBuf;

                    const filter = this.ctx.createBiquadFilter();
                    filter.type = 'lowpass';
                    filter.frequency.setValueAtTime(350, this.ctx.currentTime);

                    const gain = this.ctx.createGain();
                    gain.gain.setValueAtTime(0.3, this.ctx.currentTime);

                    noise.connect(filter);
                    filter.connect(gain);
                    gain.connect(this.ctx.destination);
                    noise.start();
                } catch (e) { }
            }

            playShieldDeflect() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(800, this.ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(300, this.ctx.currentTime + 0.2);
                    gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
                    gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.22);
                    osc.connect(gain);
                    gain.connect(this.ctx.destination);
                    osc.start();
                    osc.stop(this.ctx.currentTime + 0.23);
                } catch (e) { }
            }

            updateEngine(speedRatio) {
                if (!this.initialized || !this.enabled) return;
                const now = this.ctx.currentTime;
                this.engineGain.gain.setTargetAtTime(0.02 + speedRatio * 0.06, now, 0.1);
                this.engineOsc.frequency.setTargetAtTime(45 + speedRatio * 40, now, 0.1);
            }
        }

        const sound = new SoundEngine();
        window.addEventListener('click', () => sound.init(), { once: true });
        window.addEventListener('keydown', () => sound.init(), { once: true });

        /* -------------------------------------------------------------
           PERSISTENCE & GAME STATE MANAGER
           ------------------------------------------------------------- */
        const SAVE_KEY = "SPACE_RUNNER_3D_SAVE";

        const defaultSave = {
            coins: 0,
            highScore: 0,
            bestDistance: 0,
            level: 1,
            xp: 0,
            activeShip: 'orion',
            unlockedShips: ['orion'],
            activeWorld: 'earth',
            unlockedWorlds: ['earth', 'moon', 'mars'],
            upgrades: { boost: 1, shield: 1, magnet: 1, double: 1 },
            missions: [
                { id: "m_coins", title: "Collect 50 Energy Coins", target: 50, current: 0, rewardCoins: 150, rewardXp: 200, completed: false },
                { id: "m_dist", title: "Travel 2,000 Meters", target: 2000, current: 0, rewardCoins: 250, rewardXp: 300, completed: false },
                { id: "m_gates", title: "Fly through 8 Energy Gates", target: 8, current: 0, rewardCoins: 200, rewardXp: 250, completed: false }
            ],
            achievements: [
                { id: "ach_first", title: "Liftoff Ace", desc: "Complete your first mission run", unlocked: false },
                { id: "ach_warp", title: "Speed Demon", desc: "Activate a Warp Speed Boost", unlocked: false },
                { id: "ach_rich", title: "Cosmic Prospector", desc: "Accumulate 1,000 energy coins", unlocked: false },
                { id: "ach_explorer", title: "Solar Pioneer", desc: "Reach 5,000 meters in a single run", unlocked: false }
            ],
            dailyStreak: 1,
            lastDailyClaim: 0
        };

        let gameState = { ...defaultSave };
        try {
            const saved = localStorage.getItem(SAVE_KEY);
            if (saved) gameState = { ...defaultSave, ...JSON.parse(saved) };
        } catch (e) { }

        function saveGame() {
            try {
                localStorage.setItem(SAVE_KEY, JSON.stringify(gameState));
            } catch (e) { }
            updateMenuUI();
        }

        function addXP(amount) {
            gameState.xp += amount;
            const xpForNext = gameState.level * 500;
            if (gameState.xp >= xpForNext) {
                gameState.level++;
                gameState.xp -= xpForNext;
                showScienceToast("✦ LEVEL UP!", `Promoted to Pilot Rank Level ${gameState.level}! +200 Bonus Coins!`);
                gameState.coins += 200;
                sound.playPowerup();
            }
            saveGame();
        }

        /* -------------------------------------------------------------
           WORLDS DEFINITIONS & DATA
           ------------------------------------------------------------- */
        const WORLDS_DATA = {
            earth: {
                id: 'earth', name: 'Earth Orbit', icon: '🌍', minLevel: 1,
                desc: 'Low Earth Orbit passing over continents, auroras, and orbital communications relays.',
                bgCol: 0x01050e, fogCol: 0x031024, lightCol: 0xffffff, lightInt: 3.5,
                planetPos: [0, -120, -350], planetRadius: 90, planetTex: 'earth', hasClouds: true,
                nebulaCol: 0x0077ff,
                facts: [
                    "EARTH LEO // Orbital velocity at 400 km is approximately 7.66 km/s (27,600 km/h).",
                    "VAN ALLEN BELTS // Earth's magnetic dipole traps energetic charged particles from the solar wind.",
                    "THERMOSPHERE // Auroras occur when magnetospheric plasma excites atomic oxygen and nitrogen."
                ]
            },
            moon: {
                id: 'moon', name: 'Lunar Highlands', icon: '🌕', minLevel: 1,
                desc: 'Stark vacuum above the lunar regolith, Apollo landing sites, and ancient impact maria.',
                bgCol: 0x000104, fogCol: 0x040810, lightCol: 0xeeeef8, lightInt: 3.8,
                planetPos: [0, -75, -280], planetRadius: 55, planetTex: 'moon',
                nebulaCol: 0x4466aa,
                facts: [
                    "LUNAR GRAVITY // The Moon's surface gravity is 1.62 m/s², exactly 16.6% of Earth's.",
                    "REGOLITH // Lunar soil is comprised of microscopic, razor-sharp pulverized basalt silicate glass.",
                    "TYCHO CRATER // Rays of impact ejecta from Tycho stretch over 1,500 kilometers across the Moon."
                ]
            },
            mars: {
                id: 'mars', name: 'Mars Canyons', icon: '🔴', minLevel: 2,
                desc: 'Flying through the low stratosphere above Valles Marineris and Olympus Mons.',
                bgCol: 0x080201, fogCol: 0x220a04, lightCol: 0xffeedd, lightInt: 3.2,
                planetPos: [0, -85, -300], planetRadius: 65, planetTex: 'mars',
                nebulaCol: 0xff4411,
                facts: [
                    "VALLES MARINERIS // Mars hosts a canyon system over 4,000 km long, 200 km wide, and up to 7 km deep.",
                    "OLYMPUS MONS // The largest shield volcano in the solar system towers 21.9 km above the datum.",
                    "ATMOSPHERE // Martian air is 95% CO₂ with a surface pressure of just 6.1 millibars (0.6% Earth)."
                ]
            },
            mercury: {
                id: 'mercury', name: 'Mercury Perihelion', icon: '🌑', minLevel: 4,
                desc: 'Scorching orbital approach closest to the Sun under intense solar wind bombardment.',
                bgCol: 0x080401, fogCol: 0x261202, lightCol: 0xfffae0, lightInt: 4.8,
                planetPos: [0, -70, -260], planetRadius: 40, planetTex: 'mercury',
                nebulaCol: 0xffaa00,
                facts: [
                    "PERIHELION // Mercury experiences the highest orbital speed of any planet at 47.36 km/s.",
                    "TEMPERATURE SWINGS // Surface ranges from a blistering 430°C on day side to -180°C at night.",
                    "METALLIC CORE // Mercury's iron core accounts for nearly 70% of its total planetary mass."
                ]
            },
            venus: {
                id: 'venus', name: 'Venus Acid Deck', icon: '🟡', minLevel: 6,
                desc: 'Traversing the upper supercritical atmosphere above swirling sulfuric acid cloud decks.',
                bgCol: 0x0c0801, fogCol: 0x2e2006, lightCol: 0xffe899, lightInt: 3.4,
                planetPos: [0, -100, -320], planetRadius: 85, planetTex: 'venus',
                nebulaCol: 0xe5a820,
                facts: [
                    "SUPERCRITICAL CO₂ // Surface pressure reaches 92 bar, equivalent to 900 meters underwater on Earth.",
                    "GREENHOUSE RUNAWAY // Trapped thermal radiation keeps the entire planetary surface at a uniform 464°C.",
                    "RETROGRADE ROTATION // Venus rotates in reverse from east to west once every 243 Earth days."
                ]
            },
            jupiter: {
                id: 'jupiter', name: 'Jupiter Radiation Belt', icon: '🪐', minLevel: 8,
                desc: 'High-speed pass across the Great Red Spot storm vortex and Galilean moon orbits.',
                bgCol: 0x050402, fogCol: 0x181006, lightCol: 0xfff0dd, lightInt: 3.6,
                planetPos: [0, -140, -420], planetRadius: 130, planetTex: 'jupiter',
                nebulaCol: 0xcc7722,
                facts: [
                    "GREAT RED SPOT // An anticyclonic storm larger than Earth that has persisted for over 350 years.",
                    "MAGNETOSPHERE // Jupiter's magnetic tail stretches past Saturn's orbit, over 650 million kilometers.",
                    "MASS // Jupiter contains 2.5 times the combined mass of all other solar system planets combined."
                ]
            },
            saturn: {
                id: 'saturn', name: 'Saturn Ring Plane', icon: '✨', minLevel: 10,
                desc: 'Navigating directly inside the shimmering water-ice crystalline ring particulate plane.',
                bgCol: 0x040306, fogCol: 0x140e1a, lightCol: 0xfff2e0, lightInt: 3.4,
                planetPos: [0, -130, -380], planetRadius: 110, planetTex: 'saturn', hasRings: true,
                nebulaCol: 0xb088ff,
                facts: [
                    "RING COMPOSITION // 99% pure water-ice crystals ranging from microscopic grains to boulder size.",
                    "CASSINI DIVISION // The 4,800-kilometer gap in the rings is dynamically cleared by the moon Mimas.",
                    "DENSITY // Saturn is the only planet with average density (0.687 g/cm³) less than water."
                ]
            },
            deep_space: {
                id: 'deep_space', name: 'Interstellar Void', icon: '🌌', minLevel: 12,
                desc: 'Deep cosmic void filled with hyper-luminous nebulae, pulsar streams, and quantum anomalies.',
                bgCol: 0x020108, fogCol: 0x0c0618, lightCol: 0xd8b4ff, lightInt: 3.8,
                planetPos: [0, -100, -350], planetRadius: 75, planetTex: 'deep_space',
                nebulaCol: 0x9922ff,
                facts: [
                    "PULSAR BEAMS // Rapidly spinning neutron stars sweep electromagnetic beams with atomic precision.",
                    "INTERSTELLAR MEDIUM // Composed of neutral and ionized hydrogen gas with an average density of 1 atom/cm³.",
                    "COSMIC RAYS // High-energy atomic nuclei travelling near the speed of light originating from supernovas."
                ]
            }
        };

        /* -------------------------------------------------------------
           SPACECRAFT FLEET DEFINITIONS
           ------------------------------------------------------------- */
        const SHIPS_DATA = {
            orion: {
                id: 'orion', name: 'Orion Scout', perk: 'Balanced Explorer',
                cost: 0, speedBonus: 1.0, agility: 1.0, magnetBonus: 1.0,
                bodyCol: 0x00f0ff, wingCol: 0x122538, glowCol: 0x00f0ff,
                desc: 'Standard multi-role NASA exploration craft with optimized handling.'
            },
            phoenix: {
                id: 'phoenix', name: 'Phoenix Interceptor', perk: '+15% Speed Velocity',
                cost: 800, speedBonus: 1.15, agility: 1.1, magnetBonus: 1.0,
                bodyCol: 0xff3b30, wingCol: 0x3d0c08, glowCol: 0xff9500,
                desc: 'Aggressive forward-swept wing fighter built for raw atmospheric acceleration.'
            },
            aurora: {
                id: 'aurora', name: 'Aurora Stealth', perk: '+30% Magnet Radius',
                cost: 2000, speedBonus: 1.05, agility: 1.25, magnetBonus: 1.3,
                bodyCol: 0xb042ff, wingCol: 0x160a26, glowCol: 0xd475ff,
                desc: 'Black-ops radar-absorbent faceted hull with powerful electromagnetic field coils.'
            },
            valkyrie: {
                id: 'valkyrie', name: 'Valkyrie Titan', perk: '+1 Shield Health Pip',
                cost: 4500, speedBonus: 0.95, agility: 0.95, magnetBonus: 1.0,
                bodyCol: 0x00ff88, wingCol: 0x0a2618, glowCol: 0x55ffaa,
                desc: 'Reinforced heavy-alloy fuselage equipped with modular emergency forcefield capacitors.'
            },
            quantum: {
                id: 'quantum', name: 'Quantum Dart', perk: '+25% Score Bonus',
                cost: 8000, speedBonus: 1.2, agility: 1.3, magnetBonus: 1.2,
                bodyCol: 0xffd000, wingCol: 0x2b2204, glowCol: 0xfff066,
                desc: 'Experimental needle ship powered by zero-point energy manifold.'
            }
        };

        /* -------------------------------------------------------------
           THREE.JS ENGINE SETUP
           ------------------------------------------------------------- */
        const canvas = document.getElementById('webgl');
        const scene = new THREE.Scene();

        const camera = new THREE.PerspectiveCamera(65, window.innerWidth / window.innerHeight, 0.1, 2000);
        camera.position.set(0, 3.8, 10.5);

        const renderer = new THREE.WebGLRenderer({
            canvas,
            antialias: true,
            powerPreference: 'high-performance'
        });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.8));
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.3;

        // Space Lighting
        const ambientLight = new THREE.AmbientLight(0x182438, 1.4);
        scene.add(ambientLight);

        const sunLight = new THREE.DirectionalLight(0xffffff, 3.5);
        sunLight.position.set(-60, 100, 40);
        scene.add(sunLight);

        // Realistic Round Starfield (Texture-generated particles)
        function createStarTexture() {
            const c = document.createElement('canvas');
            c.width = 64; c.height = 64;
            const ctx = c.getContext('2d');
            const g = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
            g.addColorStop(0, 'rgba(255, 255, 255, 1)');
            g.addColorStop(0.2, 'rgba(200, 240, 255, 0.8)');
            g.addColorStop(0.6, 'rgba(100, 180, 255, 0.2)');
            g.addColorStop(1, 'rgba(0, 0, 0, 0)');
            ctx.fillStyle = g;
            ctx.fillRect(0, 0, 64, 64);
            return new THREE.CanvasTexture(c);
        }

        const starTex = createStarTexture();
        const starGeo = new THREE.BufferGeometry();
        const starPos = [];
        const starColors = [];
        const starColPalette = [
            new THREE.Color(0xffffff),
            new THREE.Color(0x9bd5ff),
            new THREE.Color(0xffe6ad),
            new THREE.Color(0xd0a8ff)
        ];

        for (let i = 0; i < 3500; i++) {
            const rad = 250 + Math.random() * 650;
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.acos(Math.random() * 2 - 1);
            starPos.push(
                rad * Math.sin(phi) * Math.cos(theta),
                rad * Math.sin(phi) * Math.sin(theta),
                rad * Math.cos(phi)
            );
            const c = starColPalette[Math.floor(Math.random() * starColPalette.length)];
            starColors.push(c.r, c.g, c.b);
        }

        starGeo.setAttribute('position', new THREE.Float32BufferAttribute(starPos, 3));
        starGeo.setAttribute('color', new THREE.Float32BufferAttribute(starColors, 3));

        const starMaterial = new THREE.PointsMaterial({
            map: starTex,
            size: 4.5,
            vertexColors: true,
            transparent: true,
            opacity: 0.9,
            blending: THREE.AdditiveBlending,
            depthWrite: false
        });
        const starField = new THREE.Points(starGeo, starMaterial);
        scene.add(starField);

        // Volumetric Nebula Clouds
        const nebulaGroup = new THREE.Group();
        scene.add(nebulaGroup);

        function createNebulaTexture(colorHex) {
            const c = document.createElement('canvas');
            c.width = 128; c.height = 128;
            const ctx = c.getContext('2d');
            const g = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
            g.addColorStop(0, colorHex);
            g.addColorStop(0.5, 'rgba(20, 5, 40, 0.2)');
            g.addColorStop(1, 'rgba(0, 0, 0, 0)');
            ctx.fillStyle = g;
            ctx.fillRect(0, 0, 128, 128);
            return new THREE.CanvasTexture(c);
        }

        for (let i = 0; i < 20; i++) {
            const sprMat = new THREE.SpriteMaterial({
                map: createNebulaTexture('rgba(0, 180, 255, 0.35)'),
                blending: THREE.AdditiveBlending,
                transparent: true,
                opacity: 0.4
            });
            const spr = new THREE.Sprite(sprMat);
            spr.scale.set(220, 220, 1);
            spr.position.set(
                (Math.random() - 0.5) * 500,
                (Math.random() - 0.5) * 200,
                -250 - Math.random() * 400
            );
            nebulaGroup.add(spr);
        }

        // Realistic Background Celestial Planet
        let backgroundPlanetMesh = null;
        let planetRingsMesh = null;

        function buildBackgroundPlanet(worldKey) {
            if (backgroundPlanetMesh) {
                scene.remove(backgroundPlanetMesh);
                backgroundPlanetMesh.geometry.dispose();
            }
            if (planetRingsMesh) {
                scene.remove(planetRingsMesh);
                planetRingsMesh.geometry.dispose();
                planetRingsMesh = null;
            }

            const w = WORLDS_DATA[worldKey] || WORLDS_DATA.earth;
            const geo = new THREE.SphereGeometry(w.planetRadius, 48, 48);

            // Procedural planet canvas
            const c = document.createElement('canvas');
            c.width = 512; c.height = 256;
            const ctx = c.getContext('2d');

            if (worldKey === 'earth') {
                ctx.fillStyle = '#0a2e5c';
                ctx.fillRect(0, 0, 512, 256);
                ctx.fillStyle = '#225528';
                ctx.beginPath(); ctx.ellipse(180, 110, 80, 50, 0, 0, Math.PI * 2); ctx.fill();
                ctx.beginPath(); ctx.ellipse(360, 130, 95, 60, 0, 0, Math.PI * 2); ctx.fill();
            } else if (worldKey === 'mars') {
                ctx.fillStyle = '#b74c24';
                ctx.fillRect(0, 0, 512, 256);
                ctx.fillStyle = '#6e2b14';
                ctx.beginPath(); ctx.ellipse(220, 130, 100, 55, 0.2, 0, Math.PI * 2); ctx.fill();
            } else if (worldKey === 'jupiter') {
                const bands = ['#8b5e34', '#c9a474', '#e2cfb1', '#9e623b', '#d8ba8e', '#6d3c1c'];
                for (let i = 0; i < 12; i++) {
                    ctx.fillStyle = bands[i % bands.length];
                    ctx.fillRect(0, i * (256 / 12), 512, 256 / 12);
                }
                ctx.fillStyle = '#c84422';
                ctx.beginPath(); ctx.ellipse(320, 160, 40, 24, 0, 0, Math.PI * 2); ctx.fill();
            } else {
                ctx.fillStyle = '#5c6470';
                ctx.fillRect(0, 0, 512, 256);
                for (let i = 0; i < 60; i++) {
                    ctx.fillStyle = '#3a3e47';
                    ctx.beginPath(); ctx.arc(Math.random() * 512, Math.random() * 256, 4 + Math.random() * 12, 0, Math.PI * 2); ctx.fill();
                }
            }

            const pTex = new THREE.CanvasTexture(c);
            const mat = new THREE.MeshStandardMaterial({
                map: pTex,
                roughness: 0.85,
                metalness: 0.1
            });
            backgroundPlanetMesh = new THREE.Mesh(geo, mat);
            backgroundPlanetMesh.position.set(...w.planetPos);
            scene.add(backgroundPlanetMesh);

            if (w.hasRings) {
                const ringGeo = new THREE.RingGeometry(w.planetRadius * 1.3, w.planetRadius * 2.2, 64);
                const ringMat = new THREE.MeshBasicMaterial({
                    color: 0xe5d0a5,
                    side: THREE.DoubleSide,
                    transparent: true,
                    opacity: 0.75
                });
                planetRingsMesh = new THREE.Mesh(ringGeo, ringMat);
                planetRingsMesh.rotation.x = -1.3;
                backgroundPlanetMesh.add(planetRingsMesh);
            }
        }

        /* -------------------------------------------------------------
           3D SPACECRAFT BUILDER (5 DISTINCT MODELS)
           ------------------------------------------------------------- */
        let shipGroup = new THREE.Group();
        scene.add(shipGroup);

        let shipVisual = new THREE.Group();
        shipGroup.add(shipVisual);

        // Shield Bubble Mesh
        const shieldGeo = new THREE.IcosahedronGeometry(2.3, 2);
        const shieldMat = new THREE.MeshBasicMaterial({
            color: 0x00f0ff,
            wireframe: true,
            transparent: true,
            opacity: 0.0,
            blending: THREE.AdditiveBlending
        });
        const shieldMesh = new THREE.Mesh(shieldGeo, shieldMat);
        shipGroup.add(shieldMesh);

        let flameMeshL, flameMeshR;

        function buildSpaceship(shipKey) {
            while (shipVisual.children.length > 0) {
                const obj = shipVisual.children[0];
                shipVisual.remove(obj);
                if (obj.geometry) obj.geometry.dispose();
            }

            const sData = SHIPS_DATA[shipKey] || SHIPS_DATA.orion;

            const hullMat = new THREE.MeshStandardMaterial({
                color: sData.bodyCol,
                metalness: 0.8,
                roughness: 0.25
            });

            const wingMat = new THREE.MeshStandardMaterial({
                color: sData.wingCol,
                metalness: 0.6,
                roughness: 0.4
            });

            const glassMat = new THREE.MeshPhysicalMaterial({
                color: 0x88e8ff,
                transmission: 0.8,
                opacity: 0.4,
                transparent: true,
                roughness: 0.1,
                metalness: 0.2
            });

            // Main Fuselage Core
            const fuselage = new THREE.Mesh(
                new THREE.ConeGeometry(0.85, 3.2, 8),
                hullMat
            );
            fuselage.rotation.x = -Math.PI / 2;
            shipVisual.add(fuselage);

            // Cockpit Canopy Glass
            const cockpit = new THREE.Mesh(
                new THREE.SphereGeometry(0.45, 16, 12),
                glassMat
            );
            cockpit.scale.set(0.7, 0.5, 1.4);
            cockpit.position.set(0, 0.35, -0.4);
            shipVisual.add(cockpit);

            // Wing configurations
            const wingL = new THREE.Mesh(new THREE.BoxGeometry(2.6, 0.1, 1.4), wingMat);
            wingL.position.set(-1.6, -0.05, 0.6);
            wingL.rotation.y = 0.25;
            shipVisual.add(wingL);

            const wingR = new THREE.Mesh(new THREE.BoxGeometry(2.6, 0.1, 1.4), wingMat);
            wingR.position.set(1.6, -0.05, 0.6);
            wingR.rotation.y = -0.25;
            shipVisual.add(wingR);

            // Dual Thruster Cones
            const engineGeo = new THREE.CylinderGeometry(0.22, 0.35, 0.6, 12);
            const engineMat = new THREE.MeshStandardMaterial({ color: 0x1f2630, metalness: 0.9, roughness: 0.2 });

            const engL = new THREE.Mesh(engineGeo, engineMat);
            engL.rotation.x = Math.PI / 2;
            engL.position.set(-0.4, 0, 1.6);
            shipVisual.add(engL);

            const engR = new THREE.Mesh(engineGeo, engineMat);
            engR.rotation.x = Math.PI / 2;
            engR.position.set(0.4, 0, 1.6);
            shipVisual.add(engR);

            // Dynamic Supersonic Flame Plumes
            const flameGeo = new THREE.ConeGeometry(0.28, 2.0, 12);
            const flameMat = new THREE.MeshBasicMaterial({
                color: sData.glowCol,
                transparent: true,
                opacity: 0.85,
                blending: THREE.AdditiveBlending
            });

            flameMeshL = new THREE.Mesh(flameGeo, flameMat);
            flameMeshL.rotation.x = -Math.PI / 2;
            flameMeshL.position.set(-0.4, 0, 2.6);
            shipVisual.add(flameMeshL);

            flameMeshR = new THREE.Mesh(flameGeo, flameMat);
            flameMeshR.rotation.x = -Math.PI / 2;
            flameMeshR.position.set(0.4, 0, 2.6);
            shipVisual.add(flameMeshR);
        }

        buildSpaceship(gameState.activeShip);
        buildBackgroundPlanet(gameState.activeWorld);

        /* -------------------------------------------------------------
           PROCEDURAL RUNNER TRACK & 3D OBSTACLE POOL
           ------------------------------------------------------------- */
        const LANES_X = [-4.5, 0.0, 4.5];
        let currentLane = 1; // 0: Left, 1: Center, 2: Right
        let targetLane = 1;
        let isJumping = false;
        let isDiving = false;
        let verticalY = 1.0;
        let targetVerticalY = 1.0;

        // Obstacles & Collectibles Pools
        const activeObstacles = [];
        const activeCollectibles = [];

        // 3D Asteroid Geometries
        const asteroidGeos = [
            new THREE.DodecahedronGeometry(1.6, 1),
            new THREE.IcosahedronGeometry(1.4, 0),
            new THREE.DodecahedronGeometry(2.0, 0)
        ];
        // Distort vertices slightly for realistic irregular rocky look
        asteroidGeos.forEach(geo => {
            const pos = geo.attributes.position;
            for (let i = 0; i < pos.count; i++) {
                pos.setXYZ(
                    i,
                    pos.getX(i) * (0.85 + Math.random() * 0.3),
                    pos.getY(i) * (0.85 + Math.random() * 0.3),
                    pos.getZ(i) * (0.85 + Math.random() * 0.3)
                );
            }
            geo.computeVertexNormals();
        });

        const asteroidMat = new THREE.MeshStandardMaterial({
            color: 0x6e7078,
            roughness: 0.9,
            metalness: 0.1
        });

        // 3D Energy Gate Mesh Factory
        function createEnergyGateMesh() {
            const group = new THREE.Group();
            const arch = new THREE.Mesh(
                new THREE.TorusGeometry(3.2, 0.22, 8, 24, Math.PI),
                new THREE.MeshBasicMaterial({ color: 0x00f0ff })
            );
            arch.rotation.z = -Math.PI;
            arch.position.y = 0.5;
            group.add(arch);

            const field = new THREE.Mesh(
                new THREE.PlaneGeometry(5.8, 3.2),
                new THREE.MeshBasicMaterial({
                    color: 0x00f0ff,
                    transparent: true,
                    opacity: 0.18,
                    side: THREE.DoubleSide
                })
            );
            field.position.y = 1.6;
            group.add(field);
            return group;
        }

        // 3D Laser Hurdle (Requires Fly Up / Jump OR Dive)
        function createLaserHurdle(isHigh) {
            const group = new THREE.Group();
            const poleGeo = new THREE.CylinderGeometry(0.15, 0.15, 5.0, 8);
            const poleMat = new THREE.MeshStandardMaterial({ color: 0x223344, metalness: 0.8 });

            const pL = new THREE.Mesh(poleGeo, poleMat); pL.position.set(-3.0, 2.5, 0); group.add(pL);
            const pR = new THREE.Mesh(poleGeo, poleMat); pR.position.set(3.0, 2.5, 0); group.add(pR);

            const beamY = isHigh ? 3.6 : 1.2;
            const beam = new THREE.Mesh(
                new THREE.BoxGeometry(6.0, 0.35, 0.2),
                new THREE.MeshBasicMaterial({ color: 0xff3344, blending: THREE.AdditiveBlending })
            );
            beam.position.y = beamY;
            group.add(beam);
            group.userData.isHigh = isHigh;
            return group;
        }

        // 3D Rotating Satellite Debris
        function createRotatingDebris() {
            const group = new THREE.Group();
            const core = new THREE.Mesh(new THREE.BoxGeometry(1.2, 1.2, 1.2), new THREE.MeshStandardMaterial({ color: 0x8899aa, metalness: 0.8 }));
            group.add(core);
            const wingGeo = new THREE.BoxGeometry(3.4, 0.08, 1.0);
            const wingMat = new THREE.MeshStandardMaterial({ color: 0x113355, roughness: 0.3 });
            const w1 = new THREE.Mesh(wingGeo, wingMat); w1.position.x = -2.4; group.add(w1);
            const w2 = new THREE.Mesh(wingGeo, wingMat); w2.position.x = 2.4; group.add(w2);
            return group;
        }

        // 3D Energy Coin
        const coinGeo = new THREE.CylinderGeometry(0.85, 0.85, 0.18, 16);
        coinGeo.rotateX(Math.PI / 2);
        const coinMat = new THREE.MeshStandardMaterial({
            color: 0xffd000,
            metalness: 0.9,
            roughness: 0.15,
            emissive: 0x443300
        });

        // 3D Powerup Orb
        function createPowerupMesh(type) {
            const group = new THREE.Group();
            const sphere = new THREE.Mesh(
                new THREE.SphereGeometry(1.1, 16, 16),
                new THREE.MeshPhysicalMaterial({
                    color: type === 'boost' ? 0x00f0ff : (type === 'shield' ? 0x00ff88 : (type === 'magnet' ? 0xb042ff : 0xffd000)),
                    transmission: 0.7,
                    opacity: 0.8,
                    transparent: true,
                    roughness: 0.1
                })
            );
            group.add(sphere);
            group.userData.powerupType = type;
            return group;
        }

        /* -------------------------------------------------------------
           SPAWNER LOGIC & CHUNKS
           ------------------------------------------------------------- */
        let nextSpawnZ = -80;
        const CHUNK_INTERVAL = 38;

        function spawnTrackChunk(spawnZ) {
            const pattern = Math.floor(Math.random() * 6);
            const laneChoices = [0, 1, 2];

            // 1. Spawn Obstacles
            if (pattern === 0) {
                // Single Asteroid in random lane
                const laneIdx = laneChoices[Math.floor(Math.random() * 3)];
                const astMesh = new THREE.Mesh(
                    asteroidGeos[Math.floor(Math.random() * asteroidGeos.length)],
                    asteroidMat
                );
                astMesh.position.set(LANES_X[laneIdx], 1.2, spawnZ);
                astMesh.userData = { type: 'asteroid', lane: laneIdx, rotSpeed: 0.02 + Math.random() * 0.03 };
                scene.add(astMesh);
                activeObstacles.push(astMesh);

            } else if (pattern === 1) {
                // Two Asteroids leaving one open lane!
                const openLane = laneChoices[Math.floor(Math.random() * 3)];
                laneChoices.filter(l => l !== openLane).forEach(lIdx => {
                    const astMesh = new THREE.Mesh(
                        asteroidGeos[Math.floor(Math.random() * asteroidGeos.length)],
                        asteroidMat
                    );
                    astMesh.position.set(LANES_X[lIdx], 1.2, spawnZ);
                    astMesh.userData = { type: 'asteroid', lane: lIdx, rotSpeed: 0.02 };
                    scene.add(astMesh);
                    activeObstacles.push(astMesh);
                });

            } else if (pattern === 2) {
                // Energy Gate (Boost / Score tunnel)
                const gate = createEnergyGateMesh();
                gate.position.set(0, 0, spawnZ);
                gate.userData = { type: 'gate', passed: false };
                scene.add(gate);
                activeObstacles.push(gate);

            } else if (pattern === 3) {
                // Laser hurdle (requires Up Jump or Down Dive)
                const isHigh = Math.random() > 0.5;
                const hurdle = createLaserHurdle(isHigh);
                hurdle.position.set(0, 0, spawnZ);
                hurdle.userData = { type: 'laser', isHigh };
                scene.add(hurdle);
                activeObstacles.push(hurdle);

            } else if (pattern === 4) {
                // Rotating Space Satellite
                const rotDebris = createRotatingDebris();
                rotDebris.position.set(0, 2.0, spawnZ);
                rotDebris.userData = { type: 'rot_debris', rotZ: 0.04 };
                scene.add(rotDebris);
                activeObstacles.push(rotDebris);
            }

            // 2. Spawn Coins in line or arc
            const coinLane = laneChoices[Math.floor(Math.random() * 3)];
            for (let c = 0; c < 5; c++) {
                const coin = new THREE.Mesh(coinGeo, coinMat);
                coin.position.set(LANES_X[coinLane], 1.2, spawnZ - 12 - c * 4.0);
                coin.userData = { type: 'coin', collected: false };
                scene.add(coin);
                activeCollectibles.push(coin);
            }

            // 3. Rare Power-up Spawner (15% chance per chunk)
            if (Math.random() < 0.18) {
                const pTypes = ['boost', 'shield', 'magnet', 'double'];
                const pType = pTypes[Math.floor(Math.random() * pTypes.length)];
                const pOrb = createPowerupMesh(pType);
                const pLane = laneChoices[Math.floor(Math.random() * 3)];
                pOrb.position.set(LANES_X[pLane], 1.6, spawnZ - 6);
                scene.add(pOrb);
                activeCollectibles.push(pOrb);
            }
        }

        /* -------------------------------------------------------------
           GAMEPLAY LOOP & STATE
           ------------------------------------------------------------- */
        let isGameRunning = false;
        let isPaused = false;
        let runScore = 0;
        let runDistance = 0;
        let runCoins = 0;
        let runShieldPips = 3;
        let runSpeed = 42.0; // m/s
        let activePowerups = {
            boost: 0,
            shield: 0,
            magnet: 0,
            double: 0
        };

        const clock = new THREE.Clock();

        // Lane Navigation Inputs
        function moveLaneLeft() {
            if (!isGameRunning || isPaused) return;
            if (targetLane > 0) {
                targetLane--;
                sound.playLaneSwitch();
            }
        }

        function moveLaneRight() {
            if (!isGameRunning || isPaused) return;
            if (targetLane < 2) {
                targetLane++;
                sound.playLaneSwitch();
            }
        }

        function triggerJump() {
            if (!isGameRunning || isPaused || isJumping) return;
            isJumping = true;
            targetVerticalY = 3.6;
            sound.playJump();
            setTimeout(() => {
                targetVerticalY = 1.0;
                setTimeout(() => { isJumping = false; }, 300);
            }, 600);
        }

        function triggerDive() {
            if (!isGameRunning || isPaused || isDiving) return;
            isDiving = true;
            targetVerticalY = -0.5;
            sound.playDive();
            setTimeout(() => {
                targetVerticalY = 1.0;
                setTimeout(() => { isDiving = false; }, 250);
            }, 500);
        }

        // Keyboard Event Listeners
        window.addEventListener('keydown', e => {
            const k = e.key.toLowerCase();
            if (k === 'arrowleft' || k === 'a') moveLaneLeft();
            if (k === 'arrowright' || k === 'd') moveLaneRight();
            if (k === 'arrowup' || k === 'w') triggerJump();
            if (k === 'arrowdown' || k === 's') triggerDive();
            if (e.code === 'Space') {
                if (isGameRunning && activePowerups.boost <= 0 && gameState.coins >= 50) {
                    // Quick Boost purchase with coins during run
                    activatePowerup('boost', 6.0);
                    gameState.coins -= 50;
                    saveGame();
                }
            }
            if (k === 'p') togglePause();
        });

        // Touch / Swipe Gesture Handlers
        let touchStartX = 0, touchStartY = 0;
        window.addEventListener('touchstart', e => {
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
        }, { passive: true });

        window.addEventListener('touchend', e => {
            const dx = e.changedTouches[0].clientX - touchStartX;
            const dy = e.changedTouches[0].clientY - touchStartY;
            if (Math.abs(dx) > Math.abs(dy)) {
                if (dx > 35) moveLaneRight();
                else if (dx < -35) moveLaneLeft();
            } else {
                if (dy < -35) triggerJump();
                else if (dy > 35) triggerDive();
            }
        }, { passive: true });

        document.getElementById('touchLaneLeft')?.addEventListener('click', moveLaneLeft);
        document.getElementById('touchLaneRight')?.addEventListener('click', moveLaneRight);
        document.getElementById('touchJump')?.addEventListener('click', triggerJump);
        document.getElementById('touchDive')?.addEventListener('click', triggerDive);
        document.getElementById('touchBoost')?.addEventListener('click', () => {
            if (isGameRunning && activePowerups.boost <= 0) activatePowerup('boost', 6.0);
        });

        /* -------------------------------------------------------------
           POWER-UP SYSTEM
           ------------------------------------------------------------- */
        function activatePowerup(type, duration) {
            sound.playPowerup();
            const upgLevel = gameState.upgrades[type] || 1;
            const finalDuration = duration * (1 + (upgLevel - 1) * 0.25);
            activePowerups[type] = finalDuration;

            // Mission trigger check
            if (type === 'boost') checkAchievement('ach_warp');

            renderActivePowerupsHUD();
        }

        function renderActivePowerupsHUD() {
            const stack = document.getElementById('hudPowerupStack');
            stack.innerHTML = '';
            Object.entries(activePowerups).forEach(([type, remaining]) => {
                if (remaining > 0) {
                    const pill = document.createElement('div');
                    pill.className = `powerup-pill ${type}`;
                    const names = { boost: '⚡ SPEED BOOST', shield: '🛡 ENERGY SHIELD', magnet: '🧲 COIN MAGNET', double: '2️⃣ DOUBLE SCORE' };
                    pill.innerHTML = `
                        <span>${names[type]}</span>
                        <div class="powerup-bar-bg"><div class="powerup-bar-fill" style="width:100%;"></div></div>
                    `;
                    stack.appendChild(pill);
                }
            });
            document.getElementById('hudMultiplierBadge').classList.toggle('active', activePowerups.double > 0);
        }

        /* -------------------------------------------------------------
           SCIENCE LEARNING & TELEMETRY DISCOVERIES
           ------------------------------------------------------------- */
        let lastScienceFactTime = 0;
        const scienceToast = document.getElementById('scienceToast');
        const scienceToastTag = document.getElementById('scienceToastTag');
        const scienceToastBody = document.getElementById('scienceToastBody');
        let scienceToastTimeout = null;

        function showScienceToast(tag, text) {
            scienceToastTag.textContent = tag;
            scienceToastBody.textContent = text;
            scienceToast.classList.add('show');
            clearTimeout(scienceToastTimeout);
            scienceToastTimeout = setTimeout(() => {
                scienceToast.classList.remove('show');
            }, 4500);
        }

        function triggerRandomScienceFact() {
            const w = WORLDS_DATA[gameState.activeWorld] || WORLDS_DATA.earth;
            if (w.facts && w.facts.length > 0) {
                const fact = w.facts[Math.floor(Math.random() * w.facts.length)];
                showScienceToast(`✦ ${w.name.toUpperCase()} TELEMETRY`, fact);
                addXP(75);
            }
        }

        /* -------------------------------------------------------------
           MISSION TRACKING & ACHIEVEMENTS
           ------------------------------------------------------------- */
        function trackMissionProgress(id, amount) {
            gameState.missions.forEach(m => {
                if (m.id === id && !m.completed) {
                    m.current += amount;
                    if (m.current >= m.target) {
                        m.completed = true;
                        gameState.coins += m.rewardCoins;
                        addXP(m.rewardXp);
                        showScienceToast("✦ MISSION ACCOMPLISHED!", `${m.title} complete! +${m.rewardCoins} Coins!`);
                        sound.playPowerup();
                    }
                }
            });
            saveGame();
        }

        function checkAchievement(achId) {
            gameState.achievements.forEach(ach => {
                if (ach.id === achId && !ach.unlocked) {
                    ach.unlocked = true;
                    addXP(500);
                    gameState.coins += 350;
                    showScienceToast("🏆 ACHIEVEMENT UNLOCKED!", `${ach.title}: ${ach.desc}`);
                    sound.playPowerup();
                }
            });
            saveGame();
        }

        /* -------------------------------------------------------------
           START RUN & GAME OVER SEQUENCE
           ------------------------------------------------------------- */
        const mainMenu = document.getElementById('mainMenu');
        const gameHud = document.getElementById('gameHud');
        const gameOverModal = document.getElementById('gameOverModal');

        function startRun() {
            sound.init();
            sound.playLaneSwitch();

            // Clear previous entities
            activeObstacles.forEach(o => scene.remove(o));
            activeCollectibles.forEach(c => scene.remove(c));
            activeObstacles.length = 0;
            activeCollectibles.length = 0;

            // Reset run metrics
            runScore = 0;
            runDistance = 0;
            runCoins = 0;
            const extraShield = (gameState.activeShip === 'valkyrie' ? 1 : 0);
            runShieldPips = 3 + extraShield;
            const sData = SHIPS_DATA[gameState.activeShip] || SHIPS_DATA.orion;
            runSpeed = 42.0 * sData.speedBonus;

            activePowerups = { boost: 0, shield: 0, magnet: 0, double: 0 };

            currentLane = 1;
            targetLane = 1;
            verticalY = 1.0;
            targetVerticalY = 1.0;
            shipGroup.position.set(LANES_X[1], 1.0, 0);

            nextSpawnZ = -80;
            for (let i = 0; i < 7; i++) {
                spawnTrackChunk(nextSpawnZ);
                nextSpawnZ -= CHUNK_INTERVAL;
            }

            // UI transitions
            mainMenu.classList.add('hidden');
            gameOverModal.classList.remove('active');
            gameHud.classList.add('active');

            updateShieldPipsUI();
            renderActivePowerupsHUD();

            const curWorld = WORLDS_DATA[gameState.activeWorld] || WORLDS_DATA.earth;
            document.getElementById('hudWorldIcon').textContent = curWorld.icon;
            document.getElementById('hudWorldTitle').textContent = curWorld.name.toUpperCase();

            isGameRunning = true;
            isPaused = false;
            clock.start();
            lastScienceFactTime = performance.now();

            checkAchievement('ach_first');
            showScienceToast("✦ FLIGHT LAUNCHED", `Entering ${curWorld.name}. Avoid space debris and collect energy tokens!`);
        }

        document.getElementById('btnLaunchGame').onclick = startRun;
        document.getElementById('btnPlayAgain').onclick = startRun;

        function endRun(reason) {
            isGameRunning = false;
            sound.playCrash();

            // Check High Score
            const isNewBest = (runScore > gameState.highScore);
            if (isNewBest) gameState.highScore = Math.round(runScore);
            if (runDistance > gameState.bestDistance) gameState.bestDistance = Math.round(runDistance);

            gameState.coins += runCoins;
            const xpEarned = Math.round(runDistance * 0.15 + runCoins * 2);
            addXP(xpEarned);

            if (gameState.coins >= 1000) checkAchievement('ach_rich');
            if (runDistance >= 5000) checkAchievement('ach_explorer');

            saveGame();

            // Populate Game Over Screen
            document.getElementById('gameoverReason').textContent = reason || "COLLISION DETECTED // FLIGHT LOST";
            document.getElementById('goDistance').textContent = `${Math.round(runDistance)} M`;
            document.getElementById('goCoins').textContent = `🪙 ${runCoins}`;
            document.getElementById('goScore').textContent = Math.round(runScore).toLocaleString();
            document.getElementById('goXpEarned').textContent = `+${xpEarned} XP`;
            document.getElementById('goLevelDisplay').textContent = `PILOT LEVEL ${gameState.level}`;

            const xpForNext = gameState.level * 500;
            const pct = (gameState.xp / xpForNext) * 100;
            document.getElementById('goXpFill').style.width = `${pct}%`;

            gameHud.classList.remove('active');
            gameOverModal.classList.add('active');
        }

        document.getElementById('btnGoHome').onclick = () => {
            gameOverModal.classList.remove('active');
            mainMenu.classList.remove('hidden');
            updateMenuUI();
        };

        function togglePause() {
            if (!isGameRunning) return;
            isPaused = !isPaused;
            document.getElementById('inGamePauseBtn').textContent = isPaused ? "▶" : "⏸";
        }
        document.getElementById('inGamePauseBtn').onclick = togglePause;

        function updateShieldPipsUI() {
            for (let i = 1; i <= 3; i++) {
                const pip = document.getElementById(`pip${i}`);
                if (pip) pip.classList.toggle('depleted', i > runShieldPips);
            }
        }

        /* -------------------------------------------------------------
           UI MENUS & MODALS INTERACTION
           ------------------------------------------------------------- */
        function updateMenuUI() {
            document.getElementById('menuCoinCount').textContent = gameState.coins.toLocaleString();
            document.getElementById('menuBestScore').textContent = gameState.highScore.toLocaleString();
            document.getElementById('menuPlayerLevel').textContent = gameState.level;

            const shipData = SHIPS_DATA[gameState.activeShip] || SHIPS_DATA.orion;
            document.getElementById('hangarShipName').textContent = shipData.name.toUpperCase();
            document.getElementById('hangarShipPerk').textContent = shipData.perk.toUpperCase();
        }
        updateMenuUI();

        // Hangar Ship Carousel in Menu
        const shipKeys = Object.keys(SHIPS_DATA);
        document.getElementById('prevShipBtn').onclick = () => {
            const idx = shipKeys.indexOf(gameState.activeShip);
            const prevKey = shipKeys[(idx - 1 + shipKeys.length) % shipKeys.length];
            gameState.activeShip = prevKey;
            buildSpaceship(prevKey);
            saveGame();
            sound.playLaneSwitch();
        };

        document.getElementById('nextShipBtn').onclick = () => {
            const idx = shipKeys.indexOf(gameState.activeShip);
            const nextKey = shipKeys[(idx + 1) % shipKeys.length];
            gameState.activeShip = nextKey;
            buildSpaceship(nextKey);
            saveGame();
            sound.playLaneSwitch();
        };

        // Worlds Modal Setup
        const worldsModal = document.getElementById('worldsModal');
        document.getElementById('btnOpenWorlds').onclick = () => {
            populateWorldsGrid();
            worldsModal.classList.add('active');
            sound.playLaneSwitch();
        };
        document.getElementById('closeWorldsModal').onclick = () => worldsModal.classList.remove('active');

        function populateWorldsGrid() {
            const grid = document.getElementById('worldsGrid');
            grid.innerHTML = '';
            Object.values(WORLDS_DATA).forEach(w => {
                const card = document.createElement('div');
                const isUnlocked = gameState.unlockedWorlds.includes(w.id) || gameState.level >= w.minLevel;
                const isActive = (gameState.activeWorld === w.id);

                card.className = `world-card ${isActive ? 'active' : ''} ${!isUnlocked ? 'locked' : ''}`;
                card.innerHTML = `
                    <div class="world-card-icon">${w.icon}</div>
                    <div class="world-card-title">${w.name.toUpperCase()}</div>
                    <div class="world-card-desc">${w.desc}</div>
                    <div class="world-status-tag ${isActive ? 'active' : (isUnlocked ? 'unlocked' : 'locked')}">
                        ${isActive ? 'CURRENT WORLD' : (isUnlocked ? 'SELECT WORLD' : `UNLOCK LVL ${w.minLevel}`)}
                    </div>
                `;

                if (isUnlocked) {
                    card.onclick = () => {
                        gameState.activeWorld = w.id;
                        buildBackgroundPlanet(w.id);
                        saveGame();
                        populateWorldsGrid();
                        sound.playCoin();
                    };
                }
                grid.appendChild(card);
            });
        }

        // Hangar Modal Setup
        const garageModal = document.getElementById('garageModal');
        document.getElementById('btnOpenHangar').onclick = () => {
            populateShipsGrid();
            garageModal.classList.add('active');
            sound.playLaneSwitch();
        };
        document.getElementById('closeGarageModal').onclick = () => garageModal.classList.remove('active');

        function populateShipsGrid() {
            const grid = document.getElementById('shipsGrid');
            grid.innerHTML = '';
            Object.values(SHIPS_DATA).forEach(s => {
                const card = document.createElement('div');
                const isOwned = gameState.unlockedShips.includes(s.id);
                const isEquipped = (gameState.activeShip === s.id);

                card.className = `ship-card ${isEquipped ? 'equipped' : ''}`;
                card.innerHTML = `
                    <div class="ship-card-header">
                        <h3>${s.name.toUpperCase()}</h3>
                        <span style="font-size:11px; font-weight:800; color:${isOwned ? 'var(--green-glow)' : 'var(--gold-glow)'}; font-family:var(--font-mono);">
                            ${isOwned ? 'OWNED' : `🪙 ${s.cost}`}
                        </span>
                    </div>
                    <div class="ship-perk">${s.perk}</div>
                    <p style="font-size:10px; color:#8be5ff; line-height:1.35;">${s.desc}</p>
                    <button class="btn-card-action ${isEquipped ? 'equipped' : ''}">
                        ${isEquipped ? 'EQUIPPED' : (isOwned ? 'EQUIP SHIP' : `UNLOCK [🪙 ${s.cost}]`)}
                    </button>
                `;

                const btn = card.querySelector('.btn-card-action');
                btn.onclick = () => {
                    if (isOwned) {
                        gameState.activeShip = s.id;
                        buildSpaceship(s.id);
                        saveGame();
                        populateShipsGrid();
                        sound.playLaneSwitch();
                    } else if (gameState.coins >= s.cost) {
                        gameState.coins -= s.cost;
                        gameState.unlockedShips.push(s.id);
                        gameState.activeShip = s.id;
                        buildSpaceship(s.id);
                        saveGame();
                        populateShipsGrid();
                        sound.playPowerup();
                    } else {
                        sound.playCrash();
                    }
                };

                grid.appendChild(card);
            });
        }

        // Upgrades Modal Setup
        const upgradesModal = document.getElementById('upgradesModal');
        document.getElementById('btnOpenUpgrades').onclick = () => {
            populateUpgradesList();
            upgradesModal.classList.add('active');
            sound.playLaneSwitch();
        };
        document.getElementById('closeUpgradesModal').onclick = () => upgradesModal.classList.remove('active');

        function populateUpgradesList() {
            const list = document.getElementById('upgradesList');
            list.innerHTML = '';
            const upgData = [
                { id: 'boost', name: 'Warp Boost Engines', icon: '⚡', desc: 'Increases speed boost duration and invincible barrier power.' },
                { id: 'shield', name: 'Shield Deflector Matrix', icon: '🛡', desc: 'Prolongs forcefield duration and resilience against impacts.' },
                { id: 'magnet', name: 'Magnetic Quantum Tether', icon: '🧲', desc: 'Widens coin attraction tractor beam radius across all lanes.' },
                { id: 'double', name: 'Hyper Score Multiplier', icon: '2️⃣', desc: 'Extends 2X double score bonus duration.' }
            ];

            upgData.forEach(u => {
                const curLvl = gameState.upgrades[u.id] || 1;
                const cost = curLvl * 350;
                const isMax = (curLvl >= 5);

                const item = document.createElement('div');
                item.className = 'upgrade-item';
                item.innerHTML = `
                    <div class="upgrade-info">
                        <div class="upgrade-icon">${u.icon}</div>
                        <div class="upgrade-meta">
                            <h4>${u.name.toUpperCase()}</h4>
                            <p>${u.desc}</p>
                            <div class="upgrade-pips">
                                ${[1, 2, 3, 4, 5].map(i => `<div class="upgrade-pip ${i <= curLvl ? 'filled' : ''}"></div>`).join('')}
                            </div>
                        </div>
                    </div>
                    <button class="btn-card-action" style="min-width:110px;">
                        ${isMax ? 'MAX LEVEL' : `UPGRADE [🪙 ${cost}]`}
                    </button>
                `;

                const btn = item.querySelector('.btn-card-action');
                if (!isMax) {
                    btn.onclick = () => {
                        if (gameState.coins >= cost) {
                            gameState.coins -= cost;
                            gameState.upgrades[u.id] = curLvl + 1;
                            saveGame();
                            populateUpgradesList();
                            sound.playPowerup();
                        } else {
                            sound.playCrash();
                        }
                    };
                }

                list.appendChild(item);
            });
        }

        // Missions & Achievements Modals
        const missionsModal = document.getElementById('missionsModal');
        document.getElementById('btnOpenMissions').onclick = () => {
            const list = document.getElementById('missionsList');
            list.innerHTML = '';
            gameState.missions.forEach(m => {
                const item = document.createElement('div');
                item.className = `mission-card ${m.completed ? 'completed' : ''}`;
                item.innerHTML = `
                    <div class="mission-meta">
                        <h4>${m.title}</h4>
                        <div style="font-size:10px; color:#8be5ff; font-family:var(--font-mono); margin-top:2px;">
                            PROGRESS: ${m.current} / ${m.target}
                        </div>
                        <div class="mission-reward">★ REWARD: +${m.rewardCoins} COINS // +${m.rewardXp} XP</div>
                    </div>
                    <span style="font-size:11px; font-weight:800; font-family:var(--font-mono); color:${m.completed ? 'var(--green-glow)' : 'var(--cyan-glow)'};">
                        ${m.completed ? '✓ COMPLETED' : 'IN PROGRESS'}
                    </span>
                `;
                list.appendChild(item);
            });
            missionsModal.classList.add('active');
            sound.playLaneSwitch();
        };
        document.getElementById('closeMissionsModal').onclick = () => missionsModal.classList.remove('active');

        const achievementsModal = document.getElementById('achievementsModal');
        document.getElementById('btnOpenAchievements').onclick = () => {
            const list = document.getElementById('achievementsList');
            list.innerHTML = '';
            gameState.achievements.forEach(a => {
                const item = document.createElement('div');
                item.className = `mission-card ${a.unlocked ? 'completed' : ''}`;
                item.innerHTML = `
                    <div class="mission-meta">
                        <h4>${a.title}</h4>
                        <p style="font-size:10px; color:#8be5ff; margin-top:2px;">${a.desc}</p>
                    </div>
                    <span style="font-size:12px; font-weight:900; color:${a.unlocked ? 'var(--green-glow)' : '#667788'};">
                        ${a.unlocked ? '🏆 UNLOCKED' : '🔒 LOCKED'}
                    </span>
                `;
                list.appendChild(item);
            });
            achievementsModal.classList.add('active');
            sound.playLaneSwitch();
        };
        document.getElementById('closeAchievementsModal').onclick = () => achievementsModal.classList.remove('active');

        // Daily Reward System
        document.getElementById('btnDailyReward').onclick = () => {
            const now = Date.now();
            const oneDay = 24 * 60 * 60 * 1000;
            if (now - gameState.lastDailyClaim > oneDay) {
                const bonusCoins = 150 * gameState.dailyStreak;
                gameState.coins += bonusCoins;
                addXP(250);
                gameState.dailyStreak = (gameState.dailyStreak % 7) + 1;
                gameState.lastDailyClaim = now;
                saveGame();
                showScienceToast("🎁 DAILY REWARD CLAIMED!", `Streak Day ${gameState.dailyStreak}: Received +${bonusCoins} Coins & +250 XP!`);
                sound.playPowerup();
            } else {
                showScienceToast("⏳ ALREADY CLAIMED", "Next daily bonus supply available in less than 24 hours!");
                sound.playLaneSwitch();
            }
        };

        // Audio Toggle
        function toggleAudio() {
            sound.init();
            sound.enabled = !sound.enabled;
            const icon = sound.enabled ? "🔊" : "🔇";
            document.getElementById('menuAudioBtn').textContent = icon;
            document.getElementById('inGameAudioBtn').textContent = icon;
        }
        document.getElementById('menuAudioBtn').onclick = toggleAudio;
        document.getElementById('inGameAudioBtn').onclick = toggleAudio;

        /* -------------------------------------------------------------
           MAIN THREE.JS RENDER LOOP
           ------------------------------------------------------------- */
        let frameCount = 0;

        function animate(timestamp) {
            requestAnimationFrame(animate);

            const delta = Math.min(clock.getDelta(), 0.05);
            frameCount++;

            // Celestial rotation & starfield movement
            starField.rotation.y += 0.0001;
            if (backgroundPlanetMesh) {
                backgroundPlanetMesh.rotation.y += 0.0004;
            }

            // In Menu Mode: Gently hover and turn active ship in the hangar
            if (!isGameRunning) {
                shipGroup.position.set(0, 0, 0);
                shipVisual.rotation.y = Math.sin(timestamp * 0.001) * 0.45;
                shipVisual.rotation.x = Math.sin(timestamp * 0.0015) * 0.12;
                camera.position.set(0, 1.8, 6.5);
                camera.lookAt(0, 0.2, 0);

                if (flameMeshL) flameMeshL.scale.set(0.4, 0.5, 0.4);
                if (flameMeshR) flameMeshR.scale.set(0.4, 0.5, 0.4);

                renderer.render(scene, camera);
                return;
            }

            // Runner Active Gameplay
            if (!isPaused) {
                // Update Powerup Durations
                let activePowerupCount = 0;
                Object.keys(activePowerups).forEach(pKey => {
                    if (activePowerups[pKey] > 0) {
                        activePowerups[pKey] = Math.max(0, activePowerups[pKey] - delta);
                        activePowerupCount++;
                    }
                });
                if (frameCount % 6 === 0) renderActivePowerupsHUD();

                // Speed calculation
                const isBoost = activePowerups.boost > 0;
                const effectiveSpeed = runSpeed * (isBoost ? 1.8 : 1.0);
                runDistance += effectiveSpeed * delta;

                // Gradual difficulty speed ramp
                runSpeed = Math.min(runSpeed + delta * 0.25, 95.0);

                // Score increment
                const scoreMult = (activePowerups.double > 0 ? 2.0 : 1.0) * (gameState.activeShip === 'quantum' ? 1.25 : 1.0);
                runScore += effectiveSpeed * delta * 1.5 * scoreMult;

                // Move ship forward along Z-axis
                shipGroup.position.z -= effectiveSpeed * delta;

                // Lane X Interpolation with Dynamic Banking Roll
                const targetX = LANES_X[targetLane];
                shipGroup.position.x = THREE.MathUtils.lerp(shipGroup.position.x, targetX, delta * 14.0);
                const laneDeltaX = targetX - shipGroup.position.x;
                shipVisual.rotation.z = -laneDeltaX * 0.28;

                // Vertical Jump / Dive Y Interpolation with Pitch
                verticalY = THREE.MathUtils.lerp(verticalY, targetVerticalY, delta * 12.0);
                shipGroup.position.y = verticalY;
                shipVisual.rotation.x = -(targetVerticalY - verticalY) * 0.18;

                // Engine flame scale
                const flameScale = isBoost ? 2.2 : 1.2;
                if (flameMeshL) flameMeshL.scale.set(flameScale, flameScale * 1.5, flameScale);
                if (flameMeshR) flameMeshR.scale.set(flameScale, flameScale * 1.5, flameScale);

                // Shield Bubble Visual
                const hasShield = (activePowerups.shield > 0 || isBoost);
                shieldMesh.visible = hasShield;
                if (hasShield) {
                    shieldMesh.rotation.y += 0.04;
                    shieldMesh.rotation.x += 0.02;
                    shieldMat.opacity = 0.5 + Math.sin(timestamp * 0.008) * 0.25;
                }

                // Smooth 3rd-Person Chase Camera
                const camTargetX = shipGroup.position.x * 0.45;
                const camTargetY = shipGroup.position.y * 0.45 + 3.8;
                const camTargetZ = shipGroup.position.z + 10.5;

                camera.position.x = THREE.MathUtils.lerp(camera.position.x, camTargetX, delta * 10.0);
                camera.position.y = THREE.MathUtils.lerp(camera.position.y, camTargetY, delta * 10.0);
                camera.position.z = camTargetZ;
                camera.lookAt(shipGroup.position.x * 0.8, shipGroup.position.y * 0.8 + 0.6, shipGroup.position.z - 20);

                // Dynamic FOV scaling on boost
                camera.fov = THREE.MathUtils.lerp(camera.fov, isBoost ? 78 : 65, delta * 6.0);
                camera.updateProjectionMatrix();

                // Spawner Progression
                if (shipGroup.position.z - 120 < nextSpawnZ) {
                    spawnTrackChunk(nextSpawnZ);
                    nextSpawnZ -= CHUNK_INTERVAL;
                }

                // Magnet Attraction
                const magnetRadius = (activePowerups.magnet > 0) ? (22.0 * (SHIPS_DATA[gameState.activeShip]?.magnetBonus || 1.0)) : 0;

                // Collectibles Collision & Magnetism
                for (let i = activeCollectibles.length - 1; i >= 0; i--) {
                    const cObj = activeCollectibles[i];

                    // Spin collectible
                    cObj.rotation.y += 0.04;

                    const distToShip = shipGroup.position.distanceTo(cObj.position);

                    // Magnet pull
                    if (magnetRadius > 0 && distToShip < magnetRadius && cObj.userData.type === 'coin') {
                        cObj.position.lerp(shipGroup.position, delta * 12.0);
                    }

                    // Collision check
                    if (distToShip < 2.0 && !cObj.userData.collected) {
                        cObj.userData.collected = true;
                        scene.remove(cObj);
                        activeCollectibles.splice(i, 1);

                        if (cObj.userData.type === 'coin') {
                            runCoins++;
                            runScore += 25 * scoreMult;
                            sound.playCoin();
                            trackMissionProgress('m_coins', 1);
                        } else if (cObj.userData.powerupType) {
                            activatePowerup(cObj.userData.powerupType, 6.0);
                        }
                        continue;
                    }

                    // Despawn behind ship
                    if (cObj.position.z > shipGroup.position.z + 25) {
                        scene.remove(cObj);
                        activeCollectibles.splice(i, 1);
                    }
                }

                // Obstacles Collision Detection
                for (let i = activeObstacles.length - 1; i >= 0; i--) {
                    const oObj = activeObstacles[i];

                    // Rotate obstacle
                    if (oObj.userData.rotSpeed) oObj.rotation.y += oObj.userData.rotSpeed;
                    if (oObj.userData.rotZ) oObj.rotation.z += oObj.userData.rotZ;

                    const dz = Math.abs(oObj.position.z - shipGroup.position.z);
                    const dx = Math.abs(oObj.position.x - shipGroup.position.x);

                    // Energy Gate Pass check
                    if (oObj.userData.type === 'gate' && dz < 2.0 && !oObj.userData.passed) {
                        oObj.userData.passed = true;
                        runScore += 150 * scoreMult;
                        sound.playCoin();
                        trackMissionProgress('m_gates', 1);
                    }

                    // Collision check
                    if (dz < 2.2) {
                        let hit = false;

                        if (oObj.userData.type === 'asteroid') {
                            if (dx < 1.6 && Math.abs(oObj.position.y - shipGroup.position.y) < 1.6) hit = true;
                        } else if (oObj.userData.type === 'rot_debris') {
                            if (dx < 2.8 && Math.abs(oObj.position.y - shipGroup.position.y) < 1.4) hit = true;
                        } else if (oObj.userData.type === 'laser') {
                            if (oObj.userData.isHigh) {
                                // High laser: only hits if NOT diving
                                if (shipGroup.position.y > 0.4) hit = true;
                            } else {
                                // Low laser: only hits if NOT jumping
                                if (shipGroup.position.y < 2.4) hit = true;
                            }
                        }

                        if (hit) {
                            if (isBoost) {
                                // Smashes obstacle during boost!
                                scene.remove(oObj);
                                activeObstacles.splice(i, 1);
                                runScore += 200 * scoreMult;
                                sound.playShieldDeflect();
                                continue;
                            } else if (activePowerups.shield > 0) {
                                // Shield absorbs hit
                                activePowerups.shield = 0;
                                sound.playShieldDeflect();
                                scene.remove(oObj);
                                activeObstacles.splice(i, 1);
                                renderActivePowerupsHUD();
                                continue;
                            } else {
                                // Take damage!
                                runShieldPips--;
                                updateShieldPipsUI();
                                sound.playCrash();
                                scene.remove(oObj);
                                activeObstacles.splice(i, 1);

                                if (runShieldPips <= 0) {
                                    endRun("CRITICAL HULL BREACH // IMPACT DETECTED");
                                    return;
                                }
                                continue;
                            }
                        }
                    }

                    // Despawn behind ship
                    if (oObj.position.z > shipGroup.position.z + 25) {
                        scene.remove(oObj);
                        activeObstacles.splice(i, 1);
                    }
                }

                // Random Science Fact Interval (every 22 seconds)
                if (performance.now() - lastScienceFactTime > 22000) {
                    lastScienceFactTime = performance.now();
                    triggerRandomScienceFact();
                }

                // Track missions
                trackMissionProgress('m_dist', Math.round(effectiveSpeed * delta));

                // Update HUD Numbers
                document.getElementById('hudScoreVal').textContent = Math.round(runScore).toLocaleString();
                document.getElementById('hudDistanceVal').textContent = Math.round(runDistance).toLocaleString();
                document.getElementById('hudCoinVal').textContent = runCoins.toLocaleString();

                sound.updateEngine(effectiveSpeed / 95.0);
            }

            renderer.render(scene, camera);
        }

        animate(performance.now());

        // Responsive Resizing
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

    </script>
</body>

</html>
'''

if __name__ == '__main__':
    content = generate_html()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully generated Space Runner 3D in index.html ({len(content)} bytes)")
