def course_room_number():
    return {
        "CSC101": "Room 3004",
        "CSC102": "Room 4501",
        "CSC103": "Room 6755",
        "NET110": "Room 1244",
        "COM241": "Room 1411"
    }

def course_instructor():
    return {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

def course_time():
    return {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

def main():
    course = input("Enter the course number (X to quit): ")
    while course != "X":
        if course not in course_room_number():  # Check if the course is in the dictionary
            print("The course number is not valid.")
        else:
            print("The course " + course + " is in " + course_room_number()[course] + " at " + course_time()[course] + 
                  " and the instructor is " + course_instructor()[course])
        course = input("Enter the course number: ")

if __name__ == "__main__":
    main()