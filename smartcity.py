import tkinter as tk
from tkinter import messagebox

class TrafficLight:
    def init(self, color):
        self.color = color.lower()

    def car_status(self):
        return "STOPPED 🚗" if self.color == "red" else "MOVING 🚗"

    def display(self):
        return self.color.upper()

class StreetLight:
    def init(self, hour):
        self.is_on = hour >= 18 or hour < 6

    def display(self):
        return "ON" if self.is_on else "OFF"

class GarbageSystem:
    def init(self, level):
        self.level = level
        self.status = "COLLECTING" if level > 80 else "NORMAL"

    def display(self):
        return f"Level: {self.level}% | Status: {self.status}"

class WeatherSystem:
    def init(self, raining):
        self.is_raining = raining

    def display(self):
        return "RAINING" if self.is_raining else "CLEAR"

class FireAlert:
    def init(self, detected):
        self.fire = detected

    def display(self):
        return "DETECTED" if self.fire else "SAFE"
def run_simulation():
    try:
        hour = int(hour_entry.get())
        if not (0 <= hour <= 23):
            raise ValueError("Hour must be between 0 and 23.")

        traffic_color = traffic_entry.get().strip().lower()
        if traffic_color not in ("red", "green"):
            raise ValueError("Traffic light color must be 'red' or 'green'.")

        garbage_level = int(garbage_entry.get())
        if not (0 <= garbage_level <= 100):
            raise ValueError("Garbage level must be between 0 and 100.")

        raining_input = raining_entry.get().strip().lower()
        if raining_input not in ("yes", "no"):
            raise ValueError("Raining input must be 'yes' or 'no'.")
        raining = raining_input == "yes"

        fire_input = fire_entry.get().strip().lower()
        if fire_input not in ("yes", "no"):
            raise ValueError("Fire input must be 'yes' or 'no'.")
        fire = fire_input == "yes"

    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))
        return

        traffic = TrafficLight(traffic_color)
    street = StreetLight(hour)
    garbage = GarbageSystem(garbage_level)
    weather = WeatherSystem(raining)
    fire_alert = FireAlert(fire)

    # Clear previous output colors
    for widget in output_frame.winfo_children():
        widget.destroy()

    # Time label
    time_label = tk.Label(output_frame, text=f"🕒 Time: {hour:02d}:00", font=("Arial", 12, "bold"))
    time_label.pack(anchor="w")

    # Street Light display
    street_color = "yellow" if street.is_on else "gray30"
    street_label = tk.Label(output_frame, text=f"💡 Street Light: {street.display()}", fg=street_color, font=("Arial", 12))
    street_label.pack(anchor="w")
