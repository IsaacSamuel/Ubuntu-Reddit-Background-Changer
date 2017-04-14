# Ubuntu Reddit Background Changer

This is a simple program that scrapes the top photos from the last week of several popular subreddits and automatically sets them as your background in Ubuntu (or similar Gnome enviornment, though other systems are untested).

To run it, simply download it and run it via the command-line.

`python ~/Downloads/Background_Changer/main.py <Arg1> <Arg2>`

 "Arg1" represents the subreddits you want to pull from ('S' represents /r/SpacePorn (SFW!), 'E' represents /r/EarthPorn (also SFW!), and 'P' represents /r/pic) and you can input any combination in any order. "Arg2" represents the interval you'd like to space between the changing of the background.

 For example, to download from /r/pic and /r/EarthPorn with the background changing every 2 hours:

 `python ~/Downloads/Background_Changer/main.py PE 120`


### Running automatically

 I hope to create a setup one day that will install this software for you, but I ran into technical snags. For now, to run this file automatically, you must (according to the [Ubuntu Documentation](https://help.ubuntu.com/stable/ubuntu-help/startup-applications.html):

 > Use the Dash to find and open Startup Applications. Alternatively you can press Alt+F2 and run the gnome-session-properties command.

> Click Add and enter the command to be executed at login (name and comment are optional). For example, to make Firefox start automatically, it's sufficient to type firefox in the Command field and confirm with Add.

In other words, open Startup Applications from the dash, hit add, enter something like `python ~/Downloads/Background_Changer/main.py PE 120`, and preferably name it something like Ubuntu Background Changer.


Hope you enjoy!
