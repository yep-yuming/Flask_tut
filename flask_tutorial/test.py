import requests

BASE = 'http://127.0.0.1:5000/'

data = [{"likes":10,'name':'hello world','views':20},
        {"likes":14,'name':'bye world','views':1111},
        {"likes":18,'name':'hello kitty','views':12345},
        {"likes":1100,'name':'hello batty','views':8888},
]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" +str(i),data[i])
#     print(response.json())


response = requests.patch(BASE + "video/2",{"views":99,"likes":101})    
print(response.json())