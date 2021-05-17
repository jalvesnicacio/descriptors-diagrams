from tkinter import *
from tkinter import filedialog
from diagram_controller import DiagramController
from PIL import Image


class MainGUI():
    def __init__(self, master):
        self.master = master
        master.title("Compose-Diagrams GUI")
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (w, h))

        # Frame Left

        self.frame_left = Frame(master, bg = "", width=200)
        self.frame_left.pack(side = LEFT, fill="both", expand=True, padx=5, pady=5)

        self.frame_left_top = Frame(self.frame_left, bg = "", height = 20)
        #self.frame_left_top.pack(side = TOP, fill="both", expand=True, padx=5, pady=0)
        self.frame_left_top.pack(fill="both")

        self.import_compose_button = Button(self.frame_left_top, text="Import Docker-compose file", command=self.import_compose)
        self.import_compose_button.pack(side = LEFT)

        self.text_yaml = Text(self.frame_left)
        self.text_yaml.pack(side = TOP, fill="both", expand=True)

        # Frame Right

        self.frame_right = Frame(master, bg = "")
        self.frame_right.pack(side = RIGHT, fill="both", expand=True, padx=5, pady=5)

        self.frame_right_top = Frame(self.frame_right, bg = "", height = 20)
        #self.frame_left_top.pack(side = TOP, fill="both", expand=True, padx=5, pady=0)
        self.frame_right_top.pack(fill="both")

        self.save_diagram_button = Button(self.frame_right_top, text="Save Diagram", command=self.save_diagram, state=DISABLED)
        #self.save_diagram_button['state'] = 'normal' ou self.save_diagram_button.config(state="normal") para mudar o status
        self.save_diagram_button.pack(side = LEFT)

        #self.show_diagram = Text(self.frame_right)
        #self.show_diagram.pack(side = TOP, fill="both", expand=True)

        self.show_diagram = Label(self.frame_right)
        self.show_diagram.pack(side = TOP, fill="both", expand=True)

        # self.close_button = Button(self.frame_right, text="Close", command=master.quit)
        # self.close_button.pack()


    def import_compose(self):
        #print("Greetings!")
        self.filename =  filedialog.askopenfilename(
                #initialdir = "/home/jalves",
                title = "Select file",
                filetypes = (("yaml files","*.yaml"),("yaml files", "*.yml"),("all files","*.*"))
            )
        if not self.filename:
            return
        compose_file = open(self.filename, 'r')
        self.text_yaml.insert(INSERT, compose_file.read())
        diagram_filename = DiagramController().build_diagram(self.filename)
        self.load_diagram(diagram_filename)

    def load_diagram(self, filename):
        load = Image.open(filename)
        #diagram = PhotoImage(master = self.master, file= filenam)
        diagram = PhotoImage(load)
        self.show_diagram.configure(image=diagram)
        self.show_diagram.image = diagram
        # self.show_diagram.insert(INSERT, '\n')
        # self.show_diagram.image_create(INSERT, image=diagram)


    def save_diagram(self):
        return None

# </ class MainGUI>


root = Tk()
my_gui = MainGUI(root)
root.mainloop()
