from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()   # otevřeme prohlížeč
    page = browser.new_page()      # otevřeme novou záložku
    page.goto("https://youtube.com/")  # načteme webovou stránku
    page.screenshot(path="example.png")     #
    browser.close()   # zavřeme prohlížeč
