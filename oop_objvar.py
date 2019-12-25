#class and object/instance variables example

class Robot:
    """Represents a robot, with a name."""
    #counting number of robots
    robot_number = 0
    
    def __init__(self, name):
        """Initialize name of robots."""
        self.name = name
        print('Initialize robot {}'. format(self.name))
        Robot.robot_number +=1

    def del_robot(self):
        """Deleting robot in the system."""
        print('{} is being destroyed!'. format(self.name))
        Robot.robot_number -=1

        if Robot.robot_number == 0:
            print('{} is the last robot in the planet'. format(self.name))
        else:
            print('Today we have {} robots in the planet'. format(Robot.robot_number))

    def robot_greeting(self):
        print('Greetings, my master call me {}'. format(self.name))


    def howmany_robots():
        """Prints the current number of robots."""
        print('We have {} robots.'. format(Robot.robot_number))

        """This another example how we can use decorators."""
    
    howmany_robots = staticmethod(howmany_robots)
#   @classmethod 
#   def howmany_robots(cls):
#       print('We have {:d} robots.'. format(cls.robot_number))

dron1 = Robot('R2-D2')
dron1.robot_greeting()
dron1.howmany_robots()

dron2 = Robot('Boobas')
dron2.robot_greeting()
dron2.howmany_robots()

print('Robots finished their work and must die')
dron1.del_robot()
dron2.del_robot()
Robot.howmany_robots()

print(Robot.__doc__)
