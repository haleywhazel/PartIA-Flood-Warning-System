# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    rivers = rivers_with_station(stations)
    print("\n{} stations. First 10 - {}".format(len(rivers), rivers[:10]))

    rivers_stations_dict = stations_by_river(stations)

    def stations_next_to(river):
        sorted([station.name for station in rivers_stations_dict[river]])

    print("\n\nStations next to River Aire: {}".format(stations_next_to("River Aire")))
    print("\n\nStations next to River Cam: {}".format(stations_next_to("River Cam")))
    print("\n\nStations next to River Thames: {}".format(stations_next_to("River Thames")))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
