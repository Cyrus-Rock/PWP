import tkinter as tk
from access import Access
import GUI_functions
#from PIL import Image, ImageTk
#from tkinter import ttk
#import os

title_font =("Helvetica", 35)
  
class tkinterApp(tk.Tk):
     
    # Initializations
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Setting the name and resolution
        self.title("Generic GUI PWP")
        self.geometry("1920x1080")

        # Creating the menu bar
        menubar = tk.Menu(self, background='#454545', fg='white')
        # Placing the menu element
        file = tk.Menu(menubar, tearoff=False)
        # Placing commands for the menu bar
        file.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="GENERIC GUI", menu=file)
        self.config(menu=menubar)
         
        # Here we create a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # Creating an empty array for pages
        self.pages = {} 
  
        # Here we iterate through a tupple of possible pages, starting with the first page
        for F in (A1, B1, B1_C2, B1_C3, B1_C4, B2, B2_C2, B2_C3, B2_C4, B2_C5, B3, B3_C2, B3_C3, B3_C4, B3_C5, B4, B4_C1, B5, B5_C2):
            frame = F(container, self)
            self.pages[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame(A1)
  
    # This is used to display a new page
    def show_frame(self, cont):
        frame = self.pages[cont]
        frame.tkraise()
  
# This is the starting page for our GUI
class A1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Defining the buttons
        button_A1 = tk.Button(self, text ="Access the seat resource", height=2, width=40, background='#eb4f34', fg='white', command = lambda : controller.show_frame(B1))
        button_A2 = tk.Button(self, text ="Access the client resource", height=2, width=40, background='#eb4f34', fg='white', command = lambda : controller.show_frame(B2))
        button_A3 = tk.Button(self, text ="Access the plane resource", height=2, width=40, background='#eb4f34', fg='white', command = lambda : controller.show_frame(B3))
        button_A4 = tk.Button(self, text ="Access the offer resource", height=2, width=40, background='#eb4f34', fg='white', command = lambda : controller.show_frame(B4))
        button_A5 = tk.Button(self, text ="Access the flight resource", height=2, width=40, background='#eb4f34', fg='white', command = lambda : controller.show_frame(B5))

        # Packing and placing the buttons
        button_A1.pack()
        button_A1.place(bordermode=tk.OUTSIDE, x=120, y=150)
        button_A2.pack()
        button_A2.place(bordermode=tk.OUTSIDE, x=120, y=230)
        button_A3.pack()
        button_A3.place(bordermode=tk.OUTSIDE, x=120, y=310)
        button_A4.pack()
        button_A4.place(bordermode=tk.OUTSIDE, x=120, y=390)
        button_A5.pack()
        button_A5.place(bordermode=tk.OUTSIDE, x=120, y=470)

        # Creating an image object
        #image = Image.open("./plane.png")
        #image_test = ImageTk.PhotoImage(image)
        #image_label = tk.Label(image=image_test)
        #image_label.image = image_test
        # Adjusting the position of the image
        #image_label.place(x=730, y=110)

        # Creating the text box
        text_box = tk.Text(self, height=30, width=85)
        text_box.place(x=530, y=110)
        # Creating an image object
        #image = Image.open("./plane.png")
        #image_test = ImageTk.PhotoImage(image)
        #image_label = tk.Label(image=image_test)
        #image_label.image = image_test
        # Adjusting the position of the image
        #image_label.place(x=730, y=110)
  
class B1(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=110)

        # Defining the buttons
        button_B1_C1 = tk.Button(self, text ="View the information for all the seats", height=2, width=40, background='blue', fg='white', command = lambda : GUI_functions.view_all_seat(text_box))
        button_B1_C2 = tk.Button(self, text ="Get the information for a specific seat", height=2, width=40, background='blue', fg='white', command = lambda : controller.show_frame(B1_C2))
        button_B1_C3 = tk.Button(self, text ="Delete the information for a specific seat", height=2, width=40, background='blue', fg='white', command = lambda : controller.show_frame(B1_C3))
        button_B1_C4 = tk.Button(self, text ="Create a new seat", height=2, width=40, background='blue', fg='white', command = lambda : controller.show_frame(B1_C4))
        button_B1_Back = tk.Button(self, text ="Back", height=2, width=40, background='blue', fg='white', command = lambda : controller.show_frame(A1))

        # Packing and placing the buttons
        button_B1_C1.pack()
        button_B1_C1.place(bordermode=tk.OUTSIDE, x=120, y=150)
        button_B1_C2.pack()
        button_B1_C2.place(bordermode=tk.OUTSIDE, x=120, y=230)
        button_B1_C3.pack()
        button_B1_C3.place(bordermode=tk.OUTSIDE, x=120, y=310)
        button_B1_C4.pack()
        button_B1_C4.place(bordermode=tk.OUTSIDE, x=120, y=390)
        button_B1_Back.pack()
        button_B1_Back.place(bordermode=tk.OUTSIDE, x=120, y=470)

        text_box = tk.Text(self, height=30, width=85)
        text_box.place(x=530, y=110)

class B2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating the text box
        text_box = tk.Text(self, height=30, width=85)
        text_box.place(x=530, y=110)

        # Defining the buttons
        button_B2_C1 = tk.Button(self, text ="View the information for all the clients", height=2, width=40, background='green', fg='white', command = lambda : GUI_functions.view_all_client(text_box))
        button_B2_C2 = tk.Button(self, text ="Get the information for a specific client", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(B2_C2))
        button_B2_C3 = tk.Button(self, text ="Create a new client", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(B2_C3))
        button_B2_C4 = tk.Button(self, text ="Delete the information for a specific client", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(B2_C4))
        button_B2_C5 = tk.Button(self, text ="Update the information for a specific client", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(B2_C5))
        button_B2_Back = tk.Button(self, text ="Back", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(A1))

        # Packing and placing the buttons
        button_B2_C1.pack()
        button_B2_C1.place(bordermode=tk.OUTSIDE, x=120, y=150)
        button_B2_C2.pack()
        button_B2_C2.place(bordermode=tk.OUTSIDE, x=120, y=230)
        button_B2_C3.pack()
        button_B2_C3.place(bordermode=tk.OUTSIDE, x=120, y=310)
        button_B2_C4.pack()
        button_B2_C4.place(bordermode=tk.OUTSIDE, x=120, y=390)
        button_B2_C5.pack()
        button_B2_C5.place(bordermode=tk.OUTSIDE, x=120, y=470)
        button_B2_Back.pack()
        button_B2_Back.place(bordermode=tk.OUTSIDE, x=120, y=550)

class B3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=110)


        # Defining the buttons
        button_B3_C1 = tk.Button(self, text ="View the information for all the planes", height=2, width=40, background='orange', fg='white', command = lambda : GUI_functions.view_all_plane(text_box))
        button_B3_C2 = tk.Button(self, text ="Get the information for a specific plane", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(B3_C2))
        button_B3_C3 = tk.Button(self, text ="Create a new plane", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(B3_C3))
        button_B3_C4 = tk.Button(self, text ="Delete the information for a specific plane", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(B3_C4))
        button_B3_C5 = tk.Button(self, text ="Update the information for a specific plane", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(B3_C5))
        button_B3_Back = tk.Button(self, text ="Back", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(A1))

        # Packing and placing the buttons
        button_B3_C1.pack()
        button_B3_C1.place(bordermode=tk.OUTSIDE, x=120, y=150)
        button_B3_C2.pack()
        button_B3_C2.place(bordermode=tk.OUTSIDE, x=120, y=230)
        button_B3_C3.pack()
        button_B3_C3.place(bordermode=tk.OUTSIDE, x=120, y=310)
        button_B3_C4.pack()
        button_B3_C4.place(bordermode=tk.OUTSIDE, x=120, y=390)
        button_B3_C5.pack()
        button_B3_C5.place(bordermode=tk.OUTSIDE, x=120, y=470)
        button_B3_Back.pack()
        button_B3_Back.place(bordermode=tk.OUTSIDE, x=120, y=550)

