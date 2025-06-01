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
