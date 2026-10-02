import sys
import os
import time
from playwright.sync_api import sync_playwright

def explore():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        print("Navigating to https://staging.lumos.education/simulations ...")
        page.goto("https://staging.lumos.education/simulations", wait_until="networkidle", timeout=60000)
        print("Current URL:", page.url)
        print("Page Title:", page.title())

        page.screenshot(path="D:/HDSD Lab029/screenshots/00_initial.png")
        
        # Check DOM elements
        inputs = page.query_selector_all("input")
        print(f"Found {len(inputs)} inputs")
        for i, inp in enumerate(inputs):
            print(f"Input {i}: type={inp.get_attribute('type')}, name={inp.get_attribute('name')}, id={inp.get_attribute('id')}, placeholder={inp.get_attribute('placeholder')}")
            
        buttons = page.query_selector_all("button")
        print(f"Found {len(buttons)} buttons")
        for i, btn in enumerate(buttons[:10]):
            print(f"Button {i}: text={btn.inner_text().strip()[:50]}")

        browser.close()

if __name__ == "__main__":
    explore()
