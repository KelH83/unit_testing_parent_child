class MusicLibrary:
    def __init__(self):
        self.library = []

    def add(self, track):
        self.library.append(track)

    def search(self, keyword):
        return [track for track in self.library if track.matches(keyword)]

