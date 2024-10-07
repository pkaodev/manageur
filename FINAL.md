# Manageur

Manageur is a personal tool to manage all my computers in a unified way. It sets standard commands, configurations, and tools across all my computers. It is a collection of scripts that can be run on any computer to set it up to my liking. It is intended to be run on a fresh install of an OS, but can be run on any computer to set it up to my liking. The intended way to set it up is by running a curl command and then execute a script which is hosted on a public website (my_website.com/scripts/script1). this then checks the os, and curl/runs the correct script from my github (which will host the repo where i update the script). this then checks if manageur is installed, if not it will install it. if it is installed it will start it. manageur will then check the state of the computer and run the relevant scripts to set it up to my liking. manageur will also have a command line interface, pyqt app, web app etc.

the code will be written in mainly python (using core libraries as much possible), with some parts in bash.

## File structure
Everything related to Manageur sits in the directory `_manageur`, located in:
- Linux: `~/_manageur/`
- Mac: `~/_manageur/`
- Windows: 




1. `curl <initial script on main website> | bash`
2. initial script checks OS and curl/run relevant script from public repo
3. initial script will curl/run relevant script from public repo
4. that script will check if manageur exists
5a. if yes it will start manageur
5b. if no it curl/run manageur install script

install script (same as start up?) will:
- check state of manageur then:

Notes:



Utils:
- curl_and_run
- M class - read, write, append, delete..... (for now with files (csv, json...), but is abstracted to be general and could be db, cache.....)
- 