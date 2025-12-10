import tkinter as tk
from tkinter import ttk
import random
import time
import threading
import winsound

simple_chords_revised = {
    'A': 'A Major', 'Am': 'A minor', 'Asus2': 'A sus2', 'Asus4': 'A sus4', 
    'Bb': 'B-flat Major', 'Bbm': 'B-flat minor', 'Bbsus2': 'B-flat sus2', 'Bbsus4': 'B-flat sus4', 
    'B': 'B Major', 'Bm': 'B minor', 'Bsus2': 'B sus2', 'Bsus4': 'B sus4', 
    'C': 'C Major', 'Cm': 'C minor', 'Csus2': 'C sus2', 'Csus4': 'C sus4', 
    'Db': 'D-flat Major', 'Dbm': 'D-flat minor', 'Dbsus2': 'D-flat sus2', 'Dbsus4': 'Dbsus4', 
    'C#': 'C-sharp Major', 'C#m': 'C-sharp minor', 'C#sus2': 'C-sharp sus2', 'C#sus4': 'C-sharp sus4',
    'D': 'D Major', 'Dm': 'D minor', 'Dsus2': 'D sus2', 'Dsus4': 'D sus4', 
    'Eb': 'E-flat Major', 'Ebm': 'E-flat minor', 'Ebsus2': 'E-flat sus2', 'Ebsus4': 'E-flat sus4', 
    'E': 'E Major', 'Em': 'E minor', 'Esus2': 'E sus2', 'Esus4': 'E sus4', 
    'F': 'F Major', 'Fm': 'F minor', 'Fsus2': 'F sus2', 'Fsus4': 'F sus4', 
    'Gb': 'G-flat Major', 'Gbm': 'G-flat minor', 'Gbsus2': 'G-flat sus2', 'Gbsus4': 'Gbsus4', 
    'F#': 'F-sharp Major', 'F#m': 'F-sharp minor', 'F#sus2': 'F-sharp sus2', 'F#sus4': 'F-sharp sus4',
    'G': 'G Major', 'Gm': 'G minor', 'Gsus2': 'G sus2', 'Gsus4': 'G sus4', 
    'Ab': 'A-flat Major', 'Abm': 'A-flat minor', 'Absus2': 'A-flat sus2', 'Absus4': 'A-flat sus4'
}

