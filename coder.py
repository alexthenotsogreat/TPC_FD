from image_to_byte import image_to_byte
from byte_to_image import bytes_to_image
from e7_4_encoder import cyclic_code_encoder
from decoder_7_4 import cyclic_code_decoder
import numpy as np
from chanel import change_array
import os


def clear_console():
    os.system('cls')


def encoding(data_array, output_file):
    ##ENCODES
    for i in range(0, len(data), 4):
        subarray = data_array[i:i+4]  # Get a subarray of 4 elements
        returned_array = cyclic_code_encoder(subarray)  # Call the place_holder function and get the returned array
        returned_arrays.extend(returned_array)

    with open(output_file, "w") as file: 
        file.write(str(returned_arrays))
    return returned_arrays

def decoding(returned_arrays):
    ##DECODES
    for i in range(0, len(returned_arrays), 7):
        subarray2 = returned_arrays[i:i+7]  # Get a subarray of 4 elements
        returned_array2 = cyclic_code_decoder(subarray2)  # Call the place_holder function and get the returned array
        returned_arrays2.extend(returned_array2)

    return returned_arrays2

returned_arrays = []
returned_arrays2 = []
option = 0

while option != '3':
    option = input("Escolha a opçao:\n 1: Encode\n 2: Decode\n 3: Sair")
    if option =='1':
        ##Calls encoding
        file = input("Qual o caminho para o ficheiro de imagem: ")
        output_file = input("Qual será o ficheiro de output: ")
        data=image_to_byte(file)
        data_array = [int(char) for char in data]
        returned_arrays = encoding(data_array,output_file)
        
    if option =='2':
        ##Calls decoding
        input_file = input("Qual o caminho para o ficheiro a ser descodificado: ")
        with open(input_file, "r") as file: 
            keeper=file.read()
            keeper = keeper.replace("[", "").replace("]", "").replace(",", "").replace("'","").replace(" ","")
            returned_arrays = [int(x) for x in keeper]

        BER = float(input("Qual o valor do BER (menor que 1, p.e 1/25), 0 para saltar: "))
        if BER != 0:
            returned_arrays = change_array(returned_arrays,BER)

        
        returned_arrays2 = decoding(returned_arrays)
        
        out_file = input("Qual o nome do ficheiro para output da imagem: ")
        ##Converts to image again
        result_string = ''.join(map(str, returned_arrays2))
        bytes_to_image(result_string,out_file)

    if option =='4':
        break

    clear_console()













