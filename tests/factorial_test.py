from programs.factorial import fact

def test_fact_zero():
    assert fact(0) == 1

def test_fact_two():
    assert fact(2) == 2

def test_fact_5():
    assert fact(5) == 120