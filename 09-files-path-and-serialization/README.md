# Chapter 9 — Files, Paths & Serialization

## Overview

So far, most Python programs we have written have worked with data that existed only while the program was running.

```text
Program starts
     ↓
Data exists in memory
     ↓
Program runs
     ↓
Program exits
     ↓
Data is lost
```

Real-world applications need **persistent data**.

Examples:

- configuration files
- logs
- datasets
- experiment results
- calibration data
- saved application state
- robot parameters
- sensor measurements

Python provides several tools for working with persistent data.

This chapter covers:

- Files and filesystem concepts
- Paths
- `pathlib`
- Current working directory
- Reading and writing files
- File modes
- Text vs binary files
- Encoding
- Context managers
- JSON
- Serialization and deserialization
- CSV
- Safe file handling
- Configuration-driven applications
- Robotics-oriented file handling

---

# 1. Filesystem Fundamentals

A filesystem organizes data into:

```text
Directories
    ↓
Files
```

For example:

```text
python-robotics-learning/
│
├── README.md
├── pixi.toml
│
├── 08-oop/
│   └── README.md
│
└── 09-files-paths-serialization/
    ├── README.md
    ├── data/
    │   ├── robots.json
    │   └── sensor_data.csv
    │
    └── src/
        └── main.py
```

A **file** stores data.

A **directory** organizes files and other directories.

---

# 2. Paths

A path tells the operating system where something exists.

There are two important types of paths:

- Absolute paths
- Relative paths

---

## 2.1 Absolute Path

An absolute path describes a location starting from the filesystem root.

Example:

```text
/home/samridhi/python-robotics-learning/data/robots.json
```

It identifies the exact location independently of the current directory.

Conceptually:

```text
/
└── home
    └── samridhi
        └── python-robotics-learning
            └── data
                └── robots.json
```

---

## 2.2 Relative Path

A relative path describes a location relative to the current working directory.

Example:

```text
data/robots.json
```

If the current working directory is:

```text
/home/samridhi/python-robotics-learning
```

then:

```text
data/robots.json
```

refers to:

```text
/home/samridhi/python-robotics-learning/data/robots.json
```

### Important

Relative paths depend on the **current working directory**.

This is a common source of bugs in real applications.

---

# 3. Current Working Directory

Python can determine the current working directory using `pathlib`.

```python
from pathlib import Path

print(Path.cwd())
```

Example:

```text
/home/samridhi/python-robotics-learning
```

`cwd` means:

> Current Working Directory

---

# 4. `pathlib`

Modern Python code should generally prefer `pathlib` for filesystem paths.

Instead of:

```python
import os

path = os.path.join("data", "robots.json")
```

prefer:

```python
from pathlib import Path

path = Path("data") / "robots.json"
```

This is one of the most important habits to develop.

---

# 5. Why `Path` Is Useful

A `Path` is not just a string.

It is an object representing a filesystem path.

Example:

```python
from pathlib import Path

path = Path("data") / "robot.json"
```

It provides useful operations.

```python
path.exists()
path.is_file()
path.is_dir()
path.name
path.stem
path.suffix
path.parent
```

---

## 5.1 `name`

```python
path.name
```

Example:

```text
robot.json
```

---

## 5.2 `stem`

```python
path.stem
```

Result:

```text
robot
```

The stem is the filename without the extension.

---

## 5.3 `suffix`

```python
path.suffix
```

Result:

```text
.json
```

---

## 5.4 `parent`

```python
path.parent
```

Result:

```text
data
```

---

## 5.5 Example

```python
from pathlib import Path

path = Path("data/robot.json")

print(path)
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
```

Output:

```text
data/robot.json
robot.json
robot
.json
data
```

---

# 6. Creating Directories

A directory can be created using:

```python
from pathlib import Path

Path("data").mkdir()
```

If the directory might already exist:

```python
Path("data").mkdir(exist_ok=True)
```

This prevents an error when the directory already exists.

---

## 6.1 Creating Nested Directories

Suppose we want:

```text
experiments/
└── run_001/
```

We can use:

```python
from pathlib import Path

Path("experiments/run_001").mkdir(
    parents=True,
    exist_ok=True
)
```

### `parents=True`

Creates missing parent directories.

### `exist_ok=True`

Does not raise an error if the directory already exists.

---

# 7. Opening Files

