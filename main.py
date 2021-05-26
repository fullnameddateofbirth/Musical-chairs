from pygame import mixer
import time
import random
# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("song.mp3")

# Setting the volume
mixer.music.set_volume(0.3)

# Start playing the song
mixer.music.play()

# infinite loop
while True:
		# Waiting For Some Time Randomly
		timeToWait = random.randint(1,100)
		time.sleep(timeToWait)
		# Pausing the music
		mixer.music.pause()	
		# Waiting for Three minutes for arrangement of chairs etc
		time.sleep(5)
		# Resuming the music
		mixer.music.unpause()
