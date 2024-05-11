import requests
from bs4 import BeautifulSoup

def extract_from_dawn():
    url = 'https://www.dawn.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    for item in soup.find_all('article'):
        title = item.find('h2')
        if title:
            title = title.text.strip()
        description = item.find('p')
        if description:
            description = description.text.strip()
        link = item.find('a', href=True)
        if link:
            link = link['href']

        if title and description and link:
            articles.append({'title': title, 'description': description, 'link': link})

    return articles

if __name__ == '__main__':
    data = extract_from_dawn()
    for article in data:
        print(article)
