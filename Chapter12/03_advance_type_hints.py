from typing import List, Dict, Tuple, Union

# List Usage
num: List[int] = [1, 2, 3, 4, ]
print(num)

# Dictionary Usage
a_dict: Dict[str, int] = {'name': 'Akhand', 'age': 23}
print(a_dict.items())

# Tuple Usage
person: Tuple[str, int] = ('Akhand', 36)
print(person)

# Union type for variables that can hold multiple types
data: Union[str, int] = "Asddf"
intdata: Union[str, int] = 123
