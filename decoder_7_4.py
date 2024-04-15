from e7_4_encoder import cyclic_code_encoder
import numpy as np

def pad_array4(arr):
    padded_arr = [0] * (4 - len(arr)) + arr
    return padded_arr

def pad_array3(arr):
    padded_arr = [0] * (3 - len(arr)) + arr
    return padded_arr

def cyclic_code_decoder(received_message):
    # Define generator polynomial: x^3 + x^2 + 1
    if len(received_message)<7:
        received_message= pad_array7(received_message)
    
    generator_polynomial = np.poly1d([1, 1, 0, 1])
    received_message_t = np.poly1d(received_message).c

    # Calculate syndrome vector by dividing received message by generator polynomial
    r, syndrome = np.polydiv(received_message_t, generator_polynomial)

    for j in range(0,len(r.coefficients)):
        if r.coefficients[j]%2 == 0:
            r.coefficients[j] = 0
        else:
            r.coefficients[j] = 1

    for j in range(0,len(syndrome.coefficients)):
        if syndrome.coefficients[j]%2 == 0:
            syndrome.coefficients[j] = 0
        else:
            syndrome.coefficients[j] = 1

    abs_syndrome = [int(abs(num)) for num in syndrome.coefficients]
    abs_syndrome = pad_array3(abs_syndrome)
    # Define syndrome lookup table
    syndrome_lookup = {
        (0, 0, 0): 0,  # No error
        (0, 0, 1): 7,  # Error in position 7
        (0, 1, 0): 6,  # Error in position 6
        (1, 0, 0): 5,  # Error in position 5
        (1, 0, 1): 4,  # Error in position 4
        (1, 1, 1): 3,  # Error in position 3
        (0, 1, 1): 2,  # Error in position 2
        (1, 1, 0): 1   # Error in position 1
    }
    # Lookup error position
    error_position = syndrome_lookup.get(tuple(abs_syndrome))
    

    # Correct errors if possible
    if error_position != -1:
        
        if error_position != 0:  # No error if error_position is 0

            received_message[error_position-1] ^= 1
            received_message_t = np.poly1d(received_message).c
            r, syndrome = np.polydiv(received_message_t, generator_polynomial)

            for j in range(0,len(r.coefficients)):
                if r.coefficients[j]%2 == 0:
                    r.coefficients[j] = 0
                else:
                    r.coefficients[j] = 1

    
    abs_rec = [int(abs(num)) for num in r.coefficients]
    abs_rec = pad_array4(abs_rec)
    return abs_rec


