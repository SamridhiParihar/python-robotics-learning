# ============================================================
# EXERCISE 11 — ROBOT INHERITANCE
# ============================================================
#
# Create a base class:
#
#   Robot
#
# with:
#
#   name
#   move()
#
# Then create:
#
#   WheeledRobot
#   FlyingRobot
#
# that inherit from Robot.
#
# Override move() in each subclass.
#
# Example behavior:
#
#   WheeledRobot.move() -> "Driving on wheels"
#   FlyingRobot.move()  -> "Flying through the air"
#
# Create objects of both types.
#
# Call move() on both.
#
# Observe polymorphic behavior.

class Robot:

    def __init__(self, name: str) -> None:
        self.name = name

    def move(self) -> None:
        pass

class WheeledRobot(Robot):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def move(self) -> None:
        print("Driving on wheels")

class FlyingRobot(Robot):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def move(self) -> None:
        print("Flying through the air")

wheel_robot = WheeledRobot("abc")
fly_robot = FlyingRobot("abc2")
wheel_robot.move()
fly_robot.move()


# ============================================================
# EXERCISE 12 — SUPER()
# ============================================================
#
# Create:
#
#   Robot
#
# with:
#
#   name
#   battery
#
# Then create:
#
#   WheeledRobot
#
# which additionally has:
#
#   wheel_count
#
# Implement __init__ in both classes.
#
# Use super() in WheeledRobot.__init__() to initialize the
# attributes belonging to Robot.
#
# Then initialize wheel_count in WheeledRobot.
#
# Create an object and print all attributes.
#
# IMPORTANT:
#
# Do not duplicate the initialization of name and battery
# inside WheeledRobot.

class Robot:

    def __init__(self, name: str , battery: float) -> None:
        self.name = name
        self.battery = battery

class WheeledRobot(Robot):

    def __init__(self, name: str, battery: float, wheel_count: int) -> None:
        super().__init__(name, battery)
        self.wheel_count = wheel_count

robot = WheeledRobot("abc",55.5,4)


# ============================================================
# EXERCISE 13 — METHOD OVERRIDING
# ============================================================
#
# Create:
#
#   Robot
#   WheeledRobot
#   FlyingRobot
#   LeggedRobot
#
# Robot should define:
#
#   move()
#
# Each subclass should override move() with behavior
# appropriate for that robot type.
#
# Create a list containing one object of each type.
#
# Loop through the list and call:
#
#   robot.move()
#
# Do NOT check the type using:
#
#   isinstance(...)
#
# inside the loop.
#
# The goal is to practice polymorphism.


class Robot:

    def __init__(self, name: str) -> None:
        self.name = name

    def move(self) -> str:
        pass

class WheeledRobot(Robot):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def move(self) -> str:
        return "Driving on wheels" 

class FlyingRobot(Robot):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def move(self) -> str:
        return "Flying through the air"

class LeggedRobot(Robot):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def move(self) -> str:
        return "Walking"


robots: list[Robot] = [WheeledRobot("wheelR"),FlyingRobot("flyingR") , LeggedRobot("leggedR")]

for robot in robots:
    print(f"{robot.name}: {robot.move()}")