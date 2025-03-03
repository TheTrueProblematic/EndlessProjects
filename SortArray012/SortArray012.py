
# Hey there, happy programmer!!
# Welcome to the SortArray012 project!
# This teeny-tiny script will sort an array of 0s, 1s, and 2s.
# All this without any external libraries or dependencies, just funktastic python!

# We start with defining our function, appropriately named sort_array, that takes our lovely array as an input. 
def sort_array(input_array):
    # Oh brilliant python's list count function! Let’s count 0s, 1s, and 2s. 
    # I mean, who doesn't love a good counting exercise?
    count_0 = input_array.count(0)
    count_1 = input_array.count(1)
    count_2 = input_array.count(2)

    # Now that we're done counting, lets start citing. Yes, I meant citing 0s, 1s, and 2s, in order!
    sorted_array = [0]*count_0 + [1]*count_1 + [2]*count_2

    # Alas! We have a sorted array! Let's not keep it to ourselves, return it :)
    return sorted_array

# Oh ho! Time to test this little marvel! Let's get an array of 0s, 1s, and 2s all jumbled up! Mystery, excitement, trilling!  
def test_sort_array():
    test_array = [2, 0, 1, 2, 1, 0, 0, 1, 2, 0, 1]
    print(f"Original array: {test_array}")

    # And the moment of truth arrives when we call our sort_array function on our jumbled array.
    sorted_array = sort_array(test_array)
    
    print(f"Sorted array: {sorted_array}")

# Let's ensure that this script can also act like a stand-alone player, I mean, it should be executable on its own, right?
if __name__ == "__main__":
    # Let's call our test function to start the magic!
    test_sort_array()

