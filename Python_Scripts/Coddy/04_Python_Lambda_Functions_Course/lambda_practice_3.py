# ==============================================================================
# Platform: Coddy.tech
# Topic: Python Lambda Functions - Practice #3 (Medium)
# 
# Challenge Description:
# Write a lambda function that receives a list of integers and returns the 
# median value of the list. The median is the middle value in a sorted list, 
# or the average of the two middle values if the list has an even number of elements.
# 
# Constraints:
# - Assign the lambda function to a variable named 'median'.
# - Don't use 'def'!
# ==============================================================================

# ==============================================================================
# 🧠 SOLUTION EXPLANATION (FOR QUICK REVIEW)
# ==============================================================================
# The single-line lambda expression works by evaluating two branches:
#
# 1. THE INPUT PROCESSING:
#    - sorted(l): Ensures the list elements are in numerical order first.
#    - len(l) // 2: Uses floor division to find the exact middle index index.
#
# 2. THE ODD LENGTH CONDITION (True branch):
#    - Syntax: `sorted(l)[len(l)//2] if len(l) % 2 == 1`
#    - If a list has an odd length (e.g., 5 items), 5 // 2 yields index 2. 
#      Index 2 is the exact central element (e.g., [0, 1, *2*, 3, 4]).
#
# 3. THE EVEN LENGTH CONDITION (False branch):
#    - Syntax: `else (sorted(l)[len(l)//2] + sorted(l)[(len(l)//2) - 1]) / 2`
#    - If a list has an even length (e.g., 6 items), 6 // 2 yields index 3.
#      The two middle elements sit at index 3 and index 2 (which is index 3 - 1).
#      The formula adds these two elements together and divides by 2 to find the average.
# ==============================================================================

# --- SOLUTION ---
median = lambda l: sorted(l)[len(l)//2] if len(l) % 2 == 1 else (sorted(l)[len(l)//2] + sorted(l)[(len(l)//2) - 1]) / 2


# --- LOCAL VERIFICATION AND TESTS ---
if __name__ == "__main__":
    print("--- Running Test Cases ---")
    
    # Test 1: Even length (6 elements) -> Sorted: [4, 5, 7, 8, 9, 10] -> Mid average: (7 + 8) / 2 = 7.5
    test_1 = [10, 5, 8, 7, 9, 4]
    print(f"Test 1: {test_1} | Median: {median(test_1)}")
    
    # Test 2: Odd length (5 elements) -> Sorted: [1, 2, 3, 4, 5] -> Mid: 3
    test_2 = [2, 1, 5, 4, 3]
    print(f"Test 2: {test_2} | Median: {median(test_2)}")
    
    # Test 3: Even length (6 elements) -> Sorted: [3, 4, 7, 8, 15, 19] -> Mid average: (7 + 8) / 2 = 7.5
    test_3 = [15, 7, 4, 19, 3, 8]
    print(f"Test 3: {test_3} | Median: {median(test_3)}")
    
    # Test 4: Even length (10 elements) -> Sorted: [1, 2, 4, 5, 7, 9, 12, 25, 50, 100] -> Mid average: (7 + 9) / 2 = 8.0
    test_4 = [100, 5, 2, 7, 9, 12, 4, 1, 50, 25]
    print(f"Test 4: {test_4} | Median: {median(test_4)}")
    
    # Test 5: Even length (4 elements) -> Sorted: [10, 20, 30, 40] -> Mid average: (20 + 30) / 2 = 25.0
    test_5 = [10, 20, 30, 40]
    print(f"Test 5: {test_5} | Median: {median(test_5)}")
