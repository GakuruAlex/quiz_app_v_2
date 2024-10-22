from tkinter import Button, Tk, Canvas, PhotoImage, WORD, Label, messagebox
from questions import Questions
from score import Score
class UI:
    BACKGROUND_COLOR = "#375362"
    FONT = ("Arial", 20, "italic")
    CANVAS_COLOR = "white"
    CORRECT_COLOR = "lime"
    WRONG_COLOR = "red"
    PAD = 20
    def __init__(self):
        self.questions: Questions= Questions()
        self.score = Score()
        self.answer = None
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.configure(pady=self.PAD, padx=self.PAD, bg=self.BACKGROUND_COLOR)
        self.canvas = Canvas(master=self.window, bg=self.CANVAS_COLOR)
        self.score_text = Label(text=f"Score: {self.score.score} / {len(self.questions.questions)}",
                                background=self.BACKGROUND_COLOR,
                                fg=self.CANVAS_COLOR,
                                font=("Arial", 12, "normal"))
        self.score_text.grid(row=0, column=1)
        self.canvas.configure(height=250, width=300)
        self.question_text=self.canvas.create_text(
            150,
            125,
            text="This is an example of wrapping text in a tkinter canvas.\
            The text will wrap within the specified width.",
            fill=self.BACKGROUND_COLOR,
            font=self.FONT,
            width= 250)

        self.canvas.grid(row=1, column=0,columnspan=2, pady=self.PAD)
        self.display_question()

        right_image = PhotoImage(master=self.canvas,file="./images/true.png")
        self.right_image = Button(self.window,image=right_image, highlightthickness=0, bg=self.BACKGROUND_COLOR, command=self.right_clicked)
        self.right_image.grid(row=2, column=0, pady=self.PAD )

        wrong_image = PhotoImage(master=self.canvas,file="./images/false.png")
        self.wrong_image = Button(self.window,image=wrong_image, highlightthickness=0, bg=self.BACKGROUND_COLOR, command=self.wrong_clicked)
        self.wrong_image.grid(row=2, column=1, pady=self.PAD)

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
            self.score.increase_score()
            self.score_text.config(text=f"Score: {self.score.score} / {len(self.questions.questions)}")
            self.canvas.config(bg=self.CORRECT_COLOR)

        else:
            self.canvas.config(bg=self.WRONG_COLOR)

        if self.questions.any_more_questions():
                self.window.after(2000, self.questions.next_question)
                self.window.after(2000, self.display_question)
        else:
            self.disable_buttons()


    def disable_buttons(self)-> None:
        """_Disable the buttons when there no more questions to display_
        """
        self.right_image.config(state="disabled")
        self.wrong_image.config(state="disabled")
        messagebox.showinfo(title="Game Over",message=f"Game Over! Your score is {self.score.score}")
        self.window.after(1000, self.kill_window)
    def kill_window(self):
        self.window.destroy()



if __name__ == "__main__":
    ui = UI()