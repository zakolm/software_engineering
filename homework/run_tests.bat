@echo off
cls
for %%i in (1 2 3) do call test.bat %%i
del f_inp.txt
del f_out.txt
pause