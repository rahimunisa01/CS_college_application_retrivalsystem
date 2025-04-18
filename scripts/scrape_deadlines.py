from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import os

# Load university URLs
with open("data/university_urls.json") as f:
    universities = json.load(f)

# Setup headless Chrome with a user-agent
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=options)

scraped_docs = []
os.makedirs("screenshots", exist_ok=True)

for univ in universities:
    for attempt in range(2):  # Retry up to 2 times
        try:
            print(f"Scraping {univ['name']} (Attempt {attempt + 1})...")
            driver.get(univ['url'])

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            time.sleep(2)  # Allow full JS load
            text = driver.find_element(By.TAG_NAME, "body").text

            if len(text.strip()) < 100:
                raise ValueError("Too little content, likely blocked or empty")

            # Take screenshot for debugging
            screenshot_path = f"screenshots/{univ['id'] if 'id' in univ else univ['name'].lower().replace(' ', '_')}.png"
            driver.save_screenshot(screenshot_path)

            scraped_docs.append({
                "id": univ["name"].lower().replace(" ", "_"),
                "title": f"{univ['name']} - MSCS Deadlines",
                "text": text[:15000],  # Limit size
                "tags": ["cs", "2025", "ms", univ["name"].lower().replace(" ", "_")]
            })
            break  # Success, break retry loop

        except Exception as e:
            print(f"⚠️ Failed on {univ['name']} (Attempt {attempt + 1}): {e}")
            time.sleep(3)

# Save final scraped documents
os.makedirs("data/documents", exist_ok=True)
with open("data/documents/docs.json", "w") as f:
    json.dump(scraped_docs, f, indent=4)

print(f"✅ Scraped {len(scraped_docs)} universities.")
driver.quit()