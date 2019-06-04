import requests
from flask import Flask, render_template

payload = {"key": "ofAEQPGV9Hv0kZPgzRT6hw", "isbns": 1451648537}
res = requests.get("https://www.goodreads.com/book/review_counts.json", params=payload)
data = res.json()
print(data)
