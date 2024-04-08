import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello, world!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# import requests
# 
# client_id = '...'
# client_secret = '...'  # get it from .env
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# payload = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret}
# response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=payload)
# access_token = response.json()['access_token']
# 
# # guess you need to do this workflow...
# # https://developer.spotify.com/documentation/web-api/tutorials/code-flow
# headers = {'Authorization': f'Bearer {access_token}'}
# response = requests.get('https://api.spotify.com/v1/me', headers=headers)
# print(response.json())
