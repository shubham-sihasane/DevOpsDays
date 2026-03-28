
* Linux Shells *

- Bourn Shell (Sh)
- Korn Shell (ksh)
- Z Shell (zsh)
- Bourn Again Shell (Bash)

`<COMMAND> -<OPTION> <ARGUMENTS>`⌘ Standard template for linux commands

`echo $SHELL` ⌘ Print the shell type

`echo "${BASH_VERSION}"` ⌘ Print the bash version | `bash` to start bash shell

`echo '<message>'` ⌘ Print a message on the console | -n for no line break -e for escape sequence

`ls` ⌘ List files and folders | `ls -l` for long listing | `ls -a` for hidden files starting with . | `ls -r` for reverse order of sorting | `ls -t` for sort by modification time, newest first

- Absolute Path = They start with `/`, complete path to file, they work everywhere
- Relative Path = Are being resolved according to our current working directory

`cd <directory>` ⌘ Change the directory | `cd /` takes you to root directory | `cd ~` OR `cd` takes to home directory | `cd ..` takes to parent directory | `cd ../..` takes you to parent's parent directory 

`pwd` ⌘ Print present current working directory

`mkdir <directory>` ⌘ Create a directory

`mkdir -p <directory1>/<directory2>/<directory3>` ⌘ Create nested directories

`rm -r <directory>` ⌘ Remove all the contents of the directory

`cp -r <source-path> <destination-path>` ⌘ Copy directory from one source to destination

`touch <filename>` ⌘ Create an empty file

`cat > <filename>` ⌘ Type contents to the file `ctr + d` to terminate

`cat <filename>` ⌘ Display the contents of the file

`cp <file-source-path> <file-destnation-path>` ⌘ Copy a file source to destination path

`mv <source-path-file/directory> <destination-path/directory>` ⌘ Move file or directory from source to destination

`rm <filename>` ⌘ Remove or delete a file

`cd <directory>; mkdir <directory>; pwd` ⌘ Execute multiple commands separated by `;`

`clear` ⌘ Clear the output of all the previous commands from console 

`vi <filename>` ⌘ Open a file in VI editor [i = Insert Mode, Esc = Command Mode]

- x = Delete a character
- dd = Delete a line
- yy = Copy a line
- p = Paste a line
- :wq = command; save, quite

`find <pattern/word>` ⌘ Find word or pattern in opened file in VI editor, `n = next`

- `find <path> -type -f -name "app.log"` ⌘ Find file
- `find <path> -type -d -name "app.log"` ⌘ Find directory
- `find / -type f -size +50M` ⌘ Find all files with size greater than 50MB

`ss -tulpn` ⌘ Socket statistics, Check all ports opened on the system

`netstat -tuln` ⌘ Network statistics, active connections, ports, PID's, protocol stats,

`ip addr show` OR `ipconfig` ⌘ Show add details around IP

`whoami` ⌘ Find which user you are

`id <user>` ⌘ Identify the ID details of the user

`sudo su -` ⌘ Switch as a root user

`su <username>` ⌘ Switch as another user, /etc/sudoers

`ssh user@hostname` ⌘ SSH into server (hostname) as user

`sudo <command>` ⌘ Execute command as root user (Higher Privileges)

`curl <URL> -O` ⌘ Save the result in file else print output on screen

`wget <URL> -O <filename>` ⌘ Save the contents of the file in filename

`cat /etc/*release*` ⌘ Print operating system details on screen

`RPM - Red Hat Package Manager` # Red Hat / CentOS distribution

`rpm -i <package-name>` ⌘ Install a package

`rpm -e <package-name>` ⌘ Uninstall a package

`rpm -q <package-name>` ⌘ Query a package

`YUM =  Yellowdog Updater, Modified` # High level package manager built on top of RPM

`yum install <package-name>` ⌘ Install a package | `/etc/yum.repos.d` Repo information | `yum repolist`

`yum list <package-name>` ⌘ List package

`yum --showduplicates list <package-name>:<version>` ⌘ Show duplicate installed packages 

