from programs.vowels import vowels

def test_vowels_party():
    assert vowels("party") == 1

def test_vowels_holiday():
    assert vowels("holiday") == 3