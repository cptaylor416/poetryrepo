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
To the body is but meager measure Of your bright beauty which is coming to be.
It
 pours
  reaches
   climbs
    sinks
     as if standing on fishes.""", lang="en")

# write audio file
tts.save("Poem3.mp3")

# play audio file
playsound("Poem3.mp3")