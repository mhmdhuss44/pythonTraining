
# i will implement a simple hash table with simple functions:

class hash_table:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size

    # we need a hash function of course , we use this one
    # we want a hash function to do a good distrbution - less collistions
    def hash_function(self, key):
        return hash(key) % self.size

    # this method is used to delete a value from hash table
    def delete_from_table(self,value):
        index=self.hash_function(value)
        if self.table[index] is not None:
            for i,temp in enumerate(self.table[index]):
                if temp==value:
                    self.table[index].remove(value)

                    break
    # we return true if the searched value is inside our hash table
    def search_hash(self,value):
        index = self.hash_function(value)
        if self.table[index] is not None:
            for i,temp in enumerate(self.table[index]):
                if temp==value:
                    return True
        else:
            return False


    def insert_hash(self,value):
        index = self.hash_function(value)
        if self.table[index] is None:
            self.table[index] = [value]
        #     we handle coliisions by just appending
        else:
            self.table[index].append(value)

if __name__ == '__main__':
    # Create a hash table with a size of 10
    my_hash_table = hash_table(10)

    # Insert values into the hash table
    values_to_insert = [15, 25, 35, 45, 55,14]
    for value in values_to_insert:
        my_hash_table.insert_hash(value)

    # Print the hash table
    print("Hash Table:")
    for i, bucket in enumerate(my_hash_table.table):
        print(f"Bucket {i}: {bucket}")


# Search for values in the hash table
    values_to_search = [25, 40, 55, 60]
    for value in values_to_search:
        if my_hash_table.search_hash(value):
            print(f"{value} is in the hash table.")
        else:
            print(f"{value} is not in the hash table.")

    # Delete values from the hash table
    values_to_delete = [25, 40, 55, 60]
    for value in values_to_delete:
        my_hash_table.delete_from_table(value)

    # Print the hash table after deletion
    print("\nHash Table after Deletion:")
    for i, bucket in enumerate(my_hash_table.table):
        print(f"Bucket {i}: {bucket}")

