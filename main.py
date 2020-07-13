try:
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.messagebox as messagebox
    import sys

    from Weather import Weather
except ImportError as error:
    print(error)
    sys.exit()


class Application:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Météo")
        self.root.geometry("500x500+500+100")

        self.fontStyle = tkFont.Font(family="Lucida Grande", size=15)

        self.frame_city = tk.Frame(self.root, width=500, height=200)
        self.frame_city.pack()
        self.info_city = tk.Frame(self.root, width=500, height=500)
        self.info_city.pack()

        self.make_widget_form()
        self.root.mainloop()

        self.entry = None

    def make_widget_form(self):
        tk.Label(self.frame_city, text="Ville").pack()

        city_name = tk.StringVar()
        self.entry = tk.Entry(self.frame_city, textvariable=city_name, width=30)
        self.entry.pack(padx=10, pady=10)

        weather_btn = tk.Button(self.frame_city, text="Chercher la météo dans cette ville", command=self.get_weather)
        weather_btn.pack(padx=10, pady=20)

        quit_btn = tk.Button(self.frame_city, text="Quitter", command=self.root.quit)
        quit_btn.pack()

        self.root.bind_all("<Return>", self.get_weather)

    def get_weather(self, event=None):
        for widget in self.info_city.winfo_children():
            widget.destroy()

        city_name = self.entry.get()
        if len(city_name) != 0:
            weather = Weather(city_name)
            informations = weather.extract_component(city_name+".txt")

            name_label = tk.Label(self.info_city, text="Météo actuelle à " + city_name, font=self.fontStyle)
            name_label.grid(padx=20, pady=15)

            cloud_label = tk.Label(self.info_city, text="Temps: " + informations[0], font=self.fontStyle)
            cloud_label.grid(padx=10, pady=10)
            temp_label = tk.Label(self.info_city, text="Température: " + str(informations[1]), font=self.fontStyle)
            temp_label.grid(padx=10, pady=10)
            preassure_label = tk.Label(self.info_city, text="Pression: " + str(informations[2]) + "hPa",
                                       font=self.fontStyle)
            preassure_label.grid(padx=10, pady=10)
            humidity_label = tk.Label(self.info_city, text="Humidité: " + str(informations[3]) + "%",
                                      font=self.fontStyle)
            humidity_label.grid(padx=10, pady=10)

        else:
            messagebox.showerror("Erreur", "Le nom de la ville est vide.")


if __name__ == "__main__":
    app = Application()