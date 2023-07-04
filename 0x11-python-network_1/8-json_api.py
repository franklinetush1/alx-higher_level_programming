import sys
import requests

letter = sys.argv[1] if len(sys.argv) > 1 else ""
payload = {"q": letter}
resp = requests.post("http://0.0.0.0:5000/search_user", data=payload)

try:
    js_response = resp.json()
    if js_response:
        user = js_response.get("name")
        user_id = js_response.get("id")
        print("[{}] {}".format(user_id, user))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
