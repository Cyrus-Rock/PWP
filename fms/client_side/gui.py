"""The module for tkinter and client side functionality"""
import tkinter as tk
from tkinter import font
import gui_functions
from PIL import Image, ImageTk
#from tkinter import ttk
#import os

# Top bar creation function
def create_top_bar(self, color):
    """Creating a pseudo top bar"""
    justifier = ' ' * 193
    button_bar = tk.Button(self,
    # An EXTREMELY janky solution, change in the future
    text = "🌠 Generic GUI" + justifier,
    bg = color,
    fg = '#ffffff',
    bd = 0,
    font = font.Font(family='Helvetica', size=18),
    height = 1,
    width = 172)
    button_bar.pack()

# Border creation function
def create_border(self, color):
    """Creating a pseudo border"""
    button_border = tk.Button(self,
    # A janky solution
    text = " ",
    bg = color,
    fg = '#ffffff',
    bd = 0,
    font= font.Font(family='Helvetica', size=18),
    height = 20,
    width =26)
    button_border.pack()
    button_border.place(bordermode=tk.OUTSIDE, x=790, y=102)

def show_image(self, boolean):
    """Displaying an image"""
    image = Image.open("../images/plane.png")
    image_test = ImageTk.PhotoImage(image)
    image_label = tk.Label(self, image=image_test)
    image_label.image = image_test
    # Adjusting the position of the image
    if boolean is True:
        image_label.place(bordermode=tk.OUTSIDE, x=820, y=130)

title_font =("Helvetica", 35)

class tkinterApp(tk.Tk):
    """The class used for the tkinter implementation"""
    # Initializations
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Setting the name and resolution
        self.title("Generic GUI PWP")
        self.geometry("1920x1080")

        # Here we create a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Creating an empty array for pages
        self.pages = {}

        # Here we iterate through a tupple of possible pages, starting with the first page
        for F in (a1, b1, b1_c2, b1_c3, b1_c4, b2, b2_c2, b2_c3, b2_c4, b2_c5,
        b3, b3_c2, b3_c3, b3_c4, b3_c5, b4, b4_c1, b5, b5_c2):
            frame = F(container, self)
            self.pages[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(a1)

    def show_frame(self, cont):
        """This is used to display a new page"""
        show_image(self, False)
        frame = self.pages[cont]
        frame.tkraise()

class a1(tk.Frame):
    """The starting page for our GUI"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        create_top_bar(self, '#eb4f34')
        create_border(self, '#eb4f34')
        show_image(self, True)

        # Defining the buttons
        button_a1 = tk.Button(self, text ="Access the seat resource", height=2, width=40,
        background='#eb4f34', fg='white', command = lambda : controller.show_frame(b1))
        button_a2 = tk.Button(self, text ="Access the client resource", height=2, width=40,
        background='#eb4f34', fg='white', command = lambda : controller.show_frame(b2))
        button_a3 = tk.Button(self, text ="Access the plane resource", height=2, width=40,
        background='#eb4f34', fg='white', command = lambda : controller.show_frame(b3))
        button_a4 = tk.Button(self, text ="Access the offer resource", height=2, width=40,
        background='#eb4f34', fg='white', command = lambda : controller.show_frame(b4))
        button_a5 = tk.Button(self, text ="Access the flight resource", height=2, width=40,
        background='#eb4f34', fg='white', command = lambda : controller.show_frame(b5))

        # Packing and placing the buttons
        button_a1.pack()
        button_a1.place(bordermode=tk.OUTSIDE, x=140, y=150+50)
        button_a2.pack()
        button_a2.place(bordermode=tk.OUTSIDE, x=140, y=230+50)
        button_a3.pack()
        button_a3.place(bordermode=tk.OUTSIDE, x=140, y=310+50)
        button_a4.pack()
        button_a4.place(bordermode=tk.OUTSIDE, x=140, y=390+50)
        button_a5.pack()
        button_a5.place(bordermode=tk.OUTSIDE, x=140, y=470+50)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

class b1(tk.Frame):
    """"The seat page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=110+50)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        create_top_bar(self, '#2461f0')

        # Defining the buttons
        button_b1_c1 = tk.Button(self, text ="View the information for all the seats",
        height=2, width=40,
        background='#2461f0', fg='white',
        command = lambda : gui_functions.view_all_seat(text_box))
        button_b1_c2 = tk.Button(self, text ="Get the information for a specific seat",
        height=2, width=40,
        background='#2461f0', fg='white', command = lambda : controller.show_frame(b1_c2))
        button_b1_c3 = tk.Button(self, text ="Delete the information for a specific seat",
        height=2, width=40,
        background='#2461f0', fg='white', command = lambda : controller.show_frame(b1_c3))
        button_b1_c4 = tk.Button(self, text ="Create a new seat", height=2, width=40,
        background='#2461f0', fg='white', command = lambda : controller.show_frame(b1_c4))
        button_b1_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#2461f0', fg='white', command = lambda : controller.show_frame(a1))

        # Packing and placing the buttons
        button_b1_c1.pack()
        button_b1_c1.place(bordermode=tk.OUTSIDE, x=140, y=150+50)
        button_b1_c2.pack()
        button_b1_c2.place(bordermode=tk.OUTSIDE, x=140, y=230+50)
        button_b1_c3.pack()
        button_b1_c3.place(bordermode=tk.OUTSIDE, x=140, y=310+50)
        button_b1_c4.pack()
        button_b1_c4.place(bordermode=tk.OUTSIDE, x=140, y=390+50)
        button_b1_back.pack()
        button_b1_back.place(bordermode=tk.OUTSIDE, x=140, y=470+50)

        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=110+50)

