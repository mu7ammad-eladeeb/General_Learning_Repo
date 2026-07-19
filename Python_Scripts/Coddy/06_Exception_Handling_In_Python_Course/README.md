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

# Exception vs Error

There are two types of errors in Python:

1.  **Syntax Error (Compile-Time Error)**
2.  **Exception (Run-Time Error)**

## Syntax Error

If the code you write doesn't follow Python syntax and rules, the
interpreter will raise a **SyntaxError**. These errors cannot be
handled.

**Example:**

``` python
print("Hello World"))
```

The above program raises a **SyntaxError** because of an unmatched
parenthesis. You need to fix it before the program can run successfully.

## Exception

An **Exception** occurs because of logical errors, runtime problems, or
invalid inputs. To avoid sudden termination of a program, exceptions can
be handled using **Exception Handling** concepts.

# try-except

The **try-except** block in Python is used to catch and handle
exceptions.

## Basic Structure

``` python
try:
    statement_1
    # statements that can cause an error
    statement_3
except [ExceptionName]:
    # code for exception handling
```

## How It Works

-   Python executes the code inside the `try` block.
-   If an exception occurs, execution immediately jumps to the `except`
    block.
-   The remaining statements in the `try` block are skipped.
-   If no exception occurs, the entire `try` block executes
    successfully, and the `except` block is skipped.

## try Block

Contains code where an exception may occur.

## except Block

Contains the code that handles the exception if it occurs.

## Example

``` python
try:
    a = int(input())
    b = int(input())
    div = a / b
    print("Division is:", div)
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Rest of code")
```

## Explanation

-   The program runs normally if the user enters a non-zero value for
    `b`.
-   If the user enters `0` for `b`, the expression `a / b` raises a
    `ZeroDivisionError`.
-   Control immediately moves to the `except` block, which prints:

``` text
Cannot divide by zero
```

-   After handling the exception, the program continues executing the
    remaining code and prints:

``` text
Rest of code
```

Using `try-except` prevents the program from terminating unexpectedly
when an exception occurs.
