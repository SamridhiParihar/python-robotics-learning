# ============================================================
# EXERCISE 7 — STATIC METHOD
# ============================================================
#
# Create a Robot class.
#
# Add a static method:
#
#   is_valid_battery(value)
#
# It should return True if the value is between 0 and 100.
#
# Otherwise return False.
#
# Example:
#
#   Robot.is_valid_battery(50)   -> True
#   Robot.is_valid_battery(120)  -> False
#   Robot.is_valid_battery(-10)  -> False
#
# The method should not depend on any particular Robot object.
#
# Therefore, do not use self or cls.

class Robot: 

    @staticmethod
    def is_valid_battery(value: float) -> bool:
        if value>=0 and value<=100:
            return True
        return False

print(Robot.is_valid_battery(50))
print(Robot.is_valid_battery(150))
print(Robot.is_valid_battery(-50))


# ============================================================
# EXERCISE 8 — BATTERY PROPERTY
# ============================================================
#
# Create a Robot class with a battery attribute.
#
# Use a property so that battery values can only be between
# 0 and 100.
#
# Example:
#
#   robot.battery = 80
#   print(robot.battery)
#
# should work.
#
# But:
#
#   robot.battery = 150
#
# should raise a ValueError.
#
# Likewise:
#
#   robot.battery = -10
#
# should raise a ValueError.
#
# Internally, use an appropriate private/internal attribute.
#
# Do NOT create explicit Java-style:
#
#   get_battery()
#   set_battery()
#
# Use Python's @property mechanism.


class Robot:

    def __init__(self, battery: float) -> None:
        self.battery = battery

    @property
    def battery(self) -> float:
        return self._battery

    @battery.setter
    def battery(self , val: float) -> None:
        if val>100 or val<0:
            raise ValueError("Value of battery should be between 0 to 100")
        self._battery = val

    robot1 = Robot(45.9)
    robot1.battery = 55


# ============================================================
# EXERCISE 9 — TEMPERATURE SENSOR
# ============================================================
#
# Create a TemperatureSensor class.
#
# It should maintain:
#
#   - sensor name
#   - current temperature
#
# Create a property called temperature.
#
# The temperature should be allowed to be between:
#
#   -50°C and 150°C
#
# If someone tries to assign a value outside this range,
# raise ValueError.
#
# Add:
#
#   read()
#
# which returns the current temperature.
#
# Add:
#
#   status()
#
# which prints useful information about the sensor.
#
# Think about why properties are useful for hardware state.


class TemperatureSensor:

    def __init__(self, name: str, temp: float) -> None:
        self.name = name
        self.temp = temp

    @property
    def temp(self) -> float:
        return self._temp

    @temp.setter
    def temp(self , val: float) -> None:
        if val<-50 or val>150:
            raise ValueError("Keep the temp range between -50°C and 150°C")

        self._temp = val

    def read(self) -> float:
        return self.temp

    def status(self) -> None:
        print(f"temp: {self.temp} , name: {self.name}")

    

