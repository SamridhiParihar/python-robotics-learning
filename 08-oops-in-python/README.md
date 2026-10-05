# Chapter 8 — Object-Oriented Programming in Python

> A practical reference for understanding, designing, and reviewing object-oriented Python code, with an emphasis on robotics and engineering systems.

---

## 1. Why OOP Matters in Python

Object-Oriented Programming (OOP) organizes software around **objects that combine state and behavior**.

In robotics, software naturally contains entities such as:

- Robots
- Sensors
- Motors
- Controllers
- Planners
- Cameras
- LiDARs
- IMUs
- ROS 2 nodes
- Simulation components

For example:

```text
Robot
├── Sensors
│   ├── Camera
│   ├── LiDAR
│   └── IMU
│
├── Controller
│   ├── PID
│   └── RL
│
├── Planner
└── Actuators
```

OOP allows these components to be represented as objects with clearly defined responsibilities.

The fundamental mental model is:

```text
Object
├── State
│   └── Attributes
│
└── Behavior
    └── Methods
```

---

# 2. Classes and Objects

A **class** defines the structure and behavior of objects.

An **object** is an instance of a class.

```python
class Robot:
    pass


robot1 = Robot()
robot2 = Robot()
```

Here:

```text
Robot
├── robot1
└── robot2
```

`robot1` and `robot2` are separate objects created from the same class.

```python
print(robot1 is robot2)
```

Output:

```text
False
```

They have the same type but are different objects.

---

# 3. Python Classes Are Objects

Python treats classes themselves as objects.

```python
class Robot:
    pass

print(type(Robot))
```

Typically:

```text
<class 'type'>
```

This means Python has a powerful object model where:

```text
Robot
  │
  └── object created by `type`

robot1
  │
  └── object created from `Robot`
```

This concept becomes important later when working with:

- decorators
- metaclasses
- frameworks
- ORMs
- advanced Python libraries

For normal application development, however, simply remember:

> Classes are objects too.

---

# 4. `__init__`

`__init__` initializes an object after it has been created.

```python
class Robot:

    def __init__(self, name):
        self.name = name
```

Creating an object:

```python
robot = Robot("Atlas")
```

Now:

```python
robot.name
```

returns:

```text
Atlas
```

Conceptually:

```text
Robot("Atlas")
      │
      ▼
object created
      │
      ▼
__init__(robot, "Atlas")
      │
      ▼
self.name = "Atlas"
```

### Java comparison

Java:

```java
class Robot {

    private String name;

    Robot(String name) {
        this.name = name;
    }
}
```

Python:

```python
class Robot:

    def __init__(self, name):
        self.name = name
```

For normal Python programming, `__init__` can be thought of as the constructor-like initialization method.

Technically, object creation and initialization are separate operations; `__new__` is involved in object creation. `__new__` is an advanced topic and is rarely needed in normal application code.

---

# 5. `self`

`self` refers to the current instance.

```python
class Robot:

    def move(self):
        print("Robot moving")
```

When calling:

```python
robot.move()
```

Python conceptually performs something similar to:

```python
Robot.move(robot)
```

Therefore:

```python
def move(self):
```

means that the method receives the object on which it is being called.

### Java comparison

Java:

```java
class Robot {

    void move() {
        System.out.println(this);
    }
}
```

Python:

```python
class Robot:

    def move(self):
        print(self)
```

Java hides the instance parameter.

Python makes it explicit.

---

## `self` is a convention

`self` is not a Python keyword.

Technically this would work:

```python
class Robot:

    def move(robot):
        print(robot)
```

But Python convention requires:

```python
def move(self):
```

Always use `self` for instance methods.

Similarly, `cls` is the conventional name for the class parameter in class methods.

---

# 6. Instance Attributes

Instance attributes belong to individual objects.

```python
class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
```

Now:

```python
r1 = Robot("Atlas", 90)
r2 = Robot("Spot", 70)
```

Conceptually:

```text
r1
├── name = "Atlas"
└── battery = 90

r2
├── name = "Spot"
└── battery = 70
```

Changing:

```python
r1.battery = 50
```

does not change:

```python
r2.battery
```

