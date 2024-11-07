
from flashcard import Flashcard
from flashcard_manager import FlashcardManager


def navigation_menu(m_items: list, manager_object: FlashcardManager):

    print('Welcome to the Flash Card App!')

    while True:
        for index, menu_item in enumerate(m_items, 1):
            print(f'{index}. {menu_item}')

        menu_selection = input(f'Please input a number from 1 to {len(m_items)}:')
        if not menu_selection or not menu_selection.isdigit() or not (1 <= int(menu_selection) <= len(m_items)):
            print('Invalid input.')
            continue
        menu_selection = int(menu_selection)
        if menu_selection == 1:
            question = input('Type the question: ')
            answer = input('Type the answer: ')
            manager_object.add_flashcard(question, answer)
        elif menu_selection == 2:
            question = input('Type the existing question: ')
            new_question = input('Type the new question: ')
            new_answer = input('Type the answer: ')
            manager_object.edit_flashcard(question, new_question, new_answer)
        elif menu_selection == 3:
            question = input('Type the question you wish to delete: ')
            manager_object.delete_flashcard(question)
        elif menu_selection == 4:
            manager_object.list_flashcard()
        elif menu_selection == 5:
            manager_object.review_flashcard()
        elif menu_selection == 6:
            break


flashcard_manager = FlashcardManager()

# Sample flashcards for testing
flashcard_manager.add_flashcard('What is the capital of France?', 'Paris', silent_mode=True)
flashcard_manager.add_flashcard('Who wrote \'To Kill a Mockingbird\'?', 'Harper Lee', silent_mode=True)
flashcard_manager.add_flashcard('What is the largest planet in our Solar System?', 'Jupiter', silent_mode=True)
flashcard_manager.add_flashcard('What is the boiling point of water in Celsius?', '100', silent_mode=True)
flashcard_manager.add_flashcard('Who painted the Mona Lisa?', 'Leonardo da Vinci', silent_mode=True)

menu_items = [
    'Add Flashcard',
    'Edit Flashcard',
    'Delete Flashcard',
    'List Flashcards',
    'Review Flashcards',
    'Exit'
]

navigation_menu(menu_items, flashcard_manager)
