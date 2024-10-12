import requests
from bs4 import BeautifulSoup
import pandas as pd
# Function to scrape data from a website (e.g., news headlines)
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h2')  # Adjust according to website's structure
    data = [headline.get_text() for headline in headlines]
    return pd.DataFrame(data, columns=['Headline'])
url = 'https://timesofindia.indiatimes.com/news'  # Replace with the actual URL
df = scrape_data(url)
print(df.head())
import matplotlib.pyplot as plt
def visualize_data(df):
    plt.figure(figsize=(5, 6))
    df['Headline'].value_counts(5).head(10).plot(kind='barh')
    plt.xlabel('Frequency')
    plt.title('Top 10 News Headlines')
    plt.show()
visualize_data(df)
