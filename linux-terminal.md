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
