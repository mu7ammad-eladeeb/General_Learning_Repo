# Python Module Aliasing (Using the `as` Keyword)

## Concept Overview

Aliasing means giving a temporary new name (an alias) to an imported
module using the `as` keyword.

## Syntax

``` python
import module_name as alias
```

## Reason 1: Making Long Names Shorter

``` python
import statistics as stats
ids=[33,123,22,798,23,33]
sales=[23,43,26,26,29,18,24]
calculated_mode=stats.mode(ids)
calculated_median=stats.median(sales)
```

Benefits: - Less typing - Cleaner code - Better readability

## Reason 2: Preventing Name Clashes

``` python
import math as math_constants
math='Grade 12 constants'
print(math_constants.pi)
print(math_constants.e)
```

Benefits: - Prevents overwriting imported modules. - Allows local
variables to use common names.

## Practical Application

``` python
import math as m
floored_value=m.floor(44.32)
print(floored_value)
```

Output: `44`

## Summary

-   Aliasing = using `as` to rename an imported module.
-   Reasons:
    1.  Shorter code.
    2.  Prevent name conflicts.

Pattern:

``` python
import original_module as alias
```
