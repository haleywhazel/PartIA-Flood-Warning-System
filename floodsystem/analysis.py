"""
This module contains analysis functions.
"""

import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    """Least squares polynomial fit. Returns polynomial and shifted date x values."""
    if dates != [] and levels != []:
        x = matplotlib.dates.date2num(dates)
        p_coeff = np.polyfit(x - x[0], levels, p)
        poly = np.poly1d(p_coeff)
        return (poly, x[0])
    else:
        return None, None
