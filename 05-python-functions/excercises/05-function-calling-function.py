# Exercise 17:
# Create:
#   celsius_to_fahrenheit(celsius)
#   fahrenheit_to_celsius(fahrenheit)
#
# Then create:
#   convert_temperature(value, unit)
#
# convert_temperature() should call the appropriate conversion function
# based on the supplied unit.
#
# Test both conversion directions.

def celsius_to_fahrenheit(celsius: float) -> float:
    '''Convert Celsius to Fahrenheit'''
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    '''Convert Fahrenheit to Celsius'''
    return (fahrenheit - 32) * 5/9

def convert_temperature(value: float, unit: str) -> float:
    '''Convert the given value to the opposite scale based on the supplied unit ('C' or 'F')'''
    normalized_unit = unit.upper()
    
    if normalized_unit == "C":
        # The input value is in Celsius; convert it to Fahrenheit
        return celsius_to_fahrenheit(value)
    elif normalized_unit == "F":
        # The input value is in Fahrenheit; convert it to Celsius
        return fahrenheit_to_celsius(value)
    else:
        # Raise an error if the unit is unrecognized
        raise ValueError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

# Test Cases
print(convert_temperature(0, "C"))    
print(convert_temperature(100, "c")) 
print(convert_temperature(98.6, "F")) 

# Exercise 18:
# Create:
#   calculate_average(marks)
#   calculate_grade(average)
#   generate_result(marks)
#
# calculate_average() should calculate the average marks.
#
# calculate_grade() should convert the average into a grade.
#
# generate_result() should call both functions and return a dictionary
# containing the average and grade.
#
# Keep each function responsible for one clear task.
def calculate_average(marks: list[float]) -> float:
    '''Calculate and return the average of a list of marks'''
    if not marks:
        return 0.0
    
    total = 0.0
    for mark in marks:
        total += mark
    return total / len(marks)

def calculate_grade(average: float) -> str:
    '''Convert the average mark into a letter grade'''
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def generate_result(marks: list[float]) -> dict[str, float | str]:
    '''Combine average and grade calculations into a single summary dictionary'''
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    
    return {
        "average": round(avg, 2),  # Rounded to 2 decimal places for clean output
        "grade": grade
    }

# Test Cases
student_a = [85.5, 92.0, 78.0, 90.0]
student_b = [55, 62, 48]
student_c = []

print(generate_result(student_a))  
print(generate_result(student_b))  
print(generate_result(student_c))  

