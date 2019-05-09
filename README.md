# Metal-Radio
Just a command line interface for an internet radio station.  The program is written in python but uses bash calls to stream the stations.
It's nothing fancy, but I wanted a command line way of accessing multiple metal stations without having to open a browser (I listen to music from a Raspberry Pi in my office).  So I wrote the code and voila, Metal Music Player! 

![Metal to the End!](https://github.com/fornitsumfornis/Metal-Radio-CLI/blob/master/1.png)

## Dependencies
This depends on quite a few packages unfortunately.  Dependencies include myplayer (sudo apt-get install myplayer -y), python (sudo apt-get install python3.5 -y), Pip (sudo apt-get install python-pip -y) and finally Colroama (pip install colorama).  

Additionally to filter out extraneous info open up your .mplayer/config file and add these lines:

lirc=no  
prefer-ipv4=yes

This should filter out all of the error messsages and leave you with the just the artist and song title! (Plus a pesky semi-colon I haven't figured out how to get rid of yet.)
