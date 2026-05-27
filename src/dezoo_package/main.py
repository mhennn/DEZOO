import simpleaudio as sa

class DezooSystem:
    def __init__(self):
        pass

    def debug_dog(self):
        song_obj = sa.WaveObject.from_wave_file(r"src\demal_package\media\Dog.wav")
        play_song = song_obj.play()
        play_song.wait_done()

    def debug_birds(self):
        song_obj = sa.WaveObject.from_wave_file(r"src\demal_package\media\Birds.wav")
        play_song = song_obj.play()
        play_song.wait_done()

    def debug_whistle(self):
        song_obj = sa.WaveObject.from_wave_file(r"src\demal_package\media\Whistle.wav")
        play_song = song_obj.play()
        play_song.wait_done()