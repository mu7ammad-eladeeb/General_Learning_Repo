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
