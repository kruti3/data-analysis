## Longitudinal Patient Data Interview Question

Here are two tables, events.psv containing dates and medical events in an 
individual patient’s timeline, and demo.psv containing demographic information
about the patient. In this case medical events are represented as ICD codes, 
which is an industry standard coding system for representing diagnoses. Each 
entry in the events table therefore represents a patient receiving a single 
diagnosis on that date in either the ICD-9 or ICD-10 coding system.

The `events.psv` file has the following columns:
- `patient_id`: The ID for the patient
- `date`: the date of the event
- `icd_version`: the ICD code version (9 or 10)
- `icd_code`: the ICD code representing a medical event in the patient’s 
history

The `demo.psv` file has the following columns:
- `patient_id`: The ID for the patient
- `birth_date`: Patient’s birthday
- `gender`: “M” or “F”

Join these tables together to produce a series of JSONs, one per patient, 
representing that patient’s complete health record. The patient JSON you 
create should contain the demographic information for the patient and a list 
of events. Each event should have the code, the date when it happened (ISO 
format preferred) and a URL for the code system for the event. 

- The URL for ICD-9 codes is: http://hl7.org/fhir/sid/icd-9-cm
- The URL for ICD-10 codes is: http://hl7.org/fhir/sid/icd-10

Some patients may not have any events, in which case do not create a patient 
JSON. Some events may have an empty code, in which case, don’t create an entry
for that code in the “eventss” section. Some events may be assigned to a patient
for which we have no demographic information, if so, don’t create a JSON for
that patient. Only events that have a date, a code and a system are valid and 
should be included, and only patients that have both complete demographic 
information (both birthdate and gender) AND at least one event should be 
included.

The specific design/key names of the JSON isn’t set in stone, but an example 
is provided below:

```
{
    "birth_date": "1974-09-02",
    "gender": "F",
    "events": [
        {
            "date": "2016-03-01",
            "system": "http://hl7.org/fhir/sid/icd-10",
            "code": "Z01.00"
        },
        {
            "date": "2014-05-23",
            "system": "http://hl7.org/fhir/sid/icd-9-cm",
            "code": "367.0"
        }
    ]
}
```

Once you have the data, please compute a few statistics on the data:

- Total number of valid patients
- Maximum/Minimun/Median length of patient timelines in days 
(the number of days contained within an individual patient’s first event and a 
patient’s last event)
- Count of males and females
- Maximum/Minimum/Median age of patient as calculated between birthdate and 
last event in timeline


Please send us a zip file of a folder with one JSON generated per patient, the 
requested statistics, as well as any code used to generate those counts and 
JSONS, and any tests (unit or otherwise) you may have written. Also include 
instructions on how to run that code, either in a brief readme or in comments 
within the code. We generally use Python or Scala here but we care more about 
the logic and thought process than the language. Pick whatever language you 
like, just be sure to include instructions on how to build and run your code. 
If using python, we would strongly prefer a solution relying exclusively on the
python standard library and not numpy, pandas or similar libraries.

Good luck! 
