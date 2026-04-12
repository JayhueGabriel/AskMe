import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int
import mss
import anthropic
import os

# Create initial environment
ctk.set_appearance_mode("dark")
root = ctk.CTk()
responseTab = ctk.CTkToplevel(root)
responseTab.withdraw()
# Sizing + positioning
searchWidth = 600
searchHeight = 50
responseWidth = 600
responseHeight = 400
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = int(screen_w / 2)
y = int(screen_h / 2)
# API call
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def lookUp():
    # Grab screenshot
    root.withdraw()
    responseTab.withdraw()
    with mss.mss() as sct:
        sct.shot()

    query = searchBar.get()

    message = client.messages.create( 
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[{"role": 'user', "content": query}]
    )
    response = message.content[0].text 
    # Set textbox
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("end", response)
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
responseTab.wm_attributes('-topmost', True)
textbox = ctk.CTkTextbox(responseTab, width=responseWidth, height=responseHeight, font=('Arial', 14))
textbox.pack()

root.bind("<Escape>", lambda e: root.destroy())
root.bind("<Return>", lambda e: lookUp() )

searchBar = ctk.CTkEntry(root, width=searchWidth, font=("Arial", 25), placeholder_text="Hmm...", border_width=0, fg_color= "#212121")
searchBar.pack(pady=10)

root.mainloop()