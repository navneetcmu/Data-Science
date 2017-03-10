import urllib3
import numpy as np
import bs4
from bs4 import BeautifulSoup
import tweepy

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "pg1kVXaCrfvdjDVIDdLj3ox7W",
    "consumer_secret"     : "Oj7M2CrtSz6MRRjSmL0ufSzlbApOG861Zo7vLtnC5bYf3r56SM",
    "access_token"        : "2205419940-X8vghsGjEqKEC6lfeIJh5BoaaFR6lhKtTJHVIWq",
    "access_token_secret" : "kgKLdE6054KeH7LspE4EqSLJqy4AgGkvIYRebDlCF9bXZ"
    }

  api = get_api(cfg)
  query1 = 'https://www.google.com/search?q='
  query3 = '%20share%20price'
  sharename = ['google','microsoft']
  for i, item in enumerate(sharename):
    query = query1 + sharename[i] + query3
    twstr = str(sharename[i] + "  " +str(magic(query)))
    status = api.update_status(status=twstr)
  # Yes, tweet is called 'status' rather confusing

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def magic(query):
    http = urllib3.PoolManager()
    urllib3.disable_warnings()

    r_go = http.request('GET', query)
    bsa_tree = bs4.BeautifulSoup(r_go.data, "lxml")
    share_price = bsa_tree.find_all("b")

    newstr = str(share_price[1])

    digits = [int(e) for e in newstr if e.isdigit()]
    price = np.sum([digit*(10**exponent) for digit, exponent in
                        zip(digits[::-1], range(len(digits)))])
    return price/100

if __name__ == '__main__':
    main()