extended_chords_revised = {
    # --- A ---
    'Adim': 'A diminished', 'Aaug': 'A augmented', 'A7': 'A Dominant 7th', 
    'Amaj7': 'A Major 7th', 'Am7': 'A minor 7th', 'A6': 'A Major 6th', 
    'Am6': 'A minor 6th', 'Amaj9': 'A Major 9th', 'A9': 'A Dominant 9th', 
    'Am9': 'A minor 9th', 'Aadd9': 'A Major add9', 'A7sus4': 'A 7th sus4', 
    # --- A#/Bb ---
    'Bbdim': 'B-flat diminished', 'Bbaug': 'B-flat augmented', 'Bb7': 'B-flat Dominant 7th', 
    'Bbmaj7': 'B-flat Major 7th', 'Bbm7': 'B-flat minor 7th', 'Bb6': 'B-flat Major 6th', 
    'Bbm6': 'B-flat minor 6th', 'Bbmaj9': 'B-flat Major 9th', 'Bb9': 'B-flat Dominant 9th', 
    'Bbm9': 'B-flat minor 9th', 'Bbadd9': 'B-flat Major add9', 'Bb7sus4': 'B-flat 7th sus4',
    # --- B ---
    'Bdim': 'B diminished', 'Baug': 'B augmented', 'B7': 'B Dominant 7th', 
    'Bmaj7': 'B Major 7th', 'Bm7': 'B minor 7th', 'B6': 'B Major 6th', 
    'Bm6': 'B minor 6th', 'Bmaj9': 'B Major 9th', 'B9': 'B Dominant 9th', 
    'Bm9': 'B minor 9th', 'Badd9': 'B Major add9', 'B7sus4': 'B 7th sus4', 
    # --- C ---
    'Cdim': 'C diminished', 'Caug': 'C augmented', 'C7': 'C Dominant 7th', 
    'Cmaj7': 'C Major 7th', 'Cm7': 'C minor 7th', 'C6': 'C Major 6th', 
    'Cm6': 'C minor 6th', 'Cmaj9': 'C Major 9th', 'C9': 'C Dominant 9th', 
    'Cm9': 'C minor 9th', 'Cadd9': 'C Major add9', 'C7sus4': 'C 7th sus4', 
    # --- C#/Db ---
    'Dbdim': 'D-flat diminished', 'Dbaug': 'D-flat augmented', 'Db7': 'D-flat Dominant 7th', 
    'Dbmaj7': 'D-flat Major 7th', 'Dbm7': 'D-flat minor 7th', 'Db6': 'D-flat Major 6th', 
    'Dbm6': 'D-flat minor 6th', 'Dbmaj9': 'D-flat Major 9th', 'Db9': 'D-flat Dominant 9th', 
    'Dbm9': 'D-flat minor 9th', 'Dbadd9': 'D-flat Major add9', 'Db7sus4': 'D-flat 7th sus4',
    'C#dim': 'C-sharp diminished', 'C#aug': 'C-sharp augmented', 'C#7': 'C-sharp Dominant 7th', 
    'C#maj7': 'C-sharp Major 7th', 'C#m7': 'C-sharp minor 7th', 'C#6': 'C-sharp Major 6th', 
    'C#m6': 'C-sharp minor 6th', 'C#maj9': 'C-sharp Major 9th', 'C#9': 'C-sharp Dominant 9th', 
    'C#m9': 'C-sharp minor 9th', 'C#add9': 'C-sharp Major add9', 'C#7sus4': 'C-sharp 7th sus4',
    # --- D ---
    'Ddim': 'D diminished', 'Daug': 'D augmented', 'D7': 'D Dominant 7th', 
    'Dmaj7': 'D Major 7th', 'Dm7': 'D minor 7th', 'D6': 'D Major 6th', 
    'Dm6': 'D minor 6th', 'Dmaj9': 'D Major 9th', 'D9': 'D Dominant 9th', 
    'Dm9': 'D minor 9th', 'Dadd9': 'D Major add9', 'D7sus4': 'D 7th sus4', 
    # --- D#/Eb ---
    'Ebdim': 'E-flat diminished', 'Ebaug': 'E-flat augmented', 'Eb7': 'E-flat Dominant 7th', 
    'Ebmaj7': 'E-flat Major 7th', 'Ebm7': 'E-flat minor 7th', 'Eb6': 'E-flat Major 6th', 
    'Ebm6': 'E-flat minor 6th', 'Ebmaj9': 'E-flat Major 9th', 'Eb9': 'E-flat Dominant 9th', 
    'Ebm9': 'E-flat minor 9th', 'Ebadd9': 'E-flat Major add9', 'Eb7sus4': 'E-flat 7th sus4',
    # --- E ---
    'Edim': 'E diminished', 'Eaug': 'E augmented', 'E7': 'E Dominant 7th', 
    'Emaj7': 'E Major 7th', 'Em7': 'E minor 7th', 'E6': 'E Major 6th', 
    'Em6': 'E minor 6th', 'Emaj9': 'E Major 9th', 'E9': 'E Dominant 9th', 
    'Em9': 'E minor 9th', 'Eadd9': 'E Major add9', 'E7sus4': 'E 7th sus4', 
    # --- F ---
    'Fdim': 'F diminished', 'Faug': 'F augmented', 'F7': 'F Dominant 7th', 
    'Fmaj7': 'F Major 7th', 'Fm7': 'F minor 7th', 'F6': 'F Major 6th', 
    'Fm6': 'F minor 6th', 'Fmaj9': 'F Major 9th', 'F9': 'F Dominant 9th', 
    'Fm9': 'F minor 9th', 'Fadd9': 'F Major add9', 'F7sus4': 'F 7th sus4', 
    # --- F#/Gb ---
    'Gbdim': 'G-flat diminished', 'Gbaug': 'G-flat augmented', 'Gb7': 'G-flat Dominant 7th', 
    'Gbmaj7': 'G-flat Major 7th', 'Gbm7': 'G-flat minor 7th', 'Gb6': 'G-flat Major 6th', 
    'Gbm6': 'G-flat minor 6th', 'Gbmaj9': 'G-flat Major 9th', 'Gb9': 'G-flat Dominant 9th', 
    'Gbm9': 'G-flat minor 9th', 'Gbadd9': 'G-flat Major add9', 'Gb7sus4': 'G-flat 7th sus4',
    'F#dim': 'F-sharp diminished', 'F#aug': 'F-sharp augmented', 'F#7': 'F-sharp Dominant 7th', 
    'F#maj7': 'F-sharp Major 7th', 'F#m7': 'F-sharp minor 7th', 'F#6': 'F-sharp Major 6th', 
    'F#m6': 'F-sharp minor 6th', 'F#maj9': 'F-sharp Major 9th', 'F#9': 'F-sharp Dominant 9th', 
    'F#m9': 'F-sharp minor 9th', 'F#add9': 'F-sharp Major add9', 'F#7sus4': 'F-sharp 7th sus4',
    # --- G ---
    'Gdim': 'G diminished', 'Gaug': 'G augmented', 'G7': 'G Dominant 7th', 
    'Gmaj7': 'G Major 7th', 'Gm7': 'G minor 7th', 'G6': 'G Major 6th', 
    'Gm6': 'G minor 6th', 'Gmaj9': 'G Major 9th', 'G9': 'G Dominant 9th', 
    'Gm9': 'G minor 9th', 'Gadd9': 'G Major add9', 'G7sus4': 'G 7th sus4', 
    # --- G#/Ab ---
    'Abdim': 'A-flat diminished', 'Abaug': 'A-flat augmented', 'Ab7': 'A-flat Dominant 7th', 
    'Abmaj7': 'A-flat Major 7th', 'Abm7': 'A-flat minor 7th', 'Ab6': 'A-flat Major 6th', 
    'Abm6': 'A-flat minor 6th', 'Abmaj9': 'A-flat Major 9th', 'Ab9': 'A-flat Dominant 9th', 
    'Abm9': 'A-flat minor 9th', 'Abadd9': 'A-flat Major add9', 'Ab7sus4': 'A-flat 7th sus4'
}

