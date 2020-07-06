class car:
#    pass #It creates an empty class
    def __init__(self,speed,color):
        print('the __init__ is called')
        print(speed,color)
        self.speed = speed
        self.color = color
#serves as a constructor for the class || used to initialize some attributes or function
#this will be the frst method which will be called when you create instance of a class.
#Since we've created 3 instances --> ford,audi,honda so this will be called 3 times at the beginning.
#init is not actually a constructor but it is the closest thing to constructor in Python.
#Python doesn't have Destructor because python has automatic garbage collector.
#----------
#if you define multiple __init__ methods so the only last writted one will be valid and overwrite all others on above.


#Creating Instances of the class
ford  = car(200,'red')
audi  = car(250,'blue')
honda = car(300,'black')



#Associating qualities || Speed and Color are variables that hold some data inside them.
ford.speed  = 200
audi.speed  = 220
honda.speed = 250

ford.color  = "red"
audi.color  = "green"
honda.color = "blue"

#Printing
print(ford.speed)
print(ford.color)
