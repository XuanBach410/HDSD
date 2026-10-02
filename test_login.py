import time
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        print("Navigating to https://staging.lumos.education/simulations ...")
        page.goto("https://staging.lumos.education/simulations", wait_until="networkidle", timeout=60000)

        # Click Đăng nhập
        print("Clicking Đăng nhập...")
        login_btn = page.locator("button:has-text('Đăng nhập'), a:has-text('Đăng nhập')").first
        login_btn.click()
        time.sleep(2)
        
        print("URL after clicking Đăng nhập:", page.url)
        page.screenshot(path="D:/HDSD Lab029/screenshots/01_login_dialog.png")
        
        # Check modal or form
        inputs = page.query_selector_all("input")
        print(f"Inputs found: {len(inputs)}")
        for i, inp in enumerate(inputs):
            print(f"  Input {i}: type={inp.get_attribute('type')}, placeholder={inp.get_attribute('placeholder')}, name={inp.get_attribute('name')}")
            
        buttons = page.query_selector_all("button")
        print(f"Buttons found: {len(buttons)}")
        for i, b in enumerate(buttons):
            t = b.inner_text().strip()
            if t:
                print(f"  Button {i}: {t}")

        browser.close()

if __name__ == "__main__":
    test_login()
