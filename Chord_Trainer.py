import random
import tkinter as tk
from tkinter import ttk

last_chord = None
root = ['A','B','C','D','E','F','G','Ab','Bb','C#','Db','Eb','F#','Gb']

def generate_chord(last_chord):
    while True:
        chord_root = random.choice(root)
        triad_type = random.choice(['major', 'minor', 'diminished', 'augmented', 'sus2', 'sus4'])

        if triad_type == 'major':
            chord_3rd = ''
            allowed_5ths = ['', 'aug']
            allowed_7ths = ['', '7', 'Maj7']

        elif triad_type == 'minor':
            chord_3rd = 'm'
            allowed_5ths = ['', '°']
            allowed_7ths = ['', '7', 'Maj7']

        elif triad_type == 'diminished':
            chord_3rd = ''
            allowed_5ths = ['°']
            allowed_7ths = ['']

        elif triad_type == 'augmented':
            chord_3rd = ''
            allowed_5ths = ['aug']
            allowed_7ths = ['', '7']

        elif triad_type == 'sus2':
            chord_3rd = 'sus2'
            allowed_5ths = ['']
            allowed_7ths = ['']

        elif triad_type == 'sus4':
            chord_3rd = 'sus4'
            allowed_5ths = ['']
            allowed_7ths = ['']

        chord_5th = random.choice(allowed_5ths)
        chord_7th = random.choice(allowed_7ths)

        if chord_3rd == 'm':
            chord_5th = ''

        combined = chord_root + chord_3rd + chord_5th + chord_7th
        if combined != last_chord:
            return combined

window = tk.Tk()
window.title("Chord Trainer")
window.geometry("400x250")
window.configure(bg="#1e1e1e")

chord_label = tk.Label(
    window,
    text="Get Ready",
    font=("Arial", 40, "bold"),
    bg="#1e1e1e",
    fg="white"
)
chord_label.pack(pady=20)

progress = ttk.Progressbar(
    window, orient="horizontal", length=350,
    mode="determinate", maximum=100
)
progress.pack(pady=10)

style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", troughcolor="#1e1e1e", background="#00ff00", thickness=20)

progress_value = 0
update_interval = 50
total_time = 5000
paused = False

def refresh_chord():
    global last_chord, progress_value
    new_chord = generate_chord(last_chord)
    last_chord = new_chord
    chord_label.config(text=new_chord)
    progress_value = 0
    progress['value'] = 0


def update_progress():
    global progress_value

    if not paused:
        progress_value += (update_interval / total_time) * 100

        if progress_value >= 100:
            refresh_chord()

        progress['value'] = progress_value

    window.after(update_interval, update_progress)

def toggle_pause():
    global paused
    paused = not paused
    pause_button.config(text="Resume" if paused else "Pause")

def skip_chord():
    refresh_chord()

button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=20)

pause_button = tk.Button(
    button_frame,
    text="Pause",
    font=("Arial", 16),
    bg="#333",
    fg="white",
    activebackground="#555",
    command=toggle_pause,
    padx=20
)
pause_button.grid(row=0, column=0, padx=10)

skip_button = tk.Button(
    button_frame,
    text="Next",
    font=("Arial", 16),
    bg="#333",
    fg="white",
    activebackground="#555",
    command=skip_chord,
    padx=20
)
skip_button.grid(row=0, column=1, padx=10)

refresh_chord()
update_progress()
window.mainloop()
