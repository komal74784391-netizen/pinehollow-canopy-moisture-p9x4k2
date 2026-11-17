import argparse, pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stations', required=True)
    args = parser.parse_args()
    df = pd.read_csv(args.stations)
    df['vpd_kpa'] = 0.61 * (1 - df['humidity_pct'] / 100.0)
    df.to_csv('features.csv', index=False)
    print('wrote', len(df), 'feature rows')

if __name__ == '__main__':
    main()