class B4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Defining the buttons
        button_B4_C1 = tk.Button(self, text ="Get the information for a specific offer", height=2, width=40, background='purple', fg='white', command = lambda : controller.show_frame(B4_C1))
        button_B4_Back = tk.Button(self, text ="Back", height=2, width=40, background='purple', fg='white', command = lambda : controller.show_frame(A1))

        # Packing and placing the buttons
        button_B4_C1.pack()
        button_B4_C1.place(bordermode=tk.OUTSIDE, x=120, y=150)
        button_B4_Back.pack()
        button_B4_Back.place(bordermode=tk.OUTSIDE, x=120, y=230)

        text_box = tk.Text(self, height=30, width=85)
        text_box.place(x=530, y=110)

class B5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=110)

        # Defining the buttons
        button_B5_C1 = tk.Button(self, text ="View the information for all flights", height=2, width=40, background='brown', fg='white', command = lambda : GUI_functions.view_all_flight(text_box))
        button_B5_C2 = tk.Button(self, text ="Get the information for a specific flight", height=2, width=40, background='brown', fg='white', command = lambda : controller.show_frame(B5_C2))
        button_B5_Back = tk.Button(self, text ="Back", height=2, width=40, background='brown', fg='white', command = lambda : controller.show_frame(A1))

        # Packing and placing the buttons
        button_B5_C1.pack()
        button_B5_C1.place(bordermode=tk.OUTSIDE, x=120, y=150)
        button_B5_C2.pack()
        button_B5_C2.place(bordermode=tk.OUTSIDE, x=120, y=230)
        button_B5_Back.pack()
        button_B5_Back.place(bordermode=tk.OUTSIDE, x=120, y=310)

