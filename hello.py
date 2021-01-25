import requests

payload = {'term': 'honeydew'}

res = requests.get('https://itunes.apple.com/search',
                   params=payload)

melon_songs = res.json()

num_results = melon_songs['resultCount']

for i in range(num_results):
    trackName = melon_songs['results'][i].get('trackName')
    artistName = melon_songs['results'][i].get('artistName')
    print({trackName})