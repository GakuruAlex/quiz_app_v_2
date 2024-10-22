from requests import get
from html import unescape

class Questions:
    URL = "https://opentdb.com/api.php?amount=20&category=18&type=boolean"
    def __init__(self):
        self.questions = {}
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
            self.questions.update({question_no + 1:{"question": unescape(result["question"]), "answer": result["correct_answer"]}})

if __name__ == "__main__":
    questions=Questions()
    questions.populate_questions()
    print(questions.questions)