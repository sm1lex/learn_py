# example how work method __init__ (this method is run as soon object (instances) of the class was created)


class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello my dear niga', self.name)

Person('Denis').say_hi()

