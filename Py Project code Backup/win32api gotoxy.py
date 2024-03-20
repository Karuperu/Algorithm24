import win32api
from ctypes import Structure, c_short, windll, POINTER

def gotoxy(x,y):
    class COORD(Structure):
            _fields_=[("X",c_short),("Y",c_short)]
    windll.kernel32.SetConsoleCursorPosition(win32api.GetStdHandle(win32api.STD_OUTPUT_HANDLE), (COORD(x,y)))

gotoxy(1,10)
print('move~')