import os
import webbrowser
import tkinter
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Toplevel
from PIL import Image, ImageTk
from utils.download_az import AzureDownload
import threading
import subprocess



class ScreenFrames():
    def __init__(self,screen):
        self.screen = screen
        #self.path = path
        self.all_frame_width = 1510
        self.all_frame_height = 1080
        self.home_fr = Frame(self.screen, bg='#03000F', width=self.all_frame_width, height=self.all_frame_height)
        self.news_fr = Frame(self.screen, bg='#03000F', width=self.all_frame_width, height=self.all_frame_height)
        self.portf_fr = Frame(self.screen, bg='#03000F', width=self.all_frame_width, height=self.all_frame_height)
        self.article_fr = Frame(self.screen, bg='#03000F', width=self.all_frame_width, height=self.all_frame_height)
        self.project_fr = Frame(self.screen, bg='#03000F', width=self.all_frame_width, height=self.all_frame_height)
        self.images_path = "assets/"

        self.high_res_img_article_main = Image.open(self.images_path + "article_main.jpg")
        #self.button_article_thumbnail_1_hf_resized = self.high_res_img_article_main.resize((465, 262))
        self.panel_article_img_main = self.high_res_img_article_main.resize((228, 128))
        self.opened_article_img_main = self.high_res_img_article_main.resize((710, 399))

        self.high_res_img_article_1 = Image.open(self.images_path + "article_1.jpg")
        self.button_article_thumbnail_1_hf_resized = self.high_res_img_article_1.resize((465, 262))
        self.panel_article_img_1 = self.high_res_img_article_1.resize((228, 128))
        self.opened_article_img_1 = self.high_res_img_article_1.resize((710, 399))
        self.button_project_thumbnail_1_pf = self.high_res_img_article_1.resize((354,199))
        self.button_article_img_1_big_nf = self.high_res_img_article_1.resize((710,399))

        self.high_res_img_article_2 = Image.open(self.images_path + "article_2.jpg")
        self.button_article_thumbnail_2_hf_resized = self.high_res_img_article_2.resize((467, 263))
        self.panel_article_img_2 = self.high_res_img_article_2.resize((228, 128))
        self.opened_article_img_2 = self.high_res_img_article_2.resize((710, 399))
        self.button_project_thumbnail_2_pf = self.high_res_img_article_2.resize((354,199))
        self.button_article_img_2_big_nf = self.high_res_img_article_2.resize((710,399))
        
        self.high_res_img_article_3 = Image.open(self.images_path + "article_3.jpg")
        self.button_article_thumbnail_3_hf_resized = self.high_res_img_article_3.resize((467, 263))
        self.panel_article_img_3 = self.high_res_img_article_3.resize((228, 128))
        self.opened_article_img_3 = self.high_res_img_article_3.resize((710, 399))
        self.button_project_thumbnail_3_pf = self.high_res_img_article_3.resize((354,199))

        self.high_res_img_article_4 = Image.open(self.images_path + "article_4.jpg")
        self.panel_article_img_4 = self.high_res_img_article_4.resize((228, 128))
        self.button_project_thumbnail_4_pf = self.high_res_img_article_4.resize((354,199))

        self.high_res_img_article_5 = Image.open(self.images_path + "article_5.jpg")
        self.panel_article_img_5 = self.high_res_img_article_5.resize((228, 128))
        self.button_project_thumbnail_5_pf = self.high_res_img_article_5.resize((354,199))

        self.high_res_img_article_6 = Image.open(self.images_path + "article_6.jpg")
        self.panel_article_img_6 = self.high_res_img_article_6.resize((228, 128))
        self.button_project_thumbnail_6_pf = self.high_res_img_article_6.resize((354,199))
        


    def home_frame(self):
        #original width 1452
        # original height 426
        #print("new width of home frame: ", self.home_fr.winfo_reqwidth())

        # self.home_image = PhotoImage(file=os.path.join('assets',"image_28.png"))
        # self.home_page_label = Label(self.home_fr, image=self.home_image )
        # self.home_page_label.place(x= 350 , y=50)
        # mystring = 'Welcome to the Home page'
        # self.home_page_text = Label(self.home_fr, text= mystring, font=('Graphik', 15))
        # self.home_page_text.place(x=50 , y=50)
        # # myscrollbar=tkinter.Scrollbar(self.home_fr,orient="vertical")
        # # myscrollbar.place()

        self.home_frame_canvas = Canvas(self.home_fr, bg = "#03000F", height = 890, width = 1460, bd = 0, highlightthickness = 0, relief = "ridge")
        self.home_frame_canvas.place(x = 0, y = 0)

        self.home_frame_gui()



        

        
        return self.home_fr
    
    def news_frame(self):

        #self.news_fr = Frame(self.screen, bg='#131116', width=1452, height=426)
        
        # self.News_image = PhotoImage(file=os.path.join('assets',"image_22.png"))
        # self.News_page_label = Label(self.news_fr, image=self.News_image)
        # self.News_page_label.place(x=450 , y=50)
        # self.news_page_text = Label(self.news_fr, text='Wow people are having fun outside', font=('Graphik', 15))
        # self.news_page_text.place(x=50 , y=50)

        self.news_frame_canvas = Canvas(self.news_fr, bg = "#03000F", height = 890, width = 1460, bd = 0, highlightthickness = 0, relief = "ridge")
        self.news_frame_canvas.place(x = 0, y = 0)

        self.news_frame_gui()

        return self.news_fr
    
    def portfolio_frame(self):

        #self.portf_fr = Frame(self.screen, bg='#131116', width=1452, height=426)
        
        # self.portfolio_image = PhotoImage(file=os.path.join('assets',"image_31.png"))
        # self.Portf_page_label = Label(self.portf_fr, image=self.portfolio_image)
        # self.Portf_page_label.place(x=450 , y=50)
        # self.portf_page_text = Label(self.portf_fr, text='This is portfolio!!!!!', font=('Graphik', 15),)
        # self.portf_page_text.place(x=50 , y=50)

        self.portf_frame_canvas = Canvas(self.portf_fr, bg = "#03000F", height = 890, width = 1460, bd = 0, highlightthickness = 0, relief = "ridge")
        self.portf_frame_canvas.place(x = 0, y = 0)

        self.portf_frame_gui()


        return self.portf_fr
    
    def download_package_thread(self,filename):
        """
        Parameter: filename
        return:None
        Start Download in a thread
        """
        self.button_project_launch['state'] = 'disabled'
        self.downloading_button.place(
            x=1050.0,
            y=459.0,
            width=437.0,
            height=56.0)
        DownloadPackage = AzureDownload()
        thread_download = threading.Thread(target=DownloadPackage.download_package, args=(filename,))
        thread_download.start()
        self.screen.after(2000,self.check_downloads)
    
    def article_frame(self, selected_article):
        print("inside article frame")
        self.article_frame_canvas = Canvas(self.article_fr, bg = "#03000F", height = 890, width = 1460, bd = 0, highlightthickness = 0, relief = "ridge")
        self.article_frame_canvas.place(x = 0, y = 0)
        
        self.article_fr.tkraise()
        self.article_fr.place(x=300,  y=100,  relx=0.01,  rely=0.01)

        self.article_frame_gui(selected_article)
        return self.article_fr


    def project_frame(self, selected_project):
        print("projectframe")
        self.project_frame_canvas = Canvas(self.project_fr, bg = "#03000F", height = 890, width = 1530, bd = 0, highlightthickness = 0, relief = "ridge")
        self.project_frame_canvas.place(x = 0, y = 0)
        
        self.project_fr.tkraise()
        self.project_fr.place(x=300,  y=100,  relx=0.01,  rely=0.01)

        self.project_frame_gui(selected_project)
        return self.project_fr


    def home_frame_gui(self):

        #region Main Top part of the frame----------------------------
        # Top main article for Home frame
        self.home_frame_canvas.create_rectangle(
            8.0,
            10.0,
            1438.0,
            439.0,
            fill="#131016",
            outline="")

        self.image_main_article_hf = PhotoImage(file=os.path.join('assets',"button_main_article_hf.png"))

        # self.image_main_article_hf = self.home_frame_canvas.create_image(
        #     1020.0,
        #     214.0,
        #     image=self.image_main_article_hf)

        self.button_main_article_hf = Button(self.home_frame_canvas,
            text="ar_main",
            image=self.image_main_article_hf,
            bg = "#131016",
            activebackground="#131016",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.article_frame(self.button_main_article_hf),
            relief="flat")

        self.button_main_article_hf.place(
            x=585.0,
            y=10.0,
            width=879,
            height=429)

        self.home_frame_canvas.create_text(
            82.0,
            230.0,
            anchor="nw",
            text="Testtext lorem ipsum dolor sit. Apit, quam nos\nelestiur sitium, consedi diciend aectur-ernam\nint volupti debitas am et eum sanduciscias ento\neos et vero. Apit, quam  nos elestiur",
            fill="#C7C7C7",
            font=("Graphik Regular", 14 * -1))

        self.home_frame_canvas.create_rectangle(
            81.0,
            202.0,
            234.0,
            203.0,
            fill="#C7C7C7",
            outline="")

        self.home_frame_canvas.create_text(
            82.0,
            124.0,
            anchor="nw",
            text="This is a subline and  here another one.",
            fill="#FFFFFF",
            font=("Graphik Medium", 24 * -1)
        )

        self.home_frame_canvas.create_text(
            82.0,
            75.0,
            anchor="nw",
            text="This is a headline",
            fill="#FFFFFF",
            font=("Graphik Semibold", 40 * -1)
        )



        #endregion

        #region Middle Part of the frame----------------------------
        # Training button definition in the middle of Home frame
        self.button_image_training_hf = PhotoImage(file=os.path.join('assets',"button_training.png"))

        self.button_training_hf = Button(self.home_frame_canvas,
            image=self.button_image_training_hf,
            bg = "#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_training clicked"),
            relief="flat") 

        self.button_training_hf.place(
            x=280,
            y=474.0,
            width=82.57275390625,
            height=34.077667236328125)

        # Demo button definition in the middle of Home frame
        self.button_image_demos_hf = PhotoImage(file=os.path.join('assets',"button_demos.png"))
        self.button_demos_hf = Button(self.home_frame_canvas,
            image=self.button_image_demos_hf,
            bg = "#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_demos clicked"),
            relief="flat")

        self.button_demos_hf.place(
            x=374,
            y=474.0,
            width=82.57275390625,
            height=34.077667236328125)

        # Middle text on Home frame
        self.home_frame_canvas.create_text(
            11,
            476.0,
            anchor="nw",
            text="Our projects / training",
            fill="#FFFFFF",
            font=("Graphik Semibold", 24 * -1) )

        #endregion

        #region Bottom Part of the frame----------------------------
        # Image Tile With Button
        self.button_threedots_image_1_hf = PhotoImage(file=os.path.join('assets',"button_threedots_1.png"))

        self.button_threedots_1_hf = Button(self.home_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_threedots_image_1_hf,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_3_hf clicked"),
            relief="flat")

        self.button_threedots_1_hf.place(
            x=1391.0,
            y=825.8643798828125,
            width=36.4384765625,
            height=35.42652893066406)

        # button_article_1 headline text
        self.home_frame_canvas.create_text(
            981.0009765625,
            815.0,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 17 * -1))

        # Article 1 thumbnail
        #self.high_res_img_article_1 = Image.open(self.images_path + "article_1.jpg")
        #self.button_article_thumbnail_1_hf_resized = self.high_res_img_article_1.resize((467, 263))
        self.button_article_thumbnail_1_hf = ImageTk.PhotoImage(self.button_article_thumbnail_1_hf_resized)
        #self.button_article_thumbnail_1_hf = PhotoImage(file=os.path.join('assets',"button_article_1.png"))
        self.button_article_1_hf = Button(self.home_frame_canvas,
            text="ar_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_article_thumbnail_1_hf,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.article_frame(self.button_article_1_hf),
            relief="flat")

        self.button_article_1_hf.place(
            x=981.0009765625,
            y=532.5,
            width=467,
            height=263)

        # Article 2 GUI
        self.button_threedots_image_2_hf = PhotoImage(file=os.path.join('assets',"button_threedots_2.png"))

        self.button_threedots_2_hf = Button(self.home_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_threedots_image_1_hf,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_3_hf clicked"),
            relief="flat")

        self.button_threedots_2_hf.place(
            x=905.5927734375,
            y=825.8643798828125,
            width=36.4384765625,
            height=35.42652893066406)

        # button_article_2 headline text
        self.home_frame_canvas.create_text(
            494.00048828125,
            815.0,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 17 * -1))

        # Article 2 thumbnail
        #self.high_res_img_article_2 = Image.open(self.images_path + "article_2.jpg")
        #self.button_article_thumbnail_2_hf_resized = self.high_res_img_article_2.resize((467, 263))
        self.button_article_thumbnail_2_hf = ImageTk.PhotoImage(self.button_article_thumbnail_2_hf_resized)

        #self.button_article_thumbnail_2_hf = PhotoImage(file=os.path.join('assets',"button_article_2.png"))
        self.button_article_2_hf = Button(self.home_frame_canvas,
            text="ar_2",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_article_thumbnail_2_hf,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.article_frame(self.button_article_2_hf),
            relief="flat")

        self.button_article_2_hf.place(
            x=493.5009765625,
            y=532.5,
            width=467,
            height=263)
        
        # Article 3 GUI
        self.button_threedots_image_3_hf = PhotoImage(file=os.path.join('assets',"button_threedots_3.png"))

        self.button_threedots_3_hf = Button(self.home_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_threedots_image_1_hf,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_3_hf clicked"),
            relief="flat")

        self.button_threedots_3_hf.place(
            x=421.0,
            y=825.8643798828125,
            width=36.4384765625,
            height=35.42652893066406)

        # button_article_3 headline text
        self.home_frame_canvas.create_text(
            9.0,
            815.0,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 17 * -1))

        # Article 3 thumbnail
        #self.high_res_img_article_3 = Image.open(self.images_path + "article_3.jpg")
        #self.button_article_thumbnail_3_hf_resized = self.high_res_img_article_3.resize((467, 263))
        self.button_article_thumbnail_3_hf = ImageTk.PhotoImage(self.button_article_thumbnail_3_hf_resized)

        #self.button_article_thumbnail_3_hf = PhotoImage(file=os.path.join('assets',"button_article_3.png"))
        self.button_article_3_hf = Button(self.home_frame_canvas,
            text="ar_3",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_article_thumbnail_3_hf,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.article_frame(self.button_article_3_hf),
            relief="flat")

        self.button_article_3_hf.place(
            x=8.5009765625,
            y=532.5,
            width=467,
            height=263)


        #endregion
        self.placeholder = []

    def news_frame_gui(self):

        #region Top part
        # top left art

        self.button_image_article_5_nf = ImageTk.PhotoImage(self.button_article_img_1_big_nf)
        self.button_article_5_nf = Button(self.news_frame_canvas,
                text="ar_1",
                bg = "#03000F",
                activebackground="#131116",
                image= self.button_image_article_5_nf ,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.article_frame(self.button_article_5_nf),
                relief="flat")
        
        self.button_article_5_nf.place(x=34, y=10, height=399, width=710)

        self.news_frame_canvas.create_text(
            34.0,
            467.0,
            anchor="nw",
            text="This is a umlaut news article",
            fill="#F1F1F1",
            font=("Graphik Semibold", 24 * -1))


        self.news_frame_canvas.create_text(
            34.0,
            446.0,
            anchor="nw",
            text="17H AGO",
            fill="#C6C6C6",
            font=("Graphik Regular", 12 * -1))

        self.news_frame_canvas.create_text(
            34.0,
            500.0,
            anchor="nw",
            text="October is Cyber Security Awareness Month, and a time to check out\nthe latest cyber adventure Feel. It’s the annual International Day for\nDisaster Risk Reduction (IDDRR). In recognition of this important...",
            fill="#C6C6C6",
            font=("Graphik Regular", 14 * -1))


        # top right art

        self.button_image_article_6_nf = ImageTk.PhotoImage(self.button_article_img_2_big_nf)
        self.button_article_6_nf = Button(self.news_frame_canvas,
                text="ar_2",
                bg = "#03000F",
                activebackground="#131116",
                image= self.button_image_article_6_nf ,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.article_frame(self.button_article_6_nf),
                relief="flat")
        
        self.button_article_6_nf.place(x=780, y=10, height=399, width=710)

        self.news_frame_canvas.create_text(
            780.0,
            446.0,
            anchor="nw",
            text="17H AGO",
            fill="#C6C6C6",
            font=("Graphik Regular", 12 * -1))

        self.news_frame_canvas.create_text(
            780.0,
            467.0,
            anchor="nw",
            text="This is a umlaut news article",
            fill="#F1F1F1",
            font=("Graphik Semibold", 24 * -1))
        
        self.news_frame_canvas.create_text(
            780.0,
            500.0,
            anchor="nw",
            text="October is Cyber Security Awareness Month, and a time to check out\nthe latest cyber adventure Feel. It’s the annual International Day for\nDisaster Risk Reduction (IDDRR). In recognition of this important...",
            fill="#C6C6C6",
            font=("Graphik Regular", 14 * -1))
        
        #endregion

        # white line
        self.news_frame_canvas.create_rectangle(
            30.5,
            600.5,
            1476.0,
            601.0,
            fill="#3D3B48",
            outline="")

        #region under first line
        # left art
        self.button_image_article_3_nf = ImageTk.PhotoImage(self.panel_article_img_3)
        self.button_article_3_nf = Button(self.news_frame_canvas,
                text = "ar_3",
                bg = "#03000F",
                activebackground="#131116",
                image= self.button_image_article_3_nf ,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.article_frame(self.button_article_3_nf),
                relief="flat")
        
        self.button_article_3_nf.place(x=28, y=611, height=128, width=228)

        self.news_frame_canvas.create_text(
            282.0,
            621.0,
            anchor="nw",
            text="17H AGO",
            fill="#C6C6C6",
            font=("Graphik Regular", 12 * -1))
        
        self.news_frame_canvas.create_text(
            282.0,
            642.0,
            anchor="nw",
            text="This is a umlaut news article",
            fill="#F1F1F1",
            font=("Graphik Semibold", 24 * -1))

        self.news_frame_canvas.create_text(
            282.0,
            675.0,
            anchor="nw",
            text="October is Cyber Security Awareness Month, and\na time to check out the latest cyber adventure Feel...",
            fill="#C6C6C6",
            font=("Graphik Regular", 14 * -1))
        
        self.news_frame_canvas.create_text(
            282.0,
            715.0,
            anchor="nw",
            text="+ SEE MORE",
            fill="#008EFF",
            font=("Graphik Semibold", 12 * -1))

        # right art

        self.button_image_article_4_nf = ImageTk.PhotoImage(self.panel_article_img_main)
        self.button_article_4_nf = Button(self.news_frame_canvas,
                text = "ar_main",
                bg = "#03000F",
                activebackground="#131116",
                image= self.button_image_article_4_nf ,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.article_frame(self.button_article_4_nf),
                relief="flat")
        
        self.button_article_4_nf.place(x=775, y=611, height=128, width=228)

        self.news_frame_canvas.create_text(
            1029.0,
            621.0,
            anchor="nw",
            text="17H AGO",
            fill="#C6C6C6",
            font=("Graphik Regular", 12 * -1))

        self.news_frame_canvas.create_text(
            1029.0,
            642.0,
            anchor="nw",
            text="This is a umlaut news article",
            fill="#F1F1F1",
            font=("Graphik Semibold", 24 * -1))

        self.news_frame_canvas.create_text(
            1029.0,
            675.0,
            anchor="nw",
            text="October is Cyber Security Awareness Month, and\na time to check out the latest cyber adventure Feel...",
            fill="#C6C6C6",
            font=("Graphik Regular", 14 * -1))
        
        self.news_frame_canvas.create_text(
            1029.0,
            715.0,
            anchor="nw",
            text="+ SEE MORE",
            fill="#008EFF",
            font=("Graphik Semibold", 12 * -1))

        
        


        

        #endregion

        # middle white line
        self.news_frame_canvas.create_rectangle(
            30.5,
            750.5,
            1476.0,
            751.0,
            fill="#3D3B48",
            outline="")

        #region under second line
        # left art
        self.button_image_article_1_nf = ImageTk.PhotoImage(self.panel_article_img_4)
        self.button_article_1_nf = Button(self.news_frame_canvas,
                text = "ar_1",
                bg = "#03000F",
                activebackground="#131116",
                image= self.button_image_article_1_nf ,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.article_frame(self.button_article_1_nf),
                relief="flat")
        
        self.button_article_1_nf.place(x=28, y=761, height=128, width=228)

        self.news_frame_canvas.create_text(
            282.0,
            771.0,
            anchor="nw",
            text="17H AGO",
            fill="#C6C6C6",
            font=("Graphik Regular", 12 * -1))
        
        self.news_frame_canvas.create_text(
            282.0,
            792.0,
            anchor="nw",
            text="This is a umlaut news article",
            fill="#F1F1F1",
            font=("Graphik Semibold", 24 * -1))

        self.news_frame_canvas.create_text(
            282.0,
            825.0,
            anchor="nw",
            text="October is Cyber Security Awareness Month, and\na time to check out the latest cyber adventure Feel...",
            fill="#C6C6C6",
            font=("Graphik Regular", 14 * -1))

        

        # right art

        self.button_image_article_2_nf = ImageTk.PhotoImage(self.panel_article_img_2)
        self.button_article_2_nf = Button(self.news_frame_canvas,
            text = "ar_2",
            bg = "#03000F",
            activebackground="#131116",
            image= self.button_image_article_2_nf,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.article_frame(self.button_article_2_nf),
            relief="flat")
        
        self.button_article_2_nf.place(x=775, y=761, height=128, width=228)

        self.news_frame_canvas.create_text(
            1029.0,
            771.0,
            anchor="nw",
            text="17H AGO",
            fill="#C6C6C6",
            font=("Graphik Regular", 12 * -1))

        self.news_frame_canvas.create_text(
            1029.0,
            792.0,
            anchor="nw",
            text="This is a umlaut news article",
            fill="#F1F1F1",
            font=("Graphik Semibold", 24 * -1))

        self.news_frame_canvas.create_text(
            1029.0,
            825.0,
            anchor="nw",
            text="October is Cyber Security Awareness Month, and\na time to check out the latest cyber adventure Feel...",
            fill="#C6C6C6",
            font=("Graphik Regular", 14 * -1))
        #endregion
        
        print("news frame")

    def portf_frame_gui(self):
        print("inportGUIIIII")

        #region Top part of portfolio
        # Text on top of the Portfolio tab
        self.portf_frame_canvas.create_text(
            24,
            22.0,
            anchor="nw",
            text="Our projects / training",
            fill="#FFFFFF",
            font=("Graphik Semibold", 24 * -1) )

        # Training button on top of portfolio frame
        self.button_image_training_pf = PhotoImage(file=os.path.join('assets',"button_training.png"))

        self.button_training_pf = Button(self.portf_frame_canvas,
            image=self.button_image_training_hf,
            bg = "#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_training clicked"),
            relief="flat") 

        self.button_training_pf.place(
            x=300,
            y=22.0,
            width=82.57275390625,
            height=34.077667236328125)

        # Demo button on top of portfolio frame
        self.button_image_demos_pf = PhotoImage(file=os.path.join('assets',"button_demos.png"))
        self.button_demos_pf = Button(self.portf_frame_canvas,
            image=self.button_image_demos_hf,
            bg = "#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_demos clicked"),
            relief="flat")

        self.button_demos_pf.place(
            x=395,
            y=22.0,
            width=82.57275390625,
            height=34.077667236328125)

        # Right top side button for List view
        self.button_image_sort1_pf = PhotoImage(file=os.path.join('assets',"button_sort1.png"))

        self.button_sort1_pf =  Button(self.portf_frame_canvas,
            image=self.button_image_sort1_pf,
            bg = "#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_sort1 clicked"),
            relief="flat")

        self.button_sort1_pf.place(
            x=1355,
            y=22.0,
            width=22,
            height=22)

        # Right top side button for Grid view
        self.button_image_sort2_pf = PhotoImage(file=os.path.join('assets',"button_sort2.png"))

        self.button_sort2_pf =  Button(self.portf_frame_canvas,
            image=self.button_image_sort2_pf,
            bg = "#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_sort2 clicked"),
            relief="flat")

        self.button_sort2_pf.place(
            x=1325,
            y=22.0,
            width=22,
            height=22)
        
        # Right top side button for Sort
        self.button_image_sort3_pf = PhotoImage(file=os.path.join('assets',"button_sort3.png"))

        self.button_sort3_pf =  Button(self.portf_frame_canvas,
            image=self.button_image_sort3_pf,
            bg = "#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_sort3 clicked"),
            relief="flat")

        self.button_sort3_pf.place(
            x=1385,
            y=22.0,
            width=22,
            height=22)

        # Right top side button for Sort by text
        self.portf_frame_canvas.create_text(
            1407.892578125,
            26.0,
            anchor="nw",
            text="SORT BY",
            fill="#FFFFFF",
            font=("Graphik Regular", 12 * -1))

        #endregion

        #region The following region shows how the projects should be defined, Distance between one project tile, text, threedot button on the one row to the next one is 363 pixels

        self.button_proj_firstrow_y = 100 -20
        self.button_proj_secondrow_y = 386-35
        self.button_proj_thirdrow_y = 672-35

        self.text_proj_firstrow_y = 305 -20
        self.text_proj_secondrow_y = 591-35
        self.text_proj_thirdrow_y = 877-35

        self.button_threedots_firstrow_y = 310 -20
        self.button_threedots_secondrow_y = 596-35
        self.button_threedots_thirdrow_y = 882-35

        #region project 1 First row on portfolio frame
        self.button_project_thumbnail_1_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_1_pf)
        self.button_project_1_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_1_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_1_pf),
            relief="flat")

        self.button_project_1_pf.place(
            x=21,
            y=self.button_proj_firstrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            21.0,
            self.text_proj_firstrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))
        

        # using the same image for threedots menu button that was used in home frame for articles
        self.button_pro_3dot_image = PhotoImage(file=os.path.join('assets',"button_threedots_1.png"))

        self.button_threedots_1_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_1_pf clicked"),
            relief="flat")

        self.button_threedots_1_pf.place(
            x=340.0,
            y=self.button_threedots_firstrow_y,
            width=27,
            height=27)
        #endregion

        #region project 2 on portfolio frame
        self.button_project_thumbnail_2_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_2_pf)
        self.button_project_2_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_2_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_2_pf),
            relief="flat")

        self.button_project_2_pf.place(
            x=383,
            y=self.button_proj_firstrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            384.0,
            self.text_proj_firstrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_2_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_2_pf clicked"),
            relief="flat")

        self.button_threedots_2_pf.place(
            x=703.0,
            y=self.button_threedots_firstrow_y,
            width=27,
            height=27)
        #endregion

        #region project 3 on portfolio frame
        self.button_project_thumbnail_3_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_3_pf)
        self.button_project_3_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_3_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_3_pf),
            relief="flat")

        self.button_project_3_pf.place(
            x=747,
            y=self.button_proj_firstrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            747.0,
            self.text_proj_firstrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_3_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_3_pf clicked"),
            relief="flat")

        self.button_threedots_3_pf.place(
            x=1066.0,
            y=self.button_threedots_firstrow_y,
            width=27,
            height=27)
        #endregion

        #region project 4 on portfolio frame
        self.button_project_thumbnail_4_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_4_pf)
        self.button_project_4_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_4_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_4_pf),
            relief="flat")

        self.button_project_4_pf.place(
            x=1110,
            y=self.button_proj_firstrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            1110.0,
            self.text_proj_firstrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_4_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_4_pf clicked"),
            relief="flat")

        self.button_threedots_4_pf.place(
            x=1429.0,
            y=self.button_threedots_firstrow_y,
            width=27,
            height=27)
        #endregion

        #region project 5 Second row on portfolio frame
        self.button_project_thumbnail_5_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_2_pf)
        self.button_project_5_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_5_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_5_pf),
            relief="flat")

        self.button_project_5_pf.place(
            x=21,
            y=self.button_proj_secondrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            21.0,
            self.text_proj_secondrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_5_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_5_pf clicked"),
            relief="flat")

        self.button_threedots_5_pf.place(
            x=340.0,
            y=self.button_threedots_secondrow_y,
            width=27,
            height=27)
        #endregion

        #region project 6 on portfolio frame
        self.button_project_thumbnail_6_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_6_pf)
        self.button_project_6_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_6_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_6_pf),
            relief="flat")

        self.button_project_6_pf.place(
            x=383,
            y=self.button_proj_secondrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            384.0,
            self.text_proj_secondrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_6_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_6_pf clicked"),
            relief="flat")

        self.button_threedots_6_pf.place(
            x=703.0,
            y=self.button_threedots_secondrow_y,
            width=27,
            height=27)
        #endregion

        #region project 7 on portfolio frame
        self.button_project_thumbnail_7_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_1_pf)
        self.button_project_7_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_7_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_7_pf),
            relief="flat")

        self.button_project_7_pf.place(
            x=747,
            y=self.button_proj_secondrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            747.0,
            self.text_proj_secondrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_7_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_7_pf clicked"),
            relief="flat")

        self.button_threedots_7_pf.place(
            x=1066.0,
            y=self.button_threedots_secondrow_y,
            width=27,
            height=27)
        #endregion

        #region project 8 on portfolio frame
        self.button_project_thumbnail_8_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_2_pf)
        self.button_project_8_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_8_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_8_pf),
            relief="flat")

        self.button_project_8_pf.place(
            x=1110,
            y=self.button_proj_secondrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            1110.0,
            self.text_proj_secondrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_8_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_8_pf clicked"),
            relief="flat")

        self.button_threedots_8_pf.place(
            x=1429.0,
            y=self.button_threedots_secondrow_y,
            width=27,
            height=27)
        #endregion

        #region project 9 Third row on portfolio frame
        self.button_project_thumbnail_9_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_3_pf)
        self.button_project_9_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_9_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_9_pf),
            relief="flat")

        self.button_project_9_pf.place(
            x=21,
            y=self.button_proj_thirdrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            21.0,
            self.text_proj_thirdrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_9_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_9_pf clicked"),
            relief="flat")

        self.button_threedots_9_pf.place(
            x=340.0,
            y=self.button_threedots_thirdrow_y,
            width=27,
            height=27)
        #endregion

        #region project 10 on portfolio frame
        self.button_project_thumbnail_10_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_4_pf)
        self.button_project_10_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_10_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_10_pf),
            relief="flat")

        self.button_project_10_pf.place(
            x=383,
            y=self.button_proj_thirdrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            384.0,
            self.text_proj_thirdrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_10_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_10_pf clicked"),
            relief="flat")

        self.button_threedots_10_pf.place(
            x=703.0,
            y=self.button_threedots_thirdrow_y,
            width=27,
            height=27)
        #endregion

        #region project 11 on portfolio frame
        self.button_project_thumbnail_11_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_1_pf)
        self.button_project_11_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_11_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_11_pf),
            relief="flat")

        self.button_project_11_pf.place(
            x=747,
            y=self.button_proj_thirdrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            747.0,
            self.text_proj_thirdrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_11_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_11_pf clicked"),
            relief="flat")

        self.button_threedots_11_pf.place(
            x=1066.0,
            y=self.button_threedots_thirdrow_y,
            width=27,
            height=27)
        #endregion

        #region project 12 on portfolio frame
        self.button_project_thumbnail_12_pf_ref = ImageTk.PhotoImage(self.button_project_thumbnail_6_pf)
        self.button_project_12_pf = Button(self.portf_frame_canvas,
            text="pr_1",
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_project_thumbnail_12_pf_ref,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.project_frame(self.button_project_12_pf),
            relief="flat")

        self.button_project_12_pf.place(
            x=1110,
            y=self.button_proj_thirdrow_y,
            width=354,
            height=199)

        self.portf_frame_canvas.create_text(
            1110.0,
            self.text_proj_thirdrow_y,
            anchor="nw",
            text="Across Accenture\nYour inbox will never\nbe the same!",
            fill="#FFFFFF",
            font=("UmlautTilde Black", 13 * -1))

        self.button_threedots_12_pf = Button(self.portf_frame_canvas,
            bg = "#03000F",
            activebackground="#131116",
            image=self.button_pro_3dot_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_threedots_12_pf clicked"),
            relief="flat")

        self.button_threedots_12_pf.place(
            x=1429.0,
            y=self.button_threedots_thirdrow_y,
            width=27,
            height=27)
        #endregion
        #endregion
        self.something = []


    def article_frame_gui(self, selected_article):
        #print("button_main_article_hf clicked")
        print(selected_article.cget("text") + " clicked")

        article_list = ["ar_main", "ar_1", "ar_2", "ar_3"]

        # checking which article is opened and putting the main image of selected article
        if selected_article.cget("text") == "ar_main":
            self.opened_article_thumbnail_ref = ImageTk.PhotoImage(self.opened_article_img_main)
        elif selected_article.cget("text") == "ar_1":
            self.opened_article_thumbnail_ref = ImageTk.PhotoImage(self.opened_article_img_1)
        elif selected_article.cget("text") == "ar_2":
            self.opened_article_thumbnail_ref = ImageTk.PhotoImage(self.opened_article_img_2)
        elif selected_article.cget("text") == "ar_3":
            self.opened_article_thumbnail_ref = ImageTk.PhotoImage(self.opened_article_img_3)

        # Article UI 
        #region

        #self.opened_article_thumbnail_ref = PhotoImage(file=os.path.join('assets',"article_main_main_image.png"))
        self.opened_article_thumbnail = self.article_frame_canvas.create_image(
            386.0,
            231.0,
            image=self.opened_article_thumbnail_ref)

        #self.opened_article_thumbnail = Label(self.article_fr, image=self.opened_article_thumbnail_ref, )
        #self.opened_article_thumbnail.place(x = 386, y=231)

        # Time text for main article
        self.article_frame_canvas.create_text(
            31.0,
            456.0,
            anchor="nw",
            text="17H AGO",
            fill="#C6C6C6",
            font=("Graphik Regular", 12 * -1))

        # Main article title Text
        self.article_frame_canvas.create_text(
            31.0,
            477.0,
            anchor="nw",
            text="This is a umlaut news article",
            fill="#F1F1F1",
            font=("Graphik Semibold", 24 * -1))

        # Main article content text
        main_content_text = ("October is Cyber Security Awareness Month, and a time to check out the latest\n"
                            "cyber adventure Feel. It’s the annual International Day for Disaster Risk Reduction\n" 
                            "(IDDRR). In recognition of this important. Lorem ipsum dolor sit amet, consetetur\n" 
                            "sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore\n"
                            "magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo \n"
                            "dolores et ea rebum.\n\n" 
                            "Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.\n" 
                            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod\n" 
                            "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At\n"
                            "vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,\n" 
                            "no sea takimata sanctus est Lorem ipsum dolor sit amet.\n\n"
                            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod\n"
                            "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At\n" 
                            "vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,\n" 
                            "no sea takimata sanctus est Lorem ipsum dolor sit amet\n")
            
        self.article_frame_canvas.create_text(
            31.0,
            510.0,
            anchor="nw",
            text=main_content_text,
            #text="October is Cyber Security Awareness Month, and a time to check out the latest\n cyber adventure Feel. It’s the annual International Day for Disaster Risk Reduction (IDDRR). In recognition of this important. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.\n\nStet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.\n\nLorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet",
            fill="#C6C6C6",
            font=("Graphik Regular", 14 * -1))
        #endregion

        # Side bar articles UI
        # Time text on the side bar articles
        self.article_frame_canvas.create_text(
            1028.0,
            32.0,
            anchor="nw",
            text="17H AGO",
            fill="#C6C6C6",
            font=("Graphik Regular", 12 * -1))


        # image_image_3 = PhotoImage(file=os.path.join('assets',"image_3.png")) 

        # image_3 = canvas.create_image(
        #     893.0,
        #     96.0,
        #     image=image_image_3)

        self.start_x = 779
        self.start_y = 32
        self.side_panel_thumbnail_width = 228
        self.side_panel_thumbnail_height = 128
        self.something = False

        # self.button_article_1_hf = Button(self.article_frame_canvas,
        #     text="ar_1",
        #     bg = "#03000F",
        #     activebackground="#131116",
        #     image=self.button_article_thumbnail_1_hf,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.article_frame(self.button_article_1_hf),
        #     relief="flat")
        
        # self.button_article_1_hf.place(x=779, y = 32, width=228, height=128)

        self.original_y = 32
        self.original_text = 86
        self.original_title = 53
        self.panel_article_img_main_resized =  ImageTk.PhotoImage(self.panel_article_img_main)
        self.panel_article_img_1_resized =  ImageTk.PhotoImage(self.panel_article_img_1)
        self.panel_article_img_2_resized =  ImageTk.PhotoImage(self.panel_article_img_2)
        self.panel_article_img_3_resized =  ImageTk.PhotoImage(self.panel_article_img_3)



        self.mylist = [self.panel_article_img_main_resized, self.panel_article_img_1_resized, self.panel_article_img_2_resized, self.panel_article_img_3_resized]
        

        for i in range(len(article_list)):
            if selected_article.cget("text") == article_list[i]:
                #article_list.pop(article)
                self.mylist.pop(i)
                print(self.mylist)


        print(self.mylist)
        for a in self.mylist:
            
            self.panel_buttons = Button(self.article_frame_canvas,
                bg = "#03000F",
                activebackground="#131116",
                image=a,
                borderwidth=0,
                highlightthickness=0,
                #command=lambda: self.article_frame(self.panel_buttons),
                relief="flat")
            
            self.panel_buttons.place(x=779, y = self.original_y, width=228, height=128)
            self.original_y= self.original_y+166

            self.article_frame_canvas.create_text(
                1028.0,
                self.original_text,
                anchor="nw",
                text="October is Cyber Security Awareness Month, and a time to check out the latest cyber adventure Feel...",
                fill="#C6C6C6",
                font=("Graphik Regular", 14 * -1))

            self.article_frame_canvas.create_text(
                1028.0,
                self.original_title,
                anchor="nw",
                text="This is a umlaut news article",
                fill="#F1F1F1",
                font=("Graphik Semibold", 24 * -1))
            
            self.original_text = self.original_text+ 167
            self.original_title = self.original_title + 167

    def project_frame_gui(self, selected_project):
        print("hello")

        # region project main page images 
        # Project title text on top
        self.project_frame_canvas.create_text(
            33.0,
            27.0,
            anchor="nw",
            text="umlaut Breakdown Tool",
            fill="#FFFFFF",
            font=("Graphik Semibold", 40 * -1))

        # Image forward button
        self.button_image_imforward = PhotoImage(
            file=os.path.join('assets',"button_imforward.png"))
        self.button_imforward = Button(self.project_frame_canvas,
            image=self.button_image_imforward,
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.img_forward(2),
            relief="flat")

        self.button_imforward.place(
            x=935.0,
            y=699.0,
            width=33.0,
            height=33.0)

        # Image back button
        self.button_image_imback = PhotoImage(
            file=os.path.join('assets',"button_imback.png"))
        self.button_imback = Button(self.project_frame_canvas,
            image=self.button_image_imback,
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self.img_back(self),
            relief="flat", state="disabled")

        self.button_imback.place(
            x=46.0,
            y=699.0,
            width=33.0,
            height=33.0)

                #define all the images 

        self.project_im1 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_1.jpg").resize((945,532)))
        self.project_im2 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_2.jpg").resize((945,532)))
        self.project_im3 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_3.jpg").resize((945,532)))
        self.project_im4 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_4.jpg").resize((945,532)))
        self.project_im5 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_5.jpg").resize((945,532)))

        self.project_im_list = [self.project_im1, self.project_im2, self.project_im3, self.project_im4, self.project_im5]
        
        self.project_small_im1 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_1.jpg").resize((140,79)))
        self.project_small_im2 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_2.jpg").resize((140,79)))
        self.project_small_im3 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_3.jpg").resize((140,79)))
        self.project_small_im4 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_4.jpg").resize((140,79)))
        self.project_small_im5 = ImageTk.PhotoImage(Image.open(self.images_path +"Breakdowntool_5.jpg").resize((140,79)))

        self.project_im_small_list = [self.project_small_im1, self.project_small_im2, self.project_small_im3, self.project_small_im4, self.project_small_im5]

        #self.project_im1 = self.project_im1.resize((945,532))
        self.project_image_big = Label(self.project_frame_canvas, image=self.project_im1, borderwidth=0,)
        self.project_image_big.place(x=32,y=127)

        self.project_image_small = Label(self.project_frame_canvas, image=self.project_small_im1, borderwidth=0,)
        self.project_image_small.place(x=96,y=675)
        self.project_image_small = Label(self.project_frame_canvas, image=self.project_small_im2, borderwidth=0,)
        self.project_image_small.place(x=262,y=675)
        self.project_image_small = Label(self.project_frame_canvas, image=self.project_small_im3, borderwidth=0,)
        self.project_image_small.place(x=428,y=675)
        self.project_image_small = Label(self.project_frame_canvas, image=self.project_small_im4, borderwidth=0,)
        self.project_image_small.place(x=594,y=675)
        self.project_image_small = Label(self.project_frame_canvas, image=self.project_small_im5, borderwidth=0,)
        self.project_image_small.place(x=760,y=675)
        #endregion

        #region Project frame side panel texts, images, buttons

        # umlaut logo project frame
        self.project_image_ref_umlsym = PhotoImage(file=os.path.join('assets',"umlaut_logo_project.png"))
        self.project_image_umlsym = self.project_frame_canvas.create_image(
            1268.0,
            127.0,
            image=self.project_image_ref_umlsym)


        # Project title text on the right
        self.project_frame_canvas.create_text(
            1045.0,
            223.0,
            anchor="nw",
            text="umlaut Breakdown Tool",
            fill="#FFFFFF",
            font=("Graphik Semibold", 40 * -1))

        # Project description text
        self.project_frame_canvas.create_text(
            1054.0,
            282.0,
            anchor="nw",
            text="Lorem ipsum dolor sit amet, consetetur sadipscing?\n eirmod tempor invidunt ut labore et dolore magna aliqu-\n yam erat, sed diam voluptua. At vero eos et\n accusam et justo duo dolores et ea rebum. ",
            fill="#C7C7C7",
            font=("Graphik Light", 16 * -1))

        
        self.project_frame_canvas.create_text(
            1057.0,
            590.0,
            anchor="nw",
            text="Developer",
            fill="#FFFFFF",
            font=("Graphik Regular", 16 * -1))

        # Name of the developer
        self.project_frame_canvas.create_text(
            1391.0,
            590.0,
            anchor="nw",
            text="Mehmet Yavuz",
            fill="#FFFFFF",
            font=("Graphik Semibold", 16 * -1))

        # Publisher name
        self.project_frame_canvas.create_text(
            1391.0,
            649.0,
            anchor="nw",
            text="Martin Willam",
            fill="#FFFFFF",
            font=("Graphik Semibold", 16 * -1))

        # Availability
        self.project_frame_canvas.create_text(
            1391.0,
            703.0,
            anchor="nw",
            text="Sebastian",
            fill="#FFFFFF",
            font=("Graphik Semibold", 16 * -1))

        self.project_frame_canvas.create_text(
            1057.0,
            649.0,
            anchor="nw",
            text="Publisher",
            fill="#FFFFFF",
            font=("Graphik Regular", 16 * -1))

        self.project_frame_canvas.create_text(
            1057.0,
            705.0,
            anchor="nw",
            text="Available",
            fill="#FFFFFF",
            font=("Graphik Regular", 16 * -1))

        self.project_frame_canvas.create_text(
            1057.0,
            752.0,
            anchor="nw",
            text="Platform",
            fill="#FFFFFF",
            font=("Graphik Regular", 16 * -1))
        
        
        # Add to library button
        self.button_image_project_addlib = PhotoImage(file=os.path.join('assets',"add_to_library.png"))

        self.button_project_addlib = Button(self.project_frame_canvas,
            image=self.button_image_project_addlib,
            bg="#03000F",
            activebackground="#131116",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("add_to_library clicked"),
            relief="flat")

        self.button_project_addlib.place(
            x=1050.0,
            y=393.0,
            width=437.0,
            height=56.0)


        # TODO
        self.button_image_project_install = PhotoImage(file=os.path.join('assets',"install_project.png"))

        self.button_project_install = Button(self.project_frame_canvas,
            image=self.button_image_project_install,
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.download_package_thread('22-09-01-Hafex-V1.7z'),
            relief="flat")

        self.button_project_install.place(
            x=1050.0,
            y=459.0,
            width=437.0,
            height=56.0)

        # Launch Button        
        self.button_image_project_launch = PhotoImage(file=os.path.join('assets',"launch_project.png"))

        self.button_project_launch = Button(self.project_frame_canvas,
            image=self.button_image_project_launch,
            text = "Launch",
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.launch_game(),
            relief="flat")

        self.button_project_launch.place(
            x=1050.0,
            y=525.0,
            width=437.0,
            height=56.0)

        #endregion
        #something
        self.something = []
        self.downloading_image  = PhotoImage(file=os.path.join('assets',"downloading.png"))
        
        self.downloading_button = Button(self.project_frame_canvas,
            image=self.downloading_image,
            text = "Launch",
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.downloaded_image  = PhotoImage(file=os.path.join('assets',"downloaded.png"))
        self.downloaded_button = Button(self.project_frame_canvas,
            image=self.downloaded_image,
            text = "Launch",
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            relief="flat")
        
    def img_forward(self, image_number):
        self.project_image_big.place_forget()
        self.project_image_big = Label(self.project_frame_canvas, image=self.project_im_list[image_number-1], borderwidth=0)
        self.project_image_big.place(x=32,y=127)

        self.button_imforward = Button(self.project_frame_canvas,
            image=self.button_image_imforward,
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.img_forward(image_number+1),
            relief="flat")

        self.button_imforward.place(
            x=935.0,
            y=699.0,
            width=33.0,
            height=33.0)

        self.button_imback = Button(self.project_frame_canvas,
            image=self.button_image_imback,
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.img_back(image_number-1),
            relief="flat")

        self.button_imback.place(
            x=46.0,
            y=699.0,
            width=33.0,
            height=33.0)
        
        if image_number == len(self.project_im_list):
            print("loooop")
            self.button_imforward.configure(state="disabled")

        print("forward")

    def img_back(self, image_number):
        self.project_image_big.place_forget()
        self.project_image_big = Label(self.project_frame_canvas, image=self.project_im_list[image_number-1], borderwidth=0,)
        self.project_image_big.place(x=32,y=127)

        self.button_imforward = Button(self.project_frame_canvas,
            image=self.button_image_imforward,
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.img_forward(image_number+1),
            relief="flat")

        self.button_imforward.place(
            x=935.0,
            y=699.0,
            width=33.0,
            height=33.0)

        self.button_imback = Button(self.project_frame_canvas,
            image=self.button_image_imback,
            bg="#03000F",
            activebackground="#03000F",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.img_back(image_number-1),
            relief="flat")

        self.button_imback.place(
            x=46.0,
            y=699.0,
            width=33.0,
            height=33.0)
        
        if image_number == 1:
            print("loooop")
            self.button_imback.configure(state="disabled")
        print("back")
    
    def check_downloads(self):
        if os.path.exists(os.path.join('data','22-09-01-Hafex-V2')):
            self.downloaded_button.place(
            x=1050.0,
            y=459.0,
            width=437.0,
            height=56.0)
            self.button_project_launch['state'] = 'active'
        print('package found')
        self.screen.after(2000, self.check_downloads)

    
    def launch_game(self):
        game_path = os.path.join('data','22-09-01-Hafex-V2','Hafex_UE5.exe')
        subprocess.Popen(game_path)


        
        




        



    