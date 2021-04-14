# Attribute


## What is an Attribute
Attributes can be set, deleted, retrieved and checked. 
At the class level, an attribute is a particular property of that class. 

## Code example


Take for example an Animal class

```python
class Animal:
    type = 'Dog'
    breed = 'Schnauzer'
    name = 'Terri'
    age = 4
    colour = 'Brown'
    vaccinated = True 
```

**setattr()**
To change a value of one of the attributes (e.g. type, breed, name, age, colour, vaccinated)
use the `setattr()` function.
setattr(object, name value)
setattr(Animal, 'age', 5) is equivalent to Animal.age = 5

```bash
>>> setattr(Animal, 'age', 5)
>>>
```

**getattr()**
To get a value from an attribute use the `getattr()` function.
getattr(object, name)
getattr(Animal, 'age') Animal.age
```bash
>>> getattr(Animal, 'age')
5
```

**delattr()**
To delete an attribute use the `delattr()` function.
delattr(object, name)
```bash
>>> delattr(Animal, 'age')
>>>
```

**hasattr()**
To check if a class contains a certain attribute use the `hasattr()` function.
hasattr(object, name)
```bash
>>> hasattr(Animal, 'age')
True
```

Please refer to the [Attribute Python Example](https://github.com/pratikshapaudyal/A-Z_of_Python/blob/develop/A/attribute_ex.py) for more details. 