because each object has its own instance state.

---

# 7. Python Does Not Require Attribute Declarations

In Java, you normally declare fields:

```java
private String name;
private int battery;
```

Python creates an instance attribute when it is assigned:

```python
self.name = name
self.battery = battery
```

Python can also dynamically add attributes:

```python
robot.location = "Lab"
```

This flexibility is powerful but should be used carefully.

For maintainable code, an object's expected state should generally be clear from its class definition and initialization.

---

# 8. Instance Methods

Instance methods operate on an individual object.

```python
class Robot:

    def __init__(self, battery):
        self.battery = battery

    def move(self):
        self.battery -= 10
```

Usage:

```python
robot = Robot(100)

robot.move()

print(robot.battery)
```

Result:

```text
90
```

The method modifies the object's state.

---

# 9. Methods Can Call Other Methods

Methods can collaborate internally.

```python
class Robot:

    def start(self):
        self.connect()
        self.enable_motors()

    def connect(self):
        print("Connected")

    def enable_motors(self):
        print("Motors enabled")
```

Calling:

```python
robot.start()
```

produces:

```text
Connected
Motors enabled
```

This allows higher-level operations to hide implementation details.

---

# 10. Class Attributes

A class attribute belongs to the class itself.

```python
class Robot:
    category = "mobile robot"
```

All instances can access it:

```python
r1 = Robot()
r2 = Robot()

print(r1.category)
print(r2.category)
```

Both see:

```text
mobile robot
```

Conceptually:

```text
Robot class
└── category = "mobile robot"
       │
       ├── r1 can access it
       └── r2 can access it
```

---

# 11. Instance Attribute vs Class Attribute

Consider:

```python
class Robot:

    category = "mobile"

    def __init__(self, name):
        self.name = name
```

Here:

```text
Class state:
    category

Instance state:
    name
```

For:

```python
r1 = Robot("Atlas")
r2 = Robot("Spot")
```

we have:

```text
Robot
└── category = "mobile"

r1
└── name = "Atlas"

r2
└── name = "Spot"
```

---

# 12. Attribute Lookup

When Python evaluates:

```python
robot.name
```

it performs attribute lookup.

A simplified mental model is:

```text
robot.name
    │
    ▼
Look on instance
    │
    ├── found → return it
    │
    └── not found
          │
          ▼
      look on class
          │
          ▼
      look through inheritance
```

This is a simplified view of Python's attribute resolution system, but it is a useful mental model for everyday development and debugging.

---

# 13. Shadowing Class Attributes

Consider:

```python
class Robot:
    battery_type = "Li-Ion"
```

Then:

```python
r1 = Robot()
r2 = Robot()
```

Both initially see:

```python
r1.battery_type
r2.battery_type
```

as:

```text
Li-Ion
```

Now:

```python
r1.battery_type = "LiPo"
```

creates an instance attribute on `r1`.

Conceptually:

```text
Robot
└── battery_type = "Li-Ion"

r1
└── battery_type = "LiPo"

r2
└── no instance battery_type
```

Therefore:

```python
r1.battery_type
```

returns:

```text
LiPo
```

while:

```python
r2.battery_type
```

returns:

```text
Li-Ion
```

This is called **shadowing**.

---

# 14. Mutable Class Attribute Trap

One of the most important Python OOP bugs is accidentally sharing mutable state.

Bad:

```python
class Robot:
    sensors = []
```

Now:

```python
r1 = Robot()
r2 = Robot()

r1.sensors.append("camera")
```

`r2.sensors` may now also contain `"camera"`.

Why?

Because the list belongs to the class.

```text
Robot
└── sensors = []
       ▲
       │
   ┌───┴───┐
   r1      r2
```

### Usually correct

```python
class Robot:

    def __init__(self):
        self.sensors = []
```

Now each instance gets its own list.

```text
r1
└── sensors → separate list

r2
└── sensors → separate list
```

### Code review rule

Be suspicious of mutable class attributes such as:

```python
items = []
config = {}
cache = set()
```

Ask:

> Is this state intentionally shared across every instance?

If not, initialize it on `self`.

---

# 15. Class Methods

A class method receives the class as its first argument.

