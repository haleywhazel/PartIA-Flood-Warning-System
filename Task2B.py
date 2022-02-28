# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    stations = build_station_list()
    update_water_levels(stations)

    for station_tuple in stations_level_over_threshold(stations, 0.8):
        print(station_tuple[0].name + " " + str(station_tuple[1]))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
