import os
import json
from datetime import datetime
import sys

TOTAL_COUNT = 0
FEMALE_COUNT = 0
MALE_COUNT = 0 
GENDER = list()
AGE = list()
TIMELINE = list()

def store_values(data):
    '''
    Populates global data variables from data (data is associated with one patient)

    '''
    GENDER.append(data["gender"])
    
    birth_date = data["birth_date"]
    all_events = data["events"]
    if len(all_events)==1:
        TIMELINE.append(0)
        last_event_day = all_events[0]["date"]
    else: 
        first_event_day = all_events[0]["date"]
        last_event_day = all_events[-1]["date"]
        days = days_between(first_event_day, last_event_day)
        TIMELINE.append(days)

    age = years_between(birth_date, last_event_day)
    AGE.append(age)
    pass

def days_between(d1, d2):

    '''
    Calculates number of days between two dates
    Input: date d1, date d2
    Output: number of years (float)
    '''
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return ((d2 - d1).days)

def years_between(d1, d2):

    '''
    Calculates number of years between two dates
    Input: date d1, date d2
    Output: number of years (float)
    '''
    return (days_between(d1, d2)/365.0)

def calculate_stats(directory):
    
    '''
    Required stats are calculated from the stored data which is declared as global

    '''
    print("Writing statistics to output/final_statistics.txt")
    FEMALE_COUNT = GENDER.count("F")
    MALE_COUNT = GENDER.count("M")
    TOTAL_COUNT = len(GENDER)

    filename = directory + "../final_stats.json"
    with open(filename, 'w+') as outfile:
         print("Created file:", filename)
         data = {
                    "total_valid_patients": TOTAL_COUNT,
                    "female_patients": FEMALE_COUNT,
                    "male_patients": MALE_COUNT,
                    "AGE": [{
                    "Max": max(AGE),
                    "Min": min(AGE),
                    "Median": median(AGE)
                    }],
                    "TIMELINE": [ {
                    "Max": max(TIMELINE),
                    "Min": min(TIMELINE),
                    "Median": median(TIMELINE)
                    }]
                    }
         json.dump(data, outfile, indent=4)
    '''
    file = open("output/final_statistics.json","w") 
    file.write("Total number of valid patients " + str(TOTAL_COUNT) + "\n")
    file.write("Total number of valid female patients " + str(FEMALE_COUNT)+ "\n")
    file.write("Total number of valid male patients " + str(MALE_COUNT)+ "\n")

    file.write("Stats for age of valid patients (in years)\n")
    file.write("Maximum :" + str(max(AGE))+ "\n")
    file.write("Minimum :" + str(min(AGE))+ "\n")
    file.write("Median :" + str(median(AGE))+ "\n")
    
    file.write("Stats for timeline of valid patients (in number of days)\n")
    file.write("Maximum :" + str(max(TIMELINE))+ "\n")
    file.write("Minimum :" + str(min(TIMELINE))+ "\n")
    file.write("Median :" + str(median(TIMELINE))+ "\n")
    
    file.close()
    '''
    pass

def median(array):
    '''
    Calculates median of the input list 
    Input: list
    Output: median of the list
    '''
    array = sorted(array)
    n = len(array)
    if n%2:
        return array[n/2]
    else:
        return (array[(n/2)] + array[(n/2)-1])/2.0

def generate_stats(directory = "output/patients/"):
    '''
    iterates each of the files of valid patients
    '''
    
    print("Reading valid patients' data from ", directory)
    
    for loc, dirs, files in os.walk(directory):
        TOTAL_COUNT = len(files)
        for file in files:
            curr_filename = os.path.join(loc, file)
            
            with open(curr_filename) as json_data:
                data = json.load(json_data)
                store_values(data)

    calculate_stats(directory)
    pass

def main():
    
    if len(sys.argv)>1:
        generate_stats(argv[1])
    else:
        generate_stats()
    pass


if __name__ == '__main__':
    main()