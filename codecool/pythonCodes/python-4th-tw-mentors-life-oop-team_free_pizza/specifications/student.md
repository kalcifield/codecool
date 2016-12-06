# Student
## Description
This class represents a student in real life. 
It should inherit all properties from the Person class, but also has some other functionalities.

##Parent class
Person

##Attributes

* ```knowledge_level```
  * data type: integer
  * description: stores the stores the knowledge level of the student in programming.
* ```energy_level```
  * data type: integer
  * description: current energy level
## Class methods

### ```create_by_csv```

Gets a csv file path as an argument (the csv contains all the data needed to instantiate a student object) and gives back a list of students.

### ```constructor```
Calls the Person's constructor, but also set's the attributes above (should raise an error, if any is empty).

### Arguments
csv file

###Return value
```Student_list``` object

```

###Instance methods
### ```__init__```
The constructor of the object, calls from Person class.