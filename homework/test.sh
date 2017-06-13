#!/bin/bash
for i in 1 2 3
do
	cat in_$i.txt > file_in.txt
	python3 main.py
	if cmp in_$i.txt file_in.txt
		then echo OK
		else echo FAIL
	fi
done
