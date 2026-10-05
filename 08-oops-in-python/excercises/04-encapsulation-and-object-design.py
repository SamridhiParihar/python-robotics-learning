# ============================================================
# EXERCISE 10 — MOTOR CONTROLLER
# ============================================================
#
# Create a Motor class.
#
# It should maintain:
#
#   - motor_id
#   - speed
#   - running state
#
# Design the class so that speed is controlled through a
# property.
#
# Speed must remain between:
#
#   -100 and 100
#
# where:
#
#   100  = full forward
#   0    = stopped
#   -100 = full reverse
#
# Add:
#
#   start()
#   stop()
#
# The motor should not be allowed to operate with an invalid
# speed.
#
# Demonstrate valid and invalid assignments.
#
# Think about which attributes should be considered part of
# the public API and which should be internal implementation
# details.


class Motor:

    def __init__(self, motor_id: int , speed: float) -> None:
        self.__motor_id = motor_id
        self.speed = speed
        self.is_running = False

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, val) -> None:
        if val<-100 or val>100:
            raise ValueError("speed should be in the range of -100 to 100")
        self._speed = val

    def start(self) -> None:
        if self.is_running:
            print("Already running.")
            return
        self.is_running = True
        print("Started!")

    def stop(self) -> None:
        if not self.is_running:
            print("Already stopped.")
            return
        self.is_running = False
        print("Stopped!")

    