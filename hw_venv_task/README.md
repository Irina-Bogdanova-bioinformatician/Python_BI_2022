# Instructions for running the ultraviolence.py script

This instruction is intended to run the script on the following system:
Ubuntu-20.04 on WSL2 on Windows 11 (for home), version 21H2, build 10.0.22000.978

### Requirements
python==3.11\
gcc==9.4.0

If these requirements are not satisfied, run:
~~~sh
sudo apt install python3.11
sudo apt-get install gcc
~~~

### Create and activate virtual environment
In work directory run:
~~~sh
python3.11 -m venv new_venv_name
source new_venv_name/bin/activate
~~~

### Install requirements
Run:
~~~sh
pip install -r requirements.txt
~~~

### Change frame.py in pandas package installed to new venv
 Open path/to/new_venv_name/lib/python3.11/site-packages/pandas/core/frame.py.\
 Don't be shy and comment out the lines 635, 636.\
 These two:\
 635      if index is not None and isinstance(index, set):\
 636          raise ValueError("index cannot be a set")

### Run ultraviolence.py
Run:
~~~sh
python3 ultraviolence.py
~~~
