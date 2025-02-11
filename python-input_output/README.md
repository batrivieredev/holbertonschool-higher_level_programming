## Resources

**Read or watch**:

*   [7.2. Reading and Writing Files](/rltoken/n4cEqOMm5PdqDE26lyWcDw "7.2. Reading and Writing Files")
*   [8.7. Predefined Clean-up Actions](/rltoken/PhUB_UH5Ry2tGGK2VGJNGA "8.7. Predefined Clean-up Actions")
*   [Dive Into Python 3: Chapter 11. Files](/rltoken/ciGk1flXa0Pbn8gv-x1FxQ "Dive Into Python 3: Chapter 11. Files") (_until “11.4 Binary Files” (included)_)
*   [JSON encoder and decoder](/rltoken/0p1V5yvlnt3iCTE0DWV2Cg "JSON encoder and decoder")
*   [Learn to Program 8 : Reading / Writing Files](/rltoken/zjejIRFH-ZgDaLLp6BWYnA "Learn to Program 8 : Reading / Writing Files")
*   [Automate the Boring Stuff with Python](/rltoken/AOiShF_tqAawS_pKaiX51w "Automate the Boring Stuff with Python") (_ch. 8 p 180-183 and ch. 14 p 326-333_)
*   [sys package](/rltoken/nIuRQWNy4mJBiqtKHgvJSw "sys package")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/Hz3CSCRXnnDyjdTSHQcUKQ "explain to anyone"), **without the help of Google**:

### General

*   Why Python programming is awesome
*   How to open a file
*   How to write text in a file
*   How to read the full content of a file
*   How to read a file line by line
*   How to move the cursor in a file
*   How to make sure a file is closed after using it
*   What is and how to use the `with` statement
*   What is `JSON`
*   What is serialization
*   What is deserialization
*   How to convert a Python data structure to a JSON string
*   How to convert a JSON string to a Python data structure
*   How to access command line parameters in a Python script

## Requirements

### Python Scripts

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle (version 2.7.\*)
*   All your files must be executable
*   The length of your files will be tested using `wc`

### Python Test Cases

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files should end with a new line
*   All your test files should be inside a folder `tests`
*   All your test files should be text files (extension: `.txt`)
*   All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks

### 1.



Write a function that reads a text file (`UTF8`) and prints it to stdout:

*   Prototype: `def read_file(filename=""):`
*   You must use the `with` statement
*   You don’t need to manage `file permission` or `file doesn't exist` exceptions.
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
read\_file = \_\_import\_\_('0-read\_file').read\_file

read\_file("my\_file\_0.txt")

guillaume@ubuntu:~/$ cat my\_file\_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!guillaume@ubuntu:~/$
```
**No test cases needed**



### 4.



Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

*   Prototype: `def write_file(filename="", text=""):`
*   You must use the `with` statement
*   You don’t need to manage file permission exceptions.
*   Your function should create the file if doesn’t exist.
*   Your function should overwrite the content of the file if it already exists.
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
write\_file = \_\_import\_\_('1-write\_file').write\_file

nb\_characters = write\_file("my\_first\_file.txt", "This School is so cool!\\n")
print(nb\_characters)

guillaume@ubuntu:~/$ ./1-main.py
24
guillaume@ubuntu:~/$ cat my\_first\_file.txt
This School is so cool!
guillaume@ubuntu:~/$
```
**No test cases needed**



### 5.



Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

*   Prototype: `def append_write(filename="", text=""):`
*   If the file doesn’t exist, it should be created
*   You must use the `with` statement
*   You don’t need to manage `file permission` or `file doesn't exist` exceptions.
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
append\_write = \_\_import\_\_('2-append\_write').append\_write

nb\_characters\_added = append\_write("file\_append.txt", "This School is so cool!\\n")
print(nb\_characters\_added)

