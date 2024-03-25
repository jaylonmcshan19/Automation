import requests

url = "http://127.0.0.1:5000/"  # Replace this with your server address if it's different

response = requests.get(url)

if response.status_code == 200:
    print("Server is running successfully!")
    print("Response from server:", response.text)
else:
    print("Failed to connect to the server.")
