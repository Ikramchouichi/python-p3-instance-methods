# lib/person.py

class Person:
    def talk(self):
        """Prints a greeting message."""
        print("Hello World!")

    def walk(self):
        """Prints a message indicating the person is walking."""
        print("The person is walking.")


if __name__ == '__main__':

    john = Person()
    
   
    john.talk()  
    john.walk()  