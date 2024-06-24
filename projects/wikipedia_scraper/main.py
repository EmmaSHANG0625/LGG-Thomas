import requests
from bs4 import BeautifulSoup
import re

def get_leaders():
    root_url = "https://country-leaders.onrender.com"
    countries_url = f"{root_url}/countries"
    leaders_url = f"{root_url}/leaders"
    cookie_url = f'{root_url}/cookie'
    req_cookie = requests.api.get(cookie_url)
    cookies = req_cookie.cookies
    response_countries = requests.get(countries_url, cookies=cookies)
    countries = response_countries.json()
    leaders_per_country = {}
    for country_code in countries:
        params = {"country": country_code}
        response_leaders = requests.get(leaders_url, params=params, cookies=cookies)
        leaders_per_country[country_code] = response_leaders.json()
    return leaders_per_country

leaders_data = get_leaders() 
print(leaders_data)

def get_first_paragraph(wikipedia_url, session): 
    response_wiki = session.get(wikipedia_url)
    soup = BeautifulSoup(response_wiki.content, 'html.parser')
    paragraphs = soup.find_all('p')
    
    for para in paragraphs:
        text = para.get_text().strip()
        if para.find('b') or para.find('strong'):
            return re.sub(r'\[.*?\]|<.*?>|/.*?/', '', text).strip()

# Fetch leaders data
leaders_data = get_leaders()

# Create a session
with requests.Session() as session:
    
    for country_code, leaders_info in leaders_data.items():
        print(f"Country Code: {country_code}")
        
        for leader_info in leaders_info:
            wikipedia_url = leader_info["wikipedia_url"]
            print(f"Wikipedia URL: {wikipedia_url}")
            
            first_paragraph = get_first_paragraph(wikipedia_url, session)
            print(first_paragraph)
            print()