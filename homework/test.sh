#!/bin/bash
for i in {1..3}
do
	if [ ! -f in_$i.txt ]
		then echo Файла in_$i.txt не существует
		else cat in_$i.txt > f_in.txt
	fi
	python3 main.py
	diff -s -q -w f_out.txt out_$i.txt
done