Python provides the built-in `open()` function.

Example:

```python
file = open("data.txt")
```

However, files should generally be used with a **context manager**.

Preferred:

```python
with open("data.txt") as file:
    ...
```

Or with `Path`:

```python
from pathlib import Path

path = Path("data.txt")

with path.open() as file:
    ...
```

---

# 8. Why `with` Is Important

Opening a file consumes an operating-system resource.

The file should eventually be closed.

Using:

```python
with path.open() as file:
    ...
```

ensures cleanup happens automatically.

Conceptually:

```text
Enter context
     ↓
Open file
     ↓
Use file
     ↓
Exit context
     ↓
Close file
```

This is closely related to the context-manager concepts from Chapter 6.

---

# 9. Writing Text Files

Example:

```python
from pathlib import Path

path = Path("robot.txt")

with path.open("w", encoding="utf-8") as file:
    file.write("Robot: Atlas")
```

The file now contains:

```text
Robot: Atlas
```

---

# 10. File Modes

Common file modes:

| Mode | Meaning |
|---|---|
| `"r"` | Read |
| `"w"` | Write / overwrite |
| `"a"` | Append |
| `"x"` | Create new file; fail if it exists |
| `"rb"` | Read binary |
| `"wb"` | Write binary |

---

# 11. Write Mode

```python
with path.open("w", encoding="utf-8") as file:
    file.write("Hello")
```

`"w"` means:

> Open for writing.

### Important

If the file already exists, its previous contents are normally **overwritten**.

For example:

```text
Before:

Hello
World
```

After:

```python
with path.open("w") as file:
    file.write("New data")
```

The file becomes:

```text
New data
```

The previous contents are gone.

---

# 12. Append Mode

Use `"a"` when existing content should remain.

```python
with path.open("a", encoding="utf-8") as file:
    file.write("New reading\n")
```

If the file contained:

```text
Reading 1
Reading 2
```

after appending:

```text
Reading 1
Reading 2
New reading
```

This is useful for:

- logs
- sensor readings
- experiment data
- audit trails

---

# 13. Reading Text Files

Read the complete file:

```python
with path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

---

## 13.1 Reading Lines

```python
with path.open("r", encoding="utf-8") as file:
    lines = file.readlines()
```

`lines` becomes a list.

Example:

```text
[
    "Robot: Atlas\n",
    "Battery: 87\n",
    "Status: operational\n"
]
```

---

## 13.2 Iterating Over a File

A better approach for potentially large files:

```python
with path.open("r", encoding="utf-8") as file:
    for line in file:
        print(line)
```

This processes the file incrementally rather than necessarily loading the entire file into memory.

This becomes important when working with:

- large logs
- datasets
- sensor recordings
- experiment results

---

# 14. Encoding

Text stored on disk is ultimately represented as bytes.

Encoding defines how bytes map to characters.

A common modern encoding is:

```text
UTF-8
```

Therefore, it is good practice to explicitly specify it:

```python
with path.open("r", encoding="utf-8") as file:
    content = file.read()
```

Similarly:

```python
with path.open("w", encoding="utf-8") as file:
    file.write("Hello")
```

---

# 15. Text vs Binary Files

Files can broadly be classified as text or binary.

### Text files

Examples:

```text
.txt
.json
.csv
.yaml
.py
.md
```

They represent human-readable text.

### Binary files

Examples:

```text
.jpg
.png
.mp4
.pth
.npz
.bin
```

They contain arbitrary bytes.

---

# 16. Binary File Operations

Use `"rb"` to read binary data:

```python
with open("image.png", "rb") as file:
    data = file.read()
```

Use `"wb"` to write binary data:

```python
with open("output.bin", "wb") as file:
    file.write(data)
```

`b` means:

> binary

---

# 17. Serialization

Serialization means converting an in-memory object into a representation that can be stored or transmitted.

For example:

```python
robot = {
    "name": "Atlas",
    "battery": 87
}
```

The Python object exists in memory.

We can serialize it:

```text
Python object
     ↓
serialization
     ↓
JSON
     ↓
file
```

Later:

```text
file
 ↓
JSON
 ↓
deserialization
 ↓
