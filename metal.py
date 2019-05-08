#!/usr/bin/python3.5

#This programs contains links to multiple metal radio stations and can be listend through the command line

import subprocess
from subprocess import Popen
from colorama import Fore, Back, Style

def cut():
    subprocess.check_call(['cat radio.dat | cut -d "=" -s -f2- --output-delimiter=" " | tr -d ";"'], shell = True) 

def query():
    print(Fore.GREEN + '\n***Welcome to the Metal Internet Radio Player!***')
    print(Fore.RED + '       **Where it\'s metal to the end!**\n')
    print(Fore.YELLOW + '\n       1    MetalRock.FM')
    print(Fore.YELLOW + '       2    Hard Rock Hell Radio')
    print('       3    Crucial Velocity Radio')
    print('       4    Mix Rock Metal Radio')
    print('       5    The Metal MIXX')
    print('       6    100hitz Heavy Metal')
    print('       7    XXX Rock FM')
    print('       8    Exit the Program\n')
    print('    Press "q" to quit and "p" to pause\n')
    print('    Press "9" to decrease voume, "0" to increase volume\n')
    rad=input(Fore.CYAN + '    Please Choose a station: ')
    print('\n')
    rad = float(rad)
    if (rad == 1):
        subprocess.check_call(['mplayer -afm --really-quiet http://bb30.sonixcast.com:9408/stream | cut -d "\'" -s -f2- --output-delimiter=" " '], shell=True)
    elif (rad == 2):
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://andromeda.shoutca.st:9254/stream | cut -d "\'" -s -f2- --output-delimiter=" " '], shell = True)
    elif (rad == 3):
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://ais-sa2.cdnstream1.com/1369_128 | cut -d "=" -s -f2- --output-delimiter=" "'], shell = True)
    elif (rad == 4):
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://94.23.23.97:13092/ | cut -d "\'" -s -f1- --output-delimiter=" "'], shell=True)
    elif (rad == 5):
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://listen.djcmedia.com/metalmixxhigh | cut -d "\'" -s -f2- --output-delimiter=" "'], shell = True)
    elif (rad == 6):
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://pureplay.cdnstream1.com/6015_128.mp3 | cut -d "=\'" -s -f2- --output-delimiter=" "'], shell = True )
    elif (rad == 7):
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://sc15.shoutcaststreaming.us:8140 | cut -d "\'" -s -f2- --output-delimiter=" "'], shell = True)
    else:
        print('\nKickass!  See you later!\n')

def main():
    subprocess.check_call(['clear'], shell = True)
    query()

main()
