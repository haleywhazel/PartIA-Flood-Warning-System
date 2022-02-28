"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    """Tests the stations level over threshold function"""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0.0, 2.0)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 1.0
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2.latest_level = 1.9
    
    assert stations_level_over_threshold([s, s2], 0.6) == [(s2, s2.relative_water_level())]
    assert stations_level_over_threshold([s], 0.1) == [(s, s.relative_water_level())]

def test_stations_highest_rel_level():
    """Tests the stations highest rel level function"""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0.0, 2.0)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 1.0
    s_list = [s] * 50
    
    assert len(stations_highest_rel_level(s_list, 10)) == 10
    assert len(stations_highest_rel_level(s_list, 40)) == 40