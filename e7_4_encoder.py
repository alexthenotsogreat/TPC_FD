def cyclic_code_encoder(data):
    # Define generator polynomial: x^3 + x^2 + 1
    generator_polynomial = [1, 1, 0, 1]
    #print(data)
    # Initialize the encoded message with zeros
    encoded_message = [0] * 7

    # Copy the original data into the encoded message
       
    # Perform cyclic encoding
    for i in range(4):
        # Perform modulo-2 addition with the generator polynomial
        if data[i] == 1:
            for j in range(len(generator_polynomial)):
                encoded_message[(i + j) % 7] ^= generator_polynomial[j] * data[i]


    #print(encoded_message)
    return encoded_message




