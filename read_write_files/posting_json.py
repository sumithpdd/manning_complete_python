import requests
import simplejson as json

url = "https://shortener.google.com/url"
payload = {"longUrl": "http://example.com"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r.status_code)
print(r.text)

print(json.loads(r.text))
