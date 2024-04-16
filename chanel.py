import random

def change_array(array, ratio):
    # Calculate the number of positions to change based on the ratio
    num_positions = int(len(array) * ratio)
    
    # Select random indices to change
    indices_to_change = random.choices(range(len(array)), k=num_positions)
    # Update the array at the selected indices
    for index in indices_to_change:
        array[index] = 1

    return array
