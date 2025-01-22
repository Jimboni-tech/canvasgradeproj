import requests
ACCESS_TOKEN = input("Please enter your access token: ")
URL = input("Please enter you instructures Canvas URL")

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}


response = requests.get(URL, headers=headers)


print(response.status_code)