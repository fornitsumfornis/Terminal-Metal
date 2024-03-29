#!/usr/bin/python3

#This programs contains links to multiple metal radio stations and can be listend through the command line

#Need subprocess to call up bash functions, need colorama Fore, Back, and Style for more robust output
import subprocess, os

from colorama import Fore, Back, Style

#Change the title of the terminal to "Terminal Metal"
def title(header = 'Terminal Metal'):
    subprocess.check_call(['PS1=$'], shell = True)
    subprocess.check_call(['PROMPT_COMMAND='], shell = True)
    print(f'\33]0;{header}\a', end='', flush=True)

def instructions():
    subprocess.check_call(['clear'], shell = True)
    print(Style.BRIGHT)
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
    print('       4    High Voltage')
    print('       5    The Metal MIXX')
    print('       6    100hitz Heavy Metal')
    print('       7    Rock Antenne')
    print('       8    Radio BOB! BOB\'s Metalcore')
    print('       9    Open FM - 500 Heavy Hits')
    print('       10   Rock Antenne')
    print('       q    Exit the Program\n')
    rad=input(Fore.CYAN + '    Please Choose a station: ')
    print('\n')
    if (rad == "1"):
        instructions()
        header = "MetalRock.FM - Baltimore Maryland, USA"
        title(header)
        print(Fore.GREEN +'MetalRock.FM - Baltimore, Maryland, USA\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://kathy.torontocast.com:2820 | cut -d "\'" -s -f 2 --output-delimiter=" " '], shell=True)
         
    elif (rad == "2"):
        instructions()
        header = "Hard Rock Hell Radio - London, United Kingdom"
        title(header)
        print(Fore.GREEN+'Hard Rock Hell Radio - London, United Kingdon')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://andromeda.shoutca.st:9254/stream | cut -d "\'" -s -f 2 --output-delimiter=" " '], shell = True)

    elif (rad == "3"):
        instructions()
        header = "Crucial Velocity Radio - Milverton, Ontario, Canada"
        title(header)
        print(Fore.GREEN +'Crucial Velocity Radio - Milverton, Ontario, Canada\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://ais-sa2.cdnstream1.com/1369_128 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    
    elif (rad == "4"):
        instructions()
        header = "High Voltage - Zug, Switzerland"
        title(header)
        print(Fore.GREEN+'High Voltage - Zug, Switzerland\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://strm112.1.fm/highvoltage_mobile_mp3 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell=True)
    
    elif (rad == "5"):
        instructions()
        header = "The Metal MIXX - Tampa, Florida, USA"
        title(header)
        print(Fore.GREEN+'The Metal MIXX - Tampa, Florida, USA\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet https://ais-sa2.cdnstream1.com/1987_128.mp3 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    
    elif (rad == "6"):
        instructions()
        header = "100hitz Heavy Metal"
        title(header)
        print(Fore.GREEN+'100hitz Heavy Metal\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://pureplay.cdnstream1.com/6015_128.mp3 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True )
    
    elif (rad == "7"):
        instructions()
        header = "Rock Antenne - Ismaning, Germany"
        title(header)
        print(Fore.GREEN+'Rock Antenne - Ismaning, Germany\n')
        print(Fore.GREEN+'(Does not output Song Artist or Song Title)\n')
        subprocess.check_call(['mplayer -afm --really-quiet https://s2-webradio.rockantenne.de/heavy-metal/stream/mp3?aw_0_1st.playerid=radio.de | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    
    elif (rad == "8"):
        instructions()
        header = "Radio BOB! BOB\'s Metalcore - Kassel, Germany"
        title(header)
        print(Fore.GREEN +'Radio BOB! BOB\' Metalcore - Kassel, Germany\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://streams.radiobob.de/metalcore/mp3-192/tunein/ | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    
    elif (rad == "9"):
        instructions()
        header = "Open FM - 500 Heavy Hits - Warsaw Poland"
        title(header)
        print(Fore.GREEN +'Open FM - 500 Heavy Hits - Warsaw, Poland\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet http://stream.open.fm/54 | cut -d "\'" -s -f 2 --output-delimiter=" "'], shell = True)
    
    elif(rad == "10"):
        instructions()
        header = "Rock Antenne - Ismaning, Germany"
        title(header)
        print(Fore.GREEN +'Rock Antenne - Ismaning, Germany\n')
        subprocess.check_call(['mplayer -nocache -afm --really-quiet https://s5-webradio.rockantenne.de/heavy-metal/stream/mp3?aw_0_1st.playerid=radio.de | cut -d "\'" -s -f 2 --output-delimiter= " "'], shell = True)

    elif (rad == "q"):
        print('\nKickass!  See you later!\n')
    
    else:
        subprocess.check_call(['clear'], shell = True)
        print('\n***Please enter a valid choice.***')
        subprocess.check_call(['sleep 2'], shell = True)
        subprocess.check_call(['clear'], shell = True)
        query()

def main():
    subprocess.check_call(['clear'], shell = True)
    query()

main()
