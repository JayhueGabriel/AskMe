import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int
from config import *

def setup_root(root, x, y):
    root.geometry(f"{SEARCHBAR_WIDTH}x{SEARCHBAR_HEIGHT}+{x}+{y}")
    root.overrideredirect(True)
    root.wm_attributes('-topmost', True)
    HWND = windll.user32.GetForegroundWindow()
    windll.dwmapi.DwmSetWindowAttribute(HWND, 33, byref(c_int(2)), sizeof(c_int))

def setup_response_tab(responseTab, x, y):
    responseTab.geometry(f"{RESPONSE_WIDTH}x{RESPONSE_HEIGHT}+{x}+{y + 200}")
    responseTab.overrideredirect(True)
    responseTab.wm_attributes('-topmost', True)

