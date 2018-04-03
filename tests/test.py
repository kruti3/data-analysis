import sys
sys.path.append("../src")
import unittest
from merge_tables import sort_files_by_ID
from merge_tables import generate_all_json
from generate_stats import generate_stats
import os

def number(n):

    return n%2

class UnitTest_MergeTables(unittest.TestCase):
    """docstring for UnitTest_Tables"""
    def test_One(self):
        
        demographics_file = "../tests/input/demo.psv" 
        events_file = "../tests/input/events.psv"
        sort_files_by_ID(demographics_file, events_file)

        new_demographics_file = demographics_file[:-4] + "_sorted.psv"
        new_events_file = events_file[:-4] + "_sorted.psv"

        self.assertTrue(os.stat(new_demographics_file).st_size != 0, "Empty file created")
        self.assertTrue(os.stat(new_events_file).st_size != 0, "Empty file created")
        pass

    def test_Two(self):
        demographics_file = "../tests/input/demo_sorted.psv" 
        events_file = "../tests/input/events_sorted.psv"
        
        generate_all_json(demographics_file, events_file)
        path = "../tests/output/patients/"

        print("id 2 doesn't have demographics")
        self.assertTrue(not os.path.exists(path+"2.json"), "2.json file present")

        print("id 3 doesn't have events")
        self.assertTrue(not os.path.exists(path+"3.json"), "2.json file present")

        print("id 4 doesn't have icd code")
        self.assertTrue(not os.path.exists(path+"4.json"), "4.json file present")

        print("id 5 has valid data")
        self.assertTrue(os.path.exists(path+"5.json"), "5.json file absent")

    def test_Three(self):

        path = "../tests/output/patients/"
        generate_stats(path)

        path = "../tests/output/final_stats.json"
        self.assertTrue(os.path.exists(path), "final_stats.json file absent")

def main():
    unittest.main()
    pass

if __name__ == '__main__':
    main()