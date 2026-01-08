from project import orbital_velocity, centripetal_acceleration, orbital_period

def test_orbital_velocity():

    M = 5.972e24
    r = 6.371e6
    expected = 7909
    assert round(orbital_velocity(M, r), 0) == expected

def test_centripetal_acceleration():
    v = 7909
    r = 6.371e6
    expected = 9.81
    assert round(centripetal_acceleration(v, r), 2) == expected

def test_orbital_period():
    v = 7909
    r = 6.371e6
    expected = (2 * 3.1416 * r) / v
    assert round(orbital_period(v, r), 2) == round(expected, 2)
