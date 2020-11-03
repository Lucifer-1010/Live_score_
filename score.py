#@author = Lucifer-1010
# simple python program to notify the live cricket score worldwide...
# for more stuff visit my github at https://www.github.cm/Lucifer-1010

# pip install sports.py
import sports
#pip install py-notifier
from pynotifier import Notification


def cricket(ch):
    matchinfo = sports.get_sport("CRICKET")    
    Notification(title = "Live Cricket score updates Lucifer-1010",
    description = str(matchinfo), duration = 60).send()

def football(ch):
    matchinfo = sports.get_sport("FOOTBALL")    
    Notification(title = "Live Football score updates Lucifer-1010",
    description = str(matchinfo), duration = 60).send()


def hockey(ch):
    matchinfo = sports.get_sport("HOCKEY")    
    Notification(title = "Live HOCKEY score updates Lucifer-1010",
    description = str(matchinfo), duration = 60).send()


def Tennis(ch):
    matchinfo = sports.get_sport("TENNIS")    
    Notification(title = "Live Tennis score updates from Lucifer-1010",
    description = str(matchinfo), duration = 60).send()

def Soccer(ch):
    matchinfo = sports.get_sport("SOCCER")    
    Notification(title = "Live Soccer score updates from Lucifer-1010",
    description = str(matchinfo), duration = 60).send()

def Baseball(ch):
    matchinfo = sports.get_sport("BASEBALL")    
    Notification(title = "Live Baseball score updates from Lucifer-1010",
    description = str(matchinfo), duration = 60).send()


def basketball(ch):
    matchinfo = sports.get_sport("BASKETBALL")    
    Notification(title = "Live Basketball score updates from Lucifer-1010",
    description = str(matchinfo), duration = 60).send()


print(" _      _______      ________    _____  _____ ____  _____  ______       ")
print("| |    |_   _\ \    / /  ____|  / ____|/ ____/ __ \|  __ \|  ____|      ")
print("| |      | |  \ \  / /| |__    | (___ | |   | |  | | |__) | |__         ")
print("| |      | |   \ \/ / |  __|    \___ \| |   | |  | |  _  /|  __|        ")
print("| |____ _| |_   \  /  | |____   ____) | |___| |__| | | \ \| |____ _ _ _ ")
print("|______|_____|   \/   |______| |_____/ \_____\____/|_|  \_\______(_|_|_)")
print("Created by Lucifer-1010")                                                                       
print("\n")    
print("\n")    
print("\n")    

ch = int(input("1.Cricket\n2.Football\n3.Hockey\n4.tennis\n5.soccer\n 6.Baseball\n7.Basketball\nEnter your choice: "))
if ch == 1:
    cricket(ch)
if ch == 2:
    football(ch)
if ch == 3:
    hockey(ch)
if ch == 4:
    Tennis(ch)
if ch == 5:
    Soccer(ch)
if ch == 6:
    Baseball(ch)
if ch == 7:
    basketball(ch)