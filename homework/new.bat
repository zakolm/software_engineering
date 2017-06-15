@echo off
rem Формируем файл с описанием команды, 
rem имя которой передано параметром
del f_inp.txt
copy in_%1.txt f_inp.txt
main.py
fc f_out.txt out_%1.txt