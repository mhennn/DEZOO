import simpleaudio as sa
from importlib.resources import files

class DezooSystem:
    def __init__(self):
        pass

    def debug_dog(self):
        dog_path = files("dezoo_package.media").joinpath("Dog.wav")
        song_obj = sa.WaveObject.from_wave_file(str(dog_path))
        play_song = song_obj.play()
        play_song.wait_done()

    def debug_birds(self):
        birds_path = files("dezoo_package.media").joinpath("Birds.wav")
        song_obj = sa.WaveObject.from_wave_file(str(birds_path))
        play_song = song_obj.play()
        play_song.wait_done()

    def debug_whistle(self):
        whistle_path = files("dezoo_package.media").joinpath("Whistle.wav")
        song_obj = sa.WaveObject.from_wave_file(str(whistle_path))
        play_song = song_obj.play()
        play_song.wait_done()