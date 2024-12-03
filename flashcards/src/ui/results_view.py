from tkinter import ttk, constants
from services.flashcard_service import flashcard_service

class ResultsView:
    def __init__(self, root, handle_flashcards_view):
        self._root = root
        self._frame = None
        self._correct_results = flashcard_service.get_practice_results_correct()
        self._incorrect_results = flashcard_service.get_practice_results_incorrect()
        self._collection = flashcard_service.get_collection()
        self._flashcards = flashcard_service.get_flashcards_from_collection()

        self._handle_flashcards_view = handle_flashcards_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        total_cards = len(self._flashcards)
        correct_answers = len(self._correct_results)
        incorrect_answers = len(self._incorrect_results)

        header_label = ttk.Label(master=self._frame, text=self._collection.name)
        return_to_flashcards_button = ttk.Button(master=self._frame, text="Palaa kokoelmaan", command=self._handle_flashcards_view)
        correct_label = ttk.Label(
            master=self._frame,
            text=(f"Oikeita vastauksia {correct_answers} / {total_cards} "
                  f"({round(correct_answers/total_cards*100, 1)} %)")
        )
        incorrect_label = ttk.Label(
            master=self._frame,
            text=(f"Vääriä vastauksia {incorrect_answers} / {total_cards} "
            f"({round(incorrect_answers/total_cards*100, 1)} %)")
        )

        header_label.grid(row=0, column=0, padx=5, pady=5)
        return_to_flashcards_button.grid(row=1, column=0, padx=5, pady=5)
        correct_label.grid(row=2, column=0, padx=5, pady=5)
        incorrect_label.grid(row=3, column=0, padx=5, pady=5)
