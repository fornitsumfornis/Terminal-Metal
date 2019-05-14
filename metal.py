#!/usr/bin/python3.5

#This programs contains links to multiple metal radio stations and can be listend through the command line

import subprocess
from subprocess import Popen
from colorama import Fore, Back, Style

def instructions():
    print(Fore.YELLOW+'********************************************************')
    print(Fore.YELLOW+'*',Fore.MAGENTA+'Press "q" to quit, "p" to pause',Fore.YELLOW+'                     *')
    print(Fore.YELLOW+'*',Fore.MAGENTA+'Press "9" to decrease volume, "0" to increase volume',Fore.YELLOW+'*')
    print(Fore.YELLOW+'********************************************************',)


def query():
    print(Style.BRIGHT)
    print(Fore.GREEN + '\n***Welcome to the Metal Internet Radio Player!***')
    print(Fore.RED + '       **Where it\'s metal to the end!**\n')
    print(Fore.YELLOW + '\n       1    MetalRock.FM')
    print(Fore.YELLOW + '       2    Hard Rock Hell Radio')
    print('       3    Crucial Velocity Radio')
    print('       4    Mix Rock Metal Radio')
    print('       5    The Metal MIXX')
    print('       6    100hitz Heavy Metal')
    print('       7    XXX Rock FM')
    print('       8    Wild Rock Radio')
    print('       9    Exit the Program\n')
    rad=input(Fore.CYAN + '    Please Choose a station: ')
    print('\n')
    rad = float(rad)
    if (rad == 1):
        instructions()
        print(Fore.GREEN +'MetalRock.FM - Baltimore, Maryland, USA\n')
        subprocess.check_call(['mplayer -afm --really-quiet http://bb30.sonixcast.com:9408/stream | cut -d "\'" -s -f 2 --output-delimiter=" " '], shell=True)
    elif (rad == 2):
        instructions()
        print(Fore.GREEN+'Hard Rock Hell Radio - London, United Kingdon\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://andromeda.shoutca.st:9254/stream | cut -d "\'" -s -f 2 --output-delimiter=" " '], shell = True)
    elif (rad == 3):
        instructions()
        print(Fore.GREEN +'Crucial Velocity Radio - Milverton, Ontario, Canada\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://ais-sa2.cdnstream1.com/1369_128 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    elif (rad == 4):
        instructions()
        print(Fore.GREEN+'Mix Rock Metal Radio - Toronto, Ontario, Canada\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://94.23.23.97:13092/ | cut -d ";" -s -f1- --output-delimiter=" "'], shell=True)
    elif (rad == 5):
        instructions()
        print(Fore.GREEN+'The Metal MIXX - Tampa, Florida, USA\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://listen.djcmedia.com/metalmixxhigh | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    elif (rad == 6):
        instructions()
        print(Fore.GREEN+'100hitz Heavy Metal\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://pureplay.cdnstream1.com/6015_128.mp3 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True )
    elif (rad == 7):
        instructions()
        print(Fore.GREEN+'XXX Rock FM - Los Angeles, California, USA\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://sc15.shoutcaststreaming.us:8140 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    elif (rad == 8):
        instructions()
        print(Fore.GREEN + 'Wild Rock Radio - Los Angeles, California, USA\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://64.150.176.87:8287 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    else:
        print('\nKickass!  See you later!\n')

def main():
    subprocess.check_call(['clear'], shell = True)
    query()

main()
