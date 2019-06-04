import requests

def main():
    base = input("First currency: ")
    other = input("Second currency: ")
    res = requests.get("http://data.fixer.io/api/latest?access_key=cbbde527c6e67279e2ccda54b4d6fb51",
                    params={"base": base, "symbols": other})
    if res.status_code != 200:
        raise Exception("ERROR: API Requests unsuccessful")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == '__main__':
    main()