`yum remove <package-name>` ⌘ Remove a package from the system

`/etc/systemd/system` ⌘ System Services files location

`systemctl start <service-name>` ⌘ Start a service

`systemctl stop <service-name>` ⌘ Stop a service

`systemctl status <service-name>` ⌘ Status a service

`systemctl enable <service-name>` ⌘ Enable a service at system start

`systemctl disable <service-name>` ⌘ Disable a service at system start

`systemctl start <service-name>` ⌘ Start a service

`systemctl daemon-reload` ⌘ Reload a daemon service to take effect

`systemctl cat <>service-name.service` ⌘ Print systemd file

`ip link` ⌘ List and modify interfaces on host

`ip addr` ⌘ IP address assigned to those interfaces

`ip addr add <IP-address> dev eth0` ⌘ Attach IP address to ethernet

`route` ⌘ Display kernel IP route table

`ip route add <IP-address-of-another-network> via <IP-address-router>` ⌘ Add route to route table

`nc -zv <IP-Address> <Port>` ⌘ Check if specific port is open at address with netcat

`cat /etc/resolv.conf` ⌘ A hostsfile which is used as a local DNS mapping

`cat /etc/hosts` ⌘ Keeps the IP and name mapping

`cat /etc/nsswitch.conf` ⌘ Switch order for precedence on hosts file and DNS server

`nslookup <IP/hostname>` ⌘ A network utility used to test DNS resolution

`dig <IP/hostname>` ⌘ A network utility used to test DNS resolution as an alternative

`mtr <IP/hostname>` OR `traceroute` ⌘ My Traceroute for hostname

`tcpdump -i eth0 port <port> -c N` ⌘ Troubleshooting from source to target for specific port

`nmap <hostname>`

`date` ⌘ Prints system time (UTC)

`cal` ⌘ Prints current month calendar

`uptime` ⌘ System boot time since started last time

`free -h` ⌘ Check the available free memory, `-h` for human-readable `-m` for MB, `-w` for wide

`df -h` ⌘ Disk free, -h for human-readable format, `-T` for type of file type, `-i` for inode

`top` ⌘ CPU, memory utilization in the system, `htop` for better view for the same

`sar [options] [interval] [count]` ⌘ interval → seconds between samples. count → number of samples, options → specify what to measure (CPU, memory, I/O, etc.).

`<command> &` ⌘ Run a command, process in background

`ps -ef` ⌘ Lists the running process for current user, `-e` for all processes on the system not just logged-in user, `-f` for full format details, `-aux` for all users, cpu, memory, username, including x for processes not attached to terminal

`vmstat [options] [delay [count]]` ⌘ System performance, delay → Time interval (in seconds) between updates.  count → Number of updates to display.  options → Flags to customize output (e.g., -s for summary).

`iostat [options] [interval] [count]` ⌘ iostat (short for I/O statistics) is part of the `sysstat` package. interval → seconds between reports. count → number of reports to generate. options → customize output (e.g., -x for extended stats).

`journalctl -u <app-name-process>` ⌘ Query and display logs collected by systemd’s journal service

`whoami` ⌘ Prints current user logged in

`who` ⌘ Displays user information including IP

`finger` `user` `id` ⌘ Displays the user information

`man <command>` ⌘ Help for any command

`<command> -h` OR `<command> --help` ⌘ Print the help manual for command

`pwd` ⌘ Print current working directory

`ls` ⌘ List files and folders in directory

`ls -l` ⌘ Extended list of files and folders

`ls -a` ⌘ List hidden files

`ls -t` ⌘ List files based on timestamps

`ls -r` ⌘ List the files in reverse order

`cat <filename>` ⌘ List content of the file

`less <filename>` ⌘ View file page by page 

`more <filename>` ⌘ Output the contents of a file

`head -N <filename>` ⌘ Output the first N lines of a file

`tail -N <filename>` ⌘ Output the last N lines of a file

`touch <filename>` ⌘ Create an empty file

`cat > <filename>` ⌘ Opens for entering the file details with over writing a file

