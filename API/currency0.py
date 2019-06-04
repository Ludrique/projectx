import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=cbbde527c6e67279e2ccda54b4d6fb51")
    print(res)

if __name__ == '__main__':
    main()
