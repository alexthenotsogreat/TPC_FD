from image_to_byte import image_to_byte
from byte_to_image import bytes_to_image
from e7_4_encoder import cyclic_code_encoder
from decoder_7_4 import cyclic_code_decoder
import numpy as np
from chanel import change_array


data=image_to_byte("ber.jpg")


data_array = [int(char) for char in data]

returned_arrays = []

returned_arrays2 = []

##ENCODES
for i in range(0, len(data), 4):
    subarray = data_array[i:i+4]  # Get a subarray of 4 elements
    returned_array = cyclic_code_encoder(subarray)  # Call the place_holder function and get the returned array
    returned_arrays.extend(returned_array)


returned_arrays = change_array(returned_arrays,1/2500)

#print(returned_arrays[1])
#print(returned_arrays[2])
#returned_arrays[7]=0
#returned_arrays[1]=1
#returned_arrays[2]=0

##DECODES
for i in range(0, len(returned_arrays), 7):
    subarray2 = returned_arrays[i:i+7]  # Get a subarray of 4 elements
    returned_array2 = cyclic_code_decoder(subarray2)  # Call the place_holder function and get the returned array
    returned_arrays2.extend(returned_array2)





result_string = ''.join(map(str, returned_arrays2))

bytes_to_image(result_string)



