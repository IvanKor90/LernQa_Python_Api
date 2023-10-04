import json
json_format = '{"name":"Ivan"}'
obj = json.loads(json_format)
key = "name2"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} нету в json")