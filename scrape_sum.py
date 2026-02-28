from playwright.sync_api import sync_playwright

BASE_URL = "https://sanand0.github.io/tdsdata/js_table/?seed="

seeds = range(74, 84)  # seeds 74 to 83
grand_total = 0

def extract_numbers(page):
    total = 0
    cells = page.query_selector_all("table td")
    for cell in cells:
        text = cell.inner_text().strip()
        try:
            total += float(text.replace(",", ""))
        except:
            pass
    return total

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    for seed in seeds:
        url = BASE_URL + str(seed)
        print(f"Opening {url}")
        page.goto(url)
        page.wait_for_selector("table", timeout=60000)
        seed_total = extract_numbers(page)
        print(f"Seed {seed} total = {seed_total}")
        grand_total += seed_total
    browser.close()

print("\nFINAL TOTAL =", grand_total)