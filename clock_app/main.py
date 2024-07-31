import tkinter as tk
import math
from datetime import datetime

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        self.root.geometry("400x400")

        # Default to dark mode
        self.is_dark_mode = True
        self.set_dark_mode()

        # Create a frame to center content
        self.frame = tk.Frame(self.root, bg=self.bg_color)
        self.frame.pack(expand=True)

        # Create canvas for analog clock
        self.canvas = tk.Canvas(self.frame, width=250, height=250, bg=self.bg_color, bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=20, pady=10)

        # Create labels for digital clock
        self.time_var = tk.StringVar()
        self.date_var = tk.StringVar()

        self.time_label = tk.Label(self.frame, textvariable=self.time_var, font=('Heebo', 40), bg=self.bg_color, fg=self.fg_color)
        self.time_label.grid(row=1, column=0, pady=10)

        self.date_label = tk.Label(self.frame, textvariable=self.date_var, font=('Heebo', 14), bg=self.bg_color, fg=self.fg_color)
        self.date_label.grid(row=2, column=0, pady=10)

        # Toggle button
        self.toggle_button = tk.Button(self.frame, text="Dark mode", command=self.toggle_mode, bg=self.toggle_bg_color, fg=self.toggle_fg_color)
        self.toggle_button.grid(row=3, column=0, pady=10)

        self.update_clock()
        self.root.mainloop()

    def set_dark_mode(self):
        self.bg_color = 'black'
        self.fg_color = 'white'
        self.toggle_bg_color = 'white'
        self.toggle_fg_color = 'black'

    def set_light_mode(self):
        self.bg_color = 'white'
        self.fg_color = 'black'
        self.toggle_bg_color = 'black'
        self.toggle_fg_color = 'white'

    def draw_hand(self, angle, length, color, width):
        angle_rad = math.radians(angle)
        x_end = 125 + length * math.cos(angle_rad - math.pi / 2)
        y_end = 125 + length * math.sin(angle_rad - math.pi / 2)
        self.canvas.create_line(125, 125, x_end, y_end, fill=color, width=width)

    def update_clock(self):
        now = datetime.now()

        # Update digital clock
        self.time_var.set(now.strftime('%I:%M:%S %p'))
        self.date_var.set(now.strftime('%A, %b %d'))

        # Update analog clock
        self.canvas.delete("all")
        self.canvas.create_oval(25, 25, 225, 225, outline=self.fg_color, width=2)
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        self.draw_hand(30 * (hours % 12) + minutes / 2, 50, self.fg_color, 6)  # Hour hand
        self.draw_hand(6 * minutes, 80, self.fg_color, 4)  # Minute hand
        self.draw_hand(6 * seconds, 90, 'red', 2)  # Second hand

        self.root.after(1000, self.update_clock)  # Update the clock every second

    def toggle_mode(self):
        if self.is_dark_mode:
            self.set_light_mode()
            self.toggle_button.configure(text="Light mode", bg=self.toggle_bg_color, fg=self.toggle_fg_color)
        else:
            self.set_dark_mode()
            self.toggle_button.configure(text="Dark mode", bg=self.toggle_bg_color, fg=self.toggle_fg_color)

        # Apply the new colors
        self.root.configure(bg=self.bg_color)
        self.frame.configure(bg=self.bg_color)
        self.canvas.configure(bg=self.bg_color)
        self.time_label.configure(bg=self.bg_color, fg=self.fg_color)
        self.date_label.configure(bg=self.bg_color, fg=self.fg_color)

        self.is_dark_mode = not self.is_dark_mode

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
