import requests

def main():
    res = requests.get("http://data.fixer.io/api/convert?access_key=cbbde527c6e67279e2ccda54b4d6fb51&from=ZAR&to=USD,GBP,USD,JPY&amount=6000")
    if res.status_code != 200:
        raise Exception("ERROR: API Requests unsuccessful")
    data = res.json()
    print(data)

if __name__ == '__main__':
    main()
