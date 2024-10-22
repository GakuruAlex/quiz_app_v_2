from tkinter import Button, Tk, Canvas, PhotoImage, WORD
from questions import Questions
class Ui:
    BACKGROUND_COLOR = "#375362"
    FONT = ("Arial", 20, "italic")
    CANVAS_COLOR = "white"
    CORRECT_COLOR = "lime"
    WRONG_COLOR = "red"
    PAD = 20
    def __init__(self):
        self.questions: Questions= Questions()
        self.answer = None
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.configure(pady=self.PAD, padx=self.PAD, bg=self.BACKGROUND_COLOR)
        self.canvas = Canvas(master=self.window, bg=self.CANVAS_COLOR)
        self.canvas.configure(height=250, width=300)
        self.question_text=self.canvas.create_text(
            150,
            125,
            text="This is an example of wrapping text in a tkinter canvas.\
            The text will wrap within the specified width.",
            fill=self.BACKGROUND_COLOR,
            font=self.FONT,
            width= 250)

        self.canvas.grid(row=0, column=0,columnspan=2, pady=self.PAD)
        self.display_question()

        right_image = PhotoImage(master=self.canvas,file="./images/true.png")
        self.right_image = Button(self.window,image=right_image, highlightthickness=0, bg=self.BACKGROUND_COLOR, command=self.right_clicked)
        self.right_image.grid(row=1, column=0, pady=self.PAD )

        wrong_image = PhotoImage(master=self.canvas,file="./images/false.png")
        self.wrong_image = Button(self.window,image=wrong_image, highlightthickness=0, bg=self.BACKGROUND_COLOR, command=self.wrong_clicked)
        self.wrong_image.grid(row=1, column=1, pady=self.PAD)

        self.window.mainloop()
    def display_question(self)-> None:
        """__Display the current question on the canvas_
        """
        self.canvas.config(bg=self.CANVAS_COLOR)
        self.canvas.itemconfig(self.question_text, text=f"{self.questions.current_question['question']}")
    def right_clicked(self)->None:
        """_Set the answer to 'True' if the right icon button is clicked_
        """
        self.answer: str = "True"
        self.correct_answer()
    def wrong_clicked(self)->None:
        """_Set the answer to 'False" when the wrong icon button is clicked_
        """
        self.answer: str = "False"
        self.correct_answer()
    def correct_answer(self)-> None:
        """_Check if the user answer was correct , change canvas color accordingly then pull next question and display it_
        """
        if self.questions.is_correct(self.answer):
            self.canvas.config(bg=self.CORRECT_COLOR)
            self.window.after(2000, self.questions.next_question)
            self.window.after(2000, self.display_question)

        else:
            self.canvas.config(bg=self.WRONG_COLOR)
            self.window.after(2000, self.questions.next_question)
            self.window.after(2000, self.display_question)



if __name__ == "__main__":
    ui = Ui()