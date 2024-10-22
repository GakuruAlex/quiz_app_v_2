from tkinter import Button, Tk, Canvas, PhotoImage, WORD

class Ui:
    BACKGROUND_COLOR = "#375362"
    FONT = ("Arial", 20, "italic")
    CANVAS_COLOR = "white"
    PAD = 20
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.configure(pady=self.PAD, padx=self.PAD, bg=self.BACKGROUND_COLOR)
        self.canvas = Canvas(master=self.window, bg=self.CANVAS_COLOR)
        self.canvas.configure(height=250, width=300)
        self.canvas.create_text(
            150,
            125,
            text="This is an example of wrapping text in a tkinter canvas.\
            The text will wrap within the specified width.",
            fill=self.BACKGROUND_COLOR,
            font=self.FONT,
            width= 250)

        self.canvas.grid(row=0, column=0,columnspan=2, pady=self.PAD)

        right_image = PhotoImage(master=self.canvas,file="./images/true.png")
        self.right_image = Button(self.window,image=right_image, highlightthickness=0, bg=self.BACKGROUND_COLOR)
        self.right_image.grid(row=1, column=0, pady=self.PAD )

        wrong_image = PhotoImage(master=self.canvas,file="./images/false.png")
        self.wrong_image = Button(self.window,image=wrong_image, highlightthickness=0, bg=self.BACKGROUND_COLOR)
        self.wrong_image.grid(row=1, column=1, pady=self.PAD)

        self.window.mainloop()


if __name__ == "__main__":
    ui = Ui()