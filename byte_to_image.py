import struct
import base64
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

from PIL import Image


def bytes_to_image(binary_string,out_file):

    binary_bytes = int(binary_string, 2).to_bytes((len(binary_string) + 7) // 8, byteorder='big')

    
    encoded_base64 = base64.b64encode(binary_bytes)
    
    with open(out_file, "wb") as fh:
        fh.write(base64.decodebytes(encoded_base64))
        fh.close()
        
    last_dot_index = out_file.rfind('.')
    if last_dot_index != -1:
        out_file_txt = out_file[:last_dot_index]
    out_file_txt += ".txt"
    
    with open(out_file_txt, "wb") as fh:
        fh.write(base64.decodebytes(encoded_base64))
        fh.close()

    #plt.title("Received Image")
    #plt.xlabel("X pixel scaling")
    #plt.ylabel("Y pixels scaling")
    #image = mpimg.imread("imageToSave.png")
    #plt.imshow(image)
    #plt.show()


    try:
        # Open the image file
        img = Image.open(out_file)
    
        # Display the image
        img.show()
    
    except Exception as e:
        print("Error:", e)


