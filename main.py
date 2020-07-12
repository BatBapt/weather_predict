import tkinter as tk


class Application:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Météo")
        self.root.geometry("500x500+500+100")
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()