import requests
url = str(input("URL : "))
responce = requests.get(url)
episodes_url = url + "episodes.js?" + str(responce.text).split("src='episodes.js?")[1].split("'defer></script>")[0]

print(episodes_url)
episodes = requests.get(episodes_url)
episodes = str(episodes.content).replace("\\r\\n", "").split("eps1 = [")[1].split(",];")[0].replace("'", "").split(",")
for episode in episodes:
    if "http" in episode:
        print(episode.replace("\\n\\t\\t", ""))