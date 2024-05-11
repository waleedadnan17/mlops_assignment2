import json

def clean_text(text):
    """Clean text by removing unwanted characters and altering the format of strings."""
    text = text.replace('\n', ' ').replace('\r', '').strip()
    # Additional cleaning logic can be added here
    return text

def transform_data(articles):
    """Transform list of article dictionaries into cleaned JSON format."""
    transformed_data = []
    for article in articles:
        cleaned_article = {
            'title': clean_text(article['title']),
            'description': clean_text(article['description']),
            'link': article['link']
        }
        transformed_data.append(cleaned_article)
    return json.dumps(transformed_data, indent=2)

if __name__ == '__main__':
    # Example usage
    example_articles = [
        {'title': '  Example \nTitle  ', 'description': 'Here is a description.\n', 'link': 'http://example.com'}
    ]
    transformed = transform_data(example_articles)
    print(transformed)
