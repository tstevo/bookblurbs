import tweepy
import bbconfig as cfg

ckey = cfg.twitter['consumer_key']
csecret = cfg.twitter['consumer_secret']
atoken = cfg.twitter['access_token']
atokensecret = cfg.twitter['access_token_secret']

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, atokensecret)
api = tweepy.API(auth)

def main(twttext):
  	status = api.update_status(status=twttext) 

if __name__ == "__main__":
  main()