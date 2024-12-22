from tkinter import ttk, constants, messagebox
from services.flashcard_service import flashcard_service


class LoginView:
    """Class for showing the login view.
    """
    def __init__(self, root, handle_collections_view, handle_register_view):
        """Class constructor for LoginView.

        Args:
            root (Tk): Top-level Tkinter element.
            handle_collections_view (funct): Handles showing the collections view.
            handle_register_view (funct): Handles showing the register view.
        """
        self._root = root
        self._frame = None

        self._handle_collections_view = handle_collections_view
        self._handle_register_view = handle_register_view

        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        """Shows the view.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the view.
        """
        self._frame.destroy()

    def _login_handler(self):
        username, password = self._username_entry.get(), self._password_entry.get()
        success = flashcard_service.login(username, password)
        if success:
            self._handle_collections_view()
        else:
            messagebox.showerror("Virhe", flashcard_service.get_message())

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._frame, text="Sisäänkirjautuminen")
        header_label.config(font=("TkDefaultFont", 15, "bold"))
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._frame)
        passwod_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame, show="*")
        login_button = ttk.Button(
            master=self._frame, text="Kirjaudu", command=self._login_handler)
        register_button = ttk.Button(
            master=self._frame, text="Rekisteröidy", command=self._handle_register_view)

        header_label.grid(row=0, column=0, columnspan=2,
                          sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(
            row=1, column=1, sticky=(constants.EW), padx=5, pady=5)
        passwod_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(
            row=2, column=1, sticky=(constants.EW), padx=5, pady=5)
        login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        register_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
