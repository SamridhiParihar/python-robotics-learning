# ============================================================
# EXERCISE 1 — PATH EXPLORER
# ============================================================
#
# Goal:
# Practice working with filesystem paths using pathlib.
#
# Requirements:
#
# 1. Import Path from pathlib.
#
# 2. Print the current working directory.
#
# 3. Create a directory named:
#
#       data/
#
# 4. Create a Path object for:
#
#       data/robot.txt
#
# 5. Print:
#       - the path
#       - the filename
#       - the stem
#       - the suffix
#       - the parent directory
#
# 6. Check whether robot.txt exists and print the result.
#
# Constraints:
# - Use pathlib.Path.
# - Do not use os.path.
#


from pathlib import Path

print(Path.cwd())

base = Path("data")

robot_path = base / "robots.txt"

print(robot_path)
print(robot_path.name)
print(robot_path.stem)
print(robot_path.suffix)
print(robot_path.parent)

# ============================================================
# EXERCISE 2 — ROBOT NOTES
# ============================================================
#
# Create:
#
#     data/robot.txt
#
# The file must contain:
#
#     Robot: Atlas
#     Battery: 87
#     Status: operational
#
# Then read the file and print its complete contents.
#
# Requirements:
#
# 1. Use pathlib.Path.
#
# 2. Use a context manager with `with`.
#
# 3. Explicitly use UTF-8 encoding.
#
# 4. First write the file.
#
# 5. Then read the file.
#
# 6. Print the contents.
#
# ============================================================

from pathlib import Path

Path("data").mkdir(parents=True, exist_ok=True)
path = Path("data") / "robot.txt"  

with path.open("w", encoding="utf-8") as file:
    file.write("Robot: Atlas\n")
    file.write("Battery: 87\n")
    file.write("Status: operational\n")

with path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)



# ============================================================
# EXERCISE 3 — APPEND SENSOR LOGS
# ============================================================
#
# Create:
#
#     data/sensor.log
#
# Every time this program runs, append the following reading:
#
#     Temperature: 32.5
#
# Requirements:
#
# 1. Do NOT overwrite existing content.
#
# 2. Each reading must appear on a separate line.
#
# 3. Use pathlib.Path.
#
# 4. Use a context manager.
#
# 5. Use the appropriate file mode for appending.
#
# 6. Run the program multiple times and verify that previous
#    readings remain in the file.
#
# ============================================================

path = base / "sensor.log"

with path.open("a", encoding="utf-8") as file:
    file.write("Temperature: 32.5\n")



# ============================================================
# EXERCISE 4 — SENSOR LOG ANALYZER
# ============================================================
#
# Assume data/sensor.log contains lines such as:
#
#     Temperature: 30.5
#     Temperature: 31.2
#     Temperature: 29.8
#     Temperature: 33.1
#     Temperature: 32.4
#
# Read the file line-by-line.
#
# For every line:
#
# 1. Extract the numeric temperature value.
#
# 2. Convert it to float.
#
# Store/process the values.
#
# Finally calculate and print:
#
#     - minimum temperature
#     - maximum temperature
#     - average temperature
#
# Requirements:
#
# - Do not use pandas.
# - Use pathlib.Path.
# - Do not load the entire file using read().
# - Process the file line-by-line.
#
# ============================================================

path = base / "sensor2.log"
temp_list: list[float] = []
with path.open("r",encoding="utf-8") as lines:
    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        _ , temp = cleaned_line.split(": ")
        temp_list.append(float(temp))

print(temp_list)
# Calculate final statistics
if temp_list:
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    avg_temp = sum(temp_list) / len(temp_list)

    # Print the results
    print(f"Minimum Temperature: {min_temp}")
    print(f"Maximum Temperature: {max_temp}")
    print(f"Average Temperature: {avg_temp:.2f}")
else:
    print("No data found in the log file.")


# ============================================================
# EXERCISE 5 — ROBOT CONFIGURATION JSON
# ============================================================
#
# Create the following Python dictionary:
#
# robot = {
#     "name": "Atlas",
#     "battery": 87,
#     "speed": 1.5,
#     "sensors": ["camera", "lidar", "imu"]
# }
#
# Requirements:
#
# 1. Create a directory:
#
#       config/
#
# 2. Save the dictionary as:
#
#       config/robot.json
#
# 3. Use json.dump().
#
# 4. Make the JSON human-readable using indentation.
#
# 5. Then load the JSON file back using json.load().
#
# 6. Print the resulting Python object.
#
# ============================================================

