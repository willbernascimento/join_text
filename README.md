# join_text: Concatenate multiples text files
A simple program to concatenate multiple text files written in python 3.

# INSTALL

## Linux

On Linux there are many different ways to use this programing. You may need to make the file executable: 

```bash
$ chmod +x /pathTofile/join_text.py

```

### Locally
You do not need root or sudo powers if you call this program in your user folder.

1. You can call the script using its address. For example:

```bash
$ python /pathTofile/join_text.py

```

2. You can paste your file into a specific folder and insert it into the environment variable group (PATH).

Create a directory for executable if not exists 

```bash
$ mkdir -p ~/bin/ 

```
Copy the script file to your new folder

```bash
$ cp /pathTofile/join_text.py ~/bin/join_text

```

Edit a .bash_profile, .bashrc or .zshrc file e inset that directory in your PATH

```bash
$ export PATH=~/bin:$PATH
```

### Globally
If you want to make this program available globally to your system, you will need root powers. You can place this program in several executable locations. An example would be:

```bash
$ sudo cp /pathTofile/join_text.py /usr/local/bin/
```

## Windows and Mac OS
I believe the script should work on these systems, but I have no deeper knowledge to configure this script on them. Feel free to develop your solutions.

## USAGE

----------------------:----------------------------------------------
 -h, --help           | show this help message and exit
 --type TYPE          | file type: .txt and .csv is working good
 --label LABEL        | The output file name
 --override OVERRIDE  | Remove existing file with same name as output file
----------------------:----------------------------------------------

### Get help
```bash
$ join_text -h
```


## DISCLAIMER
This software is not warranted of any kind. Use at your own risk.


