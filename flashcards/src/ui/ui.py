from tkinter import ttk, constants
from ui.login_view import LoginView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
    
    def _show_login_view(self):
        self._current_view = LoginView(self._root)
        self._current_view.pack()