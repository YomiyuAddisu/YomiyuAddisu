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

# Traffic Light display and car status
    traffic_light_color = "green" if traffic.color == "green" else "red"
    traffic_label = tk.Label(output_frame, text=f"🚦 Traffic Light: {traffic.display()}", fg=traffic_light_color, font=("Arial", 12, "bold"))
    traffic_label.pack(anchor="w")

    car_status = traffic.car_status()
    car_color = "green" if traffic.color == "green" else "red"
    car_label = tk.Label(output_frame, text=f"🚗 Car: {car_status}", fg=car_color, font=("Arial", 12))
    car_label.pack(anchor="w")

    # Garbage system display
    garbage_status_color = "orange" if garbage.status == "COLLECTING" else "green"
    garbage_label = tk.Label(output_frame, text=f"🗑 Garbage Level: {garbage.level}%  |  Status: {garbage.status}", fg=garbage_status_color, font=("Arial", 12))
    garbage_label.pack(anchor="w")

    # Weather display
    if weather.is_raining:
        weather_text = "🌧 Weather: RAINING"
        weather_color = "blue"
    else:
        weather_text = "☀️ Weather: CLEAR"
        weather_color = "orange"
    weather_label = tk.Label(output_frame, text=weather_text, fg=weather_color, font=("Arial", 12))
    weather_label.pack(anchor="w")

    # Fire alert display
    fire_color = "red" if fire_alert.fire else "green"
    fire_text = "🔥 Fire: DETECTED! 🚒 CALL EMERGENCY!" if fire_alert.fire else "🔥 Fire: Safe ✅"
    fire_label = tk.Label(output_frame, text=fire_text, fg=fire_color, font=("Arial", 12, "bold"))
    fire_label.pack(anchor="w")
# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Smart City Simulation")

welcome_label = tk.Label(root, text="Welcome to AAiT Pre-engineering Section 10", font=("Arial", 16, "bold"))
welcome_label.pack(pady=(10, 0))

encourage_label = tk.Label(root, text="We encourage you to write with confidence", font=("Arial", 12))
encourage_label.pack(pady=(0, 20))

input_frame = tk.Frame(root)
input_frame.pack(padx=20)
tk.Label(input_frame, text="Enter current hour (0–23):").grid(row=0, column=0, sticky="e", pady=2)
hour_entry = tk.Entry(input_frame, width=10)
hour_entry.grid(row=0, column=1, pady=2)

tk.Label(input_frame, text="Enter traffic light color (red/green):").grid(row=1, column=0, sticky="e", pady=2)
traffic_entry = tk.Entry(input_frame, width=10)
traffic_entry.grid(row=1, column=1, pady=2)

tk.Label(input_frame, text="Enter garbage level (0–100):").grid(row=2, column=0, sticky="e", pady=2)
garbage_entry = tk.Entry(input_frame, width=10)
garbage_entry.grid(row=2, column=1, pady=2)

tk.Label(input_frame, text="Is it raining? (yes/no):").grid(row=3, column=0, sticky="e", pady=2)
raining_entry = tk.Entry(input_frame, width=10)
raining_entry.grid(row=3, column=1, pady=2)

tk.Label(input_frame, text="Is fire detected? (yes/no):").grid(row=4, column=0, sticky="e", pady=2)
fire_entry = tk.Entry(input_frame, width=10)
fire_entry.grid(row=4, column=1, pady=2)