`cat >> <filename>` ⌘ Open for entering the file details without overwriting a file

`nano <filename>` OR `vi <filename>` ⌘ Opens a file 

`rm <filename>` ⌘ Remove a file, -f for forcefully

`mkdir <dir-name>` ⌘ Create a directory

`rmdir <dir-name>` ⌘ Remove an empty directory

`rm -rf <file-dir-name>` ⌘ Remove a directory and it's contents

`cd <path>` ⌘ Change directory with path

`cd ..` ⌘ Navigate to parent directory

`cp <source-path> <destination-path>` ⌘ Copy directory from source path to destination path, -r for directory

`mv <cource-path> <destination-path>` ⌘ Move file from source path to destination path, -r for directory

`tree` ⌘ Display tree structure for a directory and files

`find <path> -option <filename>` ⌘ Search for filename in path and options

`-name` For searching a file with its name | `-user` For files whose owner is a particular user | `-group` For files belonging to a particular group

`grep <pattern> <filename>` ⌘ Search for a pattern in a filename - Global Regular Expression

`more <filename>` ⌘ A pager utility used to view the contents of a text file one screen or "page" at a time

`less <filename>` ⌘ A pager utility used to view the contents of a text file one screen or "page" at a time

`sed` stands for stream editor, find and replace use case, no modification in original file

`sed "s/<old-text>/<new-text>/" <filename>` ⌘ Replace old with new specific pattern

`sed "s/<old-text>/<new-text>/g" <filename>` ⌘ Replace old with new globally 

`sed -i "s/<old-text>/<new-text>/" <filename>` ⌘ Replace old with new and update the file 

`sed "s/<old-text>/<new-text>/" <filename>` ⌘ 

`sed "s/<old-text>/<new-text>/" <filename>`

`useradd <options> <username>` ⌘ Create user in system with options like -u = user ID, -G = secondary user, -g = primary group ID, -d = home directory, -c = comment, -s = shell

`passwd <username>` ⌘ Create a password for the user

### User Management

In Linux, users can be categorized into three general categories:

- System Accounts
  - They are responsible for running background tasks on your system
  - They don't have home directory
- Regular User
  - They have access their own home directory and files
  - They can not perform admin tasks or access other users files and directories without permission
- Super User (Root)
  - They have unrestricted access to system
  - Can do pretty much everything, add/remove software
  - Can change the configuration of the system

*Elevating Privileges - sudo*
Temporarily elevate privileges by putting sudo in front of a command to become superuser.

### Package Management
- A centralized way to manage and install software packages is called package management.
- Linux system connects with centralized repositories to manage the software including install, remove various versions of same software.
- Package management is handled differently for different linux distributions.

*Package Management for Debian - Ubuntu*
-  apt or apt-get are the package managers for managing packages on debian based systems like ubuntu, needs sudo privileges | apt does install additional required dependencies as well whereas apt-get does not
- `apt update` ⌘ Refreshes the available list of packages, first thing to do on system before any other apt command
- `apt upgrade` ⌘ Upgrade the system packages, upgrades only existing packages including those package dependencies
- `apt full-upgrade` OR `apt dist-upgrade` ⌘ Upgrade the full system including installing and removing packages which may cause issues
- `apt install <package>` ⌘ Install a package 
- `apt remove <package>` ⌘ Uninstall a package
- `apt autoremove` ⌘ Removes packages that are no longer needed

*Package Management for RHEL - CentOS*
- dnf or yum are the package managers for managing packages on RHEL based systems like centos, amazon linux, needs sudo privileges | DNF is the modern successor to YUM, offering significant architectural and performance improvements.
- `dnf update` OR `dnf upgrade` ⌘ Fetches the latest version of packages and upgrades the system, dnf always keeps the local packages up to date, no need to manually refresh it like ubuntu. | crb-enable
- `dnf install <package>` ⌘ Install a package | package = epel-release - additional package for installing tools/utilities
- `dnf remove <package>` ⌘ Remove a package
- `yum install <package>` ⌘ Install a package
- `yum remove <package>` ⌘ Remove a package

