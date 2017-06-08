#echo "Hello"
#f_inp.txt = in_1.txt
#./main.py
#cp in_i f_inp
for ((i = 1; i <= 3; i++)) 
do
	#echo "HI"
	if cmp f_out.txt out_i.txt
		then echo "Файлы a и b идентичны."
		else echo "Файлы a и b имеют различия."
	fi
done
