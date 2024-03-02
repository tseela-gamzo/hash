import requests

# The user should do 2 things:
# 1) get a proof from the server of moadon tov
# 2) send a proof to the store server



# Here is a way of getting data from a server
url = 'http://localhost:5000'

# Sending a GET request
response = requests.get(url)

# Print the response
print("Response Status Code:", response.status_code)
print("Response Body:", response.text)



# Here is a way of sending data to a server
url = 'http://example.com/api'
data = {'message': 'hello'}

# try to send the data
try:
    # send a POST request
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message. Status code:", response.status_code)
# If an error occured -> print error information
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

