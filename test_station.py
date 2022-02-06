# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_inconsistent_typical_range_stations():
    """Tests the inconsistent typical range stations wrapper function."""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    badtrange1 = (12.3, 3.4445)
    badtrange2 = 0
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_bad1 = MonitoringStation(s_id, m_id, label, coord, badtrange1, river, town)
    s_bad2 = MonitoringStation(s_id, m_id, label, coord, badtrange2, river, town)

    stations = inconsistent_typical_range_stations([s])

    assert len(stations) == 0

    stations = inconsistent_typical_range_stations([s, s_bad1, s_bad2, s_bad2, s, s, s_bad2, s_bad1])

    assert len(stations) == 5
    assert stations[0].name == "some station"