```python
class Robot:

    total_robots = 0

    @classmethod
    def get_total(cls):
        return cls.total_robots
```

Usage:

```python
Robot.get_total()
```

The conventional parameter is:

```python
cls
```

Compare:

```text
Instance method
        │
        ▼
      self
        │
        ▼
    instance

Class method
        │
        ▼
       cls
        │
        ▼
      class
```

---

# 16. Alternative Constructors

A common use of class methods is providing alternative ways to create an object.

```python
class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    @classmethod
    def from_string(cls, value):
        name, battery = value.split(",")
        return cls(name, int(battery))
```

Now:

```python
robot = Robot.from_string("Atlas,90")
```

This creates a normal `Robot`.

Other examples in real systems include:

```python
Robot.from_config(...)
Robot.from_json(...)
Robot.from_yaml(...)
Camera.from_parameters(...)
```

Using:

```python
return cls(...)
```

rather than:

```python
return Robot(...)
```

also allows subclasses to inherit the alternative constructor more naturally.

---

# 17. Static Methods

A static method does not receive either `self` or `cls`.

```python
class Robot:

    @staticmethod
    def is_valid_battery(value):
        return 0 <= value <= 100
```

Usage:

```python
Robot.is_valid_battery(80)
```

A static method is appropriate when the operation is logically related to the class but doesn't need instance or class state.

---

# 18. Don't Overuse Static Methods

Python does not require utility functions to live inside classes.

Java developers sometimes write:

```python
class RobotUtils:

    @staticmethod
    def clamp(value, minimum, maximum):
        ...
```

when a module-level function would be simpler:

```python
def clamp(value, minimum, maximum):
    ...
```

Python modules are already excellent organizational units.

Use a class when the behavior genuinely belongs to an object or abstraction.

---

# 19. Encapsulation

Java provides explicit access modifiers:

```text
public
private
protected
```

Python relies more heavily on conventions.

### Public

```python
self.name
```

Generally means the attribute is part of the public interface.

### Internal / non-public convention

```python
self._name
```

A single underscore means:

> This is intended for internal use.

It is a convention, not strict access control.

### Name mangling

```python
self.__name
```

causes name mangling, approximately:

```text
_Robot__name
```

This is not equivalent to Java's `private`.

---

# 20. Properties

Properties allow attribute-style access while executing logic behind the scenes.

```python
class Robot:

    def __init__(self, battery):
        self._battery = battery

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Battery must be between 0 and 100")

        self._battery = value
```

Usage:

```python
robot = Robot(80)

print(robot.battery)

robot.battery = 90
```

But:

```python
robot.battery = 150
```

raises:

```text
ValueError
```

---

# 21. Python Property vs Java Getter/Setter

Java:

```java
robot.getBattery();
robot.setBattery(90);
```

Python:

```python
robot.battery
robot.battery = 90
```

The Python interface looks like normal attribute access while still allowing validation and other logic.

Properties are especially useful for:

- validation
- computed values
- controlled state changes
- backwards-compatible APIs

---

# 22. Inheritance

Inheritance allows one class to derive from another.

```python
class Robot:

    def move(self):
        print("Moving")


class WheeledRobot(Robot):
    pass
```

Now:

```python
robot = WheeledRobot()
robot.move()
```

works because `WheeledRobot` inherits `move()` from `Robot`.

Relationship:

```text
Robot
  ▲
  │
WheeledRobot
```

Use inheritance when the relationship genuinely represents an **IS-A** relationship.

```text
WheeledRobot IS-A Robot
FlyingRobot IS-A Robot
```

---

# 23. Method Overriding

A subclass can replace inherited behavior.

```python
class Robot:

    def move(self):
        print("Moving")


class WheeledRobot(Robot):

    def move(self):
        print("Driving wheels")
```

Now:

```python
robot = WheeledRobot()
robot.move()
```

produces:

```text
Driving wheels
```

This is method overriding.

---

# 24. Polymorphism

Polymorphism allows different objects to be used through a common operation.

```python
class WheeledRobot:

    def move(self):
        print("Driving")


class FlyingRobot:

    def move(self):
        print("Flying")
```

Then:

