import requests

timeout = 2

bad = []
good = []


proxy_file = open("proxies.txt", "r")
proxies = proxy_file.read()
proxies = proxies.splitlines()

for proxy in proxies:
  try:
      print("Checking: " + proxy)
      resp = (requests.get("http://discord.com", proxies={"http":"http://" + proxy, "https": "https://" + proxy}, timeout=timeout)) 
      good.append(proxy)
  except requests.exceptions.ProxyError:
      bad.append(proxy)
      pass
  except requests.exceptions.ConnectionError:
      bad.append(proxy)
      pass
    

print("\nBad:")
print('\n'.join(bad))
print("\nGood:")
print('\n'.join(good))
