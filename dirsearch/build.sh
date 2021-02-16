#!/bin/sh

echo 'Downloading dirsearch wordlist'
wget https://raw.githubusercontent.com/maurosoria/dirsearch/master/db/dicc.txt -O dirsearch.txt
echo 'Creating full.txt'
cp dirsearch.txt full.txt
cat manual.txt >> full.txt
cat years/years.txt >> full.txt

echo 'Creating merged wordlists'
cp full.txt medium_wordlist.txt
cat ~/wd/raft-medium-files.txt >> medium_wordlist.txt
cat ~/wd/raft-medium-directories.txt >> medium_wordlist.txt

cp full.txt large_wordlist.txt
cat ~/wd/raft-large-files.txt >> large_wordlist.txt
cat ~/wd/raft-large-directories.txt >> large_wordlist.txt

echo 'Removing duplicates'
python remove_duplicate.py medium_wordlist.txt medium_wordlist_no_dups.txt
python remove_duplicate.py large_wordlist.txt large_wordlist_no_dups.txt

mv medium_wordlist_no_dups.txt medium_wordlist.txt
mv large_wordlist_no_dups.txt large_wordlist.txt