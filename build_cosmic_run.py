#!/usr/bin/env python3
"""
Build script for COSMIC RUN – BEYOND THE UNIVERSE
Hackathon Edition: Premium 3D Space Runner & Planetary Exploration Game.
Generates an AAA-grade, self-contained, highly optimized index.html.
"""

from generate_premium_game import build_index_html

def generate_cosmic_run_html():
    return build_index_html()

if __name__ == '__main__':
    html_content = generate_cosmic_run_html()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Successfully generated COSMIC RUN – BEYOND THE UNIVERSE ({len(html_content)} bytes)")
