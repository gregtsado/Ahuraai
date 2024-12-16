
import tweepy
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv(override=True)

url = 'https://www.techinafrica.com/'  

# Define headers to mimic a browser request
r = requests.get(url)



#web scrapping
soup = BeautifulSoup(r.text, 'html.parser')

# Find the 'h3' tag with the specified class
h3_tag = soup.find('h3', class_='g1-gamma g1-gamma-1st entry-title')

# Find the 'a' tag within the 'h3' tag
a_tag = h3_tag.find('a', href=True) if h3_tag else None

# Extract the link (href attribute) and the title (text content of the 'a' tag)
link = a_tag['href'] if a_tag else None
title = a_tag.get_text(strip=True) if a_tag else None

print("Extracted Link:", link)
print("Extracted Title:", title)

api_key =  os.getenv('llm_api_key')

client = OpenAI(
    api_key =  api_key
)

completion = client.completions.create(
  model = "gpt-3.5-turbo-instruct",
  prompt = f"""
    Write a short tweet about "{title}" and include the link: {link}. 
    """,
  max_tokens = 700,
  temperature = 0
)

tweet = completion.choices[0].text.strip()



BEARER_TOKEN = os.getenv('bearer_token'),
API_KEY = os.getenv('API_KEY'),
API_SECRET_KEY = os.getenv('API_SECRET_KEY'),
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN'),
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')  # Required for v2

# Authenticate to the Twitter API
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET_KEY,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)


# Post the tweet
response = client.create_tweet(text=tweet)
# api.update_status(title)
print("Tweet posted successfully!")