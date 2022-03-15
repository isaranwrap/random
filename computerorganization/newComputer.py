# 
#
#
# Date goes here: April 4, 2022
#
#


## This is meant to be incredibly comprehensive. Bit of a readme-esque intro here, but I try to capture all the relevant details when starting a new computer and getting setup to speed
 

# First, specs: I'm working on Linux Ubuntu 20.04 here. 
# The way to check is to go Settings > About in the search bar or else 
# >> lsb_release -a 
# from commandline

# Second, I install jupyter notebook with
# >> sudo snap install jupyter
# which takes a few minutes


# Third, I get the Python versions to match up. Since Ubuntu Linux comes with Python pre-installed, there is a default Python, which can be found with 
# >> which python3
# /usr/bin/python3, for me.

# Now, if I run `which jupyter` i find it in /snap/bin/jupyter and if i open a jupyter notebook
# and run !which python from a code shell, I get /snap/jupyter/6/bin/python

# So, we've got different python versions and we need to sync them up. This is achieved by
# ensuring the file Paths are the same. So,  what follows is:

### https://gist.github.com/yasushisakai/86da64df10581d37af709387f45f9312
# 3.1 
# Open two instances of Python. One from cmd/terminal and one jupyter notebook
# >> python3
# Python 3.8.10 (default, DATETIME) 
## >> jupyter notebook & 
# 18225
# The commands are the same: 
# 
#
# >> import sys
# >> print(sys.path)

# So, here's the sys.path from jupyter:
# ['/home/ishi/github/AKITomorrow', '/snap/jupyter/6/lib/python37.zip', '/snap/jupyter/6/lib/python3.7', '/snap/jupyter/6/lib/python3.7/lib-dynload', '', '/snap/jupyter/6/lib/python3.7/site-packages', '/snap/jupyter/6/lib/python3.7/site-packages/IPython/extensions', '/home/ishi/snap/jupyter/6/.ipython']

# And here's the sys.path from terminal python:
# ['', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']

import os, sys 
print('Current working directory: {}'.format(os.getcwd()))
print('Files: {}'.format(os.listdir()))
print(sys.path)

python_paths = dict()
python_paths['jupyter'] = ['/home/ishi/github/AKITomorrow', '/snap/jupyter/6/lib/python37.zip', '/snap/jupyter/6/lib/python3.7', '/snap/jupyter/6/lib/python3.7/lib-dynload', '', '/snap/jupyter/6/lib/python3.7/site-packages', '/snap/jupyter/6/lib/python3.7/site-packages/IPython/extensions', '/home/ishi/snap/jupyter/6/.ipython'] # Just copy & pasted
python_paths['cmd'] = ['', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']

# So now, I add those in one but not the other. Let me first check which one is in Jupyter but not the system
for p in sys.path:
	if p not in python_paths['cmd']:
		print(p)
		

