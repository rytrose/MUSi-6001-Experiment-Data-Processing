from pydub import AudioSegment
from pydub.playback import play as play_segment

class Player:
    def __init__(self):
        self.forest = AudioSegment.from_file("audio/Forest-Noise.mp3")
        self.harsh = AudioSegment.from_file("audio/Harsh-Noise.mp3")
        self.street = AudioSegment.from_file("audio/Street-Noise.mp3")
        self.songs = [self.forest, self.harsh, self.street]
        print("Loaded songs.")

    def play(self, song, start, end):
        if isinstance(song, str):
            song = self.song_string_to_id(song)

        assert type(song) == int
        assert type(start) == float
        assert type(end) == float

        to_play = self.songs[song][int(1000 * start):int(1000 * end)]
        play_segment(to_play)

    def song_string_to_id(self, s):
        if s == "Forest":
            return 0
        elif s == "Harsh":
            return 1
        elif s == "Street":
            return 2

