from tkinter import ttk, constants
from services.flashcard_service import flashcard_service

class CollectionsView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(master=self._frame, text="Flashcard-kokoelmat")
        logout_button = ttk.Button(master=self._frame, text="Kirjaudu ulos", command=self._logout_handler)
        
        header_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        logout_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
    
    def _logout_handler(self):
        flashcard_service.logout()
        self._handle_logout()