# 0x00. AirBnB clone - The console

+ By: Guillaume
+ Weight: 5
 
This project is all about  creating a clone of AirBnB website.
The goal of the project is to deploy on my server a simple copy of the AirBnB website.

A Command interpreter refers to a command line interpreter or a shell where user communicates with a computer Operating system and executes various commands.

### STARTING A COMMAND INTERPRETER on windows
The default command interpreter is the "Command Prompt" or ""Windows Power Shell".  You can search for "Command Prompt" or "PowerShell" in the Start menu to open the respective interpreter. There are other command interpreter i.e "Ubuntu"

### USING THE COMMAND INTERPRETER:

* Entering Commands: After opening the command interpreter, you'll see a prompt (e.g., $ for Unix-like systems, C:\> for Command Prompt, PS> for PowerShell). This prompt indicates that the interpreter is ready to accept commands. Simply type your command after the prompt and press Enter.

* Navigating Directories: You can use commands like cd to navigate through directories. For example, cd Documents will move you into the "Documents" directory.

* Listing Files and Directories: You can use commands like ls (Unix-like) or dir (Windows) to list the contents of a directory.

* Running Programs: You can run programs by typing their name and pressing Enter. For example, notepad will open the Notepad application.

* Passing Arguments: Many commands accept additional arguments to modify their behavior. For example, ls -l (Unix-like) or dir /w (Windows) provides detailed listings.

* Piping and Redirection: You can use the | symbol to pipe the output of one command into another command. You can also use > or < to redirect input or output to/from files.
### HOW TO USE THE COMMAND LINE INTERPRETER:
Listing Files:
Unix-like: ls
Windows: dir

Changing Directory:
Unix-like: cd Documents
Windows: cd Documents

Creating a Directory:
Unix-like: mkdir NewFolder
Windows: mkdir NewFolder

Copying Files:
Unix-like: cp file.txt new_location/
Windows: copy file.txt new_location\

Running a Program:
Unix-like: firefox (opens the Firefox browser if installed)
Windows: notepad (opens Notepad)

### Resources
***Read or watch:***
* cmd module
* cmd module in depth
* uuid module
* unittest module

### Requirements
* Allowed editors: vi, vim, emacs
+ All your files will be interpreted/compiled on Ubuntu 20.04 LTS using py
  thon3 (version 3.8.5)
+ All your files must be executable
+ Your code should use the pycodestyle (version 2.8.*)
+ The length of your files will be tested using wc

### Execution
***shell in interactive mode:***
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

***shell non-interactive mode: (like the Shell project in C)***
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
