from sensor import get_sensor_data

def test_sensor():
    data = get_sensor_data()
    assert len(data) > 0