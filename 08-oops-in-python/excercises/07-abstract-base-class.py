# ============================================================
# EXERCISE 16 — ABSTRACT BASE CLASS
# ============================================================
#
# Use:
#
#   abc.ABC
#   abc.abstractmethod
#
# Create an abstract class:
#
#   Controller
#
# It should define:
#
#   compute_action(state)
#
# as an abstract method.
#
# Then create:
#
#   PIDController
#   RLController
#
# Both should implement compute_action().
#
# Demonstrate that:
#
#   PIDController()
#
# and:
#
#   RLController()
#
# can be instantiated.
#
# Also try creating:
#
#   Controller()
#
# and observe what happens.
#
# Understand why Python prevents direct instantiation of the
# abstract class.


from abc import ABC , abstractmethod

class Controller(ABC):

    @abstractmethod
    def compute_action(self, state: str) -> None:
        pass

class PIDController(Controller):

    def compute_action(self, state: str) -> None:
        print(f"[PID] Calculating smooth error correction output for state '{state}'")

class RLController(Controller):

    def compute_action(self, state:str ) -> None:
        print(f"[RL Model] Inferring optimal learned policy action for state '{state}'")

pidC = PIDController()
rlC = RLController()
state = "Obstacle detected 2 meters ahead"
pidC.compute_action(state)
rlC.compute_action(state)

# c = Controller() : TypeError: Can't instantiate abstract class Controller without an implementation for abstract method 'compute_action'



# ============================================================
# EXERCISE 17 — DUCK TYPING
# ============================================================
#
# Create:
#
#   PIDController
#   RLController
#   FakeController
#
# Do NOT make them inherit from a common base class.
#
# Each class should implement:
#
#   compute_action(state)
#
# Write a function:
#
#   run_controller(controller, state)
#
# The function should call:
#
#   controller.compute_action(state)
#
# It should not care which concrete class was provided.
#
# Demonstrate that run_controller() works with all three
# controller implementations.
#
# Think about the difference between this approach and
# Exercise 16.




class PIDController:
    def compute_action(self, state: str) -> str:
        return f"[PID] Executing smooth mathematical logic for: '{state}'"


class RLController:
    def compute_action(self, state: str) -> str:
        return f"[RL Model] Executing neural-network inference for: '{state}'"


class FakeController:
    def compute_action(self, state: str) -> str:
        return f"[Mock Fake] Returning dummy payload data for testing: '{state}'"


# funcion

def run_controller(controller, state: str) -> None:
    """
    This function accepts any object whatsoever. It doesn't check types.
    It simply trusts that the object 'quacks' correctly by having a compute_action method.
    """
    # Execute the method dynamically
    action_result = controller.compute_action(state)
    print(f"  └─ Action Result: {action_result}")




test_state = "Battery critical (5%)"

print("--- Testing Pure Duck Typing ---")

print("\n1. Injecting PID Controller:")
run_controller(PIDController(), test_state)

print("\n2. Injecting RL Controller:")
run_controller(RLController(), test_state)

print("\n3. Injecting Fake Controller:")
run_controller(FakeController(), test_state)