```python
robots = [
    WheeledRobot(),
    FlyingRobot()
]

for robot in robots:
    robot.move()
```

Output:

```text
Driving
Flying
```

The caller doesn't need to know the concrete implementation.

This is extremely useful in robotics:

```text
Controller
├── PIDController
├── MPCController
└── RLController
```

All can expose:

```python
controller.compute_action(state)
```

---

# 25. `super()`

`super()` allows method lookup to continue through the inheritance hierarchy.

```python
class Robot:

    def __init__(self, name):
        self.name = name


class WheeledRobot(Robot):

    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels
```

This avoids duplicating:

```python
self.name = name
```

inside the child.

A useful beginner mental model is:

> `super()` lets the subclass use behavior from the inherited class.

More technically, `super()` interacts with Python's **Method Resolution Order (MRO)**.

---

# 26. Method Resolution Order (MRO)

Python supports multiple inheritance.

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
```

Python determines the order in which it searches for methods.

You can inspect it:

```python
print(D.__mro__)
```

or:

```python
print(D.mro())
```

MRO becomes particularly important when multiple classes define the same method.

---

# 27. Composition

Composition means building objects from other objects.

```python
class Camera:

    def capture(self):
        ...


class Lidar:

    def scan(self):
        ...


class Robot:

    def __init__(self):
        self.camera = Camera()
        self.lidar = Lidar()
```

Now:

```python
robot.camera.capture()
robot.lidar.scan()
```

The relationship is:

```text
Robot
├── HAS-A Camera
└── HAS-A Lidar
```

This is different from inheritance:

```text
WheeledRobot IS-A Robot
```

---

# 28. Inheritance vs Composition

A useful rule:

```text
IS-A  → inheritance

HAS-A → composition
```

Examples:

```text
WheeledRobot IS-A Robot
FlyingRobot IS-A Robot

Robot HAS-A Camera
Robot HAS-A Lidar
Robot HAS-A Controller
Robot HAS-A Planner
```

For complex robotics systems, composition is often more flexible than deep inheritance hierarchies.

---

# 29. Why Composition Is Important in Robotics

A robot is naturally a collection of components:

```text
Robot
├── Camera
├── LiDAR
├── IMU
├── Controller
├── Planner
└── MotorController
```

If the system uses composition, individual components can be replaced.

For example:

```text
Controller
├── PIDController
├── MPCController
└── RLController
```

The robot doesn't need to fundamentally change when the controller changes.

This is useful for:

- experimentation
- simulation
- testing
- hardware replacement
- research
- algorithm comparison

---

# 30. Dependency Injection

Instead of creating dependencies internally:

```python
class Robot:

    def __init__(self):
        self.controller = RLController()
```

provide them from outside:

```python
class Robot:

    def __init__(self, controller):
        self.controller = controller
```

Then:

```python
robot = Robot(RLController())
```

or:

```python
robot = Robot(PIDController())
```

The Robot doesn't need to know how the controller is created.

This is **dependency injection**.

---

# 31. Why Dependency Injection Helps Robotics

Suppose you have:

```text
RealCamera
SimulatedCamera
MockCamera
```

and:

```text
PIDController
RLController
MockController
```

You can construct:

```text
Simulation
    ↓
Robot
 ├── SimulatedCamera
 └── RLController
```

or:

```text
Real Hardware
    ↓
Robot
 ├── RealCamera
 └── PIDController
```

without rewriting the Robot's core logic.

This greatly improves:

- testability
- flexibility
- experimentation
- separation of concerns

---

# 32. Abstract Base Classes

Python provides abstract base classes through `abc`.

```python
from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def compute_action(self, state):
        pass
```

Concrete implementations:

```python
class PIDController(Controller):

    def compute_action(self, state):
        ...


class RLController(Controller):

    def compute_action(self, state):
        ...
```

The base class describes the required interface.

---

# 33. Duck Typing

Python often does not require inheritance to achieve polymorphism.

Consider:

```python
class PIDController:

    def compute_action(self, state):
        ...


class RLController:

    def compute_action(self, state):
        ...
```

A function can simply do:

```python
def run_controller(controller, state):
    return controller.compute_action(state)