### File Management in Linux

`touch <filename>` ⌘ Creates one or more empty files (separated by spaces), if it does exist else only timestamp get updated.

`mkdir <directory>` ⌘ Creates one or more empty directories (separated by spaces), if it does exist

`rmdir <directory>` ⌘ Remove an empty directory

`mv <source_path> <target_path>` ⌘ Move an existing file to another location, can also be used to renaming a file

`cp <source_path> <target_path>` ⌘ Copy a file to another location, `-r` for copying directory

`rm <filename>` ⌘ Remove one or more files separated by space, remove empty or non-empty directory with `-r`

`tree <path>` ⌘ Showcase & display directory structure, `.` for current working directory

`find [path] [options] [expression]` ⌘ Search files based on expression | `-type f` for file type, `-type d` for directory | `-mtime -7` modified in last 7 days | `-size +10M` for files larger than 10 MB | `-empty -delete` for deleting all empty file | combination of options | `man find` for options

`cat <filename>` ⌘ Prints the content of a file

`head -N <filename>` ⌘ Shows top 10 lines by default, `-N` for number of top N lines

`tail -N <filename>` ⌘ Shows bottom 10 lines by default, `-N` for number of bottom N lines

`less <filename>` | Display long file page by page, `f` for one page at a time

`wc <filename>` ⌘ Prints count of words of a file

`wc -lwc <filename>` ⌘ Prints out the number of lines, number of words, number of bytes in file

`du <file/directory>` ⌘ Calculate the size of all items in this folder, `-s` for summary

### Manage data streams

`>` = Redirection Operator = Redirect the output command into a file by creating it if it does not exist else the file will be overwritten. | `ls > <filename>` redirect output of ls command in filename, except errors if any

`>>` = Redirection Operator = Redirect the output command into a file by creating it if it does not exist else the file will be overwritten. | `echo <"message"> >> <filename>` redirect and append output of echo command in existing filename, except errors if any

`<` = Redirection Operator = Standard input from a file

*Stream Editors*
- stdin (0 = standard input keyboard)
- stdout (1 = standard output on screen)
- stderr (2 = standard error output on screen)

- `<command> > <output-file>` ⌘ Redirect output
- `<command> 1> <output-file>` ⌘ Redirect output
- `<command> 2> <error-file>` ⌘ Redirect errors only
- `<command> > <output-file> 2> <error-file>` ⌘ Redirect combination of output and error in two separate files
- `<command> 2> /dev/null` ⌘ Discard stderr
- `<command> 1> <output-file> 2> <output-file>` ⌘ Combine normal putput and error in same file | `<command> <output-file> 2>&1`  

- `cat file.txt 2>&1 > out.txt` ⌘ stderr will show up in terminal
- `cat file.txt > out.txt 2>&1` ⌘ stderr will be redirected to file

`echo $?` ⌘ Prints the success or error code like 0, 1, 127

*Pipe*
- A mechanism that passes the output of one command as input to another command which helps to chain multiple commands together and build more complex functionalities.
- `command | command .. | command`

*tee*
- In combination with a pipe and the tee command you can create a standard output and write it into a file at the same time.
- `echo 'Hello World!' | tee -a hello.txt`

*sort*
- Sort contents in a file or stdin
  - By default, alphabetical, `sort -r` for reverse, `sort -n` for numerical order, `sort -c` for checking contents in a file are sorted and find unsorted elements, `-u` for unique, `-d` for duplicate,  `sort -k <col-num>` for sorting data by a specific column
- `cat users.txt | sort -rud`

`grep`
 - Grep is a tool that can find a pattern in an output or a file
 - `grep -F 'pattern' <file>` ⌘ -F for disabling the regular expression
 - `<command> | grep -F 'pattern'`
 - By default, it uses basic regular expressions
 - Ex. `ip addr show | grep -F 'inet''`

*Working with strings*

- Replace on a character level using translate
  - `echo '<message>' | tr '<original>' '<replacement>'`
