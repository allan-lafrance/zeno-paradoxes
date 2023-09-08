
# <p align="center">Zeno's paradoxes</p>

# Paradoxes    
- Achilles and the tortoise
- Arrow paradox
- Dichotomy paradox




## introduciton    
Zeno's paradoxes, formulated over two millennia ago by the Greek philosopher Zeno of Elea, are famous paradoxes that challenge the concept of motion. In this set of Python scripts, we will explore three of these paradoxes using programming. These paradoxes highlight seemingly impossible situations by dividing motion into an infinite series of infinitely small steps. For each paradox, we will create a Python script to illustrate the situation and show how it can be resolved. The three paradoxes we will address are:

### Achilles and the Tortoise

#### The code defines two classes:

Athlete: Represents an athlete with a name, speed, and position. The athlete can move forward and print their current position.

Race: Represents the race scenario. It initializes a race with a given course distance and the Tortoise's starting position. The race is started using the start_race method, which iteratively moves both Achilles and the Tortoise forward until Achilles catches up with or surpasses the Tortoise's position.

The code then creates an instance of the Race class with a course distance of 500 meters and a Tortoise starting at 10 meters. Finally, it starts the race simulation.

This code illustrates the classical paradox in a simple Python program, demonstrating the concept of infinite tasks required for Achilles to catch the Tortoise, even though Achilles is faster.

### The Dichootomy Paradox


his Python code illustrates the classic paradox involving a rock being thrown towards a tree. The code defines a function:

paradox(tree): Takes the distance to a tree as an input. Inside this function, the code attempts to calculate the position of a rock thrown towards the tree with high precision. It uses an iterative process to approach the exact position of the rock concerning the tree. The key components include the initial rock position, step size, and a tolerance value for stopping the iteration when the rock gets sufficiently close to the tree.

The function continues to update the rock's position and step size until the difference between the current rock position and the tree is less than the specified tolerance. It prints the rock's position and step size at each iteration.

The code then calls the paradox function with a tree distance of 8 units, demonstrating the concept of infinite divisions and the paradox of Zeno's dichotomy.

This code provides a simple Python implementation of Zeno's paradox, showcasing how the rock approaches the tree in an infinite sequence of steps.


### The Arrow Paradox


This Python code simulates an archery scenario where an archer named "Arrow" shoots an arrow towards a target. The code defines a class:

Archery: Represents an archer with a name, shooting speed, initial position, and a target position. The archer can move forward and print their current position. The shoot method simulates the archer shooting the arrow towards the target until it reaches or surpasses the target position.

In the main section of the code, an instance of the Archery class is created, with the archer "Arrow" having a shooting speed of 25 units and aiming for a target positioned at 250 meters. The shoot method is then called to simulate the archer hitting the target.

This code demonstrates a basic archery scenario where an archer aims and shoots an arrow at a target, showcasing how the archer's position changes until they successfully hit the target at a certain distance.
