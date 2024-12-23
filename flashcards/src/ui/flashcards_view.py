from tkinter import ttk, constants, messagebox
from services.flashcard_service import flashcard_service


class FlashcardsListView:
    """Class for creating the list view of flashcards.
    """

    def __init__(self, root, flashcards, collection, handle_delete_flashcard):
        """Class constructor for FlashcardsListView.

        Args:
            root (ttk.Frame): The parent Frame.
            flashcards (list): list of Flashcard entities.
            collection (Collection): list of Collection entities.
            handle_delete_flashcard (funct): Method to be called when deleting flashcard. Takes a Flashcard entity as argument.
        """
        self._root = root
        self._frame = None
        self._flashcards = flashcards
        self._collection = collection
        self._user_id = flashcard_service.get_user_id()
        self._handle_delete_flashcard = handle_delete_flashcard

        self._initialize()

    def pack(self):
        """Shows the view.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view.
        """
        self._frame.destroy()

    def _initialize_flashcard(self, flashcard, i):
        front_label = ttk.Label(
            master=self._frame, text=flashcard.front, wraplength=300)
        back_label = ttk.Label(
            master=self._frame, text=flashcard.back, wraplength=300)
        delete_button = ttk.Button(
            master=self._frame,
            text="Poista",
            command=lambda: self._handle_delete_flashcard(flashcard)
        )

        front_label.grid(row=i, column=0, padx=10, pady=5)
        back_label.grid(row=i, column=2, padx=10, pady=5)

        if self._user_id == self._collection.creator_id:
            delete_button.grid(row=i, column=4, padx=10, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        i = 0

        for flashcard in self._flashcards:
            self._initialize_flashcard(flashcard, i)
            i += 1

        if i > 0:
            separator1 = ttk.Separator(
                master=self._frame, orient=constants.VERTICAL)
            separator2 = ttk.Separator(
                master=self._frame, orient=constants.VERTICAL)
            separator1.grid(row=0, column=1, rowspan=i, sticky=constants.NS)
            if self._user_id == self._collection.creator_id:
                separator2.grid(row=0, column=3, rowspan=i,
                                sticky=constants.NS)
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(2, weight=1)


class FlashcardsView:
    """Class for creating the flashcards (contents of collection) view.
    """

    def __init__(self, root, handle_practice_view, handle_collections_view):
        """Class constructor for FlashcardsView.

        Args:
            root (Tk): Top-level Tkinter element.
            handle_practice_view (funct): Method for showing the practice view.
            handle_collections_view (funct): Method for showing the collections view.
        """
        self._root = root
        self._frame = None
        self._flashcard_list_frame = None
        self._flashcard_list_view = None
        self._handle_practice_view = handle_practice_view
        self._handle_collections_view = handle_collections_view

        self._create_flashcard_front_entry = None
        self._create_flashcard_back_entry = None

        self._collection = flashcard_service.get_collection()

        self._initialize()

    def pack(self):
        """Shows the view.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view.
        """
        self._frame.destroy()

    def _initialize_flashcards_list(self):
        if self._flashcard_list_view:
            self._flashcard_list_view.destroy()

        flashcards = flashcard_service.get_flashcards_from_collection(
            self._collection)

        self._flashcard_list_view = FlashcardsListView(
            self._flashcard_list_frame, flashcards, self._collection, self._handle_delete_flashcard)
        self._flashcard_list_view.pack()

    def _handle_create_flashcard(self):
        flashcard_front = self._create_flashcard_front_entry.get()
        flashcard_back = self._create_flashcard_back_entry.get()

        if flashcard_front and flashcard_back:
            success = flashcard_service.create_flashcard(
                flashcard_front, flashcard_back, self._collection.id)
            if success:
                self._initialize_flashcards_list()
                self._create_flashcard_front_entry.delete(0, constants.END)
                self._create_flashcard_back_entry.delete(0, constants.END)
            else:
                messagebox.showerror("Virhe", flashcard_service.get_message())

    def _handle_delete_flashcard(self, flashcard):
        flashcard_service.delete_flashcard(flashcard)
        self._initialize_flashcards_list()

    def _handle_practice_start(self):
        if flashcard_service.collection_not_empty():
            self._handle_practice_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._flashcard_list_frame = ttk.Frame(master=self._frame)

        self._initialize_flashcards_list()

        header_label = ttk.Label(
            master=self._frame, text=f"Kokoelma: {self._collection.name}")
        header_label.config(font=("TkDefaultFont", 15, "bold"))
        front_label = ttk.Label(master=self._frame, text="Etupuoli")
        back_label = ttk.Label(master=self._frame, text="Takapuoli")
        self._create_flashcard_front_entry = ttk.Entry(master=self._frame)
        self._create_flashcard_back_entry = ttk.Entry(master=self._frame)
        create_flashcard_button = ttk.Button(
            master=self._frame, text="Lisää flashcard", command=self._handle_create_flashcard)
        practice_collection_button = ttk.Button(
            master=self._frame, text="Harjoittele kokoelmaa", command=self._handle_practice_start)
        # note: add method to empty flashcard_service current collection
        return_to_collections_button = ttk.Button(
            master=self._frame, text="Takaisin kokoelmiin", command=self._handle_collections_view)

        header_label.grid(row=0, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)
        return_to_collections_button.grid(
            row=1, column=0, columnspan=2, padx=5, pady=5, sticky=constants.EW)
        practice_collection_button.grid(
            row=2, column=0, columnspan=2, padx=5, pady=5, sticky=constants.EW)

        if flashcard_service.get_user_id() == self._collection.creator_id:
            self._create_flashcard_front_entry.grid(
                row=4, column=0, padx=5, pady=5, sticky=constants.EW)
            self._create_flashcard_back_entry.grid(
                row=4, column=1, padx=5, pady=5, sticky=constants.EW)
            create_flashcard_button.grid(
                row=5, column=0, columnspan=2, padx=5, pady=5, sticky=constants.EW)
            front_label.grid(row=3, column=0, padx=5, pady=5)
            back_label.grid(row=3, column=1, padx=5, pady=5)
        self._flashcard_list_frame.grid(
            row=6, column=0, columnspan=2, padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
