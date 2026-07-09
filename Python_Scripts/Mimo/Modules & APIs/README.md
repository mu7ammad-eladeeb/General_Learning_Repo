# Python Module Aliasing (Using the `as` Keyword)

> **Source:** Mimo Core Curriculum Progress Notes

------------------------------------------------------------------------

## 📖 CONCEPT OVERVIEW: WHAT IS ALIASING?

Aliasing means giving a **temporary new name** to a module that you are
importing. Instead of using its full, long name throughout your code,
you use a shorter, custom nickname (**an alias**).

The primary tool for this is the `as` keyword.

------------------------------------------------------------------------

# 🔥 REASON 1: MAKING LONG NAMES SHORTER (Readability & Speed)

Standard modules like `statistics` can feel repetitive and clutter your
code. Aliasing lets you write cleaner syntax.

``` python
import statistics as stats  # Re-assigns 'statistics' to 'stats'

ids = [33, 123, 22, 798, 23, 33]
sales = [23, 43, 26, 26, 29, 18, 24]

calculated_mode = stats.mode(ids)
calculated_median = stats.median(sales)

print("--- Reason 1: Shorter Names ---")
print(f"Dataset Mode: {calculated_mode}")      # Expected Output: 33
print(f"Dataset Median: {calculated_median}")  # Expected Output: 26
print()
```

### Why?

-   Makes code shorter.
-   Improves readability.
-   Reduces repetition.

------------------------------------------------------------------------

# 🛡️ REASON 2: PREVENTING NAME CLASHES (Namespace Protection)

If you create a variable with the same name as an imported module,
Python will overwrite the module reference. Aliasing prevents this
problem.

``` python
import math as math_constants  # Renamed so 'math' remains free for variables

math = "Grade 12 constants"

print("--- Reason 2: Preventing Overwrite Errors ---")
print(f"Local String Variable: {math}")
print(f"Safe Module Constant Pi: {math_constants.pi}")
print(f"Safe Module Constant e:  {math_constants.e}")
print()
```

### Benefits

-   Prevents overwrite errors.
-   Protects the imported module.
-   Lets you freely use descriptive variable names.

------------------------------------------------------------------------

# 🧮 PRACTICAL APPLICATION: COMBINING ALIASING WITH FUNCTIONS

``` python
import math as m

# floor rounding always drops down to the nearest whole integer value
floored_value = m.floor(44.32)

print("--- Practical Application: math as m ---")
print(f"Value 44.32 floor-rounded is: {floored_value}")  # Expected Output: 44
```

------------------------------------------------------------------------

# 💡 QUICK REFRESHER SUMMARY

### Q: What is using the `as` keyword with a module known as?

**A:** Aliasing.

### Q: Why do we use it?

1.  To make code shorter and faster to write.
2.  To prevent imported modules from interfering with our local
    variables.

### Syntax Pattern

``` python
import [original_module_name] as [short_alias]
```
# Python Modules (Part 2)

> Source: Mimo Core Curriculum Progress Notes

------------------------------------------------------------------------

# 📥 Renaming a Module (Aliasing)

A module can be renamed using the **`as`** keyword.

## Syntax

``` python
import module_name as alias
```

### Example

``` python
import statistics as stats
```

Instead of:

``` python
statistics.mean(data)
```

Use:

``` python
stats.mean(data)
```

**Why use `as`?**

-   Makes code shorter.
-   Makes code easier to read.
-   Prevents name clashes.

------------------------------------------------------------------------

# 📦 Importing Parts of a Module

Import only the functionality you need.

``` python
from module import function
```

Example:

``` python
from math import sqrt

print(sqrt(25))
```

Output:

    5.0

------------------------------------------------------------------------

# 📚 Importing Multiple Modules

``` python
import statistics, math

total_plays = [232, 43, 345, 35]
```

------------------------------------------------------------------------

# ⚠️ Common Import Error

Incorrect:

``` python
import

equation = "User defined"
print(math.sqrt(100))
```

Reason: the `import` statement is unfinished.

Correct:

``` python
import math

equation = "User defined"
print(math.sqrt(100))
```

------------------------------------------------------------------------

# ❓ The `help()` Function

Displays documentation for a module.

``` python
import math

help(math)
```

------------------------------------------------------------------------

