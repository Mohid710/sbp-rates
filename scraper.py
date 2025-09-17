import requests
from bs4 import BeautifulSoup
import json
from datetime import date

# 1. Get the SBP KIBOR webpage
url = "https://www.sbp.org.pk/ecodata/kibor_index.asp"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

# 2. Find the table rows
rows = soup.select("table tr")[1:]  # skip header
rates = {}

for row in rows:
    cols = [c.text.strip() for c in row.select("td")]
    if cols and len(cols) >= 3:
        tenor = cols[0].replace(" ", "")
        offer = cols[2]
        try:
            rates[tenor] = float(offer)
        except:
            continue

# 3. Build JSON
data = {
    "baseRate": 22.00,  # update manually if needed
    "kibor1M": rates.get("1Month"),
    "kibor3M": rates.get("3Month"),
    "kibor6M": rates.get("6Month"),
    "kibor12M": rates.get("12Month"),
    "lastUpdated": str(date.today())
}

# 4. Save to rates.json
with open("rates.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ SBP KIBOR rates updated")
