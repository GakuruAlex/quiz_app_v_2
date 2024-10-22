class Score:
    def __init__(self):
        self.score: int = 0
    def increase_score(self)-> None:
        """Increase score by 1
        """
        self.score += 1