full_chord_lookup = {**simple_chords_revised, **extended_chords_revised}
MASTER_CHORD_LIST = list(full_chord_lookup.keys()) 

def generate_chord_different_from(exclude_chord):
    """Generates a random chord that is not the same as the exclude_chord."""
    possible_chords = [chord for chord in MASTER_CHORD_LIST if chord != exclude_chord]
    return random.choice(possible_chords)

BEATS_PER_CHORD = 4 
MIN_BPM = 40
MAX_BPM = 140

current_bpm = 80 
time_per_beat_s = 60.0 / current_bpm 
time_per_chord_s = time_per_beat_s * BEATS_PER_CHORD
current_beat = 0

# Initial chord setup
last_chord = generate_chord_different_from("INIT") 
previous_chord = ""                               
next_chord = generate_chord_different_from(last_chord) 

audio_enabled = False 
audio_beats_played = set() 

def calculate_time_intervals(bpm):
    global time_per_beat_s, time_per_chord_s
    time_per_beat_s = 60.0 / bpm
    time_per_chord_s = time_per_beat_s * BEATS_PER_CHORD


# --- TKINTER GUI SETUP ---

window = tk.Tk()
window.title("Chord Trainer")
window.geometry("500x400") 
window.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use('default')

# 1. Styles for Slider 
SLIDER_STYLE_NAME = "Dark.Horizontal.TScale"
style.configure(SLIDER_STYLE_NAME,
    background="#1e1e1e",
    troughcolor="#555555",      
    sliderrelief="raised",      
    sliderthickness=25,         
    groovethickness=8           
)
style.map(SLIDER_STYLE_NAME, 
    background=[('active', '#00ff00'), ('!disabled', '#BBBBBB')], 
    troughcolor=[('!disabled', '#555555')]
)


