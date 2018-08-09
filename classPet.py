class Pet:
    '''__init__() is a method of the class Pet. A method is a function that
    belongs to a class instance. All methods of a class first parameter is self'''

    def __init__(self,name,age, animal):
        '''self.name and self.age are instance attributes or data members of the
         class Pet. Instance attributes are unique in ever occurance (instance)
         of a Pet object'''
         self.name = name
         self.age = age
         self.animal = animal
         self.is_hungry = False
         self.mood = "happy"
