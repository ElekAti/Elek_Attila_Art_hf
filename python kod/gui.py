import tkinter as tk
from tkinter import messagebox
import serial

PORT = 'COM3'
BAUDRATE = 115200

try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    print(f"Connected to {PORT} port")
except serial.SerialException:
    messagebox.showerror("Error", f"Couldn't connect to: {PORT}")
    ser = None


def send_value():
    if ser is None:
        messagebox.showerror("Error", "No serial connection")
        return

    value = entry.get().strip()
    if not value.isdigit():
        messagebox.showwarning("Invalid input", "Only numeric values are allowed")
        return

    ser.write((value + '\n').encode())
    status_label.config(text=f"Send: {value} ms")
    entry.delete(0, tk.END)


def quit_app():
    if ser:
        ser.close()
    root.destroy()


root = tk.Tk()
root.title("Serial Sender")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Delay (ms):")
label.grid(row=0, column=0, pady=5)

entry = tk.Entry(frame, width=10)
entry.grid(row=0, column=1, pady=5, padx=5)

send_button = tk.Button(frame, text="Send", command=send_value)
send_button.grid(row=0, column=2, padx=5)

quit_button = tk.Button(frame, text="Quit", command=quit_app)
quit_button.grid(row=1, column=0, columnspan=3, pady=10)

status_label = tk.Label(frame, text="No data sent yet")
status_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
