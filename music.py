import vlc,thread
import time

instance = vlc.Instance()
player = instance.media_player_new()
def playMusic(song):	
	media = instance.media_new(song)
	player.set_media(media)
	player.play()
    
def playSong(song):
	while True:
		thread.start_new_thread(playMusic,(song,))
		time.sleep(131)
		
def stop():
	player.stop()
	
def change_volume(vol):
	player.audio_set_volume(vol)
