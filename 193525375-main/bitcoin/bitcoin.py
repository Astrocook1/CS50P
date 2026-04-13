import requests
import sys
try:
    coin = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument ")
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    pass
try:
    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=6675c3898e060af431d42470ab4e06a57c729ced1545db880af84779ab0716f3')
    price = float(r.json()['data']['priceUsd'])
except requests.RequestException:
    sys.exit()
else:
    pass

print(f"${price*coin:,.4f}")
