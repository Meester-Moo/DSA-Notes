class Robot:
  def __init__(self, name, color, weight): ## self is the actual instance variable when creating an instance of the class
    self.name = name
    self.color = color
    self.weight = weight
  
  def introduce_self(self):
    print("My name is " + self.name)

# robot1 = Robot()
# robot1.name = "R2-D2"
# robot1.color = "white and blue"
# robot1.weight = "40"
robot1 = Robot("R2-D2", "white and blue", 50)

# robot2 = Robot()
# robot2.name = "C-3PO"
# robot2.color = "gold"
# robot2.weight = "100"
robot2 = Robot("C-3PO", "gold", 100)

robot1.introduce_self()
robot2.introduce_self()

##################################################

