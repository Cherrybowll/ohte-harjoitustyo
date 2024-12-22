from tkinter import Tk
from ui.ui import UI


def main():
    """Runs the main program loop.
    """
    window = Tk()
    window.title("Flashcard-sovellus")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
