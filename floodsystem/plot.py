"""
This module includes a collection on functions related to flood levels plotting.
"""

import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):
    """Plot the water levels of a station given certain dates and levels.
    Also accepts lists as input, showing up to the first 6 stations."""

    if isinstance(station, list):
        if len(station) >= 6:
            stations = station[0:6]
            length = 6
        else:
            stations = station
            length = len(stations)
        for i in range(length):
            plt.subplot(int(length / 3) + 1, (int(length / 2) > 0) + int(length / 5) + 1, i + 1)
            plt.plot(dates[i], levels[i])
            plt.xlabel("Dates")
            plt.ylabel("Water Level (m)")
            plt.xticks(rotation=45)
            plt.title(stations[i].name)
            plt.plot(dates[i], [stations[i].typical_range[0]] * len(dates[i]), 'g--')
            plt.plot(dates[i], [stations[i].typical_range[1]] * len(dates[i]), 'g--')

            # Display plot
            plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()

    else:
        plt.plot(dates, levels)
        plt.xlabel("Dates")
        plt.ylabel("Water Level (m)")
        plt.xticks(rotation=45)
        plt.title(station.name)
        plt.plot(dates, [station.typical_range[0]] * len(dates), 'g--')
        plt.plot(dates, [station.typical_range[1]] * len(dates), 'g--')

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()


def plot_water_level_with_fit(station, dates, levels, p, show_typical_range=True):
    """Plot water levels for a station with polyfit.
    Also accepts lists as input, showing up to the first 6 stations."""

    if isinstance(station, list):
        if len(station) >= 6:
            stations = station[0:6]
            length = 6
        else:
            stations = station
            length = len(stations)
        for i in range(length):
            plt.subplot(int(length / 3) + 1, (int(length / 2) > 0) + int(length / 5) + 1, i + 1)
            plt.plot(dates[i], levels[i])
            x = matplotlib.dates.date2num(dates[i])
            poly, shift = polyfit(dates[i], levels[i], 4)
            if poly is not None:
                plt.plot(x, poly(x - shift))
            if show_typical_range:
                plt.plot(x, [stations[i].typical_range[0]] * len(x), 'g--')
                plt.plot(x, [stations[i].typical_range[1]] * len(x), 'g--')
            plt.xlabel("Dates")
            plt.ylabel("Water Level (m)")
            plt.xticks(rotation=45)
            plt.title(stations[i].name)

            # Display plot
            plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()

    else:
        plt.plot(dates, levels)
        plt.xlabel("Dates")
        plt.ylabel("Water Level (m)")
        plt.xticks(rotation=45)
        plt.title(station.name)
        x = matplotlib.dates.date2num(dates)
        poly, shift = polyfit(dates, levels, 4)
        if poly is not None:
            plt.plot(x, poly(x - shift))
        if show_typical_range:
            plt.plot(x, [station.typical_range[0]] * len(x), 'g--')
            plt.plot(x, [station.typical_range[1]] * len(x), 'g--')

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()
