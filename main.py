import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int
import mss

ctk.set_appearance_mode("dark")
root = ctk.CTk()
responseTab = ctk.CTkToplevel()
responseTab.withdraw()

searchWidth = 600
searchHeight = 50
responseWidth = 600
responseHeight = 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = int(screen_w / 2)
y = int(screen_h / 2)

def setUpWindow():
    root.geometry(f"{searchWidth}x{searchHeight}+{x}+{y}")
    # Apply rounded corners via Windows API
    HWND = windll.user32.GetForegroundWindow()
    windll.dwmapi.DwmSetWindowAttribute(HWND, 33, byref(c_int(2)), sizeof(c_int))
    root.overrideredirect(True)
    root.wm_attributes('-topmost', True)

def lookUp():
    root.withdraw()
    with mss.mss() as sct:
        sct.shot()
    print(searchBar.get())
    searchBar.delete(0, "end")
    setUpResponseWindow()
    root.deiconify()  

def setUpResponseWindow():
    responseTab.geometry(f"{responseWidth}x{responseHeight}+{x}+{y + 200}")
    responseTab.overrideredirect(True)
    responseTab.deiconify()


root.bind("<Escape>", lambda e: root.destroy())
root.bind("<Return>", lambda e: lookUp() )

searchBar = ctk.CTkEntry(root, width=searchWidth, font=("Arial", 25), placeholder_text="Hmm...", border_width=0, fg_color= "#212121")
searchBar.pack(pady=10)



setUpWindow()
root.mainloop()
responseTab.mainloop()