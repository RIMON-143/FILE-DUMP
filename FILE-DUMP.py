#!/data/data/com.termux/files/usr/bin/python
import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import FILECREAT.py
 
