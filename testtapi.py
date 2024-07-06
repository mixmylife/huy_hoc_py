import requests

url = "https://tiki.vn/api/v2/products/271972435?platform=web&spid=271972437&version=3"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

