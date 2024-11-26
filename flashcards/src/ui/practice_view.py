from tkinter import ttk, constants
from services.flashcard_service import flashcard_service


class PracticeFrontView:
    def __init__(self, root, flashcard, handle_turn):
        self._root = root
        self._frame = None
        self._flashcard = flashcard
        self._handle_turn = handle_turn

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        item_frame = ttk.Frame(master=self._frame)
        front_label = ttk.Label(master=item_frame, text=self._flashcard.front)
        turn_button = ttk.Button(master=item_frame, text="Käännä", command=self._handle_turn)
        
        front_label.grid(row=0, column=0, columnspan=2)
        turn_button.grid(row=1, column=0, columnspan=2)
        item_frame.pack(fill=constants.X)

class PracticeBackView:
    def __init__(self, root, flashcard, handle_next):
        self._root = root
        self._frame = None
        self._flashcard = flashcard
        self._handle_next = handle_next

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        item_frame = ttk.Frame(master=self._frame)
        back_label = ttk.Label(master=item_frame, text=self._flashcard.back)
        query_label = ttk.Label(master=item_frame, text="Osasitko?")
        yes_button = ttk.Button(master=item_frame, text="Kyllä", command=lambda: self._handle_next(True))
        no_button = ttk.Button(master=item_frame, text="Ei", command=lambda: self._handle_next(False))
        
        back_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        query_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        yes_button.grid(row=2, column=0, padx=5, pady=5)
        no_button.grid(row=2, column=1, padx=5, pady=5)
        item_frame.pack(fill=constants.X)

class PracticeView:
    def __init__(self, root, handle_flashcards_view):
        self._root = root
        self._frame = None
        self._current_flashcard_frame = None
        self._current_flashcard_view = None
        self._handle_flashcards_view = handle_flashcards_view
        self._collection = flashcard_service.get_collection()
        self._flashcards = flashcard_service.get_flashcards_from_collection()

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _handle_turn_flashcard(self):
        if self._current_flashcard_view:
            self._current_flashcard_view.destroy()
        
        current = flashcard_service.current_flashcard()
        self._current_flashcard_view = PracticeBackView(self._current_flashcard_frame, self._flashcards[current], self._handle_next_flashcard)
        self._current_flashcard_view.pack()

    def _handle_next_flashcard(self, was_correct):
        more_cards = flashcard_service.progress_practice(was_correct)
        if more_cards:
            self._initialize_current_flashcard()
        else:
            self._handle_flashcards_view()

    def _initialize_current_flashcard(self):
        if self._current_flashcard_view:
            self._current_flashcard_view.destroy()
    
        current = flashcard_service.current_flashcard()
        self._current_flashcard_view = PracticeFrontView(self._current_flashcard_frame, self._flashcards[current], self._handle_turn_flashcard)
        self._current_flashcard_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._current_flashcard_frame = ttk.Frame(master=self._frame)

        flashcard_service.start_practice()
        self._initialize_current_flashcard()

        header_label = ttk.Label(master=self._frame, text=f"Harjoitellaan kokoelmaa {self._collection.name}")

        header_label.grid(row=0, column=0, columnspan=2)
        self._current_flashcard_frame.grid(row=1, column=0, columnspan=2)

