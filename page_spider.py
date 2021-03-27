import os
import argparse

def main(database: str, url_list_file:str):
    print('we are going work with ' + database)
    print('we are going scan ' + url_list_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-db', '--database', help='SQLite file name')
    parser.add_argument('-i', '--input', help='File ontaining urls to read')
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)

