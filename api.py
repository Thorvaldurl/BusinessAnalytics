import requests

# Replace <YOUR-TOKEN> with your actual API token
token = "SG_APIM_CM1M3GXGSA98V8PJ19BQDJPM238NHTTS5TVT7JM7Y2E2VEDBFQQ0"
headers = {
    "Authorization": f"Bearer {token}"
}

# Example URL: fetching food waste info by zip code (e.g., zip code 8000)
url = "https://api.sallinggroup.com/v1/food-waste/?zip=8000"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data[0])
    print("Data fetched successfully:")
else:
    print("Error:", response.status_code)
    print(response.text)
