# Script-Tweet-Bot
A bot that automatically tweets through a text file, based on bots such as the IASIP Script bot.

To see a bot that I have set up to be running with this script, see @TheUSOfficeBot

Setting up;

Create a twitter developer account and add your API credentials to the auth.py file.

create a file named script.txt, this file will contain the script that the bot will cycle through.
The bot will tweet one line at a time with each time the program has been run.
Don't worry about adapting lines to fall under the 280 character limit, the bot handles this automatically.

Once the script.txt is set up, run main.py a couple of times to ensure the bot is tweeting as intended.

Simply use your favourite automation method to tell main.py to run whenever you want it to run and let the program handle the rest.


Optional feature:-
The bot can also tweet out the episode name and number before it begins tweeting that episode, to tell the bot what the episode is called, preface that episode's script with:

UPDATELINE 1 1 Pilot

This will make the bot tweet
"Next Episode: Season 1 Episode 1 - Pilot"

Another example would be:

UPDATELINE 7 13 The Seminar

to tweet:
"Next Episode: Season 7 Episode 13 - The Seminar"
