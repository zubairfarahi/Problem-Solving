"""
    Create a class "Animal". You will use this class later to extend it
    with other types of animals.
    This should be an abstract class (no functionality, only works as an
    interface for the other classes). https://docs.python.org/3/library/abc.html
    public attributes:
        - color: str
        - age: int
        - animal_type: Enum (https://docs.python.org/3/library/enum.html)
    public methods:
        - sound() - returns str
            - should return the sound the animal makes
                e.g. Dog - "woof"
        - tell_age() - returns int
            - returns the current animal age
        - age_up() - returns nothing
            - should add 1 year to the current age
        - all_implemented() - returns bool
            - this method must have a functionality, if all the methods
            above have been implemented, then this should return True,
            otherwise it should return False.
    This is an abstract class! Pay attention, this class MUST NOT have any
    functionality in it (besides all_implemented()).
    The explanations for what the methods should do are mainly for the classes
    that will extend the Animal class.
"""

"""
    Create 3 classes:
        - Cat
        - Dog
        - Mouse
    All of these 3 classes must inherit from the Animal class.
    public attributes:
        - inherited from Animal (on init (or also called constructor))
        - enemy (on constructor (init))
            - is reference to the enemy of the current Animal
            e.g. Dog is the enemy of Cat
    private attributes:
        - specific_sound: str
    public methods:
        - inherited from Animal
    private methods:
        - enemy_fear_sound() - returns str
            - this is called inside the sound() method, and if an enemy has
            been passed on the constructor, then the sound should be different
            than the usual sound of the animal
            e.g.
                if Cat is called with enemy = Dog, then the cat should make
            a "meoooooow scared" sound.
                else the cat makes a "meow" sound
"""

from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
from enum import Enum



class Animal(ABC):

    color: str
    age: int
    animal_type: Enum

    @abstractmethod
    def sound(self) -> str:
        pass
    @abstractmethod
    def tell_age(self) -> int:
        pass
    @abstractmethod
    def age_up(self):
        pass

    def all_implemented(self, check) -> bool:
        if check == True:
            return True
    
   

class Cat(Animal):

    __specific_sound: str

    def __init__(self, enemy) -> None:
        super().__init__()
        self.enemy = enemy

    def sound(self) -> str:
        if self.enemy == "Dog":
            return self.__enemy_fear_sound()
        else:
            return "mewooooooo!!!!"

        return "Meeow"   

    def tell_age(self) -> int:
        return 12
    
    def age_up(self):
        return 12 + 1

    def __enemy_fear_sound(self) -> str:
        return "ALERT! mewwww"


class Dog(Animal):
    __specific_sound: str

    def __init__(self, enemy) -> None:
        super().__init__()
        self.enemy = enemy

    def sound(self) -> str:
        return "Woof"   

    def tell_age(self) -> int:
        return 12
    
    def age_up(self):
        return 12 + 1
    
    def __enemy_fear_sound() -> str:
        pass

class Mouse(Animal):
    __specific_sound: str

    def __init__(self, enemy) -> None:
        super().__init__()
        self.enemy = enemy

    def sound(self) -> str:
        return "beeeee"   

    def tell_age(self) -> int:
        return 12
    
    def age_up(self):
        return 12 + 1
    
    def __enemy_fear_sound() -> str:
        pass

cat = Cat("")
print(cat.sound())