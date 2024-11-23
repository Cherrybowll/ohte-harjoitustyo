from tkinter import Tk
from ui.ui import UI

# note: remains for exploratory testing purposes
# from initialize_database import initialize_database
# initialize_database()


def main():
    window = Tk()
    window.title("Flashcard-sovellus")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
