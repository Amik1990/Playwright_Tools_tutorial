import asyncio
import playwright
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

#with sync_playwright() as p:
 #   browser = p.firefox.launch(headless=False, slow_mo=500)   # otevřeme prohlížeč
  #  page = browser.new_page()      # otevřeme novou záložku
  #  page.goto("https://playwright.dev/")  # načteme webovou stránku
  #  print(page.title())     # vypíšeme titulek stránky
 #   browser.close()   # zavřeme prohlížeč

async def main():         # druhá možnost
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=2000)   # otevřeme prohlížeč
        page = await browser.new_page()     # otevřeme novou záložku
        await page.goto("https://playwright.dev/")   # načteme webovou stránku
        print(page.title())    # vypíšeme titulek stránky
        await browser.close()   # zavřeme prohlížeč

asyncio.run(main())

# Když chci spustit generátor kódu pro wikipedia.org tak napíšu do terminálu:
#  playwright codegen wikipedia.org


