import time
from playwright.sync_api import sync_playwright

def test_student_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        print("Navigating to https://staging.lumos.education/login ...")
        page.goto("https://staging.lumos.education/login", wait_until="networkidle", timeout=60000)

        # Fill credentials
        page.fill("input[type='email']", "demo@lab029s.app")
        page.fill("input[type='password']", "Lab029sDemo!2026")
        
        # Take screenshot of filled login
        page.screenshot(path="D:/HDSD Lab029/screenshots/02_login_filled.png")
        
        # Click login
        page.click("button:has-text('Đăng nhập')")
        
        # Wait for navigation / response
        time.sleep(5)
        print("URL after login:", page.url)
        page.screenshot(path="D:/HDSD Lab029/screenshots/03_student_after_login.png")

        # Let's inspect nav links, buttons, headers
        links = page.query_selector_all("a")
        print(f"Total links: {len(links)}")
        for l in links:
            txt = l.inner_text().strip()
            href = l.get_attribute("href")
            if txt or href:
                print(f"  Link: '{txt}' -> {href}")

        buttons = page.query_selector_all("button")
        print(f"Total buttons: {len(buttons)}")
        for b in buttons:
            txt = b.inner_text().strip()
            if txt:
                print(f"  Button: '{txt}'")

        browser.close()

if __name__ == "__main__":
    test_student_login()
