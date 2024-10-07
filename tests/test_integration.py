from lib.track import *
from lib.music_library import *

track1 = Track("Korn","Freak on a Leash")
track2 = Track("Pantera", "Walk")
track3 = Track("Korn", "Coming undone")

new_library = MusicLibrary()
new_library2 = MusicLibrary()

def test_add_puts_the_tracks_into_the_library():
    new_library.add(track1)
    assert new_library.library == [track1]
    new_library.add(track2)
    new_library.add(track3)
    assert new_library.library == [track1, track2, track3]

def test_search_returns_a_list_of_matching_tracks():
    new_library2.add(track1)
    new_library2.add(track2)
    new_library2.add(track3)
    assert new_library2.search("Walk") == [track2]