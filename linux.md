
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

`find <pattern/word>` ⌘ Find word or pattern in opened file in VI editor, `n = next'

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

`cat /etc/resolv.conf` ⌘ A hostsfile which is used as a local DNS mapping

`cat /etc/hosts` ⌘ Keeps the IP and name mapping

`cat /etc/nsswitch.conf` ⌘ Switch order for precedence on hosts file and DNS server

`nslookup <IP/hostname>` ⌘ A network utility used to test DNS resolution

`dig <IP/hostname>` ⌘ A network utility used to test DNS resolution as an alternative

`date` ⌘ Prints system time (UTC)

`cal` ⌘ Prints current month calendar

`uptime` ⌘ System boot time

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

`rm <filename>` ⌘ Remove one or more files separated by space, remove a empty or non-empty directory with `-r`

`tree <path>` ⌘ Showcase & display directory structure, `.` for current working directory

`find [path] [options] [expression]` ⌘ Search files based on expression | `-type f` for file type, `-type d` for directory | `-mtime -7` modified in last 7 days | `-size +10M` for files larger than 10 MB | `-empty -delete` for deleting all empty file | combination of options | `man find` for options

`cat <filename>` ⌘ Prints the content of a file

`head -N <filename>` ⌘ Shows top 10 lines by default, `-N` for number of top N lines

`tail -N <filename>` ⌘ Shows bottom 10 lines by default, `-N` for number of bottom N lines

`less <filename>` | Display long file page by page, `f` for one page at a time

`wc <filename>` ⌘ Prints count of words of a file

`wc -lwc <filename>` ⌘ Prints out the number of lines, number of words, number of bytes in file














