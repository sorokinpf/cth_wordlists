rm -f keyboard_patterns_*.txt

python keyboard_patterns.py 1 2 > keyboard_patterns_2.txt
python keyboard_patterns.py 2 2 >> keyboard_patterns_2.txt

python keyboard_patterns.py 1 3 > keyboard_patterns_3.txt
python keyboard_patterns.py 2 3 >> keyboard_patterns_3.txt

cp keyboard_patterns_2.txt keyboard_patterns_2-3.txt
cat keyboard_patterns_3.txt >> keyboard_patterns_2-3.txt
