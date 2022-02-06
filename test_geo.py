"""Unit test for the geo module"""

from floodsystem.geo import *

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