# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from haversine import haversine

def stations_by_distance(stations, p):
    """Takes a list of stations and returns tuples containing each station and their distance to coordinate p."""
    return sorted_by_key([(station, haversine(station.coord, p)) for station in stations], 1)

def stations_within_radius(stations, centre, r):
    """Returns a list of stations within radius r of a centre coordinate."""
    station_distances = stations_by_distance(stations, centre)
    return [entry[0] for entry in station_distances if entry[1] <= r]
