from public.hash import hashs

# Implement a merkle tree here
# Use the hash functions you built

# Important emphasis- you should always save your merkle in the DataBase after changing it!!!
class MerkleTree:
    def __init__(self):
        pass

    # Add a new vertex to the tree
    # What is the functions' complexity?
    def add_data(self, data):
        pass

    # Get the merkle root
    # This function gets called quit a lot. Make sure it's complexity is O(1)!
    def get_root(self):
        pass

    # Get an existance proof for some user (in which variable type should you export the proof? list? dictionary? json? set? tuple?)
    # How should the function act if the user doesn't exists?
    # How can you implement this function in minimal complexity? What is this complexity?
    def get_proof(self, data):
        pass