guillaume@ubuntu:~/$ cat file\_append.txt
cat: file\_append.txt: No such file or directory
guillaume@ubuntu:~/$ ./2-main.py
24
guillaume@ubuntu:~/$ cat file\_append.txt
This School is so cool!
guillaume@ubuntu:~/$ ./2-main.py
24
guillaume@ubuntu:~/$ cat file\_append.txt
This School is so cool!
This School is so cool!
guillaume@ubuntu:~/$
```
**No test cases needed**



### 6.



Write a function that returns the JSON representation of an object (string):

*   Prototype: `def to_json_string(my_obj):`
*   You don’t need to manage exceptions if the object can’t be serialized.
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
to\_json\_string = \_\_import\_\_('3-to\_json\_string').to\_json\_string

my\_list = \[1, 2, 3\]
s\_my\_list = to\_json\_string(my\_list)
print(s\_my\_list)
print(type(s\_my\_list))

my\_dict = {
    'id': 12,
    'name': "John",
    'places': \[ "San Francisco", "Tokyo" \],
    'is\_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s\_my\_dict = to\_json\_string(my\_dict)
print(s\_my\_dict)
print(type(s\_my\_dict))

try:
    my\_set = { 132, 3 }
    s\_my\_set = to\_json\_string(my\_set)
    print(s\_my\_set)
    print(type(s\_my\_set))
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

guillaume@ubuntu:~/$ ./3-main.py
\[1, 2, 3\]
<class 'str'>
{"id": 12, "name": "John", "places": \["San Francisco", "Tokyo"\], "is\_active": true, "info": {"age": 36, "average": 3.14}}
<class 'str'>
\[TypeError\] Object of type set is not JSON serializable
guillaume@ubuntu:~/$
```
**No test cases needed**



### 7.



Write a function that returns an object (Python data structure) represented by a JSON string:

*   Prototype: `def from_json_string(my_str):`
*   You don’t need to manage exceptions if the JSON string doesn’t represent an object.
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
from\_json\_string = \_\_import\_\_('4-from\_json\_string').from\_json\_string

s\_my\_list = "\[1, 2, 3\]"
my\_list = from\_json\_string(s\_my\_list)
print(my\_list)
print(type(my\_list))

s\_my\_dict = """
{"is\_active": true, "info": {"age": 36, "average": 3.14},
"id": 12, "name": "John", "places": \["San Francisco", "Tokyo"\]}
"""
my\_dict = from\_json\_string(s\_my\_dict)
print(my\_dict)
print(type(my\_dict))

try:
    s\_my\_dict = """
    {"is\_active": true, 12 }
    """
    my\_dict = from\_json\_string(s\_my\_dict)
    print(my\_dict)
    print(type(my\_dict))
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

guillaume@ubuntu:~/$ ./4-main.py
\[1, 2, 3\]
<class 'list'>
{'id': 12, 'is\_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': \['San Francisco', 'Tokyo'\]}
<class 'dict'>
\[JSONDecodeError\] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
guillaume@ubuntu:~/$
```
**No test cases needed**



### 8.



Write a function that writes an Object to a text file, using a JSON representation:

*   Prototype: `def save_to_json_file(my_obj, filename):`
*   You must use the `with` statement
*   You don’t need to manage exceptions if the object can’t be serialized.
*   You don’t need to manage file permission exceptions.
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
save\_to\_json\_file = \_\_import\_\_('5-save\_to\_json\_file').save\_to\_json\_file

filename = "my\_list.json"
my\_list = \[1, 2, 3\]
save\_to\_json\_file(my\_list, filename)

filename = "my\_dict.json"
my\_dict = {
    'id': 12,
    'name': "John",
    'places': \[ "San Francisco", "Tokyo" \],
    'is\_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save\_to\_json\_file(my\_dict, filename)

try:
    filename = "my\_set.json"
    my\_set = { 132, 3 }
    save\_to\_json\_file(my\_set, filename)
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

guillaume@ubuntu:~/$ ./5-main.py
\[TypeError\] Object of type set is not JSON serializable
guillaume@ubuntu:~/$ cat my\_list.json ; echo ""
\[1, 2, 3\]
guillaume@ubuntu:~/$ cat my\_dict.json ; echo ""
{"name": "John", "places": \["San Francisco", "Tokyo"\], "id": 12, "info": {"average": 3.14, "age": 36}, "is\_active": true}
guillaume@ubuntu:~/$ cat my\_set.json ; echo ""

guillaume@ubuntu:~/$
```
**No test cases needed**



### 9.



Write a function that creates an Object from a “JSON file”:

