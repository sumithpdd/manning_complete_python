import requests

my_data = {"name": "John", "email": "test@test.com"}
r = requests.post("http://httpbin.org/post", data=my_data)  

print("Status code:", r.status_code)    
f = open("./myfile.html", "w+")
f.write(r.text)

