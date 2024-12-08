from hypotenuse import Triangle

def test_pythagorean_triple_3_4_5():
    t = Triangle(3, 4)
    assert t.hypotenuse() == 5

def test_pythagorean_triple_5_12_13():
    t = Triangle(5, 12)
    assert t.hypotenuse() == 13

def test_pythagorean_triple_39_80_89():
    t = Triangle(39, 80)
    assert t.hypotenuse() == 89

def test_pythagorean_triple_68_285_293():
    t = Triangle(68, 285)
    assert t.hypotenuse() == 293