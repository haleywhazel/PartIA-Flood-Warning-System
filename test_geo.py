"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation


def test_stations_by_distance():
    """Test the stations by distance function."""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    distances_from_cambridge = stations_by_distance([s, s], (-2.0, 4.0))

    assert distances_from_cambridge[1][1] == 0.0


def test_stations_within_radius():
    """Test stations within radius function."""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord1 = (-2.0, 4.0)
    coord2 = (1000.0, 1000.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord1, trange, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord2, trange, river, town)

    stations = stations_within_radius([s1, s1, s1, s2, s1, s2], (-2.0, 4.0), 20)

    assert len(stations) == 4


def test_rivers_with_station():
    """Test rivers with station function."""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    riverx = "River X"
    rivery = "River Y"
    riverz = "River Z"
    town = "My Town"
    sx = MonitoringStation(s_id, m_id, label, coord, trange, riverx, town)
    sy = MonitoringStation(s_id, m_id, label, coord, trange, rivery, town)
    sz = MonitoringStation(s_id, m_id, label, coord, trange, riverz, town)

    stations = [sx, sy, sz]
    rivers = rivers_with_station(stations)

    assert len(rivers) == 3
    assert "River X" in rivers
    assert "River Y" in rivers
    assert "River Z" in rivers


def test_stations_by_river():
    """Test stations by river function."""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    riverx = "River X"
    rivery = "River Y"
    riverz = "River Z"
    town = "My Town"
    sx = MonitoringStation(s_id, m_id, label, coord, trange, riverx, town)
    sy = MonitoringStation(s_id, m_id, label, coord, trange, rivery, town)
    sz = MonitoringStation(s_id, m_id, label * 2, coord, trange, riverz, town)

    stations = [sx, sy, sz]
    rivers_stations_dict = stations_by_river(stations)

    assert rivers_stations_dict["River X"] == ["some station"]
    assert rivers_stations_dict["River Y"] == ["some station"]
    assert rivers_stations_dict["River Z"] == ["some station" * 2]


def test_rivers_by_station_number():
    """Test rivers by station number function."""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    riverx = "River X"
    rivery = "River Y"
    riverz = "River Z"
    town = "My Town"
    sx = MonitoringStation(s_id, m_id, label, coord, trange, riverx, town)
    sy = MonitoringStation(s_id, m_id, label, coord, trange, rivery, town)
    sz = MonitoringStation(s_id, m_id, label * 2, coord, trange, riverz, town)

    stations = [sx, sx, sz, sz, sy, sz, sx]
    rivers_with_number = rivers_by_station_number(stations, 3)

    assert len(rivers_with_number) == 3
    assert rivers_with_number[0][0] == "River X"

    stations = [sx, sx, sz, sz, sy, sy]
    rivers_with_number = rivers_by_station_number(stations, 1)

    assert len(rivers_with_number) == 3
