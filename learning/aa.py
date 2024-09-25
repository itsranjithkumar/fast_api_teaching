


    import requests

while True:
    # make an api call to any url
    response = requests.get("https://xamprepp-v3-flask-api-s.onrender.com/")
    print(response.text)
    print(response.status_code)