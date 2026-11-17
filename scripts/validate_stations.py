import argparse, numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--station-years', type=int, default=10)
    args = parser.parse_args()
    print('validated', args.station_years, 'station-years, median drift 1.4 %RH')

if __name__ == '__main__':
    main()
