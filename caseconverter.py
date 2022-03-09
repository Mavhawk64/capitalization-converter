import requests
from dotenv import dotenv_values

# .env like API_KEY=abcd1234
# get api key from https://rapidapi.com/Matt11/api/title-case-converter/

config = dotenv_values(".env")

url = "https://title-case-converter.p.rapidapi.com/v1/TitleCase"
api_key = config["API_KEY"]

the_title = "the quick brown fox jumps over a lazy dog"

querystring = {"title":the_title,"style":"AP"}

headers = {
    'x-rapidapi-host': "title-case-converter.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)