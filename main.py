import json
import os
import time
import tweet

with open("Tracking.json", "r") as f:
    info = json.load(f)
    epnum = info["Main"]["Song"]
    linenum = info["Main"]["LineNum"]
    seasonnum = info["Main"]["Album"]

def splitlongquotes(quote):
    quotenew = quote.split(".")

    notweet = True
    startplace = 0
    while notweet:

        pt1 = quotenew[startplace]
        try:
            pt2 = quotenew[startplace + 1]
        except:
            break
        test = f"{pt1} {pt2}"
        if len(test) <= 280:
            quotenew[startplace] = test
            quotenew.pop(startplace + 1)
        if len(test) > 280:
            quotenew[startplace] = f"{quotenew[startplace]}\n"
            startplace += 1
    output = ""
    for quote in quotenew:
        out = quote.replace("  ", ". ")
        output = f"{output}{out}"
    return output

def prepare():
    global linenum

    with open(f"script.txt", "r") as f:
        script = f.readlines()
        currentline = script[linenum]

    if "UPDATELINE" in currentline:
        currentalbum = currentline.split("-")[1]
        currentsong = currentline.split("-")[2]
        with open("Tracking.json", "r") as f:
            info = json.load(f)
            info["Main"]["Song"] = currentsong
            info["Main"]["Album"] = currentalbum
        with open("Tracking.json", "w") as w:
            json.dump(info, w, indent=4)
        linenum += 1
        currentline = f"Next song:{currentalbum}-{currentsong}"
        tweet.WriteTweet(currentline)
        tweet.Updater(currentalbum, currentsong)
    elif currentline == "\n" or currentline == "" or currentline == " \n":
        linenum += 1
        prepare()
    else:
        if len(currentline) <= 280:
            tweet.WriteTweet(currentline)
        else:
            currentline = splitlongquotes(currentline)
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