# Initial dictionary containing key-value pairs
data = {
    'John' : 89,
    'Mike' : 91,
    'Angela': 85,
}

def insert_data(key, value):
    try:
        # Attempt to insert or update the key-value pair in the dictionary
        data[key] = value
    except TypeError:
        # Catch exception if key is mutable (e.g., a list) and cannot be hashed
        print("Cannot give mutable keys")
    else:
        # Executes if no exception occurred; prints the newly inserted value
        print(data[key])
    finally:
        # Always executes regardless of exceptions; prints the dictionary state
        print(data)
