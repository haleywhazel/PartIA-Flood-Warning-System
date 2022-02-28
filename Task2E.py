# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels


def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 10

    stations_at_risk = stations_highest_rel_level(stations, 5)

    dates = []
    levels = []

    for station in stations_at_risk:
        results = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        dates.append(results[0])
        levels.append(results[1])

    plot_water_levels(stations_at_risk, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