# --- CHORD DISPLAY FRAME (Fixed Width, Closer Spacing) ---
chord_display_frame = tk.Frame(window, bg="#1e1e1e")
chord_display_frame.pack(pady=20)

# Determine maximum chord lengths for consistent alignment
SIDE_LABEL_WIDTH = 7
CURRENT_LABEL_WIDTH = 7 
CHORD_PADX = 5 

# 1. Previous Chord Label (Left - Aligned Left)
previous_chord_label = tk.Label(
    chord_display_frame, 
    text=previous_chord, 
    font=("Arial", 20), 
    bg="#1e1e1e", 
    fg="#555555",
    width=SIDE_LABEL_WIDTH, 
    anchor="w" 
)
previous_chord_label.grid(row=0, column=0, padx=CHORD_PADX)

# 2. Current Chord Label (Center - Aligned Center)
current_chord_label = tk.Label(
    chord_display_frame, 
    text=last_chord, 
    font=("Arial", 40, "bold"), 
    bg="#1e1e1e", 
    fg="white",
    width=CURRENT_LABEL_WIDTH,
    anchor="center"
)
current_chord_label.grid(row=0, column=1, padx=CHORD_PADX) 

# 3. Next Chord Label (Right - Aligned Right)
next_chord_label = tk.Label(
    chord_display_frame, 
    text=next_chord, 
    font=("Arial", 20), 
    bg="#1e1e1e", 
    fg="#555555", # <--- Corrected to muted gray
    width=SIDE_LABEL_WIDTH,
    anchor="e" 
)
next_chord_label.grid(row=0, column=2, padx=CHORD_PADX)


light_frame = tk.Frame(window, bg="#1e1e1e")
light_frame.pack(pady=10)

metronome_lights = []
for i in range(4):
    light = tk.Label(light_frame, text="█", font=("Arial", 30), bg="#1e1e1e", fg="#333333")
    light.grid(row=0, column=i, padx=5)
    metronome_lights.append(light)


def update_bpm(val):
    global current_bpm
    current_bpm = int(float(val))
    bpm_label.config(text=f"BPM: {current_bpm}")
    calculate_time_intervals(current_bpm)

bpm_label = tk.Label(window, text=f"BPM: {current_bpm}", bg="#1e1e1e", fg="white", font=("Arial", 14))
bpm_label.pack(pady=(10, 0)) 

bpm_slider = ttk.Scale(window, 
    style=SLIDER_STYLE_NAME,
    from_=MIN_BPM, 
    to=MAX_BPM, 
    orient=tk.HORIZONTAL, 
    length=300, 
    command=update_bpm
)
bpm_slider.set(current_bpm) 
bpm_slider.pack(pady=5)


# --- BUTTON FUNCTIONS and AUDIO LOGIC ---
def toggle_audio():
    global audio_enabled
    audio_enabled = not audio_enabled
    if audio_enabled:
        audio_button.config(text="Sound ON", bg="#008800")
    else:
        audio_button.config(text="Sound OFF", bg="#880000")
        
def toggle_pause():
    global paused
    paused = not paused
    pause_button.config(text="Resume" if paused else "Pause")

def skip_chord():
    global paused
    if paused:
        toggle_pause() 
    refresh_chord()

def play_audio_sync(file_path):
    try:
        winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception as e:
        print(f"Error playing sync sound via winsound: {e}")

def play_beat_click(beat_number):
    STRONG_CLICK_FILE = "Simple_beat.wav"
    file_to_play = STRONG_CLICK_FILE 
    threading.Thread(target=play_audio_sync, args=(file_to_play,)).start()

def reset_progress():
    global timer_ms, current_beat, audio_beats_played
    timer_ms = 0
    current_beat = 1  
    audio_beats_played.clear() 
    update_lights()

