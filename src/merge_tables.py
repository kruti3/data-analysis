import os
from patient import Patient
import csv
import linecache
import sys
import re

FILE_POINTER = 1

def read_all_patient_details(demographics_file):

    '''
    Gets patients demographics from demo_sorted.psv
    '''
    print("Reading patient demographics")
    file = open(demographics_file, "r")
    reader = csv.reader(file)
    patient_list = list()
    for row in reader:
        patient_list.extend(row)

    file.close()
    return patient_list


def read_events(patient_id, events_file):

    '''
    Get all events for patient_id
    Input: patient_id

    Output: events_list (containing entries from events.psv)

    '''
    global FILE_POINTER
    events_list = list()

    while True:
        current_line = linecache.getline("input/events_sorted.psv", FILE_POINTER)
        current_line = re.sub(r"[\n\t\s]*", "", current_line)
        if len(current_line):
            current_id, visit_date, icd_version, icd_code = current_line.split("|")
            current_id = int(current_id[3:])
            if current_id == patient_id:
                events_list.append(current_line)
                FILE_POINTER += 1
            elif current_id > patient_id:
                break
            else:
                FILE_POINTER += 1
        else:
            break

    return events_list


def generate_all_json(demographics_file="input/demo_sorted.psv", events_file="input/events_sorted.psv"):
    '''
    Generating all valid patient json files one by one (can extend to batch processing to open events once 
    per batch)
    '''
    print("Merging Tables...")
    patient_list = read_all_patient_details(demographics_file)

    for one_patient in patient_list:
        one_patient = re.sub(r"[\n\t\s]*", "", one_patient)
        patient_id, birth_date, gender = one_patient.split("|")
        patient_id = int(patient_id[3:])
        patient_object = Patient(patient_id, birth_date, gender)

        event_list = read_events(patient_id, events_file)
        if len(event_list):
            patient_object.validate_patient_data(event_list)
            patient_object.write_json()
    pass

def sort_files_by_ID(demographics_file="input/demo.psv", events_file="input/events.psv"):
    '''
    Sort both files by patient ID
    (To avoid loading entire file contents into memory)
    '''
    print("Sorting input files...")
    print("Storing as *_sorted")
    new_demographics_file = demographics_file[:-4] + "_sorted.psv"
    new_events_file = events_file[:-4] + "_sorted.psv"

    os.system('sort -V ' + demographics_file +'| head -n -1 > ' + new_demographics_file)
    os.system('sort -V ' + events_file + ' | head -n -1 > ' + new_events_file)
    os.system('mkdir output/patients/')
    return new_demographics_file, new_events_file


def main():

    if len(sys.argv)>1:
        demographics_file = sys.argv[1]
        events_file = sys.argv[2]
        new_demographics_file, new_events_file = sort_files_by_ID(demographics_file, events_file)
    else:
        new_demographics_file, new_events_file = sort_files_by_ID()
    generate_all_json(new_demographics_file, new_events_file)
    pass


if __name__ == '__main__':
    main()