```

It doesn't care about the object's concrete class.

The important question is:

> Does the object provide the behavior I need?

This is **duck typing**.

> "If it behaves like the required object, it can be used like the required object."

---

# 34. ABC vs Duck Typing

### Abstract Base Class

```text
Controller
    ▲
    │
    ├── PIDController
    └── RLController
```

Explicit relationship.

### Duck typing

```text
PIDController ──┐
                │
RLController ───┼──→ compute_action()
                │
FakeController ─┘
```

No required inheritance relationship.

Python often favors behavioral interfaces over rigid class hierarchies.

---

# 35. Protocols

Protocols allow Python's type system to express duck-typed interfaces.

```python
from typing import Protocol


class Controller(Protocol):

    def compute_action(self, state):
        ...
```

A class can satisfy this protocol by providing the required behavior without explicitly inheriting from it.

Protocols become particularly useful in larger typed Python codebases.

They are covered more deeply later in:

> Chapter 13 — Type Hints, Dataclasses & Static Analysis

---

# 36. Dataclasses

For objects primarily representing data, Python provides `dataclass`.

```python
from dataclasses import dataclass


@dataclass
class RobotState:
    x: float
    y: float
    velocity: float
    battery: float
```

Now:

```python
state = RobotState(
    x=1.2,
    y=3.4,
    velocity=0.8,
    battery=90.0
)
```

Dataclasses automatically provide useful boilerplate such as initialization and representation.

They are useful for:

- sensor data
- configuration
- robot state
- experiment parameters
- messages
- model configuration

Dataclasses will be covered more deeply later.

---

# 37. Special Methods / Dunder Methods

Python classes can define special methods with names such as:

```python
__init__
__str__
__repr__
__len__
__eq__
__lt__
```

These allow objects to integrate with Python's language features.

For example:

```python
class Robot:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Robot({self.name})"
```

Now:

```python
robot = Robot("Atlas")

print(robot)
```

can produce:

```text
Robot(Atlas)
```

These methods are often called **dunder methods** because of the double underscores.

They will become important when reading mature Python codebases.

---

# 38. Pythonic OOP vs Java-Style OOP

One of the most important lessons:

> Python OOP is not Java OOP with different syntax.

Java often encourages:

```java
private fields
getters/setters
interfaces
explicit types
large class hierarchies
```

Python provides alternatives such as:

```text
properties
duck typing
protocols
dynamic typing
composition
modules
first-class functions
dataclasses
```

For example, Java-style Python:

```python
class Robot:

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
```

Often becomes:

```python
class Robot:

    def __init__(self, name):
        self.name = name
```

or, if validation is required, a property can be used.

---

# 39. Avoid Unnecessary Classes

Not everything needs to be an object.

This:

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b
```

may be unnecessary.

A module-level function is often better:

```python
def add(a, b):
    return a + b
```

Use classes when they provide a meaningful abstraction around:

- state
- behavior
- identity
- lifecycle
- responsibilities
- interchangeable implementations

---

# 40. High Cohesion and Low Coupling

Good OOP design generally aims for:

### High cohesion

A class should have closely related responsibilities.

Bad:

```text
Robot
├── database operations
├── HTTP requests
├── image processing
├── motor control
├── logging configuration
└── user authentication
```

Better:

```text
Robot
├── MotorController
├── SensorManager
├── Planner
├── Controller
└── StateManager
```

### Low coupling

Classes should avoid unnecessary dependencies on implementation details of other classes.

For example:

```text
Robot → Controller interface
```

is generally more flexible than:

```text
Robot → specific RL algorithm implementation
```

---

# 41. A Robotics OOP Mental Model

A useful architecture is:

```text
                    Robot
                      │
       ┌──────────────┼──────────────┐
       │              │              │
    Sensors       Controller       Planner
       │              │              │
   ┌───┼───┐      ┌───┼───┐       ┌─┴─┐
   │   │   │      │   │   │       │   │
Camera Lidar IMU  PID  RL  MPC    A*  RRT
```

The important relationships are:

```text
Robot HAS-A Sensor
Robot HAS-A Controller
Robot HAS-A Planner

PIDController IS-A Controller
RLController IS-A Controller
```

