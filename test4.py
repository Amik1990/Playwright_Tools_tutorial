import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)   # otevřeme prohlížeč
    context = browser.new_context()
    page = context.new_page()   # otevřeme novou záložku
    page.goto("https://www.wikipedia.org/")  #  načteme webovou stránku
    context.tracing.start(screenshots=True, snapshots=True, sources=True)   # umožní zaznamenat další kroky
    page.get_by_label("Top languages").click()   #  kliknu na top languages
    page.get_by_role("link", name="English 6,792,000+ articles").click()   #  kliknu na english
    page.get_by_placeholder("Search Wikipedia").click()    #  kliknu do vyhledávače
    page.get_by_placeholder("Search Wikipedia").fill("akita inu")   #  napíšu aktita inu
    page.get_by_role("link", name="Akita (dog breed) Dog breed").click()  #  ze seznamu vyberu dog breed
    page.get_by_role("link", name="Hachikō").nth(1).click()      # kliknu na Hachiko
    page.get_by_role("figure", name="Shibuya Station as it was in").get_by_role("link").first.click()  #kliknu na obrázek
    # ---------------------
    context.tracing.stop(path="trace.zip")   # zde se ukončí záznam a uloží se do trace.zip
    context.close()    # zavřeme kontext
    browser.close()    # zavřeme prohlížeč


with sync_playwright() as playwright:
    run(playwright)

# abychom to spustili promítání, tak musíme do terminálu napsat:
# python test4.py

# když budeme chtít otevřít playright trace viewer, tak do terminálu napíšu:
# playwright show-trace trace.zip
