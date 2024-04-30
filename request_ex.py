import requests

def fetch_api_app():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    #print(response)
    data=response.json()
    if data["success"] and "data" in data:
        userdata=data['data']
        username = userdata['login']['username']
        location1 = userdata['location']['country']
        birth=userdata['dob']['age']
        act = userdata['email']
        return username,location1,birth,act
    else:
        return 'Not Found'
    

print(fetch_api_app())