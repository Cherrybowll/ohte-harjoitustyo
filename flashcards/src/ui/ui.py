from tkinter import ttk, constants
from ui.login_view import LoginView
from ui.collections_view import CollectionsView
from ui.register_view import RegisterView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = None
    
    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._show_collections_view, self._show_register_view)
        self._current_view.pack()
    
    def _show_collections_view(self):
        self._hide_current_view()
        self._current_view = CollectionsView(self._root, self._show_login_view)
        self._current_view.pack()
    
    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(self._root, self._show_collections_view, self._show_login_view)
        self._current_view.pack()