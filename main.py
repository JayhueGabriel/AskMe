import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int
import mss

ctk.set_appearance_mode("dark")
root = ctk.CTk()
responseTab = ctk.CTkToplevel(root)
responseTab.withdraw()

searchWidth = 600
searchHeight = 50
responseWidth = 600
responseHeight = 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = int(screen_w / 2)
y = int(screen_h / 2)

def lookUp():
    # Grab screenshot
    root.withdraw()
    responseTab.withdraw()
    with mss.mss() as sct:
        sct.shot()

    # Set textbox
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("end", searchBar.get())
    textbox.see("1.0")
    textbox.configure(state="disabled")

    # Clear search and appear
    searchBar.delete(0, "end")
    root.deiconify()  
    responseTab.deiconify()


#Create window size + poistion
root.geometry(f"{searchWidth}x{searchHeight}+{x}+{y}")
responseTab.geometry(f"{responseWidth}x{responseHeight}+{x}+{y + 200}")
# Remove title & force to front
root.overrideredirect(True)
responseTab.overrideredirect(True)
root.wm_attributes('-topmost', True)

textbox = ctk.CTkTextbox(responseTab, width=responseWidth, height=responseHeight, font=('Arial', 14))
textbox.pack()

root.bind("<Escape>", lambda e: root.destroy())
root.bind("<Return>", lambda e: lookUp() )

searchBar = ctk.CTkEntry(root, width=searchWidth, font=("Arial", 25), placeholder_text="Hmm...", border_width=0, fg_color= "#212121")
searchBar.pack(pady=10)

root.mainloop()