def refresh_chord():
    global last_chord, previous_chord, next_chord
    
    # 1. SHIFT CHORDS: Next becomes Current, Current becomes Previous
    previous_chord = last_chord 
    last_chord = next_chord
    
    # 2. Generate a NEW Next Chord (MUST be different from the *current* chord)
    next_chord = generate_chord_different_from(last_chord) 
    
    # 3. Update the labels
    previous_chord_label.config(text=previous_chord)
    current_chord_label.config(text=last_chord) 
    next_chord_label.config(text=next_chord)
    
    # 4. Reset metronome and fire beat 1 audio
    reset_progress()
    
    if audio_enabled:
        play_beat_click(1)
        audio_beats_played.add(1)
    

def check_audio_anticipation():
    global timer_ms, audio_beats_played, time_per_beat_s

    if paused or not audio_enabled:
        return

    beat_duration_ms = time_per_beat_s * 1000
    
    for beat in range(1, BEATS_PER_CHORD + 1):
        if beat in audio_beats_played:
            continue

        target_start_ms = (beat - 1) * beat_duration_ms
        AUDIO_ANTICIPATION_MS = 60
        anticipation_start_ms = target_start_ms - AUDIO_ANTICIPATION_MS
            
        if timer_ms >= anticipation_start_ms:
            play_beat_click(beat)
            audio_beats_played.add(beat)
    
# --- MAIN BUTTON FRAME ---
control_frame = tk.Frame(window, bg="#1e1e1e")
control_frame.pack(pady=20) 

audio_button = tk.Button(
    control_frame, 
    text="Sound OFF", 
    font=("Arial", 12), 
    bg="#880000", 
    fg="white", 
    command=toggle_audio, 
    padx=10, 
    pady=5
)
audio_button.grid(row=0, column=0, columnspan=2, pady=(0, 15))

pause_button = tk.Button(
    control_frame, 
    text="Pause", 
    font=("Arial", 16), 
    bg="#333", 
    fg="white", 
    activebackground="#555", 
    command=toggle_pause, 
    padx=20
)
pause_button.grid(row=1, column=0, padx=10) 

skip_button = tk.Button(
    control_frame,
    text="Next",
    font=("Arial", 16),
    bg="#333",
    fg="white",
    activebackground="#555",
    command=skip_chord,
    padx=20
)
skip_button.grid(row=1, column=1, padx=10) 


# --- TIMER FUNCTION ---
update_interval_ms = 50 
paused = False
timer_ms = 0 

def update_lights():
    global current_beat
    beat_colors = { 1: "yellow", 2: "yellow", 3: "yellow", 4: "red" }
    for i, light in enumerate(metronome_lights):
        beat_number = i + 1 
        if beat_number <= current_beat:
            light.config(fg=beat_colors[beat_number])
        else:
            light.config(fg="#333333") 

def update_timer_and_progress():
    global timer_ms, current_beat, time_per_chord_s, time_per_beat_s
    
    if not paused:
        check_audio_anticipation()
        timer_ms += update_interval_ms
        
        # Check if the chord time is over
        if timer_ms >= time_per_chord_s * 1000:
            refresh_chord()
            
        # Check for beat change
        if current_beat < BEATS_PER_CHORD:
            beat_duration_ms = time_per_beat_s * 1000
            next_beat_start_ms = (current_beat) * beat_duration_ms
            if timer_ms >= next_beat_start_ms:
                current_beat += 1
                update_lights() 
    window.after(update_interval_ms, update_timer_and_progress)

# --- START APPLICATION ---

# The very first chord needs to be generated before the first refresh
# To maintain the previous="" state for the first real 'refresh_chord'
last_chord = generate_chord_different_from("INIT_CHORD") 
next_chord = generate_chord_different_from(last_chord)

# Manually update labels for the true initial state before the timer starts
# We use an empty string for the first previous chord
previous_chord_label.config(text="") 
current_chord_label.config(text=last_chord)
next_chord_label.config(text=next_chord)

update_timer_and_progress()
window.mainloop()