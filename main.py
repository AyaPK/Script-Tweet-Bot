import json
import os
import time
import tweet

with open("Tracking.json", "r") as f:
    info = json.load(f)
    epnum = info["Main"]["EpNum"]
    epname = info["Main"]["EpName"]
    linenum = info["Main"]["LineNum"]
    seasonnum = info["Main"]["SeasonNum"]

def prepare():
    global linenum

    with open(f"script.txt", "r") as f:
        script = f.readlines()
        currentline = script[linenum]

    if "UPDATELINE" in currentline:
        currentseason = currentline.split()[1]
        currentep = currentline.split()[2]
        eptitle = " ".join(currentline.split()[3:])
        with open("Tracking.json", "r") as f:
            info = json.load(f)
            info["Main"]["EpNum"] = currentep
            info["Main"]["SeasonNum"] = currentseason
            info["Main"]["EpName"] = eptitle
        with open("Tracking.json", "w") as w:
            json.dump(info, w, indent=4)
        linenum += 1
        currentline = f"Next Episode: Season {currentseason} Episode {currentep} - {eptitle}"
        tweet.WriteTweet(currentline)
    elif currentline == "\n":
        linenum += 1
        prepare()
    else:
        if len(currentline) <= 280:
            tweet.WriteTweet(currentline)
        else:
            currentline = currentline.replace(". ", ".\n")
            with open(f"script.txt", "r") as f:
                script = f.readlines()
                script[linenum] = currentline
                with open(f"script.txt", "w+") as w:
                    w.writelines(script)
            with open("script.txt", "r") as f:
                script = f.readlines()
                currentline = script[linenum]
            tweet.WriteTweet(currentline)
    with open("Tracking.json", "r") as f:
        info = json.load(f)
        info["Main"]["LineNum"] = linenum+1
        with open("Tracking.json", "w") as w:
            json.dump(info, w, indent=4)

prepare()