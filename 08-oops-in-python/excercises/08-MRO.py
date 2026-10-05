# ============================================================
# EXERCISE 18 — METHOD RESOLUTION ORDER
# ============================================================
#
# Create:
#
#   class A
#   class B(A)
#   class C(A)
#   class D(B, C)
#
# Give A, B, and C a method:
#
#   show()
#
# Each implementation should print its own class name.
#
# Create:
#
#   d = D()
#
# Call:
#
#   d.show()
#
# Then print:
#
#   D.__mro__
#
# or use:
#
#   D.mro()
#
# Study the order Python uses to resolve the method.
#
# Add comments explaining the resulting MRO.


# ============================================================
# 1. CLASS DEFINITIONS (The Diamond Hierarchy)
# ============================================================

class A:
    def show(self) -> None:
        print("show() executed from Class A")


class B(A):
    def show(self) -> None:
        print("show() executed from Class B")


class C(A):
    def show(self) -> None:
        print("show() executed from Class C")


class D(B, C):
    """
    Class D uses multiple inheritance to inherit from both B and C.
    This creates the classic 'Diamond' inheritance tree structure.
    """
    pass


# ============================================================
# 2. VERIFICATION AND RESOLUTION LOOKUP
# ============================================================

print("--- Testing Method Resolution Order ---")

d = D()

print("\nCalling d.show():")
d.show()  # Triggering the lookup chain

print("\nInspecting the precise MRO chain layout:")
# Printing the MRO list using the built-in .mro() method
for index, cls in enumerate(D.mro(), start=1):
    print(f"  Step {index}: {cls}")


# =====================================================================
#  EXPLANATION OF THE RESULTING MRO (THE DIAMOND PROBLEM)
# =====================================================================
# The output sequence you see from D.mro() is:
# [ D -> B -> C -> A -> object ]
#
# Python determines this path using an algorithm called C3 Linearization. 
# It resolves the hierarchy using three core structural rules:
#
# 1. Subclasses Before Parents (Depth-First):
#    Python always checks the immediate class 'D' first, before looking at
#    any of its parent classes.
#
# 2. Left-to-Right Priority (Definition Order):
#    When you declared 'class D(B, C):', you listed B before C. 
#    Therefore, Python prioritizes the path through B over the path through C. 
#    This is why 'd.show()' outputs Class B's implementation.
#
# 3. No Monotonicity Violations (Clean Ancestor Postponement):
#    Even though Python explores B first, it knows B is a child of A, and A 
#    is also a parent to C. To prevent skipping C entirely, Python deliberately 
#    postpones evaluating the shared root grandparent 'A' until ALL intermediate 
#    subclasses (both B and C) have been completely checked.
# =====================================================================



# ============================================================
# EXERCISE 19 — COOPERATIVE SUPER()
# ============================================================
#
# Create:
#
#   class Robot
#   class CameraMixin
#   class LidarMixin
#   class AutonomousRobot
#
# Experiment with multiple inheritance.
#
# Each class should implement a method such as:
#
#   initialize()
#
# Use super() so that initialization can continue through
# the MRO rather than explicitly calling a specific parent.
#
# Print messages from each class so that you can observe
# the order in which methods execute.
#
# Then print AutonomousRobot.__mro__.
#
# Your goal is NOT to memorize multiple inheritance.
#
# Your goal is to understand why blindly writing:
#
#   Parent.method(self)
#
# can behave differently from:
#
#   super().method()


# ============================================================
# 1. THE CLASS HIERARCHY (Cooperative Layout)
# ============================================================

class Robot:
    def initialize(self) -> None:
        # The base root class ends the chain gracefully
        print(" [Base Robot] Core chassis power lines online.")


class CameraMixin:
    def initialize(self) -> None:
        print("[CameraMixin] Booting optic processor...")
        super().initialize()  # Pass baton to next in MRO
        print(" [CameraMixin] Optic lens alignment calibrated.")


class LidarMixin:
    def initialize(self) -> None:
        print("[LidarMixin] Spooling laser mirror motors...")
        super().initialize()  # Pass baton to next in MRO
        print("[LidarMixin] Laser sensor array locked.")


class AutonomousRobot(CameraMixin, LidarMixin, Robot):
    def initialize(self) -> None:
        print("[AutonomousRobot] Global system initialization triggered.")
        super().initialize()  # Start the chain reaction
        print("[AutonomousRobot] Autonomous systems fully operational!")


# ============================================================
# 2. VERIFICATION AND EXECUTION TRACE
# ============================================================

print("--- Testing Cooperative super() ---")
bot = AutonomousRobot()

print("\nRunning bot.initialize():")
bot.initialize()

print("\nInspecting the exact AutonomousRobot MRO Chain Layout:")
for idx, cls in enumerate(AutonomousRobot.mro(), start=1):
    print(f"  Step {idx}: {cls}")


# =====================================================================
# EXPLANATION: super() vs. Parent.method(self)
# =====================================================================
# This exercise reveals why blindly hardcoding parent class names is dangerous.
#
# If you wrote hardcoded calls inside AutonomousRobot like this:
#   CameraMixin.initialize(self)
#   LidarMixin.initialize(self)
#   Robot.initialize(self)
#
# 1. Redundant Execution: 'Robot.initialize(self)' would run MULTIPLE times 
#    because both CameraMixin and LidarMixin would also call their parents directly.
# 2. Broken Chains: If CameraMixin hardcoded 'Robot.initialize(self)', it would 
#    skip 'LidarMixin' completely!
#
# Why super() wins here:
# In Python multiple inheritance, super() DOES NOT mean "call my parent". 
# It means "look at the MRO chain, find where my current class sits, and call the 
# NEXT sibling class in that ordered list."
#
# The MRO path here is: [ AutonomousRobot -> CameraMixin -> LidarMixin -> Robot ]
# - AutonomousRobot calls super() -> Jumps to CameraMixin.
# - CameraMixin calls super()     -> Jumps HORIZONTALLY to LidarMixin!
# - LidarMixin calls super()      -> Jumps to Robot.
#
# This ensures every single module in your composition executes exactly ONCE in 
# a safe, predictable stack order.
# =====================================================================
