# os_and_sys

Python scripts that are analogous to the following UNIX utilities: wc (with -l -w -c options), ls (with -a option), rm (with -r option), sort (no options).

## Requirements:
python>=3.6

## Description

### wc.py

Unix wc imitation.
  
Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified. With no FILE, or when FILE is -, read standard input.

**Options**:
- [-c, --bytes] Print the byte counts.
- [-l, --lines] Print the newline counts.
- [-w, --words] Print the word counts.

**Usage:**
Run in directory containing wc.py:
~~~sh
./wc.py [OPTION] [FILE or FILES]
~~~

### ls.py

Unix ls imitation.
  
List information about the FILEs (the current directory by default).

**Options**:
- [-a, --all] Do not ignore entries starting with '.'

**Usage:**
Run in directory containing ls.py:
~~~sh
./ls.py [OPTION] [DIR]
~~~

### sort.py

Unix sort imitation.
  
Write sorted concatenation of all FILE(s) to standard output. With no FILE, or when FILE is -, read standard input.

**Usage:**
Run in directory containing sort.py:
~~~sh
./sort.py [FILE or FILES]
~~~

### rm.py

Unix rm imitation.
  
Remove each specified file. By default, it does not remove directories.

**Options**:
- [-r, --recursive'] Remove directories and their contents recursively.

**Usage:**
Run in directory containing rm.py:
~~~sh
./rm.py [OPTION] [FILE/FILES/DIR]
~~~
