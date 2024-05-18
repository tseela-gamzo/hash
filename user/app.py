import requests

# The user should do 2 things:
# 1) get a proof from the server of moadon tov
# 2) send a proof to the store server


# Here is a way of sending data to the server
url = 'http://localhost:5050/api'
json_data = {'message': 'hii :), af paam lo raiti od hiyuh kaze (lo, lo, lo)'}

try:
    # Send the POST request and capture the response
    response = requests.post(url, json=json_data)
    print('Status Code:', response.status_code)
    print('Response Content:', response.text)
    response.raise_for_status()  # Raise an HTTPError if the response was unsuccessful
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')