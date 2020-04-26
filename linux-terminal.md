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