- Convert upper and lower case
  - `echo '<message>' | tr 'a-z' 'A-Z'`
- Delete characters
  - `echo '<message>' | tr -d ' '`
- Reverse a string
  - `echo '<message>' | rev`

`cut` ⌘ It allows us to process and extract data a file or standard input
- `<command> | cut -b 1-10` ⌘ Cut by bytes ex 1-10
- `<command> | cut -c 1-10` ⌘ Cut by characters ec 1-10
- `<command> | cut -d ' ' -f 2` ⌘ Cut by delimiters

`sed` ⌘ It allows us to easily execute commands on a file or on stdin
- `sed <command1>; <command2>; ...`
- s/[pattern]/[replacement]/[flags]:
- Replace a string with another, `-g` for all occurrence and not just first

Examples:
- `cat access.log | grep -F '.zip' | wc -l` 
- `grep -F '.zip' access.log | cut -d ' ' -f 7` # column 7
- `cat <log.file> | grep -i -A2 -B2 <keyword>` for 2 lines after and before keyword

`sed [options] <command> <filename>` ⌘ Search and replace text pattern, delete lines or specific text, insert/append new text, transform text using regular expression

- `sed 's/foo/bar/' file.txt` ⌘ Replace first occurrence of "foo" with "bar" per line
- `sed 's/foo/bar/g' file.txt`	⌘ Replace all occurrences of "foo" with "bar"
- `sed -i 's/foo/bar/g' file.txt`	⌘ Replace in place (edit file directly)
- `sed '/error/d' file.txt`	⌘ Delete lines containing "error"
- `sed -n '5,10p' file.txt`	⌘ Print only lines 5–10
- `sed '2i\New line here' file.txt`	⌘ Insert a line before line 2
- `sed 's/[0-9]/#/g' file.txt`	⌘ Replace all digits with #

`awk [pattern] <action> <filename>` ⌘ A text processing tool

- `awk '{print $1}' file.txt`	Print the first column of each line
- `awk '{print $1,$3}' file.txt`	Print first and third columns
- `awk '/error/ {print $0}' logfile.txt`	Print lines containing "error"
- `awk '{sum+=$2} END {print sum}'` data.txt	Sum values in column 2
- `awk -F, '{print $1,$2}' file.csv`	Use comma as delimiter, print first two fields
- `cat app.log | awk -F " " '{print $NF}' | sort | uniq -c | sort -rn` ⌘ sort, find unique, sort reverse

#### Shell
- A shell is an outer layer of the OS, takes commands from user and translates them into a form that the kernel can understand and display the results of those commands on console to end user.
- Everything that allows the outer world to access the OS, the GUI is always a shell.
- Shell only refers to the command line interface (CLI) of an operating system.
- CLI = A text based interface that allows users to interact with systems by typing commands (CLI, terminal, console)
- Linux shell allows us to work on devices that don't support GUI and more efficient to use CLI instead of the GUI.

*Environment Variables*
- Used to store configuration information and settings
- They influence the shell and program behaviour
- By convention Env variables are written in uppercase letters
- `env` lists all the environment variables
- Ex. `echo "${PWD}"`,  `echo "$PWD"`, `echo "${PATH}"`
- IMP = `HOME`, `PWD`, `SHELL`, `USER`


*Set/Unset Environment Variables*
- Set environment variable
  - `export VAR=value`
- Unset environment variable
  - unset VAR
- These are useful for troubleshooting and cleaning up of the environment

*PATH*
- `PATH` is one of the most important variables in our shell
- Stores a list of directories
- Directories searched for executable programs
- Left to right order
- Multiple directories separated by colons (":")

`which <command>` ⌘ Prints location of executable program of command

- Filesystem hierarchy standard: Unified standard of where to place files
- Single user mode: A special way to launch Linux for repairing a broken system
- `/bin` - Essential binaries that need to be always available
- `/sbin` - Essential binaries that usually executed as root and need to be always available
- `/usr/bin` - Non-essential for all users, could be shared with other computers
- `/usr/sbin` - Non-essential binaries, usually executed as root, could be shared with other computer
- `/usr/local/bin` - Non-essential binaries, for all users, specific to this host
- `/usr/local/sbin` - Non-essential binaries, usually executed as root, specific to this host

