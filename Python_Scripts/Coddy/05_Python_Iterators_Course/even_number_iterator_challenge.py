class EvenNumberIterator:
    """
    A custom iterator that generates even numbers up to a specified limit.
    """
    def __init__(self, limit):
        # Start generating numbers from 2 (current initialized to 0, adds 2 on first next call)
        self.current = 0
        self.limit = limit

    def __iter__(self):
        # An iterator must return itself in its __iter__ method
        return self

    def __next__(self):
        # Generate the next even number
        self.current += 2
        
        # Stop when the current value exceeds the specified limit
        if self.current > self.limit:
            raise StopIteration
            
        return self.current

if __name__ == "__main__":
    # This block allows the script to be executed directly in the terminal
    print("--- Even Number Iterator Solution ---")
    print("Enter the maximum limit integer:")
    
    try:
        # Read user input and convert it to an integer
        user_input = input()
        limit = int(user_input)
        
        # Create the iterator instance
        even_iterator = EvenNumberIterator(limit)
        
        print(f"\nEven numbers up to {limit}:")
        # Loop through the iterator until StopIteration is raised
        while True:
            print(next(even_iterator))
            
    except StopIteration:
        # Gracefully exit the loop when iteration finishes
        pass
    except ValueError:
        print("Error: Please provide a valid integer string as input.")