*   Prototype: `def load_from_json_file(filename):`
*   You must use the `with` statement
*   You don’t need to manage exceptions if the JSON string doesn’t represent an object.
*   You don’t need to manage file permissions / exceptions.
```
guillaume@ubuntu:~/$ cat my\_fake.json
{"is\_active": true, 12 }
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
load\_from\_json\_file = \_\_import\_\_('6-load\_from\_json\_file').load\_from\_json\_file

filename = "my\_list.json"
my\_list = load\_from\_json\_file(filename)
print(my\_list)
print(type(my\_list))

filename = "my\_dict.json"
my\_dict = load\_from\_json\_file(filename)
print(my\_dict)
print(type(my\_dict))

try:
    filename = "my\_set\_doesnt\_exist.json"
    my\_set = load\_from\_json\_file(filename)
    print(my\_set)
    print(type(my\_set))
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

try:
    filename = "my\_fake.json"
    my\_fake = load\_from\_json\_file(filename)
    print(my\_fake)
    print(type(my\_fake))
except Exception as e:
    print("\[{}\] {}".format(e.\_\_class\_\_.\_\_name\_\_, e))

guillaume@ubuntu:~/$ cat my\_list.json ; echo ""
\[1, 2, 3\]
guillaume@ubuntu:~/$ cat my\_dict.json ; echo ""
{"name": "John", "places": \["San Francisco", "Tokyo"\], "id": 12, "info": {"average": 3.14, "age": 36}, "is\_active": true}
guillaume@ubuntu:~/$ cat my\_fake.json ; echo ""
{"is\_active": true, 12 }
guillaume@ubuntu:~/$ ./6-main.py
\[1, 2, 3\]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': \['San Francisco', 'Tokyo'\], 'is\_active': True}
<class 'dict'>
\[FileNotFoundError\] \[Errno 2\] No such file or directory: 'my\_set\_doesnt\_exist.json'
\[JSONDecodeError\] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
guillaume@ubuntu:~/$
```
**No test cases needed**



### 10.



Write a script that adds all arguments to a Python list, and then save them to a file:

*   You must use your function `save_to_json_file` from `5-save_to_json_file.py`
*   You must use your function `load_from_json_file` from `6-load_from_json_file.py`
*   The list must be saved as a JSON representation in a file named `add_item.json`
*   If the file doesn’t exist, it should be created
*   You don’t need to manage file permissions / exceptions.
```
guillaume@ubuntu:~/$ cat add\_item.json
cat: add\_item.json: No such file or directory
guillaume@ubuntu:~/$ ./7-add\_item.py
guillaume@ubuntu:~/$ cat add\_item.json ; echo ""
\[\]
guillaume@ubuntu:~/$ ./7-add\_item.py Best School
guillaume@ubuntu:~/$ cat add\_item.json ; echo ""
\["Best", "School"\]
guillaume@ubuntu:~/$ ./7-add\_item.py 89 Python C
guillaume@ubuntu:~/$ cat add\_item.json ; echo ""
\["Best", "School", "89", "Python", "C"\]
guillaume@ubuntu:~/$
```
**No test cases needed**



### 11.



Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

*   Prototype: `def class_to_json(obj):`
*   `obj` is an instance of a Class
*   All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 8-my\_class.py
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def \_\_init\_\_(self, name):
        self.name = name
        self.number = 0

    def \_\_str\_\_(self):
        return "\[MyClass\] {} - {:d}".format(self.name, self.number)

guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
MyClass = \_\_import\_\_('8-my\_class').MyClass
class\_to\_json = \_\_import\_\_('8-class\_to\_json').class\_to\_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class\_to\_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/$ ./8-main.py
<class '8-my\_class.MyClass'>
\[MyClass\] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 8-my\_class\_2.py
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    score = 0

    def \_\_init\_\_(self, name, number = 4):
        self.\_\_name = name
        self.number = number
        self.is\_team\_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def \_\_str\_\_(self):
        return "\[MyClass\] {} - {:d} => {:d}".format(self.\_\_name, self.number, self.score)

guillaume@ubuntu:~/$ cat 8-main\_2.py
#!/usr/bin/python3
MyClass = \_\_import\_\_('8-my\_class\_2').MyClass
class\_to\_json = \_\_import\_\_('8-class\_to\_json').class\_to\_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class\_to\_json(m)
print(type(mj))
print(mj)

guillaume@ubuntu:~/$ ./8-main\_2.py
<class '8-my\_class\_2.MyClass'>
\[MyClass\] John - 4 => 1
<class 'dict'>
{'number': 4, '\_MyClass\_\_name': 'John', 'is\_team\_red': True, 'score': 1}
guillaume@ubuntu:~/$
```
**No test cases needed**



### 12.



Write a class `Student` that defines a student by:

*   Public instance attributes:
    *   `first_name`
    *   `last_name`
    *   `age`
*   Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
*   Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
Student = \_\_import\_\_('9-student').Student

students = \[Student("John", "Doe", 23), Student("Bob", "Dylan", 27)\]

for student in students:
    j\_student = student.to\_json()
    print(type(j\_student))
    print(j\_student\['first\_name'\])
    print(type(j\_student\['first\_name'\]))
    print(j\_student\['age'\])
    print(type(j\_student\['age'\]))

guillaume@ubuntu:~/$ ./9-main.py
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
guillaume@ubuntu:~/$
```
**No test cases needed**



