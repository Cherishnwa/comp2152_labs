class Character:
   def __init__(self, combat_strength, health_points):
       self._health_points = health_points
       self._combat_strength = combat_strength

#Getter & Setter for combat_strength
   @property
   def combat_strength(self):
        return self._combat_strength
   
   @combat_strength.setter
   def combat_strength(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("Combat strength cannot be negative")
        self._combat_strength = value

#Getter & Setter for health_points
   @property
   def health_points(self):
        return self._health_points
   @health_points.setter
   def health_points(self, value):
        value = int(value)
        if value < 0:
            self._health_points = 0
            print("Health points cannot be negative")
        else:
             self._health_points = value 

    #Deletes the object
   def __del__ (self):
        print(f"The {self.__class__.__name__} object is being destroyed by the garbage collector")
     