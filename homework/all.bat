@echo off
REM f_out.txt == OUT_%1.TXT ?
del f_inp.txt
copy in_%1.txt f_inp.txt
main.py
fc f_out.txt out_%1.txt
pause