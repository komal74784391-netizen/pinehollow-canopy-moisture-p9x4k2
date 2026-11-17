import pandas as pd

def flag_gaps(frame, max_gap='2H'):
    gap = frame['timestamp'].diff()
    return gap > pd.Timedelta(max_gap)

def flag_saturation(frame, low=2.0, high=98.0):
    return (frame['humidity_pct'] < low) | (frame['humidity_pct'] > high)
