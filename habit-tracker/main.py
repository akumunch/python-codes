import requests 
from datetime import datetime
import os

pixela_endpoint= "https://pixe.la/v1/users"
USERNAME= "akumunch"
TOKEN= os.environ.get("TOKEN")

params= {
    "token":TOKEN,
    "username":"akumunch",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

request= requests.post(url=pixela_endpoint,json=params)

# graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config= {
#     "id":"graph2",
#     "name":"Cycling Graph",
#     "unit":"kms",
#     "type":"float",
#     "color":"ichou",
#     "timezone":"Asia/Kolkata",
# }
headers={
    "X-USER-TOKEN":TOKEN
}
# response= requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
today= datetime.now()
pixel_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_config= {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("Enter the distance you cycled: "),
}
response= requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)

# today= datetime.now()
# update_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
# pixel_config= {
#     "quantity":"20.5",
# }
# response= requests.put(url=update_endpoint,json=pixel_config,headers=headers)
# print(response.text)
# delete_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
# response= requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)