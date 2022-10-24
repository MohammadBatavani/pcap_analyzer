import argparse
import os
import sys
from process_packet import process_csv , process_arrival_time_average

#Error handling for csv file:
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSV reader')
    parser.add_argument('--csv', metavar='<csv file name>', required=True)
    args = parser.parse_args()
    
    file_name = args.csv
    if not os.path.isfile(file_name):
        print('"{}" does not exist'.format(file_name), file=sys.stderr)
        sys.exit(-1)

    proccesed_data=process_csv(file_name)
    process_arrival_time_average(proccesed_data)
    sys.exit(0)