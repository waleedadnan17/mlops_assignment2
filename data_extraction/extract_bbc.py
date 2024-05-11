import requests
from bs4 import BeautifulSoup

def extract_from_bbc():
    url = 'https://www.bbc.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    for item in soup.select('div.media__content'):
        title = item.find('h3')
        if title:
            title = title.text.strip()
        description = item.find('p')
        if description:
            description = description.text.strip()
        link = item.find('a', href=True)
        if link:
            link = 'https://www.bbc.com' + link['href']

        if title and description and link:
            articles.append({'title': title, 'description': description, 'link': link})

    return articles

if __name__ == '__main__':
    data = extract_from_bbc()
    for article in data:
        print(article)
