import requests
import  json

url = "http://127.0.0.1:8000/stucreate/"
def post_data():
   data = {
       "id": "1",
      "name": "mudassir",
      "roll": "3456",
      "city": "lahore",
   }
   json_data = json.dumps(data)
   r = requests.post(url = url,data = json_data)
   data = r.json()
   print(data)
post_data()


# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id': id}
#
#     json_data = json.dumps(data)
#     r = requests.get(url = url, data = json_data)
#     print(r.json())
# get_data()

# def update_data():
#     data = {
#         'id': 1,
#         'name': 'ali',
#         'city': 'Multan'
#     }
#     json_data = json.dumps(data)
#     r = requests.put(url = url, data = json_data)
#     print(r.json())
# update_data()
# def delete_data():
#     data = {'id': 1}
#     json_data = json.dumps(data)
#     r = requests.delete(url= url, data = json_data)
#     print(r.json())
# delete_data()


