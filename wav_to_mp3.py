from pathlib import Path

# import tkinter for file selector GUI

from tkinter import Tk
from tkinter.filedialog import askopenfilename

# import AudioSegment module from pydub which lets us convert between audio formats

from pydub import AudioSegment

# make a GUI window

Tk().withdraw()

# call which ever file you select "beat_wav"

beat_wav=askopenfilename()

# extract the name of the beat from the selected directory and remove the ".wav" so it can be renamed

p = Path(beat_wav)
old_name = (p.parts[-1])
new_name = old_name.replace(".wav", "")

# set your desktop as the path to export the beat to

desktop= ("/Users/macuser/desktop/"+ new_name + ".mp3")

# run the magical pydub module which converts wav to mp3

AudioSegment.from_wav(beat_wav).export(desktop, format="mp3")