# 📥 Installing Libraries

Install third-party libraries before importing them.

``` bash
pip install torch
```

Then:

``` python
import torch
```

------------------------------------------------------------------------

# 🔍 Finding Available Modules

Read the library's **official documentation** to learn:

-   Available modules
-   Functions
-   Classes
-   Installation instructions
-   Usage examples

------------------------------------------------------------------------

# 🎯 Importing Only One Function

``` python
from time import sleep

print("This message is shown immediately.")

sleep(1)

print("This message is shown after a 1-second delay.")
```

Output:

    This message is shown immediately.
    This message is shown after a 1-second delay.

------------------------------------------------------------------------

# 🧠 Summary

## Import a module

``` python
import math
```

Use:

``` python
math.sqrt(25)
```

## Import with an alias

``` python
import statistics as stats
```

Use:

``` python
stats.mean(data)
```

## Import a single function

``` python
from time import sleep
```

Use:

``` python
sleep(1)
```

------------------------------------------------------------------------

# 📋 Quick Review

  -----------------------------------------------------------------------
  Question                            Answer
  ----------------------------------- -----------------------------------
  How do we rename a module?          Using `as`

  How do we import only part of a     `from ... import ...`
  module?                             

  How do we import multiple modules?  `import module1, module2`

  What's wrong with `import` alone?   It is incomplete.

  What does `help()` do?              Displays documentation.

  What must be done before importing  Install them first.
  third-party libraries?              

  How do we know what modules a       Read the official documentation.
  library has?                        

  How do we import only one function? `from module import function`
  -----------------------------------------------------------------------
# Python Modules: Importing, Aliasing, and the math Module

This section covers how to import built-in modules (module = a file containing pre-written Python code you can reuse), use specific functions from them, and give them shorter names (aliases) for convenience.

---

## Importing a Module

To use functions from Python's built-in `math` module (a module containing mathematical functions and constants), you import it first:

```python
import math
```

Once imported, you access its functions using dot notation (dot notation = accessing something inside an object using a period, like `module.function`), e.g., `math.sqrt()`, `math.ceil()`.

---

## Example: math.sqrt()

```python
import math
print(math.sqrt(10000))
```

**Output:**
```
100.0
```

`math.sqrt()` returns the square root (square root = the number that, when multiplied by itself, gives the original number) of a number. Note that the result is always a float (float = a number with a decimal point), even if the answer is a whole number — this is correct behavior, not a bug.

---

## Example: math.ceil()

```python
import math
print(math.ceil(65.9))
```

**Output:**
```
66
```

`math.ceil()` rounds a number **up** (ceil = short for "ceiling," meaning the nearest whole number equal to or greater than the given value) to the nearest integer (integer = a whole number, no decimals), regardless of how small the decimal part is.

---

## Importing Multiple Modules at Once

You can import more than one module in a single line by separating them with commas:

```python
import statistics, math

number_of_cases = [2, 2, 4, 5]
result = statistics.mean(number_of_cases)
print(f"Mean cases: {result}")
```

**Output:**
```
Mean cases: 3.25
```

`statistics.mean()` calculates the average (mean = the sum of all values divided by how many there are) of a list of numbers.

---

## Importing Specific Functionality with `from`

Instead of importing an entire module, you can import just one specific piece of it using the `from` keyword:

```python
from math import pi
print(pi)
```

**Output:**
```
3.141592653589793
```

The `from` keyword allows you to import parts of a module's functionality (rather than the whole module), so you can call `pi` directly instead of writing `math.pi`.

---

## Aliasing Modules (Giving Modules a Shorter Name)

Aliasing (aliasing = giving something an alternate, usually shorter, name) is done using the `as` keyword. This is useful for modules with long names that you'll reference often.

```python
import statistics as stats
```

Now `stats` can be used anywhere you'd normally write `statistics`.

### Another Example:

```python
import math as mths
```

This renames the `math` module to `mths` for the rest of the script (script = a Python file containing a sequence of instructions).

---

## Key Takeaways

