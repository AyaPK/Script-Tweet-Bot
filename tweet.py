from twython import Twython
from twython import TwythonError
import json
import os
tweetmode = False
class WriteTweet:
    def __init__(self, tweet):
        if tweetmode:
            from auth import (
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
            )
            twitter = Twython(
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
            )
            while True:
                try:
                    twitter.update_status(status=tweet)
                    break
                except TwythonError as e:
                    if e.error_code == 403:
                        tweet = f"-{tweet}"
                    else:
                        print("Error with tweet")
                        print(e)
                        os.system("pause")


            with open("Tracking.json", "r") as f:
                info = json.load(f)
                num = info["Main"]["LinesPrinted"]
                num += 1
                info["Main"]["LinesPrinted"] = num
                info["Main"]["LastLine"] = tweet
            with open("Tracking.json", "w+") as w:
                json.dump(info, w, indent=4)
        else:
            print(tweet)
            with open("Tracking.json", "r") as f:
                info = json.load(f)
                num = info["Main"]["LinesPrinted"]
                num += 1
                info["Main"]["LinesPrinted"] = num
                info["Main"]["LastLine"] = tweet
            with open("Tracking.json", "w+") as w:
                json.dump(info, w, indent=4)

class Updater:
    def __init__(self, season, ep, name):
        if tweetmode:
            from auth import (
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
            )
            twitter = Twython(
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
            )
            twitter.update_profile(description=f"A bot posting the entire US Office script one line at a time. Currently on Season {season}, Episode {ep} - {name}. Transcripts from officequotes.net")