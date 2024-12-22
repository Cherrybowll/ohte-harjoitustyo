from tkinter import ttk, constants, messagebox, BooleanVar, StringVar, simpledialog
from services.flashcard_service import flashcard_service


class CollectionListView:
    """Class for showing the list view for collections.
    """
    def __init__(self, root, collections, handle_flashcards_view, handle_flashcards, handle_delete_collection, handle_copy_collection, handle_make_public):
        """Class constructor for CollectionListView.

        Args:
            root (ttk.Frame): The parent Frame.
            collections (list): list of Collection entities.
            handle_flashcards_view (funct): Handles showing the flashcards view.
            handle_flashcards (funct): Handles showing the flashcards view.
            handle_delete_collection (funct): Handles deleting the collection.
            handle_copy_collection (funct): Handles copying the collection.
            handle_make_public (funct): Handles toggling the publicity status of the collection.
        """
        self._root = root
        self._collections = collections
        self._user_id = flashcard_service.get_user_id()
        self._frame = None
        self._handle_flashcards_view = handle_flashcards_view # USELESS
        self._handle_flashcards = handle_flashcards
        self._handle_delete_collection = handle_delete_collection
        self._handle_copy_collection = handle_copy_collection
        self._handle_make_public = handle_make_public
        self._public_vars = [BooleanVar()
                             for i in range(len(self._collections))]
        self._viewing_public = flashcard_service.get_public_view_state()

        self._initialize()

    def pack(self):
        """Shows the view.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view.
        """
        self._frame.destroy()

    def _initialize_collection(self, collection, i):
        label = ttk.Label(master=self._frame, text=collection.name)

        self._public_vars[i].set(collection.public)
        make_public_checkbox = ttk.Checkbutton(
            master=self._frame,
            text="Julkinen",
            variable=self._public_vars[i],
            command=lambda: self._handle_make_public(collection)
        )

        open_collection_button = ttk.Button(
            master=self._frame, text="Avaa", command=lambda: self._handle_flashcards(collection))
        delete_collection_button = ttk.Button(
            master=self._frame,
            text="Poista",
            command=lambda: self._handle_delete_collection(collection)
        )
        copy_collection_button = ttk.Button(
            master=self._frame,
            text="Kopioi",
            command=lambda: self._handle_copy_collection(collection)
        )
        if self._user_id != collection.creator_id:
            delete_collection_button.config(state=constants.DISABLED)
            make_public_checkbox.config(state=constants.DISABLED)

        label.grid(row=i, column=0, padx=5, pady=5, sticky=constants.EW)
        open_collection_button.grid(
            row=i, column=1, padx=5, pady=5, sticky=constants.EW)
        delete_collection_button.grid(
            row=i, column=2, padx=5, pady=5, sticky=constants.EW)
        copy_collection_button.grid(
            row=i, column=3, padx=5, pady=5, sticky=constants.EW)
        make_public_checkbox.grid(
            row=i, column=4
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        i = 0  # Index for grid row
        for collection in self._collections:
            self._initialize_collection(collection, i)
            i += 1

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)


