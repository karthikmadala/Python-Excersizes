def greeting(name):
    print(f"Hello {name}")

person1 = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": None,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}

import numpy as np

print(np.__version__)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[1, 1, 0])

arr = np.array([-1, 0, 1])
newarr = arr.astype(bool)
print(newarr)
arr = np.array([15, 38, 41, 46])
x = np.where(arr%2 == 1)
print(x)