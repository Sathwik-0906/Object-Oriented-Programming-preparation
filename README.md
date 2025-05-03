# Object-Oriented Programming
OOPs (Object-Oriented Programming) is a way of writing programs by organizing code into objects, which are like real-world things.

## Why do we needed it:
- To organize code better.
- To make code more reusable, readable, and easier to manage.
- To model real-world problems in programming easily.
- To support modularity (breaking a big program into smaller parts).

## Description
Imagine you are building a video game with cars. Each car has some properties like color, speed, and fuel — and it can do things like move, stop, or honk. In OOP:

1. ### Object - A Specific Car (e.g., Red Car)
   - An **object** is an instance of a **class**. It represents a real-world item.
   - Example: A red car object might have properties like color = "red", speed = 120 km/h, and fuel = "full".

2. ### Class - A Blueprint for the Car
   - A **class** defines the properties and behaviors that every car (object) must have. It’s like a template or blueprint.
   - Example: The class `Car` might define the properties `color`, `speed`, and `fuel`, and the methods `move()`, `stop()`, and `honk()`.



   ```python
   class Car:
       def __init__(self, color, speed, fuel):
           self.color = color
           self.speed = speed
           self.fuel = fuel

       def move(self):
           print("The car is moving")

       def stop(self):
           print("The car has stopped")

       def honk(self):
           print("Beep beep!")


3. ### Encapsulation - Hiding the Complex Stuff

   * **Encapsulation** is the practice of hiding the complex inner workings of an object and only exposing necessary functionality (methods).
   * Example: You don’t need to know how the engine works internally to drive the car. You just use the `move()` method.
   * In code: By using methods, you can control how the data inside the object is accessed or modified.

4. ### Inheritance - Building on Existing Cars

   * **Inheritance** allows you to create new classes that inherit the features of an existing class but can also have their own specific features.
   * Example: A `RaceCar` class can inherit from the `Car` class, keeping the properties and methods of `Car`, but adding new features like `boost()` for extra speed.

   ```python
   class RaceCar(Car):
       def __init__(self, color, speed, fuel, turbo):
           super().__init__(color, speed, fuel)
           self.turbo = turbo

       def boost(self):
           print("Turbo boost activated!")
   ```

5. ### Polymorphism - The Same Action, Different Output

   * **Polymorphism** means that you can perform the same action on different objects, but the outcome may vary depending on the object.
   * Example: In the game, `move()` might have different effects depending on the car's class. A regular car moves normally, while a race car moves faster.

   ```python
   def move_car(car):
       car.move()

   # Creating objects
   car1 = Car("red", 120, "full")
   car2 = RaceCar("blue", 200, "half", "on")

   move_car(car1)  # Output: The car is moving
   move_car(car2)  # Output: The car is moving, with turbo boost activated!

" Encapsulation


