python ../../builder.py for_build.yml vectors builded.txt
cat generic.txt > all.txt
cat builded.txt >> all.txt
echo >> all.txt
cat all.txt | sed 's/ /\/**\//g' >> all.txt