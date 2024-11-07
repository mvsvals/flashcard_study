import random
from flashcard import Flashcard


class FlashcardManager:

    def __init__(self):
        self.flashcards = {}

    def add_flashcard(self, question, answer, silent_mode=False):
        # Add a new flashcard.
        self.flashcards[question] = Flashcard(question, answer)
        if not silent_mode:
            print('A new flashcard has been successfully created.')

    def edit_flashcard(self, question, new_question, new_answer):
        # Edit an existing flashcard.
        if question in self.flashcards:
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            if new_question != question:
                del self.flashcards[question]
            print('The changes to the flashcard have been saved.')
        else:
            print('The flashcard doesn\'t exist.')

    def delete_flashcard(self, question):
        # Delete a flashcard.
        if question in self.flashcards:
            print(f'Flashcard {self.flashcards[question]} has been deleted.')
            del self.flashcards[question]
        else:
            print('The flashcard doesn\'t exist.')

    def list_flashcard(self):
        # Display all flashcards.
        index = 0
        for question, flashcard in self.flashcards.items():
            index += 1
            print(f'{index}. {flashcard.display_question()}')

    def review_flashcard(self):
        # Pick a random flashcard to display for review.
        if self.flashcards:
            print('Picking a random flashcard...')
            question = random.choice(list(self.flashcards.keys()))
            flashcard = self.flashcards[question]
            print(flashcard.display_question())
            input("Press Enter to show the answer...")
            print(flashcard.display_answer())
        else:
            print("No flashcards to review!")
