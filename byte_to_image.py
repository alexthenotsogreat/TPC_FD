import struct
import base64
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

from PIL import Image


def bytes_to_image(binary_string):

    binary_bytes = int(binary_string, 2).to_bytes((len(binary_string) + 7) // 8, byteorder='big')

    
    encoded_base64 = base64.b64encode(binary_bytes)
    
    with open("imageToSave.jpg", "wb") as fh:
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
        img = Image.open("imageToSave.jpg")
    
        # Display the image
        img.show()
    
    except Exception as e:
        print("Error:", e)

