# Explicit imports to satisfy Flake8
#from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import tkinter
import json
import pip._vendor.requests 
from tkinter import *
from pathlib import Path
from frames import ScreenFrames
from launcher import LauncherApp
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Toplevel
from ctypes import windll



class loginWindow(Toplevel):
        def __init__(self, title, parent):
                Toplevel.__init__(self, parent)

                # Log in page size and background color definition
                self.geometry("1280x791")
                self.maxsize(1280,791)
                self.minsize(1280,791)
                
                self.configure(bg = "#FFFFFF")
                self.title("Login? ")
                self.access = None
                self.version = "Version 1.0.24"
                #-------------------------------------Log in page GUI--------------------------------------------
                #region Log in page GUI Variables, Images, Buttons
                # Main canvas for the log in page
                self.canvas_login = Canvas(
                        self,
                        bg = "#111111",
                        height = 791,
                        width = 1280,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")

                self.canvas_login.place(x = 0, y = 0)

                self.overrideredirect(True)

                self.minimized = False # only to know if window is minimized
                self.maximized = False # only to know if window is maximized

                self.titlebar = Label(self.canvas_login, bg= "#03000F")
                self.titlebar.place(x=0,y=0,width=1920,height=28)

                self.titlebar.bind('<Button-1>', self.get_pos)
                

                self.bind("<FocusIn>",self.deminimize)
                self.after(10, lambda: self.set_appwindow(self)) # to see the icon on the task bar

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
                        x=1200.0,
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
                        x=1225.0,
                        y=0.0,
                        width=28.0,
                        height=28.0)

                self.button_image_quit = PhotoImage(file=os.path.join('assets',"button_quit.png"))

                self.button_quit = Button(self.titlebar,
                        image=self.button_image_quit,
                        borderwidth=0,
                        bg="#03000F",
                        activebackground="red",
                        highlightthickness=0,
                        command=lambda: print("button_quit clicked"),
                        relief="flat")

                self.button_quit.place(
                        x=1245.0,
                        y=0.0,
                        width=37.0,
                        height=28.0)
                self.button_quit.bind("<Button-1>", self.quit_window)
                self.bind("<FocusIn>",self.deminimize)
                self.after(10, lambda: self.set_appwindow(self)) # to see the icon on the task bar
                #endregion


                #-------------------------------------Log in page GUI--------------------------------------------
                #region Log in page GUI Variables, Images, Buttons
                # Main canvas for the log in page
                # self.canvas_login = Canvas(
                #         self,
                #         bg = "#111111",
                #         height = 791,
                #         width = 1280,
                #         bd = 0,
                #         highlightthickness = 0,
                #         relief = "ridge")

                # self.canvas_login.place(x = 0, y = 0)

                # Adding image of the person and defining it on the canvas
                self.image_login_person = PhotoImage(file=os.path.join('assets','image_login_person.png'))

                self.image_log_person = self.canvas_login.create_image(
                        900.0858764648438,
                        575.5435180664062,
                        image=self.image_login_person)

                # Log in page background


                self.image_grad = PhotoImage(file=os.path.join('assets',"login_background.png"))
                self.image_gradient = self.canvas_login.create_image(
                        800.0858764648438,
                        450.5435180664062,
                        image=self.image_grad)

                # Purple log in button image and definition
                self.button_image_login = PhotoImage(file=os.path.join('assets',"login_button.png"))
                self.button_login = Button(self,
                        image=self.button_image_login,
                        borderwidth=0,
                        bg='#111111',
                        activebackground="#111111",
                        highlightthickness=0,
                        command=lambda: self.login(),
                        relief="flat")
                self.button_login.place(
                        x=90.0,
                        y=624.0,
                        width=153.0,
                        height=41.0)


                # Purple Text on the log in page
                self.canvas_login.create_text(
                        87.0,
                        310.0,
                        anchor="nw",
                        text="AUTHORIZATION\nOF YOUR ACCOUNT",
                        fill="#BE82FF",
                        font=("Graphik Semibold", 55 * -1))

                # Entry box (this is an image) for email address later to be removed
                self.entry_image_email = PhotoImage(file=os.path.join('assets',"entry_email.png"))


                self.entry_bg_email = self.canvas_login.create_image(
                        272.4320831298828,
                        469.70188903808594,
                        image=self.entry_image_email)

                # actual entry box for email address
                self.entry_bg_email = Entry(self,
                        bd=0,
                        bg="#131116",
                        highlightthickness=0)

                self.entry_bg_email.place(
                        x=95.369140625,
                        y=445.06805419921875,
                        width=354.1258850097656,
                        height=51.267669677734375)

                self.canvas_login.create_text(
                        118.0,
                        461.0,
                        anchor="nw",
                        text="Account name (Email Address)",
                        fill="#C7C7C7",
                        font=("Graphik Regular", 19 * -1))


                # Entry box for Password (this is an image) later to be removed
                self.entry_image_2 = PhotoImage(file=os.path.join('assets',"entry_password.png"))

                self.entry_bg_2 = self.canvas_login.create_image(
                        272.4320831298828,
                        541.7176971435547,
                        image=self.entry_image_2)

                # actual entry box for password
                self.entry_2 = Entry(self,
                        bd=0,
                        bg="#131116",
                        highlightthickness=0)

                self.entry_2.place(
                        x=95.369140625,
                        y=517.0838623046875,
                        width=354.1258850097656,
                        height=51.267669677734375)

                self.canvas_login.create_text(
                        118.0,
                        533.0,
                        anchor="nw",
                        text="Password",
                        fill="#C7C7C7",
                        font=("Graphik Regular", 19 * -1))

                # Forgot password button definition (this is an image) later to be removed
                self.button_image_forg_pass = PhotoImage(file=os.path.join('assets',"forgot_pass.png"))

                self.button_forgot_pass = Button(self,
                        image=self.button_image_forg_pass,
                        borderwidth=0,
                        bg='#111111',
                        activebackground="#111111",
                        # text="Forgot Password",
                        # font=("Graphik Light", 12 * -1),
                        # fg='#D9D9D9',
                        highlightthickness=0,
                        command=lambda: print("forgot password clicked"),
                        relief="flat")

                self.button_forgot_pass.place(
                        x=87.0,
                        y=576.0,
                        width=158.0,
                        height=19.0)

                # Create account button definition (this is an image) later to be removed
                self.button_image_cret_acc = PhotoImage(file=os.path.join('assets',"create_acc.png"))

                self.button_create_acc = Button(self,
                        image=self.button_image_cret_acc,
                        borderwidth=0,
                        bg='#131116',
                        activebackground="#131116",
                        highlightthickness=0,
                        command=lambda: print("create account clicked"),
                        relief="flat")

                self.button_create_acc.place(
                        x=262.0,
                        y=638.0,
                        width=151.0,
                        height=20.0)

                # Remember me button definition (this is an image) later to be removed
                self.button_image_remem_me = PhotoImage(file=os.path.join('assets',"remember_me.png"))

                self.button_remember_me = Button(self,
                        image=self.button_image_remem_me,
                        borderwidth=0,
                        bg='#131116',
                        activebackground="#131116",
                        highlightthickness=0,
                        command=lambda: print("remember me clicked"),
                        relief="flat")

                self.button_remember_me.place(
                        x=336.0,
                        y=574.0,
                        width=138.28228759765625,
                        height=24.0)

                # Terms and Policy button definition (this is an image) later to be removed
                self.button_image_terms_pol = PhotoImage(file=os.path.join('assets',"terms_policies.png"))

                self.button_terms_pol = Button(self,
                        image=self.button_image_terms_pol,
                        borderwidth=0,
                        bg='#131116',
                        activebackground="#131116",
                        highlightthickness=0,
                        command=lambda: print("Terms and policies clicked"),
                        relief="flat")

                self.button_terms_pol.place(
                        x=90.0,
                        y=744.0,
                        width=397.0,
                        height=16.0)

                # Umalut Logo image
                self.image_logo = PhotoImage(file=os.path.join('assets',"umlaut_logo.png"))

                self.image_logo_um = self.canvas_login.create_image(
                        247.19351196289062,
                        229.26376342773438,
                        image=self.image_logo)

                # Change Language button definition (this is an image) later to be removed
                self.button_image_lang = PhotoImage(file=os.path.join('assets',"button_image_lang.png"))

                self.button_lang = Button(self,
                        image=self.button_image_lang,
                        borderwidth=0,
                        bg='#111111',
                        activebackground="#111111",
                        highlightthickness=0,
                        command=lambda: print("lanuage button clicked"),
                        relief="flat")

                self.button_lang.place(
                        x=36.0,
                        y=129.0,
                        width=73.0,
                        height=25.0)

                # Version text
                self.canvas_login.create_text(
                        90.0,
                        675.0,
                        anchor="nw",
                        text=self.version,
                        fill="#C7C7C7",
                        font=("Graphik Light", 12 * -1))
                #endregion
                # PLACE HOLDER NEEDS TO REMOVE
                self.something = []

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
                        self.geometry("1280x791" + '+{0}+{1}'.format(e.x_root + self.xwin, e.y_root + self.ywin))  
                
                
                self.startx = e.x_root
                self.starty = e.y_root
                self.titlebar.bind("<B1-Motion>", move_window)
                

        def move_window(self,e):
                        #window.geometry(f'+{e.x_root}+{e.y_root}')
                self.geometry("1280x791" + '+{0}+{1}'.format(e.x_root + self.xwin, e.y_root + self.ywin))        

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


        def login(self):
                self.access = True
                if self.access:
                        url = 'https://login.microsoft.com/81330ed1-77c9-4cf3-91cc-6113a7acd383/oauth2/v2.0/token'
                        data={'grant_type': 'password', 'username': self.entry_bg_email.get(), 'password': self.entry_2.get() ,'client_id': '1de4c1fc-5615-47c1-bd2e-36754ba5f518','client_secret': 'uJw8Q~k4Vx.XPCWerM179l_e2XBEJ6rqvZf~lcYY','scope': 'https://graph.microsoft.com/.default'}
                        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                        s = pip._vendor.requests.post(url, headers=headers, data=data)
                        token = s.json().get("access_token")
                        print("token is ", token)
                        if token is not None:
                                url = 'https://graph.microsoft.com/v1.0/me/' 
                                headers = {'Authorization': 'Bearer {}'.format(token)}
                                r = pip._vendor.requests.get(url, headers=headers)
                                print(r.json())
                                self.destroy()
                                LauncherApp()
                        elif token is None:
                                tkinter.messagebox.showinfo("Authentication Error - Login Failed","Please enter correct user email and/or password")
                return True
