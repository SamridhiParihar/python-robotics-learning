from typing import Self
# ============================================================
# EXERCISE 4 — CLASS ATTRIBUTE
# ============================================================
#
# Create a Robot class with a class attribute:
#
#   category = "Mobile Robot"
#
# Create three Robot objects.
#
# Access category through all three objects.
#
# Then change the class-level category.
#
# Observe what happens when you access category through
# the different objects.
#
# Finally, assign a category directly to ONE robot instance.
#
# Observe the difference between:
#
#   Robot.category
#
# and:
#
#   robot.category
#
# Explain in comments what you observe.

class Robot :
    category: str = "Mobile Robot"
    def __init__(self):
        pass

robot1 = Robot()
robot2 = Robot()
robot3 = Robot()

print("Before changing")
print(f"by 1: {robot1.category}, by 2: {robot2.category} by 3: {robot3.category}")

Robot.category = "Mobile Robot 2.0"
print("After changing")
print(f"by 1: {robot1.category}, by 2: {robot2.category} by 3: {robot3.category}")

robot1.category = "Mobile Robot 3.0"
print("After changing with instance ")
print(f"by 1: {robot1.category}, by 2: {robot2.category} by 3: {robot3.category}")

# with instance variable it change only for that instance and doesn't change for others but class itself i.e, Robot variable it changes for
# all the instance as it is class property

print(robot1.__dict__)
print(Robot.__dict__)


# ============================================================
# EXERCISE 5 — ROBOT COUNTER
# ============================================================
#
# Create a Robot class that keeps track of how many Robot
# objects have been created.
#
# Example:
#
#   r1 = Robot(...)
#   r2 = Robot(...)
#   r3 = Robot(...)
#
# The class should know that three robots exist.
#
# Implement a class method:
#
#   get_robot_count()
#
# which returns the number of robots created.
#
# Demonstrate that:
#
#   Robot.get_robot_count()
#
# returns the expected value.
#
# IMPORTANT:
#
# Use a class attribute for the counter.
#
# Do not use a global variable.


class Robot:

    total_robot: int = 0

    def __init__(self) -> None:
        Robot.total_robot+=1

    @classmethod
    def get_robot_count(cls) -> int:
        return cls.total_robot

print(Robot.total_robot)
robot1 = Robot()
robot2 = Robot()
print(Robot.get_robot_count())


# ============================================================
# EXERCISE 6 — ALTERNATIVE CONSTRUCTOR
# ============================================================
#
# Create a Robot class with:
#
#   name
#   battery
#
# Normal construction should work like:
#
#   robot = Robot("Atlas", 90)
#
# Now add a class method:
#
#   from_string(...)
#
# that can create a Robot from a string such as:
#
#   "Atlas,90"
#
# Example:
#
#   robot = Robot.from_string("Atlas,90")
#
# The resulting object should have:
#
#   name = "Atlas"
#   battery = 90
#
# Think about why this is better implemented as a
# class method rather than an instance method.

class Robot:

    def __init__(self, name: str, battery: float) -> None:
        self.name = name
        self.battery = battery

    def __repr__(self) -> str:
        return f"Robot(name='{self.name}', battery={self.battery}%)"

    @classmethod
    def from_string(cls, val: str) -> Self:
        name, battery = val.split(",")
        return cls(name, battery)


# 1. Normal Construction
robot1 = Robot("Atlas", 90.0)
print(f"Normal init   : {robot1}")

# 2. Alternative String Construction
robot2 = Robot.from_string("Atlas,90")
print(f"Alternative init: {robot2}")