class b2(tk.Frame):
    """The client page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=110+50)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        create_top_bar(self, '#20a124')

        # Defining the buttons
        button_b2_c1 = tk.Button(self, text ="View the information for all the clients",
        height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : gui_functions.view_all_client(text_box))
        button_b2_c2 = tk.Button(self, text ="Get the information for a specific client",
        height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : controller.show_frame(b2_c2))
        button_b2_c3 = tk.Button(self, text ="Create a new client", height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : controller.show_frame(b2_c3))
        button_b2_c4 = tk.Button(self, text ="Delete the information for a specific client",
        height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : controller.show_frame(b2_c4))
        button_b2_c5 = tk.Button(self, text ="Update the information for a specific client",
        height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : controller.show_frame(b2_c5))
        button_b2_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : controller.show_frame(a1))

        # Packing and placing the buttons
        button_b2_c1.pack()
        button_b2_c1.place(bordermode=tk.OUTSIDE, x=140, y=150+50)
        button_b2_c2.pack()
        button_b2_c2.place(bordermode=tk.OUTSIDE, x=140, y=230+50)
        button_b2_c3.pack()
        button_b2_c3.place(bordermode=tk.OUTSIDE, x=140, y=310+50)
        button_b2_c4.pack()
        button_b2_c4.place(bordermode=tk.OUTSIDE, x=140, y=390+50)
        button_b2_c5.pack()
        button_b2_c5.place(bordermode=tk.OUTSIDE, x=140, y=470+50)
        button_b2_back.pack()
        button_b2_back.place(bordermode=tk.OUTSIDE, x=140, y=550+50)

class b3(tk.Frame):
    """The plane page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=110+50)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        create_top_bar(self, 'orange')

        # Defining the buttons
        button_b3_c1 = tk.Button(self, text ="View the information for all the planes",
        height=2, width=40,
        background='orange', fg='white',
        command = lambda : gui_functions.view_all_plane(text_box))
        button_b3_c2 = tk.Button(self, text ="Get the information for a specific plane",
        height=2, width=40,
        background='orange', fg='white',
        command = lambda : controller.show_frame(b3_c2))
        button_b3_c3 = tk.Button(self, text ="Create a new plane", height=2, width=40,
        background='orange', fg='white',
        command = lambda : controller.show_frame(b3_c3))
        button_b3_c4 = tk.Button(self, text ="Delete the information for a specific plane",
        height=2, width=40,
        background='orange', fg='white',
        command = lambda : controller.show_frame(b3_c4))
        button_b3_c5 = tk.Button(self, text ="Update the information for a specific plane",
        height=2, width=40,
        background='orange', fg='white',
        command = lambda : controller.show_frame(b3_c5))
        button_b3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='orange', fg='white',
        command = lambda : controller.show_frame(a1))

        # Packing and placing the buttons
        button_b3_c1.pack()
        button_b3_c1.place(bordermode=tk.OUTSIDE, x=140, y=150+50)
        button_b3_c2.pack()
        button_b3_c2.place(bordermode=tk.OUTSIDE, x=140, y=230+50)
        button_b3_c3.pack()
        button_b3_c3.place(bordermode=tk.OUTSIDE, x=140, y=310+50)
        button_b3_c4.pack()
        button_b3_c4.place(bordermode=tk.OUTSIDE, x=140, y=390+50)
        button_b3_c5.pack()
        button_b3_c5.place(bordermode=tk.OUTSIDE, x=140, y=470+50)
        button_b3_back.pack()
        button_b3_back.place(bordermode=tk.OUTSIDE, x=140, y=550+50)