class CollectionsView:
    """Class for showing the collections view.
    """
    def __init__(self, root, handle_login_view, handle_flashcards_view):
        """Class constructor for CollectionsView.

        Args:
            root (Tk): Top-level Tkinter element.
            handle_login_view (funct): Handles showing the login view.
            handle_flashcards_view (funct): Handles showing the flashcard view.
        """
        self._root = root
        self._handle_login_view = handle_login_view
        self._handle_flashcards_view = handle_flashcards_view
        self._frame = None
        self._collection_list_frame = None
        self._collection_list_view = None
        self._create_collection_entry = None
        self._public_private_var = StringVar()
        self._public_private_switch_var = StringVar()
        self._viewing_public = flashcard_service.get_public_view_state()

        self._initialize()

    def pack(self):
        """Shows the view.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view.
        """
        self._frame.destroy()

    def _logout_handler(self):
        flashcard_service.logout()
        self._handle_login_view()

    def _initialize_collection_list(self):
        if self._collection_list_view:
            self._collection_list_view.destroy()

        if self._viewing_public:
            collections = flashcard_service.get_all_public_collections()
        else:
            collections = flashcard_service.get_collections_from_user()

        self._collection_list_view = CollectionListView(
            self._collection_list_frame,
            collections,
            self._handle_flashcards_view,
            self._handle_flashcards,
            self._handle_delete_collection,
            self._handle_copy_collection,
            self._handle_make_public
        )

        self._collection_list_view.pack()

    def _switch_public_private_view(self, to_public):
        flashcard_service.set_public_view_state(to_public)
        self._viewing_public = flashcard_service.get_public_view_state()
        if self._viewing_public:
            self._public_private_switch_var.set("Omat kokoelmat")
            self._public_private_var.set("Julkiset kokoelmat")
        else:
            self._public_private_switch_var.set("Julkiset kokoelmat")
            self._public_private_var.set("Omat kokoelmat")
        self._initialize_collection_list()

    def _handle_create_collection(self):
        collection_name = self._create_collection_entry.get()

        if collection_name:
            success = flashcard_service.create_collection(collection_name)
            if success:
                self._initialize_collection_list()
                self._create_collection_entry.delete(0, constants.END)
            else:
                messagebox.showerror("Virhe", flashcard_service.get_message())

    def _handle_delete_collection(self, collection):
        user_confirmation = messagebox.askokcancel(
            title="Kokoelman poistaminen",
            message="Kokoelman poistaminen on peruuttamaton operaatio. Haluatko varmasti jatkaa?"
        )
        if user_confirmation:
            flashcard_service.delete_collection(collection)
            self._initialize_collection_list()

    def _handle_copy_collection(self, collection):
        copy_name = simpledialog.askstring(
            "Kopio", "Anna kopiolle nimi:", initialvalue=f"{collection.name}_kopio")
        if copy_name == None:
            return

        success = flashcard_service.create_collection(copy_name)
        if success:
            copy_collection = flashcard_service.get_collection_from_user_with_name(
                flashcard_service.get_user_id(), copy_name
            )
            copy_flashcards = flashcard_service.get_flashcards_from_collection(collection)
            for flashcard in copy_flashcards:
                flashcard_service.create_flashcard(
                    flashcard.front, flashcard.back, copy_collection.id)
        else:
            messagebox.showerror("Virhe", flashcard_service.get_message())
        self._initialize_collection_list()

    def _handle_make_public(self, collection):
        flashcard_service.collection_toggle_public(collection)
        self._initialize_collection_list()

    def _handle_flashcards(self, collection):
        flashcard_service.open_collection(collection)
        self._handle_flashcards_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._collection_list_frame = ttk.Frame(master=self._frame)

        self._switch_public_private_view(self._viewing_public)

        self._initialize_collection_list()

        header_label = ttk.Label(
            master=self._frame, text="Flashcard-kokoelmat")
        header_label.config(font=("TkDefaultFont", 15, "bold"))
        switch_view_public_button = ttk.Button(
            master=self._frame,
            textvariable=self._public_private_switch_var,
            command=lambda: self._switch_public_private_view(not self._viewing_public)
        )
        collections_label = ttk.Label(
            master=self._frame, textvariable=self._public_private_var)
        self._create_collection_entry = ttk.Entry(master=self._frame)
        create_collection_button = ttk.Button(
            master=self._frame, text="Luo kokoelma", command=self._handle_create_collection)
        logout_button = ttk.Button(
            master=self._frame, text="Kirjaudu ulos", command=self._logout_handler)

        header_label.grid(row=0, column=0, columnspan=2,
                          sticky=constants.W, padx=5, pady=5)
        collections_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        switch_view_public_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self._collection_list_frame.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky=constants.EW)
        self._create_collection_entry.grid(
            row=4, column=0, padx=5, pady=5, sticky=constants.EW)
        create_collection_button.grid(
            row=4, column=1, padx=5, pady=5, sticky=constants.EW)
        logout_button.grid(row=5, column=0, columnspan=2,
                           padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