*Profile Configuration*
- ~/.bash_profile
- ~/.bash_login
- ~/.profile
- ~/.bashrc

- Bash can start in various startup modes:
  - Interactive login shell
  - Interactive non-login shell
  - Non-interactive non-login shell
  - Non-interactive login shell

*Alias*
 - Use as alias to shorten commands
 - `alias <alias>='cd ~'`
 - `unalias <alias>` by default, valid till the terminal session

*Set Shell*
 - Enable a feature `set -[feature]`
 - Disable a feature `set +[feature]`



#### File Management
File - A container for storing, accessing and or managing data with unique name combined with its path provides a unique location for each file in a filesystem

- Size = The amount of data stored in the file
- Permissions = Who can read, write or execute the file
- Ownership = Which user and group owns the file
- Timestamp = When the file was created, modified, accessed

*How data is stored*
filename -> Inode (stores metadata) -> Data on Disk
folder -> Inode (stores metadata) -> file/s

Everything in linux is considered as a file.
- Ordinary file (-)
- Directories (d)
- Symbolic Links (l)
- Character device (c)
- Block device (b)
- Named Pipes (p)
- Sockets (s)

*Symbolic Link*
A symlink is a special kind of file on Unix systems.
- It serves as a reference to another file or directory
- A special way of shortcut to another destination

- We create a special file that contains a reference to the destination path
- This reference is being resolved on access of the symlink
- This affects read and write operations

`ls -s <target> <link>` ⌘ Create a link for taget

- `ls -s desktop desk` desk link for desktop
- `ls -s file.zip file` # file link for file.xip

*Hard Link*
- a directory entry or reference to an existing inode, technically the first filename of a file is already a hardlink but one file can have multiple hardlinks, can not be created to directories to avoid looping
Multiple files -> Inode (Stores metadata) -> Data on Disk
`ls <target> <link>`
- `cp -al source dest` # Copy the while source folder, and create hrd links for all files

`df -ih` ⌘ Human readable format inode usage

*Buffered vs Unbuffered Input/Output*
- Unbuffered: Directly handles data between the IO device and the program
  - Real-time data and control
- Buffered: 
  - Utilizes a temporary storage area to hold before it's being received / sent to the IO device

*/proc files* Inspect system 
- `/proc/cpuinfo` ⌘ Get CPU related info from system
- `/proc/meminfo` ⌘ Get memory related info from system
- `/proc/version` ⌘ Kernel information
- `/proc/uptime` ⌘ System uptime since started
- `/proc/loadavg` ⌘ Average CPU load on system

`Devices`
- Everything is a file, everything is a stream of bytes.
- Devices refers to a physical or virtual entity that can be accessed through a file life interface
- Devices in unix serve as the interface between the OS system and various hardware or virtual components

- Character Device
  - We gain unbuffered, direct access to the hardware
  - Usually, we can access those devices by reading a byte
- Block Device
  - We gain buffered access to the hardware
  - Multiple bytes are bundled into a block
- Pseudo Device
  - Those are devices that don't necessarily refer to a physical device

*Filesystem Hierarchy*
It defines the directory structure and directory contents in unix like operating systems
It provides a consistent and predictable location for specific types of files and directories
- Ensures compatibility across different distributions
- Makes it easier for users, administrators, and developers to locate files

