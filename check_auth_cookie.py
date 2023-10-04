import requests
payload = {"login":"secret_login", "password":"secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
value_cookie = response1.cookies.get("auth_cookie")
cookies = {}
if value_cookie is not None:
    cookies.update({"auth_cookie":value_cookie})
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response2.text)