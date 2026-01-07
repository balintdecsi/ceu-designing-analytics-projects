#!/usr/bin/env python3
"""
Check Marp slides for text overflow.

Loads each HTML slide file in a headless browser and checks if any slide's
content height exceeds the 720px container height.
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright


async def check_slides_for_overflow(html_path: Path):
    """Check all slides in a Marp HTML file for text overflow."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'file://{html_path.absolute()}')

        # Check each slide section for overflow
        overflows = await page.evaluate('''
            () => {
                const results = [];
                const sections = document.querySelectorAll('section[data-marpit-pagination]');
                sections.forEach(section => {
                    const slideNum = section.getAttribute('data-marpit-pagination');
                    const contentHeight = section.scrollHeight;
                    const containerHeight = 720; // Marp default

                    if (contentHeight > containerHeight) {
                        results.push({
                            slide: parseInt(slideNum),
                            contentHeight: contentHeight,
                            overflow: contentHeight - containerHeight
                        });
                    }
                });
                return results;
            }
        ''')

        await browser.close()
        return overflows


async def main():
    slides_dir = Path('/Users/earino/CEU/ECBS5228/slides')
    html_files = sorted(slides_dir.glob('*.html'))

    total_overflows = 0

    for html_file in html_files:
        print(f"\n{html_file.name}:")
        overflows = await check_slides_for_overflow(html_file)

        if not overflows:
            print("  All slides OK")
        else:
            for o in overflows:
                print(f"  Slide {o['slide']}: OVERFLOW ({o['contentHeight']}px, +{o['overflow']}px)")
                total_overflows += 1

    print(f"\n{'='*50}")
    print(f"Total slides with overflow: {total_overflows}")


if __name__ == '__main__':
    asyncio.run(main())
