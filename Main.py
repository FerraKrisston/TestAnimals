#!/usr/bin/env python3
import sys
import CatClass
import DogClass
import HippoClass
import LionClass
import WolfClass
import PetClass
import AnimalClass

C = CatClass.Cat()
D = DogClass.Dog()
H = HippoClass.Hippo()
L = LionClass.Lion()
W = WolfClass.Wolf()

def main():
    animalType = sys.argv[1]
    commandType = sys.argv[2]
    print("Команда: ", animalType + "." + commandType)
    animalType + "." + commandType
    W.eat

if __name__ == "__main__":
    main()
