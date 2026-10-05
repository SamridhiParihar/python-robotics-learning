# ============================================================
# EXERCISE 1 — ROBOT CLASS
# ============================================================
#
# Create a class called Robot.
#
# The Robot should have:
#   - name
#   - model
#   - battery
#
# Initialize these using __init__.
#
# Create two different Robot objects.
#
# Print their information.
#
# Then:
#   1. Change robot1's battery.
#   2. Print robot1's battery.
#   3. Print robot2's battery.
#
# Verify that changing robot1 does not affect robot2.
#
# Do not use a dictionary to represent the robot.
# Use a proper class.

class Robot:

    def __init__(self, name: str, model: str, battery: float):
        self.name = name
        self.model = model
        self.battery = battery
        self.is_stopped = False

    def __repr__(self) -> str:
        return f"Robot(name='{self.name}', model='{self.model}', battery={self.battery}%)"

    def start(self) -> None :
        if self.is_stopped : 
            print (f"can't move {self.name} as it has been stopped")
            return 
        print(f"{self.name} starts now ! ")

    def move(self) -> None : 
        if self.is_stopped : 
            print (f"can't move {self.name} as it has been stopped")
            return 
        print (f"{self.name} starts moving")

    def charge(self) -> None:
        for self.battery in range(101):
            print(f"current battery : {self.battery}")
            self.battery+=1
        



robot1: Robot = Robot(
    name = "chitti",
    model = "1.0",
    battery= 88.4
)

robot2: Robot = Robot(
    name = "chitti",
    model = "2.0",
    battery= 88.7
)

robot1.model = "1.1"

print(robot1)
print(robot2)

# ============================================================
# EXERCISE 2 — ROBOT METHODS
# ============================================================
#
# Extend your Robot class.
#
# Add methods:
#
#   start()
#   stop()
#   move()
#   charge()
#
# The robot should maintain enough state to know whether
# it is currently running.
#
# Design reasonable behavior for each method.
#
# Requirements:
#
#   - A stopped robot should not move.
#   - Moving should consume some battery.
#   - Charging should increase the battery.
#   - Battery should never exceed 100.
#   - Battery should never go below 0.
#
# Create a robot and demonstrate a realistic sequence:
#
#   start
#   move
#   move
#   charge
#   stop
#
# Print useful messages showing what is happening.

class Robot:

    def __init__(self, name: str, model: str, battery: float):
        self.name = name
        self.model = model
        self.battery = battery
        self.is_running = False  

    def __repr__(self) -> str:
        return f"Robot(name='{self.name}', model='{self.model}', battery={self.battery:.1f}%)"

    def start(self) -> None:
        if self.is_running:
            print(f"[{self.name}] Already running.")
            return
        if self.battery <= 0:
            print(f"[{self.name}] Cannot start. Battery is dead (0%). Please charge.")
            return
        
        self.is_running = True
        print(f"[{self.name}] System starting up... Online! (Battery: {self.battery:.1f}%)")

    def stop(self) -> None:
        if not self.is_running:
            print(f"[{self.name}] Already stopped.")
            return
        
        self.is_running = False
        print(f"[{self.name}] System shutting down... Offline.")

    def move(self) -> None:
        if not self.is_running:
            print(f"Action Denied: Cannot move {self.name} because it is currently stopped.")
            return
        
        # Base consumption logic
        consumption = 15.0
        if self.battery - consumption < 0:
            print(f"Warning: [{self.name}] Not enough battery to complete the full movement!")
            self.battery = 0.0
            self.stop()  # Auto shutoff if battery hits absolute zero
        else:
            self.battery -= consumption
            print(f"[{self.name}] moves forward. Consumed {consumption}% battery. (Remaining: {self.battery:.1f}%)")

    def charge(self) -> None:
        if self.battery >= 100:
            print(f"[{self.name}] is already fully charged at 100%.")
            return
        
        print(f"Plugging in [{self.name}]... Charging from {self.battery:.1f}% to 100%.")
        self.battery = 100.0  
        print(f"[{self.name}] Charging complete! Battery: {self.battery:.1f}%")



# Create a robot with 40% battery to see depletion safely
my_robot = Robot(name="Chitti v2", model="Speedster", battery=40.0)
print(f"Initial State: {my_robot}\n")

# 1. Start
my_robot.start()

# 2. Move
my_robot.move()

# 3. Move
my_robot.move()

# 4. Charge
my_robot.charge()

# 5. Stop
my_robot.stop()




# ============================================================
# EXERCISE 3 — ROBOT STATE
# ============================================================
#
# Create a Robot class representing a simple 2D mobile robot.
#
# The robot should maintain:
#
#   - name
#   - battery
#   - x position
#   - y position
#   - speed
#   - running state
#
# Implement:
#
#   start()
#   stop()
#   move(dx, dy)
#   status()
#
# Rules:
#
#   - The robot cannot move if it is stopped.
#   - Moving changes x and y.
#   - Moving consumes battery.
#   - status() should display the current robot state.
#
# Create a robot and perform several movements.
#
# Think carefully about:
#
#   What belongs to the object's state?
#   What should be handled by methods?

class Robot: 

    def __init__(self, name: str, battery: float, x_position: int, y_position: int, speed: float = 1.0):
        self.name = name
        self.battery = battery
        self.x_position = x_position
        self.y_position = y_position
        self.speed = speed         
        self.is_running = False

    def __repr__(self) -> str:
        return f"Robot(name='{self.name}', position=({self.x_position}, {self.y_position}), battery={self.battery:.1f}%)"
    
    def start(self) -> None:
        if self.is_running:
            print(f"[{self.name}] Already running.")
            return
        if self.battery <= 0:
            print(f"[{self.name}] Cannot start. Battery is dead (0%). Please charge.")
            return
        self.is_running = True
        print(f"[{self.name}] System starting up... Online! (Battery: {self.battery:.1f}%)")

    def stop(self) -> None:
        if not self.is_running:
            print(f"[{self.name}] Already stopped.")
            return
            
        self.is_running = False
        print(f"[{self.name}] System shutting down... Offline.")

    def charge(self) -> None:
        if self.battery >= 100:
            print(f"[{self.name}] is already fully charged at 100%.")
            return
        
        print(f"Plugging in [{self.name}]... Charging from {self.battery:.1f}% to 100%.")
        self.battery = 100.0  
        print(f"[{self.name}] Charging complete! Battery: {self.battery:.1f}%")

    def move(self, dx: int, dy: int) -> None: 
        if not self.is_running:
            print(f"Action Denied: Cannot move {self.name} because it is currently stopped.")
            return
        
        # Pro Tip: A realistic touch would be using speed to calculate battery consumption!
        # For now, let's keep your base cost logic
        consumption = 15.0
        
        if self.battery - consumption < 0:
            print(f"Warning: [{self.name}] Not enough battery to complete the movement!")
            self.battery = 0.0
            self.stop()  
        else:
            self.battery -= consumption
            self.x_position += dx * self.speed
            self.y_position += dy * self.speed
            print(f"🏃 [{self.name}] shifted coordinates by ({dx}, {dy}). (Remaining Battery: {self.battery:.1f}%)")

    # 3. Enhanced: Status now completely displays the full state as required
    def status(self) -> None:
        print("\n" + "="*30)
        print(f"SYSTEM STATUS: {self.name}")
        print(f"  - Position : ({self.x_position}, {self.y_position})")
        print(f"  - Battery  : {self.battery:.1f}%")
        print(f"  - Speed    : {self.speed} units/step")
        print(f"  - State    : {'Running' if self.is_running else 'Stopped'}")
        print("="*30 + "\n")








        
        



        