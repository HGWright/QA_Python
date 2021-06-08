from programs.list_of_squares import list_of_squares

def test_list_of_squares_five():
    assert list_of_squares(5)[2] == 4
    assert list_of_squares(5)[5] == 25

def test_list_of_squares_ten():
    assert list_of_squares(10)[9] == 81
    assert list_of_squares(10)[5] == 25

    