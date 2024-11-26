from tkinter import ttk, constants
from services.flashcard_service import flashcard_service

class FlashcardsListView:
    def __init__(self, root, flashcards):
        self._root = root
        self._frame = None
        self._flashcards = flashcards

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize_flashcard(self, flashcard):
        item_frame = ttk.Frame(master=self._frame)
        front_label = ttk.Label(master=item_frame, text=flashcard.front)
        back_label = ttk.Label(master=item_frame, text=flashcard.back)
        front_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.EW)
        back_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for flashcard in self._flashcards:
            self._initialize_flashcard(flashcard)


class FlashcardsView:
    def __init__(self, root, handle_practice_view):
        self._root = root
        self._frame = None
        self._flashcard_list_frame = None
        self._flashcard_list_view = None
        self._handle_practice_view = handle_practice_view

        self._create_flashcard_front_entry = None
        self._create_flashcard_back_entry = None

        self._collection = flashcard_service.get_collection()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize_flashcards_list(self):
        if self._flashcard_list_view:
            self._flashcard_list_view.destroy()
        
        flashcards = flashcard_service.get_flashcards_from_collection()

        self._flashcard_list_view = FlashcardsListView(self._flashcard_list_frame, flashcards)
        self._flashcard_list_view.pack()

    def _handle_create_flashcard(self):
        flashcard_front = self._create_flashcard_front_entry.get()
        flashcard_back = self._create_flashcard_back_entry.get()

        if flashcard_front and flashcard_back:
            flashcard_service.create_flashcard(flashcard_front, flashcard_back)
            self._initialize_flashcards_list()
            self._create_flashcard_front_entry.delete(0, constants.END)
            self._create_flashcard_back_entry.delete(0, constants.END)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._flashcard_list_frame = ttk.Frame(master=self._frame)

        self._initialize_flashcards_list()

        header_label = ttk.Label(master=self._frame, text=self._collection.name)
        front_label = ttk.Label(master=self._frame, text="Etupuoli")
        back_label = ttk.Label(master=self._frame, text="Takapuoli")
        self._create_flashcard_front_entry = ttk.Entry(master=self._frame)
        self._create_flashcard_back_entry = ttk.Entry(master=self._frame)
        create_flashcard_button = ttk.Button(master=self._frame, text="Lisää flashcard", command=self._handle_create_flashcard)
        practice_collection_button = ttk.Button(master=self._frame, text="Harjoittele kokoelmaa", command=self._handle_practice_view)

        header_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        practice_collection_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        front_label.grid(row=2, column=0, padx=5, pady=5)
        back_label.grid(row=2, column=1, padx=5, pady=5)
        self._create_flashcard_front_entry.grid(row=3, column=0, padx=5, pady=5)
        self._create_flashcard_back_entry.grid(row=3, column=1, padx=5, pady=5)
        create_flashcard_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self._flashcard_list_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)