- `/:` ⌘ Root directory
- `/bin` ⌘ Essential binaries
- `/usr/bin` ⌘ User specific binaries
- `/boot` ⌘ Contains files for bootloader
- `/dev` ⌘ Contains device files that represents hardware and software devices
- `/etc` ⌘ Contains system-wide config files
- `media` ⌘ Contains mount points for removable storage media
- `/mnt` ⌘ Mount points for additional filesystem
- `/opt` ⌘ Optional software application packages
- `/proc` ⌘ Virtual filesystem info about processes and kernel
- `/root` ⌘ Contains personal data for root user
- `/run` ⌘ Run time data, file here will be removed during boot or will be discarded on shutdown, 'systemd'
- `/sbin` ⌘ Contains essential system binaries that are generally used by the root user
- `/src` ⌘ Files for services
- `/sys` ⌘ Info about devices, drivers, kernel features
- `/tmp` ⌘ Contains temporary files, usually deleted after reboot
- `/usr` ⌘ Contains shareable data with multiple computers, read only data, 
- `/usr/local` ⌘ Contains user data which should be shared between multiple computer
- `/var` ⌘ Contains variable data files such as logs, databases, websites, this directory contains changes as the system runs


#### User Management
1. Root User
- Highest privileges
- It has the user ID `0`
- There can be only one root user on the system
2. Regular User
- Limited privileges
- Can be temporarily get root access through sudo
3. System user
- For specific tasks
- This allows us to safely run webserver, database etc

Groups
- All users have a primary groups
- And can be assigned to zero to unlimited additional groups

Managing Users
- `/etc/passwd` ⌘ Contains basic info, username, user ID, group ID, user description, home directory, default shell, readable by all users
- `/etc/shadow` ⌘ Stores encrypted user passwords and password aging info, Also stores additional info such date of last pass change, expiry dates, Readable only by the root users
- `/etc/group` ⌘ Contains info about the groups, and their members

*useradd*
- `useradd [options] [username]`
  - `-m` ⌘ for home directory
  - `-d` ⌘ set custom home directory
  - `-s` ⌘ specify default shell
  - `-g` ⌘ specify primary group instead of using default configuration
  - `-G` ⌘ Add user to secondary group

*passwd*
- `passwd [options] [username]`
  - `-S` ⌘ Display password status
  - `-d` ⌘ Delete password
  - `-n` ⌘ Set minimum password age (days)
  - `-x` ⌘ Set maximum password age (days)
  - `-l` ⌘ Lock user account
  - `-u` ⌘ Unlock user account

`sudo -u [user] -g [group] <task/program>` ⌘ Start program as different user Ex. `sudo -u shubham bash`

*/etc/sudoers*
- `[user] ALL:(ALL:ALL) ALL` (username), (hostname), (Run config - user:group), (command)
- `NOPASSWD` : To allow sudo without a password (security risk)

*usermod*
 - With usermod command, we can modify another users details
 - `usermod [options] username`
 - `-c` ⌘ Change user description
 - `-s` ⌘ Change default shell
 - `-d` ⌘ Change home directory
 - `-l` ⌘ Change username
 - `-g` ⌘ Change primary group
 - `-G` ⌘ Change secondary group
 - `-aG` ⌘ Add secondary group
 - Ex `sudo docker -aG <user>` ⌘ Add user in docker group

`groupmod -n <group-name <new-group-name>`

`cat /etc/shells` ⌘ Lists shells in the system
- If user wants to change their default shell, it must be on of /etc/shells
- `chsh -s /bin/bash` ⌘ Change shell to bash

`userdel`
- We can delete an existing user
- `userdel [options] [username]`
- `-r` ⌘ Removes the home directory
- `-f` ⌘ Also removes home directory, forces the removal of the user, even if the user is still logged in
- Might also delete a group with same name as this user

* Switch User - su*
- su stands for switch user - `su [other user]`
- Provide password and will be logged in as other user

*Best Practices*
- Prefer groups to manage privileges
- Useful meaningful group names
- Assigning users only the necessary permissions and group membership required
- Avoiding the use of overly permissive access rights
- Don't give write access to everybody
- Minimizing the number of users with elevated privileges
- Keep group memberships up-to-date
- Regularly review group membership


#### Processes and Signals
- A process is an instance of a program
- Independent execution unit with its own resources
  - CPU and Memory resource
  - Opened files, network connections etc
- It is managed by kernel
- Each process has a process ID (PID), a user under which a process runs under, a state
- All processes are organized in a hierarchy


