from lib.track import *

track1 = Track("Underground","Lindsey Stirling")
def test_creates_instance_of_track():
    assert isinstance(track1, Track)
    assert track1.title == "Underground"
    assert track1.artist == "Lindsey Stirling"

def test_matches_returns_true_for_match_false_for_no_match():
    assert track1.matches("Lindsey") == True
    assert track1.matches("Underground") == True
    assert track1.matches("hello") == False
