import requests

param = {"q":"python"}

r = requests.get('http://www.google.com',params=param)

print("Status : " ,r.status_code)

print("Header : " ,r.headers['content-type'])
print("Contnet : ",r.text)

f = open("page.html","w+")
f.write(r.text)
f.close()