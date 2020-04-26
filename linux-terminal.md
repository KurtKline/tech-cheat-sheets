`cd /` go to root directory  
`cd` or `cd ~` go to home directory  
`ls -a` list all files, including hidden files and directories  
`ls -l` show files and permissions of files in current directory
`tree` shows tree view of filesystem  
`tree -d` shows just directories  
`less` view larger files in a paging manner. Use `/` to search for a pattern forwards, and `?` backwards  
`rm -rf` remove a directory and all of its contents  
`rmdir` remove an empty directory  
`rm -f` forcefully remove a file  
`rm -i` interactively remove a file  
`mv` rename and/or move a file  
`find -name "*.swp" -exec rm {} ’;’` finds files ending in .swp, and removing them  
`find -name "*.swp" -ok rm {} ’;’` finds files ending in .swp, and asks user to confirm removal  
`find -size +10M` finds files larger than 10MB  
`top, uptime, htop` to see CPU load averages  
`ps` lists currently running processes  
`pstree` displays processes in tree diagram  
`df -Th` displays information about mounted filesystems, and currently used and available space  
`diff3 MY-FILE COMMON-FILE YOUR-FILE` compares 3 files, using one common file as reference  
`file *` shows files and directories, and types of files  
`rsync sourcefile destinationfile` syncs file or entire directory from source to destination   
`echo line one > myfile.txt` writes "line one" to a file  
`echo line two >> myfile.txt` writes "line two" to the existing myfile.txt  
`cat << EOF > myfile.txt` creates file myfile.txt, and will prompt user to enter lines of file until EOF is entered  
`vimtutor` to access vim tutorial  
`whoami` current user  
`who` currently logged-on users  
`set`, `env`, or `export` to see environment variables  
`echo $USER` show the value of a specific environment variable  
`export VARIABLE=value` set a new environment variable (temporarily)  
Edit `~/.bashrc` and add line `export VARIABLE=value`; type `source ~/.bashrc` reads and executes new commands  
`export PATH=$HOME/bin:$PATH` prefix a private bin directory to your path  
`history` show recently used terminal commands 
    `CTRL-R` to search previously used commands  
    `!!` execute last command
    `!n` refer to the nth command line shown in history  
`cat > <filename>` interactively insert lines into new file until `CTRL-D` is pressed  
`cat > <filename> << EOF` interactively insert lines into new file until `EOF` is entered  
`sed` used to find and replace values within files  
`awk` extract and print specific contents of a file  

