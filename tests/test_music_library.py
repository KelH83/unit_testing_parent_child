from lib.music_library import *
from unittest.mock import Mock


new_library = MusicLibrary()

def test_creates_an_instance_of_music_library():
    assert isinstance(new_library, MusicLibrary)
    assert new_library.library == []

def test_add_add_the_track_to_the_library():
    new_library2 = MusicLibrary()
    faketrack1 = Mock()
    faketrack2 = Mock()
    faketrack3 = Mock()
    new_library2.add(faketrack1)
    new_library2.add(faketrack2)
    new_library2.add(faketrack3)
    assert new_library2.library == [faketrack1, faketrack2, faketrack3]

def test_search_library_returns_list_of_matching_tracks():
    fake_match = Mock()
    fake_match.matches.return_value = True
    fake_non_match = Mock()
    fake_non_match.matches.return_value = False
    new_library.add(fake_match)
    new_library.add(fake_non_match)
    assert new_library.search("Korn") == [fake_match]
