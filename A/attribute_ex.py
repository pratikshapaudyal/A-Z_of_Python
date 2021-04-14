class Animal:
    genus = 'Canis'
    breed = 'Schnauzer'
    name = 'Terri'
    age = 4
    colour = 'Brown'
    vaccinated = True 

#Set Attribute
setattr(Animal, 'age', 5)

#Get Attribute
print(getattr(Animal, 'age'))

#Check Attribute
print(hasattr(Animal, 'age'))

#Delete Attribute
delattr(Animal, 'age')

#Check Attribute
print(hasattr(Animal, 'age'))

