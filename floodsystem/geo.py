# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from haversine import haversine


def stations_by_distance(stations, p):
    """Takes a list of stations and returns tuples containing each station and their distance to coordinate p."""
    return sorted_by_key([(station, haversine(station.coord, p)) for station in stations], 1)


def stations_within_radius(stations, centre, r):
    """Returns a list of stations within radius r of a centre coordinate."""
    station_distances = stations_by_distance(stations, centre)
    return [entry[0] for entry in station_distances if entry[1] <= r]


def rivers_with_station(stations):
    """Returns a list of rivers by monitoring stations."""
    return sorted(list(set([station.river for station in stations])))


def stations_by_river(stations):
    """Returns a dictionary containing the river name as the key and a list of stations on that river as the value."""
    rivers_stations_dict = {}
    for river in rivers_with_station(stations):
        rivers_stations_dict[river] = list(filter(lambda station: station.river == river, stations))
    return rivers_stations_dict


def rivers_by_station_number(stations, N):
    """Return the first N entries of the list of rivers by greatest number of stations.
    If there are more rivers with the same number of stations the Nth river,
    they will also be included in the output."""
    unsorted_rivers_number = [(river[0], len(river[1])) for river in stations_by_river(stations).items()]
    rivers_number = sorted_by_key(unsorted_rivers_number, 1, reverse=True)
    nth_value = rivers_number[N - 1][1]
    rivers_output = []
    for river in rivers_number:
        if river[1] < nth_value:
            break
        rivers_output.append(river)
    return rivers_output
