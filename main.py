import tkinter as tk
from Weather import Weather


class Application:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Météo")
        self.root.geometry("500x500+500+100")
        self.make_widget()
        self.root.mainloop()

        self.entry = None

    def make_widget(self):
        frame_city = tk.Frame(self.root, width=500, height=200)
        frame_city.pack()

        tk.Label(frame_city, text="Ville").pack()

        city_name = tk.StringVar()
        self.entry = tk.Entry(frame_city, textvariable=city_name, width=30)
        self.entry.pack()

        weather_btn = tk.Button(frame_city, text="Chercher la météo dans cette ville", command=self.get_weather)
        weather_btn.pack()

        self.root.bind_all("<Return>", self.get_weather)

    def get_weather(self, event=None):
        city_name = self.entry.get()
        if len(city_name) != 0:
            weather = Weather(city_name)
            weather.extract_component(city_name+".txt")



if __name__ == "__main__":
    app = Application()