# Generic class

Link : https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb

User defined generic types

In the following example we have made a registry class. The type of the contents of the registry is generic.
This type is stated when we instantiate this class. After instantiation that instance will only accept arguments
of that type.

Here we have added a generic type named T. We did this by using the TypeVar factory, giving the name of the type
we want to create and then capturing that in a variable named T. This is then used the same way as any other 
type is used in Python type hints. T and U are commonly used names in generics (T standing for Type and U 
standing for…. nothing. It’s just the next letter in the alphabet) similar to how i and x are used as 
iteration variables.

Example of **dependency injection**. 

```python
from typing import Dict, Generic, TypeVar

T = TypeVar("T")

class Registry(Generic[T]):
    def __init__(self) -> None:
        self._store: Dict[str, T] = {}
          
    def set_item(self, k: str, v: T) -> None:
        self._store[k] = v
    
    def get_item(self, k: str) -> T:
        return self._store[k]
  
if __name__ == "__main__":
    family_name_reg = Registry[str]()
    family_age_reg = Registry[int]()
    
    family_name_reg.set_item("husband", "steve")
    family_name_reg.set_item("dad", "john")
    
    family_age_reg.set_item("steve", 30)
    
    family_age_reg.set_item("steve", "yeah")
    # mypy raises: Argument 2 to "set_item" of "Registry" has incompatible type "str"; expected "int"
```

Here we have created the generic class Registry. This is done by extending the Generic base class, and by 
defining the generic types we want to be valid within this class. In this case we define T(line 5) which is 
then used within methods of the Registry class.

When we instantiate family_name_reg, we state that it will only hold values of type string 
(by using Registry[str]), and the family_age_reg instance will only hold values of type integer 
(by using Registry[int]).

Generics have allowed us to create a class that can be used with multiple types, and then enforce 
(through the use of tools such as mypy) that only arguments of the specified type are sent to the methods 
of the instance.

Using our example above, if we try to set a string value in the age registry, we can see that mypy will 
raise this as an error.

Generics are very powerful and help you to better reason about what you are doing and why. They also 
communicate that information to others, or your future self, that are reading your code and add a contract 
that static analysis tools can use to check your code is correct. In Python we don’t need to use them, but 
only in the same way we don’t need to add type hints. Much for the same reasons why we try to make code 
readable by writing small functions and using naming conventions that are meaningful, using type hints and 
generics just makes things easier to reason about, which means less time trying to understand what is going
on and more time progressing your project.

## Generic Data Repository Class

Link : https://www.slingacademy.com/article/python-generic-types-tutorial-examples/

This example demonstrates a more advanced use case of generic types in Python. We’ll make a generic data
repository class that can work with different data types.

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class DataRepository(Generic[T]):
    def __init__(self):
        self.data = []

    def add_data(self, item: T) -> None:
        self.data.append(item)

    def remove_data(self, item: T) -> None:
        self.data.remove(item)

    def get_all_data(self) -> List[T]:
        return self.data

# Example usage
repo = DataRepository[int]()
repo.add_data(10)
repo.add_data(20)
repo.add_data(30)
print(repo.get_all_data()) # Output: [10, 20, 30]
repo.remove_data(20)
print(repo.get_all_data()) # Output: [10, 30]

repo2 = DataRepository[str]()
repo2.add_data('apple')
repo2.add_data('banana')
repo2.add_data('orange')
print(repo2.get_all_data()) # Output: ['apple', 'banana', 'orange']
repo2.remove_data('banana')
print(repo2.get_all_data()) # Output: ['apple', 'orange']
```

Our DataRepository class uses a generic type T to define the type of data that the repository can store. 
The **generic type T ensures that the data added to the repository is of the correct type**, and the generic 
return type **List[T] ensures that the data retrieved from the repository is of the correct type**, too.
