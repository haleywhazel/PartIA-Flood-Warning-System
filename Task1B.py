# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    distances_from_cambridge = stations_by_distance(stations, (52.2053, 0.1218))

    print("\nClosest 10 stations:")
    print([(entry[0].name, entry[0].town, entry[1]) for entry in distances_from_cambridge[:10]])

    print("\nFarthest 10 stations:")
    print([(entry[0].name, entry[0].town, entry[1]) for entry in distances_from_cambridge[-10:]])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
