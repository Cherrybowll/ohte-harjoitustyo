from tkinter import ttk, constants, StringVar
from services.flashcard_service import flashcard_service


class PracticeFrontView:
    """Class for showing the front side of the current Flashcard in practice mode.
    """

    def __init__(self, root, flashcard, handle_turn):
        """Class constructor for PracticeFrontView.

        Args:
            root (ttk.Frame): The parent Frame.
            flashcard (Flashcard): a Flashcard entity.
            handle_turn (funct): Handles turning the flashcard backside.
        """
        self._root = root
        self._frame = None
        self._flashcard = flashcard
        self._handle_turn = handle_turn

        self._initialize()

    def pack(self):
        """Shows the view.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view.
        """
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        item_frame = ttk.Frame(master=self._frame)
        front_label = ttk.Label(master=item_frame, text=self._flashcard.front)
        turn_button = ttk.Button(
            master=item_frame, text="Käännä", command=self._handle_turn)

        front_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        turn_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        item_frame.pack(fill=constants.X)


class PracticeBackView:
    """Class for showing the back side of the current Flashcard in practice mode.
    """

    def __init__(self, root, flashcard, handle_next):
        """Class constructor for PracticeBackView.

        Args:
            root (ttk.Frame): The parent Frame.
            flashcard (Flashcard): a Flashcard entity.
            handle_next (funct): Handles progressing the practice state and view.
        """
        self._root = root
        self._frame = None
        self._flashcard = flashcard
        self._handle_next = handle_next

        self._initialize()

    def pack(self):
        """Shows the view.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view.
        """
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        item_frame = ttk.Frame(master=self._frame)
        back_label = ttk.Label(master=item_frame, text=self._flashcard.back)
        query_label = ttk.Label(master=item_frame, text="Osasitko?")
        yes_button = ttk.Button(
            master=item_frame, text="Kyllä", command=lambda: self._handle_next(True))
        no_button = ttk.Button(master=item_frame, text="Ei",
                               command=lambda: self._handle_next(False))

        back_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        query_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        yes_button.grid(row=2, column=0, padx=5, pady=5)
        no_button.grid(row=2, column=1, padx=5, pady=5)
        item_frame.pack(fill=constants.X)


class PracticeView:
    """Class for showing the practice mode view.
    """

    def __init__(self, root, handle_flashcards_view, handle_results_view):
        """Class constructor for PracticeView.

        Args:
            root (Tk): Top-level Tkinter element.
            handle_flashcards_view (funct): Handles showing the flashcards view.
            handle_results_view (funct): Handles showing the results view.
        """
        self._root = root
        self._frame = None
        self._current_flashcard_frame = None
        self._current_flashcard_view = None
        self._handle_flashcards_view = handle_flashcards_view
        self._handle_results_view = handle_results_view
        self._collection = flashcard_service.get_collection()
        self._flashcards = flashcard_service.get_flashcards_from_collection(
            self._collection)
        self._current_card_variable = None

        self._initialize()

    def pack(self):
        """Shows the current view.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the current view.
        """
        self._frame.destroy()

    def _handle_turn_flashcard(self):
        if self._current_flashcard_view:
            self._current_flashcard_view.destroy()

        current = flashcard_service.current_flashcard()
        self._current_flashcard_view = PracticeBackView(
            self._current_flashcard_frame,
            self._flashcards[current],
            self._handle_next_flashcard
        )
        self._current_flashcard_view.pack()

    def _handle_next_flashcard(self, was_correct):
        more_cards = flashcard_service.progress_practice(was_correct)
        if more_cards:
            self._current_card_variable.set(
                f"{flashcard_service.current_flashcard()+1} / {len(self._flashcards)}")
            self._initialize_current_flashcard()
        else:
            self._handle_results_view()

    def _initialize_current_flashcard(self):
        if self._current_flashcard_view:
            self._current_flashcard_view.destroy()

        current = flashcard_service.current_flashcard()
        self._current_flashcard_view = PracticeFrontView(
            self._current_flashcard_frame, self._flashcards[current], self._handle_turn_flashcard)
        self._current_flashcard_view.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._current_flashcard_frame = ttk.Frame(master=self._frame)
        self._current_card_variable = StringVar()
        self._current_card_variable.set(f"1 / {len(self._flashcards)}")
        self._current_card_label = ttk.Label(
            master=self._frame, textvariable=self._current_card_variable)

        flashcard_service.start_practice()
        self._initialize_current_flashcard()

        header_label = ttk.Label(
            master=self._frame, text=f"Kokoelma: {self._collection.name}")
        header_label.config(font=("TkDefaultFont", 15, "bold"))

        header_label.grid(row=0, column=0, columnspan=2,
                          padx=5, pady=5, sticky=constants.W)
        self._current_flashcard_frame.grid(
            row=1, column=0, columnspan=2, padx=5, pady=5)
        self._current_card_label.grid(row=2, column=0, padx=5, pady=5)
