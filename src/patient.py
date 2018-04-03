from events import Events
import json

class Patient(object):

    """
	One patient object is associated with a patient unique defined by patient_id
	other class members: birth_date: birth date of the patient
						 gender: M or F
						 events object

    """
    def __init__(self, patient_id, birth_date, gender):
        super(Patient, self).__init__()
        self.patient_id = patient_id
        self.birth_date = birth_date
        self.gender = gender
        self.events_data_obj = Events()

    def validate_patient_data(self, event_list):
    	'''
		Patient data is validated according to demographics and then events 
		to populate the respective patient object
    	'''
        if self.validate_demographics():
            self.events_data_obj.append_valid_events(event_list)
        pass

    def validate_demographics(self):
    	'''
		Validate demographics of patient. Check whether gender and date of birth are
		specified

    	'''
        if self.birth_date and self.gender:
            return True
        return False

    def write_json(self):

    	'''
		Validated patient object is written to respective <patient_id>.json file

    	'''
        if self.events_data_obj.valid_events:
            filename = "output/patients/" + str(self.patient_id) + ".json"
            with open(filename, 'w+') as outfile:
            	print("Created file:", filename)
                data = {
                    "birth_date": self.birth_date,
                    "gender": self.gender,
                    "events": self.events_data_obj.valid_events}
                json.dump(data, outfile, indent=4)
        pass
