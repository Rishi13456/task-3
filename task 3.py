import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h3")

    extracted_headlines = []

    for h in headlines:
        text = h.get_text(strip=True)
        if text and text not in extracted_headlines:
            extracted_headlines.append(text)

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(extracted_headlines, 1):
            file.write(f"{i}. {headline}\n")

    print(f"{len(extracted_headlines)} headlines saved to 'headlines.txt'")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
