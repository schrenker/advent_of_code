import requests

if __name__ == "__main__":
    r = requests.get("https://wp.pl")
    print(r.status_code)