Or, if using duck typing:

```text
PIDController ──┐
RLController ───┼── implements expected behavior
MPCController ──┘
```

---

# 42. OOP in ROS 2

Many ROS 2 Python programs use classes extensively.

A simplified example:

```python
class RobotNode(Node):

    def __init__(self):
        super().__init__("robot_node")

        self.publisher = ...
        self.subscription = ...
        self.timer = ...
```

This combines several concepts:

```text
class
  ↓
inheritance
  ↓
super()
  ↓
__init__
  ↓
instance attributes
  ↓
composition
  ↓
methods
```

A ROS 2 node may itself contain:

```text
RobotNode
├── Publishers
├── Subscribers
├── Timers
├── Parameters
├── Sensors
├── Controllers
└── Robot state
```

Therefore, understanding Python OOP is directly useful for ROS 2.

---

# 43. OOP Code Reading Checklist

When encountering an unfamiliar Python class, ask:

### Class

- What responsibility does this class have?
- What does the class represent?
- Who creates instances of it?

### Initialization

- What happens inside `__init__()`?
- What state is initialized?
- Are all expected attributes initialized?

### Instance state

- Which attributes belong to each instance?
- Is any state unexpectedly shared?

### Class state

- Are there class attributes?
- Are mutable class attributes intentional?

### Methods

- Which methods modify state?
- Which methods only calculate values?
- Which methods have side effects?

### Dependencies

- Does the class create its own dependencies?
- Could dependencies be injected?

### Inheritance

- Does the class inherit from something?
- Is the IS-A relationship meaningful?
- Is `super()` being used correctly?

### Composition

- What objects does the class contain?
- Is composition more appropriate than inheritance?

### Polymorphism

- Does the class implement a common interface?
- Could another implementation be substituted?

### Pythonic design

- Are there unnecessary getters/setters?
- Are static methods being overused?
- Could a module-level function be simpler?
- Is duck typing sufficient?
- Would a property improve the API?

---

# 44. OOP Code Review Checklist

When reviewing Python OOP code, look for:

### State problems

```python
class Robot:
    sensors = []
```

Potential shared mutable state.

### Initialization problems

```python
class Robot:

    def move(self):
        self.speed = 10
```

State may not exist until a method is called.

### Excessive inheritance

```text
A
└── B
    └── C
        └── D
            └── E
```

Deep hierarchies can become difficult to maintain.

### Excessive coupling

```python
class Robot:

    def __init__(self):
        self.controller = ConcreteRLController()
```

The Robot is tightly coupled to one implementation.

### Java-style boilerplate

```python
get_name()
set_name()
get_battery()
set_battery()
```

Check whether Python properties or direct attributes would be more appropriate.

### Unnecessary classes

Some classes exist only to group static utility functions.

A module may be simpler.

### God objects

One class doing everything:

```text
Robot
├── sensors
├── motors
├── database
├── networking
├── logging
├── ML inference
├── navigation
└── UI
```

This usually indicates poor separation of responsibilities.

---

# 45. Common Mistakes for Java Developers

Coming from Java, pay particular attention to these:

### Mistake 1 — Treating Python as Java

Don't automatically recreate Java patterns.

### Mistake 2 — Overusing getters/setters

Python properties often provide a cleaner interface.

### Mistake 3 — Assuming `private` works the same way

Python uses conventions rather than strict access control.

### Mistake 4 — Overusing inheritance

Prefer composition when the relationship is HAS-A.

### Mistake 5 — Ignoring duck typing

Python often doesn't require explicit interface inheritance.

### Mistake 6 — Creating utility classes unnecessarily

Modules and functions are often enough.

### Mistake 7 — Forgetting mutable class attributes

Shared mutable state can cause subtle bugs.

### Mistake 8 — Not understanding `self`

Remember:

```python
robot.move()
```

conceptually involves:

```python
Robot.move(robot)
```

### Mistake 9 — Assuming `super()` simply means "parent"

`super()` actually follows Python's method resolution rules.

### Mistake 10 — Making every object responsible for creating its dependencies

Dependency injection often produces more flexible systems.

