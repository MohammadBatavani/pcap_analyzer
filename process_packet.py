import csv
from operator import le
import pprint
from struct import pack

##Reading a CSV File of captured packets and make a dictionray of source IPs and their ariaval times:
def process_csv(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        packet = dict()
        for row in csv_reader:
            if row["ip.src"] not in list(packet.keys()):
                packet[row['ip.src']] = []
                packet[row['ip.src']].append(row["frame.time_epoch"])
            elif row["ip.src"] in list(packet.keys()):
                packet[row['ip.src']].append(row["frame.time_epoch"])
    return packet
##To determine average arrival time of packets related to each links:
def process_arrival_time_average(packet_dict):
    avgDict = {}
    for ip,time in packet_dict.items():
        sum = 0
        for i in range(1,len(time)):
            sum += float(time[i])-float(time[i-1])

        avg = sum / (len(time) - 1)
        avgDict[ip] = avg
    sorted_avg = sorted(avgDict.items(), key=lambda item: item[1])
    print('The two fastest links are:', '\n', sorted_avg[0],'\n', sorted_avg[1])
    
