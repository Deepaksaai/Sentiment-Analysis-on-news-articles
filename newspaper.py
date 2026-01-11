import requests
#fetch top headlines from the US
url = "https://newsapi.org/v2/top-headlines"
params = {
    'country': 'us',
    'apiKey': '24eb538ed65d4fe29a81ec519e82fb1c' 
}
response = requests.get(url, params=params)
data = response.json()
articles = data.get('articles', [])
for article in articles:
    print(f"Title(usa): {article['title']}")
    print(f"Description: {article['description']}\n")

#convert it to a csv file
import csv
with open('us_headlines.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Description', 'URL'])
    for article in articles:
        writer.writerow([article['title'], article['description'], article['url']])

