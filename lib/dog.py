# lib/dog.py

class Dog:
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

# This should be outside the Dog class definition
if __name__ == '__main__':
    fido = Dog()
    fido.bark()  # This will print "Woof!"
    fido.sit()   # This will print "The dog is sitting."
