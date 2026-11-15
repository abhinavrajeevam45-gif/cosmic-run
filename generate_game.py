#!/usr/bin/env python3
"""
Generator script for COSMIC QUEST 3D - Upgraded Space Exploration & Planet Landing Simulator.
Produces the comprehensive, fully-functional index.html.
"""

import os

html_content = r'''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>COSMIC QUEST - 3D NASA Interplanetary Flight Simulator</title>

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
            --cyan-dim: #0099b8;
            --amber-warn: #ffaa00;
            --red-alert: #ff3344;
            --green-ok: #00ffaa;
            --purple-accent: #a855f7;
            --gold-accent: #facc15;
            --panel-bg: rgba(3, 12, 26, 0.78);
            --panel-border: rgba(0, 240, 255, 0.32);
            --font-mono: "SF Mono", "Consolas", "Courier New", monospace;
            --font-ui: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
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
           START / TITLE SCREEN OVERLAY
           ------------------------------------------------------------- */
        #startScreen {
            position: fixed;
            inset: 0;
            z-index: 100;
            background: radial-gradient(circle at center, rgba(3, 16, 36, 0.88) 0%, rgba(1, 6, 14, 0.96) 80%);
            backdrop-filter: blur(14px);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            transition: opacity 0.5s ease, visibility 0.5s ease;
            pointer-events: auto;
            overflow-y: auto;
        }

        #startScreen.hidden {
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
        }

        .title-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 240, 255, 0.12);
            border: 1px solid rgba(0, 240, 255, 0.4);
            padding: 4px 14px;
            border-radius: 20px;
            color: var(--cyan-glow);
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }

        .title-badge .nasa-tag {
            background: linear-gradient(135deg, #0b3d91, #fc3d21);
            color: #ffffff;
            font-size: 9px;
            padding: 1px 7px;
            border-radius: 3px;
            font-weight: 900;
        }

        .title-main {
            font-size: clamp(28px, 4.5vw, 52px);
            font-weight: 900;
            letter-spacing: 6px;
            color: #ffffff;
            text-shadow: 0 0 30px rgba(0, 240, 255, 0.8), 0 0 60px rgba(0, 240, 255, 0.3);
            margin-bottom: 4px;
            text-align: center;
        }

        .title-sub {
            font-size: clamp(11px, 1.4vw, 14px);
            color: #8be5ff;
            letter-spacing: 2.5px;
            margin-bottom: 22px;
            text-align: center;
            font-family: var(--font-mono);
        }

        .dest-card-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
            margin-bottom: 24px;
            max-width: 960px;
            width: 100%;
        }

        @media (max-width: 860px) {
            .dest-card-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        @media (max-width: 540px) {
            .dest-card-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .dest-card {
            background: rgba(4, 20, 42, 0.7);
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 8px;
            padding: 10px 8px;
            cursor: pointer;
            transition: all 0.22s ease;
            text-align: center;
            backdrop-filter: blur(8px);
        }

        .dest-card:hover {
            border-color: var(--cyan-glow);
            background: rgba(0, 240, 255, 0.18);
            transform: translateY(-2px);
            box-shadow: 0 0 16px rgba(0, 240, 255, 0.4);
        }

        .dest-card.selected {
            border-color: var(--cyan-glow);
            background: rgba(0, 240, 255, 0.28);
            box-shadow: 0 0 22px rgba(0, 240, 255, 0.6);
        }

        .dest-card .dest-icon {
            font-size: 22px;
            margin-bottom: 4px;
        }

        .dest-card .dest-name {
            font-size: 11.5px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 1px;
        }

        .dest-card .dest-dist {
            font-size: 9.5px;
            color: #8be5ff;
            font-family: var(--font-mono);
            margin-top: 2px;
        }

        .btn-play-mission {
            background: linear-gradient(135deg, #00f0ff, #0099bb);
            color: #01121e;
            font-size: 15px;
            font-weight: 900;
            letter-spacing: 2.5px;
            padding: 13px 36px;
            border-radius: 6px;
            border: 1px solid #ffffff;
            cursor: pointer;
            box-shadow: 0 0 28px rgba(0, 240, 255, 0.6), inset 0 0 10px rgba(255, 255, 255, 0.4);
            transition: all 0.25s ease;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }

        .btn-play-mission:hover {
            background: #ffffff;
            color: #001f33;
            box-shadow: 0 0 45px rgba(0, 240, 255, 0.95);
            transform: scale(1.03);
        }

        .start-manual-hint {
            margin-top: 18px;
            font-size: 11px;
            color: #72a4be;
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
            justify-content: center;
            font-family: var(--font-mono);
        }

        .start-manual-hint span {
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        .start-manual-hint kbd {
            background: rgba(0, 240, 255, 0.15);
            border: 1px solid rgba(0, 240, 255, 0.4);
            color: var(--cyan-glow);
            padding: 2px 6px;
            border-radius: 3px;
        }

        /* -------------------------------------------------------------
           IN-GAME MINIMALIST AAA HUD
           ------------------------------------------------------------- */
        #hud {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 10;
            transition: opacity 0.3s ease;
        }

        #hud.hud-hidden {
            opacity: 0;
            pointer-events: none;
        }

        .topbar {
            position: absolute;
            top: 10px;
            left: 12px;
            right: 12px;
            height: 44px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-radius: 8px;
            padding: 0 10px;
            backdrop-filter: blur(12px);
            pointer-events: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }

        .top-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo {
            color: var(--cyan-glow);
            font-size: 14px;
            font-weight: 800;
            letter-spacing: 1.8px;
            text-shadow: 0 0 12px rgba(0, 240, 255, 0.7);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .target-pill {
            display: flex;
            align-items: center;
            gap: 6px;
            background: rgba(0, 240, 255, 0.12);
            border: 1px solid rgba(0, 240, 255, 0.35);
            padding: 3px 10px;
            border-radius: 14px;
            font-size: 11px;
            font-family: var(--font-mono);
            color: #d0f4ff;
        }

        .target-pill strong {
            color: var(--cyan-glow);
        }

        .score-pill {
            display: flex;
            align-items: center;
            gap: 5px;
            background: rgba(250, 204, 21, 0.12);
            border: 1px solid rgba(250, 204, 21, 0.4);
            padding: 3px 9px;
            border-radius: 14px;
            font-size: 11px;
            font-family: var(--font-mono);
            color: var(--gold-accent);
            font-weight: 700;
        }

        .nasa-ticker {
            font-family: var(--font-mono);
            font-size: 10px;
            letter-spacing: 0.8px;
            color: #8be5ff;
            background: rgba(11, 61, 145, 0.4);
            border: 1px solid rgba(0, 240, 255, 0.3);
            padding: 3px 8px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .nasa-ticker .dot {
            width: 6px;
            height: 6px;
            background: #00ffaa;
            border-radius: 50%;
            box-shadow: 0 0 6px #00ffaa;
            animation: pulse-dot 1.2s infinite alternate;
        }

        @keyframes pulse-dot {
            from { opacity: 0.4; }
            to { opacity: 1; }
        }

        .top-right {
            display: flex;
            align-items: center;
            gap: 5px;
        }

        /* Camera Switcher Button Group */
        .camera-btn-group {
            display: flex;
            background: rgba(2, 10, 22, 0.7);
            border: 1px solid rgba(0, 240, 255, 0.35);
            border-radius: 6px;
            overflow: hidden;
            margin-right: 2px;
        }

        .cam-mode-btn {
            background: transparent;
            border: none;
            color: #8be5ff;
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 0.8px;
            padding: 5px 9px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-family: var(--font-ui);
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .cam-mode-btn:hover {
            background: rgba(0, 240, 255, 0.2);
            color: #ffffff;
        }

        .cam-mode-btn.active {
            background: var(--cyan-glow);
            color: #011422;
            box-shadow: 0 0 10px var(--cyan-glow);
        }

        .hud-btn {
            background: rgba(4, 24, 48, 0.8);
            border: 1px solid rgba(0, 240, 255, 0.35);
            color: var(--cyan-glow);
            font-size: 10.5px;
            font-weight: 700;
            letter-spacing: 0.8px;
            padding: 5px 9px;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 4px;
            font-family: var(--font-ui);
        }

        .hud-btn:hover {
            background: var(--cyan-glow);
            color: #011422;
            border-color: #ffffff;
            box-shadow: 0 0 14px var(--cyan-glow);
        }

        .hud-btn.active {
            background: rgba(0, 240, 255, 0.3);
            border-color: var(--cyan-glow);
            color: #ffffff;
            box-shadow: 0 0 12px rgba(0, 240, 255, 0.4);
        }

        .hud-btn.accent-btn {
            background: linear-gradient(135deg, rgba(0, 240, 255, 0.25), rgba(0, 153, 184, 0.35));
            border-color: var(--cyan-glow);
            font-weight: 800;
        }

        .hud-btn.land-btn {
            background: linear-gradient(135deg, rgba(0, 255, 170, 0.25), rgba(0, 180, 120, 0.35));
            border-color: var(--green-ok);
            color: var(--green-ok);
            font-weight: 800;
        }
        .hud-btn.land-btn:hover {
            background: var(--green-ok);
            color: #011422;
            box-shadow: 0 0 16px var(--green-ok);
        }

        /* Sleek Left Telemetry Bracket (Bottom-Left) */
        .hud-bracket-left {
            position: absolute;
            bottom: 44px;
            left: 14px;
            width: 215px;
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-left: 3px solid var(--cyan-glow);
            border-radius: 6px;
            padding: 11px 13px;
            backdrop-filter: blur(12px);
            pointer-events: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }

        .bracket-header {
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 1.5px;
            color: var(--cyan-glow);
            margin-bottom: 7px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(0, 240, 255, 0.18);
            padding-bottom: 4px;
        }

        .speed-hero {
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            margin-bottom: 3px;
        }

        .speed-number {
            font-size: 26px;
            font-weight: 900;
            font-family: var(--font-mono);
            color: #ffffff;
            text-shadow: 0 0 14px rgba(0, 240, 255, 0.6);
        }

        .speed-unit {
            font-size: 10px;
            color: #8be5ff;
            letter-spacing: 1px;
            font-family: var(--font-mono);
        }

        .mini-stat {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 10.5px;
            color: #b0d8eb;
            margin: 5px 0;
            font-family: var(--font-mono);
        }

        .mini-stat .val {
            color: var(--cyan-glow);
            font-weight: 700;
        }

        .hud-bar {
            height: 4px;
            background: #091a2c;
            border-radius: 2px;
            overflow: hidden;
            margin-top: 3px;
            border: 1px solid rgba(0, 240, 255, 0.2);
        }

        .hud-bar .fill {
            height: 100%;
            background: linear-gradient(90deg, #0099bb, var(--cyan-glow));
            box-shadow: 0 0 8px var(--cyan-glow);
            transition: width 0.15s ease-out;
        }

        .hud-bar .fill.warn {
            background: linear-gradient(90deg, #bb6600, var(--amber-warn));
            box-shadow: 0 0 8px var(--amber-warn);
        }

        .hud-bar .fill.alert {
            background: linear-gradient(90deg, #bb0022, var(--red-alert));
            box-shadow: 0 0 8px var(--red-alert);
        }

        /* Sleek Right Mission & Life Support Bracket (Bottom-Right) */
        .hud-bracket-right {
            position: absolute;
            bottom: 44px;
            right: 14px;
            width: 250px;
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-right: 3px solid var(--cyan-glow);
            border-radius: 6px;
            padding: 11px 13px;
            backdrop-filter: blur(12px);
            pointer-events: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }

        select.mini-select {
            width: 100%;
            background: #041426;
            border: 1px solid rgba(0, 240, 255, 0.35);
            color: var(--cyan-glow);
            font-family: var(--font-mono);
            font-size: 11px;
            padding: 5px 7px;
            border-radius: 4px;
            outline: none;
            cursor: pointer;
            margin: 4px 0 6px 0;
        }

        .btn-controls-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 5px;
            margin-top: 7px;
        }

        .btn-action {
            background: linear-gradient(180deg, #00b4c8, #007c8a);
            border: 1px solid #7effff;
            color: #00121d;
            padding: 5px 8px;
            font-weight: 800;
            font-size: 10px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s ease;
            text-align: center;
        }

        .btn-action:hover {
            background: #ffffff;
            color: #001a2b;
            box-shadow: 0 0 12px var(--cyan-glow);
        }

        .btn-action.quick-land-action {
            background: linear-gradient(180deg, #00ffaa, #00aa66);
            border-color: #aaffdd;
            color: #002214;
        }

        #missionStatus {
            font-size: 10.5px;
            font-weight: 700;
            color: var(--green-ok);
            font-family: var(--font-mono);
            margin: 3px 0;
        }

        #message {
            font-size: 10.5px;
            color: #8be0ff;
            line-height: 1.35;
            min-height: 26px;
        }

        /* -------------------------------------------------------------
           IN-WORLD 3D TARGET MARKER & SCREEN-EDGE BEARING ARROW
           ------------------------------------------------------------- */
        #navTargetMarker {
            position: fixed;
            pointer-events: none;
            z-index: 15;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            opacity: 0;
            transition: opacity 0.2s ease;
        }

        #navTargetMarker.visible {
            opacity: 1;
        }

        .nav-reticle-box {
            width: 48px;
            height: 48px;
            border: 1.5px solid var(--cyan-glow);
            position: relative;
            box-shadow: 0 0 12px rgba(0, 240, 255, 0.4);
            animation: pulse-reticle 2s infinite ease-in-out;
        }

        @keyframes pulse-reticle {
            0%, 100% { transform: scale(1); border-color: var(--cyan-glow); }
            50% { transform: scale(1.08); border-color: #ffffff; }
        }

        .nav-reticle-box::before, .nav-reticle-box::after {
            content: '';
            position: absolute;
            background: var(--cyan-glow);
        }
        .nav-reticle-box::before {
            top: 50%; left: -6px; width: 60px; height: 1px;
        }
        .nav-reticle-box::after {
            left: 50%; top: -6px; height: 60px; width: 1px;
        }

        .nav-reticle-label {
            margin-top: 6px;
            background: rgba(3, 16, 36, 0.85);
            border: 1px solid var(--cyan-glow);
            border-radius: 4px;
            padding: 2px 7px;
            font-family: var(--font-mono);
            font-size: 10px;
            color: #ffffff;
            white-space: nowrap;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
        }

        .nav-reticle-label strong {
            color: var(--cyan-glow);
        }

        /* Off-screen Bearing Indicator Arrow */
        #navBearingArrow {
            position: fixed;
            pointer-events: none;
            z-index: 15;
            display: flex;
            align-items: center;
            gap: 6px;
            transform: translate(-50%, -50%);
            opacity: 0;
            transition: opacity 0.2s ease;
        }

        #navBearingArrow.visible {
            opacity: 1;
        }

        .bearing-arrow-icon {
            width: 26px;
            height: 26px;
            background: rgba(0, 240, 255, 0.2);
            border: 1.5px solid var(--cyan-glow);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--cyan-glow);
            font-size: 14px;
            font-weight: 900;
            box-shadow: 0 0 10px var(--cyan-glow);
        }

        .bearing-label {
            background: rgba(2, 12, 28, 0.85);
            border: 1px solid var(--cyan-glow);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 9.5px;
            font-family: var(--font-mono);
            color: #8be5ff;
            white-space: nowrap;
        }

        /* Flight Reticle */
        #crosshair-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            pointer-events: none;
        }

        #crosshair {
            color: var(--cyan-glow);
            font-size: 22px;
            text-shadow: 0 0 8px cyan;
            opacity: 0.8;
            line-height: 1;
            text-align: center;
        }

        #flightReticle {
            position: absolute;
            width: 14px;
            height: 14px;
            border: 1.5px solid var(--cyan-glow);
            border-radius: 50%;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 8px cyan;
            opacity: 0;
            transition: opacity 0.2s;
        }

        #flightReticle::after {
            content: "";
            position: absolute;
            inset: 3px;
            background: cyan;
            border-radius: 50%;
        }

        #flightReticle.active {
            opacity: 0.9;
        }

        /* Bottom Controls Guide Ribbon */
        .bottom-ribbon {
            position: absolute;
            bottom: 12px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(3, 12, 26, 0.65);
            border: 1px solid rgba(0, 240, 255, 0.22);
            border-radius: 20px;
            padding: 4px 18px;
            backdrop-filter: blur(8px);
            font-size: 10px;
            color: #82b0c8;
            font-family: var(--font-mono);
            display: flex;
            align-items: center;
            gap: 12px;
            white-space: nowrap;
            pointer-events: auto;
        }

        .bottom-ribbon span kbd {
            color: var(--cyan-glow);
            background: rgba(0, 240, 255, 0.12);
            border: 1px solid rgba(0, 240, 255, 0.35);
            padding: 1px 4px;
            border-radius: 3px;
        }

        /* Alert Notification Banner */
        #alertBanner {
            position: absolute;
            top: 66px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(220, 20, 40, 0.9);
            border: 1px solid #ff5566;
            color: #ffffff;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 2px;
            padding: 5px 16px;
            border-radius: 4px;
            box-shadow: 0 0 20px rgba(255, 30, 60, 0.6);
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
            z-index: 20;
        }

        #alertBanner.show {
            opacity: 1;
            animation: pulse-alert 0.7s infinite alternate;
        }

        @keyframes pulse-alert {
            from { opacity: 0.6; }
            to { opacity: 1; }
        }

        /* Toast notification for mission tasks */
        #toastNotice {
            position: absolute;
            top: 66px;
            right: 20px;
            background: rgba(4, 28, 54, 0.92);
            border: 1px solid var(--cyan-glow);
            border-left: 4px solid var(--green-ok);
            color: #ffffff;
            font-size: 11px;
            font-family: var(--font-mono);
            padding: 8px 14px;
            border-radius: 4px;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
            opacity: 0;
            transform: translateY(-10px);
            transition: all 0.3s ease;
            pointer-events: none;
            z-index: 25;
        }

        #toastNotice.show {
            opacity: 1;
            transform: translateY(0);
        }

        /* -------------------------------------------------------------
           INTERACTIVE SOLAR SYSTEM MAP MODAL (#solarSystemMap)
           ------------------------------------------------------------- */
        #solarSystemMap {
            position: fixed;
            inset: 0;
            z-index: 90;
            background: radial-gradient(circle at center, rgba(3, 14, 32, 0.94) 0%, rgba(1, 4, 10, 0.98) 100%);
            backdrop-filter: blur(16px);
            display: flex;
            flex-direction: column;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: opacity 0.35s ease, visibility 0.35s ease;
        }

        #solarSystemMap.active {
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }

        .map-header {
            height: 52px;
            background: rgba(3, 16, 36, 0.85);
            border-bottom: 1px solid var(--panel-border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
        }

        .map-title {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 15px;
            font-weight: 900;
            letter-spacing: 2.5px;
            color: #ffffff;
        }

        .map-title .badge {
            font-size: 10px;
            background: rgba(0, 240, 255, 0.15);
            border: 1px solid rgba(0, 240, 255, 0.4);
            color: var(--cyan-glow);
            padding: 2px 8px;
            border-radius: 10px;
            letter-spacing: 1px;
            font-family: var(--font-mono);
        }

        .map-body {
            flex: 1;
            display: flex;
            position: relative;
            overflow: hidden;
        }

        .map-canvas-container {
            flex: 1;
            position: relative;
            height: 100%;
        }

        #solarMapCanvas {
            width: 100%;
            height: 100%;
            display: block;
            cursor: grab;
        }

        #solarMapCanvas:active {
            cursor: grabbing;
        }

        /* Map Controls Toolbar */
        .map-toolbar {
            position: absolute;
            bottom: 20px;
            left: 20px;
            display: flex;
            gap: 6px;
            background: rgba(3, 16, 36, 0.85);
            border: 1px solid var(--panel-border);
            border-radius: 6px;
            padding: 6px;
            backdrop-filter: blur(8px);
        }

        .map-tool-btn {
            background: rgba(4, 24, 48, 0.8);
            border: 1px solid rgba(0, 240, 255, 0.3);
            color: var(--cyan-glow);
            font-size: 11px;
            font-weight: 700;
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-family: var(--font-mono);
        }

        .map-tool-btn:hover {
            background: var(--cyan-glow);
            color: #011422;
        }

        /* Map Planet Sidebar */
        .map-sidebar {
            width: 320px;
            background: rgba(3, 14, 30, 0.9);
            border-left: 1px solid var(--panel-border);
            padding: 20px;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            backdrop-filter: blur(12px);
        }

        .map-planet-preview {
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 16px;
            padding-bottom: 14px;
            border-bottom: 1px solid rgba(0, 240, 255, 0.2);
        }

        .planet-preview-glyph {
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: radial-gradient(circle at 35% 35%, #00f0ff, #003366);
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.6);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }

        .planet-preview-meta h3 {
            font-size: 18px;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 2px;
        }

        .planet-preview-meta .class-tag {
            font-size: 10px;
            color: #8be5ff;
            font-family: var(--font-mono);
            letter-spacing: 1px;
        }

        .map-spec-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 8px;
            margin-bottom: 16px;
        }

        .map-spec-item {
            background: rgba(0, 240, 255, 0.06);
            border: 1px solid rgba(0, 240, 255, 0.15);
            border-radius: 4px;
            padding: 7px 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: var(--font-mono);
            font-size: 11px;
        }

        .map-spec-item span:first-child {
            color: #7ab3cc;
        }

        .map-spec-item span:last-child {
            color: #ffffff;
            font-weight: 700;
        }

        .map-description {
            font-size: 11px;
            line-height: 1.5;
            color: #9bd5ff;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(0, 240, 255, 0.15);
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 16px;
            font-family: var(--font-ui);
        }

        .map-action-stack {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-top: auto;
        }

        .map-action-btn {
            background: linear-gradient(135deg, #00b4c8, #007c8a);
            border: 1px solid #7effff;
            color: #00121d;
            font-weight: 800;
            font-size: 11.5px;
            letter-spacing: 1.5px;
            padding: 10px 14px;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.2s ease;
            text-align: center;
        }

        .map-action-btn:hover {
            background: #ffffff;
            color: #001a2b;
            box-shadow: 0 0 16px var(--cyan-glow);
        }

        .map-action-btn.green {
            background: linear-gradient(135deg, #00ffaa, #00aa66);
            border-color: #aaffdd;
            color: #002414;
        }

        .map-action-btn.secondary {
            background: rgba(4, 24, 48, 0.8);
            border: 1px solid rgba(0, 240, 255, 0.4);
            color: var(--cyan-glow);
        }

        /* -------------------------------------------------------------
           QUICK PLANET LANDING CINEMATIC OVERLAY (#landingCinematicOverlay)
           ------------------------------------------------------------- */
        #landingCinematicOverlay {
            position: fixed;
            inset: 0;
            z-index: 110;
            background: #010612;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: opacity 0.4s ease, visibility 0.4s ease;
        }

        #landingCinematicOverlay.active {
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }

        canvas#landingVFXCanvas {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }

        .landing-telemetry-hud {
            position: relative;
            z-index: 2;
            background: rgba(3, 16, 36, 0.88);
            border: 1.5px solid var(--cyan-glow);
            box-shadow: 0 0 40px rgba(0, 240, 255, 0.5);
            border-radius: 10px;
            padding: 26px 36px;
            max-width: 520px;
            width: 90%;
            text-align: center;
            backdrop-filter: blur(16px);
        }

        .landing-title {
            font-size: 22px;
            font-weight: 900;
            letter-spacing: 3px;
            color: #ffffff;
            text-shadow: 0 0 16px var(--cyan-glow);
            margin-bottom: 6px;
        }

        .landing-phase-tag {
            font-size: 11px;
            color: var(--green-ok);
            letter-spacing: 2px;
            font-family: var(--font-mono);
            font-weight: 700;
            margin-bottom: 16px;
        }

        .landing-readout-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 16px 0;
        }

        .landing-metric-box {
            background: rgba(0, 240, 255, 0.08);
            border: 1px solid rgba(0, 240, 255, 0.25);
            border-radius: 6px;
            padding: 10px;
            text-align: center;
        }

        .landing-metric-box .label {
            font-size: 9.5px;
            color: #7ecae6;
            letter-spacing: 1px;
            font-family: var(--font-mono);
        }

        .landing-metric-box .num {
            font-size: 20px;
            font-weight: 900;
            color: #ffffff;
            font-family: var(--font-mono);
            margin-top: 2px;
        }

        .landing-progress-bar {
            height: 6px;
            background: #041424;
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 3px;
            overflow: hidden;
            margin-top: 14px;
        }

        .landing-progress-fill {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, #0099bb, var(--green-ok));
            box-shadow: 0 0 12px var(--green-ok);
            transition: width 0.1s linear;
        }

        .landing-btn-abort {
            margin-top: 18px;
            background: rgba(220, 20, 40, 0.25);
            border: 1px solid #ff4455;
            color: #ff8899;
            font-size: 10.5px;
            font-weight: 800;
            letter-spacing: 1.5px;
            padding: 7px 18px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-family: var(--font-mono);
        }

        .landing-btn-abort:hover {
            background: #ff3344;
            color: #ffffff;
        }

        /* -------------------------------------------------------------
           SURFACE EXPLORATION VIEW (#surfaceExplorationView)
           ------------------------------------------------------------- */
        #surfaceExplorationView {
            position: fixed;
            inset: 0;
            z-index: 105;
            background: #01040a;
            display: flex;
            flex-direction: column;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: opacity 0.4s ease, visibility 0.4s ease;
        }

        #surfaceExplorationView.active {
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }

        canvas#surfaceCanvas {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            display: block;
            z-index: 1;
        }

        .surface-hud-overlay {
            position: absolute;
            inset: 0;
            z-index: 2;
            pointer-events: none;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 18px 24px;
        }

        .surface-top-row {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            pointer-events: auto;
        }

        .surface-banner {
            background: rgba(3, 16, 36, 0.85);
            border: 1px solid var(--panel-border);
            border-left: 4px solid var(--green-ok);
            border-radius: 6px;
            padding: 12px 18px;
            backdrop-filter: blur(12px);
        }

        .surface-banner h2 {
            font-size: 20px;
            font-weight: 900;
            letter-spacing: 3px;
            color: #ffffff;
            text-shadow: 0 0 14px var(--green-ok);
        }

        .surface-banner .surface-sub {
            font-size: 11px;
            color: #8be5ff;
            font-family: var(--font-mono);
            letter-spacing: 1px;
            margin-top: 3px;
        }

        .surface-tasks-card {
            background: rgba(3, 16, 36, 0.88);
            border: 1px solid var(--panel-border);
            border-radius: 8px;
            padding: 16px 20px;
            max-width: 440px;
            width: 100%;
            backdrop-filter: blur(14px);
            pointer-events: auto;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);
        }

        .surface-tasks-card h3 {
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 2px;
            color: var(--cyan-glow);
            margin-bottom: 10px;
            border-bottom: 1px solid rgba(0, 240, 255, 0.2);
            padding-bottom: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .surface-task-item {
            background: rgba(0, 240, 255, 0.05);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 5px;
            padding: 9px 12px;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: all 0.2s ease;
        }

        .surface-task-item:hover {
            border-color: var(--cyan-glow);
            background: rgba(0, 240, 255, 0.12);
        }

        .surface-task-info {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .surface-task-name {
            font-size: 11.5px;
            font-weight: 700;
            color: #ffffff;
        }

        .surface-task-pts {
            font-size: 9.5px;
            font-family: var(--font-mono);
            color: var(--gold-accent);
        }

        .btn-surface-action {
            background: linear-gradient(135deg, #00f0ff, #0099bb);
            color: #011422;
            border: none;
            font-weight: 800;
            font-size: 10px;
            letter-spacing: 1px;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .btn-surface-action:hover {
            background: #ffffff;
            box-shadow: 0 0 10px var(--cyan-glow);
        }

        .btn-surface-action.completed {
            background: rgba(0, 255, 170, 0.2);
            border: 1px solid var(--green-ok);
            color: var(--green-ok);
            cursor: default;
        }

        .surface-bottom-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            pointer-events: auto;
        }

        .btn-liftoff {
            background: linear-gradient(135deg, #00f0ff, #007799);
            color: #011422;
            font-size: 13px;
            font-weight: 900;
            letter-spacing: 2px;
            padding: 12px 28px;
            border-radius: 6px;
            border: 1px solid #ffffff;
            cursor: pointer;
            box-shadow: 0 0 24px rgba(0, 240, 255, 0.6);
            transition: all 0.25s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-liftoff:hover {
            background: #ffffff;
            color: #001f33;
            box-shadow: 0 0 40px rgba(0, 240, 255, 0.95);
            transform: scale(1.02);
        }

        /* -------------------------------------------------------------
           MISSION TASKS CHECKLIST DRAWER / MODAL (#missionTasksDrawer)
           ------------------------------------------------------------- */
        #missionTasksDrawer {
            position: fixed;
            top: 60px;
            right: 14px;
            width: 320px;
            background: rgba(3, 14, 30, 0.94);
            border: 1px solid var(--panel-border);
            border-radius: 8px;
            padding: 16px;
            backdrop-filter: blur(14px);
            z-index: 85;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
            display: none;
        }

        #missionTasksDrawer.show {
            display: block;
            animation: fadeInRight 0.25s ease;
        }

        @keyframes fadeInRight {
            from { opacity: 0; transform: translateX(12px); }
            to { opacity: 1; transform: translateX(0); }
        }

        .drawer-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(0, 240, 255, 0.2);
            padding-bottom: 8px;
            margin-bottom: 12px;
        }

        .drawer-header h3 {
            font-size: 12px;
            font-weight: 800;
            color: var(--cyan-glow);
            letter-spacing: 1.5px;
        }

        .drawer-close {
            background: transparent;
            border: none;
            color: #8be5ff;
            cursor: pointer;
            font-size: 14px;
            padding: 2px 6px;
        }

        .drawer-task-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
            max-height: 380px;
            overflow-y: auto;
        }

        .drawer-task-item {
            background: rgba(0, 240, 255, 0.05);
            border: 1px solid rgba(0, 240, 255, 0.15);
            border-radius: 5px;
            padding: 8px 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .drawer-task-item.completed {
            border-color: rgba(0, 255, 170, 0.4);
            background: rgba(0, 255, 170, 0.08);
        }

        .status-pill {
            font-size: 9px;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: var(--font-mono);
            font-weight: 700;
        }

        .status-pill.pending {
            background: rgba(140, 160, 180, 0.2);
            color: #8aa4ba;
        }

        .status-pill.in-progress {
            background: rgba(255, 170, 0, 0.2);
            color: var(--amber-warn);
        }

        .status-pill.completed {
            background: rgba(0, 255, 170, 0.2);
            color: var(--green-ok);
        }

        /* -------------------------------------------------------------
           MOBILE ON-SCREEN TOUCH CONTROLS
           ------------------------------------------------------------- */
        #mobileControls {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 30;
            display: none;
        }

        @media (max-width: 900px), (pointer: coarse) {
            #mobileControls {
                display: block;
            }
        }

        .mobile-dpad {
            position: absolute;
            bottom: 40px;
            left: 20px;
            width: 120px;
            height: 120px;
            pointer-events: auto;
        }

        .dpad-btn {
            position: absolute;
            width: 38px;
            height: 38px;
            background: rgba(3, 16, 36, 0.7);
            border: 1px solid rgba(0, 240, 255, 0.4);
            color: var(--cyan-glow);
            border-radius: 8px;
            font-size: 14px;
            font-weight: 900;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            touch-action: manipulation;
        }

        .dpad-btn:active {
            background: var(--cyan-glow);
            color: #011422;
        }

        .dpad-up { top: 0; left: 41px; }
        .dpad-down { bottom: 0; left: 41px; }
        .dpad-left { top: 41px; left: 0; }
        .dpad-right { top: 41px; right: 0; }

        .mobile-actions {
            position: absolute;
            bottom: 40px;
            right: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            pointer-events: auto;
        }

        .touch-action-btn {
            width: 48px;
            height: 48px;
            background: rgba(3, 16, 36, 0.75);
            border: 1.5px solid var(--cyan-glow);
            border-radius: 50%;
            color: var(--cyan-glow);
            font-size: 12px;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
            touch-action: manipulation;
        }

        .touch-action-btn:active {
            background: var(--cyan-glow);
            color: #011422;
        }

        /* Mission Accomplished Victory Modal */
        #missionCompleteModal {
            position: fixed;
            inset: 0;
            background: rgba(2, 10, 24, 0.88);
            backdrop-filter: blur(14px);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 120;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: all 0.4s ease;
        }

        #missionCompleteModal.active {
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }

        .modal-card {
            background: rgba(4, 20, 44, 0.94);
            border: 1px solid var(--cyan-glow);
            box-shadow: 0 0 40px rgba(0, 240, 255, 0.5);
            border-radius: 10px;
            padding: 30px 38px;
            text-align: center;
            max-width: 480px;
            width: 90%;
        }

        .modal-card h2 {
            font-size: 22px;
            color: #ffffff;
            letter-spacing: 3px;
            margin-bottom: 8px;
            text-shadow: 0 0 20px var(--green-ok);
        }

        .modal-card p {
            color: #9bd5ff;
            font-size: 13px;
            line-height: 1.5;
            margin-bottom: 22px;
            font-family: var(--font-mono);
        }

        @media (max-width: 900px) {
            .nasa-ticker {
                display: none;
            }
            .top-left .target-pill {
                display: none;
            }
        }

        @media (max-width: 768px) {
            .hud-bracket-left, .hud-bracket-right {
                width: 175px;
                padding: 8px 10px;
                bottom: 38px;
            }

            .bottom-ribbon {
                display: none;
            }

            .cam-mode-btn span:last-child {
                display: none;
            }

            .hud-btn span:last-child {
                display: none;
            }

            .map-sidebar {
                width: 250px;
                padding: 14px;
            }
        }
    </style>
</head>

<body>

    <canvas id="webgl"></canvas>

    <!-- 1. CINEMATIC START SCREEN -->
    <div id="startScreen">
        <div class="title-badge">
            <span class="nasa-tag">NASA</span>
            <span>DEEP SPACE EXPLORATION PROGRAM</span>
        </div>
        <div class="title-main">COSMIC QUEST</div>
        <div class="title-sub">SOLAR SYSTEM EXPLORATION & PLANET LANDING SIMULATOR</div>

        <div class="dest-card-grid" id="destGrid">
            <!-- Dynamically populated or initial 10 celestial bodies -->
            <div class="dest-card selected" data-target="Moon">
                <div class="dest-icon">🌕</div>
                <div class="dest-name">MOON</div>
                <div class="dest-dist">384,400 KM</div>
            </div>
            <div class="dest-card" data-target="Earth">
                <div class="dest-icon">🌍</div>
                <div class="dest-name">EARTH</div>
                <div class="dest-dist">LOW ORBIT</div>
            </div>
            <div class="dest-card" data-target="Mars">
                <div class="dest-icon">🔴</div>
                <div class="dest-name">MARS</div>
                <div class="dest-dist">225M KM</div>
            </div>
            <div class="dest-card" data-target="Mercury">
                <div class="dest-icon">🌑</div>
                <div class="dest-name">MERCURY</div>
                <div class="dest-dist">77M KM</div>
            </div>
            <div class="dest-card" data-target="Venus">
                <div class="dest-icon">🟡</div>
                <div class="dest-name">VENUS</div>
                <div class="dest-dist">41M KM</div>
            </div>
            <div class="dest-card" data-target="Jupiter">
                <div class="dest-icon">🪐</div>
                <div class="dest-name">JUPITER</div>
                <div class="dest-dist">778M KM</div>
            </div>
            <div class="dest-card" data-target="Saturn">
                <div class="dest-icon">✨</div>
                <div class="dest-name">SATURN</div>
                <div class="dest-dist">1.4B KM</div>
            </div>
            <div class="dest-card" data-target="Uranus">
                <div class="dest-icon">🔷</div>
                <div class="dest-name">URANUS</div>
                <div class="dest-dist">2.8B KM</div>
            </div>
            <div class="dest-card" data-target="Neptune">
                <div class="dest-icon">🔵</div>
                <div class="dest-name">NEPTUNE</div>
                <div class="dest-dist">4.5B KM</div>
            </div>
            <div class="dest-card" data-target="Sun">
                <div class="dest-icon">☀️</div>
                <div class="dest-name">SUN</div>
                <div class="dest-dist">149M KM</div>
            </div>
        </div>

        <button class="btn-play-mission" id="playMissionBtn">
            <span>▶ PLAY MISSION</span>
        </button>

        <div class="start-manual-hint">
            <span><kbd>W</kbd> Thrust</span>
            <span><kbd>S</kbd> Brake</span>
            <span><kbd>A</kbd><kbd>D</kbd> Turn</span>
            <span><kbd>Q</kbd><kbd>E</kbd> Roll</span>
            <span><kbd>SPACE</kbd> Warp Boost</span>
            <span><kbd>C</kbd> Camera View</span>
            <span><kbd>M</kbd> Solar Map</span>
            <span><kbd>O</kbd> Autopilot</span>
            <span><kbd>L</kbd> Quick Land</span>
        </div>
    </div>

    <!-- 2. IN-FLIGHT AAA HUD -->
    <div id="hud">

        <!-- Top Status Bar -->
        <div class="topbar">
            <div class="top-left">
                <div class="logo">✦ COSMIC QUEST</div>
                <div class="target-pill">
                    DEST: <strong id="topTargetName">MOON</strong>
                    <span>//</span>
                    <span id="targetDist">340 km</span>
                    <span>//</span>
                    <span id="targetEta">--</span>
                </div>
                <div class="score-pill">
                    <span>★</span>
                    <span id="scoreText">0 PTS</span>
                </div>
                <div class="nasa-ticker" id="nasaTicker">
                    <span class="dot"></span>
                    <span id="nasaText">NASA DONKI // SOLAR WIND: 462 KM/S</span>
                </div>
            </div>

            <div class="top-right">
                <!-- 3 Camera Modes Switcher -->
                <div class="camera-btn-group" title="Camera Mode [C]">
                    <button class="cam-mode-btn active" id="btnCamCockpit">
                        <span>🧑‍🚀</span> <span>COCKPIT</span>
                    </button>
                    <button class="cam-mode-btn" id="btnCamChase">
                        <span>🚀</span> <span>CHASE</span>
                    </button>
                    <button class="cam-mode-btn" id="btnCamExternal">
                        <span>🌌</span> <span>EXTERNAL</span>
                    </button>
                </div>

                <button class="hud-btn accent-btn" id="mapBtn" title="Solar System Tactical Map [M]">
                    <span>🗺</span> <span>MAP</span>
                </button>
                <button class="hud-btn land-btn" id="topLandBtn" title="Quick Planet Landing [L]">
                    <span>🚀</span> <span>LAND</span>
                </button>
                <button class="hud-btn" id="autopilotBtn" title="Autopilot System [O]">
                    <span>🤖</span> <span id="autoBtnText">AUTO</span>
                </button>
                <button class="hud-btn" id="tasksBtn" title="Mission Checklist">
                    <span>📋</span> <span>TASKS</span>
                </button>
                <button class="hud-btn" id="mouseBtn" title="Toggle Mouse Flight Steering">
                    <span>🎯</span> <span id="mouseBtnText">STEER</span>
                </button>
                <button class="hud-btn" id="audioBtn" title="Toggle Sound">
                    <span>🔊</span> <span id="audioBtnText">SOUND</span>
                </button>
                <button class="hud-btn" id="hudToggleBtn" title="Hide/Show HUD [H]">
                    <span>👁</span> <span>HUD</span>
                </button>
                <button class="hud-btn" id="pauseBtn" title="Pause Flight [P]">
                    <span>⏸</span> <span>PAUSE</span>
                </button>
                <button class="hud-btn" id="resetBtn" title="Reset Flight [R]">
                    <span>⟲</span> <span>RESET</span>
                </button>
            </div>
        </div>

        <div id="alertBanner">WARNING: OXYGEN SUPPLY LOW</div>
        <div id="toastNotice">✦ TASK COMPLETED: +300 PTS</div>

        <!-- Left Telemetry Bracket (Bottom-Left) -->
        <div class="hud-bracket-left">
            <div class="bracket-header">
                <span>FLIGHT TELEMETRY</span>
                <span style="color:#00ffaa;" id="flightMode">ACTIVE</span>
            </div>

            <div class="speed-hero">
                <div class="speed-number" id="speed">0</div>
                <div class="speed-unit">KM/S</div>
            </div>
            <div class="hud-bar">
                <div class="fill" id="speedBar" style="width:0%;"></div>
            </div>

            <div class="mini-stat">
                <span>ALTITUDE</span>
                <span class="val" id="altitude">100 km</span>
            </div>

            <div class="mini-stat">
                <span>G-FORCE</span>
                <span class="val" id="gForce">1.0 G</span>
            </div>

            <div class="mini-stat">
                <span>THRUST</span>
                <span class="val" id="thrustStatus">IDLE</span>
            </div>

            <div class="mini-stat">
                <span>AUTOPILOT</span>
                <span class="val" id="autoStatusText" style="color:#8be5ff;">STANDBY</span>
            </div>
        </div>

        <!-- Right Mission & Life Support Bracket (Bottom-Right) -->
        <div class="hud-bracket-right">
            <div class="bracket-header">
                <span>MISSION CONTROL</span>
                <span id="missionStatus">EN ROUTE</span>
            </div>

            <div class="mini-stat">
                <span>SPACESHIP HEALTH</span>
                <span class="val" id="hullText">100%</span>
            </div>
            <div class="hud-bar">
                <div class="fill" id="hullBar" style="width:100%;"></div>
            </div>

            <div class="mini-stat" style="margin-top:6px;">
                <span>PROPELLANT</span>
                <span class="val" id="fuelText">100%</span>
            </div>
            <div class="hud-bar">
                <div class="fill" id="fuelBar" style="width:100%;"></div>
            </div>

            <div class="mini-stat" style="margin-top:6px;">
                <span>OXYGEN</span>
                <span class="val" id="oxygenText">100%</span>
            </div>
            <div class="hud-bar">
                <div class="fill" id="oxygenBar" style="width:100%;"></div>
            </div>

            <select class="mini-select" id="planetSelect">
                <option value="Moon" selected>TARGET: MOON</option>
                <option value="Earth">TARGET: EARTH</option>
                <option value="Mars">TARGET: MARS</option>
                <option value="Mercury">TARGET: MERCURY</option>
                <option value="Venus">TARGET: VENUS</option>
                <option value="Jupiter">TARGET: JUPITER</option>
                <option value="Saturn">TARGET: SATURN</option>
                <option value="Uranus">TARGET: URANUS</option>
                <option value="Neptune">TARGET: NEPTUNE</option>
                <option value="Sun">TARGET: SUN</option>
            </select>

            <div id="message">Awaiting pilot command...</div>

            <div class="btn-controls-row">
                <button class="btn-action quick-land-action" id="hudQuickLandBtn">🚀 QUICK LAND</button>
                <button class="btn-action" id="hudAutopilotToggleBtn">🤖 AUTOPILOT</button>
            </div>
            <div class="btn-controls-row">
                <button class="btn-action" id="startBtn">START</button>
                <button class="btn-action" id="menuBtn">MENU</button>
            </div>
        </div>

        <!-- In-World 3D Destination Target Marker -->
        <div id="navTargetMarker">
            <div class="nav-reticle-box"></div>
            <div class="nav-reticle-label">
                <strong id="markerTargetName">MOON</strong> // <span id="markerTargetDist">340 KM</span>
            </div>
        </div>

        <!-- Screen-Edge Bearing Arrow -->
        <div id="navBearingArrow">
            <div class="bearing-arrow-icon" id="bearingArrowIcon">▲</div>
            <div class="bearing-label" id="bearingLabel">TGT // 34° RIGHT</div>
        </div>

        <!-- Minimalist Flight Reticle -->
        <div id="crosshair-container">
            <div id="crosshair">⊕</div>
            <div id="flightReticle"></div>
        </div>

        <!-- Bottom Controls Guide Ribbon -->
        <div class="bottom-ribbon">
            <span><kbd>W</kbd>/<kbd>S</kbd> Thrust & Brake</span>
            <span><kbd>A</kbd>/<kbd>D</kbd> Turn</span>
            <span><kbd>Q</kbd>/<kbd>E</kbd> Roll</span>
            <span><kbd>SPACE</kbd> Boost</span>
            <span><kbd>C</kbd> Camera</span>
            <span><kbd>M</kbd> Solar Map</span>
            <span><kbd>O</kbd> Autopilot</span>
            <span><kbd>L</kbd> Quick Land</span>
            <span><kbd>H</kbd> HUD</span>
        </div>

        <!-- Mission Tasks Drawer -->
        <div id="missionTasksDrawer">
            <div class="drawer-header">
                <h3>✦ MISSION OBJECTIVES</h3>
                <button class="drawer-close" id="drawerCloseBtn">✕</button>
            </div>
            <div class="drawer-task-list" id="drawerTaskList">
                <!-- Dynamically generated tasks for target planet -->
            </div>
        </div>

    </div>

    <!-- 3. INTERACTIVE SOLAR SYSTEM MAP MODAL -->
    <div id="solarSystemMap">
        <div class="map-header">
            <div class="map-title">
                <span>✦ SOLAR SYSTEM TACTICAL MAP</span>
                <span class="badge">10 BODIES TRACKED</span>
            </div>
            <button class="hud-btn" id="closeMapBtn">✕ CLOSE MAP [M]</button>
        </div>

        <div class="map-body">
            <div class="map-canvas-container">
                <canvas id="solarMapCanvas"></canvas>
                <div class="map-toolbar">
                    <button class="map-tool-btn" id="mapZoomIn">+</button>
                    <button class="map-tool-btn" id="mapZoomOut">-</button>
                    <button class="map-tool-btn" id="mapRotate">↻ ROTATE</button>
                    <button class="map-tool-btn" id="mapCenterShip">🚀 CENTER SHIP</button>
                    <button class="map-tool-btn" id="mapReset">⟲ RESET</button>
                </div>
            </div>

            <div class="map-sidebar" id="mapPlanetSidebar">
                <div class="map-planet-preview">
                    <div class="planet-preview-glyph" id="mapPreviewGlyph">🌕</div>
                    <div class="planet-preview-meta">
                        <h3 id="mapTargetTitle">MOON</h3>
                        <div class="class-tag" id="mapTargetClass">NATURAL SATELLITE</div>
                    </div>
                </div>

                <div class="map-spec-grid">
                    <div class="map-spec-item">
                        <span>DISTANCE TO SHIP</span>
                        <span id="mapSpecDist">384,400 KM</span>
                    </div>
                    <div class="map-spec-item">
                        <span>SURFACE GRAVITY</span>
                        <span id="mapSpecGrav">1.62 m/s² (0.166 g)</span>
                    </div>
                    <div class="map-spec-item">
                        <span>ATMOSPHERE</span>
                        <span id="mapSpecAtmo">Ultra-thin exosphere</span>
                    </div>
                    <div class="map-spec-item">
                        <span>SURFACE TEMP</span>
                        <span id="mapSpecTemp">-130°C to +120°C</span>
                    </div>
                </div>

                <div class="map-description" id="mapTargetDesc">
                    The Moon is Earth's only natural satellite. Features extensive cratered highlands, dark volcanic maria, and zero breathable atmosphere.
                </div>

                <div class="map-action-stack">
                    <button class="map-action-btn green" id="mapQuickLandBtn">🚀 QUICK LANDING</button>
                    <button class="map-action-btn" id="mapAutopilotBtn">🤖 ENGAGE AUTOPILOT</button>
                    <button class="map-action-btn secondary" id="mapSetDestBtn">🎯 SET DESTINATION</button>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. QUICK PLANET LANDING CINEMATIC OVERLAY -->
    <div id="landingCinematicOverlay">
        <canvas id="landingVFXCanvas"></canvas>
        <div class="landing-telemetry-hud">
            <div class="landing-title" id="landingPlanetTitle">APPROACHING MOON</div>
            <div class="landing-phase-tag" id="landingPhaseTag">PHASE 1 // WARP TRANSIT & ORBITAL INSERTION</div>

            <div class="landing-readout-grid">
                <div class="landing-metric-box">
                    <div class="label">ALTITUDE</div>
                    <div class="num" id="landingAltNum">120.0 KM</div>
                </div>
                <div class="landing-metric-box">
                    <div class="label">DESCENT VELOCITY</div>
                    <div class="num" id="landingVelNum">4.2 KM/S</div>
                </div>
                <div class="landing-metric-box">
                    <div class="label">ATMOSPHERIC PLASMA</div>
                    <div class="num" id="landingPlasmaNum" style="color:#00f0ff;">NOMINAL</div>
                </div>
                <div class="landing-metric-box">
                    <div class="label">RETRO-THRUSTERS</div>
                    <div class="num" id="landingRetroNum" style="color:#00ffaa;">ARMED</div>
                </div>
            </div>

            <div class="landing-progress-bar">
                <div class="landing-progress-fill" id="landingProgressFill"></div>
            </div>

            <button class="landing-btn-abort" id="abortLandingBtn">✕ ABORT LANDING</button>
        </div>
    </div>

    <!-- 5. SURFACE EXPLORATION VIEW -->
    <div id="surfaceExplorationView">
        <canvas id="surfaceCanvas"></canvas>
        <div class="surface-hud-overlay">
            <div class="surface-top-row">
                <div class="surface-banner">
                    <h2 id="surfaceTitle">MOON SURFACE EXPLORATION</h2>
                    <div class="surface-sub" id="surfaceSub">LANDING SITE: TAURUS-LITTROW BASIN // ELEVATION: -1400 M</div>
                </div>

                <div class="surface-tasks-card">
                    <h3>
                        <span>SURFACE RESEARCH TASKS</span>
                        <span id="surfaceTasksCounter" style="color:var(--green-ok);">0/3 COMPLETED</span>
                    </h3>
                    <div id="surfaceTasksContainer">
                        <!-- Dynamic task items with clickable action buttons -->
                    </div>
                </div>
            </div>

            <div class="surface-bottom-row">
                <button class="btn-liftoff" id="surfaceLiftoffBtn">
                    <span>🚀 RETURN TO ORBIT</span>
                </button>
                <button class="hud-btn" id="surfaceOpenMapBtn" style="padding:10px 18px; font-size:12px;">
                    <span>🗺 SOLAR SYSTEM MAP</span>
                </button>
            </div>
        </div>
    </div>

    <!-- 6. MOBILE ON-SCREEN TOUCH CONTROLS -->
    <div id="mobileControls">
        <div class="mobile-dpad">
            <button class="dpad-btn dpad-up" id="dpadUp">▲</button>
            <button class="dpad-btn dpad-down" id="dpadDown">▼</button>
            <button class="dpad-btn dpad-left" id="dpadLeft">◄</button>
            <button class="dpad-btn dpad-right" id="dpadRight">►</button>
        </div>
        <div class="mobile-actions">
            <button class="touch-action-btn" id="touchBoost" style="color:#ffaa00; border-color:#ffaa00;">⚡</button>
            <button class="touch-action-btn" id="touchLand" style="color:#00ffaa; border-color:#00ffaa;">🚀</button>
            <button class="touch-action-btn" id="touchMap">🗺</button>
            <button class="touch-action-btn" id="touchCam">🎥</button>
        </div>
    </div>

    <!-- 7. MISSION COMPLETED MODAL -->
    <div id="missionCompleteModal">
        <div class="modal-card">
            <h2>✦ MISSION ACCOMPLISHED</h2>
            <p id="modalMessage">Orbital insertion around target celestial body achieved successfully.</p>
            <div style="display:flex; gap:10px; justify-content:center;">
                <button class="btn-play-mission" id="nextMissionBtn" style="font-size:13px; padding:10px 24px;">
                    NEXT DESTINATION
                </button>
                <button class="hud-btn" id="dismissModalBtn" style="font-size:13px; padding:10px 20px;">
                    CONTINUE FLIGHT
                </button>
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
        class AudioSynth {
            constructor() {
                this.ctx = null;
                this.enabled = true;
                this.engineGain = null;
                this.engineOsc = null;
                this.boostGain = null;
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
                    this.engineOsc.frequency.setValueAtTime(54, this.ctx.currentTime);

                    const filter = this.ctx.createBiquadFilter();
                    filter.type = 'lowpass';
                    filter.frequency.setValueAtTime(120, this.ctx.currentTime);

                    this.engineGain = this.ctx.createGain();
                    this.engineGain.gain.setValueAtTime(0.01, this.ctx.currentTime);

                    this.engineOsc.connect(filter);
                    filter.connect(this.engineGain);
                    this.engineGain.connect(this.ctx.destination);
                    this.engineOsc.start();

                    const bufLen = this.ctx.sampleRate * 2;
                    const noiseBuf = this.ctx.createBuffer(1, bufLen, this.ctx.sampleRate);
                    const out = noiseBuf.getChannelData(0);
                    for (let i = 0; i < bufLen; i++) {
                        out[i] = (Math.random() * 2 - 1) * 0.4;
                    }
                    const noiseSource = this.ctx.createBufferSource();
                    noiseSource.buffer = noiseBuf;
                    noiseSource.loop = true;

                    const boostFilter = this.ctx.createBiquadFilter();
                    boostFilter.type = 'bandpass';
                    boostFilter.frequency.setValueAtTime(220, this.ctx.currentTime);
                    boostFilter.Q.setValueAtTime(1.8, this.ctx.currentTime);

                    this.boostGain = this.ctx.createGain();
                    this.boostGain.gain.setValueAtTime(0, this.ctx.currentTime);

                    noiseSource.connect(boostFilter);
                    boostFilter.connect(this.boostGain);
                    this.boostGain.connect(this.ctx.destination);
                    noiseSource.start();

                    this.initialized = true;
                } catch (e) {
                    console.warn("Audio initialization bypassed", e);
                }
            }

            playClick() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(1400, this.ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(320, this.ctx.currentTime + 0.04);
                    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);
                    osc.connect(gain);
                    gain.connect(this.ctx.destination);
                    osc.start();
                    osc.stop(this.ctx.currentTime + 0.05);
                } catch (e) { }
            }

            playAlarm() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(880, this.ctx.currentTime);
                    osc.frequency.setValueAtTime(659, this.ctx.currentTime + 0.1);
                    gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
                    gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.22);
                    osc.connect(gain);
                    gain.connect(this.ctx.destination);
                    osc.start();
                    osc.stop(this.ctx.currentTime + 0.24);
                } catch (e) { }
            }

            playWarp() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(120, this.ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(1800, this.ctx.currentTime + 0.8);
                    gain.gain.setValueAtTime(0.01, this.ctx.currentTime);
                    gain.gain.linearRampToValueAtTime(0.2, this.ctx.currentTime + 0.4);
                    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.9);
                    osc.connect(gain);
                    gain.connect(this.ctx.destination);
                    osc.start();
                    osc.stop(this.ctx.currentTime + 0.95);
                } catch (e) { }
            }

            playSuccess() {
                if (!this.enabled || !this.initialized) return;
                try {
                    const now = this.ctx.currentTime;
                    const notes = [523.25, 659.25, 783.99, 1046.5];
                    notes.forEach((freq, idx) => {
                        const osc = this.ctx.createOscillator();
                        const gain = this.ctx.createGain();
                        osc.type = 'sine';
                        osc.frequency.setValueAtTime(freq, now + idx * 0.08);
                        gain.gain.setValueAtTime(0.15, now + idx * 0.08);
                        gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.25);
                        osc.connect(gain);
                        gain.connect(this.ctx.destination);
                        osc.start(now + idx * 0.08);
                        osc.stop(now + idx * 0.08 + 0.28);
                    });
                } catch (e) { }
            }

            update(thrusting, boosting, speedNorm) {
                if (!this.initialized || !this.enabled) return;
                const now = this.ctx.currentTime;
                if (thrusting) {
                    this.engineGain.gain.setTargetAtTime(0.05 + speedNorm * 0.12, now, 0.08);
                    this.engineOsc.frequency.setTargetAtTime(50 + speedNorm * 42, now, 0.08);
                } else {
                    this.engineGain.gain.setTargetAtTime(0.012, now, 0.15);
                    this.engineOsc.frequency.setTargetAtTime(45, now, 0.15);
                }

                if (boosting) {
                    this.boostGain.gain.setTargetAtTime(0.16, now, 0.05);
                } else {
                    this.boostGain.gain.setTargetAtTime(0, now, 0.09);
                }
            }
        }

        const audio = new AudioSynth();
        window.addEventListener('click', () => audio.init(), { once: true });
        window.addEventListener('keydown', () => audio.init(), { once: true });

        /* -------------------------------------------------------------
           NASA DONKI LIVE SPACE WEATHER DATA INTEGRATION
           ------------------------------------------------------------- */
        const nasaTextEl = document.getElementById('nasaText');
        async function fetchNasaDonki() {
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 4500);
                const res = await fetch('https://api.nasa.gov/DONKI/CME?api_key=DEMO_KEY', { signal: controller.signal });
                clearTimeout(timeoutId);
                if (res.ok) {
                    const data = await res.json();
                    if (Array.isArray(data) && data.length > 0) {
                        const latest = data[data.length - 1];
                        const spd = latest.cmeAnalyses?.[0]?.speed || 485;
                        const typ = latest.cmeAnalyses?.[0]?.type || "Common";
                        nasaTextEl.textContent = `NASA DONKI // LIVE CME: ${Math.round(spd)} KM/S [${typ.toUpperCase()}]`;
                        return;
                    }
                }
            } catch (err) { }
            nasaTextEl.textContent = `NASA DONKI // SOLAR WIND: 462 KM/S | FLUX: NOMINAL`;
        }
        fetchNasaDonki();

        /* -------------------------------------------------------------
           THREE.JS SCENE SETUP & RENDERER
           ------------------------------------------------------------- */
        const canvasElement = document.getElementById('webgl');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x01050e);
        scene.fog = new THREE.FogExp2(0x01050e, 0.00008);

        const camera = new THREE.PerspectiveCamera(
            65,
            window.innerWidth / window.innerHeight,
            0.05,
            65000
        );

        const renderer = new THREE.WebGLRenderer({
            canvas: canvasElement,
            antialias: true,
            powerPreference: "high-performance"
        });

        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.8));
        renderer.outputColorSpace = THREE.SRGBColorSpace;
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.35;

        /* -------------------------------------------------------------
           CINEMATIC SPACE LIGHTING
           ------------------------------------------------------------- */
        const spaceAmbient = new THREE.AmbientLight(0x18263e, 1.35);
        scene.add(spaceAmbient);

        const sunPos = new THREE.Vector3(-1200, 420, 800);
        const sunLight = new THREE.DirectionalLight(0xfffaee, 4.0);
        sunLight.position.copy(sunPos);
        scene.add(sunLight);

        /* -------------------------------------------------------------
           PROCEDURAL PLANETARY TEXTURE GENERATORS (ALL 10 BODIES)
           ------------------------------------------------------------- */
        function createSunTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 512; canvas.height = 256;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#fff9e6';
            ctx.fillRect(0, 0, 512, 256);
            ctx.fillStyle = '#ffbb33';
            for (let i = 0; i < 180; i++) {
                ctx.beginPath();
                ctx.arc(Math.random() * 512, Math.random() * 256, 8 + Math.random() * 24, 0, Math.PI * 2);
                ctx.fill();
            }
            ctx.fillStyle = '#ff8800';
            for (let i = 0; i < 90; i++) {
                ctx.beginPath();
                ctx.arc(Math.random() * 512, Math.random() * 256, 4 + Math.random() * 12, 0, Math.PI * 2);
                ctx.fill();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createSunCorona() {
            const cCanvas = document.createElement('canvas');
            cCanvas.width = 256; cCanvas.height = 256;
            const cCtx = cCanvas.getContext('2d');
            const grad = cCtx.createRadialGradient(128, 128, 10, 128, 128, 128);
            grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
            grad.addColorStop(0.25, 'rgba(255, 215, 120, 0.7)');
            grad.addColorStop(0.55, 'rgba(255, 140, 20, 0.25)');
            grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
            cCtx.fillStyle = grad;
            cCtx.fillRect(0, 0, 256, 256);
            const tex = new THREE.CanvasTexture(cCanvas);
            const mat = new THREE.SpriteMaterial({
                map: tex,
                blending: THREE.AdditiveBlending,
                color: 0xffeedd
            });
            const sprite = new THREE.Sprite(mat);
            sprite.scale.set(480, 480, 1);
            sprite.position.copy(sunPos);
            scene.add(sprite);
        }
        createSunCorona();

        function createMercuryTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 512; canvas.height = 256;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#5a5b62';
            ctx.fillRect(0, 0, 512, 256);
            for (let i = 0; i < 140; i++) {
                const x = Math.random() * 512, y = Math.random() * 256, r = 2 + Math.random() * 12;
                ctx.fillStyle = '#36373d';
                ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
                ctx.strokeStyle = '#8d8f99';
                ctx.lineWidth = 1;
                ctx.beginPath(); ctx.arc(x, y, r, Math.PI * 0.6, Math.PI * 1.8); ctx.stroke();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createVenusTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 512; canvas.height = 256;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 0, 256);
            grad.addColorStop(0, '#e5be6b');
            grad.addColorStop(0.3, '#d4a24c');
            grad.addColorStop(0.6, '#eed494');
            grad.addColorStop(1, '#c59139');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 512, 256);
            ctx.fillStyle = 'rgba(255, 240, 180, 0.35)';
            for (let i = 0; i < 20; i++) {
                ctx.beginPath();
                ctx.ellipse(Math.random() * 512, 40 + Math.random() * 170, 70 + Math.random() * 90, 12 + Math.random() * 20, 0.1, 0, Math.PI * 2);
                ctx.fill();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createEarthTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 0, 512);
            grad.addColorStop(0, '#040d1e');
            grad.addColorStop(0.25, '#071f45');
            grad.addColorStop(0.5, '#0b2e66');
            grad.addColorStop(0.75, '#071f45');
            grad.addColorStop(1, '#040d1e');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 1024, 512);

            ctx.fillStyle = 'rgba(18, 115, 160, 0.45)';
            function shelf(x, y, w, h) {
                ctx.beginPath(); ctx.ellipse(x, y, w, h, 0, 0, Math.PI * 2); ctx.fill();
            }
            shelf(240, 170, 95, 75);
            shelf(320, 360, 85, 95);
            shelf(540, 160, 110, 65);
            shelf(560, 310, 90, 110);
            shelf(740, 190, 160, 90);
            shelf(850, 380, 85, 65);

            // North America
            ctx.fillStyle = '#225528';
            ctx.beginPath();
            ctx.moveTo(150, 100); ctx.lineTo(260, 110); ctx.lineTo(310, 170);
            ctx.lineTo(290, 240); ctx.lineTo(230, 270); ctx.lineTo(190, 230);
            ctx.closePath(); ctx.fill();

            // South America
            ctx.fillStyle = '#1c4a22';
            ctx.beginPath();
            ctx.moveTo(270, 290); ctx.lineTo(350, 310); ctx.lineTo(380, 370);
            ctx.lineTo(330, 460); ctx.lineTo(290, 420); ctx.lineTo(270, 340);
            ctx.closePath(); ctx.fill();

            // Eurasia
            ctx.fillStyle = '#26542d';
            ctx.beginPath();
            ctx.moveTo(480, 140); ctx.lineTo(600, 100); ctx.lineTo(840, 110);
            ctx.lineTo(890, 210); ctx.lineTo(760, 270); ctx.lineTo(660, 210);
            ctx.lineTo(520, 220); ctx.closePath(); ctx.fill();

            // Africa
            ctx.fillStyle = '#8a7746';
            ctx.beginPath();
            ctx.moveTo(480, 210); ctx.lineTo(620, 210); ctx.lineTo(620, 280);
            ctx.lineTo(560, 290); ctx.lineTo(470, 260); ctx.closePath(); ctx.fill();
            ctx.fillStyle = '#245224';
            ctx.beginPath();
            ctx.moveTo(470, 260); ctx.lineTo(560, 290); ctx.lineTo(580, 390);
            ctx.lineTo(530, 420); ctx.lineTo(500, 330); ctx.closePath(); ctx.fill();

            // Australia
            ctx.fillStyle = '#9b6c38';
            ctx.beginPath();
            ctx.moveTo(790, 340); ctx.lineTo(890, 340); ctx.lineTo(880, 420);
            ctx.lineTo(800, 410); ctx.closePath(); ctx.fill();

            // Polar ice
            ctx.fillStyle = '#f0f7ff';
            ctx.fillRect(0, 0, 1024, 45);
            ctx.fillRect(0, 470, 1024, 42);

            return new THREE.CanvasTexture(canvas);
        }

        function createEarthCloudsTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, 1024, 512);
            ctx.fillStyle = 'rgba(255, 255, 255, 0.72)';
            for (let i = 0; i < 180; i++) {
                const cx = Math.random() * 1024, cy = 60 + Math.random() * 390;
                const rx = 25 + Math.random() * 70, ry = 10 + Math.random() * 25;
                ctx.beginPath();
                ctx.ellipse(cx, cy, rx, ry, (Math.random() - 0.5) * 0.4, 0, Math.PI * 2);
                ctx.fill();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createMoonTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#656770';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.fillStyle = '#373940';
            function maria(x, y, rx, ry) {
                ctx.beginPath();
                ctx.ellipse(x, y, rx, ry, (Math.random() - 0.5) * 0.4, 0, Math.PI * 2);
                ctx.fill();
            }
            maria(290, 230, 85, 70);
            maria(370, 180, 65, 50);
            maria(460, 190, 50, 40);
            maria(490, 250, 55, 45);
            maria(580, 220, 38, 32);
            maria(540, 310, 45, 38);
            maria(340, 340, 50, 40);

            for (let i = 0; i < 150; i++) {
                const x = Math.random() * 1024, y = Math.random() * 512, r = 3 + Math.random() * 18;
                ctx.fillStyle = '#212226';
                ctx.beginPath(); ctx.arc(x + r * 0.2, y + r * 0.15, r * 0.85, 0, Math.PI * 2); ctx.fill();
                ctx.strokeStyle = '#c6c9d6';
                ctx.lineWidth = Math.max(1, r * 0.22);
                ctx.beginPath(); ctx.arc(x, y, r, Math.PI * 0.7, Math.PI * 1.8); ctx.stroke();
            }

            const tychoX = 380, tychoY = 390;
            ctx.strokeStyle = 'rgba(230, 235, 250, 0.4)';
            ctx.lineWidth = 1.5;
            for (let a = 0; a < 16; a++) {
                const ang = (a / 16) * Math.PI * 2;
                ctx.beginPath();
                ctx.moveTo(tychoX, tychoY);
                ctx.lineTo(tychoX + Math.cos(ang) * 180, tychoY + Math.sin(ang) * 180);
                ctx.stroke();
            }
            return new THREE.CanvasTexture(canvas);
        }

        function createMarsTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#b74c24';
            ctx.fillRect(0, 0, 1024, 512);

            ctx.fillStyle = '#6e2b14';
            function darkSpot(x, y, rx, ry) {
                ctx.beginPath(); ctx.ellipse(x, y, rx, ry, 0.2, 0, Math.PI * 2); ctx.fill();
            }
            darkSpot(350, 280, 120, 60);
            darkSpot(650, 250, 140, 75);
            darkSpot(850, 310, 80, 50);

            ctx.strokeStyle = '#481909';
            ctx.lineWidth = 9;
            ctx.beginPath();
            ctx.moveTo(280, 270); ctx.lineTo(460, 290); ctx.stroke();

            ctx.fillStyle = '#ffffff';
            ctx.fillRect(0, 0, 1024, 30);
            ctx.fillRect(0, 485, 1024, 27);
            return new THREE.CanvasTexture(canvas);
        }

        function createJupiterTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            const bands = [
                '#8b5e34', '#c9a474', '#e2cfb1', '#9e623b',
                '#d8ba8e', '#6d3c1c', '#deb986', '#9c5932',
                '#e8cfad', '#a56b3e', '#d2b183', '#794825'
            ];
            const sliceH = 512 / bands.length;
            for (let i = 0; i < bands.length; i++) {
                ctx.fillStyle = bands[i];
                ctx.fillRect(0, i * sliceH, 1024, sliceH);
            }
            ctx.fillStyle = '#c84422';
            ctx.beginPath(); ctx.ellipse(620, 330, 55, 35, 0, 0, Math.PI * 2); ctx.fill();
            ctx.fillStyle = '#e87248';
            ctx.beginPath(); ctx.ellipse(620, 330, 35, 20, 0, 0, Math.PI * 2); ctx.fill();
            return new THREE.CanvasTexture(canvas);
        }

        function createSaturnTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 1024; canvas.height = 512;
            const ctx = canvas.getContext('2d');
            const satGrad = ctx.createLinearGradient(0, 0, 0, 512);
            satGrad.addColorStop(0, '#98835e');
            satGrad.addColorStop(0.3, '#d8c292');
            satGrad.addColorStop(0.5, '#e5d3a5');
            satGrad.addColorStop(0.7, '#cfb989');
            satGrad.addColorStop(1, '#947f5b');
            ctx.fillStyle = satGrad;
            ctx.fillRect(0, 0, 1024, 512);
            return new THREE.CanvasTexture(canvas);
        }

        function createSaturnRingTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 512; canvas.height = 64;
            const ctx = canvas.getContext('2d');
            const rGrad = ctx.createLinearGradient(0, 0, 512, 0);
            rGrad.addColorStop(0, 'rgba(120, 100, 70, 0)');
            rGrad.addColorStop(0.15, 'rgba(180, 150, 100, 0.4)');
            rGrad.addColorStop(0.35, 'rgba(225, 195, 140, 0.85)');
            rGrad.addColorStop(0.60, 'rgba(210, 180, 125, 0.9)');
            rGrad.addColorStop(0.66, 'rgba(30, 25, 15, 0.1)');
            rGrad.addColorStop(0.72, 'rgba(190, 160, 115, 0.75)');
            rGrad.addColorStop(0.95, 'rgba(160, 135, 95, 0.4)');
            rGrad.addColorStop(1, 'rgba(100, 80, 50, 0)');
            ctx.fillStyle = rGrad;
            ctx.fillRect(0, 0, 512, 64);
            return new THREE.CanvasTexture(canvas);
        }

        function createUranusTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 512; canvas.height = 256;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 0, 256);
            grad.addColorStop(0, '#75c8d6');
            grad.addColorStop(0.5, '#99e0ec');
            grad.addColorStop(1, '#66b8c8');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 512, 256);
            return new THREE.CanvasTexture(canvas);
        }

        function createUranusRingTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 256; canvas.height = 32;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 256, 0);
            grad.addColorStop(0, 'rgba(120, 180, 200, 0)');
            grad.addColorStop(0.5, 'rgba(160, 220, 230, 0.5)');
            grad.addColorStop(1, 'rgba(120, 180, 200, 0)');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 256, 32);
            return new THREE.CanvasTexture(canvas);
        }

        function createNeptuneTexture() {
            const canvas = document.createElement('canvas');
            canvas.width = 512; canvas.height = 256;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 0, 256);
            grad.addColorStop(0, '#1c4a96');
            grad.addColorStop(0.4, '#2862bd');
            grad.addColorStop(0.7, '#1f53a8');
            grad.addColorStop(1, '#173d80');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 512, 256);

            // Great Dark Spot
            ctx.fillStyle = '#0f295e';
            ctx.beginPath(); ctx.ellipse(320, 150, 42, 22, 0, 0, Math.PI * 2); ctx.fill();

            // White cirrus streaks
            ctx.fillStyle = 'rgba(255, 255, 255, 0.6)';
            for (let i = 0; i < 12; i++) {
                ctx.beginPath();
                ctx.ellipse(Math.random() * 512, 60 + Math.random() * 140, 35 + Math.random() * 40, 2 + Math.random() * 3, 0, 0, Math.PI * 2);
                ctx.fill();
            }
            return new THREE.CanvasTexture(canvas);
        }

        /* -------------------------------------------------------------
           CELESTIAL BODIES METADATA & CONFIGURATIONS
           ------------------------------------------------------------- */
        const planetData = {
            "Moon": {
                name: "Moon", class: "NATURAL SATELLITE", distStr: "384,400 KM",
                gravity: "1.62 m/s² (0.166 g)", atmo: "Ultra-thin exosphere (< 10⁻¹⁰ Pa)",
                temp: "-130°C to +120°C", radius: 12, pos: [100, 30, -350],
                color: "#c6c9d6", glyph: "🌕",
                desc: "Earth's companion. Rocky regolith surface, extensive basaltic maria basins, and zero breathable atmosphere.",
                tasks: [
                    { id: "m1", title: "Soft Touchdown at Taurus-Littrow", pts: 300, completed: false },
                    { id: "m2", title: "Collect Regolith Core Samples", pts: 350, completed: false },
                    { id: "m3", title: "Deploy Surface Seismometer", pts: 250, completed: false },
                    { id: "m4", title: "Survey Shackleton Crater Rim", pts: 400, completed: false }
                ]
            },
            "Earth": {
                name: "Earth", class: "TERRESTRIAL / HABITABLE", distStr: "LOW ORBIT",
                gravity: "9.80 m/s² (1.00 g)", atmo: "78% N₂, 21% O₂ (1.0 bar)",
                temp: "+15°C Mean", radius: 28, pos: [-300, 60, -650],
                color: "#3aa8ff", glyph: "🌍",
                desc: "Cradle of humanity. Liquid water oceans, nitrogen-oxygen atmosphere, and active magnetosphere.",
                tasks: [
                    { id: "e1", title: "Orbital Altitude Insertion Scan", pts: 250, completed: false },
                    { id: "e2", title: "Telemetry Relay Satellite Sync", pts: 300, completed: false },
                    { id: "e3", title: "Collect Upper Mesosphere Data", pts: 350, completed: false }
                ]
            },
            "Mars": {
                name: "Mars", class: "TERRESTRIAL PLANET", distStr: "225M KM",
                gravity: "3.72 m/s² (0.38 g)", atmo: "95% CO₂, 2.6% N₂ (0.006 bar)",
                temp: "-60°C Mean", radius: 20, pos: [450, 100, -850],
                color: "#e0582d", glyph: "🔴",
                desc: "The Red Planet. Iron oxide desert, ancient river valleys, massive shield volcano Olympus Mons, and polar ice caps.",
                tasks: [
                    { id: "ma1", title: "Atmospheric Entry & Jezero Touchdown", pts: 350, completed: false },
                    { id: "ma2", title: "Deploy Perseverance Explorer Rover", pts: 400, completed: false },
                    { id: "ma3", title: "Spectroscopic Rock & Hydration Scan", pts: 300, completed: false },
                    { id: "ma4", title: "Sample Ancient Lakebed Clay", pts: 350, completed: false }
                ]
            },
            "Mercury": {
                name: "Mercury", class: "TERRESTRIAL PLANET", distStr: "77M KM",
                gravity: "3.70 m/s² (0.38 g)", atmo: "Trace exosphere (Na, He, O₂)",
                temp: "-180°C to +430°C", radius: 10, pos: [-160, 40, -220],
                color: "#8d8f99", glyph: "🌑",
                desc: "Closest to the Sun. Extreme temperature swings, heavily cratered terrain, and high density metallic core.",
                tasks: [
                    { id: "me1", title: "Solar Orbit Insertion & Deceleration", pts: 350, completed: false },
                    { id: "me2", title: "Caloris Basin Geological Mapping", pts: 400, completed: false },
                    { id: "me3", title: "Permanent Shadow Water Ice Probe", pts: 450, completed: false }
                ]
            },
            "Venus": {
                name: "Venus", class: "TERRESTRIAL PLANET", distStr: "41M KM",
                gravity: "8.87 m/s² (0.90 g)", atmo: "96.5% CO₂, 3.5% N₂ (92 bar)",
                temp: "+464°C Runaway Greenhouse", radius: 26, pos: [-240, 50, -420],
                color: "#e8b858", glyph: "🟡",
                desc: "Earth's sister world shrouded in thick sulfuric acid clouds with intense atmospheric crushing pressure.",
                tasks: [
                    { id: "v1", title: "Sulfuric Cloud Deck Aerobraking", pts: 350, completed: false },
                    { id: "v2", title: "Radar Penetration Surface Survey", pts: 400, completed: false },
                    { id: "v3", title: "Supercritical Gas Specimen Capture", pts: 450, completed: false }
                ]
            },
            "Jupiter": {
                name: "Jupiter", class: "GAS GIANT", distStr: "778M KM",
                gravity: "24.79 m/s² (2.53 g)", atmo: "89% H₂, 10% He (Gas Deck)",
                temp: "-110°C Cloud Top", radius: 65, pos: [-800, 250, -1400],
                color: "#d8ba8e", glyph: "🪐",
                desc: "King of the planets. Colossal gas giant with Great Red Spot anticyclone and powerful radiation belts.",
                tasks: [
                    { id: "j1", title: "Jovian Magnetosphere Radiation Pass", pts: 400, completed: false },
                    { id: "j2", title: "Deploy Atmospheric Drop Probe", pts: 450, completed: false },
                    { id: "j3", title: "Observe Great Red Spot Vortices", pts: 400, completed: false },
                    { id: "j4", title: "Galilean Moons Gravitational Survey", pts: 500, completed: false }
                ]
            },
            "Saturn": {
                name: "Saturn", class: "GAS GIANT", distStr: "1.4B KM",
                gravity: "10.44 m/s² (1.06 g)", atmo: "96% H₂, 3% He",
                temp: "-140°C Cloud Top", radius: 55, pos: [850, -180, -1700],
                color: "#e5d3a5", glyph: "✨",
                desc: "Adorned with glorious icy rings spanning thousands of kilometers, composed of billions of water-ice particles.",
                tasks: [
                    { id: "s1", title: "Navigate Cassini Ring Division", pts: 400, completed: false },
                    { id: "s2", title: "Ice Particle Laser Spectrometry", pts: 450, completed: false },
                    { id: "s3", title: "Probe Titan Hydrocarbon Lakes", pts: 500, completed: false }
                ]
            },
            "Uranus": {
                name: "Uranus", class: "ICE GIANT", distStr: "2.8B KM",
                gravity: "8.69 m/s² (0.89 g)", atmo: "83% H₂, 15% He, 2.3% CH₄",
                temp: "-195°C Coldest Atmosphere", radius: 36, pos: [-1150, -120, -2100],
                color: "#7ad5e5", glyph: "🔷",
                desc: "Tilted ice giant rotating nearly on its side (98° axial tilt). Pale aquamarine methane clouds and vertical rings.",
                tasks: [
                    { id: "u1", title: "Axial Tilt Dynamics Orbit Scan", pts: 450, completed: false },
                    { id: "u2", title: "Methane Cloud Absorption Profiling", pts: 400, completed: false },
                    { id: "u3", title: "Vertical Ring System Navigation", pts: 450, completed: false }
                ]
            },
            "Neptune": {
                name: "Neptune", class: "ICE GIANT", distStr: "4.5B KM",
                gravity: "11.15 m/s² (1.14 g)", atmo: "80% H₂, 19% He, 1.5% CH₄",
                temp: "-200°C", radius: 34, pos: [1250, 180, -2600],
                color: "#2862bd", glyph: "🔵",
                desc: "Outermost giant planet. Supersonic winds topping 2,100 km/h, vivid azure hue, and active cryovolcanic moon Triton.",
                tasks: [
                    { id: "n1", title: "Supersonic Jet Stream Speed Tracking", pts: 450, completed: false },
                    { id: "n2", title: "Great Dark Spot Spectroscopy", pts: 500, completed: false },
                    { id: "n3", title: "Triton Nitrogen Geyser Detection", pts: 500, completed: false }
                ]
            },
            "Sun": {
                name: "Sun", class: "YELLOW DWARF STAR (G2V)", distStr: "149M KM",
                gravity: "274 m/s² (28.0 g)", atmo: "Photosphere & Corona Plasma",
                temp: "5,500°C Surface / 15M°C Core", radius: 50, pos: [-1200, 420, 800],
                color: "#fff0aa", glyph: "☀️",
                desc: "Center of the solar system. Containing 99.8% of system mass, driving solar wind and space weather throughout the heliosphere.",
                tasks: [
                    { id: "su1", title: "Parker-Class Perihelion Pass", pts: 500, completed: false },
                    { id: "su2", title: "Coronal Magnetic Reconnection Scan", pts: 550, completed: false },
                    { id: "su3", title: "Solar Flare Particle Flux Analysis", pts: 500, completed: false }
                ]
            }
        };

        /* -------------------------------------------------------------
           SPAWN 10 CELESTIAL BODIES IN THREE.JS SCENE
           ------------------------------------------------------------- */
        const planets = {};
        let earthCloudMesh = null;

        const planetConfigs = [
            { name: "Sun", radius: 48, pos: planetData["Sun"].pos, texFn: createSunTexture, isEmissive: true },
            { name: "Mercury", radius: 10, pos: planetData["Mercury"].pos, texFn: createMercuryTexture },
            { name: "Venus", radius: 26, pos: planetData["Venus"].pos, texFn: createVenusTexture, hasAtmosphere: true, atmoCol: 0xf5d070 },
            { name: "Earth", radius: 28, pos: planetData["Earth"].pos, texFn: createEarthTexture, hasClouds: true, hasAtmosphere: true, atmoCol: 0x3aa8ff },
            { name: "Moon", radius: 12, pos: planetData["Moon"].pos, texFn: createMoonTexture },
            { name: "Mars", radius: 20, pos: planetData["Mars"].pos, texFn: createMarsTexture, hasAtmosphere: true, atmoCol: 0xff6644 },
            { name: "Jupiter", radius: 65, pos: planetData["Jupiter"].pos, texFn: createJupiterTexture },
            { name: "Saturn", radius: 55, pos: planetData["Saturn"].pos, texFn: createSaturnTexture, hasRings: true },
            { name: "Uranus", radius: 36, pos: planetData["Uranus"].pos, texFn: createUranusTexture, hasUranusRings: true },
            { name: "Neptune", radius: 34, pos: planetData["Neptune"].pos, texFn: createNeptuneTexture, hasAtmosphere: true, atmoCol: 0x2060ff }
        ];

        planetConfigs.forEach(cfg => {
            const geo = new THREE.SphereGeometry(cfg.radius, 64, 64);
            let mat;
            if (cfg.isEmissive) {
                mat = new THREE.MeshBasicMaterial({
                    map: cfg.texFn(),
                    color: 0xffffff
                });
            } else {
                mat = new THREE.MeshStandardMaterial({
                    map: cfg.texFn(),
                    roughness: 0.8,
                    metalness: 0.1
                });
            }
            const planet = new THREE.Mesh(geo, mat);
            planet.position.set(...cfg.pos);
            scene.add(planet);

            if (cfg.hasClouds) {
                const cloudGeo = new THREE.SphereGeometry(cfg.radius * 1.018, 64, 64);
                const cloudMat = new THREE.MeshStandardMaterial({
                    map: createEarthCloudsTexture(),
                    transparent: true,
                    opacity: 0.85,
                    blending: THREE.NormalBlending
                });
                earthCloudMesh = new THREE.Mesh(cloudGeo, cloudMat);
                planet.add(earthCloudMesh);
            }

            if (cfg.hasAtmosphere) {
                const atmoGeo = new THREE.SphereGeometry(cfg.radius * 1.055, 48, 48);
                const atmoMat = new THREE.MeshBasicMaterial({
                    color: cfg.atmoCol || 0x3aa8ff,
                    side: THREE.BackSide,
                    transparent: true,
                    opacity: 0.35,
                    blending: THREE.AdditiveBlending
                });
                planet.add(new THREE.Mesh(atmoGeo, atmoMat));
            }

            if (cfg.hasRings) {
                const ringGeo = new THREE.RingGeometry(70, 120, 128);
                const ringMat = new THREE.MeshBasicMaterial({
                    map: createSaturnRingTexture(),
                    side: THREE.DoubleSide,
                    transparent: true,
                    opacity: 0.85
                });
                const ring = new THREE.Mesh(ringGeo, ringMat);
                ring.rotation.x = -1.35;
                planet.add(ring);
            }

            if (cfg.hasUranusRings) {
                const ringGeo = new THREE.RingGeometry(48, 62, 64);
                const ringMat = new THREE.MeshBasicMaterial({
                    map: createUranusRingTexture(),
                    side: THREE.DoubleSide,
                    transparent: true,
                    opacity: 0.7
                });
                const ring = new THREE.Mesh(ringGeo, ringMat);
                ring.rotation.y = Math.PI / 2;
                ring.rotation.x = 0.4;
                planet.add(ring);
            }

            planets[cfg.name] = planet;
        });

        /* -------------------------------------------------------------
           DYNAMIC 3D TRAJECTORY ROUTE LINE
           ------------------------------------------------------------- */
        const trajectoryPoints = [new THREE.Vector3(), new THREE.Vector3()];
        const trajectoryGeo = new THREE.BufferGeometry().setFromPoints(trajectoryPoints);
        const trajectoryMat = new THREE.LineDashedMaterial({
            color: 0x00f0ff,
            dashSize: 15,
            gapSize: 8,
            linewidth: 2,
            transparent: true,
            opacity: 0.65,
            blending: THREE.AdditiveBlending
        });
        const trajectoryLine = new THREE.Line(trajectoryGeo, trajectoryMat);
        scene.add(trajectoryLine);

        /* -------------------------------------------------------------
           STARFIELD & COSMIC DUST
           ------------------------------------------------------------- */
        const starGeo = new THREE.BufferGeometry();
        const starPositions = [];
        const starColors = [];
        const colorPalette = [
            new THREE.Color(0xffffff),
            new THREE.Color(0x9bd5ff),
            new THREE.Color(0xffeaad),
            new THREE.Color(0xffb896),
            new THREE.Color(0x70c5ff)
        ];

        for (let i = 0; i < 8000; i++) {
            const rad = 7000 + Math.random() * 11500;
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.acos(Math.random() * 2 - 1);
            starPositions.push(
                rad * Math.sin(phi) * Math.cos(theta),
                rad * Math.sin(phi) * Math.sin(theta),
                rad * Math.cos(phi)
            );
            const col = colorPalette[Math.floor(Math.random() * colorPalette.length)];
            starColors.push(col.r, col.g, col.b);
        }

        starGeo.setAttribute('position', new THREE.Float32BufferAttribute(starPositions, 3));
        starGeo.setAttribute('color', new THREE.Float32BufferAttribute(starColors, 3));

        const stars = new THREE.Points(
            starGeo,
            new THREE.PointsMaterial({
                size: 2.2,
                vertexColors: true,
                sizeAttenuation: true,
                transparent: true,
                opacity: 0.95
            })
        );
        scene.add(stars);

        const dustCount = 400;
        const dustGeo = new THREE.BufferGeometry();
        const dustPos = new Float32Array(dustCount * 3);
        for (let i = 0; i < dustCount * 3; i += 3) {
            dustPos[i] = (Math.random() - 0.5) * 60;
            dustPos[i + 1] = (Math.random() - 0.5) * 40;
            dustPos[i + 2] = (Math.random() - 0.5) * 70;
        }
        dustGeo.setAttribute('position', new THREE.BufferAttribute(dustPos, 3));
        const dustMat = new THREE.PointsMaterial({
            color: 0x88e5ff,
            size: 1.8,
            transparent: true,
            opacity: 0.55,
            blending: THREE.AdditiveBlending
        });
        const dustParticles = new THREE.Points(dustGeo, dustMat);
        scene.add(dustParticles);

        /* -------------------------------------------------------------
           SPACECRAFT & DETAILED NASA 3D COCKPIT MODEL
           ------------------------------------------------------------- */
        const ship = new THREE.Group();
        scene.add(ship);

        const hullMat = new THREE.MeshStandardMaterial({
            color: 0xbdd3e3,
            metalness: 0.85,
            roughness: 0.25
        });

        const darkTileMat = new THREE.MeshStandardMaterial({
            color: 0x161c24,
            metalness: 0.6,
            roughness: 0.7
        });

        // Forward Aerodynamic Nose Cone
        const noseCone = new THREE.Mesh(
            new THREE.ConeGeometry(1.05, 3.2, 16),
            hullMat
        );
        noseCone.rotation.x = -Math.PI / 2;
        noseCone.position.set(0, -0.1, -2.6);
        ship.add(noseCone);

        // Lower heat shield
        const heatShield = new THREE.Mesh(
            new THREE.BoxGeometry(1.4, 0.22, 4.2),
            darkTileMat
        );
        heatShield.position.set(0, -0.48, 0.3);
        ship.add(heatShield);

        // Aft fuselage / Service module
        const aftFuselage = new THREE.Mesh(
            new THREE.CylinderGeometry(1.2, 1.35, 2.5, 16),
            hullMat
        );
        aftFuselage.rotation.x = Math.PI / 2;
        aftFuselage.position.set(0, 0.08, 1.55);
        ship.add(aftFuselage);

        // Wings
        const wingGeo = new THREE.BoxGeometry(3.6, 0.12, 1.8);
        const wingL = new THREE.Mesh(wingGeo, hullMat);
        wingL.position.set(-2.4, -0.05, 0.8);
        wingL.rotation.y = 0.12;
        ship.add(wingL);

        const wingR = new THREE.Mesh(wingGeo, hullMat);
        wingR.position.set(2.4, -0.05, 0.8);
        wingR.rotation.y = -0.12;
        ship.add(wingR);

        // Twin fins
        const finGeo = new THREE.BoxGeometry(0.1, 1.2, 1.2);
        const finL = new THREE.Mesh(finGeo, hullMat);
        finL.position.set(-1.1, 0.6, 2.0);
        finL.rotation.z = 0.35;
        finL.rotation.y = 0.08;
        ship.add(finL);

        const finR = new THREE.Mesh(finGeo, hullMat);
        finR.position.set(1.1, 0.6, 2.0);
        finR.rotation.z = -0.35;
        finR.rotation.y = -0.08;
        ship.add(finR);

        // Wingtip beacons
        const navLightL = new THREE.PointLight(0xff2233, 1, 8);
        navLightL.position.set(-4.2, 0, 0.8);
        ship.add(navLightL);

        const navLightR = new THREE.PointLight(0x00ff66, 1, 8);
        navLightR.position.set(4.2, 0, 0.8);
        ship.add(navLightR);

        // Thruster group
        const thrusterGroup = new THREE.Group();
        thrusterGroup.position.set(0, 0, 2.9);
        ship.add(thrusterGroup);

        const bellGeo = new THREE.CylinderGeometry(0.38, 0.65, 0.8, 16, 1, true);
        const bellMat = new THREE.MeshStandardMaterial({
            color: 0x1f2630,
            metalness: 0.9,
            roughness: 0.2
        });
        const bellL = new THREE.Mesh(bellGeo, bellMat);
        bellL.rotation.x = Math.PI / 2;
        bellL.position.set(-0.45, 0, 0);
        thrusterGroup.add(bellL);

        const bellR = new THREE.Mesh(bellGeo, bellMat);
        bellR.rotation.x = Math.PI / 2;
        bellR.position.set(0.45, 0, 0);
        thrusterGroup.add(bellR);

        // Supersonic plasma flame cones
        const flameGeo = new THREE.ConeGeometry(0.48, 3.2, 16);
        const flameMat = new THREE.MeshBasicMaterial({
            color: 0x00f0ff,
            transparent: true,
            opacity: 0.85,
            blending: THREE.AdditiveBlending
        });

        const flameMeshL = new THREE.Mesh(flameGeo, flameMat);
        flameMeshL.rotation.x = -Math.PI / 2;
        flameMeshL.position.set(-0.45, 0, 1.8);
        thrusterGroup.add(flameMeshL);

        const flameMeshR = new THREE.Mesh(flameGeo, flameMat);
        flameMeshR.rotation.x = -Math.PI / 2;
        flameMeshR.position.set(0.45, 0, 1.8);
        thrusterGroup.add(flameMeshR);

        // Supersonic shock diamonds
        const shockGeo = new THREE.TorusGeometry(0.18, 0.05, 8, 16);
        const shockMat = new THREE.MeshBasicMaterial({ color: 0xffffff, blending: THREE.AdditiveBlending });
        const shock1 = new THREE.Mesh(shockGeo, shockMat);
        shock1.position.set(-0.45, 0, 1.0);
        thrusterGroup.add(shock1);
        const shock2 = new THREE.Mesh(shockGeo, shockMat);
        shock2.position.set(0.45, 0, 1.0);
        thrusterGroup.add(shock2);

        const engineLight = new THREE.PointLight(0x00dfff, 3, 24);
        engineLight.position.set(0, 0, 1.5);
        thrusterGroup.add(engineLight);

        // Trailing sparks
        const exhaustCount = 200;
        const exhaustGeo = new THREE.BufferGeometry();
        const exhaustPos = new Float32Array(exhaustCount * 3);
        for (let i = 0; i < exhaustCount; i++) {
            exhaustPos[i * 3] = (Math.random() - 0.5) * 0.8;
            exhaustPos[i * 3 + 1] = (Math.random() - 0.5) * 0.4;
            exhaustPos[i * 3 + 2] = 2.9 + Math.random() * 5.0;
        }
        exhaustGeo.setAttribute('position', new THREE.BufferAttribute(exhaustPos, 3));
        const exhaustMat = new THREE.PointsMaterial({
            color: 0x00f0ff,
            size: 2.2,
            transparent: true,
            opacity: 0.7,
            blending: THREE.AdditiveBlending
        });
        const exhaustParticles = new THREE.Points(exhaustGeo, exhaustMat);
        ship.add(exhaustParticles);

        /* -------------------------------------------------------------
           COCKPIT INTERIOR (DASHBOARD, MFDS, GLOWING CONTROLS, WINDSHIELD)
           ------------------------------------------------------------- */
        const cockpitGroup = new THREE.Group();
        ship.add(cockpitGroup);

        const cockpitTub = new THREE.Mesh(
            new THREE.BoxGeometry(1.5, 0.5, 2.0),
            new THREE.MeshStandardMaterial({ color: 0x0f151e, roughness: 0.85 })
        );
        cockpitTub.position.set(0, -0.05, -0.3);
        cockpitGroup.add(cockpitTub);

        const seatGroup = new THREE.Group();
        seatGroup.position.set(0, 0.22, 0.15);
        const seatBack = new THREE.Mesh(
            new THREE.BoxGeometry(0.7, 1.0, 0.18),
            new THREE.MeshStandardMaterial({ color: 0x1b232e, roughness: 0.9 })
        );
        seatGroup.add(seatBack);
        const headRest = new THREE.Mesh(
            new THREE.BoxGeometry(0.38, 0.32, 0.16),
            new THREE.MeshStandardMaterial({ color: 0x273344, roughness: 0.9 })
        );
        headRest.position.set(0, 0.62, -0.02);
        seatGroup.add(headRest);
        cockpitGroup.add(seatGroup);

        const dashBase = new THREE.Mesh(
            new THREE.BoxGeometry(1.65, 0.38, 0.75),
            new THREE.MeshStandardMaterial({ color: 0x121720, roughness: 0.8, metalness: 0.3 })
        );
        dashBase.position.set(0, 0.25, -0.92);
        dashBase.rotation.x = -0.32;
        cockpitGroup.add(dashBase);

        const browStrip = new THREE.Mesh(
            new THREE.BoxGeometry(1.62, 0.025, 0.04),
            new THREE.MeshBasicMaterial({ color: 0x00f0ff })
        );
        browStrip.position.set(0, 0.44, -0.84);
        cockpitGroup.add(browStrip);

        // Three In-Cockpit MFD Screens
        const navCanvas = document.createElement('canvas'); navCanvas.width = 384; navCanvas.height = 384;
        const pfdCanvas = document.createElement('canvas'); pfdCanvas.width = 384; pfdCanvas.height = 384;
        const sysCanvas = document.createElement('canvas'); sysCanvas.width = 384; sysCanvas.height = 384;

        const navCtx = navCanvas.getContext('2d');
        const pfdCtx = pfdCanvas.getContext('2d');
        const sysCtx = sysCanvas.getContext('2d');

        const texNav = new THREE.CanvasTexture(navCanvas);
        const texPFD = new THREE.CanvasTexture(pfdCanvas);
        const texSys = new THREE.CanvasTexture(sysCanvas);

        const screenGeoSide = new THREE.BoxGeometry(0.38, 0.32, 0.01);
        const screenGeoCenter = new THREE.BoxGeometry(0.42, 0.34, 0.01);

        const screenL = new THREE.Mesh(screenGeoSide, new THREE.MeshBasicMaterial({ map: texNav }));
        screenL.position.set(-0.52, 0.27, -0.93);
        screenL.rotation.x = -0.35;
        screenL.rotation.y = 0.16;
        cockpitGroup.add(screenL);

        const screenC = new THREE.Mesh(screenGeoCenter, new THREE.MeshBasicMaterial({ map: texPFD }));
        screenC.position.set(0.0, 0.28, -0.97);
        screenC.rotation.x = -0.35;
        cockpitGroup.add(screenC);

        const screenR = new THREE.Mesh(screenGeoSide, new THREE.MeshBasicMaterial({ map: texSys }));
        screenR.position.set(0.52, 0.27, -0.93);
        screenR.rotation.x = -0.35;
        screenR.rotation.y = -0.16;
        cockpitGroup.add(screenR);

        // Annunciator CWP
        const cwpGroup = new THREE.Group();
        cwpGroup.position.set(0, 0.42, -0.90);
        cwpGroup.rotation.x = -0.35;
        const cwpColors = [0x00f0ff, 0x00ff88, 0x00f0ff, 0xffaa00, 0x00f0ff, 0x00ff88];
        for (let i = 0; i < 6; i++) {
            const tile = new THREE.Mesh(
                new THREE.BoxGeometry(0.065, 0.024, 0.01),
                new THREE.MeshBasicMaterial({ color: cwpColors[i] })
            );
            tile.position.set((i - 2.5) * 0.075, 0, 0);
            cwpGroup.add(tile);
        }
        cockpitGroup.add(cwpGroup);

        // Glowing Switchboard Arrays
        const switchGeo = new THREE.BoxGeometry(0.028, 0.028, 0.02);
        const switchMatCyan = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
        const switchMatGreen = new THREE.MeshBasicMaterial({ color: 0x00ff88 });
        const switchMatAmber = new THREE.MeshBasicMaterial({ color: 0xffaa00 });

        for (let row = 0; row < 2; row++) {
            for (let col = 0; col < 12; col++) {
                const sMat = (col % 3 === 0) ? switchMatCyan : (col % 3 === 1 ? switchMatGreen : switchMatAmber);
                const sw = new THREE.Mesh(switchGeo, sMat);
                sw.position.set(-0.5 + col * 0.09, 0.12 + row * 0.04, -0.84);
                sw.rotation.x = -0.35;
                cockpitGroup.add(sw);
            }
        }

        // Flight Control Stick
        const stickBase = new THREE.Group();
        stickBase.position.set(0, 0.12, -0.58);
        const stickBoot = new THREE.Mesh(
            new THREE.CylinderGeometry(0.06, 0.09, 0.08, 12),
            new THREE.MeshStandardMaterial({ color: 0x1a212c, roughness: 0.9 })
        );
        stickBase.add(stickBoot);

        const flightStick = new THREE.Group();
        const stickShaft = new THREE.Mesh(
            new THREE.CylinderGeometry(0.018, 0.018, 0.28, 10),
            new THREE.MeshStandardMaterial({ color: 0x8898a8, metalness: 0.9, roughness: 0.2 })
        );
        stickShaft.position.y = 0.14;
        flightStick.add(stickShaft);

        const stickGrip = new THREE.Mesh(
            new THREE.BoxGeometry(0.05, 0.14, 0.06),
            new THREE.MeshStandardMaterial({ color: 0x1f2733, roughness: 0.8 })
        );
        stickGrip.position.set(0, 0.25, 0);
        flightStick.add(stickGrip);

        const triggerBtn = new THREE.Mesh(
            new THREE.BoxGeometry(0.02, 0.03, 0.02),
            new THREE.MeshBasicMaterial({ color: 0xff2233 })
        );
        triggerBtn.position.set(0, 0.27, -0.035);
        flightStick.add(triggerBtn);
        stickBase.add(flightStick);
        cockpitGroup.add(stickBase);

        // Throttle Quadrant
        const throttleBase = new THREE.Mesh(
            new THREE.BoxGeometry(0.18, 0.1, 0.38),
            new THREE.MeshStandardMaterial({ color: 0x151b24, roughness: 0.8 })
        );
        throttleBase.position.set(-0.62, 0.22, -0.55);
        cockpitGroup.add(throttleBase);

        const throttleLever = new THREE.Group();
        throttleLever.position.set(-0.62, 0.28, -0.55);
        const leverHandle = new THREE.Mesh(
            new THREE.BoxGeometry(0.14, 0.05, 0.06),
            new THREE.MeshStandardMaterial({ color: 0x334455, roughness: 0.6 })
        );
        throttleLever.add(leverHandle);
        cockpitGroup.add(throttleLever);

        // Overhead Switch Console
        const overheadPanel = new THREE.Mesh(
            new THREE.BoxGeometry(0.5, 0.12, 0.85),
            new THREE.MeshStandardMaterial({ color: 0x121822, roughness: 0.7 })
        );
        overheadPanel.position.set(0, 0.92, -0.45);
        overheadPanel.rotation.x = 0.18;
        cockpitGroup.add(overheadPanel);

        // Structural Canopy Frame
        const strutMat = new THREE.MeshStandardMaterial({
            color: 0x1a212d,
            metalness: 0.8,
            roughness: 0.3
        });

        const pillarL = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.3), strutMat);
        pillarL.position.set(-0.72, 0.58, -0.65);
        pillarL.rotation.z = -0.38;
        pillarL.rotation.x = -0.42;
        cockpitGroup.add(pillarL);

        const pillarR = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.3), strutMat);
        pillarR.position.set(0.72, 0.58, -0.65);
        pillarR.rotation.z = 0.38;
        pillarR.rotation.x = -0.42;
        cockpitGroup.add(pillarR);

        const centerPost = new THREE.Mesh(new THREE.CylinderGeometry(0.025, 0.025, 1.1), strutMat);
        centerPost.position.set(0, 0.68, -0.72);
        centerPost.rotation.x = -0.54;
        cockpitGroup.add(centerPost);

        // Large Transparent Glass Windshield
        const glassMat = new THREE.MeshPhysicalMaterial({
            color: 0x9be8ff,
            transparent: true,
            opacity: 0.16,
            roughness: 0.05,
            metalness: 0.12,
            transmission: 0.88,
            reflectivity: 0.95,
            clearcoat: 1.0,
            clearcoatRoughness: 0.04
        });

        const frontGlass = new THREE.Mesh(
            new THREE.BoxGeometry(1.5, 0.75, 0.015),
            glassMat
        );
        frontGlass.position.set(0, 0.68, -0.75);
        frontGlass.rotation.x = -0.52;
        cockpitGroup.add(frontGlass);

        const glassL = new THREE.Mesh(
            new THREE.BoxGeometry(0.015, 0.65, 0.95),
            glassMat
        );
        glassL.position.set(-0.76, 0.6, -0.45);
        glassL.rotation.z = -0.18;
        cockpitGroup.add(glassL);

        const glassR = new THREE.Mesh(
            new THREE.BoxGeometry(0.015, 0.65, 0.95),
            glassMat
        );
        glassR.position.set(0.76, 0.6, -0.45);
        glassR.rotation.z = 0.18;
        cockpitGroup.add(glassR);

        // Exterior canopy dome for 3rd person views
        const extCanopy = new THREE.Mesh(
            new THREE.SphereGeometry(0.85, 24, 16),
            glassMat
        );
        extCanopy.position.set(0, 0.48, -0.42);
        extCanopy.scale.set(0.9, 0.65, 1.3);
        ship.add(extCanopy);

        // Projected Holographic HUD Reticle on front glass
        const hudCanvas = document.createElement('canvas'); hudCanvas.width = 256; hudCanvas.height = 256;
        const hudCtx = hudCanvas.getContext('2d');
        const hudTex = new THREE.CanvasTexture(hudCanvas);
        const hudReticleMesh = new THREE.Mesh(
            new THREE.PlaneGeometry(0.5, 0.5),
            new THREE.MeshBasicMaterial({
                map: hudTex,
                transparent: true,
                blending: THREE.AdditiveBlending,
                opacity: 0.8
            })
        );
        hudReticleMesh.position.set(0, 0.64, -0.76);
        hudReticleMesh.rotation.x = -0.52;
        cockpitGroup.add(hudReticleMesh);

        function drawHoloHUD() {
            hudCtx.clearRect(0, 0, 256, 256);
            hudCtx.strokeStyle = 'rgba(0, 240, 255, 0.75)';
            hudCtx.lineWidth = 1.5;
            hudCtx.fillStyle = 'rgba(0, 240, 255, 0.75)';
            hudCtx.font = '10px monospace';

            hudCtx.beginPath();
            hudCtx.arc(128, 128, 8, 0, Math.PI * 2);
            hudCtx.moveTo(112, 128); hudCtx.lineTo(120, 128);
            hudCtx.moveTo(136, 128); hudCtx.lineTo(144, 128);
            hudCtx.moveTo(128, 112); hudCtx.lineTo(128, 120);
            hudCtx.moveTo(128, 136); hudCtx.lineTo(128, 144);
            hudCtx.stroke();

            const pOff = (ship.rotation.x % (Math.PI / 4)) * 70;
            hudCtx.beginPath();
            hudCtx.moveTo(85, 100 + pOff); hudCtx.lineTo(110, 100 + pOff);
            hudCtx.moveTo(146, 100 + pOff); hudCtx.lineTo(171, 100 + pOff);
            hudCtx.moveTo(95, 156 + pOff); hudCtx.lineTo(115, 156 + pOff);
            hudCtx.moveTo(141, 156 + pOff); hudCtx.lineTo(161, 156 + pOff);
            hudCtx.stroke();

            hudCtx.fillText("HUD // ORION-3D", 80, 45);
            hudTex.needsUpdate = true;
        }

        const cockpitGlow = new THREE.PointLight(0x00f0ff, 1.8, 2.4);
        cockpitGlow.position.set(0, 0.44, -0.6);
        cockpitGroup.add(cockpitGlow);

        /* -------------------------------------------------------------
           DYNAMIC MFD SCREEN RENDERING ROUTINES
           ------------------------------------------------------------- */
        let radarSweep = 0;

        function updateMFDs(speedVal, altVal, fuelVal, o2Val, targetPlanetName) {
            radarSweep += 0.05;

            // 1. LEFT MFD: RADAR & NAVIGATION
            navCtx.fillStyle = '#020d18';
            navCtx.fillRect(0, 0, 384, 384);

            navCtx.strokeStyle = 'rgba(0, 220, 255, 0.25)';
            navCtx.lineWidth = 1;

            const cx = 192, cy = 192;
            [45, 95, 145].forEach(r => {
                navCtx.beginPath();
                navCtx.arc(cx, cy, r, 0, Math.PI * 2);
                navCtx.stroke();
            });

            navCtx.beginPath();
            navCtx.moveTo(cx - 155, cy); navCtx.lineTo(cx + 155, cy);
            navCtx.moveTo(cx, cy - 155); navCtx.lineTo(cx, cy + 155);
            navCtx.stroke();

            navCtx.strokeStyle = 'rgba(0, 255, 230, 0.85)';
            navCtx.beginPath();
            navCtx.moveTo(cx, cy);
            navCtx.lineTo(cx + Math.cos(radarSweep) * 145, cy + Math.sin(radarSweep) * 145);
            navCtx.stroke();

            navCtx.fillStyle = '#00f0ff';
            navCtx.font = 'bold 13px monospace';
            navCtx.fillText("ORBITAL RADAR // NAV-1", 16, 24);
            navCtx.font = '11px monospace';
            navCtx.fillStyle = '#7ad8ff';
            navCtx.fillText(`TGT: [ ${targetPlanetName.toUpperCase()} ]`, 16, 42);

            Object.entries(planets).forEach(([pName, pObj]) => {
                const rel = pObj.position.clone().sub(ship.position);
                const scale = 0.065;
                const bx = cx + rel.x * scale;
                const by = cy + rel.z * scale;

                if (Math.hypot(bx - cx, by - cy) < 155) {
                    const isTgt = (pName === targetPlanetName);
                    navCtx.fillStyle = isTgt ? '#00ffaa' : '#00aacc';
                    navCtx.beginPath();
                    navCtx.arc(bx, by, isTgt ? 5 : 3, 0, Math.PI * 2);
                    navCtx.fill();

                    navCtx.font = '9px monospace';
                    navCtx.fillText(pName.toUpperCase(), bx + 6, by + 3);

                    if (isTgt) {
                        navCtx.strokeStyle = '#00ffaa';
                        navCtx.strokeRect(bx - 7, by - 7, 14, 14);
                    }
                }
            });

            texNav.needsUpdate = true;

            // 2. CENTER MFD: PRIMARY FLIGHT DISPLAY (PFD)
            pfdCtx.fillStyle = '#010914';
            pfdCtx.fillRect(0, 0, 384, 384);

            const pitchPix = (ship.rotation.x % Math.PI) * 120;
            const rollRad = ship.rotation.z;

            pfdCtx.save();
            pfdCtx.translate(192, 192);
            pfdCtx.rotate(rollRad);

            pfdCtx.fillStyle = '#08233e';
            pfdCtx.fillRect(-160, -160 + pitchPix, 320, 160);
            pfdCtx.fillStyle = '#04101e';
            pfdCtx.fillRect(-160, 0 + pitchPix, 320, 160);

            pfdCtx.strokeStyle = '#00f0ff';
            pfdCtx.lineWidth = 2;
            pfdCtx.beginPath();
            pfdCtx.moveTo(-110, pitchPix); pfdCtx.lineTo(110, pitchPix);
            pfdCtx.moveTo(-45, pitchPix - 30); pfdCtx.lineTo(45, pitchPix - 30);
            pfdCtx.moveTo(-45, pitchPix + 30); pfdCtx.lineTo(45, pitchPix + 30);
            pfdCtx.stroke();

            pfdCtx.restore();

            pfdCtx.strokeStyle = '#00ffaa';
            pfdCtx.lineWidth = 2;
            pfdCtx.beginPath();
            pfdCtx.arc(192, 192, 12, 0, Math.PI * 2);
            pfdCtx.moveTo(155, 192); pfdCtx.lineTo(180, 192);
            pfdCtx.moveTo(204, 192); pfdCtx.lineTo(229, 192);
            pfdCtx.stroke();

            pfdCtx.fillStyle = 'rgba(2, 20, 40, 0.7)';
            pfdCtx.fillRect(16, 70, 75, 240);
            pfdCtx.fillRect(293, 70, 75, 240);
            pfdCtx.strokeStyle = 'rgba(0, 240, 255, 0.4)';
            pfdCtx.strokeRect(16, 70, 75, 240);
            pfdCtx.strokeRect(293, 70, 75, 240);

            pfdCtx.fillStyle = '#00f0ff';
            pfdCtx.font = 'bold 12px monospace';
            pfdCtx.fillText("SPD KM/S", 22, 90);
            pfdCtx.font = 'bold 17px monospace';
            pfdCtx.fillText((speedVal * 100).toFixed(0), 22, 196);

            pfdCtx.font = 'bold 12px monospace';
            pfdCtx.fillText("ALT KM", 304, 90);
            pfdCtx.font = 'bold 15px monospace';
            pfdCtx.fillText(Math.round(altVal), 302, 196);

            pfdCtx.font = 'bold 13px monospace';
            pfdCtx.fillText("PFD-1 // AP-OFF // SAS-ON", 16, 24);

            texPFD.needsUpdate = true;

            // 3. RIGHT MFD: SYSTEMS & LIFE SUPPORT
            sysCtx.fillStyle = '#020d18';
            sysCtx.fillRect(0, 0, 384, 384);

            sysCtx.fillStyle = '#00f0ff';
            sysCtx.font = 'bold 13px monospace';
            sysCtx.fillText("LIFE SUPPORT & DIAGNOSTICS", 16, 24);

            sysCtx.fillStyle = '#a6e2f7';
            sysCtx.font = '11px monospace';
            sysCtx.fillText(`OXYGEN SUPPLY: ${Math.round(o2Val)}%`, 16, 60);
            sysCtx.fillStyle = '#081e30';
            sysCtx.fillRect(16, 70, 350, 14);
            sysCtx.fillStyle = (o2Val < 20) ? '#ff3344' : '#00e5ff';
            sysCtx.fillRect(16, 70, (o2Val / 100) * 350, 14);

            sysCtx.fillStyle = '#a6e2f7';
            sysCtx.fillText(`PROPELLANT TANK: ${Math.round(fuelVal)}%`, 16, 120);
            sysCtx.fillStyle = '#081e30';
            sysCtx.fillRect(16, 130, 350, 14);
            sysCtx.fillStyle = (fuelVal < 20) ? '#ffaa00' : '#00ffaa';
            sysCtx.fillRect(16, 130, (fuelVal / 100) * 350, 14);

            sysCtx.fillStyle = '#00f0ff';
            sysCtx.fillText(`CABIN PRESSURE: 101.3 kPa [NOMINAL]`, 16, 180);
            sysCtx.fillText(`REACTOR CORE: 412 K [STABLE]`, 16, 210);
            sysCtx.fillText(`MAIN ENGINE: ${fuelVal > 0 ? 'ARMED' : 'OFFLINE'}`, 16, 240);
            sysCtx.fillText(`RCS SYSTEM: 16/16 OPERATIONAL`, 16, 270);
            sysCtx.fillText(`POWER BUS: 28.4 VDC [NOMINAL]`, 16, 300);

            const sysOk = (fuelVal > 15 && o2Val > 15);
            sysCtx.fillStyle = sysOk ? 'rgba(0, 255, 170, 0.15)' : 'rgba(255, 50, 70, 0.2)';
            sysCtx.strokeStyle = sysOk ? '#00ffaa' : '#ff3344';
            sysCtx.fillRect(16, 330, 350, 35);
            sysCtx.strokeRect(16, 330, 350, 35);
            sysCtx.fillStyle = sysOk ? '#00ffaa' : '#ff3344';
            sysCtx.font = 'bold 12px monospace';
            sysCtx.fillText(sysOk ? "SYSTEM STATUS: ALL SYSTEMS NOMINAL" : "CAUTION: TELEMETRY ALERT", 32, 352);

            texSys.needsUpdate = true;
        }

        /* -------------------------------------------------------------
           FLIGHT SYSTEM & THREE FULLY FUNCTIONAL CAMERA MODES
           ------------------------------------------------------------- */
        const keys = {};
        window.addEventListener('keydown', e => {
            keys[e.key.toLowerCase()] = true;
            if (e.code === "Space") e.preventDefault();

            // C key cycles camera mode
            if (e.key.toLowerCase() === 'c') {
                cycleCameraMode();
            }

            // M key toggles Solar System Map
            if (e.key.toLowerCase() === 'm') {
                toggleSolarMap();
            }

            // O key toggles Autopilot
            if (e.key.toLowerCase() === 'o') {
                toggleAutopilot();
            }

            // L key triggers Quick Landing
            if (e.key.toLowerCase() === 'l') {
                triggerQuickLanding();
            }

            if (e.key.toLowerCase() === 'p') {
                togglePause();
            }

            if (e.key.toLowerCase() === 'r') {
                resetFlight();
            }

            if (e.key.toLowerCase() === 'h') {
                toggleHUD();
            }
        });

        window.addEventListener('keyup', e => {
            keys[e.key.toLowerCase()] = false;
        });

        let speed = 0;
        let fuel = 100;
        let oxygen = 100;
        let hullHealth = 100;
        let missionScore = 0;
        let active = false;
        let paused = false;
        let boost = false;
        let autopilotActive = false;
        let missionTarget = "Moon";

        const velocity = new THREE.Vector3();
        const direction = new THREE.Vector3(0, 0, -1);
        const clock = new THREE.Clock();

        // 3 CAMERA MODES: 'cockpit', 'chase', 'external'
        let cameraMode = 'cockpit';
        const cockpitEyeOffset = new THREE.Vector3(0, 0.52, -0.32);
        let pilotHeadPan = { x: 0, y: 0 };

        // Chase view follow smoothing
        const chaseCamPos = new THREE.Vector3(0, 3.8, 14.0);

        // Wide external orbit camera
        let orbitTheta = 0.5;
        let orbitPhi = 1.25;
        let orbitDistance = 28.0;
        let isOrbitDragging = false;
        let lastMousePos = { x: 0, y: 0 };

        // Mouse flight steering
        let mouseSteerActive = false;
        let mouseNorm = { x: 0, y: 0 };
        const reticleEl = document.getElementById('flightReticle');

        // Window Mouse Handlers
        window.addEventListener('mousedown', e => {
            if (cameraMode === 'external' && !e.target.closest('.topbar, .hud-bracket-left, .hud-bracket-right, #startScreen, #missionCompleteModal, #solarSystemMap, #surfaceExplorationView, #landingCinematicOverlay, #missionTasksDrawer')) {
                isOrbitDragging = true;
                lastMousePos = { x: e.clientX, y: e.clientY };
            }
        });

        window.addEventListener('mouseup', () => {
            isOrbitDragging = false;
        });

        window.addEventListener('mousemove', e => {
            if (isOrbitDragging && cameraMode === 'external') {
                const dx = e.clientX - lastMousePos.x;
                const dy = e.clientY - lastMousePos.y;
                orbitTheta -= dx * 0.007;
                orbitPhi = THREE.MathUtils.clamp(orbitPhi - dy * 0.007, 0.15, Math.PI - 0.15);
                lastMousePos = { x: e.clientX, y: e.clientY };
                return;
            }

            const nx = (e.clientX - window.innerWidth / 2) / (window.innerWidth / 2);
            const ny = (e.clientY - window.innerHeight / 2) / (window.innerHeight / 2);

            if (mouseSteerActive) {
                mouseNorm.x = nx;
                mouseNorm.y = ny;
                reticleEl.style.transform = `translate(calc(-50% + ${nx * 45}px), calc(-50% + ${ny * 45}px))`;
            } else if (cameraMode === 'cockpit') {
                pilotHeadPan.x = THREE.MathUtils.clamp(-nx * 0.35, -0.4, 0.4);
                pilotHeadPan.y = THREE.MathUtils.clamp(-ny * 0.25, -0.3, 0.3);
            }
        });

        window.addEventListener('wheel', e => {
            if (cameraMode === 'external') {
                orbitDistance = THREE.MathUtils.clamp(orbitDistance + e.deltaY * 0.04, 12, 90);
            }
        }, { passive: true });

        // CAMERA MODE SWITCHER UI BUTTONS
        const btnCamCockpit = document.getElementById('btnCamCockpit');
        const btnCamChase = document.getElementById('btnCamChase');
        const btnCamExternal = document.getElementById('btnCamExternal');

        function setCameraMode(newMode) {
            audio.playClick();
            cameraMode = newMode;

            btnCamCockpit.classList.toggle('active', cameraMode === 'cockpit');
            btnCamChase.classList.toggle('active', cameraMode === 'chase');
            btnCamExternal.classList.toggle('active', cameraMode === 'external');

            // Hide canopy dome in cockpit view to prevent clipping
            extCanopy.visible = (cameraMode !== 'cockpit');
        }

        function cycleCameraMode() {
            if (cameraMode === 'cockpit') {
                setCameraMode('chase');
            } else if (cameraMode === 'chase') {
                setCameraMode('external');
            } else {
                setCameraMode('cockpit');
            }
        }

        btnCamCockpit.onclick = () => setCameraMode('cockpit');
        btnCamChase.onclick = () => setCameraMode('chase');
        btnCamExternal.onclick = () => setCameraMode('external');
        setCameraMode('cockpit');

        // HUD TOGGLE
        let hudVisible = true;
        const hudElement = document.getElementById('hud');
        const hudToggleBtn = document.getElementById('hudToggleBtn');
        function toggleHUD() {
            audio.playClick();
            hudVisible = !hudVisible;
            hudElement.classList.toggle('hud-hidden', !hudVisible);
        }
        hudToggleBtn.onclick = toggleHUD;

        // MOUSE STEER TOGGLE
        const mouseBtn = document.getElementById('mouseBtn');
        const mouseBtnText = document.getElementById('mouseBtnText');

        function toggleMouseSteer() {
            audio.playClick();
            mouseSteerActive = !mouseSteerActive;
            if (mouseSteerActive) {
                mouseBtn.classList.add('active');
                mouseBtnText.textContent = "STEER: ON";
                reticleEl.classList.add('active');
            } else {
                mouseBtn.classList.remove('active');
                mouseBtnText.textContent = "STEER";
                reticleEl.classList.remove('active');
                mouseNorm.x = 0;
                mouseNorm.y = 0;
            }
        }
        mouseBtn.onclick = toggleMouseSteer;

        // AUDIO TOGGLE
        const audioBtn = document.getElementById('audioBtn');
        const audioBtnText = document.getElementById('audioBtnText');
        audioBtn.onclick = () => {
            audio.init();
            audio.enabled = !audio.enabled;
            audioBtnText.textContent = audio.enabled ? "SOUND" : "MUTED";
            audioBtn.classList.toggle('active', audio.enabled);
        };

        // AUTOPILOT TOGGLE
        const autopilotBtn = document.getElementById('autopilotBtn');
        const autoBtnText = document.getElementById('autoBtnText');
        const autoStatusText = document.getElementById('autoStatusText');
        const hudAutopilotToggleBtn = document.getElementById('hudAutopilotToggleBtn');

        function toggleAutopilot() {
            audio.playClick();
            autopilotActive = !autopilotActive;
            if (autopilotActive) {
                autopilotBtn.classList.add('active');
                autoBtnText.textContent = "AUTO: ON";
                autoStatusText.textContent = "ENGAGED";
                autoStatusText.style.color = "#00ffaa";
                document.getElementById('message').textContent = `Autopilot locked onto ${missionTarget}. Aligning vector...`;
            } else {
                autopilotBtn.classList.remove('active');
                autoBtnText.textContent = "AUTO";
                autoStatusText.textContent = "STANDBY";
                autoStatusText.style.color = "#8be5ff";
                document.getElementById('message').textContent = "Manual pilot flight control restored.";
            }
        }
        autopilotBtn.onclick = toggleAutopilot;
        hudAutopilotToggleBtn.onclick = toggleAutopilot;

        // TOAST NOTICE HELPER
        const toastNotice = document.getElementById('toastNotice');
        let toastTimeout = null;
        function showToast(text) {
            toastNotice.textContent = text;
            toastNotice.classList.add('show');
            clearTimeout(toastTimeout);
            toastTimeout = setTimeout(() => {
                toastNotice.classList.remove('show');
            }, 3500);
        }

        function addScore(pts, reason) {
            missionScore += pts;
            document.getElementById('scoreText').textContent = `${missionScore.toLocaleString()} PTS`;
            audio.playSuccess();
            showToast(`★ +${pts} PTS // ${reason}`);
        }

        /* -------------------------------------------------------------
           TARGET SELECTION & START SCREEN
           ------------------------------------------------------------- */
        const startScreen = document.getElementById('startScreen');
        const playMissionBtn = document.getElementById('playMissionBtn');
        const startBtn = document.getElementById('startBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const resetBtn = document.getElementById('resetBtn');
        const menuBtn = document.getElementById('menuBtn');
        const topTargetName = document.getElementById('topTargetName');
        const planetSelect = document.getElementById('planetSelect');

        function setMissionTarget(targetName) {
            if (!planetData[targetName]) return;
            missionTarget = targetName;
            planetSelect.value = targetName;
            topTargetName.textContent = targetName.toUpperCase();
            document.getElementById('markerTargetName').textContent = targetName.toUpperCase();

            document.querySelectorAll('.dest-card').forEach(c => {
                c.classList.toggle('selected', c.dataset.target === targetName);
            });

            updateMapSidebar(targetName);
            updateDrawerTasks();
        }

        document.querySelectorAll('.dest-card').forEach(card => {
            card.onclick = () => {
                audio.playClick();
                setMissionTarget(card.dataset.target);
            };
        });

        planetSelect.onchange = (e) => {
            audio.playClick();
            setMissionTarget(e.target.value);
            document.getElementById('message').textContent = "Target locked: " + missionTarget;
        };

        function launchGameMission() {
            audio.playClick();
            startScreen.classList.add('hidden');
            active = true;
            paused = false;
            document.getElementById('missionStatus').textContent = "EN ROUTE";
            document.getElementById('flightMode').textContent = "ACTIVE";
            document.getElementById('message').textContent = "Course locked to " + missionTarget + ". All systems nominal.";
            updateDrawerTasks();
        }

        playMissionBtn.onclick = launchGameMission;
        startBtn.onclick = () => {
            if (!active) launchGameMission();
            else document.getElementById('message').textContent = "Mission currently active.";
        };

        menuBtn.onclick = () => {
            audio.playClick();
            startScreen.classList.remove('hidden');
        };

        function togglePause() {
            if (!active) return;
            audio.playClick();
            paused = !paused;
            pauseBtn.querySelector('span:last-child').textContent = paused ? "RESUME" : "PAUSE";
            document.getElementById('message').textContent = paused ? "Flight paused" : "Flight resumed";
            document.getElementById('flightMode').textContent = paused ? "PAUSED" : "ACTIVE";
        }
        pauseBtn.onclick = togglePause;

        function resetFlight() {
            audio.playClick();
            speed = 0;
            fuel = 100;
            oxygen = 100;
            hullHealth = 100;
            active = false;
            paused = false;
            autopilotActive = false;

            velocity.set(0, 0, 0);
            ship.position.set(0, 0, 0);
            ship.rotation.set(0, 0, 0);

            autopilotBtn.classList.remove('active');
            autoBtnText.textContent = "AUTO";
            autoStatusText.textContent = "STANDBY";
            autoStatusText.style.color = "#8be5ff";

            document.getElementById('missionStatus').textContent = "STANDBY";
            document.getElementById('flightMode').textContent = "STANDBY";
            document.getElementById('message').textContent = "Flight deck reset. Systems online.";
            pauseBtn.querySelector('span:last-child').textContent = "PAUSE";
            document.getElementById('alertBanner').classList.remove('show');
            document.getElementById('missionCompleteModal').classList.remove('active');
        }
        resetBtn.onclick = resetFlight;

        /* -------------------------------------------------------------
           MISSION TASKS CHECKLIST SYSTEM
           ------------------------------------------------------------- */
        const tasksBtn = document.getElementById('tasksBtn');
        const missionTasksDrawer = document.getElementById('missionTasksDrawer');
        const drawerCloseBtn = document.getElementById('drawerCloseBtn');
        const drawerTaskList = document.getElementById('drawerTaskList');

        function toggleTasksDrawer() {
            audio.playClick();
            const isOpen = missionTasksDrawer.classList.contains('show');
            if (isOpen) {
                missionTasksDrawer.classList.remove('show');
            } else {
                updateDrawerTasks();
                missionTasksDrawer.classList.add('show');
            }
        }
        tasksBtn.onclick = toggleTasksDrawer;
        drawerCloseBtn.onclick = () => missionTasksDrawer.classList.remove('show');

        function updateDrawerTasks() {
            const data = planetData[missionTarget] || planetData["Moon"];
            drawerTaskList.innerHTML = '';
            data.tasks.forEach(task => {
                const item = document.createElement('div');
                item.className = 'drawer-task-item' + (task.completed ? ' completed' : '');

                const statusClass = task.completed ? 'completed' : 'in-progress';
                const statusLabel = task.completed ? 'COMPLETED' : 'IN PROGRESS';

                item.innerHTML = `
                    <div style="display:flex; flex-direction:column; gap:2px;">
                        <span style="font-size:11px; font-weight:700; color:#fff;">${task.title}</span>
                        <span style="font-size:9px; color:var(--gold-accent); font-family:var(--font-mono);">+${task.pts} PTS</span>
                    </div>
                    <span class="status-pill ${statusClass}">${statusLabel}</span>
                `;
                drawerTaskList.appendChild(item);
            });
        }

        /* -------------------------------------------------------------
           INTERACTIVE SOLAR SYSTEM MAP ENGINE (#solarSystemMap)
           ------------------------------------------------------------- */
        const solarMapModal = document.getElementById('solarSystemMap');
        const mapBtn = document.getElementById('mapBtn');
        const closeMapBtn = document.getElementById('closeMapBtn');
        const solarMapCanvas = document.getElementById('solarMapCanvas');
        const mapCtx = solarMapCanvas.getContext('2d');

        let mapOpen = false;
        let mapZoom = 1.0;
        let mapPan = { x: 0, y: 0 };
        let mapDragging = false;
        let mapDragStart = { x: 0, y: 0 };
        let mapRotationAngle = 0;

        function toggleSolarMap() {
            audio.playClick();
            mapOpen = !mapOpen;
            solarMapModal.classList.toggle('active', mapOpen);
            if (mapOpen) {
                resizeMapCanvas();
                updateMapSidebar(missionTarget);
            }
        }
        mapBtn.onclick = toggleSolarMap;
        closeMapBtn.onclick = toggleSolarMap;

        function resizeMapCanvas() {
            const rect = solarMapCanvas.parentElement.getBoundingClientRect();
            solarMapCanvas.width = rect.width;
            solarMapCanvas.height = rect.height;
        }
        window.addEventListener('resize', () => {
            if (mapOpen) resizeMapCanvas();
        });

        // Map pan and zoom handlers
        solarMapCanvas.addEventListener('mousedown', e => {
            mapDragging = true;
            mapDragStart.x = e.clientX - mapPan.x;
            mapDragStart.y = e.clientY - mapPan.y;
        });

        window.addEventListener('mouseup', () => { mapDragging = false; });

        window.addEventListener('mousemove', e => {
            if (mapDragging && mapOpen) {
                mapPan.x = e.clientX - mapDragStart.x;
                mapPan.y = e.clientY - mapDragStart.y;
            }
        });

        solarMapCanvas.addEventListener('wheel', e => {
            e.preventDefault();
            const factor = e.deltaY < 0 ? 1.15 : 0.87;
            mapZoom = THREE.MathUtils.clamp(mapZoom * factor, 0.4, 4.0);
        }, { passive: false });

        document.getElementById('mapZoomIn').onclick = () => { mapZoom = Math.min(mapZoom * 1.25, 4.0); };
        document.getElementById('mapZoomOut').onclick = () => { mapZoom = Math.max(mapZoom * 0.8, 0.4); };
        document.getElementById('mapRotate').onclick = () => { mapRotationAngle += Math.PI / 4; };
        document.getElementById('mapReset').onclick = () => { mapZoom = 1.0; mapPan.x = 0; mapPan.y = 0; mapRotationAngle = 0; };
        document.getElementById('mapCenterShip').onclick = () => {
            mapPan.x = -ship.position.x * 0.18;
            mapPan.y = -ship.position.z * 0.18;
        };

        // Map Planet Click Detection
        solarMapCanvas.addEventListener('click', e => {
            const rect = solarMapCanvas.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const clickY = e.clientY - rect.top;
            const cx = solarMapCanvas.width / 2 + mapPan.x;
            const cy = solarMapCanvas.height / 2 + mapPan.y;

            let clickedPlanet = null;
            let minDist = 24;

            Object.entries(planets).forEach(([pName, pObj]) => {
                const rx = pObj.position.x * 0.18 * mapZoom;
                const rz = pObj.position.z * 0.18 * mapZoom;
                const rotX = rx * Math.cos(mapRotationAngle) - rz * Math.sin(mapRotationAngle);
                const rotY = rx * Math.sin(mapRotationAngle) + rz * Math.cos(mapRotationAngle);
                const screenX = cx + rotX;
                const screenY = cy + rotY;

                const d = Math.hypot(clickX - screenX, clickY - screenY);
                if (d < minDist) {
                    minDist = d;
                    clickedPlanet = pName;
                }
            });

            if (clickedPlanet) {
                audio.playClick();
                setMissionTarget(clickedPlanet);
            }
        });

        // Update Map Sidebar telemetry
        function updateMapSidebar(pName) {
            const data = planetData[pName] || planetData["Moon"];
            document.getElementById('mapPreviewGlyph').textContent = data.glyph;
            document.getElementById('mapTargetTitle').textContent = data.name.toUpperCase();
            document.getElementById('mapTargetClass').textContent = data.class;

            const pObj = planets[pName];
            const liveDistKm = pObj ? Math.round(ship.position.distanceTo(pObj.position) * 100) : 384400;
            document.getElementById('mapSpecDist').textContent = `${liveDistKm.toLocaleString()} KM`;
            document.getElementById('mapSpecGrav').textContent = data.gravity;
            document.getElementById('mapSpecAtmo').textContent = data.atmo;
            document.getElementById('mapSpecTemp').textContent = data.temp;
            document.getElementById('mapTargetDesc').textContent = data.desc;
        }

        document.getElementById('mapSetDestBtn').onclick = () => {
            audio.playClick();
            toggleSolarMap();
            document.getElementById('message').textContent = `Destination locked: ${missionTarget}`;
        };

        document.getElementById('mapAutopilotBtn').onclick = () => {
            audio.playClick();
            if (!autopilotActive) toggleAutopilot();
            toggleSolarMap();
        };

        document.getElementById('mapQuickLandBtn').onclick = () => {
            audio.playClick();
            toggleSolarMap();
            triggerQuickLanding();
        };

        // Render the 2.5D Tactical Solar System Map on Canvas
        function drawSolarSystemMap() {
            if (!mapOpen) return;
            mapCtx.clearRect(0, 0, solarMapCanvas.width, solarMapCanvas.height);

            const cx = solarMapCanvas.width / 2 + mapPan.x;
            const cy = solarMapCanvas.height / 2 + mapPan.y;

            // Background tactical grid
            mapCtx.strokeStyle = 'rgba(0, 240, 255, 0.05)';
            mapCtx.lineWidth = 1;
            const gridSpacing = 40 * mapZoom;
            for (let x = (cx % gridSpacing); x < solarMapCanvas.width; x += gridSpacing) {
                mapCtx.beginPath(); mapCtx.moveTo(x, 0); mapCtx.lineTo(x, solarMapCanvas.height); mapCtx.stroke();
            }
            for (let y = (cy % gridSpacing); y < solarMapCanvas.height; y += gridSpacing) {
                mapCtx.beginPath(); mapCtx.moveTo(0, y); mapCtx.lineTo(solarMapCanvas.width, y); mapCtx.stroke();
            }

            // Draw concentric orbital rings
            const orbitalRadii = [60, 110, 160, 210, 270, 340, 420, 500, 580];
            mapCtx.strokeStyle = 'rgba(0, 240, 255, 0.12)';
            orbitalRadii.forEach(r => {
                mapCtx.beginPath();
                mapCtx.arc(cx, cy, r * mapZoom, 0, Math.PI * 2);
                mapCtx.stroke();
            });

            // Draw route line from spacecraft to target planet
            const targetObj = planets[missionTarget];
            if (targetObj) {
                const sX = cx + (ship.position.x * 0.18 * Math.cos(mapRotationAngle) - ship.position.z * 0.18 * Math.sin(mapRotationAngle)) * mapZoom;
                const sY = cy + (ship.position.x * 0.18 * Math.sin(mapRotationAngle) + ship.position.z * 0.18 * Math.cos(mapRotationAngle)) * mapZoom;

                const tX = cx + (targetObj.position.x * 0.18 * Math.cos(mapRotationAngle) - targetObj.position.z * 0.18 * Math.sin(mapRotationAngle)) * mapZoom;
                const tY = cy + (targetObj.position.x * 0.18 * Math.sin(mapRotationAngle) + targetObj.position.z * 0.18 * Math.cos(mapRotationAngle)) * mapZoom;

                mapCtx.strokeStyle = '#00f0ff';
                mapCtx.lineWidth = 2;
                mapCtx.setLineDash([8, 6]);
                mapCtx.beginPath();
                mapCtx.moveTo(sX, sY);
                mapCtx.lineTo(tX, tY);
                mapCtx.stroke();
                mapCtx.setLineDash([]);
            }

            // Draw each celestial body on the map
            Object.entries(planets).forEach(([pName, pObj]) => {
                const rx = pObj.position.x * 0.18 * mapZoom;
                const rz = pObj.position.z * 0.18 * mapZoom;
                const px = cx + (rx * Math.cos(mapRotationAngle) - rz * Math.sin(mapRotationAngle));
                const py = cy + (rx * Math.sin(mapRotationAngle) + rz * Math.cos(mapRotationAngle));

                const isTarget = (pName === missionTarget);
                const data = planetData[pName];
                const col = data ? data.color : '#00f0ff';

                // Glowing halo for selected planet
                if (isTarget) {
                    mapCtx.strokeStyle = '#00ffaa';
                    mapCtx.lineWidth = 2;
                    mapCtx.beginPath();
                    mapCtx.arc(px, py, 15 * mapZoom, 0, Math.PI * 2);
                    mapCtx.stroke();

                    mapCtx.strokeStyle = 'rgba(0, 255, 170, 0.3)';
                    mapCtx.lineWidth = 6;
                    mapCtx.beginPath();
                    mapCtx.arc(px, py, 18 * mapZoom, 0, Math.PI * 2);
                    mapCtx.stroke();
                }

                // Planet node circle
                mapCtx.fillStyle = col;
                mapCtx.beginPath();
                mapCtx.arc(px, py, Math.max(4, (pName === "Sun" ? 12 : 6) * mapZoom), 0, Math.PI * 2);
                mapCtx.fill();

                // Planet label
                mapCtx.fillStyle = isTarget ? '#00ffaa' : '#ffffff';
                mapCtx.font = `${Math.round(10 * THREE.MathUtils.clamp(mapZoom, 0.8, 1.3))}px monospace`;
                mapCtx.fillText(pName.toUpperCase(), px + 10, py + 4);
            });

            // Draw Orion Spacecraft Marker on Map
            const shipScreenX = cx + (ship.position.x * 0.18 * Math.cos(mapRotationAngle) - ship.position.z * 0.18 * Math.sin(mapRotationAngle)) * mapZoom;
            const shipScreenY = cy + (ship.position.x * 0.18 * Math.sin(mapRotationAngle) + ship.position.z * 0.18 * Math.cos(mapRotationAngle)) * mapZoom;

            mapCtx.fillStyle = '#00f0ff';
            mapCtx.beginPath();
            mapCtx.arc(shipScreenX, shipScreenY, 5, 0, Math.PI * 2);
            mapCtx.fill();

            mapCtx.strokeStyle = '#00f0ff';
            mapCtx.lineWidth = 1.5;
            mapCtx.beginPath();
            mapCtx.arc(shipScreenX, shipScreenY, 9, 0, Math.PI * 2);
            mapCtx.stroke();

            mapCtx.fillStyle = '#00f0ff';
            mapCtx.font = 'bold 9px monospace';
            mapCtx.fillText("▲ ORION SHIP", shipScreenX + 12, shipScreenY - 6);
        }

        /* -------------------------------------------------------------
           QUICK PLANET LANDING CINEMATIC SYSTEM (#landingCinematicOverlay)
           ------------------------------------------------------------- */
        const landingOverlay = document.getElementById('landingCinematicOverlay');
        const landingVFXCanvas = document.getElementById('landingVFXCanvas');
        const landingVFXCtx = landingVFXCanvas.getContext('2d');
        const landingPlanetTitle = document.getElementById('landingPlanetTitle');
        const landingPhaseTag = document.getElementById('landingPhaseTag');
        const landingAltNum = document.getElementById('landingAltNum');
        const landingVelNum = document.getElementById('landingVelNum');
        const landingPlasmaNum = document.getElementById('landingPlasmaNum');
        const landingRetroNum = document.getElementById('landingRetroNum');
        const landingProgressFill = document.getElementById('landingProgressFill');
        const abortLandingBtn = document.getElementById('abortLandingBtn');

        let isLandingCinematic = false;
        let landingStartTime = 0;
        let landingPlanetName = "Moon";
        const LANDING_DURATION = 3.6; // Seconds total for smooth fast cinematic

        function triggerQuickLanding() {
            audio.playClick();
            audio.playWarp();
            landingPlanetName = missionTarget;
            landingPlanetTitle.textContent = `APPROACHING ${landingPlanetName.toUpperCase()}`;
            landingOverlay.classList.add('active');
            isLandingCinematic = true;
            landingStartTime = performance.now();

            const rect = landingVFXCanvas.parentElement.getBoundingClientRect();
            landingVFXCanvas.width = rect.width;
            landingVFXCanvas.height = rect.height;

            active = false; // Freeze normal flight inputs during sequence
        }

        document.getElementById('topLandBtn').onclick = triggerQuickLanding;
        document.getElementById('hudQuickLandBtn').onclick = triggerQuickLanding;

        abortLandingBtn.onclick = () => {
            audio.playClick();
            isLandingCinematic = false;
            landingOverlay.classList.remove('active');
            active = true;
            document.getElementById('message').textContent = "Landing sequence aborted. Flight controls online.";
        };

        function updateLandingCinematic(now) {
            if (!isLandingCinematic) return;
            const elapsed = (now - landingStartTime) / 1000;
            const progress = THREE.MathUtils.clamp(elapsed / LANDING_DURATION, 0, 1);

            landingProgressFill.style.width = `${progress * 100}%`;

            // Canvas warp stars & re-entry plasma effect
            landingVFXCtx.fillStyle = 'rgba(1, 6, 18, 0.25)';
            landingVFXCtx.fillRect(0, 0, landingVFXCanvas.width, landingVFXCanvas.height);

            const vcx = landingVFXCanvas.width / 2;
            const vcy = landingVFXCanvas.height / 2;

            if (progress < 0.35) {
                // Phase 1: Warp Transit
                landingPhaseTag.textContent = "PHASE 1 // WARP TRANSIT & ORBITAL INSERTION";
                landingPhaseTag.style.color = "#00f0ff";
                landingAltNum.textContent = `${(150 - progress * 200).toFixed(1)} KM`;
                landingVelNum.textContent = "WARP BOOST >> 8.4 KM/S";
                landingPlasmaNum.textContent = "COMPRESSION 14%";
                landingRetroNum.textContent = "STANDBY";

                // Radial warp speed lines
                landingVFXCtx.strokeStyle = 'rgba(0, 240, 255, 0.7)';
                landingVFXCtx.lineWidth = 2;
                for (let i = 0; i < 40; i++) {
                    const ang = Math.random() * Math.PI * 2;
                    const r1 = 30 + Math.random() * 80;
                    const r2 = r1 + 80 + Math.random() * 200;
                    landingVFXCtx.beginPath();
                    landingVFXCtx.moveTo(vcx + Math.cos(ang) * r1, vcy + Math.sin(ang) * r1);
                    landingVFXCtx.lineTo(vcx + Math.cos(ang) * r2, vcy + Math.sin(ang) * r2);
                    landingVFXCtx.stroke();
                }

            } else if (progress < 0.75) {
                // Phase 2: Atmospheric Entry & Plasma Compression
                landingPhaseTag.textContent = "PHASE 2 // ATMOSPHERIC BRAKING & HEAT SHIELD BURN";
                landingPhaseTag.style.color = "#ffaa00";
                const alt = THREE.MathUtils.lerp(75, 8, (progress - 0.35) / 0.4);
                landingAltNum.textContent = `${alt.toFixed(1)} KM`;
                landingVelNum.textContent = `${(3.2 - progress * 2.5).toFixed(2)} KM/S`;
                landingPlasmaNum.textContent = "PLASMA 2,400°C";
                landingPlasmaNum.style.color = "#ff5544";
                landingRetroNum.textContent = "PRE-HEATING";

                // Fiery plasma particles
                for (let i = 0; i < 35; i++) {
                    landingVFXCtx.fillStyle = Math.random() > 0.4 ? 'rgba(255, 120, 20, 0.8)' : 'rgba(255, 230, 80, 0.9)';
                    const px = Math.random() * landingVFXCanvas.width;
                    const py = Math.random() * landingVFXCanvas.height;
                    const sz = 3 + Math.random() * 6;
                    landingVFXCtx.beginPath();
                    landingVFXCtx.arc(px, py, sz, 0, Math.PI * 2);
                    landingVFXCtx.fill();
                }

            } else {
                // Phase 3: Retro-thrusters & Touchdown
                landingPhaseTag.textContent = "PHASE 3 // TERMINAL DESCENT & TOUCHDOWN CONFIRMED";
                landingPhaseTag.style.color = "#00ffaa";
                const alt = THREE.MathUtils.lerp(8, 0, (progress - 0.75) / 0.25);
                landingAltNum.textContent = `${alt.toFixed(2)} KM`;
                landingVelNum.textContent = "-12 M/S (TOUCHDOWN)";
                landingPlasmaNum.textContent = "SUB-CRITICAL";
                landingRetroNum.textContent = "RETRO-BURN 100%";
                landingRetroNum.style.color = "#00ffaa";
            }

            // Sequence Complete -> Open Surface Exploration Mode!
            if (progress >= 1.0) {
                isLandingCinematic = false;
                landingOverlay.classList.remove('active');
                audio.playSuccess();
                openSurfaceExploration(landingPlanetName);
            }
        }

        /* -------------------------------------------------------------
           SURFACE EXPLORATION VIEW ENGINE (#surfaceExplorationView)
           ------------------------------------------------------------- */
        const surfaceView = document.getElementById('surfaceExplorationView');
        const surfaceCanvas = document.getElementById('surfaceCanvas');
        const surfaceCtx = surfaceCanvas.getContext('2d');
        const surfaceTitle = document.getElementById('surfaceTitle');
        const surfaceSub = document.getElementById('surfaceSub');
        const surfaceTasksContainer = document.getElementById('surfaceTasksContainer');
        const surfaceTasksCounter = document.getElementById('surfaceTasksCounter');
        const surfaceLiftoffBtn = document.getElementById('surfaceLiftoffBtn');
        const surfaceOpenMapBtn = document.getElementById('surfaceOpenMapBtn');

        let surfaceActive = false;
        let activeSurfacePlanet = "Moon";

        function openSurfaceExploration(planetName) {
            surfaceActive = true;
            activeSurfacePlanet = planetName;
            surfaceView.classList.add('active');

            const data = planetData[planetName] || planetData["Moon"];
            surfaceTitle.textContent = `${data.name.toUpperCase()} SURFACE EXPLORATION`;
            surfaceSub.textContent = `LANDING SITE // GRAVITY: ${data.gravity} // ATMOSPHERE: ${data.atmo}`;

            resizeSurfaceCanvas();
            renderSurfaceLandscape(planetName);
            populateSurfaceTasks(planetName);

            document.getElementById('missionStatus').textContent = "LANDED";
            document.getElementById('message').textContent = `Touchdown confirmed on ${data.name}. Ready for surface exploration.`;
        }

        function resizeSurfaceCanvas() {
            surfaceCanvas.width = window.innerWidth;
            surfaceCanvas.height = window.innerHeight;
        }

        function populateSurfaceTasks(planetName) {
            const data = planetData[planetName] || planetData["Moon"];
            surfaceTasksContainer.innerHTML = '';
            let completedCount = 0;

            data.tasks.forEach(task => {
                if (task.completed) completedCount++;

                const item = document.createElement('div');
                item.className = 'surface-task-item';

                item.innerHTML = `
                    <div class="surface-task-info">
                        <div class="surface-task-name">${task.title}</div>
                        <div class="surface-task-pts">★ REWARD: +${task.pts} PTS</div>
                    </div>
                    <button class="btn-surface-action ${task.completed ? 'completed' : ''}" data-task-id="${task.id}">
                        ${task.completed ? '✓ DONE' : 'EXECUTE'}
                    </button>
                `;

                const btn = item.querySelector('.btn-surface-action');
                if (!task.completed) {
                    btn.onclick = () => {
                        task.completed = true;
                        btn.classList.add('completed');
                        btn.textContent = '✓ DONE';
                        addScore(task.pts, `TASK COMPLETED: ${task.title}`);
                        populateSurfaceTasks(planetName);
                        updateDrawerTasks();
                    };
                }

                surfaceTasksContainer.appendChild(item);
            });

            surfaceTasksCounter.textContent = `${completedCount}/${data.tasks.length} COMPLETED`;
        }

        // Procedural Planet Surface Landscape Rendering on Canvas
        function renderSurfaceLandscape(planetName) {
            const w = surfaceCanvas.width;
            const h = surfaceCanvas.height;
            surfaceCtx.clearRect(0, 0, w, h);

            // Sky gradient tailored to planet
            const skyGrad = surfaceCtx.createLinearGradient(0, 0, 0, h * 0.75);
            if (planetName === "Mars") {
                skyGrad.addColorStop(0, '#100508');
                skyGrad.addColorStop(0.7, '#6e2b14');
                skyGrad.addColorStop(1, '#c55225');
            } else if (planetName === "Venus") {
                skyGrad.addColorStop(0, '#1a1405');
                skyGrad.addColorStop(0.6, '#9b7524');
                skyGrad.addColorStop(1, '#e5b850');
            } else if (planetName === "Earth") {
                skyGrad.addColorStop(0, '#041028');
                skyGrad.addColorStop(0.6, '#185098');
                skyGrad.addColorStop(1, '#5ca3e8');
            } else if (planetName === "Jupiter" || planetName === "Saturn") {
                skyGrad.addColorStop(0, '#080d18');
                skyGrad.addColorStop(0.6, '#3a2818');
                skyGrad.addColorStop(1, '#9e7545');
            } else if (planetName === "Uranus" || planetName === "Neptune") {
                skyGrad.addColorStop(0, '#040d18');
                skyGrad.addColorStop(0.6, '#143c58');
                skyGrad.addColorStop(1, '#3b86a8');
            } else {
                // Moon / Mercury / Deep space airless bodies
                skyGrad.addColorStop(0, '#010308');
                skyGrad.addColorStop(1, '#040a16');
            }
            surfaceCtx.fillStyle = skyGrad;
            surfaceCtx.fillRect(0, 0, w, h);

            // Stars in the sky (visible on Moon, Mars, airless worlds)
            surfaceCtx.fillStyle = '#ffffff';
            for (let i = 0; i < 180; i++) {
                surfaceCtx.fillRect(Math.random() * w, Math.random() * h * 0.65, 1.5, 1.5);
            }

            // Distant celestial body in the sky (e.g. Earth hanging in the lunar sky)
            if (planetName === "Moon") {
                surfaceCtx.save();
                const earthGrad = surfaceCtx.createRadialGradient(w * 0.25, h * 0.28, 10, w * 0.25, h * 0.28, 55);
                earthGrad.addColorStop(0, '#3aa8ff');
                earthGrad.addColorStop(0.7, '#144d8c');
                earthGrad.addColorStop(1, 'rgba(0,0,0,0)');
                surfaceCtx.fillStyle = earthGrad;
                surfaceCtx.beginPath();
                surfaceCtx.arc(w * 0.25, h * 0.28, 55, 0, Math.PI * 2);
                surfaceCtx.fill();
                surfaceCtx.restore();
            }

            // Distant mountain ridge
            surfaceCtx.fillStyle = (planetName === "Mars") ? '#481909' : ((planetName === "Venus") ? '#4a3810' : '#22252c');
            surfaceCtx.beginPath();
            surfaceCtx.moveTo(0, h * 0.65);
            for (let x = 0; x <= w; x += 40) {
                const y = h * 0.65 - Math.sin(x * 0.008) * 45 - Math.cos(x * 0.015) * 25;
                surfaceCtx.lineTo(x, y);
            }
            surfaceCtx.lineTo(w, h);
            surfaceCtx.lineTo(0, h);
            surfaceCtx.closePath();
            surfaceCtx.fill();

            // Foreground surface terrain
            const groundGrad = surfaceCtx.createLinearGradient(0, h * 0.68, 0, h);
            if (planetName === "Mars") {
                groundGrad.addColorStop(0, '#9e3d1c');
                groundGrad.addColorStop(1, '#521d0a');
            } else if (planetName === "Venus") {
                groundGrad.addColorStop(0, '#947025');
                groundGrad.addColorStop(1, '#3b2b0a');
            } else {
                groundGrad.addColorStop(0, '#4a4d56');
                groundGrad.addColorStop(1, '#1b1d22');
            }
            surfaceCtx.fillStyle = groundGrad;
            surfaceCtx.beginPath();
            surfaceCtx.moveTo(0, h * 0.72);
            for (let x = 0; x <= w; x += 30) {
                const y = h * 0.72 + Math.sin(x * 0.01) * 20;
                surfaceCtx.lineTo(x, y);
            }
            surfaceCtx.lineTo(w, h);
            surfaceCtx.lineTo(0, h);
            surfaceCtx.closePath();
            surfaceCtx.fill();

            // Rocks & Surface boulders
            surfaceCtx.fillStyle = 'rgba(10, 10, 15, 0.7)';
            for (let i = 0; i < 24; i++) {
                const rx = (i / 24) * w + (Math.random() - 0.5) * 60;
                const ry = h * 0.76 + Math.random() * (h * 0.2);
                const rw = 12 + Math.random() * 28;
                const rh = 6 + Math.random() * 16;
                surfaceCtx.beginPath();
                surfaceCtx.ellipse(rx, ry, rw, rh, 0, 0, Math.PI * 2);
                surfaceCtx.fill();
            }

            // Spacecraft Landing Module Silhouette
            const landerX = w * 0.5;
            const landerY = h * 0.76;
            surfaceCtx.fillStyle = '#b0c8d8';
            surfaceCtx.fillRect(landerX - 25, landerY - 45, 50, 45);
            surfaceCtx.fillStyle = '#112233';
            surfaceCtx.fillRect(landerX - 18, landerY - 35, 36, 18);
            // Landing legs
            surfaceCtx.strokeStyle = '#88a0b0';
            surfaceCtx.lineWidth = 3;
            surfaceCtx.beginPath();
            surfaceCtx.moveTo(landerX - 25, landerY); surfaceCtx.lineTo(landerX - 45, landerY + 22);
            surfaceCtx.moveTo(landerX + 25, landerY); surfaceCtx.lineTo(landerX + 45, landerY + 22);
            surfaceCtx.stroke();
        }

        // Return to Orbit action
        surfaceLiftoffBtn.onclick = () => {
            audio.playClick();
            audio.playWarp();
            surfaceActive = false;
            surfaceView.classList.remove('active');
            active = true;

            // Place ship safely in orbit around planet
            const pObj = planets[activeSurfacePlanet];
            if (pObj) {
                ship.position.copy(pObj.position).add(new THREE.Vector3(0, 40, 75));
                ship.lookAt(pObj.position);
            }
            speed = 1.8;
            document.getElementById('missionStatus').textContent = "IN ORBIT";
            document.getElementById('flightMode').textContent = "ACTIVE";
            document.getElementById('message').textContent = `Lift-off successful. Orbit established around ${activeSurfacePlanet}.`;
            showToast(`🚀 LIFT-OFF COMPLETE // ORBIT AROUND ${activeSurfacePlanet.toUpperCase()}`);
        };

        surfaceOpenMapBtn.onclick = () => {
            audio.playClick();
            toggleSolarMap();
        };

        /* -------------------------------------------------------------
           MOBILE ON-SCREEN TOUCH CONTROLLERS
           ------------------------------------------------------------- */
        function bindTouchBtn(elementId, keyName) {
            const el = document.getElementById(elementId);
            if (!el) return;
            el.addEventListener('touchstart', e => { e.preventDefault(); keys[keyName] = true; }, { passive: false });
            el.addEventListener('touchend', e => { e.preventDefault(); keys[keyName] = false; }, { passive: false });
            el.addEventListener('mousedown', () => { keys[keyName] = true; });
            el.addEventListener('mouseup', () => { keys[keyName] = false; });
        }

        bindTouchBtn('dpadUp', 'w');
        bindTouchBtn('dpadDown', 's');
        bindTouchBtn('dpadLeft', 'a');
        bindTouchBtn('dpadRight', 'd');
        bindTouchBtn('touchBoost', ' ');

        document.getElementById('touchLand')?.addEventListener('click', triggerQuickLanding);
        document.getElementById('touchMap')?.addEventListener('click', toggleSolarMap);
        document.getElementById('touchCam')?.addEventListener('click', cycleCameraMode);

        /* -------------------------------------------------------------
           NAVIGATION HUD PROJECTION (3D TARGET RETICLE & BEARING ARROW)
           ------------------------------------------------------------- */
        const navTargetMarker = document.getElementById('navTargetMarker');
        const markerTargetDist = document.getElementById('markerTargetDist');
        const navBearingArrow = document.getElementById('navBearingArrow');
        const bearingArrowIcon = document.getElementById('bearingArrowIcon');
        const bearingLabel = document.getElementById('bearingLabel');

        const tempVec = new THREE.Vector3();

        function updateNavigationIndicators(distKm) {
            const targetObj = planets[missionTarget];
            if (!targetObj || !active || mapOpen || surfaceActive || isLandingCinematic) {
                navTargetMarker.classList.remove('visible');
                navBearingArrow.classList.remove('visible');
                return;
            }

            tempVec.copy(targetObj.position);
            tempVec.project(camera);

            const isBehind = (tempVec.z > 1.0);
            const screenX = (tempVec.x * 0.5 + 0.5) * window.innerWidth;
            const screenY = (-tempVec.y * 0.5 + 0.5) * window.innerHeight;

            const margin = 50;
            const inScreenBounds = (
                !isBehind &&
                screenX >= margin && screenX <= window.innerWidth - margin &&
                screenY >= margin && screenY <= window.innerHeight - margin
            );

            if (inScreenBounds) {
                // In field of view: show floating 3D bracket
                navTargetMarker.style.left = `${screenX}px`;
                navTargetMarker.style.top = `${screenY}px`;
                markerTargetDist.textContent = `${Math.round(distKm)} KM`;
                navTargetMarker.classList.add('visible');
                navBearingArrow.classList.remove('visible');
            } else {
                // Out of field of view: show screen-edge directional arrow
                navTargetMarker.classList.remove('visible');

                let dx = screenX - window.innerWidth / 2;
                let dy = screenY - window.innerHeight / 2;
                if (isBehind) {
                    dx = -dx;
                    dy = -dy;
                }

                const angle = Math.atan2(dy, dx);
                const edgeX = THREE.MathUtils.clamp(
                    window.innerWidth / 2 + Math.cos(angle) * (window.innerWidth / 2 - 35),
                    35, window.innerWidth - 35
                );
                const edgeY = THREE.MathUtils.clamp(
                    window.innerHeight / 2 + Math.sin(angle) * (window.innerHeight / 2 - 35),
                    65, window.innerHeight - 55
                );

                navBearingArrow.style.left = `${edgeX}px`;
                navBearingArrow.style.top = `${edgeY}px`;
                bearingArrowIcon.style.transform = `rotate(${angle + Math.PI / 2}rad)`;

                const deg = Math.round(Math.abs(angle * 180 / Math.PI));
                bearingLabel.textContent = `${missionTarget.toUpperCase()} // ${deg}°`;
                navBearingArrow.classList.add('visible');
            }
        }

        /* -------------------------------------------------------------
           MISSION COMPLETE MODAL
           ------------------------------------------------------------- */
        const missionCompleteModal = document.getElementById('missionCompleteModal');
        const nextMissionBtn = document.getElementById('nextMissionBtn');
        const dismissModalBtn = document.getElementById('dismissModalBtn');

        const planetOrder = ["Moon", "Mars", "Jupiter", "Saturn", "Mercury", "Venus", "Uranus", "Neptune", "Earth"];
        nextMissionBtn.onclick = () => {
            audio.playClick();
            missionCompleteModal.classList.remove('active');
            const curIdx = planetOrder.indexOf(missionTarget);
            const nextTarget = planetOrder[(curIdx + 1) % planetOrder.length];
            setMissionTarget(nextTarget);
            resetFlight();
            launchGameMission();
        };

        dismissModalBtn.onclick = () => {
            audio.playClick();
            missionCompleteModal.classList.remove('active');
        };

        /* -------------------------------------------------------------
           HUD TELEMETRY UPDATE
           ------------------------------------------------------------- */
        const speedValEl = document.getElementById('speed');
        const speedBarEl = document.getElementById('speedBar');
        const altValEl = document.getElementById('altitude');
        const fuelValEl = document.getElementById('fuelText');
        const fuelBarEl = document.getElementById('fuelBar');
        const o2ValEl = document.getElementById('oxygenText');
        const o2BarEl = document.getElementById('oxygenBar');
        const hullValEl = document.getElementById('hullText');
        const hullBarEl = document.getElementById('hullBar');
        const gForceEl = document.getElementById('gForce');
        const thrustStatusEl = document.getElementById('thrustStatus');
        const targetDistEl = document.getElementById('targetDist');
        const targetEtaEl = document.getElementById('targetEta');
        const alertBanner = document.getElementById('alertBanner');

        function updateHUD(altKm, distTargetKm, accelerating) {
            speedValEl.textContent = Math.round(speed * 100);
            speedBarEl.style.width = Math.min(speed * 100, 100) + "%";

            altValEl.textContent = Math.round(altKm) + " km";

            fuelValEl.textContent = Math.round(fuel) + "%";
            fuelBarEl.style.width = fuel + "%";
            fuelBarEl.className = 'fill' + (fuel < 20 ? ' alert' : (fuel < 40 ? ' warn' : ''));

            o2ValEl.textContent = Math.round(oxygen) + "%";
            o2BarEl.style.width = oxygen + "%";
            o2BarEl.className = 'fill' + (oxygen < 20 ? ' alert' : (oxygen < 40 ? ' warn' : ''));

            hullValEl.textContent = Math.round(hullHealth) + "%";
            hullBarEl.style.width = hullHealth + "%";

            const gVal = 1.0 + (accelerating ? (boost ? 2.8 : 0.8) : 0);
            gForceEl.textContent = gVal.toFixed(1) + " G";

            thrustStatusEl.textContent = boost ? "WARP BOOST" : (accelerating ? "MAIN 100%" : (speed > 0.05 ? "CRUISE" : "IDLE"));
            thrustStatusEl.style.color = boost ? "#00f0ff" : (accelerating ? "#00ffaa" : "#b0d8eb");

            targetDistEl.textContent = Math.round(distTargetKm) + " km";
            if (speed > 0.1) {
                const sec = Math.round(distTargetKm / (speed * 10));
                targetEtaEl.textContent = sec > 60 ? `${Math.floor(sec / 60)}m ${sec % 60}s` : `${sec}s`;
            } else {
                targetEtaEl.textContent = "--";
            }

            if (oxygen < 20 || fuel < 15) {
                alertBanner.textContent = (oxygen < 20) ? "WARNING: LIFE SUPPORT OXYGEN CRITICAL" : "CAUTION: PROPELLANT LEVEL LOW";
                alertBanner.classList.add('show');
            } else {
                alertBanner.classList.remove('show');
            }
        }

        /* -------------------------------------------------------------
           MAIN ANIMATION & FLIGHT SIMULATOR LOOP
           ------------------------------------------------------------- */
        let frameCount = 0;

        function animate(now) {
            requestAnimationFrame(animate);

            const delta = Math.min(clock.getDelta(), 0.05);
            frameCount++;

            // Celestial rotations
            stars.rotation.y += 0.00001;
            Object.values(planets).forEach(p => {
                p.rotation.y += 0.0005;
            });
            if (earthCloudMesh) {
                earthCloudMesh.rotation.y += 0.0007;
            }

            // Cinematic & Map Loops
            if (isLandingCinematic) {
                updateLandingCinematic(now);
            }
            if (mapOpen && frameCount % 2 === 0) {
                drawSolarSystemMap();
            }

            // Space speed dust particles
            const dPos = dustGeo.attributes.position.array;
            for (let i = 2; i < dustCount * 3; i += 3) {
                dPos[i] += (4.0 + speed * 25.0) * delta;
                if (dPos[i] > 25) dPos[i] = -65;
            }
            dustGeo.attributes.position.needsUpdate = true;

            const targetObj = planets[missionTarget] || planets["Moon"];
            const distToTarget = ship.position.distanceTo(targetObj.position);
            const altKm = 100 + ship.position.length() * 0.1;

            // Update 3D Trajectory Route Line
            const tPosArr = trajectoryGeo.attributes.position.array;
            tPosArr[0] = ship.position.x; tPosArr[1] = ship.position.y; tPosArr[2] = ship.position.z;
            tPosArr[3] = targetObj.position.x; tPosArr[4] = targetObj.position.y; tPosArr[5] = targetObj.position.z;
            trajectoryGeo.attributes.position.needsUpdate = true;
            trajectoryLine.computeLineDistances();

            let accelerating = false;

            if (active && !paused && !isLandingCinematic && !surfaceActive) {
                accelerating = keys['w'] || keys['arrowup'];
                const braking = keys['s'] || keys['arrowdown'];
                const turningLeft = keys['a'] || keys['arrowleft'];
                const turningRight = keys['d'] || keys['arrowright'];
                const rollingLeft = keys['q'];
                const rollingRight = keys['e'];
                boost = keys[' '] && accelerating && fuel > 0;

                // AUTOPILOT GUIDANCE CONTROLLER
                if (autopilotActive) {
                    const toTarget = targetObj.position.clone().sub(ship.position).normalize();
                    const targetQuat = new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0, 0, -1), toTarget);
                    ship.quaternion.slerp(targetQuat, delta * 2.2);

                    // Regulate speed to optimal cruise
                    if (distToTarget > 120) {
                        if (speed < 4.5 && fuel > 0) {
                            speed += delta * 0.8;
                            accelerating = true;
                            fuel -= delta * 0.8;
                        }
                    } else if (distToTarget > 45) {
                        // Safe approach deceleration
                        if (speed > 1.2) {
                            speed -= delta * 1.2;
                        }
                    } else {
                        // Proximity reached!
                        speed = Math.max(0.4, speed - delta * 0.8);
                    }
                }

                // Mouse flight steering
                if (mouseSteerActive && !autopilotActive) {
                    const deadzone = 0.08;
                    const mx = Math.abs(mouseNorm.x) > deadzone ? (mouseNorm.x > 0 ? mouseNorm.x - deadzone : mouseNorm.x + deadzone) / (1 - deadzone) : 0;
                    const my = Math.abs(mouseNorm.y) > deadzone ? (mouseNorm.y > 0 ? mouseNorm.y - deadzone : mouseNorm.y + deadzone) / (1 - deadzone) : 0;

                    ship.rotateY(-mx * delta * 1.35);
                    ship.rotateX(-my * delta * 1.15);
                    ship.rotateZ(-mx * delta * 0.55);
                }

                // Keyboard manual steering
                if (!autopilotActive) {
                    if (turningLeft) ship.rotateY(delta * 1.25);
                    if (turningRight) ship.rotateY(-delta * 1.25);

                    if (rollingLeft) ship.rotateZ(delta * 1.4);
                    if (rollingRight) ship.rotateZ(-delta * 1.4);

                    if (keys['arrowup'] && !mouseSteerActive) ship.rotateX(-delta * 0.9);
                    if (keys['arrowdown'] && !mouseSteerActive) ship.rotateX(delta * 0.9);

                    // Manual thrust & braking
                    if (accelerating && fuel > 0) {
                        const thrustPower = boost ? 1.5 : 0.55;
                        speed += delta * thrustPower;
                        fuel -= delta * (boost ? 4.0 : 1.0);
                    }

                    if (braking) {
                        speed -= delta * 0.8;
                    }
                }

                oxygen -= delta * 0.08;

                speed = THREE.MathUtils.clamp(speed, 0, 8.0);
                fuel = Math.max(0, fuel);
                oxygen = Math.max(0, oxygen);

                // Spacecraft momentum & inertia
                direction.set(0, 0, -1).applyQuaternion(ship.quaternion);
                const targetVelocity = direction.clone().multiplyScalar(speed * 12.0);
                velocity.lerp(targetVelocity, delta * 2.2);
                ship.position.addScaledVector(velocity, delta);

                // Animated Engine Thrust Flames & Shocks
                const flameScale = boost ? 2.4 : (accelerating ? 1.3 : 0.35);
                flameMeshL.scale.set(flameScale, flameScale * 1.4, flameScale);
                flameMeshR.scale.set(flameScale, flameScale * 1.4, flameScale);

                shock1.visible = (accelerating && fuel > 0);
                shock2.visible = (accelerating && fuel > 0);
                shock1.scale.setScalar(boost ? 1.5 : 1.0);
                shock2.scale.setScalar(boost ? 1.5 : 1.0);

                engineLight.intensity = boost ? 10 : (accelerating ? 5.0 : 1.5);
                engineLight.color.setHex(boost ? 0xaae8ff : 0x00dfff);

                flightStick.rotation.x = (accelerating ? -0.22 : (braking ? 0.22 : 0));
                flightStick.rotation.z = (turningLeft ? 0.25 : (turningRight ? -0.25 : 0));
                throttleLever.position.z = -0.55 - (speed / 8.0) * 0.14;

                // Mission complete proximity check
                if (distToTarget < 55) {
                    document.getElementById('missionStatus').textContent = "COMPLETED";
                    document.getElementById('message').textContent = missionTarget + " reached! Orbital insertion achieved.";
                    document.getElementById('modalMessage').textContent = "Orbital insertion around " + missionTarget + " achieved successfully.";
                    missionCompleteModal.classList.add('active');
                    active = false;
                    speed = 0;
                    audio.playSuccess();
                }

                // Exhaust particles
                const ePos = exhaustGeo.attributes.position.array;
                for (let i = 0; i < exhaustCount; i++) {
                    const idx = i * 3;
                    ePos[idx + 2] += (accelerating ? (boost ? 40 : 22) : 10) * delta;
                    if (ePos[idx + 2] > 18) {
                        ePos[idx] = (Math.random() - 0.5) * (boost ? 0.8 : 0.45);
                        ePos[idx + 1] = (Math.random() - 0.5) * 0.35;
                        ePos[idx + 2] = 2.9;
                    }
                }
                exhaustGeo.attributes.position.needsUpdate = true;

                audio.update(accelerating && fuel > 0, boost, speed / 8.0);

            } else {
                flameMeshL.scale.set(0.3, 0.4, 0.3);
                flameMeshR.scale.set(0.3, 0.4, 0.3);
                shock1.visible = false;
                shock2.visible = false;
                engineLight.intensity = 1.0;
                audio.update(false, false, 0);
            }

            if (frameCount % 2 === 0) {
                updateMFDs(speed, altKm, fuel, oxygen, missionTarget);
                drawHoloHUD();
                updateNavigationIndicators(distToTarget);
            }

            /* -------------------------------------------------------------
               STABLE UNIFIED CAMERA CONTROLLER (3 MODES - ZERO UNCONTROLLED SPIN)
               ------------------------------------------------------------- */
            if (cameraMode === 'cockpit') {
                // A. COCKPIT FIRST-PERSON VIEW
                const localEye = cockpitEyeOffset.clone();
                if (pilotHeadPan.x !== 0 || pilotHeadPan.y !== 0) {
                    localEye.x += pilotHeadPan.x * 0.15;
                    localEye.y += pilotHeadPan.y * 0.12;
                }

                // Eye position follows ship exactly
                const worldEye = localEye.applyQuaternion(ship.quaternion).add(ship.position);
                camera.position.copy(worldEye);

                // Stable quaternion orientation (directly derived from ship, no lookAt gimbal lock)
                camera.quaternion.copy(ship.quaternion);

                // Subtle pilot head turn offset
                if (pilotHeadPan.x !== 0 || pilotHeadPan.y !== 0) {
                    const headEuler = new THREE.Euler(pilotHeadPan.y, pilotHeadPan.x, 0, 'YXZ');
                    const headQuat = new THREE.Quaternion().setFromEuler(headEuler);
                    camera.quaternion.multiply(headQuat);
                }

                if (boost) {
                    camera.position.x += (Math.random() - 0.5) * 0.015;
                    camera.position.y += (Math.random() - 0.5) * 0.015;
                }

            } else if (cameraMode === 'chase') {
                // B. THIRD-PERSON CHASE VIEW (Smooth Damped Tracking)
                const targetPos = chaseCamPos.clone().applyQuaternion(ship.quaternion).add(ship.position);
                camera.position.lerp(targetPos, 0.14);

                const targetQuat = ship.quaternion.clone();
                const downPitch = new THREE.Quaternion().setFromAxisAngle(new THREE.Vector3(1, 0, 0), -0.13);
                targetQuat.multiply(downPitch);
                camera.quaternion.slerp(targetQuat, 0.14);

            } else if (cameraMode === 'external') {
                // C. WIDE EXTERNAL SPACE VIEW (Interactive Orbit & Zoom, Zero Auto-Spin)
                const ox = orbitDistance * Math.sin(orbitPhi) * Math.sin(orbitTheta);
                const oy = orbitDistance * Math.cos(orbitPhi);
                const oz = orbitDistance * Math.sin(orbitPhi) * Math.cos(orbitTheta);

                const targetOrbitPos = ship.position.clone().add(new THREE.Vector3(ox, oy, oz));
                camera.position.lerp(targetOrbitPos, 0.16);

                camera.up.set(0, 1, 0);
                camera.lookAt(ship.position);
            }

            updateHUD(altKm, distToTarget, accelerating);

            renderer.render(scene, camera);
        }

        animate(performance.now());

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

    </script>
</body>

</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated index.html ({len(html_content)} bytes)")