### 13.



Write a class `Student` that defines a student by: (based on `9-student.py`)

*   Public instance attributes:
    *   `first_name`
    *   `last_name`
    *   `age`
*   Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
*   Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
    *   If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
    *   Otherwise, all attributes must be retrieved
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
Student = \_\_import\_\_('10-student').Student

student\_1 = Student("John", "Doe", 23)
student\_2 = Student("Bob", "Dylan", 27)

j\_student\_1 = student\_1.to\_json()
j\_student\_2 = student\_2.to\_json(\['first\_name', 'age'\])
j\_student\_3 = student\_2.to\_json(\['middle\_name', 'age'\])

print(j\_student\_1)
print(j\_student\_2)
print(j\_student\_3)

guillaume@ubuntu:~/$ ./10-main.py
{'age': 23, 'last\_name': 'Doe', 'first\_name': 'John'}
{'age': 27, 'first\_name': 'Bob'}
{'age': 27}
guillaume@ubuntu:~/$
```
**No test cases needed**



### 14.



Write a class `Student` that defines a student by: (based on `10-student.py`)

*   Public instance attributes:
    *   `first_name`
    *   `last_name`
    *   `age`
*   Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
*   Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
    *   If `attrs` is a list of strings, only attributes name contain in this list must be retrieved.
    *   Otherwise, all attributes must be retrieved
*   Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
    *   You can assume `json` will always be a dictionary
    *   A dictionary key will be the public attribute name
    *   A dictionary value will be the value of the public attribute
*   You are not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
import os
import sys

Student = \_\_import\_\_('11-student').Student
read\_file = \_\_import\_\_('0-read\_file').read\_file
save\_to\_json\_file = \_\_import\_\_('5-save\_to\_json\_file').save\_to\_json\_file
load\_from\_json\_file = \_\_import\_\_('6-load\_from\_json\_file').load\_from\_json\_file

path = sys.argv\[1\]

if os.path.exists(path):
    os.remove(path)

student\_1 = Student("John", "Doe", 23)
j\_student\_1 = student\_1.to\_json()
print("Initial student:")
print(student\_1)
print(type(student\_1))
print(type(j\_student\_1))
print("{} {} {}".format(student\_1.first\_name, student\_1.last\_name, student\_1.age))

save\_to\_json\_file(j\_student\_1, path)
read\_file(path)
print("\\nSaved to disk")

print("Fake student:")
new\_student\_1 = Student("Fake", "Fake", 89)
print(new\_student\_1)
print(type(new\_student\_1))
print("{} {} {}".format(new\_student\_1.first\_name, new\_student\_1.last\_name, new\_student\_1.age))

print("Load dictionary from file:")
new\_j\_student\_1 = load\_from\_json\_file(path)

new\_student\_1.reload\_from\_json(j\_student\_1)
print(new\_student\_1)
print(type(new\_student\_1))
print("{} {} {}".format(new\_student\_1.first\_name, new\_student\_1.last\_name, new\_student\_1.age))

guillaume@ubuntu:~/$ ./11-main.py student.json
Initial student:
<11-student.Student object at 0x7f832826eda0>
<class '11-student.Student'>
<class 'dict'>
John Doe 23
{"last\_name": "Doe", "first\_name": "John", "age": 23}
Saved to disk
Fake student:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
Fake Fake 89
Load dictionary from file:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
John Doe 23
guillaume@ubuntu:~/$ cat student.json ; echo ""
{"last\_name": "Doe", "first\_name": "John", "age": 23}
guillaume@ubuntu:~/$
```
**No test cases needed**



### 15.



**Technical interview preparation**:

*   You are not allowed to google anything
*   Whiteboard first

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

*   Returns an empty list if `n <= 0`
*   You can assume `n` will be always an integer
*   You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
"""
12-main
"""
pascal\_triangle = \_\_import\_\_('12-pascal\_triangle').pascal\_triangle

def print\_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("\[{}\]".format(",".join(\[str(x) for x in row\])))

if \_\_name\_\_ == "\_\_main\_\_":
    print\_triangle(pascal\_triangle(5))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./12-main.py
\[1\]
\[1,1\]
\[1,2,1\]
\[1,3,3,1\]
\[1,4,6,4,1\]
guillaume@ubuntu:~/$
```
