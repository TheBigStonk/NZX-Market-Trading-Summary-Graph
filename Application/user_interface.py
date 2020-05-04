## tkinter Interface to Handle and Provide Functionality in a friendly maner
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

LARGE_FONT = ("Verdana", 12)

class NzxMarketTradingSummary(tk.Tk) :

    # Init self method (not a function) taking defaults and stting up TK container
    def __init__(self, *args, **kwargs) :
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default="thumbnail.ico")
        tk.Tk.wm_title(self, "NzxTradingStats")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Dictionary of frames
        self.frames = {}

        for f in (StartPage, PageOne, PageTwo, PageThree):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "The Beginning of a good trade tool", font=LARGE_FONT)
        label.pack(pady=10,padx=200)

        # Use of a Lambda function in order to allow
        button1 = ttk.Button(self, text = "Enter the platform", 
        command = lambda : controller.show_frame(PageOne))
        button1.pack()
        # Use of a Lambda function in order to allow
        button2 = ttk.Button(self, text = "Jump to Two", 
        command = lambda : controller.show_frame(PageTwo))
        button2.pack()
        # Use of a Lambda function in order to allow
        button3 = ttk.Button(self, text = "Graph", 
        command = lambda : controller.show_frame(PageThree))
        button3.pack()

class PageOne(tk.Frame) :

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Trade Trading Trade Trade", font=LARGE_FONT)
        label.pack(pady=10,padx=200)

        
        # Use of a Lambda function in order to allow
        button1 = ttk.Button(self, text = "Back to home", 
        command = lambda : controller.show_frame(StartPage))
        button1.pack()

        # Use of a Lambda function in order to allow
        button2 = ttk.Button(self, text = "Go to Two", 
        command = lambda : controller.show_frame(PageTwo))
        button2.pack()

 
class PageTwo(tk.Frame) :

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "More Trading", font=LARGE_FONT)
        label.pack(pady=10,padx=200)

        
        # Use of a Lambda function in order to allow
        button1 = ttk.Button(self, text = "Back to One", 
        command = lambda : controller.show_frame(PageOne))
        button1.pack()

        # Use of a Lambda function in order to allow
        button2 = ttk.Button(self, text = "Back to Start", 
        command = lambda : controller.show_frame(StartPage))
        button2.pack()

class PageThree(tk.Frame) :

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Graph Page", font=LARGE_FONT)
        label.pack(pady=10,padx=200)

        # Use of a Lambda function in order to allow
        button1 = ttk.Button(self, text = "Back to Start", 
        command = lambda : controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)


               
app = NzxMarketTradingSummary()
app.mainloop()