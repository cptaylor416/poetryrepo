"""
SCRIPT:  text-to-audio.py
AUTHOR:  Courtney Taylor
DATE: 10.23.18
PURPOSE: Open educational materials for a seminar on digital culture
LICENSE: GNU General Public License v2
DEPENDENCIES: playsound and gTTs
"""

# import libraries
from playsound import playsound
from gtts import gTTS

# text to speech
tts = gTTS(text= """Nowhere you can go is more peaceful.
How easy it is succeeded by another which is of the Universe for all who were once much celebrated now sound strangely in our power is good fortune.
It
 pours
  reaches
   climbs
    sinks
     as if standing on fishes.""", lang="en")

# write audio file
tts.save("Poem5.mp3")

# play audio file
playsound("Poem5.mp3")
