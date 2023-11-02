import tkinter
import os
from tkinter import *
from pathlib import Path
from frames import ScreenFrames
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Toplevel

from ctypes import windll

#import tkinter as tk
# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class LauncherApp(Toplevel):
        def __init__(self, *args, **kwargs):
                Toplevel.__init__(self, *args, **kwargs)
                #self.window = Tk()
                
                self.title("Main")
                self.geometry("1920x1080")
                self.maxsize(1920,1080)
                self.minsize(1920,1080)

                self.overrideredirect(True)

                self.minimized = False # only to know if window is minimized
                self.maximized = False # only to know if window is maximized

                #self.iconbitmap(os.path.join('assets','Umlaut-Part-of-Accenture-logo_White.ico'))

                self.configure(bg = "#FFFFFF")
                self.can = None
                self.bind("<Configure>",self.resize_manager)


                self.canvas = Canvas(
                        self,
                        bg = "#FFFFFF",
                        height = 1080,
                        width = 1920,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")

                self.canvas.place(x=0,y=0, relx= 0,rely=0,anchor=NW)
                
                self.canvas_width = self.canvas.winfo_reqwidth()
                self.canvas_height = self.canvas.winfo_reqheight()
                #print(self.canvas_width)
                #print(self.canvas_height)
                
                

                self.frames= ScreenFrames(self.canvas)
                home_frame = self.frames.home_frame()
                self.show_frame(home_frame)
                self.active_frame = 'home'
                
                self.titlebar = Label(self.canvas, bg= "#03000F")
                self.titlebar.place(x=0,y=0,width=1920,height=28)

                self.titlebar.bind('<Button-1>', self.get_pos)
                

                self.bind("<FocusIn>",self.deminimize)
                self.after(10, lambda: self.set_appwindow(self)) # to see the icon on the task bar

                # Reading the frames original width and height in the begining 
                
                # self.frame_home_width = self.frames.home_fr.winfo_reqwidth()
                # self.frame_home_height = self.frames.home_fr.winfo_reqheight()

                # self.frame_news_width = self.frames.news_fr.winfo_reqwidth()
                # self.frame_news_height = self.frames.news_fr.winfo_reqheight()

                # self.frame_portf_width = self.frames.portf_fr.winfo_reqwidth()
                # self.frame_portf_height = self.frames.portf_fr.winfo_reqheight()
                

                #self.container = Frame(self.canvas)
                #self.Home_page = Home(parent=container)
                #self.News_page = News(parent=container)
                #self.Portf_page = Portfolio(parent=container)


                #self.News_page = Frame(self.canvas, bg='#131116', width=1452, height=426)
                #self.Portf_page = Frame(self.canvas, bg='#131116', width=1452, height=426)
                #self.show_frame(Home(parent=self.container))

                #region Custom TitleBar components
                self.logocanvas = Canvas(self.titlebar,
                        height=32, 
                        width=32,
                        bd = 0,
                        highlightthickness = 0,bg="#03000F",
                        relief = "ridge")
                self.logocanvas.place(x=0, y=0)


                self.image_titlebar_logo = PhotoImage(file=os.path.join('assets',"titlebar_logo.png"))
                self.titlebar_logo = self.logocanvas.create_image(
                        17.0,
                        14.0,
                        image=self.image_titlebar_logo)

                self.button_image_minimize = PhotoImage(file=os.path.join('assets',"button_minimize.png"))
                self.button_minimize = Button(self.titlebar,
                        image=self.button_image_minimize,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        highlightthickness=0,
                        command=self.minimize_me,
                        relief="flat")

                self.button_minimize.place(
                        x=1822.0,
                        y=0.0,
                        width=28.0,
                        height=28.0)

                self.button_image_maximize = PhotoImage(file=os.path.join('assets',"button_maximize.png"))

                self.button_maximize = Button(self.titlebar,
                        image=self.button_image_maximize,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        highlightthickness=0,
                        command=self.maximize_me,
                        relief="flat")
                
                self.button_maximize.place(
                        x=1857.0,
                        y=0.0,
                        width=28.0,
                        height=28.0)

                self.button_image_quit = PhotoImage(file=os.path.join('assets',"button_quit.png"))

                self.button_quit = Button(self.titlebar,
                        image=self.button_image_quit,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        highlightthickness=0,
                        command=lambda: print("button_quit clicked"),
                        relief="flat")

                self.button_quit.place(
                        x=1882.0,
                        y=0.0,
                        width=37.0,
                        height=28.0)
                self.button_quit.bind("<Button-1>", self.quit_window)
                self.bind("<FocusIn>",self.deminimize)
                self.after(10, lambda: self.set_appwindow(self)) # to see the icon on the task bar
                #endregion

                #-------------------------------------Main_window GUI--------------------------------------------
                #region Main_window GUI
                # The main window with black background
                self.canvas.create_rectangle(
                        0.0,
                        0.0,
                        1920.0,
                        1080.0,
                        fill="#03000F",
                        outline="")

                # The side bar rectangle with grey background
                self.canvas.create_rectangle(
                        0.0,
                        0.0,
                        300.0,
                        1080.0,
                        fill="#03000F",
                        outline="")

                # The main Umlaut symbol on top left side bar
                self.image_image_1 = PhotoImage(file=os.path.join('assets',"umlaut_logo_new.png"))
                self.image_1 = self.canvas.create_image(
                        165.0,
                        51.0,
                        image=self.image_image_1)

                # image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
                # image_10 = canvas.create_image(
                #         257.330078125,
                #         51.0,
                #         image=image_image_10)        
                        
                # The Top bar (Tab bar with Home, news etc.) rectangle with grey background
                self.canvas.create_rectangle(
                        438.0,
                        0.0,
                        1919.0,
                        108.0,
                        fill="#03000F",
                        outline="")

                #endregion
                
                #-------------------------------------Side_bar buttons defination GUI--------------------------------------------

                #region Categories Panel within Side_bar

                # Categories Text
                self.canvas.create_text(
                        22.0,
                        155.0,
                        anchor="nw",
                        text="CATEGORIES",
                        fill="#C7C7C7",
                        font=("Graphik Regular", 12 * -1))        

                # Profile Button definition on the left side bar
                self.button_image_sb_profile = PhotoImage(file=os.path.join('assets',"profile_new.png"))
        
                self.button_sb_profile = Button(self,
                        image=self.button_image_sb_profile,
                        #text="Profile",
                        borderwidth=0,
                        anchor= W,
                        bg="#03000F",
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_sb_profile clicked"),
                        relief="flat")

                self.button_sb_profile.place(
                        x=75.0,
                        y=170.0,
                        width=235,
                        height=39.0, anchor=NW)

                self.icon_image_profile = PhotoImage(file=os.path.join('assets',"profile_icon.png"))

                self.icon_profile = self.canvas.create_image(
                        50.7548828125,
                        188.0,
                        image=self.icon_image_profile)

                # Contact Button definition on the left side bar
                self.button_image_contacts = PhotoImage(file=os.path.join('assets',"contact_new.png"))

                self.button_contacts = Button(self,
                        image=self.button_image_contacts,
                        borderwidth=0,
                        anchor= W,
                        bg="#03000F",
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_contacts clicked"),
                        relief="flat")

                self.button_contacts.place(
                        x=75.0,
                        y=210.85498046875,
                        width=235.0,
                        height=39.0)
                
                self.icon_image_contacts = PhotoImage(file=os.path.join('assets',"contact_icon.png"))

                self.icon_contacts = self.canvas.create_image(
                        50.7548828125,
                        230.0,
                        image=self.icon_image_contacts)        


                # sb_download Button definition on the left side bar
                self.button_image_sb_download = PhotoImage(file=os.path.join('assets',"downloads_new.png"))

                self.button_sb_download = Button(self,
                        image=self.button_image_sb_download,
                        borderwidth=0,
                        bg="#03000F",
                        anchor= W,
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_sb_download clicked"),
                        relief="flat")

                self.button_sb_download.place(
                        x=75.0,
                        y=250.0,
                        width=235,
                        height=39.0)
                
                self.icon_image_sb_download = PhotoImage(file=os.path.join('assets',"sb_download_icon.png"))

                self.icon_sb_download = self.canvas.create_image(
                        50.70458984375,
                        272.634765625,
                        image=self.icon_image_sb_download)
                

                self.canvas.create_rectangle(
                        27.97631871700287,
                        322.97631871700287,
                        357.0,
                        324.0,
                        fill="#707070",
                        outline="")


                # updates Button definition on the left side bar
                self.button_image_updates = PhotoImage(file=os.path.join('assets',"updates.png"))

                self.button_updates = Button(self,
                        image=self.button_image_updates,
                        borderwidth=0,
                        anchor= W,
                        bg="#03000F",
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_updates clicked"),
                        relief="flat")

                self.button_updates.place(
                        x=75.0,
                        y=344.4150390625,
                        width=235.0,
                        height=39)
                
                self.icon_image_updates = PhotoImage(file=os.path.join('assets',"updates_icon.png"))

                self.icon_updates = self.canvas.create_image(
                        50.7548828125,
                        362.43994140625,
                        image=self.icon_image_updates)
                

                # Tutorials Button definition on the left side bar
                self.button_image_tutorials = PhotoImage(file=os.path.join('assets',"Tutorials.png"))

                self.button_tutorials = Button(self,
                        image=self.button_image_tutorials,
                        borderwidth=0,
                        bg="#03000F",
                        anchor= W,
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_tutorials clicked"),
                        relief="flat")

                self.button_tutorials.place(
                        x=75.0,
                        y=384.0,
                        width=235.0,
                        height=39)
                
                self.icon_image_tutorials = PhotoImage(file=os.path.join('assets',"tutorials_icon.png"))

                self.icon_tutorials = self.canvas.create_image(
                        50.0,
                        403.27001953125,
                        image=self.icon_image_tutorials)        


                # Patch notes Button definition on the left side bar
                self.button_image_patch = PhotoImage(file=os.path.join('assets',"patch_notes.png"))

                self.button_patch = Button(self,
                        image=self.button_image_patch,
                        borderwidth=0,
                        bg="#03000F",
                        anchor= W,
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_patch clicked"),
                        relief="flat")

                self.button_patch.place(
                        x=75.0,
                        y=424.0,
                        width=235.0,
                        height=39.0)
                
                self.icon_image_patch = PhotoImage(file=os.path.join('assets',"patch_notes_icon.png"))

                self.icon_patch = self.canvas.create_image(
                        50.0,
                        444.0,
                        image=self.icon_image_patch)


                # Settings Button definition on the left side bar
                self.button_image_settings = PhotoImage(file=os.path.join('assets',"settings.png"))

                self.button_settings = Button(self,
                        image=self.button_image_settings,
                        borderwidth=0,
                        bg="#03000F",
                        anchor= W,
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_settings clicked"),
                        relief="flat")

                self.button_settings.place(
                        x=75.0,
                        y=464.0,
                        width=235.0,
                        height=39.0)

                self.icon_image_settings = PhotoImage(file=os.path.join('assets',"settings_icon.png"))

                self.icon_settings = self.canvas.create_image(
                        50.0,
                        485.0,
                        image=self.icon_image_settings)
                #endregion

                #region Information Panel within Side_bar
                # Information Text
                self.canvas.create_text(
                        22.0,
                        800.0,
                        anchor="nw",
                        text="INFORMATION",
                        fill="#C7C7C7",
                        font=("Graphik Regular", 12 * -1))

                # Help Button definition on the left side bar
                self.button_image_help = PhotoImage(file=os.path.join('assets',"help.png"))

                self.button_help = Button(self,
                        image=self.button_image_help,
                        borderwidth=0,
                        bg="#03000F",
                        anchor= W,
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_help clicked"),
                        relief="flat")

                self.button_help.place(
                        x=75.0,
                        y=825.0,
                        width=235.0,
                        height=39.0)
                
                self.icon_image_help = PhotoImage(file=os.path.join('assets',"help_icon.png"))

                self.icon_help = self.canvas.create_image(
                        50.0,
                        842.0,
                        image=self.icon_image_help)

                # Conditions Button definition on the left side bar
                self.button_image_conditions = PhotoImage(file=os.path.join('assets',"conditions.png"))

                self.button_conditions = Button(self,
                        image=self.button_image_conditions,
                        borderwidth=0,
                        bg="#03000F",
                        anchor= W,
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_conditions clicked"),
                        relief="flat")

                self.button_conditions.place(
                        x=75.0,
                        y=865.0,
                        width=235.0,
                        height=39.0)
                
                self.icon_image_conditions = PhotoImage(file=os.path.join('assets',"conditions_icon.png"))

                self.icon_conditions = self.canvas.create_image(
                        50.0,
                        884.0,
                        image=self.icon_image_conditions)

                # confidentiality Button definition on the left side bar
                self.button_image_confidentiality = PhotoImage(file=os.path.join('assets',"confidentiality.png"))

                self.button_confidentiality = Button(self,
                        image=self.button_image_confidentiality,
                        borderwidth=0,
                        bg="#03000F",
                        anchor= W,
                        activebackground="#C7C7C7",
                        highlightthickness=0,
                        command=lambda: print("button_confidentiality clicked"),
                        relief="flat")

                self.button_confidentiality.place(
                        x=75.0,
                        y=904.0,
                        width=235.0,
                        height=39.0)
                
                self.icon_image_confidentiality = PhotoImage(file=os.path.join('assets',"confidentiality_icon.png"))

                self.icon_confidentiality = self.canvas.create_image(
                        50.0,
                        922.0,
                        image=self.icon_image_confidentiality)
                #endregion
                
                #-------------------------------------Top_bar buttons defination GUI--------------------------------------------
                #region Top bar components
                # Back button on top bar
                # button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))

                # button_10 = Button(
                #                 image=button_image_10,
                #                 borderwidth=0,
                #                 highlightthickness=0,
                #                 command=lambda: print("button_10 clicked"),
                #                 relief="flat")

                # button_10.place(
                #         x=386.0,
                #         y=29.0,
                #         width=50.0,
                #         height=50.0)


                self.button_image_back = PhotoImage(file=os.path.join('assets',"back_button_new.png"))

                self.button_back = Button(self,
                        image=self.button_image_back,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        highlightthickness=0,
                        command=lambda: print("button_back clicked"),
                        relief="flat")

                self.button_back.place(
                        x=335.0,
                        y=28.0,
                        width=50.0,
                        height=50.0)    
                
                # Forward Button top bar
                self.button_image_forward = PhotoImage(file=os.path.join('assets',"forward_button.png"))

                self.button_forward = Button(self,
                        image=self.button_image_forward,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        highlightthickness=0,
                        command=lambda: print("button_forward clicked"),
                        relief="flat")

                self.button_forward.place(
                        x=395.0,
                        y=28.0,
                        width=50.0,
                        height=50.0)    

                # Search barimage and input
                self.entry_image_searchbar = PhotoImage(file=os.path.join('assets',"entry_search.png"))

                self.entry_bg_searchbar = self.canvas.create_image(
                        605.0,
                        55.0,
                        #image=self.entry_image_searchbar
                        )

                self.entry_searchbar = Entry(self,
                        bd=0,
                        bg="#3D3B48",
                        highlightthickness=0)

                self.entry_searchbar.place(
                        x=460.0,
                        y=34.0,
                        width=300.0,
                        height=40.0)
                
                # Blue searchbar rectangle
                self.canvas.create_rectangle(
                        761.0,
                        34.0,
                        811.0,
                        74.0,
                        fill="#008EFF",
                        outline="")
                
                self.magnifier_image_searchbar = PhotoImage(file=os.path.join('assets',"magnifier.png"))
                        
                self.magnifier_bg_searchbar =  Button(self,
                        image=self.magnifier_image_searchbar,
                        borderwidth=0,
                        bg="#008EFF",
                        activebackground="#008EFF",
                        highlightthickness=0,
                        command=lambda: print("magnifier_image_searchbar clicked"),
                        relief="flat")
                
                self.magnifier_bg_searchbar.place(x=776, y=44)

                # self.magnifier_bg_searchbar = self.canvas.create_image(
                #         761.0,
                #         34.0,
                #         image=self.magnifier_image_searchbar
                #         )

                # Underline in the main window under tabs
                self.canvas.create_rectangle(
                        385.5,
                        106.5,
                        1831.0,
                        107.0,
                        fill="#3D3B48",
                        outline="")

                # self.canvas.create_text(
                #         473.0,
                #         48.14813232421875,
                #         anchor="nw",
                #         text="Search...",
                #         fill="#D9D9D9",
                #         font=("Graphik Regular", 15 * -1))
                
                # self.canvas.create_text(
                #         473.0,
                #         48.14813232421875,
                #         anchor="ne",
                #         text="Search...",
                #         fill="#D9D9D9",
                #         font=("Graphik Regular", 15 * -1))

                # Profile button on the top bar
                self.button_image_profile = PhotoImage(file=os.path.join('assets',"profile_button.png"))

                self.button_profile = Button(self,
                        image=self.button_image_profile,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        highlightthickness=0,
                        command=lambda: print("button_profile clicked"),
                        relief="flat")

                self.button_profile.place(
                        x=-130.0,
                        y=32.0,
                        relx = 1,
                        width=50.0,
                        height=50.0, anchor = NW)

                # use the following lines when resizing 
                #, relx = 1,anchor = "ne"
                #x=1783.0,
                #x=-137.0,
                #y=32.0,
                # Language Button on the top bar
                self.button_image_language = PhotoImage(file=os.path.join('assets',"language_button.png"))

                self.button_language = Button(self,
                        image=self.button_image_language,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        highlightthickness=0,
                        command=lambda: print("button_language clicked"),
                        relief="flat")

                self.button_language.place(
                        x=-290.0,
                        y=48.0,
                        relx = 1,
                        width=56.0,
                        height=19.0, anchor = NW)
                # x=1624.0,
                # Download button on the top bar
                self.button_image_download = PhotoImage(file=os.path.join('assets',"download_button.png"))

                self.button_download = Button(self,
                        image=self.button_image_download,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        highlightthickness=0,
                        command=lambda: print("button_download clicked"),
                        relief="flat")

                self.button_download.place(
                        x=-178.0,
                        y=42.0,
                        relx = 1,
                        width=25.0,
                        height=28.0, anchor = NW)
                # x=1736.0
                # notification button on the top bar
                self.button_image_notification = PhotoImage(file=os.path.join('assets',"notification_button.png"))

                self.button_notification = Button(self,
                        image=self.button_image_notification,
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#03000F",
                        activebackground="#03000F",
                        command=lambda: print("button_image_notification clicked"),
                        relief="flat")

                self.button_notification.place(
                        x=-230.0,
                        y=38.0,
                        relx = 1,
                        width=35.0,
                        height=34.0, anchor = NW)
                #x=1685.0
                #endregion
                
                #-------------------------------------Top_bar Tabs GUI--------------------------------------------
                
                #region Three tabs on top of the window Home, News and Portfolio

                # Home button on the top bar
                self.button_image_home = PhotoImage(file=os.path.join('assets',"Home_button.png"))

                self.button_home = Button(self.canvas,
                        #image=button_image_home,
                        text="Home",
                        font="Graphik",
                        fg="#D9D9D9",
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#131116",
                        activebackground="#131116",
                        command=lambda: self.frame_management(self.button_home,self.underline_home),
                        relief="flat")

                self.button_home.place(
                        x=823.0,
                        y=1.0,
                        width=105.0,
                        height=103.0, anchor=NW)
                
                self.underline_home = self.canvas.create_rectangle(
                        824.0,
                        105.0,
                        934.0,
                        108.0,
                        fill="#BE82FF",
                        #fill="#040305",
                        outline="")
                
                # News button on the top bar
                self.button_image_news = PhotoImage(file=os.path.join('assets',"news_button.png"))

                self.button_news = Button(self.canvas,
                        #image=button_image_news,
                        text="News",
                        font="Graphik",
                        fg="#D9D9D9",
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#03000F",
                        activebackground="#131116",
                        command=lambda: self.frame_management(self.button_news,self.underline_news),
                        relief="flat")

                self.button_news.place(
                        x=928.0,
                        y=1.0,
                        width=105.0,
                        height=103.0, anchor=NW)
                
                self.underline_news = self.canvas.create_rectangle(
                        929.0,
                        105.0,
                        1037.0,
                        108.0,
                        fill="#040305",
                        outline="")

                # Portfolio button on the top bar
                self.button_image_portf = PhotoImage(file=os.path.join('assets',"portfolio_button.png"))

                self.button_portf = Button(self.canvas,
                        #image=button_image_portf,
                        text="Portfolio",
                        font="Graphik",
                        fg="#D9D9D9",
                        borderwidth=0,
                        highlightthickness=0,
                        bg="#03000F",
                        activebackground="#131116",
                        command=lambda: self.frame_management(self.button_portf,self.underline_portf),
                        relief="flat")

                self.button_portf.place(
                        x=1033.0,
                        y=1.0,
                        width=105.0,
                        height=103.0, anchor=NW)
                
                self.underline_portf = self.canvas.create_rectangle(
                        1034.0,
                        105.0,
                        1142.0,
                        108.0,
                        fill="#040305",
                        outline="")

                # Dropdown button for Home, News and Portfolio
                self.button_options = [self.button_home.cget('text'), self.button_news.cget('text'),self.button_portf.cget('text')]
                self.value_inside = StringVar(self.canvas)
                self.value_inside.set(self.button_home.cget('text'))
                self.underline_filler = None
                self.dropdown =  OptionMenu(self.canvas, self.value_inside, *self.button_options, command= self.frame_management_dropdown)
                self.dropdown.config(relief="flat",bg="#040405", fg="#D9D9D9", activebackground="#040405",highlightthickness=0)
                self.dropdown["menu"].config(bg="#040405", fg="#D9D9D9", activebackground="#131116")
                self.dropdown.place_forget()
                #endregion
                # PLACE HOLDER NEEDS TO REMOVE
                self.some = []
                self.canvas.addtag_all("all")
                


        def change_color(self, selected_button, selected_line):

                print( selected_button.cget('text') + " clicked")
                all_buttons = [self.button_home, self.button_news, self.button_portf]
                all_underlines = [self.underline_home, self.underline_news,self.underline_portf]
                for unselected_button in all_buttons:
                        for unselected_underline in all_underlines:
                                if not unselected_underline == selected_line:
                                        self.canvas.itemconfig(unselected_underline, fill="#03000F")
                                if not unselected_button == selected_button:
                                        unselected_button.configure(bg='#03000F')

                

                if not selected_button.cget('bg') == "#131116":
                        selected_button.configure(bg='#131116')
                        self.canvas.itemconfig(selected_line, fill="#BE82FF")
                # else:
                #         selected_button.configure(bg='#03000F') #040305
                #         self.canvas.itemconfig(selected_line, fill="#03000F") #040305
                
        def frame_management(self, selected_button,selected_line):
                print("inside FRAMEEEE management")
 
                self.change_color(selected_button,selected_line)


                if selected_button.cget('text').lower() == "home":
                        home_frame = self.frames.home_frame()
                        self.show_frame(home_frame)
                        self.active_frame = 'home'
                elif selected_button.cget('text').lower() == "news":
                        news_frame = self.frames.news_frame()
                        self.show_frame(news_frame)
                        self.active_frame = 'news'
                elif selected_button.cget('text').lower() == "portfolio":
                        portfol_frame = self.frames.portfolio_frame()
                        self.show_frame(portfol_frame)
                        self.active_frame = 'portf'

                        
        def frame_management_dropdown(self,event):
                selected_button = self.value_inside.get()
                print(selected_button)
                if selected_button.lower() == "home":
                        home_frame = self.frames.home_frame()
                        self.show_frame(home_frame)
                        self.active_frame = 'home'
                elif selected_button.lower() == "news":
                        news_frame = self.frames.news_frame()
                        self.show_frame(news_frame)
                        self.active_frame = 'news'
                elif selected_button.lower() == "portfolio":
                        portfol_frame = self.frames.portfolio_frame()
                        self.show_frame(portfol_frame)
                        self.active_frame = 'portf'

        def show_frame(self, frame):

                
                frame.place(x=300,  y=100,  relx=0.01,  rely=0.01)
                frame.tkraise()
                
                #frame.pack()
                print("inside show frame")
        
        def resize_manager(self,event):

                # Main window width and height
                self.current_winH = self.winfo_height()
                self.current_winW = self.winfo_width()

                #print("window height is :",self.current_winH)
                #print("window width is :",self.current_winW)


                canvas_width = self.canvas.winfo_reqwidth()
                canvas_height = self.canvas.winfo_reqheight()

                # determine the ratio of old width/height to new width/height
                self.wscale = canvas_width/self.current_winW
                self.hscale = canvas_height/self.current_winH


                self.canvas.config(width=self.current_winW, height=self.current_winH)
                #self.canvas.scale("all",0,0,wscale,hscale)


                # Adjusting all the frames(home, news, port) sizes dynamically
                
                self.frame_home_width = self.frames.home_fr.winfo_reqwidth()
                self.frame_home_height = self.frames.home_fr.winfo_reqheight()

                self.frame_news_width = self.frames.news_fr.winfo_reqwidth()
                self.frame_news_height = self.frames.news_fr.winfo_reqheight()

                self.frame_portf_width = self.frames.portf_fr.winfo_reqwidth()
                self.frame_portf_height = self.frames.portf_fr.winfo_reqheight()

                self.frames.home_fr.config(width=self.frame_home_width/self.wscale, height=self.frame_home_height/self.hscale)
                self.frames.news_fr.config(width=self.frame_news_width/self.wscale, height=self.frame_news_height/self.hscale)
                self.frames.portf_fr.config(width=self.frame_portf_width/self.wscale, height=self.frame_portf_height/self.hscale)


                #print("NEW Canvas height is : ", self.canvas.winfo_reqheight())
                #print("NEW Canvas width is : ", self.canvas.winfo_reqwidth())
                self.topbar_button_resizing()

        def topbar_button_resizing(self):
                if self.current_winH < 1500 and self.current_winH < 950:
                        #print("inside change size")

                        self.dropdown.place(x=780.0, y=1.0, width=105.0,
                        height=103.0, anchor=NW)

                        

                        self.button_home.place_forget()
                        self.button_news.place_forget()
                        self.button_portf.place_forget()
                        self.canvas.itemconfig(self.underline_home, fill="#040305")

                else:
                        self.dropdown.place_forget()
                        self.button_home.place(x=823.0, y=1.0, width=105.0,
                        height=103.0, anchor=NW)
                        self.button_news.place(x=928.0, y=1.0, width=105.0,
                        height=103.0, anchor=NW)
                        self.button_portf.place(x=1033.0, y=1.0, width=105.0,
                        height=103.0, anchor=NW)


        def set_appwindow(self, mainWindow): # to display the window icon on the taskbar, 
                                        # even when using root.overrideredirect(True
                # Some WindowsOS styles, required for task bar integration
                GWL_EXSTYLE = -20
                WS_EX_APPWINDOW = 0x00040000
                WS_EX_TOOLWINDOW = 0x00000080
                # Magic
                hwnd = windll.user32.GetParent(mainWindow.winfo_id())
                stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
                stylew = stylew & ~WS_EX_TOOLWINDOW
                stylew = stylew | WS_EX_APPWINDOW
                res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
                
                mainWindow.wm_withdraw()
                mainWindow.after(10, lambda: mainWindow.wm_deiconify())


        def minimize_me(self):
                self.attributes("-alpha",0) # so you can't see the window when is minimized
                self.minimized = True

        def deminimize(self, event):

                self.focus() 
                self.attributes("-alpha",1) # so you can see the window when is not minimized
                if self.minimized == True:
                        self.minimized = False                              

        def quit_window(self, e):
                self.quit()
                self.destroy()

        def get_pos(self,e):
                self.xwin = self.winfo_x()
                self.ywin = self.winfo_y()
                self.startx = e.x_root
                self.starty = e.y_root

                self.ywin = self.ywin - self.starty
                self.xwin = self.xwin - self.startx
                
                def move_window(e):
                        #window.geometry(f'+{e.x_root}+{e.y_root}')
                        self.geometry("1920x1080" + '+{0}+{1}'.format(e.x_root + self.xwin, e.y_root + self.ywin))  
                
                
                self.startx = e.x_root
                self.starty = e.y_root
                self.titlebar.bind("<B1-Motion>", move_window)
                

        def move_window(self,e):
                        #window.geometry(f'+{e.x_root}+{e.y_root}')
                self.geometry("1920x1080" + '+{0}+{1}'.format(e.x_root + self.xwin, e.y_root + self.ywin))        

        def maximize_me(self):

                if self.maximized == False: # if the window was not maximized
                        self.normal_size = self.geometry()
                        #expand_button.config(text=" 🗗 ")
                        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
                        self.maximized = not self.maximized 
                        # now it's maximized
                        
                else: # if the window was maximized
                        #expand_button.config(text=" 🗖 ")
                        self.geometry(self.normal_size)
                        self.maximized = not self.maximized
                        # now it is not maximized




#if __name__ == "__main__":
    #root = Tk.Tk()
    #root.geometry("1920x1080")

# app = LauncherApp()
# app.mainloop()


# root = Tk()
# root.withdraw()
# loginWindow('title', root)
# root.mainloop() 