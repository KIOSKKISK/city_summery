from processing.preprocessing import add_warm_clothes, add_expensive


def test_warm_clothes():
    weather = {"temp_c": -5}
    result = add_warm_clothes(weather)

    assert result["warm_clothes"] is True


def test_no_warm_clothes():
    weather = {"temp_c": 10}
    result = add_warm_clothes(weather)

    assert result["warm_clothes"] is False


def test_expensive_rate():
    assert add_expensive(101) is True


def test_normal_rate():
    assert add_expensive(90) is False