import json
robot = {
     "name": "Atlas",
     "battery": 87,
     "speed": 1.5,
     "sensors": ["camera", "lidar", "imu"]
 }

Path("config").mkdir(exist_ok=True)

base = Path("config")
path = base / "robot.json"

with path.open("w", encoding="utf-8") as file:
    json.dump(robot, file, indent=4)

with path.open("r", encoding="utf-8") as file:
    robot_ = json.load(file)
print(robot_)


# ============================================================
# EXERCISE 6 — CONFIGURATION VALIDATOR
# ============================================================
#
# Load config/robot.json.
#
# Validate the following:
#
#     name
#       → must be a string
#
#     battery
#       → must be between 0 and 100 inclusive
#
#     speed
#       → must be greater than 0
#
#     sensors
#       → must be a list
#
# Requirements:
#
# 1. Create a validation function:
#
#       validate_robot_config(config)
#
# 2. Raise appropriate exceptions when validation fails.
#
# 3. Do not silently ignore invalid data.
#
# 4. Use the JSON file as the input.
#
# 5. Test the validator with both valid and invalid
#    configurations.
#
# ============================================================


def validate_robot_config(robot: dict) -> None:
    # 1. Validate name
    if "name" not in robot or not isinstance(robot["name"], str):
        raise TypeError("Validation failed: 'name' must be a string.")
    
    # 2. Validate battery (type check + value check)
    if "battery" not in robot or not isinstance(robot["battery"], (int, float)):
        raise TypeError("Validation failed: 'battery' must be a number.")
    if not (0 <= robot["battery"] <= 100):
        raise ValueError("Validation failed: 'battery' must be between 0 and 100 inclusive.")
    
    # 3. Validate speed (type check + value check)
    if "speed" not in robot or not isinstance(robot["speed"], (int, float)):
        raise TypeError("Validation failed: 'speed' must be a number.")
    if robot["speed"] <= 0:  # Must be strictly greater than 0
        raise ValueError("Validation failed: 'speed' must be greater than 0.")
    
    # 4. Validate sensors
    if "sensors" not in robot or not isinstance(robot["sensors"], list):
        raise TypeError("Validation failed: 'sensors' must be a list.")
    
    print("Validation successful! ")

base = Path("config")
path = base / "robot.json"

with path.open("r", encoding="utf-8") as file:
    robot = json.load(file)

validate_robot_config(robot)


# ============================================================
# EXERCISE 7 — JSON → PYTHON → JSON
# ============================================================
#
# Load:
#
#     config/robot.json
#
# Modify the configuration:
#
#     battery = 75
#     speed = 2.0
#
# Save the modified configuration as:
#
#     config/robot_updated.json
#
# Requirements:
#
# 1. Do not modify the original robot.json.
#
# 2. Load using json.load().
#
# 3. Modify the Python dictionary.
#
# 4. Save using json.dump().
#
# 5. Make the output JSON human-readable.
#
# ============================================================

def modify(robot: dict, key: str, val: float | int) -> None:
    if key not in robot or not isinstance(robot[key], type(val)):
        raise TypeError("Validation failed")
    else:
        robot[key] = val
    

base = Path("config")
path = base / "robot.json"
path_updated = base / "robot_updated.json"
with path.open("r", encoding="utf-8") as file:
    robot = json.load(file)

modify(robot, "speed", 2.0)
modify(robot, "battery", 75)

with path_updated.open("w", encoding="utf-8") as file:
    robot = json.dump(robot, file , indent=4)

 
# ============================================================
# EXERCISE 8 — EXPERIMENT LOGGER
# ============================================================
#
# Create the following directory structure:
#
#     experiments/
#         run_001/
#             config.json
#             results.txt
#
# Requirements:
#
# 1. Create the directories programmatically.
#
# 2. config.json must contain:
#
#     {
#         "robot": "Atlas",
#         "controller": "PID",
#         "duration": 30
#     }
#
# 3. results.txt must contain some experiment results.
#
# 4. The program must work even if run_001 does not already exist.
#
# 5. Use pathlib.Path.
#
# 6. Use JSON for config.json.
#
# 7. Use normal text-file operations for results.txt.
#
# ============================================================

