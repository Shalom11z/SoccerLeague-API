import http.client
import requests
import json

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "77e94ba8eb0526542adbbea14d9ad6cc"
    }

conn.request("GET", "/leagues", headers=headers)

res = conn.getresponse()
data = res.read()
jsonData = json.loads(data)
responses = jsonData['response']
for response in responses:
  leagueName = response['league'] ['name']
  countryName = response['country'] ['name']
  seasons = year['start']['end']
 
  
print(f"League name is {leagueName}")
print(f"The country that the Champions league take place is{countryName}")
print(f"The season begins on the{startdate}")
print(f"and the season ends on {endDate}")
