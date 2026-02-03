
* Linux Shells *

- Bourn Shell (Sh)
- Korn Shell (ksh)
- Z Shell (zsh)
- Bourn Again Shell (Bash)

`echo $SHELL` ⌘ Print the shell type

`echo <message>` ⌘ Print a message on the console

`ls` ⌘ List files and folders

`cd <directory>` ⌘ Change the directory

`pwd` ⌘ Print current working directory

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

`su <username>` ⌘ Switch as another user

`ssh user@hostname` ⌘ SSH into server (hostname) as user

`sudo <command>` ⌘ Execute command as root user

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

`route` ⌘ Display route table

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

``












