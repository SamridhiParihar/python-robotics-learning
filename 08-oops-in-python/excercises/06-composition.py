# ============================================================
# EXERCISE 14 — ROBOT HAS SENSORS
# ============================================================
#
# Create these classes:
#
#   Camera
#   Lidar
#   IMU
#   Robot
#
# Each sensor class should have at least one meaningful
# method.
#
# For example:
#
#   Camera.capture()
#   Lidar.scan()
#   IMU.read()
#
# Robot should contain:
#
#   - a Camera
#   - a Lidar
#   - an IMU
#
# Robot should provide a method:
#
#   read_sensors()
#
# that obtains data from all three sensors.
#
# IMPORTANT:
#
# Do NOT make Camera, Lidar, and IMU inherit from Robot.
#
# Think about the relationship:
#
# Robot HAS-A Camera
# Robot HAS-A Lidar
# Robot HAS-A IMU
#
# rather than:
#
# Camera IS-A Robot


# ============================================================
# SENSOR COMPONENT CLASSES
# ============================================================

class Camera:
    def __init__(self, resolution: str = "1080p") -> None:
        self.resolution = resolution

    def capture(self) -> str:
        """Captures a visual matrix frame."""
        return f"[Camera Frame ({self.resolution}): Image processed - Object detected ahead]"


class Lidar:
    def __init__(self, beam_count: int = 360) -> None:
        self.beam_count = beam_count

    def scan(self) -> str:
        """Generates a spatial depth point cloud map."""
        return f"[Lidar Point Cloud ({self.beam_count} beams): Obstacle at 1.4 meters]"


class IMU:
    def __init__(self, frequency_hz: int = 100) -> None:
        self.frequency_hz = frequency_hz

    def read(self) -> str:
        """Reads linear acceleration and angular velocity metrics."""
        return f"[IMU Orientation ({self.frequency_hz}Hz): Pitch: 0.1°, Roll: -0.2°, Yaw: 45.0°]"




class Robot:
    def __init__(self, name: str) -> None:
        self.name = name
        
        # Establishing the "HAS-A" relationship by composing components inside __init__
        self.camera = Camera(resolution="4K")
        self.lidar = Lidar(beam_count=720)
        self.imu = IMU(frequency_hz=200)

    def read_sensors(self) -> None:
        """Orchestrates and polls metrics across all aggregate component units."""
        print(f"\n⚡ Polling telemetry data for system: {self.name} ...")
        print(f"  └─ {self.camera.capture()}")
        print(f"  └─ {self.lidar.scan()}")
        print(f"  └─ {self.imu.read()}")


# Instantiating a clean Robot instance
my_robot = Robot("Curiosity-Rover")

# Poll the internal composite sensor array
my_robot.read_sensors()


# ============================================================
# EXERCISE 15 — DEPENDENCY INJECTION
# ============================================================
#
# Create:
#
#   Controller
#   PIDController
#   RLController
#   Robot
#
# Robot should receive a controller through its constructor.
#
# Example concept:
#
#   controller = PIDController()
#   robot = Robot(controller)
#
# Do NOT make Robot directly create:
#
#   PIDController()
#
# inside its constructor.
#
# Robot should simply use the controller it receives.
#
# Give the Controller classes a method:
#
#   compute_action(state)
#
# Robot should have a method:
#
#   step(state)
#
# which asks the controller for an action.
#
# Demonstrate that you can create:
#
#   Robot(PIDController())
#
# and:
#
#   Robot(RLController())
#
# without changing the Robot class.
#
# Think carefully about why this design is useful for:
#
#   - testing
#   - simulation
#   - real hardware
#   - experimenting with different algorithms

from abc import ABC, abstractmethod

class Controller(ABC):
    
    @abstractmethod
    def compute_action(self, state: str) -> str:
        pass


class PIDController(Controller):
    def compute_action(self, state: str) -> str:
        return f"[PID] Calculating smooth error correction output for state '{state}'"

class RLController(Controller):
    def compute_action(self, state: str) -> str:
        return f"[RL Model] Inferring optimal learned policy action for state '{state}'"


class Robot:
    def __init__(self, name: str, controller: Controller) -> None:
        self.name = name
        self.controller = controller 

    def step(self, state: str) -> None:
        """Asks the injected controller to evaluate the state and fetch an action."""
        print(f"\n[{self.name}] Scanning current environment...")
        action = self.controller.compute_action(state)
        print(f"  └─ Action Taken: {action}")



current_state = "Obstacle detected 2 meters ahead"

pid_robot = Robot(name="FactoryRover", controller=PIDController())
pid_robot.step(current_state)

rl_robot = Robot(name="NeuroBot", controller=RLController())
rl_robot.step(current_state)
