import os
from pathlib import Path
from tkinter import Tk, PhotoImage
from login import loginWindow
from launcher import LauncherApp
from tkinter import messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


root = Tk()

cl = loginWindow('title',root)

# if cl.login:
#     print('hello')
                

root.withdraw()
root.mainloop()
