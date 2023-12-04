import tkinter as tk
from tkinter import font as tkfont

# tkinter switching frames: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

# TODO: fix exit button (destroy all frames)
# TODO: pet name user input screen [done]
# TODO: new game pet gameplay screen

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Jerry the Game")
        self.title_font = tkfont.Font(family='Helvetica', size=50, weight="bold", slant="italic")
        self.option_font = tkfont.Font(family='Helvetica', size=12)
        self.text_font = tkfont.Font(family='Helvetica', size=12)
        # self.configure(bg="white")

        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set the window dimensions to be 60% of the screen width and height
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)

        # Set the initial geometry of the window
        self.geometry(
            f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

        # Configure row and column weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, bg="green")
        container.pack(expand=True, fill=tk.BOTH)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creating the frames (identical)
        self.frames = {}
        list_of_frames = [MainMenu, IntroScreen, EnterName]
        for F in list_of_frames:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def destroy_all_frames(self):
        for frame_name in self.frames.keys():
            self.frames[frame_name].destroy_frame()
        self.show_frame("MainMenu")


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Frame.config(self, bg='yellow')
        # label = tk.Label(self, text="This is the start page", font=controller.title_font)
        # label.grid(pady=10)
        # tk.Frame.pack(self, expand=True, fill='both')
        # tk.Frame.place(self, relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        tk.Frame.grid(self, row=0, column=0, sticky="")
        # tk.Frame.pack(self, expand=True)

        gameName = tk.Label(
            self,
            text="Jerry the Game!",
            font=controller.title_font,
            bg="white")
        gameName.grid(row=0, column=0, pady=20)

        newGameButton = tk.Button(
            self,
            text="New Game",
            font=controller.option_font,
            width=20,
            height=2,
            bg="blue",
            fg="white",
            command=lambda: controller.show_frame("IntroScreen"))
        # command=self.new_game)
        newGameButton.grid(row=1, column=0, pady=0)

        """
        continueGameButton = tk.Button(
            self,
            text="Continue Game",
            font=controller.option_font,
            width=20,
            height=2,
            bg="blue",
            fg="white",
            command=self.continue_game)
        continueGameButton.grid(row=2, column=0, pady=0)
        """

        creditsButton = tk.Button(
            self,
            text="Credits",
            font=controller.option_font,
            width=20,
            height=2,
            bg="blue",
            fg="white",
            command=self.credits)
        creditsButton.grid(row=2, column=0, pady=0)

        exitButton = tk.Button(
            self,
            text="Exit",
            font=controller.option_font,
            width=12,
            height=2,
            bg="blue",
            fg="white",
            command=self.exit_game)
        exitButton.grid(row=3, column=0, pady=30)

    def new_game(self):
        print("New Game!")

    def continue_game(self):
        print("Continue")

    def credits(self):
        print("All me baby")

    def exit_game(self):
        self.controller.destroy_all_frames()  # does not work lol

    def destroy_frame(self):
        self.destroy()


class IntroScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Frame.config(self, bg='red')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        tk.Frame.grid(self, row=0, column=0, sticky="")

        game_text = ("You are a new student living in a dorm in SUTD when you happen to come across Jerry, the dorm "
                     "cat! \nYou fell in love at first sight and want to learn how to take care of her, but you have "
                     "no experience with animals :( \nHowever! With our game, you can learn how to care for cats, "
                     "along with different types of animals. \nTake good care of your pet to make sure it does not "
                     "run away!")

        label = tk.Label(self, text=game_text, font=('Helvetica', 15), justify='center', wraplength=550, pady=10)
        label.grid(row=0, column=0)
        button = tk.Button(self,
                           text="Continue",
                           font=controller.option_font,
                           width=20,
                           height=2,
                           bg="blue",
                           fg="white",
                           command=lambda: controller.show_frame("EnterName"))
        button.grid(row=1, column=0, pady=(0, 50))

        def destroy_frame(self):
            self.destroy()

class EnterName(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Frame.config(self, bg='white')
        """
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        tk.Frame.grid(self, row=0, column=0, sticky="")
        """
        f1 = tk.Frame(self)
        input_name = "Please name your pet: "
        label = tk.Label(f1,
                         text=input_name,
                         font=('Helvetica', 15))
        #label.grid(row=1, column=1)
        label.pack(pady=10)

        input_textbox = tk.Entry(f1,
                           width=50)
        #input_textbox.grid(row=1, column=2)
        input_textbox.pack(pady=10)

        def get_input():
            entered_text = input_textbox.get()
            return entered_text

        button = tk.Button(f1,
                           text="Continue",
                           font=controller.option_font,
                           width=20,
                           height=2,
                           bg="blue",
                           fg="white",
                           command=get_input)
        # button.grid(row=2, column=1, pady=0)
        button.pack(pady=(20,0))

        f1.pack(expand=True, fill='both')

        def destroy_frame(self):
            self.destroy()

class Gameplay(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Frame.config(self, bg='red')
        """
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        tk.Frame.grid(self, row=0, column=0, sticky="")
        """
        # Frame 1: Name + Statistics bar
        # Frame 2: F1 + shop button
        # Frame 3: Action buttons (Feed, Play, Groom)
        # Frame 4: Day display + pet image
        # Frame 5: Save + Exit buttons
        # Frame 6: Coin display + daily reward button
        # Frame 7: Inventory

        f1 = tk.Frame(self)
        input_name = "Please name your pet: "
        label = tk.Label(f1,
                         text=input_name,
                         font=('Helvetica', 15))
        label.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()

