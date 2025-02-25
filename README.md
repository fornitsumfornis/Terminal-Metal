# Terminal-Metal
Just a command line interface for an internet radio station for linux distributions.  The program is written in python but uses bash calls to stream the stations.
It's nothing fancy, but I wanted a command line way of accessing multiple metal stations without having to open a browser (I listen to music from a Raspberry Pi in my office).  So I wrote the code and voila, Metal Music Player! 

![Metal to the End!](https://github.com/fornitsumfornis/Metal-Radio-CLI/blob/master/terminal-metal.png)

## Dependencies
This depends on quite a few packages unfortunately.  Dependencies include myplayer, python3.5 or higher, Pip (sudo apt-get install python3-pip) and finally Colroama (pip3 install colorama).  

Additionally to filter out extraneous info open up your .mplayer/config file and add these lines:

lirc=no  
prefer-ipv4=yes

This should filter out all of the error messsages and leave you with the just the artist and song title!

## Distributions

The actual script, when placed in the /usr/local/bin folder, will work in any linux distribution.  The install script, however, only works in debian and debian based distributions.

## Installation

git clone https://github.com/fornitsumfornis/Terminal-Metal.git

cd Terminal-Metal-Master

chmod 755 metal  

sudo mv metal /usr/local/bin

## Usage

To operate, simply open up the command line and type "metal.py".  Choose your station and headbang away!  If you chose the install script it should be located under "Sound & Video".

## Problems

I have run into issues using my script on certain networks.  For example, I have a guest network at the University that I work at and there are limits to what stations will work on our guest network.
