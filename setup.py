import os


print("Welcome to the Reddit Ubuntu Background changer. First off, which subreddits would you like to pull from? Your options are /r/SpacePorn (S), /r/EarthPorn (E) and /r/pic (P). Enter your choices in any order. (Default: All")
x = raw_input()

if 'S' in x and 'P' in x and 'E' in x:
	#Get pics from /r/SpacePorn, /r/Pic, /r/EarthPorn
	arg = 'SPE'

elif 'S' in x and 'P' in x:
	#Get pics from /r/SpacePorn, /r/Pic
	arg = 'SP'

elif 'S' in x and 'E' in x:
	#Get pics from /r/SpacePorn, /r/EarthPorn
	arg = 'SE'
elif 'E' in x and 'P' in x:
	#Get pics from /r/EarthPorn, /r/Pic
	arg = 'EP'

elif 'P' in x:
	#Get pics from /r/Pic
	arg = 'P'
elif 'E' in x:
	#Get pics from /r/EarthPorn
	arg = 'E'
elif 'S' in x:
	#Get pics from /r/SpacePorn
	arg = 'S'
else:
	print("Argument not recognized. Resorting to default.")
	arg = 'SPE'

print("How often would you like it to take place (enter answer in minutes)? ")
minutes = float(input())*60

path = os.path.abspath('.')

with open(os.path.expanduser("~/.config/autostart/a.desktop"), "w") as file:
	command = "[Desktop Entry] \nType=Application \nExec=python {}/main.py {} {}\nName=desktop_changer\nX-GNOME-Autostart-enabled=true\n".format(path, arg, minutes)
	file.write(command)

os.system("python main.py %s %s" % (arg, minutes))

	