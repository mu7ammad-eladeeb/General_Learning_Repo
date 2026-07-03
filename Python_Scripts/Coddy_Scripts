# ==============================================================================
# Challenge: Python Lambda Functions - Practice #2 (Coddy)
# Description: Write a lambda function assigned to 'sum_bigger' that receives a 
#              list of tuples (three integers each) and returns a list containing 
#              only the sums of the tuples that are strictly greater than 20.
# Constraints: Do not use standard function definitions (def keyword).
# ==============================================================================

# ==============================================================================
# 🧠 QUICK REFERENCE: HOW THIS SOLUTION WORKS
# ==============================================================================
# Code line: sum_bigger = lambda lst: list(filter(lambda summ: summ > 20, map(sum, lst)))
#
# PIPELINE STEP-BY-STEP breakdown using input: [(1, 2, 3), (10, 11, 12)]
#
# 🛠️ Step 1: map(sum, lst)
#    - Loops through the parent list 'lst' element by element.
#    - Passes each tuple into Python's built-in sum() function.
#    - Transformation: (1,2,3) -> 6   and   (10,11,12) -> 33
#    - Output at this stage: [6, 33]
#
# 🛠️ Step 2: filter(lambda summ: summ > 20, ...)
#    - Checks the fresh list of sums one by one using a temporary variable 'summ'.
#    - Keeps items where the condition (summ > 20) evaluates to True.
#    - Evaluation: Is 6 > 20? (False, dropped) | Is 33 > 20? (True, kept)
#    - Output at this stage: [33]
#
# 🛠️ Step 3: list(...)
#    - Wraps around the filter operation to extract the matching data out of
#      memory and cast it back into a standard Python list format.
# ==============================================================================

# One-line optimized solution combining map and filter pipelines
sum_bigger = lambda lst: list(filter(lambda summ: summ > 20, map(sum, lst)))


# ==============================================================================
# TEST CASES (Local Verification Environment)
# ==============================================================================
if __name__ == "__main__":
    print("--- Running Coddy Practice #2 Test Cases ---")

    # Test Case 1 | Expected Output: [24, 33]
    tc1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    print(f"Test #1 Output: {sum_bigger(tc1)}")

    # Test Case 2 | Expected Output: [21, 27]
    tc2 = [(2, 8, 11), (1, 7, 12), (5, 5, 10), (9, 9, 9)]
    print(f"Test #2 Output: {sum_bigger(tc2)}")

    # Test Case 3 | Expected Output: [25, 30, 25]
    tc3 = [(5, 15, 5), (10, 10, 10), (20, 0, 5), (2, 4, 6)]
    print(f"Test #3 Output: {sum_bigger(tc3)}")

    # Test Case 4 | Expected Output: []
    tc4 = [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3)]
    print(f"Test #4 Output: {sum_bigger(tc4)}")
    
    print("--------------------------------------------")