Python object
```

---

# 18. JSON

JSON stands for:

> JavaScript Object Notation

Despite its name, JSON is widely used across programming languages.

Example:

```json
{
    "name": "Atlas",
    "battery": 87,
    "speed": 1.5
}
```

Python provides the built-in `json` module.

```python
import json
```

---

# 19. JSON Serialization with `json.dump()`

Example:

```python
import json
from pathlib import Path

robot = {
    "name": "Atlas",
    "battery": 87,
    "speed": 1.5,
    "sensors": ["camera", "lidar", "imu"]
}

path = Path("robot.json")

with path.open("w", encoding="utf-8") as file:
    json.dump(robot, file, indent=4)
```

The Python dictionary has been serialized into JSON.

---

# 20. Why `indent`?

Without indentation, JSON may look like:

```json
{"name":"Atlas","battery":87,"speed":1.5}
```

With:

```python
indent=4
```

it becomes:

```json
{
    "name": "Atlas",
    "battery": 87,
    "speed": 1.5
}
```

This is much easier for humans to read.

For configuration files, human readability is valuable.

---

# 21. JSON Deserialization with `json.load()`

To read the JSON back:

```python
with path.open("r", encoding="utf-8") as file:
    robot = json.load(file)
```

Now `robot` is again a Python object.

For the previous example:

```python
print(type(robot))
```

would produce:

```text
<class 'dict'>
```

---

# 22. Serialization Cycle

The complete cycle is:

```text
              Serialization
Python object ───────────────→ JSON
      ▲                         │
      │                         │
      │                         ▼
      └────── Deserialization ─ File
```

More accurately:

```text
Python dict
    │
    │ json.dump()
    ▼
JSON file
    │
    │ json.load()
    ▼
Python dict
```

This is a fundamental pattern in application development.

---

# 23. Configuration-Driven Applications

Instead of hardcoding configuration:

```python
robot_name = "Atlas"
max_speed = 2.0
battery_limit = 20
```

we can store configuration externally:

```json
{
    "robot_name": "Atlas",
    "max_speed": 2.0,
    "battery_limit": 20
}
```

Then the application loads it.

Conceptually:

```text
Configuration file
        ↓
      Python
        ↓
     Application
```

This separates:

```text
Configuration
```

from:

```text
Program logic
```

This is an important software-engineering principle.

---

# 24. Configuration in Robotics

A robot application might have:

```text
config/
├── robot.json
├── sensors.json
└── controller.json
```

For example:

```json
{
    "name": "Atlas",
    "max_speed": 2.0,
    "wheel_radius": 0.15
}
```

Sensor configuration:

```json
{
    "camera": {
        "enabled": true,
        "fps": 30
    },
    "lidar": {
        "enabled": true,
        "range": 20
    }
}
```

The same software can potentially operate with different configurations.

---

# 25. CSV

CSV means:

> Comma-Separated Values

Example:

```csv
timestamp,temperature,battery
0,30.5,100
1,31.2,98
2,32.1,95
3,33.0,92
```

CSV is common for:

- sensor measurements
- experiment results
- datasets
- tabular logs

---

# 26. Reading CSV with Python

Python provides the built-in `csv` module.

```python
import csv

