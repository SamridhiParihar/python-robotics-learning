# Python for Robotics Learning

A hands-on, chapter-by-chapter path from Python fundamentals to building robotics applications with Python. The course connects language concepts to practical engineering work, including scientific computing, sensors, and ROS 2.

> **Progress:** Chapters 1–9 are complete. **Chapter 10 — Iterators, Generators & `yield` — is next.**

## How to use this repository

1. Start with a chapter's README and work through its concepts in order.
2. Write the examples yourself, then solve the small exercises before looking back.
3. Read the repository's example code and explain what it does; review it for edge cases and clarity.
4. Use the project's Pixi environment when running Python examples.
5. Keep notes on questions and revisit earlier chapters when a later topic builds on them.

The aim is to understand why the code works, not just memorize syntax. Practice writing, reading, and reviewing code throughout the course.

## Getting started

This project uses [Pixi](https://pixi.sh/) to manage its Python 3.12 environment. From the repository root:

```bash
pixi install
pixi run python --version
```

The first chapter explains environments, dependencies, and the repository's Pixi workflow in more detail.

## Chapter guide

### Completed

| Chapter | Subject | Guide |
|---:|---|---|
| 01 | Python environment and Pixi | [Read chapter 1](01-python-environment/README.md) |
| 02 | Python fundamentals | [Read chapter 2](02-python-fundamentals/README.md) |
| 03 | Data types and strings | [Read chapter 3](03-data-types-and-strings/README.md) |
| 04 | Collections and data structures | [Read chapter 4](04-python-collections-and-data-structures/README.md) |
| 05 | Functions | [Read chapter 5](05-python-functions/README.md) |
| 06 | Exception handling | [Read chapter 6](06-exception-handling/README.md) |
| 07 | Modules, packages, and imports | [Read chapter 7](07-modules-packages-imports/README.md) |
| 08 | Object-oriented programming | [Read chapter 8](08-oops-in-python/README.md) |
| 09 | Files, paths, and serialization | [Read chapter 9](09-files-path-and-serialization/README.md) |

## 30-chapter roadmap

The roadmap below shows the intended progression. Only the first nine chapter guides exist today; Chapter 10 is the next planned chapter.

### Phase 1 — Python foundations

| # | Chapter | Status |
|---:|---|---|
| 01 | Python Environment and Pixi | Complete |
| 02 | Python Fundamentals | Complete |
| 03 | Data Types and Strings | Complete |
| 04 | Collections and Data Structures | Complete |
| 05 | Functions | Complete |
| 06 | Exception Handling | Complete |
| 07 | Modules, Packages, and Imports | Complete |
| 08 | Object-Oriented Programming in Python | Complete |
| 09 | Files, Paths, and Serialization | Complete |

### Phase 2 — Deeper Python and development practice

| # | Chapter | Status |
|---:|---|---|
| 10 | Iterators, Generators & `yield` | **Next / upcoming** |
| 11 | Comprehensions and Functional Patterns | Planned |
| 12 | Decorators | Planned |
| 13 | Context Managers and Resource Management | Planned |
| 14 | Type Hints, Protocols, and Static Analysis | Planned |
| 15 | Testing Python Code | Planned |
| 16 | Debugging, Logging, and Command-Line Tools | Planned |
| 17 | Concurrency and Asynchronous Python | Planned |

### Phase 3 — Scientific Python and perception

| # | Chapter | Status |
|---:|---|---|
| 18 | NumPy for Scientific Computing | Planned |
| 19 | Data Visualization with Matplotlib | Planned |
| 20 | Data Analysis with Pandas | Planned |
| 21 | SciPy: Linear Algebra, Optimization, and Signal Processing | Planned |
| 22 | Computer Vision with OpenCV | Planned |

### Phase 4 — Robotics systems and ROS 2

| # | Chapter | Status |
|---:|---|---|
| 23 | Robotics Math, Units, and Coordinate Frames | Planned |
| 24 | Kinematics, Dynamics, and Motion Models | Planned |
| 25 | Sensors and Hardware Interfaces | Planned |
| 26 | ROS 2 with `rclpy`: Nodes, Topics, Services, and Actions | Planned |
| 27 | ROS 2 Parameters, Launch, QoS, and Architecture | Planned |
| 28 | Simulation, Bag Data, and Integration Testing | Planned |

### Phase 5 — Control and application

| # | Chapter | Status |
|---:|---|---|
| 29 | Robot Control and Planning | Planned |
| 30 | Capstone: An End-to-End Robotics Application | Planned |

## Repository map

```text
python-robotics-learning/
├── 01-python-environment/
├── 02-python-fundamentals/
├── 03-data-types-and-strings/
├── 04-python-collections-and-data-structures/
├── 05-python-functions/
├── 06-exception-handling/
├── 07-modules-packages-imports/
├── 08-oops-in-python/
├── 09-files-path-and-serialization/
├── pixi.toml
└── pixi.lock
```

Each completed chapter folder contains its own README guide and, where applicable, example code. This root page is the index for the chapter guides currently in the repository.