import json
from pathlib import Path

base_dir = Path("experiments") / "run_001"
base_dir.mkdir(parents=True, exist_ok=True)

#  paths
config_path = base_dir / "config.json"
results_path = base_dir / "results.txt"

config_data = {
    "robot": "Atlas",
    "controller": "PID",
    "duration": 30
}

with config_path.open("w", encoding="utf-8") as file:
    json.dump(config_data, file, indent=4)

results_content = (
    "--- Experiment Run 001 Results ---\n"
    "Status: Completed successfully\n"
    "Average Error: 0.042m\n"
    "Max Overshoot: 0.12m\n"
)

with results_path.open("w", encoding="utf-8") as file:
    file.write(results_content)

print("Experiment directory structure and logs generated successfully! ")



# ============================================================
# EXERCISE 9 — CSV SENSOR DATA
# ============================================================
#
# Create:
#
#     data/sensors.csv
#
# With the following data:
#
#     timestamp,temperature,battery
#     0,30.5,100
#     1,31.2,98
#     2,32.1,95
#     3,33.0,92
#     4,34.4,89
#
# Read the CSV using Python's built-in csv module.
#
# Calculate:
#
#     1. Average temperature
#     2. Minimum battery
#     3. Maximum battery
#
# Requirements:
#
# - Use csv module.
# - Do not use pandas.
# - Convert numeric values to appropriate numeric types.
#
# ============================================================

import csv

base = Path("data")
base.mkdir(parents=True, exist_ok=True)
path = base / "sensors.csv"

csv_content = (
    "timestamp,temperature,battery\n"
    "0,30.5,100\n"
    "1,31.2,98\n"
    "2,32.1,95\n"
    "3,33.0,92\n"
    "4,34.4,89\n"
)

with path.open("w", encoding="utf-8") as file:
    file.write(csv_content)

temperature : list[float] = []
battery : list[int] = []

with path.open("r",encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        temperature.append(float(row["temperature"]))
        battery.append(int(row["battery"]))

if temperature and battery  :
    avg_temp = sum(temperature) / len(temperature)
    min_battery = min(battery)
    max_battery = max(battery)

    # Print the results formatted to 2 decimal places
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Min Battery : {min_battery}")
    print(f"Max Battery : {max_battery}")


else:
    print("No data found in the CSV file.")




# ============================================================
# EXERCISE 10 — SAFE JSON LOADER
# ============================================================
#
# Write:
#
#     def load_json(path: Path) -> dict:
#         ...
#
# The function must:
#
# 1. Check whether the file exists.
#
# 2. Raise FileNotFoundError if it doesn't exist.
#
# 3. Open the file safely.
#
# 4. Parse the JSON.
#
# 5. Allow invalid JSON errors to propagate appropriately.
#
# 6. Return the loaded dictionary.
#
# Requirements:
#
# - Use pathlib.Path.
# - Use json.load().
# - Use a context manager.
# - Do not use a bare `except`.
# - Do not silently swallow errors.
#
# ============================================================

def load_json(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(f"JSON configuration file not found at: {path.resolve()}")
    
    with path.open("r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            
            if not isinstance(data, dict):
                raise TypeError(f"Expected a JSON object/dictionary, but got {type(data).__name__}")
                
            return data
            
        except json.JSONDecodeError:
            print(f"Critial parsing error: The file at {path} contains invalid JSON.")
            raise


base = Path("config")
base.mkdir(exist_ok=True)

valid_path = base / "valid.json"
invalid_path = base / "invalid.json"
missing_path = base / "ghost.json"

valid_path.write_text('{"robot": "Atlas", "battery": 87}', encoding="utf-8")
invalid_path.write_text('{"robot": "Atlas", "battery": }', encoding="utf-8") # Missing value

print("--- Test 1: Valid JSON ---")
try:
    print(load_json(valid_path))
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n--- Test 2: Missing File ---")
try:
    load_json(missing_path)
except FileNotFoundError as e:
    print(f"Caught expected error: {e}")

print("\n--- Test 3: Invalid JSON Structure ---")
try:
    load_json(invalid_path)
except json.JSONDecodeError as e:
    print(f"Caught expected error: {e}")
