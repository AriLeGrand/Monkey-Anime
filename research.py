import requests

url = "https://anime-sama.fr/template-php/defaut/fetch.php"
headers = {
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-requested-with": "XMLHttpRequest"
}
data = {
    "query": str(input("Recherche: "))
}

response = requests.post(url, headers=headers, data=data)

print(response.text)
with open("output.html", "w") as f:
    f.write(response.text)