1. `import module_name` — imports an entire module.
2. `import module_one, module_two` — imports multiple modules in one line.
3. `from module_name import function_name` — imports only a specific function or constant (constant = a fixed value that doesn't change, like `pi`) from a module, letting you call it directly without the module prefix (prefix = the module name written before the dot, like `math.`).
4. `import module_name as alias` — renames a module to a shorter or more convenient name using the `as` keyword. This process is called **aliasing**.


markdown_content = """# Python Syntax Errors: A Complete Guide

> A comprehensive guide to understanding, identifying, and fixing Python `SyntaxError` and `IndentationError`.


## What is a SyntaxError?

Sometimes Python is unable to understand our code. This results in something called a **`SyntaxError`**.

When Python encounters code it cannot parse, it stops execution and displays an error message in the console pointing to where the problem occurred.

---

## Common Causes of SyntaxError

### 1. Misspelled Keywords

Syntax errors are usually due to typos, such as misspelled keywords.

**Example:** Using `iff` instead of `if` at the beginning of a code block.

```python
# ❌ Incorrect
iff cost > 10:
```

**Output:**
```
File "script.py", line 1
  iff cost > 10
      ^
SyntaxError: invalid syntax
```

**Fix:** Always double-check keyword spelling. Python keywords include: `if`, `else`, `elif`, `for`, `while`, `def`, `class`, `return`, `import`, etc.

---

### 2. Incorrect or Missing Indentation

Incorrect or missing indentation will result in an **`IndentationError`**, which is a specific type of `SyntaxError`.

**Example:** Missing indentation after an `if` statement.

```python
# ❌ Incorrect
if cost > 10:
print("Too expensive.")
```

**Output:**
```
File "script.py", line 2
  print("Too expensive.")
  ^
IndentationError: expected an indented block
```

**Fix:** Always indent the block of code under a colon (`:`) by 4 spaces (or 1 tab, consistently).

```python
# ✅ Correct
if cost > 10:
    print("Too expensive.")
```

---

### 3. Keywords in Wrong Places

Putting a keyword in the wrong place will also cause a `SyntaxError`.

**Example:** Using `for` incorrectly inside a list literal.

```python
# ❌ Incorrect
* 1 for item in [1, 2, 3]
```

**Output:**
```
File "script.py", line 1
  * 1 for item in [1, 2, 3]
      ^
SyntaxError: invalid syntax
```

**Fix:** Ensure keywords are used in their proper syntactic context.

---

### 4. Incomplete Statements

If we try to run incomplete statements, we'll also receive a `SyntaxError`.

**Example:** An `if` statement without a body.

```python
# ❌ Incorrect
if cost > 10:
```

**Output:**
```
File "script.py", line 2

  ^
SyntaxError: unexpected EOF while parsing
```

> **EOF** stands for "End of File." This error means Python reached the end of the file while still expecting more code.

**Fix:** Complete all statements with proper blocks or use `pass` as a placeholder.

```python
# ✅ Correct
if cost > 10:
    pass  # placeholder for future code
```

---

### 5. Missing Symbols (Colons, Brackets)

Leaving out symbols, such as colons and brackets, will also cause a `SyntaxError`.

**Example:** Missing colon (`:`) after an `if` condition.

```python
# ❌ Incorrect
if cost < 10
  print('You can buy it.')
```

**Output:**
```
File "script.py", line 1
  if cost < 10
              ^
SyntaxError: invalid syntax
```

**Fix:** Always include required punctuation:
- Colon (`:`) after `if`, `else`, `elif`, `for`, `while`, `def`, `class`, `try`, `except`
- Matching brackets `()`, `[]`, `{}`

```python
# ✅ Correct
if cost < 10:
    print('You can buy it.')
```

---

### 6. Using Strings as Variable Names

Sometimes Python can add more detail to the error, like in the following code where a string is mistakenly used as a variable name.

**Example:** Trying to assign a value to a string literal.

```python
# ❌ Incorrect
"name" = "John"
```

**Output:**
```
File "script.py", line 1
  "name" = "John"
  ^
SyntaxError: can't assign to literal
```

**Fix:** Variable names must not be quoted strings.

```python
# ✅ Correct
name = "John"
```

---

### 7. Assigning to Function Calls

Similarly, you cannot assign a value to a function call.

**Example:** Trying to assign to `len()`.

```python
# ❌ Incorrect
len('Happy Birthday') = 6
```

**Output:**
```
File "script.py", line 1
  len('Happy Birthday') = 6
                        ^
SyntaxError: can't assign to function call
```

**Fix:** Use variables to store results, not function calls.

```python
# ✅ Correct
length = len('Happy Birthday')
```

---

## Understanding Error Messages

The **`^`** symbol, known as a **caret**, indicates in the console where the error has been found in the code.

```
File "script.py", line 1
  len('Happy Birthday') = 6
                        ^
SyntaxError: can't assign to function call
```

> **Tip:** The caret points to the exact location where Python detected the syntax violation. Always read the error message carefully — it tells you the file, line number, and type of error.

---

## Knowledge Check: Quiz

Test your understanding with these questions:

### Question 1
**Which statement will result in a SyntaxError?**

```python
age = 16
```
```python
while age < 11:    # ❌ SyntaxError: expected an indented block after 'while' statement
```

> **Answer:** `wile age < 11:` — Misspelled keyword.

---

### Question 2
**What error will appear if there are extra blank spaces in the code?**

- `Indentation Error` ✅
- `Syntax Error`

> **Answer:** `Indentation Error` — Extra or inconsistent whitespace causes indentation issues.

---

### Question 3
**Which statement will result in a SyntaxError?**

```python
print("help")
```
```python
else print("hello")    # ❌ SyntaxError: 'else' without matching 'if'
```

> **Answer:** `else print("hello")` — `else` must follow an `if` block.

---

### Question 4
**Which statement will result in a SyntaxError?**

```python
total = 5 + 3 + 8
```
```python
total = 5 + 3  8    # ❌ SyntaxError: invalid syntax (missing operator)
```

> **Answer:** `total = 5 + 3  8` — Missing operator between `3` and `8`.

---

### Question 5
**Which error will the following code produce?**

```python
if 75 > 50:
```

- `SyntaxError: can't assign to literal`
- `SyntaxError: unexpected EOF while parsing` ✅

> **Answer:** `SyntaxError: unexpected EOF while parsing` — The `if` statement is incomplete (missing body).

---

### Question 6
**Which character in an error message can help us work out where the error in the code is?**

- A hashtag `#`
- A caret `^` ✅

> **Answer:** A caret `^` — It points directly to the error location.

---

## Hands-On Exercises

### Exercise 1: Fix the If Statement

**Task:** Add an `if` statement that does not result in a `SyntaxError`.

```python
attendance = 11
if attendance > 10:
    print("We are full.")
```

**Output:**
```
We are full.
```

---

### Exercise 2: Fix the Indentation

**Task:** Complete the `print()` statement and avoid an `IndentationError`.

```python
values = [2, 8, 7]
for value in values:
    print(value)
```

**Output:**
```
2
8
7
```

---

### Exercise 3: Write a Valid Conditional

**Task:** Code a statement which does not result in an error.

```python
apples = 5
oranges = 1
if apples < 3 or oranges < 3:
    print("low stock")
```

**Output:**
```
low stock
```

---

### Exercise 4: Complete the Calculation

**Task:** Complete this statement without producing a `SyntaxError`.

```python
bill = 50 * 1.2
print(bill)
```

**Output:**
```
60.0
```

---

### Exercise 5: Complete the Code to Print a Value

**Task:** Complete the code so that `value` is printed.

```python
value = 50
if value >= 20:
    print(value)
```

**Output:**
```
50
```

---

### Exercise 6: Produce a Specific SyntaxError

**Task:** Complete the code so that an error is produced in the console.

```python
"david" = name
```

**Output:**
```
File "script.py", line 1
  "david" = name
  ^
SyntaxError: can't assign to literal
```

---

### Exercise 7: Produce an EOF Error

**Task:** Complete the code to produce a `SyntaxError`.

```python
users = ["Alan", "Betty", "Clara"]
if "Betty" in users:
```

**Output:**
```
File "script.py", line 3

  ^
SyntaxError: unexpected EOF while parsing
```

---

## Quick Reference Table

| Error Type | Common Cause | Example Fix |
|---|---|---|
| `SyntaxError: invalid syntax` | Misspelled keyword | `if` not `iff` |
| `IndentationError` | Missing/extra indentation | Indent block after `:` |
| `SyntaxError: unexpected EOF while parsing` | Incomplete statement | Add body after `if`/`for`/`while` |
| `SyntaxError: can't assign to literal` | String used as variable | `name = "John"` not `"name" = "John"` |
| `SyntaxError: can't assign to function call` | Assigning to function result | `x = len(s)` not `len(s) = x` |
| Missing colon | Forgot `:` after condition | `if x > 5:` |
| Missing operator | Two values without operator | `5 + 3 + 8` not `5 + 3  8` |

---

## Summary

- **SyntaxError** occurs when Python cannot parse your code.
- **IndentationError** is a specific type of syntax error related to whitespace.
- The **caret (`^`)** in error messages points to the exact location of the issue.
- Common causes include: typos, missing colons, bad indentation, incomplete statements, and invalid assignments.
- Always read error messages carefully — they tell you the **file**, **line number**, and **type of error**.

---

# Python Exceptions: A Complete Guide

> A comprehensive guide to understanding Python exceptions, tracebacks, and common runtime errors.

---

## What Are Exceptions?

Sometimes Python understands our code, but cannot execute it. When Python cannot perform an operation, it raises an **exception**.

Python will raise an **exception** when it cannot perform an operation. It will show one for the given code since a variable isn't defined.

---

## Understanding the Traceback

The text shown in the console when an exception is raised is called the **traceback**. It helps us **debug** our code, which means finding errors.

A typical traceback looks like this:

```
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    share = 100 / 0
ZeroDivisionError: division by zero
```

> **Tip:** Always read the traceback from bottom to top. The last line tells you the error type and message, while the lines above show where it occurred.

---

## Common Exception Types

### ZeroDivisionError

Raised when you try to divide a number by zero.

**Example:**

```python
# ❌ Incorrect
share = 100 / 0
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    share = 100 / 0
ZeroDivisionError: division by zero
```

**Fix:** Always check that the denominator is not zero before dividing.

```python
# ✅ Correct
divisor = 0
if divisor != 0:
    share = 100 / divisor
else:
    print("Cannot divide by zero!")
```

---

### NameError

Raised when you try to use a variable that doesn't exist or hasn't been defined.

**Example 1:** Using an undefined variable in an expression.

```python
# ❌ Incorrect
share = size / 6
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    share = size / 6
NameError: name "size" is not defined
```

**Example 2:** Referencing a variable that doesn't exist in a loop.

```python
# ❌ Incorrect
for student in ["Mark", "Andreas", "Irina"]:
    score = results[student]
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 2, in <module>
    score = results[student]
NameError: name "results" is not defined
```

**Fix:** Define all variables before using them.

```python
# ✅ Correct
size = 120
share = size / 6

results = {"Mark": 85, "Andreas": 92, "Irina": 78}
for student in ["Mark", "Andreas", "Irina"]:
    score = results[student]
```

---

### KeyError

Raised when you try to access a dictionary key that doesn't exist.

**Example:**

```python
# ❌ Incorrect
details = {"name": "Pablo",
           "age": 27}

details["email"]
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 4, in <module>
    details["email"]
KeyError: "email"
```

**Fix:** Use `.get()` to safely access dictionary keys, or check if the key exists first.

```python
# ✅ Correct
details = {"name": "Pablo", "age": 27}

# Method 1: Using .get() (returns None if key doesn't exist)
email = details.get("email")

# Method 2: Check if key exists
if "email" in details:
    print(details["email"])
else:
    print("Email not found")
```

---

### TypeError

Raised when an operation is performed on an inappropriate type.

**Example:** Adding a string and an integer.

```python
# ❌ Incorrect
"3" + 1
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    "3" + 1
TypeError: must be str, not int
```

**Fix:** Convert types before performing operations.

```python
# ✅ Correct
# Convert int to str for concatenation
result = "3" + str(1)  # "31"

# Or convert str to int for arithmetic
result = int("3") + 1  # 4
```

> **`ZeroDivisionError`**, **`NameError`**, and **`TypeError`** are examples of different types of exceptions.

---

### FileNotFoundError

Raised when trying to open a file that doesn't exist.

**Example:**

```python
# ❌ Incorrect
with open("myfile.txt"):
    print(file)
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    with open("myfile.txt"):
FileNotFoundError: [Errno 2] No such file or directory: "myfile.txt"
```

**Fix:** Check if the file exists before opening, or handle the exception.

```python
# ✅ Correct
import os

if os.path.exists("myfile.txt"):
    with open("myfile.txt") as file:
        print(file.read())
else:
    print("File not found!")
```

> We'll encounter many types of exceptions when creating programs, relating to things such as indexing, file references, and variables.

---

### AttributeError

Raised when you try to access an attribute or method that doesn't exist for an object.

**Example:** Calling a `.mean()` method on a list (lists don't have this method).

```python
# ❌ Incorrect
scores = [25, 70, 45]
scores.mean()
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 2, in <module>
    scores.mean()
AttributeError: "list" object has no attribute "mean"
```

**Fix:** Use the correct method or import the appropriate module.

```python
# ✅ Correct
import statistics

scores = [25, 70, 45]
average = statistics.mean(scores)
print(average)
```

> Objects may not have attributes or methods that we think they have, like using a mean function that does not exist for lists.

---

## Safe Operations That Don't Raise Exceptions

Some methods don't produce errors and are able to handle issues themselves.

**Example:** The `.count()` method returns zero when the item doesn't exist in the list.

```python
# ✅ Safe - no exception raised
grades = ["A", "B", "C"]
print(grades.count("D"))
```

**Output:**
```
0
```

> The `count()` method returns zero when nothing exists — it doesn't raise an error.

---

## Knowledge Check: Quiz

### Question 1
**Which type of exception will this code raise?**

```python
print("Hello, " + user)
```

- `TypeError`
- `NameError` ✅

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    print("Hello, " + user)
NameError: name "user" is not defined
```

> **Answer:** `NameError` — The variable `user` is not defined.

---

### Question 2
**Which of the following will result in a `NameError`?**

- Using a string which is very long as a variable name
- Referencing a variable that doesn't exist ✅

> **Answer:** Referencing a variable that doesn't exist — `NameError` occurs when Python cannot find the variable name in the current scope.

---

### Question 3
**Will this code raise an exception?**

```python
users = ["Alex", "Ben", "Chelsea"]
if "Diane" in users:
    print("User found")
```

- Yes, using `in` in this context produces an error
- No, as using `in` on the list where the value isn't present does not cause an error ✅

> **Answer:** No exception — The `in` operator safely returns `False` when the value isn't found. It does not raise an error.

---

## Hands-On Exercises

### Exercise 1: Raise a ZeroDivisionError

**Task:** Code a statement which will raise a `ZeroDivisionError`.

```python
average = 100 / 0
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    average = 100 / 0
ZeroDivisionError: division by zero
```

---

### Exercise 2: Raise a NameError

**Task:** Code a statement which will raise a `NameError`.

```python
users = ["Alice", "Barbara"]
members.append("Kevin")
```

**Output:**
```
Traceback (most recent call last):
  File "script.py", line 2, in <module>
    members.append("Kevin")
NameError: name "members" is not defined
```

> The variable `members` was never defined — only `users` was.

---

### Exercise 3: Print False Without Raising an Exception

**Task:** Add a statement which prints `False`, without raising an exception.

```python
print("Paris" in ["London", "New York", "France"])
```

**Output:**
```
False
```

> The `in` operator safely checks membership and returns `False` when the item is not found.

---

## Quick Reference Table

| Exception | Cause | Example Fix |
|---|---|---|
| `ZeroDivisionError` | Division by zero | Check divisor `!= 0` |
| `NameError` | Variable not defined | Define variable before use |
| `KeyError` | Dictionary key not found | Use `.get()` or check `in` |
| `TypeError` | Wrong type for operation | Convert types with `int()`, `str()` |
| `FileNotFoundError` | File doesn't exist | Check `os.path.exists()` |
| `AttributeError` | Method/attribute doesn't exist | Use correct method or import module |

---

## Summary

- **Exceptions** occur when Python understands the code but cannot execute it.
- The **traceback** is the error message shown in the console — it helps us **debug** our code.
- Common exceptions include: `ZeroDivisionError`, `NameError`, `KeyError`, `TypeError`, `FileNotFoundError`, and `AttributeError`.
- Some operations are **safe** and don't raise exceptions (e.g., `.count()` returns `0` instead of error).
- The `in` operator is safe for checking membership in lists — it returns `False` rather than raising an error.

---

