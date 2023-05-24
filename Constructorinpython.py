class Person:
   
    def __init__(self, name, age, address=None, email=None):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
     

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        print("Email:", self.email)



# Creating objects of the class with different constructor parameter types
person1 = Person("John Doe", 25)
person2 = Person("Jane Smith", 30, "123 Main St")
person3 = Person("Mike Johnson", 40, "456 Elm St", "mike@example.com")

# Displaying details of the persons
person1.display_details()
print("--------------------")
person2.display_details()
print("--------------------")
person3.display_details()


'''
The provided program demonstrates the use of a class called `Person` with a constructor (`__init__`) and a method (`display_details`). Let's go through the program step by step to understand its functionality:

1. The `Person` class is defined. It represents a person and has attributes like `name`, `age`, `address`, and `email`. The class provides a constructor (`__init__`) and a method (`display_details`).

2. The constructor (`__init__`) is a special method that is automatically called when an object of the class is created. It takes several parameters:
   - `self`: The first parameter represents the instance of the class and is used to refer to the object being created.
   - `name`: This is a required parameter and represents the name of the person (type: string).
   - `age`: This is a required parameter and represents the age of the person (type: integer).
   - `address`: This is an optional parameter that defaults to `None`. It represents the address of the person (type: string).
   - `email`: This is an optional parameter that defaults to `None`. It represents the email address of the person (type: string).

3. Inside the constructor, the parameters (`name`, `age`, `address`, `email`) are assigned to the corresponding attributes of the object using the `self` keyword. For example, `self.name = name` assigns the value of `name` to the `name` attribute of the object.

4. The `display_details` method is defined within the `Person` class. It is responsible for displaying the details of the person stored in the object. It doesn't take any additional parameters apart from `self`.

5. Inside the `display_details` method, the details of the person (name, age, address, and email) are printed using the `print` function. The attributes are accessed using the `self` keyword, such as `self.name` and `self.age`.

6. Objects of the `Person` class are created:
   - `person1` represents a person named "John Doe" with an age of 25. It doesn't have an address or email specified.
   - `person2` represents a person named "Jane Smith" with an age of 30 and an address of "123 Main St". It doesn't have an email specified.
   - `person3` represents a person named "Mike Johnson" with an age of 40, an address of "456 Elm St", and an email of "mike@example.com".

7. The details of each person are displayed by calling the `display_details` method on each object. This prints the person's name, age, address, and email using the `print` function.

Overall, this program demonstrates how to define a class with a constructor and methods, create objects of the class with different sets of constructor parameters, and display the details stored in the objects. It highlights the use of constructors to initialize object attributes and the usage of methods to perform actions on the objects.

'''