class B4_C1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=80)
        e1.insert(1, "Replace this with the token of the client you wish to see the infromation for this offer")

        e2 = tk.Entry(self, width=140)
        e2.place(x=530, y=120)
        e2.insert(1, "Replace this with the origin")

        e3 = tk.Entry(self, width=140)
        e3.place(x=530, y=160)
        e3.insert(1, "Replace this with the destination")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B5_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='purple', fg='white', command = lambda : GUI_functions.get_offer(e1.get(), e2.get(), e3.get(), text_box))
        button_B5_Back = tk.Button(self, text ="Back", height=2, width=40, background='purple', fg='white', command = lambda : controller.show_frame(B4))

        # Packing and placing the buttons
        button_B5_Enter.pack()
        button_B5_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B5_Back.pack()
        button_B5_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B5_C2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=80)
        e1.insert(1, "Replace this with the origin")

        e2 = tk.Entry(self, width=140)
        e2.place(x=530, y=120)
        e2.insert(1, "Replace this with the destination")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B5_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='brown', fg='white', command = lambda : GUI_functions.get_flight(e1.get(), e2.get(), text_box))
        button_B5_Back = tk.Button(self, text ="Back", height=2, width=40, background='brown', fg='white', command = lambda : controller.show_frame(B5))

        # Packing and placing the buttons
        button_B5_Enter.pack()
        button_B5_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B5_Back.pack()
        button_B5_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B3_C2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=120)
        e1.insert(1, "Replace this with the plane's id you wish to see the infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C2_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='orange', fg='white', command = lambda : GUI_functions.get_plane(e1.get(), text_box))
        button_B3_C2_Back = tk.Button(self, text ="Back", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(B3))

        # Packing and placing the buttons
        button_B3_C2_Enter.pack()
        button_B3_C2_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C2_Back.pack()
        button_B3_C2_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B3_C3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=80)
        e1.insert(1, "Replace this with  the name for the plane")

        e2 = tk.Entry(self, width=140)
        e2.place(x=530, y=120)
        e2.insert(1, "Replace this with the current location for the plane")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='orange', fg='white', command = lambda : GUI_functions.post_plane(e1.get(), e2.get(), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(B3))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B3_C4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=120)
        e1.insert(1, "Replace this with the plane's id you wish to delete the infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=105)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C2_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='orange', fg='white', command = lambda : GUI_functions.delete_plane(e1.get(), text_box))
        button_B3_C2_Back = tk.Button(self, text ="Back", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(B3))

        # Packing and placing the buttons
        button_B3_C2_Enter.pack()
        button_B3_C2_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C2_Back.pack()
        button_B3_C2_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B3_C5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=80)
        e1.insert(1, "Replace this with the plane's id you want to update")

        e2 = tk.Entry(self, width=140)
        e2.place(x=530, y=120)
        e2.insert(1, "Replace this with a new name for the plane")

        e3 = tk.Entry(self, width=140)
        e3.place(x=530, y=160)
        e3.insert(1, "Replace this with a new location for the plane")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='orange', fg='white', command = lambda : GUI_functions.put_plane(e1.get(), e2.get(), e3.get(), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='orange', fg='white', command = lambda : controller.show_frame(B3))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B2_C2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=120)
        e1.insert(1, "Replace this with the token of the client you wish to see the infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='green', fg='white', command = lambda : GUI_functions.get_client(e1.get(), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(B2))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B2_C3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=80)
        e1.insert(1, "Replace this with the token for the client")

        e2 = tk.Entry(self, width=140)
        e2.place(x=530, y=120)
        e2.insert(1, "Replace this with the name for the client")

        e3 = tk.Entry(self, width=140)
        e3.place(x=530, y=160)
        e3.insert(1, "Replace this with the surname for the client")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='green', fg='white', command = lambda : GUI_functions.post_client(e1.get(), e2.get(), e3.get(), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(B2))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B2_C4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=120)
        e1.insert(1, "Replace this with the token of the client you wish to delete the information for")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='green', fg='white', command = lambda : GUI_functions.delete_client(e1.get(), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(B2))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B2_C5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e0 = tk.Entry(self, width=140)
        e0.place(x=530, y=40)
        e0.insert(1, "Replace this with the token for the client")

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=80)
        e1.insert(1, "Replace this with the new name for the client")

        e2 = tk.Entry(self, width=140)
        e2.place(x=530, y=120)
        e2.insert(1, "Replace this with the new surname for the client")

        e3 = tk.Entry(self, width=140)
        e3.place(x=530, y=160)
        e3.insert(1, "Replace this with the new token for the client")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='green', fg='white', command = lambda : GUI_functions.put_client(e0.get(), e1.get(), e2.get(), e3.get(), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='green', fg='white', command = lambda : controller.show_frame(B2))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B1_C2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=120)
        e1.insert(1, "Replace this with the plane's id you wish to see the seat infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='blue', fg='white', command = lambda : GUI_functions.get_seat(e1.get(), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='blue', fg='white', command = lambda : controller.show_frame(B1))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B1_C3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=120)
        e1.insert(1, "Replace this with the plane's id you wish to delete the seat infromation")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='blue', fg='white', command = lambda : GUI_functions.delete_seat(e1.get(), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='blue', fg='white', command = lambda : controller.show_frame(B1))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

class B1_C4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        e1 = tk.Entry(self, width=140)
        e1.place(x=530, y=80)
        e1.insert(1, "Replace this with the plane's id you wish to add new seat infromation")

        e2 = tk.Entry(self, width=140)
        e2.place(x=530, y=120)
        e2.insert(1, "Replace this with the types of the seat seperated by comma (,)")

        e3 = tk.Entry(self, width=140)
        e3.place(x=530, y=160)
        e3.insert(1, "Replace this with the capacities of the seats' type seperated by comma (,)")

        # Creating the text box
        text_box = tk.Text(self, height=30, width=110)
        text_box.place(x=530, y=200)

        # Defining the buttons
        button_B3_C3_Enter = tk.Button(self, text ="Enter", height=2, width=40, background='blue', fg='white', command = lambda : GUI_functions.post_seat(e1.get(), list(map(lambda x: x.strip(), e2.get().split(','))),list(map(lambda x: x.strip(), e3.get().split(','))), text_box))
        button_B3_C3_Back = tk.Button(self, text ="Back", height=2, width=40, background='blue', fg='white', command = lambda : controller.show_frame(B1))

        # Packing and placing the buttons
        button_B3_C3_Enter.pack()
        button_B3_C3_Enter.place(bordermode=tk.OUTSIDE, x=800, y=700)
        button_B3_C3_Back.pack()
        button_B3_C3_Back.place(bordermode=tk.OUTSIDE, x=120, y=150)

# Main loop
app = tkinterApp()
app.mainloop()