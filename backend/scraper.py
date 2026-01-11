import requests
from bs4 import BeautifulSoup

# GitHub Jobs API is no longer available, so we focus on other sources.

def scrape_internshala(keyword):
    url = f"https://internshala.com/internships/keywords-{keyword}"
    jobs = []

    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    cards = soup.select(".individual_internship")

    for card in cards:
        title = card.select_one(".job-internship-name")
        company = card.select_one(".company-name")
        location = card.select_one(".locations")
        link = card.select_one("a")
        
        posted = card.find(string=lambda text: text and "ago" in text)

        jobs.append({
            "title": title.text.strip() if title else keyword,
            "company": company.text.strip() if company else "Unknown",
            "location": location.text.strip() if location else "India",
            "description": card.text.strip(),
            "source": "Internshala",
            "url": "https://internshala.com" + link["href"] if link else "",
            "posted": posted.strip() if posted else "recently"
        })

    return jobs
