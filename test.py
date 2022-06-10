import requests

BASE = "http://127.0.0.1:5000/"


data = [
    {'likes' : 12, 'name' : 'shahriaarrr', 'views' : 1000},
    {'likes' : 100, 'name' : 'yolang', 'views' : 100000000},
    {'likes' : 100, 'name' : 'agah', 'views' : 543522},
    {'likes' : 354, 'name' : 'hasan', 'views' : 70878262}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.patch(BASE + "video/2", {'views' : 1000000, 'likes' : 101})
print(response.json())

input()
response = requests.delete(BASE + "video/8")
print(response) 
input()
response = requests.get(BASE + "video/2")
print(response.json())