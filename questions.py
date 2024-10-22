from requests import get
from html import unescape

class Questions:
    URL = "https://opentdb.com/api.php?amount=20&category=18&type=boolean"
    def __init__(self):
        self.questions = {}
        self.question_counter = 0
        self.current_question = None
        self.get_questions()
    def get_questions(self)-> None:
        """_Fetch questions from Open Trivia Api, check for any HTTP error and store the response_
        """
        response = get(self.URL)
        response.raise_for_status()
        self.results = response.json()["results"]
    def populate_questions(self)-> None:
        """_Iterate over the results question list  and create a questions dict_
        """
        for question_no, result in enumerate(self.results):
            self.questions.update({question_no :{"question": unescape(result["question"]), "answer": result["correct_answer"]}})
    def next_question(self)->None:
        """_Get current question to display_
        """
        if self.question_counter < len(self.questions):
            self.current_question = self.questions[self.question_counter]
            self.question_counter += 1
    def is_right(self, answer: str)->bool:
        """_Check whether the user answer is correct_

        Args:
            answer (str): _Answer given by user_

        Returns:
            bool: _True if answer correct else False_
        """
        return answer == self.current_question["answer"]

if __name__ == "__main__":
    questions=Questions()
    questions.populate_questions()
    questions.next_question()
    print(questions.current_question)