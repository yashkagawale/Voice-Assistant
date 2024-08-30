import requests

api_addrees ="https://newsapi.org/v2/top-headlines?country=in&apiKey=f402164ccf374ca4bdbcca0e1dfc64d3"
json_data = requests.get(api_addrees).json()


ar=[]


def news():
    for i in range(4):
        ar.append("Number " + str(i+1) + ":" + json_data["articles"][i]["title"]+".")

    return ar