del /Q build
del /Q dist
del SerialPortTool.exe
pyinstaller -F -w -i ico.ico main.py
copy dist\main.exe main.exe
ren main.exe SerialPortTool.exe