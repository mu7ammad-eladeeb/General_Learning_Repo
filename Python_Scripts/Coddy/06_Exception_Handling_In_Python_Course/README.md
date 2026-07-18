# What is an Exception?

An **Exception** is an error that occurs **during the execution** of a program.

Even if your code is **syntactically correct**, it may encounter an unexpected situation while running (such as invalid operations, missing variables, or running out of memory). When this happens, the Python interpreter **raises an exception** and, unless it is handled, the program stops execution.

---

## Example 1: `TypeError`

```python
a = 10
b = "Hii"

print(a + b)   # TypeError
print("Rest of Code")
```

### Explanation

- Here, we are trying to add an **integer** (`a`) and a **string** (`b`).
- Python does **not** allow addition between different data types.
- For the `+` operator, both operands must be of compatible types.
- Therefore, Python stops execution and raises a **`TypeError`**.
- The line:

```python
print("Rest of Code")
```

is **not executed**.

---

## Example 2: `NameError`

```python
MY_NAME = "Mike"

print(my_name)   # NameError
```

### Explanation

- The variable `MY_NAME` exists.
- However, we are trying to print `my_name`, which has **not** been defined.
- Since Python cannot find a variable with that exact name, it raises a **`NameError`**.

---

## Notes

> **Note 1:** Python is a **case-sensitive** language.

This means:

```python
MY_NAME != my_name
```

They are treated as two completely different variable names.

> **Note 2:** Both example programs are **syntactically correct**.

The errors occur **during execution**, not while parsing the code. Therefore, they are called **Exceptions** rather than syntax errors.

---

## Key Points

- **Exceptions** are errors that occur **during program execution**.
- A program can be **syntactically correct** and still raise exceptions.
- When an exception is not handled, Python **terminates the program**.
- Examples of exceptions:
  - `TypeError`
  - `NameError`
  - `ValueError`
  - `IndexError`
  - `KeyError`
  - `ZeroDivisionError`
