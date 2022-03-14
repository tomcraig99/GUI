import tkinter
import tkinter.messagebox


class OutputGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # configure the main window
        self.main_window.geometry("1000x700")
        self.main_window.title("Frame/button Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in kilometers:")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.descr_label = tkinter.Label(self.mid_frame, text="Converted to Miles:")
        
        self.miles_var = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame,textvariable=self.miles_var)
        
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.calcbutton = tkinter.Button(self.main_window, text="convert", command=self.convert)
        self.quit_button = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        self.calcbutton.pack(side="left")
        self.quit_button.pack(side="right")

        self.top_frame.pack(side="top")
        self.mid_frame.pack(side="top")
        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(kilo * 0.6214, 2)

        self.miles_var.set(miles)


output = OutputGUI()

print("moving on.....")