class b4(tk.Frame):
    """The offer page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        create_top_bar(self, '#8b32c2')
        create_border(self, '#8b32c2')
        show_image(self, True)

        # Defining the buttons
        button_b4_c1 = tk.Button(self, text ="Get the information for a specific offer",
        height=2, width=40,
        background='#8b32c2', fg='white', command = lambda : controller.show_frame(b4_c1))
        button_b4_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#8b32c2', fg='white', command = lambda : controller.show_frame(a1))

        # Packing and placing the buttons
        button_b4_c1.pack()
        button_b4_c1.place(bordermode=tk.OUTSIDE, x=140, y=150+50)
        button_b4_back.pack()
        button_b4_back.place(bordermode=tk.OUTSIDE, x=140, y=230+50)

        #text_box = tk.Text(self, height=30, width=105)
        #text_box.place(x=530, y=110+50)

class b5(tk.Frame):
    """The flight page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=110+50)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        create_top_bar(self, '#b04f46')

        # Defining the buttons
        button_b5_c1 = tk.Button(self, text ="View the information for all flights",
        height=2, width=40,
        background='#b04f46', fg='white',
        command = lambda : gui_functions.view_all_flight(text_box))
        button_b5_c2 = tk.Button(self, text ="Get the information for a specific flight",
        height=2, width=40,
        background='#b04f46', fg='white', command = lambda : controller.show_frame(b5_c2))
        button_b5_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#b04f46', fg='white', command = lambda : controller.show_frame(a1))

        # Packing and placing the buttons
        button_b5_c1.pack()
        button_b5_c1.place(bordermode=tk.OUTSIDE, x=140, y=150+50)
        button_b5_c2.pack()
        button_b5_c2.place(bordermode=tk.OUTSIDE, x=140, y=230+50)
        button_b5_back.pack()
        button_b5_back.place(bordermode=tk.OUTSIDE, x=140, y=310+50)

