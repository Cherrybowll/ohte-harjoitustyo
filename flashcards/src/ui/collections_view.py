from tkinter import ttk, constants
from services.flashcard_service import flashcard_service


class CollectionListView:
    def __init__(self, root, collections, handle_flashcards_view, handle_flashcards):
        self._root = root
        self._collections = collections
        self._frame = None
        self._handle_flashcards_view = handle_flashcards_view
        self._handle_flashcards = handle_flashcards

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_collection(self, collection):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=collection.name)
        open_collection_button = ttk.Button(master=item_frame, text="Avaa", command=lambda: self._handle_flashcards(collection))

        label.grid(row=0, column=0, padx=5, pady=5)
        open_collection_button.grid(row=0, column=1, padx=5, pady=5)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for collection in self._collections:
            self._initialize_collection(collection)


class CollectionsView:
    def __init__(self, root, handle_logout, handle_flashcards):
        self._root = root
        self._handle_logout = handle_logout
        self._handle_flashcards_view = handle_flashcards
        self._frame = None
        self._collection_list_frame = None
        self._collection_list_view = None
        self._create_collection_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        flashcard_service.logout()
        self._handle_logout()

    def _initialize_collection_list(self):
        if self._collection_list_view:
            self._collection_list_view.destroy()

        collections = flashcard_service.get_all_collections()

        self._collection_list_view = CollectionListView(
            self._collection_list_frame,
            collections,
            self._handle_flashcards_view,
            self._handle_flashcards
        )

        self._collection_list_view.pack()

    def _handle_create_collection(self):
        collection_name = self._create_collection_entry.get()

        if collection_name:
            flashcard_service.create_collection(collection_name)
            self._initialize_collection_list()
            self._create_collection_entry.delete(0, constants.END)

    def _handle_flashcards(self, collection):
        flashcard_service.open_collection(collection)
        self._handle_flashcards_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._collection_list_frame = ttk.Frame(master=self._frame)

        self._initialize_collection_list()

        header_label = ttk.Label(
            master=self._frame, text="Flashcard-kokoelmat")
        self._create_collection_entry = ttk.Entry(master=self._frame)
        create_collection_button = ttk.Button(
            master=self._frame, text="Luo kokoelma", command=self._handle_create_collection)
        logout_button = ttk.Button(
            master=self._frame, text="Kirjaudu ulos", command=self._logout_handler)

        header_label.grid(row=0, column=0, columnspan=2,
                          sticky=constants.EW, padx=5, pady=5)
        self._collection_list_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self._create_collection_entry.grid(row=2, column=0, padx=5, pady=5)
        create_collection_button.grid(row=2, column=1, padx=5, pady=5)
        logout_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