with open("sensors.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Each row is represented as a dictionary.

Example:

```python
{
    "timestamp": "0",
    "temperature": "30.5",
    "battery": "100"
}
```

Notice that CSV values are initially strings.

If numeric calculations are required:

```python
temperature = float(row["temperature"])
battery = int(row["battery"])
```

---

# 27. JSON vs CSV

Both are useful but serve different purposes.

| JSON | CSV |
|---|---|
| Structured/hierarchical data | Tabular data |
| Configuration | Measurements |
| Nested objects | Rows/columns |
| Lists/dictionaries | Tables |
| Human-readable | Human-readable |
| APIs/configuration | Datasets/logs |

Example JSON:

```json
{
    "robot": "Atlas",
    "sensors": {
        "camera": true,
        "lidar": true
    }
}
```

Example CSV:

```csv
timestamp,temperature,battery
0,30.5,100
1,31.2,98
```

---

# 28. `Path` + File + JSON

A common pattern in real projects:

```python
from pathlib import Path
import json


def load_robot_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


config_path = Path("config") / "robot.json"

config = load_robot_config(config_path)

print(config["name"])
```

This combines several concepts:

```text
Path
 ↓
File
 ↓
JSON
 ↓
Python dictionary
```

---

# 29. Exception Handling with Files

File operations can fail.

Possible errors include:

```text
FileNotFoundError
PermissionError
IsADirectoryError
OSError
json.JSONDecodeError
```

Example:

```python
from pathlib import Path

path = Path("robot.json")

if not path.exists():
    raise FileNotFoundError(path)
```

However, checking first is not always necessary.

Python often follows an EAFP style:

> Easier to Ask Forgiveness than Permission.

For example:

```python
try:
    with path.open("r", encoding="utf-8") as file:
        data = file.read()
except FileNotFoundError:
    ...
```

Choose the approach based on what your application needs.

---

# 30. Don't Silently Swallow File Errors

Avoid:

```python
try:
    ...
except Exception:
    pass
```

This hides problems.

If a configuration file cannot be loaded, silently continuing could result in a robot operating with incorrect defaults.

Prefer:

```python
try:
    ...
except FileNotFoundError:
    ...
```

or allow the exception to propagate when the caller should handle it.

---

# 31. `pickle`

Python provides another serialization mechanism:

```python
import pickle
```

Example:

```python
pickle.dump(obj, file)
```

and:

```python
obj = pickle.load(file)
```

`pickle` can serialize more Python-specific objects than JSON.

However:

> **Never unpickle untrusted data.**

Loading malicious pickle data can execute arbitrary Python code.

For configuration and interoperable data, prefer safer formats such as:

```text
JSON
CSV
```

when appropriate.

---

# 32. Python vs Java

Because Python is being learned alongside your Java background, the following mapping is useful.

| Python | Java |
|---|---|
| `pathlib.Path` | `java.nio.file.Path` |
| `Path.open()` | `Files.newBufferedReader()` / `Files.newBufferedWriter()` |
| `with` | try-with-resources |
| `dict` | `Map` |
| `json` | Jackson / Gson |
| `open()` | File/stream APIs |
| `csv` | CSV libraries / manual parsing |
| `pickle` | Roughly comparable to Java object serialization, but not equivalent |

---

# 33. Important Java → Python Difference

In Java, you might write:

```java
try (BufferedReader reader = ...) {
    ...
}
```

Python uses:

```python
with path.open(...) as file:
    ...
```

Both solve the same fundamental problem:

```text
Acquire resource
       ↓
Use resource
       ↓
Guarantee cleanup
```

This is one reason understanding Python's context managers is important.

---

# 34. Filesystem vs Python Object

A useful mental model:

```text
Python Process
│
├── Objects
│   ├── dict
│   ├── list
│   ├── class instances
│   └── variables
│
└── Filesystem
    ├── files
    └── directories
```

Python objects live in memory.

Files provide persistence.

Serialization provides the bridge:

```text
Python objects
      ↕
Serialization
      ↕
Persistent representation
```

---

# 35. Persistence

Without persistence:

```text
Program
   ↓
Data
   ↓
Program exits
   ↓
Data disappears
```

With persistence:

```text
Program
   ↓
Data
   ↓
Serialize
   ↓
File
   ↓
Program exits
   ↓
Program starts again
   ↓
Read file
   ↓
Deserialize
   ↓
Data restored
```

This is the fundamental reason files and serialization matter.

---

# 36. Experiment Data in Robotics

A robotics experiment may produce:

```text
experiments/
└── run_001/
    ├── config.json
    ├── sensors.csv
    └── summary.json
```

For example:

### `config.json`

```json
{
    "robot": "Atlas",
    "controller": "PID",
    "duration": 30
}
```

### `sensors.csv`

```csv
timestamp,temperature,battery
0,30.5,100
1,31.2,98
2,32.1,95
```

### `summary.json`

```json
{
    "average_temperature": 31.26,
    "minimum_battery": 95
}
```

This is already very close to how real research experiments are organized.

---

# 37. Recommended Project Pattern

For small Python projects:

```text
project/
│
├── config/
│   └── config.json
│
├── data/
│   ├── input.csv
│   └── output.csv
│
├── logs/
│   └── application.log
│
├── src/
│   └── main.py
│
└── README.md
```

For robotics/ML experiments:

```text
project/
│
├── config/
│
├── data/
│
├── experiments/
│   ├── run_001/
│   └── run_002/
│
├── models/
│
├── logs/
│
├── src/
│
└── README.md
```

The exact structure will vary by project, but separating configuration, data, code, logs, and experiment outputs is often useful.

---

# 38. Code Reading Checklist

When you encounter filesystem code in an unfamiliar Python project, ask:

### Paths

- Is this path absolute or relative?
- What is the current working directory?
- Is `pathlib` being used?
- Where does this path actually point?

### Files

- Is the file being read or written?
- Which mode is being used?
- Could `"w"` accidentally overwrite data?
- Is `"a"` appropriate?
- Is encoding specified?

### Resources

- Is the file opened using `with`?
- Could the file remain open?
- What happens if opening fails?

### Structured data

- Is the file JSON?
- CSV?
- YAML?
- Binary?
- Pickle?

### Errors

- What happens if the file doesn't exist?
- What happens if JSON is invalid?
- Are exceptions swallowed?
- Is the error handled at the correct layer?

### Architecture

- Is configuration separated from application logic?
- Are paths hardcoded unnecessarily?
- Is experiment data organized consistently?

---

# 39. Common Mistakes

## Mistake 1 — Using string concatenation for paths

Avoid:

```python
path = "data/" + filename
```

Prefer:

```python
path = Path("data") / filename
```

---

## Mistake 2 — Forgetting that `"w"` overwrites

```python
open("log.txt", "w")
```

can destroy existing content.

---

## Mistake 3 — Not using a context manager

Avoid:

```python
file = open("data.txt")
data = file.read()
file.close()
```

Prefer:

```python
with open("data.txt") as file:
    data = file.read()
```

---

## Mistake 4 — Treating JSON as a Python dictionary

This:

```text
JSON file
```

is not the same thing as:

```python
dict
```

You need serialization/deserialization:

```python
json.dump()
json.load()
```

---

## Mistake 5 — Forgetting type conversion with CSV

CSV values are typically strings.

```python
row["temperature"]
```

may produce:

```python
"32.5"
```

rather than:

```python
32.5
```

Convert when necessary:

```python
float(row["temperature"])
```

---

## Mistake 6 — Trusting Pickle files

Never load pickle data from an untrusted source.

---

# 40. Chapter Summary

The most important concepts from this chapter are:

```text
Filesystem
    ↓
Paths
    ↓
pathlib.Path
    ↓
Files
    ↓
Reading / Writing
    ↓
Context Managers
    ↓
Encoding
    ↓
Structured Data
    ↓
JSON / CSV
    ↓
Serialization
    ↓
Persistence
```

### Core APIs

```python
from pathlib import Path
```

```python
Path.cwd()
Path("data")
Path("data") / "robot.json"
path.exists()
path.is_file()
path.is_dir()
path.name
path.stem
path.suffix
path.parent
path.mkdir()
```

File operations:

```python
with path.open("r", encoding="utf-8") as file:
    ...
```

```python
with path.open("w", encoding="utf-8") as file:
    ...
```

JSON:

```python
import json

json.dump(...)
json.load(...)
```

CSV:

```python
import csv

csv.reader(...)
csv.DictReader(...)
csv.writer(...)
csv.DictWriter(...)
```

---

# 41. Key Mental Models

### Files are persistent storage

```text
RAM
 ↓
temporary program state

Filesystem
 ↓
persistent state
```

### `Path` represents a location

```text
Path
 ↓
filesystem location
```

### Context managers manage resources

```text
with
 ↓
acquire
 ↓
use
 ↓
cleanup
```

### Serialization bridges memory and storage

```text
Python object
      ↓
serialize
      ↓
File
      ↓
deserialize
      ↓
Python object
```

### Configuration separates data from logic

```text
Configuration
      ↓
Application
```

rather than:

```text
Application
 └── everything hardcoded
```

---

# 42. Connection to Future Chapters

Chapter 9 provides foundations for many later topics.

### Testing

Tests may need:

```text
temporary files
temporary directories
test data
```

### Logging

Applications write:

```text
logs/
```

### NumPy

Scientific applications read/write:

```text
CSV
NPY
NPZ
```

### Pandas

Large tabular datasets:

```text
CSV
JSON
Parquet
```

### PyTorch

Models and tensors may be persisted using:

```text
.pt
.pth
```

### Robotics

Robot applications use:

```text
configuration
calibration
sensor logs
maps
experiment data
```

### ROS 2

Later you'll encounter:

```text
packages
parameters
configuration
URDF
launch files
bags
logs
```

Understanding paths and files now will make those concepts much easier.