class b4_c1(tk.Frame):
    """The page for a specific offer"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=80)
        entry1.insert(1, "Replace this with the"
        " token of the client you wish to see the infromation for this offer")

        entry2 = tk.Entry(self, width=140)
        entry2.place(x=530, y=120)
        entry2.insert(1, "Replace this with the"
        " origin")

        entry3 = tk.Entry(self, width=140)
        entry3.place(x=530, y=160)
        entry3.insert(1, "Replace this with the"
        " destination")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=200)

        create_top_bar(self, '#8b32c2')

        # Defining the buttons
        button_b5_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#8b32c2', fg='white',
        command = lambda : gui_functions.get_offer(entry1.get(),
        entry2.get(), entry3.get(), text_box))
        button_b5_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#8b32c2', fg='white',
        command = lambda : controller.show_frame(b4))

        # Packing and placing the buttons
        button_b5_enter.pack()
        button_b5_enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_b5_back.pack()
        button_b5_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b5_c2(tk.Frame):
    """The page for a specific flight"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=80)
        entry1.insert(1, "Replace this with the"
        " origin")

        entry2 = tk.Entry(self, width=140)
        entry2.place(x=530, y=120)
        entry2.insert(1, "Replace this with the"
        " destination")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=160)

        create_top_bar(self, '#b04f46')

        # Defining the buttons
        button_b5_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#b04f46', fg='white',
        command = lambda : gui_functions.get_flight(entry1.get(), entry2.get(), text_box))
        button_b5_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#b04f46', fg='white',
        command = lambda : controller.show_frame(b5))

        # Packing and placing the buttons
        button_b5_enter.pack()
        button_b5_enter.place(bordermode=tk.OUTSIDE, x=800, y=665)
        button_b5_back.pack()
        button_b5_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b3_c2(tk.Frame):
    """The page for a specific plane"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=120)
        entry1.insert(1, "Replace this with the"
        " plane's id you wish to see the infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=160)

        create_top_bar(self, 'orange')

        # Defining the buttons
        button_b3_c2_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='orange', fg='white',
        command = lambda : gui_functions.get_plane(entry1.get(), text_box))
        button_b3_c2_back = tk.Button(self, text ="Back", height=2, width=40,
        background='orange', fg='white',
        command = lambda : controller.show_frame(b3))

        # Packing and placing the buttons
        button_b3_c2_enter.pack()
        button_b3_c2_enter.place(bordermode=tk.OUTSIDE, x=800, y=665)
        button_b3_c2_back.pack()
        button_b3_c2_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b3_c3(tk.Frame):
    """The page for plane creation"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=146)
        entry1.place(x=530, y=80)
        entry1.insert(1, "Replace this with the"
        " name for the plane")

        entry2 = tk.Entry(self, width=146)
        entry2.place(x=530, y=120)
        entry2.insert(1, "Replace this with the"
        " current location for the plane")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=160)

        create_top_bar(self, 'orange')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='orange', fg='white',
        command = lambda : gui_functions.post_plane(entry1.get(),
        entry2.get(), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='orange', fg='white', command = lambda : controller.show_frame(b3))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=665)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b3_c4(tk.Frame):
    """The page for plane deletion"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=120)
        entry1.insert(1, "Replace this with the"
        " plane's id you wish to delete the infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=160)

        create_top_bar(self, 'orange')

        # Defining the buttons
        button_b3_c2_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='orange', fg='white',
        command = lambda : gui_functions.delete_plane(entry1.get(), text_box))
        button_b3_c2_back = tk.Button(self, text ="Back", height=2, width=40,
        background='orange', fg='white',
        command = lambda : controller.show_frame(b3))

        # Packing and placing the buttons
        button_b3_c2_enter.pack()
        button_b3_c2_enter.place(bordermode=tk.OUTSIDE, x=800, y=665)
        button_b3_c2_back.pack()
        button_b3_c2_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b3_c5(tk.Frame):
    """The page for plane updating"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=146)
        entry1.place(x=530, y=80)
        entry1.insert(1, "Replace this with the"
        " plane's id you want to update")

        entry2 = tk.Entry(self, width=146)
        entry2.place(x=530, y=120)
        entry2.insert(1, "Replace this with a new name for the plane")

        entry3 = tk.Entry(self, width=146)
        entry3.place(x=530, y=160)
        entry3.insert(1, "Replace this with a new location for the plane")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        create_top_bar(self, 'orange')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='orange', fg='white',
        command = lambda : gui_functions.put_plane(entry1.get(),
        entry2.get(), entry3.get(), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='orange', fg='white', command = lambda : controller.show_frame(b3))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b2_c2(tk.Frame):
    """The page for a specific client"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=120)
        entry1.insert(1, "Replace this with the"
        " token of the client you wish to see the infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=160)

        create_top_bar(self, '#20a124')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : gui_functions.get_client(entry1.get(), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : controller.show_frame(b2))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=665)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b2_c3(tk.Frame):
    """The page for new client creation"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=80)
        entry1.insert(1, "Replace this with the"
        " token for the client")

        entry2 = tk.Entry(self, width=140)
        entry2.place(x=530, y=120)
        entry2.insert(1, "Replace this with the"
        " name for the client")

        entry3 = tk.Entry(self, width=140)
        entry3.place(x=530, y=160)
        entry3.insert(1, "Replace this with the"
        " surname for the client")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        create_top_bar(self, '#20a124')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : gui_functions.post_client(entry1.get(),
        entry2.get(), entry3.get(), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#20a124', fg='white', command = lambda : controller.show_frame(b2))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b2_c4(tk.Frame):
    """The page for client info deletion"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=120)
        entry1.insert(1, "Replace this with the"
        " token of the client you wish to delete the information for")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=160)

        create_top_bar(self, '#20a124')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : gui_functions.delete_client(entry1.get(), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : controller.show_frame(b2))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=665)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b2_c5(tk.Frame):
    """The page for changing client info"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry0 = tk.Entry(self, width=140)
        entry0.place(x=530, y=40+40)
        entry0.insert(1, "Replace this with the"
        " token for the client")

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=80+40)
        entry1.insert(1, "Replace this with the"
        " new name for the client")

        entry2 = tk.Entry(self, width=140)
        entry2.place(x=530, y=120+40)
        entry2.insert(1, "Replace this with the"
        " new surname for the client")

        entry3 = tk.Entry(self, width=140)
        entry3.place(x=530, y=160+40)
        entry3.insert(1, "Replace this with the"
        " new token for the client")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200+40)

        create_top_bar(self, '#20a124')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#20a124', fg='white',
        command = lambda : gui_functions.put_client(entry0.get(),
        entry1.get(), entry2.get(), entry3.get(), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#20a124', fg='white', command = lambda : controller.show_frame(b2))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=700+40)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b1_c2(tk.Frame):
    """The page for a specific seat"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=120)
        entry1.insert(1, "Replace this with the"
        " plane's id you wish to see the seat infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=160)

        create_top_bar(self, '#2461f0')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#2461f0', fg='white',
        command = lambda : gui_functions.get_seat(entry1.get(), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#2461f0', fg='white',
        command = lambda : controller.show_frame(b1))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=665)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b1_c3(tk.Frame):
    """The page for seat info deletion"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=120)
        entry1.insert(1, "Replace this with the"
        " plane's id you wish to delete the seat infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=160)

        create_top_bar(self, '#2461f0')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#2461f0', fg='white',
        command = lambda : gui_functions.delete_seat(entry1.get(), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#2461f0', fg='white',
        command = lambda : controller.show_frame(b1))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=665)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

class b1_c4(tk.Frame):
    """The page for new seat information"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating and placing text sections
        label1 = tk.Label(self, text = "Your options are:")
        label1.config(font =("Helvetica", 14))
        label1.place(x=140, y=140)

        entry1 = tk.Entry(self, width=140)
        entry1.place(x=530, y=80)
        entry1.insert(1, "Replace this with the"
        " plane's id you wish to add new seat infromation")

        entry2 = tk.Entry(self, width=140)
        entry2.place(x=530, y=120)
        entry2.insert(1, "Replace this with the"
        " types of the seat seperated by comma (,)")

        entry3 = tk.Entry(self, width=140)
        entry3.place(x=530, y=160)
        entry3.insert(1, "Replace this with the"
        " capacities of the seats' type seperated by comma (,)")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        create_top_bar(self, '#2461f0')

        # Defining the buttons
        button_b3_c3_enter = tk.Button(self, text ="Enter", height=2, width=40,
        background='#2461f0', fg='white',
        command = lambda : gui_functions.post_seat(entry1.get(),
        list(map(lambda x: x.strip(), entry2.get().split(','))),list(map(lambda x: x.strip(),
        entry3.get().split(','))), text_box))
        button_b3_c3_back = tk.Button(self, text ="Back", height=2, width=40,
        background='#2461f0', fg='white', command = lambda : controller.show_frame(b1))

        # Packing and placing the buttons
        button_b3_c3_enter.pack()
        button_b3_c3_enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_b3_c3_back.pack()
        button_b3_c3_back.place(bordermode=tk.OUTSIDE, x=140, y=150+50)

# Main loop
app = tkinterApp()
app.mainloop()
