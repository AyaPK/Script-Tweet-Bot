from twython import Twython
import json

tweetmode = True

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
            twitter.update_status(status=tweet)

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

class Updater:
    def __init__(self, album, song):
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
            twitter.update_profile(description=f"Bot posting the Lyrics to Taylor Swift songs one line at a time. Current song:{album}-{song}")