---

# 46. Java → Python OOP Quick Comparison

| Concept | Java | Python |
|---|---|---|
| Class | `class` | `class` |
| Object | `new Robot()` | `Robot()` |
| Constructor-like initialization | `Robot()` | `__init__()` |
| Current instance | `this` | `self` |
| Class/static state | `static` | class attributes |
| Class method | static/class patterns | `@classmethod` |
| Static method | `static` | `@staticmethod` |
| Private | `private` | `_name` convention / name mangling |
| Getter/setter | explicit methods | properties |
| Interface | `interface` | ABC / Protocol / duck typing |
| Inheritance | `extends` | `(Parent)` |
| Parent behavior | `super` | `super()` |
| Polymorphism | explicit type hierarchy common | duck typing very common |
| Data object | POJO/record | dataclass |
| Utility organization | utility class common | module-level functions common |

---

# 47. Core Mental Model

Keep this model in your head:

```text
                       CLASS
                         │
             ┌───────────┴───────────┐
             │                       │
           STATE                   BEHAVIOR
             │                       │
        attributes                methods
             │                       │
             └───────────┬───────────┘
                         │
                         ▼
                       OBJECT
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       instance       instance       instance
          │              │              │
       state A        state B        state C
```

Then:

```text
Inheritance
    ↓
IS-A relationship

Composition
    ↓
HAS-A relationship

Polymorphism
    ↓
Same interface / behavior, different implementation

Dependency Injection
    ↓
Dependencies supplied from outside

Duck Typing
    ↓
Behavior matters more than inheritance

Protocols
    ↓
Formalize expected behavior for type checking
```

---

# 48. Robotics Architecture Mental Model

A mature robotics system may eventually look conceptually like:

```text
                         Robot
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
      Sensors          Controller           Planner
        │                  │                  │
   ┌────┼────┐        ┌────┼────┐        ┌───┴───┐
   │    │    │        │    │    │        │       │
Camera Lidar IMU      PID   RL   MPC      A*      RRT
        │                  │
        └──────────────────┼──────────────────┐
                           │                  │
                       Actuators          Robot State
```

The goal of OOP is not to create as many classes as possible.

The goal is to create **clear boundaries between responsibilities**.

---

# 49. The Most Important Principles

If you remember only a few things from this chapter, remember these:

### 1. Objects combine state and behavior

```text
Object = State + Behavior
```

### 2. `self` represents the current instance

```python
robot.move()
```

is conceptually similar to:

```python
Robot.move(robot)
```

### 3. Class attributes are shared

Be careful with mutable class attributes.

### 4. Composition is extremely powerful

```text
Robot HAS-A Sensor
Robot HAS-A Controller
```

### 5. Inheritance represents IS-A

```text
RLController IS-A Controller
```

### 6. Polymorphism reduces coupling

Different implementations can satisfy the same expected behavior.

### 7. Python favors flexibility

Duck typing, properties, protocols, modules, functions, and composition are important parts of Python's design philosophy.

### 8. Don't blindly translate Java into Python

Write **Pythonic Python**, not Java with Python syntax.

---

# 50. What Comes Next

After mastering OOP, the next chapters build on these foundations:

```text
Chapter 8
Object-Oriented Programming
        │
        ▼
Chapter 9
Files, Paths & Serialization
        │
        ▼
Chapter 10
Iterators, Generators & yield
        │
        ▼
Chapter 11
Decorators & Context Managers
        │
        ▼
Chapter 12
Pythonic Programming & Advanced Patterns
        │
        ▼
Chapter 13
Type Hints, Dataclasses & Static Analysis
        │
        ▼
Chapter 14
Testing & Debugging
        │
        ▼
Chapter 15+
Advanced Python
        │
        ▼
NumPy → PyTorch → DL → CV → RL
        │
        ▼
ROS 2
        │
        ▼
Robotics
        │
        ▼
Embodied AI
```

The most important transition is:

> **OOP gives you the ability to understand the structure of a robotics codebase. The upcoming chapters teach you the Python mechanisms used inside those structures.**

This README is intended as the **long-term Chapter 8 reference**; the exercises and your solutions should remain separate from it.
