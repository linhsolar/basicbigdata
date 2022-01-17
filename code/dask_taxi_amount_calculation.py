import dask.dataframe as dd
import argparse

'''
the field name of amount is "total_amount"
'''

if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', help='input taxi data file')
    args = parser.parse_args()
    input_file=args.input_file
    taxi_df =dd.read_csv(input_file)
    total_amount =taxi_df["total_amount"].sum().compute()
    print(f'The total amount calculated from this file is {total_amount}')
