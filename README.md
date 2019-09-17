# text_bind: Concatenate multiple text files
A simple program to concatenate multiple text files written in Python 3.

# INSTALL

## Linux

### Download
```bash
git clone https://github.com/willbernascimento/text_bind.git

```

### Dependencies
Your can see requeriments on *requeriments.txt* file. If you use [pip](https://pip.pypa.io/en/latest/reference/pip_install/#id18):

```bash
pip install requeriments.txt

```

On Linux there are many different ways to use this programing. You may need to make the file executable: 

```bash
$ chmod +x /pathTofile/text_bind.py

```

### Locally
You do not need root or sudo powers if you call this program in your user folder.

1. You can call the script using its address. For example:

```bash
$ python /pathTofile/text_bind.py

```

2. You can paste your file into a specific folder and insert it into the environment variable group (PATH).

Create a directory for executable if not exists 

```bash
$ mkdir -p ~/bin/ 

```
Copy the script file to your new folder

```bash
$ cp /pathTofile/text_bind.py ~/bin/text_bind

```

Edit a .bash_profile, .bashrc or .zshrc file e inset that directory in your PATH

```bash
$ export PATH=~/bin:$PATH
```

### Globally
If you want to make this program available globally to your system, you will need root powers. You can place this program in several executable locations. An example would be:

```bash
$ sudo cp /pathTofile/text_bind.py /usr/local/bin/
```

## Windows and MacOSX
I believe the script should work on these systems, but I have no deeper knowledge to configure this script on them. Feel free to develop your solutions.

## USAGE
In the working directory replete of .txt files, all you need is:

```bash
$ text_bind
```

The range of supported commands are in the table:

| Arguments            | Description
|----------------------|----------------------------------------------
| -h, --help           | show this help message and exit
| --type TYPE          | file type: .txt and .csv is working good (default .txt)
| --label LABEL        | The output file name (default merged.fileExtension)
| --override OVERRIDE  | Remove existing file with same name as output file (default No)
|                      |

You can specify the file type

```bash
$ text_bind --type ".csv"
```

or the name of output file

```bash
$ text_bind --type ".csv" --label "myoutput.csv"
```

**OBS:**
If there is a file with the same name as the output file you chose, you must choose what to do.

1. You can manually rename the file, delete it or move it.

2. You can set the override option (This option permanently deletes the file in question.)

```bash
$ text_bind --type ".csv" --label "myoutput.csv" --override "Yes"
```

### Get help
```bash
$ text_bind -h
```


## DISCLAIMER
This software is not warranted of any kind. Use at your own risk.

