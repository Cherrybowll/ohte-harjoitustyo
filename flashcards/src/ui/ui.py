from tkinter import ttk, constants
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.collections_view import CollectionsView
from ui.flashcards_view import FlashcardsView
from ui.practice_view import PracticeView
from ui.results_view import ResultsView
from ui.public_collections_view import PublicCollectionsView
from config import COLOR_SCHEME


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._style = ttk.Style()
        self._default_style()

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root, self._show_collections_view, self._show_register_view)
        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(
            self._root, self._show_collections_view, self._show_login_view)
        self._current_view.pack()

    def _show_collections_view(self):
        self._hide_current_view()
        self._current_view = CollectionsView(
            self._root, self._show_login_view, self._show_flashcards_view)
        self._current_view.pack()

    def _show_public_collections_view(self):
        self._hide_current_view()
        self._current_view = PublicCollectionsView(
            self._root, self._show_login_view, self._show_flashcards_view, self._show_collections_view)
        self._current_view.pack()

    def _show_flashcards_view(self):
        self._hide_current_view()
        self._current_view = FlashcardsView(
            self._root, self._show_practice_view, self._show_collections_view)
        self._current_view.pack()

    def _show_practice_view(self):
        self._hide_current_view()
        self._current_view = PracticeView(
            self._root, self._show_flashcards_view, self._show_results_view)
        self._current_view.pack()

    def _show_results_view(self):
        self._hide_current_view()
        self._current_view = ResultsView(
            self._root, self._show_flashcards_view)
        self._current_view.pack()

    def _default_style(self):
        bg_color, text_color, btn_color = "", "", ""
        match COLOR_SCHEME:
            case "orange":
                bg_color = "#FAB12F"
                text_color = "#FEF3E2"
                btn_color = "#FA4032"
            case "cherry":
                bg_color = "#FFCCE1"
                text_color = "#FFFFFF"
                btn_color = "#E195AB"
            case "green":
                bg_color = "#5A6C57"
                text_color = "#D3F1DF"
                btn_color = "#85A98F"
            case _:
                # Defaults to orange
                bg_color = "#E5C3A7"
                text_color = "#FFFFFF"
                btn_color = "#E5A970"


        self._root.option_add("*Background", bg_color)
        self._root.option_add("*Foreground", text_color)

        self._style.configure("TFrame", background=bg_color)
        self._style.configure("TLabel", background=bg_color, foreground=text_color)
        self._style.configure("TCheckbutton", background=bg_color, foreground=text_color)
        self._style.configure("TButton", background=btn_color, foreground=text_color)
