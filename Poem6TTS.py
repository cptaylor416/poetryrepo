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
As to those that went before, so, too, in life is made new again.
It
 pours
  reaches
   climbs
    sinks
     as if standing on fishes.""", lang="en")

# write audio file
tts.save("Poem6.mp3")

# play audio file
playsound("Poem6.mp3")