from datetime import datetime

def validate_task_title(title):
    if not title or len(title.strip()) ==0:
        print ("Error: Title cannot be empty.")
        return False
    if len(title) > 100:
        print("Error: Title cannot exceed 100 characters.")
        return False
    return True
    
def validate_task_description(description):
    if not description or len(description.strip())  ==0:
        print("Error:Description cannot be empty.")
        return False
    if len(description) > 300:
        print("Error:Description cannot exceed 300 characters.")   
        return False
    return True


def validate_due_date(due_date):
    try: 
        date = datetime.strptime(due_date, "%Y-%m-%d")
        if date < datetime.now():
            print("Error:Due date cannot be in the past.")
            return False
        return True
    except ValueError:
        print("Error:Invalid date format.Please use YYYY-MM-DD.")
        return False