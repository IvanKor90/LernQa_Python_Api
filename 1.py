import requests
payload = {"name":"p0wEr"}
response = requests.get("https://playground.learnqa.ru/api/hello",params=payload)
print(response.text)