
class Flashcard:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def display_question(self):
        return f'Question: {self.question}'

    def display_answer(self):
        return f'Answer: {self.answer}'
