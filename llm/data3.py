import requests
url = "https://developers.coinmarketcal.com/v1/coins"
querystring = {"max":"10","coins":"bitcoin"}
payload = ""
headers = {
    'x-api-key': "EitKASIIRR1GicBFvhR5eaRNFLxZLzUl40oVgI4s",
    'Accept-Encoding': "deflate, gzip",
    'Accept': "application/json"
}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
print(response.text) 