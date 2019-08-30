# Script-Tweet-Bot
A bot that automatically tweets through a text file

Setting up;

Create a twitter developer account and add your API credentials to the auth.py file.

create a file named script.txt, this file will contain the script that the bot will cycle through.


Optional feature:-
The bot can also tweet out the episode name and number, to tell the bot what the episode is called, preface that episode's script with:

UPDATELINE 1 1 Pilot

This will make the bot tweet
"Next Episode: Season 1 Episode 1 - Pilot"

Another example would be:

UPDATELINE 7 13 The Seminar

to tweet:
"Next Episode: Season 7 Episode 13 - The Seminar"


