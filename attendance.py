
"""
Attendance Register

Task:
- Track attendance of students.
- Use a dictionary { "student_id": {"name": str, "present_days": list, "absent_days": list} }
- Functions to mark attendance, check history, and get reports.
- Use your head/logic to mark multiple students at once.
- Use **kwargs for flexible reporting (e.g., only_present=True).

// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Student class with mark_present() and mark_absent().
- AttendanceRegister class that manages records.
"""

import datetime

attendance = {}

def register_student(student_id, name):
    #"""Register a student in the system."""
	if student_id not in attendance:
		attendance[student_id] = {
                "name": name,
                "present_days": [],
                "absent_days" : []
		}
		print(attendance)
	else:
		print(f"Student ID {student_id} already exists.")
register_student(1, "Tosin")
    #pass

def mark_present(*student_ids):
    #"""Mark multiple students as present for today."""
	today = str(datetime.date.today())
	for sid in student_ids:
		if sid in attendance:
			if today not in attendance[sid]["present_days"]:
                		attendance[sid]["present_days"].append(today)
            
	    		if today in attendance[sid]["absent_days"]:
                		attendance[sid]["absent_days"].remove(today)
        	else:
            		print(f"Student ID {sid} not found.")
mark_present(1, 3)
   # implement logic
    #pass

def mark_absent(*student_ids):
    #"""Mark multiple students as absent for today."""
	today = str(datetime.date.today())
    	for sid in student_ids:
        	if sid in attendance:
            		if today not in attendance[sid]["absent_days"]:
                		attendance[sid]["absent_days"].append(today)
            		
			if today in attendance[sid]["present_days"]:
                		attendance[sid]["present_days"].remove(today)
        	else:
            		print(f"Student ID {sid} not found.")
mark_absent(1, 2, 3)
    #implement logic
    #pass

def get_report(**kwargs):
    #"""Generate attendance report with optional filters."""
	report = {}
	today = str(datetime.date.today())

    	for sid, data in attendance.items():
        	only_present = True

        	if kwargs.get("student_id") and kwargs["student_id"] != sid:
            		only_present = False

        	if kwargs.get("only_present"):
            		only_present = today in data["present_days"]

        	if kwargs.get("only_absent"):
            		only_present = today in data["absent_days"]

        	if include:
            		report[sid] = data

    	return report
get_report(only_present = True)

    # implement logic

