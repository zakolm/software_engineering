@ECHO OFF 
cd c:\source
REM ��� ������������ ������, ������� �� ������ �������������
FOR %%f IN (*.doc *.txt) DO XCOPY c:\source\"%%f" c:\text /m /y
REM ��� ������� ���������� ����� � ����������� .doc ��� 
REM .txt �� ����� c:\source � ����� c:\text
REM %%f ��� ����������
FOR %%f IN (*.jpg *.png *.bmp) DO XCOPY C:\source\"%%f" c:\images /m /y
REM ��� ������� ���������� ����� � ����������� .jpg, .png, 
REM ��� .bmp �� ����� c:\source � ����� c:\images
pause