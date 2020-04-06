from urllib.request import urlopen
import requests


# send request to get complete data from poe (all stash tabs from all players)
r = requests.get("http://api.pathofexile.com/public-stash-tabs")

#check server is responding and sending Response 200
print("Response from POE server: ", r)

print(r)