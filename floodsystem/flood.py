"""
This module includes a collection on functions related to flood warning.
"""

from .utils import sorted_by_key, gt_with_none

def stations_level_over_threshold(stations, tol):
    """Provides a list of stations over the tolerance"""
    return sorted_by_key([(station, station.relative_water_level()) for station in stations if gt_with_none(station.relative_water_level(), tol)], 1, True)

def stations_highest_rel_level(stations, N):
    """Provides a list of N stations most at risk"""
    return stations_level_over_threshold(stations, -9999.9)[0:N]