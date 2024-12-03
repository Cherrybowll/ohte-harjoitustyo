from tkinter import ttk, constants
from services.flashcard_service import flashcard_service


class ResultsListView:
    def __init__(self, root, subflashcards):
        self._root = root
        self._frame = None
        self._subflashcards = subflashcards

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_flashcard(self, flashcard, i):
        front_label = ttk.Label(master=self._frame, text=flashcard.front)
        back_label = ttk.Label(master=self._frame, text=flashcard.back)

        front_label.grid(row=i, column=0, padx=5, pady=5)
        back_label.grid(row=i, column=2, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        i = 0

        for flashcard in self._subflashcards:
            self._initialize_flashcard(flashcard, i)
            i += 1

        if i > 0:
            separator = ttk.Separator(
                master=self._frame, orient=constants.VERTICAL)
            separator.grid(row=0, column=1, rowspan=i, sticky=constants.NS)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)


class ResultsView:
    def __init__(self, root, handle_flashcards_view):
        self._root = root
        self._frame = None
        self._subflashcard_list_frame = None
        self._subflashcard_list_view = None
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

    def _initialize_subflashcard_list(self):
        if self._subflashcard_list_view:
            self._subflashcard_list_view.destroy()

        self._subflashcard_list_view = ResultsListView(
            self._subflashcard_list_frame,
            self._incorrect_results
        )
        self._subflashcard_list_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._subflashcard_list_frame = ttk.Frame(master=self._frame)

        self._initialize_subflashcard_list()

        total_cards = len(self._flashcards)
        correct_answers = len(self._correct_results)
        incorrect_answers = len(self._incorrect_results)

        header_label = ttk.Label(
            master=self._frame, text=self._collection.name)
        return_to_flashcards_button = ttk.Button(
            master=self._frame,
            text="Palaa kokoelmaan",
            command=self._handle_flashcards_view
        )
        incorrect_header_label = ttk.Label(
            master=self._frame,
            text="Näitä pitää vielä harjoitella:"
        )
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
        incorrect_header_label.grid(row=4, column=0, padx=5, pady=5)
        self._subflashcard_list_frame.grid(row=5, column=0, padx=5, pady=5)
