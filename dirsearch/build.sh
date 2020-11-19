#!/bin/sh

wget https://raw.githubusercontent.com/maurosoria/dirsearch/master/db/dicc.txt -O dirsearch.txt
cp dirsearch.txt full.txt
cat manual.txt >> full.txt
cat years/years.txt >> full.txt
