import base64 


def image_to_byte(path):
  
    with open(path, "rb") as image2string: 
        converted_string = base64.b64encode(image2string.read()) 
     
  
    with open('encode.bin', "wb") as file: 
        file.write(converted_string)


    decoded = base64.decodebytes(converted_string)

    


    y=''.join([bin(i)[2:].zfill(8) for i in decoded])

    with open('binary.txt', "w") as file: 
        file.write(y)

    return y
