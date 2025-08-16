import requests

def requests_examples():
    print("Requests examples below")
    github_example = requests.get("https://api.github.com/")

    print(f"Status code: {github_example.status_code}")
    print(f"Response json: {github_example.json()}")
    print("___________________________________")
    pass
