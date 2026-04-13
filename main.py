import customtkinter as ctk
import mss
import threading
from pynput import keyboard
from config import *
from windows import *
from api import ask

ctk.set_appearance_mode("dark")
root = ctk.CTk()
responseTab = ctk.CTkToplevel(root)
responseTab.withdraw()
root.withdraw()

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = int(screen_w / 2)
y = int(screen_h / 2)

setup_root(root, x, y)
setup_response_tab(responseTab, x, y + 50)

def onActivate():
    root.deiconify()
    searchBar.focus()
    
def on_escape():
    root.withdraw()
    responseTab.withdraw()

def startListening():
    with keyboard.GlobalHotKeys({"<ctrl>+<space>": onActivate}) as h:
        h.join()

def take_screenshot():
    with mss.mss() as sct:
        sct.shot()

def print_response(response):
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("end", response)
    textbox.see("1.0")
    textbox.configure(state="disabled")

def look_up():
    root.withdraw()
    responseTab.withdraw()

    take_screenshot()
    response = ask(searchBar.get())
    print_response(response)

    responseTab.deiconify()
    root.deiconify()


textbox = ctk.CTkTextbox(responseTab, width=RESPONSE_WIDTH, height=RESPONSE_HEIGHT, font=('Arial', 14))
textbox.pack()

root.bind("<Return>", lambda e: look_up())
root.bind("<Escape>", lambda e: on_escape())
searchBar = ctk.CTkEntry(root, width=SEARCHBAR_WIDTH, font=("Arial", 25), placeholder_text="Hmm...", border_width=0, fg_color="#212121")
searchBar.pack(pady=10)

thread = threading.Thread(target=startListening, daemon=True)
thread.start()

root.mainloop()