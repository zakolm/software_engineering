@ECHO OFF 
cd c:\source
REM Это расположение файлов, которые вы хотите отсортировать
FOR %%f IN (*.doc *.txt) DO XCOPY c:\source\"%%f" c:\text /m /y
REM Эта команда перемещает файлы с расширением .doc или 
REM .txt из папки c:\source в папку c:\text
REM %%f это переменная
FOR %%f IN (*.jpg *.png *.bmp) DO XCOPY C:\source\"%%f" c:\images /m /y
REM Эта команда перемещает файлы с расширением .jpg, .png, 
REM или .bmp из папки c:\source в папку c:\images
pause