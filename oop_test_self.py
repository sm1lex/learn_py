#coco = 'mofo'
class Person:
    coco = 'dodo'
    def say(self, name):
        self.name = name
    def show(self):
        print('holol youlo', self.name)

p = Person()
p.say('jopa')
p.show()
