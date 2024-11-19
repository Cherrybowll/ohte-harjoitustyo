from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_login):
        self._root = root
        self._frame = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(master=self._frame, text="Sisäänkirjautuminen")
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        username_entry = ttk.Entry(master=self._frame)
        passwod_label = ttk.Label(master=self._frame, text="Salasana")
        password_entry = ttk.Entry(master=self._frame)
        login_button = ttk.Button(master=self._frame, text="Kirjaudu")
        
        header_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.EW), padx=5, pady=5)
        passwod_label.grid(row=2, column=0, padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.EW), padx=5, pady=5)
        login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)