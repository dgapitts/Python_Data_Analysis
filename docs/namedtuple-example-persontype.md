## Advanced Python containers - collections.namedtuple - example persontype

### Summary 
* Starts with immutable tuples (familiar with this datatype which is the basis of postgres row storage)
* Using collections.namedtuple we can structure the tuples likes a database record and even have virtual columns (e.g. fullname below)

### Details

Running 

```
~/projects/Python_Data_Analysis $ cat docs/namedtuple-example-persontype.py 
# namedtuple-persontype.py
import collections

people = [("Michele", "Vallisneri", "July 15"),
          ("Albert", "Einstein", "March 14"),
          ("John", "Lennon", "October 9"),
          ("Jocelyn", "Bell Burnell", "July 15")]


print([person for person in people if person[2] == "July 15"])

# defining the namedtuple "person"
persontype = collections.namedtuple('person', ['firstname', 'lastname', "birthday"])

michele = persontype("Michele", "Vallisneri", "July 15")
print(michele)
print(type(michele))
michele = persontype(lastname="Vallisneri", firstname="Michele", birthday="July 15")
print(michele)
print(type(michele))

print(persontype(*people[1]))


from dataclasses import dataclass

# defining a data class with the same content as the "person" nametuple
# and with a default for "birthday"

@dataclass
class personclass:
    firstname: str
    lastname: str
    birthday: str = 'unknown'

michele = personclass('Michele', 'Vallisneri')

print(michele)
print(type(michele))


@dataclass
class personclass2:
    firstname: str
    lastname: str
    birthday: str = 'unknown'
    
    # all methods in a class carry a conventional argument "self";
    # when the methods are called on an instance (here, a specific person),
    # "self" points the instance itself, so self.firstname and self.lastname
    # are the data fields in that instance
    def fullname(self):
        return self.firstname + ' ' + self.lastname

michele = personclass2('Michele', 'Vallisneri', 'July 15')        
print(michele.fullname())
```

gives

```
~/projects/Python_Data_Analysis $ python3  docs/namedtuple-example-persontype.py 
[('Michele', 'Vallisneri', 'July 15'), ('Jocelyn', 'Bell Burnell', 'July 15')]
person(firstname='Michele', lastname='Vallisneri', birthday='July 15')
<class '__main__.person'>
person(firstname='Michele', lastname='Vallisneri', birthday='July 15')
<class '__main__.person'>
person(firstname='Albert', lastname='Einstein', birthday='March 14')
personclass(firstname='Michele', lastname='Vallisneri', birthday='unknown')
<class '__main__.personclass'>
Michele Vallisneri

```