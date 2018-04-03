PYTHON VERSION 2.7.13

Following is the description of directory structure:

_ input
	__ demo.psv
	__ demo_sorted.psv* 
	__ events.psv
	__ events_sorted.psv*
_ output
	__ patients
		_ <patient_id>.json* 
	__ final_stats.json* (-> contains expected stats data)
_ src
	__ events.py
	__ generate_stats.py
	__ merge_tables.py
	__ patient.py
_ tests
	_ input
		__ demo.psv
		__ demo_sorted.psv* 
		__ events.psv
		__ events_sorted.psv*
	_ output
	    __ patients
			_ <patient_id>.json* 
		__ final_stats.json* (-> contains expected stats data)
	_ test.py 
 README.md
 run_me.sh

Note:
1. demo -> demo_sorted: file is sorted by patient_id
	events -> events_sorted: file is sorted by patient_id
2. *are the files generated by the code.

Steps to run the code:
1. chmod 755 run_me.sh
2. ./run_me.sh

Steps to run the test cases:
1. python test.py
