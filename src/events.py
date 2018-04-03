import re 

# global variables
ICD_9 = "http://hl7.org/fhir/sid/icd-9-cm"
ICD_10 = "http://hl7.org/fhir/sid/icd-10"

class Events(object):
    """
    One Events object contains all the events associated with a particular patient
    valid_events: contains all the validated events associated with a patient
    current_event : contains current event under analysis
    """

    def __init__(self):
        super(Events, self).__init__()
        self.valid_events = list()
        self.current_event = dict()

    def append_valid_events(self, events_list):
        '''
        Adds all the validated events associated to a patient to valid_events list
        '''

        for event in events_list:
            if self.validate_event(event):
                self.valid_events.append(self.current_event)
        pass

    def validate_event(self, event):

        '''
        Validates one event associated with a patient
        input: one entry line present in demo_sorted.psv
        '''
        event = re.sub(r"[\n\t\s]*", "", event)
        current_id, visit_date, icd_version, icd_code = event.split("|")
        if current_id and visit_date and (icd_version=="9" or icd_version=="10") and icd_code:
                if icd_version == "9":
                    val = ICD_9 
                else:
                    val = ICD_10
                self.current_event = {
                    "date": visit_date,
                    "system": val,
                    "code": icd_code
                }
                return True
        return False
