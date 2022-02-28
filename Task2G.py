import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit


def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 10

    stations = stations_level_over_threshold(stations, -999)

    stations_risk_level = []

    for station_tuple in stations:
        if station_tuple[1] <= 1.2:
            stations_risk_level.append(station_tuple)
            continue

        station = station_tuple[0]
        skip = False
        try:
            print("Fetching levels for " + station.name)
            results = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        except KeyError:
            print("Levels for " + station.name + " not found.")
            skip = True
        if skip:
            continue
        try:
            poly, _ = polyfit(results[0], results[1], 4)
        except TypeError:
            print("Cannot process retrieved data.")
            skip = True
        if skip:
            continue

        severity = 0

        levels_tomorrow = poly(1)
        levels_in_two_days = poly(2)
        rel_level_tomorrow = levels_tomorrow - station.typical_range[0]
        rel_level_tomorrow /= station.typical_range[1] - station.typical_range[0]
        rel_level_in_two_days = levels_in_two_days - station.typical_range[0]
        rel_level_in_two_days /= station.typical_range[1] - station.typical_range[0]

        severity += station_tuple[1]
        if rel_level_tomorrow > 1.5:
            severity += station_tuple[1]
        if rel_level_in_two_days > 2:
            severity += station_tuple[1]

        stations_risk_level.append((station, severity))

    low_risk = []
    moderate_risk = []
    high_risk = []
    severe_risk = []

    for station_tuple in stations_risk_level:
        if station_tuple[1] < 1:
            low_risk.append(station_tuple[0])
        elif station_tuple[1] < 4:
            moderate_risk.append(station_tuple[0])
        elif station_tuple[1] < 6:
            high_risk.append(station_tuple[0])
        else:
            severe_risk.append(station_tuple[0])

    print("\nLow risk stations:\n")
    for station in low_risk:
        print(station.name)
    print("\nModerate risk stations:\n")
    for station in moderate_risk:
        print(station.name)
    print("\nHigh risk stations:\n")
    for station in high_risk:
        print(station.name)
    print("\nSevere risk stations:\n")
    for station in severe_risk:
        print(station.name)

    print(len(low_risk))
    print(len(moderate_risk))
    print(len(high_risk))
    print(len(severe_risk))


if __name__ == "__main__":
    print("*** CUED Part IA Flood Warning System ***")
    run()
