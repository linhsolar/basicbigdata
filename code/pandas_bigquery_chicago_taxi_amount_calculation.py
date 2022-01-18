from google.oauth2 import service_account
import pandas as pd
import pandas_gbq
import argparse

'''
You need to setup google service account for accessing your google bigquery instance.
'''
if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--credential_file', help='google credential file/service account')
    parser.add_argument('-p', '--project_id', help='google project id')
    args = parser.parse_args()
    credentials = service_account.Credentials.from_service_account_file(args.credential_file
    )
    query="SELECT sum(trip_total) as total_amount FROM bigquery-public-data.chicago_taxi_trips.taxi_trips"
    taxi_df = pandas_gbq.read_gbq(query,project_id=args.project_id, credentials=credentials)
    total_amount =taxi_df["total_amount"].sum()
    print(f'The total amount calculated  is {total_amount}')
