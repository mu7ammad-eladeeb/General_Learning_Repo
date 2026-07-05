# Python Learning Notes — Part 3 (OOP & Design Patterns)

## Table of Contents
- [OOP Fundamentals](#oop-fundamentals)
- [Attributes & Methods](#attributes--methods)
- [Encapsulation & Access Control](#encapsulation--access-control)
- [Properties & Decorators](#properties--decorators)
- [Inheritance](#inheritance)
- [Polymorphism & Duck Typing](#polymorphism--duck-typing)
- [Abstract Classes & Interfaces](#abstract-classes--interfaces)
- [Magic Methods & Operator Overloading](#magic-methods--operator-overloading)
- [Advanced OOP](#advanced-oop)
- [Design Patterns](#design-patterns)

---

## OOP Fundamentals

### What Is OOP? (البرمجة الكائنية التوجه — أسلوب برمجة يُنظّم الكود حول كائنات تحتوي على بيانات وسلوكيات)
```python
class Car:
    pass  # placeholder (عنصر نائب — لا يفعل شيئاً، يُستخدم لتعريف كلاس فارغ)

my_car = Car()           # Create an object (كائن — نسخة من الكلاس)
print(type(my_car))      # <class 'car.Car'>
```

### Importing a Class
```python
from filename import ClassName

# Example
from my_class import MyClass
obj = MyClass("Alice")
print(obj.greet())
```

### Class vs Object (الكلاس مقابل الكائن)
```python
class Dog:
    species = "Canis familiaris"   # Class attribute (خاصية الكلاس — مشتركة بين جميع الكائنات)

# Create objects (instances — نسخ من الكلاس)
dog1 = Dog()
dog2 = Dog()

# Add individual attributes (خصائص فردية — فريدة لكل كائن)
dog1.name = "Nicky"
dog1.breed = "Siberian Husky"

print(dog1.name)       # Individual attribute
print(Dog.species)     # Class attribute
```

---

## Attributes & Methods

### self Parameter (المعامل الذاتي — يُشير إلى نسخة الكائن الحالية داخل الكلاس)
```python
class Car:
    def honk(self):
        print("Beep beep!")

    def describe(self):
        print(f"I am a {self.color} {self.model}")

my_car = Car()
my_car.color = "Red"
my_car.model = "Sedan"
my_car.honk()        # Beep beep!
my_car.describe()    # I am a Red Sedan
```

> Always include `self` as the first parameter — never pass it when calling methods.

### Methods (الدوال — وظائف تنتمي إلى الكلاس)
```python
class Calculator:
    def greet(self):
        print("Hello! I'm a calculator.")

    def add(self, a, b):
        return a + b

    def multiply(self, x, y):
        result = x * y
        print(f"{x} × {y} = {result}")
        return result

my_calc = Calculator()
my_calc.greet()
sum_result = my_calc.add(5, 3)
product = my_calc.multiply(4, 7)
```

### Attributes (الخصائص — البيانات المرتبطة بالكلاس أو الكائن)
```python
class Student:
    school_name = "Python Academy"     # Class attribute (خاصية الكلاس)

    def set_info(self, name, age):
        self.name = name               # Instance attribute (خاصية الكائن — فريدة لكل نسخة)
        self.age = age

student1 = Student()
student1.set_info("Alice", 20)
print(student1.name)          # Alice
print(Student.school_name)    # Python Academy
```

### __init__ Constructor (المُنشئ — يُنفَّذ تلقائياً عند إنشاء كائن جديد لتهيئة خصائصه)
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

rex = Dog("Rex", "German Shepherd")
print(rex.name)    # Rex
print(rex.breed)   # German Shepherd
```

**With default values (قيم افتراضية):**
```python
class Cat:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

fluffy = Cat("Fluffy", 3)
whiskers = Cat("Whiskers")   # age defaults to 1
```

### Class vs Instance Variables
```python
class Student:
    school = "Python High School"    # Class variable (متغير الكلاس — مشترك بين جميع الكائنات)

    def __init__(self, name, grade):
        self.name = name             # Instance variable (متغير الكائن — فريد لكل نسخة)
        self.grade = grade

alice = Student("Alice", "A")
bob = Student("Bob", "B")

print(alice.school)     # Python High School
print(bob.school)       # Python High School

Student.school = "Python Academy"   # Affects ALL instances
print(alice.school)     # Python Academy
```

### Static Methods (الدوال الساكنة — لا تحتاج إلى self أو cls)
```python
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Call from class or instance
result = MathHelper.add(5, 3)
check = MathHelper.is_even(10)
```

### Class Methods (دوال الكلاس — تستقبل الكلاس نفسه كأول معامل عبر cls)
```python
class Student:
    school_name = "Python Academy"
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1

    @classmethod
    def get_school_info(cls):
        return f"School: {cls.school_name}, Students: {cls.student_count}"

    @classmethod
    def create_guest_student(cls):
        return cls("Guest")

info = Student.get_school_info()
guest = Student.create_guest_student()
```

**Three Method Types Summary:**
| Type | Decorator | First Param | Accesses |
|------|-----------|-------------|----------|
| Instance method | None | `self` | Instance data |
| Class method | `@classmethod` | `cls` | Class data |
| Static method | `@staticmethod` | None | Neither |

---

## Encapsulation & Access Control

### Access Levels (مستويات الوصول — تحديد من يمكنه الوصول إلى خصائص الكلاس)
```python
class BankAccount:
    def __init__(self, owner, balance, account_id):
        self.owner = owner              # Public (عام — متاح للجميع)
        self._balance = balance         # Protected (محمي — للاستخدام الداخلي فقط)
        self.__account_id = account_id  # Private (خاص — للكلاس فقط، يتم تشويه اسمه)
```

**Accessing each level:**
```python
account = BankAccount("Alice", 1000, "12345")

print(account.owner)                       # ✅ Public — works fine
print(account._balance)                    # ⚠️ Protected — works but discouraged
print(account._BankAccount__account_id)   # ⚠️ Private — name mangled (تشويه الاسم — آلية تُصعّب الوصول المباشر) but accessible
# print(account.__account_id)            # ❌ AttributeError
```

**In subclasses (الكلاسات الفرعية):**
```python
class SavingsAccount(BankAccount):
    def show_balance(self):
        return self._balance            # ✅ Protected accessible

    def show_id(self):
        # return self.__account_id    # ❌ Private not accessible
        return "Cannot access private"
```

### Information Hiding (إخفاء المعلومات — تقييد الوصول المباشر للبيانات)
```python
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._balance = initial_balance
        self.__account_number = "ACC123456"

    # Controlled access through public methods
    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
```

---

## Properties & Decorators

### Basic Decorator (المُزيِّن — يُعدِّل أو يُحسِّن دوالاً بدون تغيير كودها الأصلي)
```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator        # Equivalent to: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")
```

### @property — Getter (قارئ الخاصية — يُتيح الوصول للبيانات الخاصة بصيغة خاصية عادية)
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

my_circle = Circle(5)
print(my_circle.radius)  # Access like attribute, no parentheses
print(my_circle.area)    # Computed property (خاصية محسوبة — تُحسب تلقائياً)
```

### @property with Setter (كاتب الخاصية — يُتيح تعديل البيانات مع التحقق منها)
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

person = Person("Alice", 30)
person.age = 31    # Uses setter with validation (تحقق — التأكد من صحة البيانات)
```

### Full Property (getter + setter + deleter)
```python
class Temperature:
    def __init__(self):
        self._temp = 0

    @property
    def temperature(self):
        return self._temp

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._temp = value

    @temperature.deleter
    def temperature(self):
        print("Resetting temperature to 0")
        self._temp = 0

temp = Temperature()
temp.temperature = 25     # Setter
print(temp.temperature)   # Getter
del temp.temperature      # Deleter
```

### Class Decorators (مُزيِّنات الكلاس — تُعدِّل الكلاسات بإضافة دوال أو تغيير سلوكها)
```python
# Adding a method to a class
def add_farewell(cls):
    def farewell(self):
        return f"Goodbye from {self.name}"
    cls.farewell = farewell
    return cls

@add_farewell
class EnhancedPerson:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

person = EnhancedPerson("Alice")
print(person.greet())    # Hello, my name is Alice
print(person.farewell()) # Goodbye from Alice
```

**Wrapping an existing method (تغليف دالة موجودة — تعديل سلوكها دون حذفها):**
```python
def loud_greet(cls):
    original_greet = cls.greet    # Step 1: Save original

    def new_greet(self):
        result = original_greet(self)  # Step 2: Call original
        return result.upper()          # Step 3: Enhance result

    cls.greet = new_greet    # Step 4: Replace on class
    return cls
```

### Private Attributes with Properties
```python
class Person:
    def __init__(self, name, age):
        self.__name = name    # Private (خاص)
        self.__age = age

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age must be positive!")

person = Person("Bob", 25)
print(person.get_name())    # Bob
person.set_age(30)
# print(person.__name)      # ❌ AttributeError
print(person._Person__name) # ⚠️ Works but discouraged
```

---

## Inheritance

### Basic Inheritance (الوراثة — يرث الكلاس الفرعي خصائص ودوال الكلاس الأب)
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am {self.name}, an animal")

class Dog(Animal):
    pass    # Inherits everything from Animal

buddy = Dog("Buddy")
buddy.info()    # Uses inherited method
```

**Adding methods to child class:**
```python
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

buddy = Dog("Buddy")
buddy.info()    # Inherited method
buddy.bark()    # New method
```

### Method Overriding (تجاوز الدوال — يُعيد الكلاس الفرعي تعريف دوال الكلاس الأب)
```python
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")    # Overrides parent method

class Cat(Animal):
    def make_sound(self):
        print("Meow!")
```

### super() — Extending Parent Functionality (توسيع وظائف الكلاس الأب بدلاً من استبدالها)
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # Call parent's __init__
        self.breed = breed

    def make_sound(self):
        super().make_sound()      # Call parent's method first
        print("Woof!")            # Add child-specific behavior
```

### Multiple Inheritance (الوراثة المتعددة — الوراثة من أكثر من كلاس أب)
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

class Flyable:
    def fly(self):
        return f"{self.name} is flying"

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

sparrow = Bird("Sparrow", "House sparrow")
print(sparrow.eat())    # From Animal
print(sparrow.fly())    # From Flyable
print(Bird.__mro__)     # Show inheritance order
```

### Method Resolution Order — MRO (ترتيب تحليل الدوال — تسلسل البحث عن الدوال عند الوراثة المتعددة)
```python
class C(A, B):
    pass

print(C.__mro__)    # Python searches: C → A → B

c = C()
c.method()    # Uses A's method (A comes before B)
```

### Composition vs Inheritance (التركيب مقابل الوراثة)
```python
# Inheritance — "is-a" relationship (علاقة "هو نوع من")
class Dog(Animal):
    pass

# Composition — "has-a" relationship (علاقة "يحتوي على")
class Car:
    def __init__(self):
        self.engine = Engine()    # Car "has an" Engine

    def start(self):
        return self.engine.start()
```

| | Inheritance | Composition |
|---|---|---|
| Relationship | "is-a" | "has-a" |
| Coupling (الترابط) | Tight (محكم) | Loose (مرن) |
| Flexibility | Less | More |
| Best for | True hierarchies | Most other cases |

### Mixins (الخلطات — وراثة متعددة لإضافة وظائف محددة قابلة لإعادة الاستخدام)
```python
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class PrintableMixin:
    def pretty_print(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

class ComparableMixin:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

# Combine multiple mixins
class Product(JSONSerializableMixin, PrintableMixin, ComparableMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

> Mixins are NOT meant to be instantiated (إنشاء كائن مستقل) on their own. Names often end with "Mixin" or "able".

---

## Polymorphism & Duck Typing

### Polymorphism (تعدد الأشكال — تتصرف كائنات مختلفة بشكل مختلف عند استدعاء نفس الدالة)
```python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())   # Each prints different output

# Polymorphic function (دالة تتعامل مع كائنات مختلفة بنفس الطريقة)
def make_animal_speak(animal):
    print(animal.speak())
```

### Duck Typing (الكتابة البطية — إذا كان الكائن يحتوي على الدوال المطلوبة، يمكن استخدامه بغض النظر عن نوعه)
```python
class Duck:
    def swim(self):
        return "Duck swimming"
    def quack(self):
        return "Quack!"

class Person:
    def swim(self):
        return "Person swimming"
    def quack(self):
        return "Person imitating a duck: Quack!"

# Works with ANY object that has swim() and quack()
def make_it_swim_and_quack(duck_like_object):
    print(duck_like_object.swim())
    print(duck_like_object.quack())

make_it_swim_and_quack(Duck())
make_it_swim_and_quack(Person())
```

> "If it walks like a duck and quacks like a duck, it's a duck." — Python follows: "it's easier to ask forgiveness than permission."

---

## Abstract Classes & Interfaces

### Abstract Classes (الكلاسات المجردة — لا يمكن إنشاء كائن منها مباشرةً، وتُلزم الكلاسات الفرعية بتنفيذ دوال معينة)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return "This is a shape"    # Concrete method (دالة منفَّذة — لها كود فعلي)

# shape = Shape()   # ❌ TypeError: Can't instantiate abstract class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print(circle.area())        # 78.5
print(circle.describe())    # Inherited concrete method
```

### Interfaces Using Abstract Classes (الواجهات — تُعرِّف ما يجب أن تفعله الكلاسات دون تحديد كيفية ذلك)
```python
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, width, height):
        pass

class Circle(Drawable):
    def draw(self):
        return "Drawing a circle"

    def resize(self, width, height):
        self.radius = min(width, height) / 2

# Use interfaces as type hints (تلميحات النوع — لتوضيح نوع المعامل المتوقع)
def render_shape(drawable: Drawable):
    return drawable.draw()

# Use polymorphically
shapes = [Circle(5), Rectangle(3, 4)]
for shape in shapes:
    print(shape.draw())
```

---

## Magic Methods & Operator Overloading

### Common Magic Methods (الدوال السحرية — دوال ذات شرطتين تُستدعى تلقائياً عند عمليات معينة)
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):      # Called by str() or print()
        return f"{self.title} by {self.author}"

    def __len__(self):      # Called by len()
        return self.pages

my_book = Book("Python Programming", "John Smith", 350)
print(my_book)          # Calls __str__ automatically
print(len(my_book))     # Calls __len__ automatically
```

### Operator Overloading (تحميل المعاملات الزائد — تعريف سلوك المعاملات الحسابية للكلاسات المخصصة)
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):     # + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):     # - operator
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):    # * operator
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):      # == operator
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)
result = v1 + v2     # Calls v1.__add__(v2)
scaled = v1 * 3      # Calls v1.__mul__(3)
print(v1 == v2)      # Calls v1.__eq__(v2)
```

### Container Magic Methods (دوال سحرية للحاويات — تجعل الكائن يتصرف كقائمة أو قاموس)
```python
class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):    # Enable indexing for retrieval
        return self.items[index]

    def __setitem__(self, index, value):    # Enable indexing for assignment
        self.items[index] = value

    def __iter__(self):     # Enable iteration (التكرار)
        return iter(self.items)

    def __contains__(self, item):    # Enable `in` operator
        return item in self.items

my_list = CustomList([1, 2, 3, 4])
print(len(my_list))    # 4
print(my_list[2])      # 3
print(3 in my_list)    # True
for item in my_list:
    print(item)
```

---

## Advanced OOP

### *args (معامل النجمة — يجمع أي عدد من الوسائط الموضعية في صف)
```python
class Calculator:
    def add_numbers(self, *args):
        return sum(args)

calc = Calculator()
calc.add_numbers(1, 2, 3)         # 6
calc.add_numbers(10, 20, 30, 40)  # 100

# Combine with regular params
class Logger:
    def log_message(self, level, *messages):
        print(f"[{level}]", end=" ")
        for message in messages:
            print(message, end=" ")

# Unpack a list when calling
numbers = [1, 2, 3, 4, 5]
result = calc.add_numbers(*numbers)   # Unpacks the list
```

### **kwargs (معامل النجمتين — يجمع أي عدد من الوسائط بالكلمات الرئيسية في قاموس)
```python
class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        self.details = kwargs

    def show_info(self):
        print(f"Name: {self.name}")
        for key, value in self.details.items():
            print(f"{key}: {value}")

person = Person("Alice", age=25, city="New York", job="Engineer")

# Unpack dictionary when calling
settings = {"debug": True, "verbose": False, "log_level": "INFO"}
config = Config(**settings)

# Combine all parameter types
class Logger:
    def log(self, level, *messages, **options):
        timestamp = options.get('timestamp', False)
        color = options.get('color', 'default')
```

### Context Managers (مديرو السياق — يضمنون تنظيف الموارد تلقائياً حتى عند حدوث أخطاء)
```python
# Using built-in context manager
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
    # File is automatically closed here

# Custom context manager
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        return False    # Don't suppress (تجاهل) exceptions

with MyContext() as ctx:
    print("Inside the context")
```

**__exit__ parameters:**
| Parameter | Meaning |
|-----------|---------|
| `exc_type` | Exception type (نوع الاستثناء) or None |
| `exc_val` | Exception value (قيمة الاستثناء) or None |
| `exc_tb` | Exception traceback (مسار الخطأ) or None |

---

## Design Patterns

### What Are Design Patterns? (أنماط التصميم — حلول جاهزة وقابلة لإعادة الاستخدام لمشاكل شائعة في البرمجة)

| Category | Examples |
|----------|---------|
| **Creational (إنشائية — تتحكم في كيفية إنشاء الكائنات)** | Singleton, Factory |
| **Structural (هيكلية — تتحكم في كيفية تركيب الكائنات)** | Adapter, Decorator, Composite |
| **Behavioral (سلوكية — تتحكم في كيفية تفاعل الكائنات)** | Observer, Strategy, Command, State, Template Method |

---

### Singleton Pattern (نمط الفردي — يضمن وجود نسخة واحدة فقط من الكلاس)
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)   # True — same object

# Practical example
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to MySQL database"
        return cls._instance

    def query(self, sql):
        return f"Executing: {sql}"
```

> Use Singleton for: database connections, loggers, configuration managers — anything that should have only ONE copy.

---

### Factory Pattern (نمط المصنع — ينشئ الكائنات دون تحديد الكلاس المستخدم بشكل مباشر)
```python
class VehicleFactory:
    def create_vehicle(self, vehicle_type, brand):
        if vehicle_type == "car":
            return Car(brand)
        elif vehicle_type == "bike":
            return Bike(brand)
        else:
            raise ValueError(f"Unknown type: {vehicle_type}")

factory = VehicleFactory()
my_car = factory.create_vehicle("car", "Toyota")
my_bike = factory.create_vehicle("bike", "Honda")

# Flexible factory with *args
class FlexibleFactory:
    def create_vehicle(self, vehicle_type, *args):
        if vehicle_type == "car":
            return Car(args[0])
        elif vehicle_type == "truck":
            return Truck(args[0], args[1])
```

---

### Observer Pattern (نمط المراقب — علاقة واحد-لكثيرين، يُخطر كائن واحد عدة كائنات عند تغيير حالته)
```python
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class EmailNotifier:
    def update(self, message):
        print(f"Email sent: {message}")

class SMSNotifier:
    def update(self, message):
        print(f"SMS sent: {message}")

news = Subject()
news.add_observer(EmailNotifier())
news.add_observer(SMSNotifier())
news.notify("Breaking news: Python is awesome!")
```

---

### Strategy Pattern (نمط الاستراتيجية — يُعرِّف عائلة من الخوارزميات القابلة للتبديل وقت التشغيل)
```python
class CreditCard:
    def pay(self, amount):
        return f"Paid ${amount} with Credit Card"

class PayPal:
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class ShoppingCart:
    def __init__(self):
        self.total = 0
        self.payment_strategy = None

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def checkout(self):
        return self.payment_strategy.pay(self.total)

cart = ShoppingCart()
cart.set_payment_strategy(CreditCard())
print(cart.checkout())

cart.set_payment_strategy(PayPal())   # Switch strategy at runtime
print(cart.checkout())
```

---

### Command Pattern (نمط الأمر — يُغلِّف الطلب ككائن، ويدعم التراجع عن العمليات)
```python
class Light:
    def turn_on(self):
        print("Light is on")
    def turn_off(self):
        print("Light is off")

class LightOnCommand:
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.turn_on()
    def undo(self):
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.last_command = None

    def execute_command(self, command):
        command.execute()
        self.last_command = command

    def undo(self):
        if self.last_command:
            self.last_command.undo()

light = Light()
remote = RemoteControl()
remote.execute_command(LightOnCommand(light))
remote.undo()
```

---

### Adapter Pattern (نمط المحوِّل — يجعل الواجهات غير المتوافقة تعمل معاً)
```python
class OldPrinter:
    def old_print(self, text):
        return f"OLD: {text}"

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, text):
        return self.old_printer.old_print(text)   # Adapt old interface to new

def print_document(printer, text):
    return printer.print(text)

adapter = PrinterAdapter(OldPrinter())
print(print_document(adapter, "Hello"))   # OLD: Hello
```

---

### Decorator Pattern (نمط المُزيِّن — يُضيف وظائف جديدة للكائنات ديناميكياً بدون تغيير بنيتها)
```python
class Coffee:
    def cost(self):
        return 5
    def description(self):
        return "Simple coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() + 2
    def description(self):
        return self.coffee.description() + " + Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() + 1
    def description(self):
        return self.coffee.description() + " + Sugar"

# Chain decorators (تسلسل المُزيِّنات)
my_coffee = Coffee()
my_coffee = MilkDecorator(my_coffee)
my_coffee = SugarDecorator(my_coffee)
print(f"{my_coffee.description()}: ${my_coffee.cost()}")
# Output: Simple coffee + Milk + Sugar: $8
```

---

### Composite Pattern (نمط المركّب — يُعامل الكائنات الفردية ومجموعات الكائنات بشكل موحَّد)
```python
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def display(self):
        return f"File: {self.name} ({self.size}KB)"

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def get_size(self):
        return sum(child.get_size() for child in self.children)

    def display(self):
        result = f"Folder: {self.name}"
        for child in self.children:
            result += f"\n  {child.display()}"
        return result

# Build tree structure (هيكل شجري — ترتيب هرمي)
file1 = File("document.txt", 10)
documents = Folder("Documents")
root = Folder("Root")
documents.add(file1)
root.add(documents)
print(root.display())
```

---

### State Pattern (نمط الحالة — يُغيِّر سلوك الكائن عند تغيير حالته الداخلية)
```python
class RedState:
    def next_state(self, light):
        light.state = GreenState()
    def current_color(self):
        return "Red"

class GreenState:
    def next_state(self, light):
        light.state = YellowState()
    def current_color(self):
        return "Green"

class TrafficLight:
    def __init__(self):
        self.state = RedState()

    def change(self):
        self.state.next_state(self)

    def get_color(self):
        return self.state.current_color()

light = TrafficLight()
print(light.get_color())   # Red
light.change()
print(light.get_color())   # Green
```

---

### Template Method Pattern (نمط الدالة النموذجية — يُحدِّد هيكل الخوارزمية في الكلاس الأب، ويترك تفاصيل معينة للكلاسات الفرعية)
```python
class DataProcessor:
    def process(self):
        """Template method (الدالة النموذجية) — defines algorithm structure"""
        self.read_data()
        self.process_data()
        self.save_data()

    def read_data(self):
        print("Reading data...")

    def process_data(self):
        raise NotImplementedError("Subclasses must implement this")

    def save_data(self):
        print("Saving data...")

class CSVProcessor(DataProcessor):
    def process_data(self):
        print("Processing CSV data")

class JSONProcessor(DataProcessor):
    def process_data(self):
        print("Processing JSON data")

csv_processor = CSVProcessor()
csv_processor.process()
```
